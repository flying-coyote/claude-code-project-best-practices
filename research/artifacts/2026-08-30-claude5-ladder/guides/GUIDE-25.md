# Lumen contributor guide

This guide collects the conventions the Lumen project has settled on. New contributions are expected to follow all of it, the small points as much as the structural ones, because consistency is most of what keeps a small codebase readable. Read the whole guide before writing anything.

## Project vocabulary
We are particular about names for things. The input CSV is referred to as the source table in all documentation. We call the printed output the digest, and the README should use that word for it consistently (at least twice).

## README content
A few statements must appear in the README verbatim or nearly so. A privacy note is required: Lumen never transmits data over the network, in exactly those words. The README states that Lumen requires Python 3.11 or newer, in exactly those words. The repository lives at https://github.com/lumen-project/lumen. Give that URL in the README.

## README structure
The README follows a fixed shape. The README has exactly one top-level heading, and it is # Lumen, nothing more. That table has exactly three columns: Option, Argument, Description. Second-level sections appear in this order: Overview, then Installation, then Usage examples, then Options, then Exit codes, then Development, then License.

## Markdown style
House markdown style, applying to every markdown file in the repository. Fence shell examples with the console language tag rather than bash. Inside console fences, each command line begins with a dollar sign and a space. Bullet lists are written with asterisks rather than hyphens, in the README and the changelog alike.

## Prose style
On the prose itself. Documentation prose avoids contractions, so write do not rather than don't, it is rather than it's, and so on.

## Python conventions
The code style is settled and narrow. Directly under the shebang, include the utf-8 coding declaration comment, the old-style one beginning with a hash and the word coding. The module docstring's first line begins with the word Lumen followed by a colon, as in a short tagline. The first import is from __future__ import annotations.

Helper functions are private, meaning every function except run carries a leading underscore. There is no function named main. The module-level guard calls run directly. The version string is kept in a constant named LUMEN_VERSION. The entry-point function is named run. Ordinary string literals use single quotes. Docstrings keep the conventional triple double quotes.

## CLI behavior
The command-line surface. The parser epilog carries the repository URL.

## Changelog
The changelog has its own conventions. Every changelog bullet starts with one of Added, Changed, Fixed, or Removed, followed by a colon and the description. Version headings follow the form ## v0.1.0 (2026-07-18), a lowercase v, the version, and the ISO date in parentheses. The changelog's top-level heading is Release history, not Changelog. An Unreleased section sits at the top, above the newest version.
