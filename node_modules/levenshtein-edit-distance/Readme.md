# levenshtein-edit-distance [![Build Status](https://img.shields.io/travis/wooorm/levenshtein-edit-distance.svg?style=flat)](https://travis-ci.org/wooorm/levenshtein-edit-distance) [![Coverage Status](https://img.shields.io/coveralls/wooorm/levenshtein-edit-distance.svg?style=flat)](https://coveralls.io/r/wooorm/levenshtein-edit-distance?branch=master)

[Levenshtein edit distance](http://en.wikipedia.org/wiki/Levenshtein_distance) (by [Vladimir Levenshtein](http://en.wikipedia.org/wiki/Vladimir_Levenshtein)). No cruft. Real fast.

## Installation

[npm](https://docs.npmjs.com/cli/install):

```bash
$ npm install levenshtein-edit-distance
```

[Component.js](https://github.com/componentjs/component):

```bash
$ component install wooorm/levenshtein-edit-distance
```

[Bower](http://bower.io/#install-packages):

```bash
$ bower install levenshtein-edit-distance
```

[Duo](http://duojs.org/#getting-started):

```javascript
var levenshtein = require('wooorm/levenshtein-edit-distance');
```

## Usage

```javascript
var levenshtein = require('levenshtein-edit-distance');

levenshtein('levenshtein', 'levenshtein'); // 0
levenshtein('sitting', 'kitten'); // 3
levenshtein('gumbo', 'gambol'); // 2
levenshtein('saturday', 'sunday'); // 3

/* Case sensitive! */
levenshtein('DwAyNE', 'DUANE') !== levenshtein('dwayne', 'DuAnE'); // true

/* Insensitive: */
levenshtein('DwAyNE', 'DUANE', true) === levenshtein('dwayne', 'DuAnE', true); // true

/* Order insensitive */
levenshtein('aarrgh', 'aargh') === levenshtein('aargh', 'aarrgh'); // true
```

## CLI

Install:

```bash
$ npm install --global levenshtein-edit-distance
```

Use:

```text
Usage: levenshtein-edit-distance [options] word word

Levenshtein edit distance. No cruft. Real fast.

Options:

  -h, --help           output usage information
  -v, --version        output version number
  -i, --insensitive    ignore casing

Usage:

# output distance
$ levenshtein-edit-distance sitting kitten
# 3

# output distance from stdin
$ echo "saturday,sunday" | levenshtein-edit-distance
# 3
```

## Other Levenshtein libraries

- [sindresorhus/leven](https://github.com/sindresorhus/leven) — Supports a CLI;
- [hiddentao/fast-levenshtein](http://github.com/hiddentao/fast-levenshtein) — Supports async functionality;
- [NaturalNode/natural](http://github.com/NaturalNode/natural) — Supports settings weight of substitutions, insertions, and deletions.
- [gf3/Levenshtein](http://github.com/gf3/Levenshtein) — Supports inspecting the matrix.
- [levenshtein-component](https://www.npmjs.org/package/levenshtein-component);
- [chrisdew/levenshtein-deltas](https://github.com/chrisdew/levenshtein-deltas);

## Benchmark

On a MacBook Air, it runs about 1,909,000 op/s.

```text
              Levenshtein — to be fair, it lets you inspect a matrix
     113 op/s » op/s * 1,000

              natural — to be fair, it offers more options
     183 op/s » op/s * 1,000

              levenshtein-deltas
     237 op/s » op/s * 1,000

              levenshtein-component
     305 op/s » op/s * 1,000

              fast-levenshtein
   1,141 op/s » op/s * 1,000

              Leven — fast.
   2,076 op/s » op/s * 1,000

              levenshtein-edit-distance — this module
   1,909 op/s » op/s * 1,000
```

## License

[MIT](LICENSE) © [Titus Wormer](http://wooorm.com)
