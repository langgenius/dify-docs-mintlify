/**
 * @import {Landmarks} from './index.js'
 */

import {constants, promises as fs} from 'node:fs'

/**
 * @param {Landmarks} landmarks
 *   Landmarks.
 * @param {ReadonlyArray<string>} references
 *   References.
 * @returns {Promise<undefined>}
 *   Nothing.
 */
export async function checkFiles(landmarks, references) {
  /** @type {Array<Promise<undefined>>} */
  const promises = []

  for (const filePath of references) {
    const marks = landmarks.get(filePath)

    if (!marks) {
      /** @type {Map<string, boolean>} */
      const map = new Map()

      landmarks.set(filePath, map)

      promises.push(
        fs.access(filePath, constants.F_OK).then(
          /**
           * @returns {undefined}
           */
          function () {
            map.set('', true)
          },
          /**
           * @param {NodeJS.ErrnoException} error
           * @returns {undefined}
           */
          function (error) {
            map.set('', error.code !== 'ENOENT' && error.code !== 'ENOTDIR')
          }
        )
      )
    }
  }

  await Promise.all(promises)
}
