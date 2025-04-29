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
export function parseArgv(flags: Array<string>, options: Options): State;
export type EngineOptions = import('unified-engine').Options;
export type Preset = import('unified-engine').Preset;
export type Field = import('./schema.js').Field;
export type PluggableMap = Exclude<Preset['plugins'], Array<any> | undefined>;
/**
 * Configuration specific to `unified-args`.
 */
export type ArgsFields = {
    /**
     *   Name of executable.
     */
    name: string;
    /**
     *   Description of executable.
     */
    description: string;
    /**
     *   Version (semver) of executable.
     */
    version: string;
};
/**
 * Configuration for `unified-args`.
 */
export type ArgsOptions = {
    /**
     *   Whether to show help info.
     */
    help: boolean;
    /**
     *   Help message.
     */
    helpMessage: string;
    /**
     *   Whether to show version info.
     */
    version: boolean;
    /**
     *   Whether to run in watch mode.
     */
    watch: boolean;
};
/**
 * Optional configuration for `unified-engine` that can be passed.
 */
export type EngineFieldsOptional = {
    cwd?: string | URL | undefined;
};
/**
 * Configuration for `unified-engine` that must be passed.
 */
export type EngineFieldsRequired = {
    processor: () => import("unified").Processor<any, any, any, any, any>;
    extensions: string[];
    rcName: string;
    packageField: string;
    ignoreName: string;
    pluginPrefix: string;
};
/**
 * Configuration.
 */
export type Options = ArgsFields & EngineFieldsOptional & EngineFieldsRequired;
/**
 * Parsed options for `args` itself and for the engine.
 */
export type State = {
    /**
     *   Configuration for `unified-engine`.
     */
    engine: EngineOptions;
    /**
     *   Configuration for `unified-args`.
     */
    args: ArgsOptions;
};
