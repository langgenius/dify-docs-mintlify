/**
 * @typedef Field
 *   Field.
 * @property {boolean} [common=false]
 *   Whether this is a commonly used field.
 * @property {boolean | string} [default='']
 *   Default (default: `''`).
 * @property {string} description
 *   Description of this field.
 * @property {string} long
 *   Long flag.
 * @property {string} [short]
 *   Short flag.
 * @property {boolean} [truelike=false]
 *   Whether this field is like `true`: the default is typically “on”, but that
 *   depends on a bit on what `unified-engine` does.
 * @property {'boolean' | 'string'} [type='string']
 *   Type of field (default: `'string'`).
 * @property {string} [value]
 *   Description of value for this field.
 */
/** @type {Array<Field>} */
export const schema: Array<Field>;
/**
 * Field.
 */
export type Field = {
    /**
     * Whether this is a commonly used field.
     */
    common?: boolean;
    /**
     * Default (default: `''`).
     */
    default?: boolean | string;
    /**
     *   Description of this field.
     */
    description: string;
    /**
     *   Long flag.
     */
    long: string;
    /**
     * Short flag.
     */
    short?: string;
    /**
     * Whether this field is like `true`: the default is typically “on”, but that
     * depends on a bit on what `unified-engine` does.
     */
    truelike?: boolean;
    /**
     * Type of field (default: `'string'`).
     */
    type?: 'boolean' | 'string';
    /**
     * Description of value for this field.
     */
    value?: string;
};
