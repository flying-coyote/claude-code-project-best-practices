# Lumen

Lumen is a CSV digest tool for the command-line workflow. Status: alpha.

## Overview

Lumen reads a source table and prints a compact digest: the number of rows, the number
of columns, and the minimum, maximum, and mean of the numeric fields. It is written in
pure Python, standard library only, and ships as a single file, `lumen.py`. There are
no third-party dependencies. The first row of the source table is treated as the header
row. Empty cells are ignored when computing statistics, and means are rounded to four
decimal places. Lumen reads the source table exactly once, comfortably handles files up
to one gigabyte, and expects input to be UTF-8 encoded. Lumen reads a file path argument
and does not read from standard input. Lumen never transmits data over the network.

## Installation

Requires Python 3.11 or newer. Tested on Linux and macOS. Windows is not currently supported.

```console
$ pip install lumen-csv
```

## Usage examples

Print the digest of a source table:

```console
$ lumen sales.csv
```

```text
rows: 120
columns: 4
amount: min=3.5 max=812.0 mean=97.4183
```

Emit the digest as JSON:

```console
$ lumen --json sales.csv
```

Use a semicolon as the delimiter:

```console
$ lumen -d ";" european.csv
```

## Options

| Option | Argument | Description |
|:-------|:---------|:------------|
| `-d`, `--delimiter` | character | Field delimiter, comma by default |
| `--json` | none | Emit the digest as JSON |
| `--version` | none | Print the version and exit |

## Exit codes

* 0 when the digest is printed
* 1 when the source table is malformed
* 2 when the source table is missing or unreadable

## Development

Lumen follows semantic versioning. Release notes live in `CHANGELOG.md`. Contributors
should open an issue before submitting a pull request. Support questions go to
support@lumen.dev. The repository lives at
https://github.com/lumen-project/lumen.

## License

Released under the MIT License. Copyright 2026 The Lumen Project.
