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
export function args(options: Options): undefined;
export type EngineCallback = import('unified-engine').Callback;
export type EngineContext = import('unified-engine').Context;
export type Options = import('./parse-argv.js').Options;
export type State = import('./parse-argv.js').State;
