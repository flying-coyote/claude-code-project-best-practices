#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lumen: a CSV digest tool for the command line."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

LUMEN_VERSION = '0.1.0'


def _build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for the lumen command."""
    parser = argparse.ArgumentParser(
        prog='lumen',
        description='Compute the digest of a CSV source table.',
        epilog='Project home: https://github.com/lumen-project/lumen')
    parser.add_argument('source', help='path to the source table')
    parser.add_argument('-d', '--delimiter', default=',',
                        help='field delimiter, comma by default')
    parser.add_argument('--json', action='store_true',
                        help='emit the digest as JSON')
    parser.add_argument('--version', action='version',
                        version=f'lumen {LUMEN_VERSION}')
    return parser


def _numeric_summary(values: list[float]) -> dict[str, float]:
    """Return min, max, and mean for one numeric field."""
    total = sum(values)
    return {'min': min(values), 'max': max(values),
            'mean': round(total / len(values), 4)}


def _read_table(path: Path, delimiter: str) -> tuple[list[str], list[list[str]]]:
    """Read the source table once, returning the header row and body rows."""
    with path.open(newline='', encoding='utf-8') as handle:
        rows = list(csv.reader(handle, delimiter=delimiter))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def _collect_numeric(header: list[str], rows: list[list[str]]) -> dict[str, list[float]]:
    """Gather parseable numeric values per field, ignoring empty cells."""
    columns: dict[str, list[float]] = {name: [] for name in header}
    for row in rows:
        for name, cell in zip(header, row):
            text = cell.strip()
            if not text:
                continue
            try:
                columns[name].append(float(text))
            except ValueError:
                columns[name] = columns.get(name, [])
    return {name: vals for name, vals in columns.items() if vals}


def _render(digest: dict[str, object], as_json: bool) -> str:
    """Format the digest for printing."""
    if as_json:
        return json.dumps(digest, indent=2)
    lines = [f'rows: {digest["rows"]}', f'columns: {digest["columns"]}']
    fields = digest.get('numeric_fields', {})
    for name, stats in sorted(fields.items()):
        lines.append(f'{name}: min={stats["min"]} max={stats["max"]} mean={stats["mean"]}')
    return '\n'.join(lines)


def run(argv: list[str] | None = None) -> int:
    """Entry point: parse arguments, read the source table, print the digest."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    path = Path(args.source)
    if not path.is_file():
        print(f'lumen: no such source table: {path}', file=sys.stderr)
        return 2
    try:
        header, rows = _read_table(path, args.delimiter)
    except csv.Error as exc:
        print(f'lumen: malformed source table: {exc}', file=sys.stderr)
        return 1
    numeric = {name: _numeric_summary(vals)
               for name, vals in _collect_numeric(header, rows).items()}
    digest = {'rows': len(rows), 'columns': len(header),
              'numeric_fields': numeric}
    print(_render(digest, args.json))
    return 0


if __name__ == '__main__':
    sys.exit(run())
