/**
 * @import {Options} from 'remark-validate-links'
 * @import {VFile} from 'vfile'
 */

import {exec as execCallback} from 'node:child_process'
import path from 'node:path'
import {promisify} from 'node:util'

const exec = promisify(execCallback)

/**
 * @param {VFile} file
 *   File.
 * @param {Readonly<Options>} options
 *   Configuration.
 * @returns {Promise<[repo: string | false | undefined, root: string] | undefined>}
 *   Info.
 */
export async function findRepo(file, options) {
  const givenRepo = options.repository
  const givenRoot = options.root
  let base = file.cwd
  /** @type {string | false | undefined} */
  let repo
  /** @type {string | undefined} */
  let root

  if (file.path) {
    base = path.dirname(path.resolve(base, file.path))
  }

  if (givenRepo === null || givenRepo === undefined) {
    const result = await exec('git remote -v', {cwd: base})
    const match = result.stdout.match(/origin\t(.+?) \(fetch\)/)

    if (match) {
      repo = match[1]
    }

    if (!repo) {
      throw new Error(
        'Cannot find remote `origin` of local Git repo; pass `repository: false` if you are not using Git'
      )
    }
  } else {
    repo = givenRepo
  }

  if (givenRoot) {
    root = path.resolve(file.cwd, givenRoot)
  } else if (givenRepo === null || givenRepo === undefined) {
    const {stdout} = await exec('git rev-parse --show-cdup', {cwd: base})
    const out = stdout.trim()
    root = out ? path.join(base, out) : base
  } else {
    root = file.cwd
  }

  return [repo, root]
}
