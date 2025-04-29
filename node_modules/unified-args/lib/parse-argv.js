/**
 * @typedef {import('unified-engine').Options} EngineOptions
 * @typedef {import('unified-engine').Preset} Preset
 *
 * @typedef {import('./schema.js').Field} Field
 */

/**
 * @typedef {Exclude<Preset['plugins'], Array<any> | undefined>} PluggableMap
 */

/**
 * @typedef ArgsFields
 *   Configuration specific to `unified-args`.
 * @property {string} name
 *   Name of executable.
 * @property {string} description
 *   Description of executable.
 * @property {string} version
 *   Version (semver) of executable.
 *
 * @typedef ArgsOptions
 *   Configuration for `unified-args`.
 * @property {boolean} help
 *   Whether to show help info.
 * @property {string} helpMessage
 *   Help message.
 * @property {boolean} version
 *   Whether to show version info.
 * @property {boolean} watch
 *   Whether to run in watch mode.
 *
 * @typedef {{[Key in 'cwd']?: EngineOptions[Key]}} EngineFieldsOptional
 *   Optional configuration for `unified-engine` that can be passed.
 *
 * @typedef {(
 *   {
 *     [Key in 'extensions' | 'ignoreName' | 'packageField' | 'pluginPrefix' | 'processor' | 'rcName']:
 *       Exclude<EngineOptions[Key], null | undefined>
 *   }
 * )} EngineFieldsRequired
 *
 *   Configuration for `unified-engine` that must be passed.
 *
 * @typedef {ArgsFields & EngineFieldsOptional & EngineFieldsRequired} Options
 *   Configuration.
 *
 * @typedef State
 *   Parsed options for `args` itself and for the engine.
 * @property {EngineOptions} engine
 *   Configuration for `unified-engine`.
 * @property {ArgsOptions} args
 *   Configuration for `unified-args`.
 */

import assert from 'node:assert/strict'
import {parse as commaParse} from 'comma-separated-tokens'
import chalk from 'chalk'
import json5 from 'json5'
import minimist from 'minimist'
import stripAnsi from 'strip-ansi'
import table from 'text-table'
import {schema} from './schema.js'

const own = {}.hasOwnProperty

/**
 * Schema for `minimist`.
 *
 * @satisfies {minimist.Opts}
 */
const minischema = {
  /** @type {Record<string, string>} */
  alias: {},
  /** @type {Array<string>} */
  boolean: [],
  /** @type {Record<string, string | boolean | null>} */
  default: {},
  /** @type {Array<string>} */
  string: [],
  unknown: handleUnknownArgument
}

let index = -1
while (++index < schema.length) {
  const field = schema[index]

  // Has to be `null`, otherwise it fails.
  minischema.default[field.long] =
    field.default === undefined ? null : field.default

  if (field.type && field.type in minischema) {
    minischema[field.type].push(field.long)
  }

  if (field.short) {
    minischema.alias[field.short] = field.long
  }
}

/**
 * Parse CLI options.
 *
 * @param {Array<string>} flags
 *   Flags.
 * @param {Options} options
 *   Configuration (required).
 * @returns {State}
 *   Parsed options.
 */
// eslint-disable-next-line complexity
export function parseArgv(flags, options) {
  /** @type {Record<string, Array<string> | string | boolean | undefined>} */
  const config = minimist(flags, minischema)
  let index = -1

  // Fix defaults: minimist only understand `null`, not `undefined`, so we had to use `null`.
  // But we want `undefined`, so clean it here.
  /** @type {string} */
  let key

  for (key in config) {
    if (config[key] === null) {
      config[key] = undefined
    }
  }

  // Crash on passed but missing string values.
  while (++index < schema.length) {
    const field = schema[index]
    if (field.type === 'string' && config[field.long] === '') {
      throw new Error('Missing value: ' + inspect(field).join(' ').trimStart())
    }
  }

  // Make sure we parsed everything correctly.
  // Minimist guarantees that `''` is an array of strings.
  assert(Array.isArray(config._))
  // Minimist guarantees that our booleans are never strings.
  // Most have defaults, so they’re not `undefined`.
  assert(typeof config.color === 'boolean')
  assert(typeof config.config === 'boolean')
  assert(typeof config.frail === 'boolean')
  assert(typeof config.help === 'boolean')
  assert(typeof config.ignore === 'boolean')
  assert(typeof config.inspect === 'boolean')
  assert(typeof config.quiet === 'boolean')
  assert(typeof config.silent === 'boolean')
  assert(typeof config['silently-ignore'] === 'boolean')
  assert(typeof config.tree === 'boolean')
  assert(typeof config.verbose === 'boolean')
  assert(typeof config.version === 'boolean')
  assert(typeof config.watch === 'boolean')
  assert(config.stdout === undefined || typeof config.stdout === 'boolean')
  assert(
    config['tree-in'] === undefined || typeof config['tree-in'] === 'boolean'
  )
  assert(
    config['tree-out'] === undefined || typeof config['tree-out'] === 'boolean'
  )

  // The rest are strings, never booleans, but with minimist they could be
  // arrays.
  // `ignore-path-resolve-from` is an enum.
  const ignorePathResolveFrom = undefinedIfBoolean(
    lastIfArray(config['ignore-path-resolve-from'])
  )

  if (
    ignorePathResolveFrom !== undefined &&
    ignorePathResolveFrom !== 'cwd' &&
    ignorePathResolveFrom !== 'dir'
  ) {
    throw new Error(
      "Expected `'cwd'` or `'dir'` for `ignore-path-resolve-from`, not: `" +
        ignorePathResolveFrom +
        '`'
    )
  }

  const filePath = lastIfArray(undefinedIfBoolean(config['file-path']))
  const ignorePath = lastIfArray(undefinedIfBoolean(config['ignore-path']))
  const rcPath = lastIfArray(undefinedIfBoolean(config['rc-path']))
  const output = lastIfArray(config.output)

  const ext = parseIfString(joinIfArray(undefinedIfBoolean(config.ext))) || []
  const ignorePattern =
    parseIfString(joinIfArray(undefinedIfBoolean(config['ignore-pattern']))) ||
    []

  const setting = toArray(undefinedIfBoolean(config.setting)) || []
  /** @type {Record<string, unknown>} */
  const settings = {}
  index = -1
  while (++index < setting.length) {
    parseConfig(setting[index], settings)
  }

  const report = lastIfArray(undefinedIfBoolean(config.report))
  /** @type {string | undefined} */
  let reporter
  /** @type {Record<string, unknown>} */
  const reporterOptions = {}

  if (report) {
    const [key, value] = splitOptions(report)
    reporter = key
    if (value) parseConfig(value, reporterOptions)
  }

  const use = toArray(undefinedIfBoolean(config.use)) || []
  /** @type {PluggableMap} */
  const plugins = {}
  index = -1
  while (++index < use.length) {
    /** @type {Record<string, unknown>} */
    const options = {}
    const [key, value] = splitOptions(use[index])
    if (value) parseConfig(value, options)
    plugins[key] = options
  }

  return {
    args: {
      help: config.help,
      helpMessage: generateHelpMessage(options),
      version: config.version,
      watch: config.watch
    },
    engine: {
      color: config.color,
      cwd: options.cwd,
      detectConfig: config.config,
      detectIgnore: config.ignore,
      extensions: ext.length === 0 ? options.extensions : ext,
      filePath,
      files: config._,
      frail: config.frail,
      ignoreName: options.ignoreName,
      ignorePath,
      ignorePathResolveFrom,
      ignorePatterns: ignorePattern,
      inspect: config.inspect,
      output,
      out: config.stdout,
      packageField: options.packageField,
      pluginPrefix: options.pluginPrefix,
      plugins,
      processor: options.processor,
      quiet: config.quiet,
      rcName: options.rcName,
      rcPath,
      reporter,
      reporterOptions,
      settings,
      silent: config.silent,
      silentlyIgnore: config['silently-ignore'],
      tree: config.tree,
      treeIn: config['tree-in'],
      treeOut: config['tree-out'],
      verbose: config.verbose
    }
  }
}

/**
 * Generate a help message.
 *
 * @param {Options} options
 *   Configuration.
 * @returns {string}
 *   Help message.
 */
function generateHelpMessage(options) {
  const extension = options.extensions[0]
  const name = options.name

  return [
    inspectAll(schema),
    '',
    'Examples:',
    '',
    '  # Process `input.' + extension + '`',
    '  $ ' + name + ' input.' + extension + ' -o output.' + extension,
    '',
    '  # Pipe',
    '  $ ' + name + ' < input.' + extension + ' > output.' + extension,
    '',
    '  # Rewrite all applicable files',
    '  $ ' + name + ' . -o'
  ].join('\n')
}

/**
 * Parse configuration as JSON5.
 *
 * @param {string} value
 *   Settings.
 * @param {Record<string, unknown>} cache
 *   Map to add to.
 * @returns {undefined}
 *   Nothing.
 */
function parseConfig(value, cache) {
  /** @type {Record<string, unknown>} */
  let flags
  /** @type {string} */
  let flag

  try {
    flags = json5.parse('{' + value + '}')
  } catch (error) {
    const cause = /** @type {Error} */ (error)
    cause.message = cause.message.replace(/at(?= position)/, 'around')
    throw new Error('Cannot parse `' + value + '` as JSON', {cause})
  }

  for (flag in flags) {
    if (own.call(flags, flag)) {
      cache[flag] = flags[flag]
    }
  }
}

/**
 * Handle an unknown flag.
 *
 * @param {string} flag
 *   Flag.
 * @returns {true}
 *   Returns `true` for flags that are instead part of the files.
 * @throws {Error}
 *   For incorrect cases.
 */
function handleUnknownArgument(flag) {
  // Not a glob.
  if (flag.charAt(0) === '-') {
    // Long options, always unknown.
    if (flag.charAt(1) === '-') {
      throw new Error(
        'Unknown option `' + flag + '`, expected:\n' + inspectAll(schema)
      )
    }

    // Short options, can be grouped.
    const found = flag.slice(1).split('')
    const known = schema.filter(function (d) {
      return d.short
    })
    const knownShort = new Set(
      known.map(function (d) {
        return d.short
      })
    )
    let index = -1

    while (++index < found.length) {
      const key = found[index]
      if (!knownShort.has(key)) {
        throw new Error(
          'Unknown short option `-' + key + '`, expected:\n' + inspectAll(known)
        )
      }
    }
  }

  return true
}

/**
 * Inspect all `options`.
 *
 * @param {Array<Field>} fields
 *   Fields.
 * @returns {string}
 *   Table.
 */
function inspectAll(fields) {
  return table(
    fields.map(function (d) {
      return inspect(d)
    }),
    {
      stringLength(d) {
        return stripAnsi(d).length
      }
    }
  )
}

/**
 * Inspect one field.
 *
 * @param {Field} field
 *   Field.
 * @returns {Array<string>}
 *   Cells.
 */
function inspect(field) {
  let description = field.description
  let long = field.long

  if (field.default === true || field.truelike) {
    description += ' (on by default)'
    long = '[no-]' + long
  }

  long = '--' + long

  if (field.common) {
    long = chalk.bold(long)
  }

  return [
    '',
    field.short ? '-' + field.short : '',
    long + (field.value ? ' ' + field.value : ''),
    description
  ]
}

/**
 * @param {string} value
 *   Value.
 * @returns {[key: string, value?: string]}
 *   Tuple of a key and an optional value, delimited by `=`.
 */
function splitOptions(value) {
  const index = value.indexOf('=')
  return index === -1
    ? [value]
    : [value.slice(0, index), value.slice(index + 1)]
}

/**
 * @template {unknown} T
 *   Value.
 * @param {T} value
 *   Value.
 * @returns {T extends string ? Array<string> : T}
 *   Value, or an on commas parsed array of it if it’s a string.
 */
function parseIfString(value) {
  // @ts-expect-error: this is good.
  return typeof value === 'string' ? commaParse(value) : value
}

/**
 * @template {unknown} T
 *   Value.
 * @param {T} value
 *   Value.
 * @returns {T extends Array<string> ? string : T}
 *   Value, or the last item of it if it’s an array.
 */
function lastIfArray(value) {
  return Array.isArray(value) ? value[value.length - 1] : value
}

/**
 * @template {unknown} T
 *   Value.
 * @param {T} value
 *   Value.
 * @returns {T extends Array<string> ? string : T}
 *   Value, or an on commas joined string of it if it’s an array.
 */
function joinIfArray(value) {
  // @ts-expect-error: this is good.
  return Array.isArray(value) ? value.join(',') : value
}

/**
 * @template {unknown} T
 *   Value.
 * @param {T} value
 *   Value.
 * @returns {T extends boolean | number | string ? Array<T> : T}
 *   Value, or an array of it if it’s a non-nully primitive.
 */
function toArray(value) {
  // @ts-expect-error: this is good.
  return Array.isArray(value) || value === null || value === undefined
    ? value
    : [value]
}

/**
 * Ignore booleans.
 *
 * @template {unknown} T
 *   Value.
 * @param {T} value
 *   Value.
 * @returns {T extends boolean ? undefined : T}
 *   Value, or `undefined` if `value` is a boolean.
 */
function undefinedIfBoolean(value) {
  // @ts-expect-error: this is good.
  return typeof value === 'boolean' ? undefined : value
}
