/**
 * @typedef {import('unified-engine').Callback} EngineCallback
 * @typedef {import('unified-engine').Context} EngineContext
 *
 * @typedef {import('./parse-argv.js').Options} Options
 * @typedef {import('./parse-argv.js').State} State
 */

import process from 'node:process'
import stream from 'node:stream'
import {fileURLToPath} from 'node:url'
import chalk from 'chalk'
import chokidar from 'chokidar'
import {engine} from 'unified-engine'
import {parseArgv} from './parse-argv.js'

// Fake TTY stream.
const ttyStream = new stream.Readable()
// @ts-expect-error: TS doesn’t understand but that’s how Node streams work.
ttyStream.isTTY = true

// Handle uncaught errors, such as from unexpected async behaviour.
process.on('uncaughtException', fail)

/**
 * Start the CLI.
 *
 * > 👉 **Note**: this takes over the entire process.
 * > It parses `process.argv`, exits when its done, etc.
 *
 * @param {Options} options
 *   Configuration (required).
 * @returns {undefined}
 *   Nothing.
 */
export function args(options) {
  /** @type {State} */
  let state
  /** @type {chokidar.FSWatcher | undefined} */
  let watcher
  /** @type {URL | boolean | string | undefined} */
  let output

  try {
    state = parseArgv(process.argv.slice(2), options)
  } catch (error) {
    const exception = /** @type {Error} */ (error)
    return fail(exception)
  }

  if (state.args.help) {
    process.stdout.write(
      [
        'Usage: ' + options.name + ' [options] [path | glob ...]',
        '',
        '  ' + options.description,
        '',
        'Options:',
        '',
        state.args.helpMessage,
        ''
      ].join('\n'),
      noop
    )

    return
  }

  if (state.args.version) {
    process.stdout.write(options.version + '\n', noop)
    return
  }

  // Modify `state` for watching.
  if (state.args.watch) {
    output = state.engine.output

    // Do not read from stdin(4).
    state.engine.streamIn = ttyStream

    // Do not write to stdout(4).
    state.engine.out = false

    process.stderr.write(
      chalk.bold('Watching...') + ' (press CTRL+C to exit)\n',
      noop
    )

    // Prevent infinite loop if set to regeneration.
    if (output === true) {
      state.engine.output = false
      process.stderr.write(
        chalk.yellow('Note') + ': Ignoring `--output` until exit.\n',
        noop
      )
    }
  }

  // Initial run.
  engine(state.engine, done)

  /**
   * Handle complete run.
   *
   * @type {EngineCallback}
   */
  function done(error, code, context) {
    if (error) {
      clean()
      fail(error)
    } else {
      if (typeof code === 'number') process.exitCode = code

      if (state.args.watch && !watcher && context) {
        subscribe(context)
      }
    }
  }

  // Clean the watcher.
  function clean() {
    if (watcher) {
      process.removeListener('SIGINT', onsigint)
      watcher.close()
      watcher = undefined
    }
  }

  /**
   * Subscribe a chokidar watcher to all processed files.
   *
   * @param {EngineContext} context
   *   Context.
   * @returns {undefined}
   *   Nothing.
   */
  function subscribe(context) {
    /** @type {Array<string>} */
    const urls = context.fileSet.origins
    /* c8 ignore next 4 - this works, but it’s only used in `watch`, where we have one config for */
    const cwd =
      typeof state.engine.cwd === 'object'
        ? fileURLToPath(state.engine.cwd)
        : state.engine.cwd

    watcher = chokidar
      .watch(
        urls,
        // @ts-expect-error: chokidar types are wrong w/
        // `exactOptionalPropertyTypes`,
        // `cwd` can be `undefined`.
        {cwd, ignoreInitial: true}
      )
      .on('error', done)
      .on('change', function (filePath) {
        state.engine.files = [filePath]
        engine(state.engine, done)
      })

    process.on('SIGINT', onsigint)
  }

  /**
   * Handle a SIGINT.
   */
  function onsigint() {
    // Hide the `^C` in terminal.
    process.stderr.write('\n', noop)

    clean()

    // Do another process if `output` specified regeneration.
    if (output === true) {
      state.engine.output = output
      state.args.watch = false
      engine(state.engine, done)
    }
  }
}

/**
 * Print an error to `stderr`, optionally with stack.
 *
 * @param {Error} error
 *   Error to print.
 * @returns {undefined}
 *   Nothing.
 */
function fail(error) {
  process.exitCode = 1
  process.stderr.write(String(error.stack || error).trimEnd() + '\n', noop)
}

/**
 * Do nothing.
 *
 * @returns {undefined}
 *   Nothing.
 */
function noop() {}
