/**
 * @import {Hosts} from 'hosted-git-info'
 * @import {} from 'mdast-util-to-hast'
 * @import {Nodes, Resource, Root} from 'mdast'
 * @import {FileSet} from 'unified-engine'
 */

/**
 * @typedef {Map<string, Map<string, boolean>>} Landmarks
 *   Landmarks.
 */

/**
 * @typedef Options
 *   Configuration.
 * @property {string | false | null | undefined} [repository]
 *   URL to hosted Git (default: detected from Git remote);
 *   if you’re not in a Git repository, you must pass `false`;
 *   if the repository resolves to something npm understands as a Git host such
 *   as GitHub, GitLab, or Bitbucket, full URLs to that host (say,
 *   `https://github.com/remarkjs/remark-validate-links/readme.md#install`) are
 *   checked.
 * @property {string | null | undefined} [root]
 *   Path to Git root folder (default: local Git folder);
 *   if both `root` and `repository` are nullish, the Git root is detected;
 *   if `root` is not given but `repository` is, `file.cwd` is used.
 * @property {ReadonlyArray<RegExp | string> | null | undefined} [skipPathPatterns]
 *   List of patterns for *paths* that should be skipped;
 *   each absolute local path + hash will be tested against each pattern and
 *   will be ignored if `new RegExp(pattern).test(value) === true`;
 *   example value are then `/Users/tilde/path/to/repo/readme.md#some-heading`.
 * @property {Readonly<UrlConfig> | null | undefined} [urlConfig]
 *   Config on how hosted Git works (default: detected from repo);
 *   `github.com`, `gitlab.com`, or `bitbucket.org` work automatically;
 *   otherwise, pass `urlConfig` manually.
 */

/**
 * @callback Propose
 * @param {string} value
 * @param {ReadonlyArray<string>} dictionary
 * @param {Readonly<ProposeOptions> | null | undefined} [options]
 * @returns {string | undefined}
 */

/**
 * @typedef ProposeOptions
 *   Configuration for `propose`.
 * @property {number| null | undefined} [threshold]
 *   Threshold.
 */

/**
 * @typedef Reference
 *   Reference to something.
 * @property {string} filePath
 *   Path to file.
 * @property {string | undefined} hash
 *   Hash.
 */

/**
 * @typedef ReferenceInfo
 *   Info on a reference.
 * @property {VFile} file
 *   File.
 * @property {Readonly<Reference>} reference
 *   Reference.
 * @property {ReadonlyArray<Readonly<Resources>>} nodes
 *   Nodes that reference it.
 */

/**
 * @typedef {Extract<Nodes, Resource>} Resources
 *   Resources.
 */

/**
 * @typedef State
 *   Info passed around.
 * @property {string} base
 *   Folder of file.
 * @property {string} path
 *   Path to file.
 * @property {string | null | undefined} root
 *   Path to Git folder.
 * @property {ReadonlyArray<RegExp>} skipPathPatterns
 *   List of patterns for paths that should be skipped.
 * @property {Readonly<UrlConfig>} urlConfig
 *   Configuration.
 */

/**
 * @typedef UrlConfig
 *   Hosted Git info.
 *
 *   ###### Notes
 *
 *   For this repository (`remarkjs/remark-validate-links` on GitHub)
 *   `urlConfig` looks as follows:
 *
 *   ```js
 *   {
 *     // Domain of URLs:
 *     hostname: 'github.com',
 *     // Path prefix before files:
 *     prefix: '/remarkjs/remark-validate-links/blob/',
 *     // Prefix of headings:
 *     headingPrefix: '#',
 *     // Hash to top of markdown documents:
 *     topAnchor: '#readme',
 *     // Whether lines in files can be linked:
 *     lines: true
 *   }
 *   ```
 *
 *   If this project were hosted on Bitbucket, it would be:
 *
 *   ```js
 *   {
 *     hostname: 'bitbucket.org',
 *     prefix: '/remarkjs/remark-validate-links/src/',
 *     headingPrefix: '#markdown-header-',
 *     lines: false
 *   }
 *   ```
 * @property {string | null | undefined} [headingPrefix]
 *   Prefix of headings (example: `'#'`, `'#markdown-header-'`).
 * @property {string | null | undefined} [hostname]
 *   Domain of URLs (example: `'github.com'`, `'bitbucket.org'`).
 * @property {boolean | null | undefined} [resolveAbsolutePathsInRepo]
 *   Whether absolute paths (`/x/y/z.md`) resolve relative to a repo.
 * @property {boolean | null | undefined} [lines]
 *   Whether lines in files can be linked.
 * @property {string | null | undefined} [prefix]
 *   Path prefix before files (example:
 *   `'/remarkjs/remark-validate-links/blob/'`,
 *   `'/remarkjs/remark-validate-links/src/'`).
 * @property {string | null | undefined} [topAnchor]
 *   Hash to top of readme (example: `#readme`).
 */

import fs from 'node:fs/promises'
import path from 'node:path'
import GithubSlugger from 'github-slugger'
import hostedGitInfo from 'hosted-git-info'
import {toString} from 'mdast-util-to-string'
// @ts-expect-error: untyped.
import propose_ from 'propose'
import {visit} from 'unist-util-visit'
import {VFile} from 'vfile'
import {constants} from './constants.js'
import {checkFiles} from '#check-files'
import {findRepo} from '#find-repo'

const propose = /** @type {Propose} */ (propose_)

cliCompleter.pluginId = constants.sourceId

/** @type {Readonly<Partial<Record<Hosts, string>>>} */
const viewPaths = {bitbucket: 'src', github: 'blob', gitlab: 'blob'}
/** @type {Readonly<Partial<Record<Hosts, string>>>} */
const headingPrefixes = {
  bitbucket: '#markdown-header-',
  github: '#',
  gitlab: '#'
}
/** @type {Readonly<Partial<Record<Hosts, string>>>} */
const topAnchors = {github: '#readme', gitlab: '#readme'}
/** @type {Readonly<Partial<Record<Hosts, boolean>>>} */
const lineLinks = {github: true, gitlab: true}

const slugger = new GithubSlugger()

const slash = '/'
const numberSign = '#'
const questionMark = '?'
const https = 'https:'
const http = 'http:'
const slashes = '//'
const lineExpression = /^#l\d/i

// List from: https://github.com/github/markup#markups
const readmeExtensions = new Set(['.markdown', '.mdown', '.md', '.mkdn'])
const readmeBasename = /^readme$/i

/**
 * Check that markdown links and images point to existing local files and
 * headings in a Git repo.
 *
 * > ⚠️ **Important**: The API in Node.js checks links to headings and files
 * > but does not check whether headings in other files exist.
 * > The API in browsers only checks links to headings in the same file.
 * > The CLI can check everything.
 *
 * @param {Readonly<Options> | null | undefined} [options]
 *   Configuration (optional).
 * @param {FileSet | null | undefined} [fileSet]
 *   File set (optional).
 * @returns
 *   Transform.
 */
export default function remarkValidateLinks(options, fileSet) {
  const settings = options || {}
  const skipPathPatterns = settings.skipPathPatterns
    ? settings.skipPathPatterns.map(function (d) {
        return typeof d === 'string' ? new RegExp(d) : d
      })
    : []

  // Attach a `completer`.
  if (fileSet) {
    fileSet.use(cliCompleter)
  }

  /**
   * Transform.
   *
   * @param {Root} tree
   *   Tree.
   * @param {VFile} file
   *   File.
   * @returns {Promise<void>}
   *   Nothing.
   *
   *   Note: `void` needed because `unified` doesn’t seem to accept `undefined`.
   */
  return async function (tree, file) {
    /* c8 ignore next -- this yields `undefined` in browsers. */
    const [repo, root] = (await findRepo(file, settings)) || []
    let urlConfig = settings.urlConfig

    if (!urlConfig) {
      /** @type {UrlConfig} */
      const config = {
        headingPrefix: '#',
        hostname: undefined,
        lines: false,
        prefix: '',
        topAnchor: undefined
      }

      if (repo) {
        const info = hostedGitInfo.fromUrl(repo)

        if (info && info.type !== 'gist') {
          if (info.type in viewPaths) {
            config.prefix = '/' + info.path() + '/' + viewPaths[info.type] + '/'
          }

          if (info.type in headingPrefixes) {
            config.headingPrefix = headingPrefixes[info.type]
          }

          if (info.type in lineLinks) {
            config.lines = lineLinks[info.type]
          }

          if (info.type === 'github') {
            config.resolveAbsolutePathsInRepo = true
          }

          if (info.type in topAnchors) {
            config.topAnchor = topAnchors[info.type]
          }

          config.hostname = info.domain
        }
      }

      urlConfig = config
    }

    const absolute = file.path ? path.resolve(file.cwd, file.path) : ''
    const space = file.data
    /** @type {Map<string, Map<string, Array<Resources>>>} */
    const references = new Map()
    /** @type {Landmarks} */
    const landmarks = new Map()
    /** @type {State} */
    const state = {
      base: absolute ? path.dirname(absolute) : file.cwd,
      path: absolute,
      root,
      skipPathPatterns,
      urlConfig
    }
    /** @type {Set<string>} */
    const statted = new Set()
    /** @type {Set<string>} */
    const added = new Set()
    /** @type {Array<Promise<void>>} */
    const promises = []

    space[constants.referenceId] = references
    space[constants.landmarkId] = landmarks

    addLandmarks(absolute, '')

    slugger.reset()

    visit(tree, function (node) {
      const data = node.data || {}
      const hProperties = data.hProperties || {}
      // @ts-expect-error: accept a `data.id`, which is not standard mdast, but
      // is here for historical reasons.
      const dataId = /** @type {unknown} */ (data.id)
      let id = String(hProperties.name || hProperties.id || dataId || '')

      if (!id && node.type === 'heading') {
        id = slugger.slug(
          toString(node, {includeHtml: false, includeImageAlt: false})
        )
      }

      if (id) {
        addLandmarks(absolute, id)
      }

      if ('url' in node && node.url) {
        const info = urlToPath(node.url, state, node.type)

        if (info) {
          const fp = info.filePath
          const hash = info.hash
          const together = fp + (hash ? '#' + hash : '')

          if (
            state.skipPathPatterns.some(function (skipPattern) {
              return skipPattern.test(together)
            })
          ) {
            return
          }

          addReference(fp, '', node)

          if (hash) {
            if (fileSet || fp === absolute) {
              addReference(fp, hash, node)
            }

            if (fileSet && fp && !statted.has(fp)) {
              promises.push(addFile(fp))
            }
          }
        }
      }
    })

    await Promise.all(promises)

    if (!fileSet) {
      await checkAll([file])
    }

    /**
     * @param {string} filePath
     *   Absolute path to file.
     * @param {string} hash
     *   Hash.
     * @returns {undefined}
     *   Nothing.
     */
    function addLandmarks(filePath, hash) {
      addLandmark(filePath, hash)

      // Note: this may add marks too many anchors as defined.
      // For example, if there is both a `readme.md` and a `readme.markdown` in a
      // folder, both their landmarks will be defined for their parent folder.
      // To solve this, we could check whichever sorts first, and ignore the
      // others.
      // This is an unlikely scenario though, and adds a lot of complexity, so
      // we’re ignoring it.
      if (readme(filePath)) {
        addLandmark(path.dirname(filePath), hash)
      }
    }

    /**
     * @param {string} filePath
     *   Absolute path to file.
     * @param {string} hash
     *   Hash.
     * @returns {undefined}
     *   Nothing.
     */
    function addLandmark(filePath, hash) {
      let marks = landmarks.get(filePath)

      if (!marks) {
        marks = new Map()
        landmarks.set(filePath, marks)
      }

      marks.set(hash, true)
    }

    /**
     * @param {string} filePath
     *   Absolute path to file.
     * @param {string} hash
     *   Hash.
     * @param {Resources} node
     *   Node.
     * @returns {undefined}
     *   Nothing.
     */
    function addReference(filePath, hash, node) {
      let referenceMap = references.get(filePath)

      if (!referenceMap) {
        referenceMap = new Map()
        references.set(filePath, referenceMap)
      }

      let hashes = referenceMap.get(hash)

      if (!hashes) {
        hashes = []
        referenceMap.set(hash, hashes)
      }

      hashes.push(node)
    }

    /**
     * @param {string} filePath
     *   Absolute path to file.
     * @returns {Promise<undefined>}
     *   Nothing.
     */
    async function addFile(filePath) {
      statted.add(filePath)

      try {
        const stats = await fs.stat(filePath)

        if (stats.isDirectory()) {
          /** @type {Array<string>} */
          let entries = []

          try {
            entries = await fs.readdir(filePath)
            /* c8 ignore next -- seems to never happen after a stat. */
          } catch {}

          const files = entries.sort()
          /** @type {string | undefined} */
          let file

          for (const entry of files) {
            if (readme(entry)) {
              file = entry
              break
            }
          }

          // To do: test for no readme in folder.

          // Else, there’s no readme that we can parse, so add the folder.
          if (file) {
            filePath = path.join(filePath, file)
            statted.add(filePath)
          }
        }
      } catch {}

      if (fileSet && !added.has(filePath)) {
        added.add(filePath)
        fileSet.add(
          new VFile({cwd: file.cwd, path: path.relative(file.cwd, filePath)})
        )
      }
    }
  }
}

/**
 * Completer for the CLI (multiple files, supports parsing more files).
 *
 * @param {FileSet} set
 * @returns {Promise<undefined>}
 */
async function cliCompleter(set) {
  await checkAll(set.valueOf())
}

/**
 * Completer for the CLI (multiple files, supports parsing more files).
 *
 * @param {ReadonlyArray<VFile>} files
 *   Files.
 * @returns {Promise<undefined>}
 *   Nothing.
 */
async function checkAll(files) {
  // Merge landmarks.
  /** @type {Landmarks} */
  const landmarks = new Map()

  for (const file of files) {
    const fileLandmarks = /** @type {Landmarks | undefined} */ (
      file.data[constants.landmarkId]
    )

    if (fileLandmarks) {
      for (const [filePath, marks] of fileLandmarks) {
        landmarks.set(filePath, new Map(marks))
      }
    }
  }

  // Merge references.
  /** @type {Map<string, Map<string, Array<ReferenceInfo>>>} */
  const references = new Map()

  for (const file of files) {
    const fileReferences =
      /** @type {Map<string, Map<string, Array<Resources>>> | undefined} */ (
        file.data[constants.referenceId]
      )

    if (!fileReferences) {
      continue
    }

    for (const [reference, internal] of fileReferences) {
      let all = references.get(reference)
      if (!all) {
        all = new Map()
        references.set(reference, all)
      }

      for (const [hash, nodes] of internal) {
        let list = all.get(hash)

        if (!list) {
          list = []
          all.set(hash, list)
        }

        list.push({
          file,
          nodes,
          reference: {filePath: reference, hash}
        })
      }
    }
  }

  // Access files to see whether they exist.
  await checkFiles(landmarks, [...references.keys()])

  /** @type {Array<ReferenceInfo>} */
  const missing = []

  for (const [key, referenceMap] of references) {
    const lands = landmarks.get(key)

    for (const [hash, infos] of referenceMap) {
      /* c8 ignore next -- `else` can only happen in browser. */
      const exists = lands ? lands.get(hash) : false

      if (!exists) {
        missing.push(...infos)
      }
    }
  }

  for (const reference of missing) {
    warn(landmarks, reference)
  }
}

/**
 * @param {Landmarks} landmarks
 *   Landmarks.
 * @param {ReferenceInfo} reference
 *   Reference.
 * @returns {undefined}
 *   Nothing.
 */
function warn(landmarks, reference) {
  const absolute = reference.file.path
    ? path.resolve(reference.file.cwd, reference.file.path)
    : ''
  const base = absolute ? path.dirname(absolute) : undefined
  const filePath = base
    ? path.relative(base, reference.reference.filePath)
    : reference.reference.filePath
  const hash = reference.reference.hash
  /** @type {Array<string>} */
  const dictionary = []
  /** @type {string} */
  let reason
  /** @type {string} */
  let ruleId

  if (hash) {
    reason = 'Cannot find heading for `#' + hash + '`'
    ruleId = constants.headingRuleId

    if (base && path.join(base, filePath) !== absolute) {
      reason += ' in `' + filePath + '`'
      ruleId = constants.headingInFileRuleId
    }
  } else {
    reason = 'Cannot find file `' + filePath + '`'
    ruleId = constants.fileRuleId
  }

  const origin = [constants.sourceId, ruleId].join(':')
  for (const [landmark, marks] of landmarks) {
    // Only suggest if file exists.
    if (!marks || !marks.get('')) {
      continue
    }

    const relativeLandmark = base ? path.relative(base, landmark) : landmark

    if (!hash) {
      dictionary.push(relativeLandmark)
      continue
    }

    if (relativeLandmark !== filePath) {
      continue
    }

    for (const [subhash] of marks) {
      if (subhash !== '') {
        dictionary.push(subhash)
      }
    }
  }

  const suggestion = propose(hash || filePath, dictionary, {
    threshold: 0.7
  })

  if (suggestion) {
    reason += '; did you mean `' + suggestion + '`'
  }

  for (const node of reference.nodes) {
    const message = reference.file.message(reason, {
      place: node.position,
      source: origin,
      ruleId
    })
    message.url = 'https://github.com/remarkjs/remark-validate-links#readme'
  }
}

/**
 * @param {string} value
 *   URL.
 * @param {State} state
 *   State.
 * @param {Resources['type']} type
 *   Type of node (`'link'` or `'image'`).
 * @returns {Reference | undefined}
 *   Reference.
 */
// eslint-disable-next-line complexity
function urlToPath(value, state, type) {
  // Absolute paths: `/folder/example.md`.
  if (value.charAt(0) === slash) {
    if (!state.urlConfig.hostname) {
      return
    }

    const pathname =
      state.urlConfig.resolveAbsolutePathsInRepo && state.urlConfig.prefix
        ? state.urlConfig.prefix + 'main' + value
        : value

    // Create a URL.
    value = https + slashes + state.urlConfig.hostname + pathname
  }

  /** @type {URL | undefined} */
  let url

  try {
    url = new URL(value)
  } catch {}

  // URLs: `https://github.com/wooorm/test/blob/main/folder/example.md`.
  if (url && state.root) {
    // Exit if we don’t have hosted Git info or this is not a URL to the repo.
    if (
      !state.urlConfig.prefix ||
      !state.urlConfig.hostname ||
      (url.protocol !== https && url.protocol !== http) ||
      url.hostname !== state.urlConfig.hostname ||
      url.pathname.slice(0, state.urlConfig.prefix.length) !==
        state.urlConfig.prefix
    ) {
      return
    }

    value = url.pathname.slice(state.urlConfig.prefix.length)

    // Things get interesting here: branches: `foo/bar/baz` could be `baz` on
    // the `foo/bar` branch, or, `baz` in the `bar` folder on the `foo`
    // branch.
    // Currently, we’re ignoring this and just not supporting branches.
    value = value.split(slash).slice(1).join(slash)

    return normalize(
      path.resolve(state.root, value + (type === 'image' ? '' : url.hash)),
      state
    )
  }

  // Remove the search: `?foo=bar`.
  // But don’t remove stuff if it’s in the hash: `readme.md#heading?`.
  let numberSignIndex = value.indexOf(numberSign)
  const questionMarkIndex = value.indexOf(questionMark)

  if (
    questionMarkIndex !== -1 &&
    (numberSignIndex === -1 || numberSignIndex > questionMarkIndex)
  ) {
    value =
      value.slice(0, questionMarkIndex) +
      (numberSignIndex === -1 ? '' : value.slice(numberSignIndex))
    numberSignIndex = value.indexOf(numberSign)
  }

  // Ignore "headings" in image links: `image.png#metadata`
  if (numberSignIndex !== -1 && type === 'image') {
    value = value.slice(0, numberSignIndex)
  }

  // Local: `#heading`.
  if (value.charAt(0) === numberSign) {
    value = state.path ? state.path + value : value
  }
  // Anything else, such as `readme.md`.
  else {
    value = state.path ? path.resolve(state.base, value) : ''
  }

  return normalize(value, state)
}

/**
 * @param {string} url
 *   URL.
 * @param {State} state
 *   State.
 * @returns {Reference}
 *   Reference.
 */
function normalize(url, state) {
  const numberSignIndex = url.indexOf(numberSign)
  const lines = state.urlConfig.lines
  const prefix = state.urlConfig.headingPrefix
  const topAnchor = state.urlConfig.topAnchor
  /** @type {string} */
  let filePath
  /** @type {string | undefined} */
  let hash

  if (numberSignIndex === -1) {
    filePath = url
  } else {
    filePath = url.slice(0, numberSignIndex)
    hash = url.slice(numberSignIndex).toLowerCase()

    // Ignore the hash if it references the top anchor of the environment
    if (topAnchor && hash === topAnchor) {
      hash = undefined
    }
    // Ignore the hash if it references lines in a file or doesn’t start
    // with a heading prefix.
    else if (
      prefix &&
      ((lines && lineExpression.test(hash)) ||
        hash.slice(0, prefix.length) !== prefix)
    ) {
      hash = undefined
    }
    // Use the hash if it starts with a heading prefix.
    else if (prefix) {
      hash = hash.slice(prefix.length)
    }
  }

  return {filePath: decodeURIComponent(filePath), hash}
}

/**
 * @param {string} filePath
 *   Absolute path to file.
 * @returns {boolean}
 *   Whether `filePath` is a readme.
 */
function readme(filePath) {
  const extension = path.extname(filePath)

  return (
    readmeExtensions.has(extension) &&
    readmeBasename.test(path.basename(filePath, extension))
  )
}
