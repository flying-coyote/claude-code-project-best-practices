# Lumen contributor guide

This guide collects the conventions the Lumen project has settled on. New contributions are expected to follow all of it, the small points as much as the structural ones, because consistency is most of what keeps a small codebase readable. Read the whole guide before writing anything.

## Project vocabulary
We are particular about names for things. GitHub is written with a capital H. The input CSV is referred to as the source table in all documentation. We call the printed output the digest, and the README should use that word for it consistently (at least twice).

## README content
A few statements must appear in the README verbatim or nearly so. The repository lives at https://github.com/lumen-project/lumen. Give that URL in the README. The README states that Lumen requires Python 3.11 or newer, in exactly those words. A privacy note is required: Lumen never transmits data over the network, in exactly those words. Somewhere in the README, state plainly that Lumen has no third-party dependencies.

The Exit codes section documents all three statuses, 0 for success, 1 for a malformed source table, and 2 for a missing file.

## README structure
The README follows a fixed shape. The README has exactly one top-level heading, and it is # Lumen, nothing more. The README includes a second-level section titled License. The Options section is a table, not a list. Second-level sections appear in this order: Overview, then Installation, then Usage examples, then Options, then Exit codes, then Development, then License. That table has exactly three columns: Option, Argument, Description.

## Markdown style
House markdown style, applying to every markdown file in the repository. Inside console fences, each command line begins with a dollar sign and a space. Shell examples are fenced as console, not bash or sh. No emoji anywhere in the repository.

Bullet lists are written with asterisks rather than hyphens, in the README and the changelog alike.

## Prose style
On the prose itself. Do not use the word battle-tested in the documentation. Documentation never uses an exclamation mark. The word nifty does not appear in Lumen documentation. The word straightforward does not appear in Lumen documentation. Do not use the word obviously in the documentation.

The word handy does not appear in Lumen documentation. The word production-ready does not appear in Lumen documentation. Do not use the word blazing in the documentation. Do not use the word unlock in the documentation.

Do not use the word excellent in the documentation. Documentation prose avoids contractions, so write do not rather than don't, it is rather than it's, and so on. The word comprehensive does not appear in Lumen documentation. Do not use the word convenient in the documentation.

Do not use the word elegant in the documentation.

## Python conventions
The code style is settled and narrow. No wildcard imports. String formatting is f-strings only. The format method and percent formatting stay out. The version string is kept in a constant named LUMEN_VERSION. The argument parser sets its program name to lumen explicitly. Ordinary string literals use single quotes. Docstrings keep the conventional triple double quotes.

Helper functions are private, meaning every function except run carries a leading underscore. The module docstring's first line begins with the word Lumen followed by a colon, as in a short tagline. The first import is from __future__ import annotations. Filesystem paths go through pathlib, not os.path.

There is no function named main. The module-level guard calls run directly. The entry-point function is named run. Directly under the shebang, include the utf-8 coding declaration comment, the old-style one beginning with a hash and the word coding.

## CLI behavior
The command-line surface. A --version flag prints the version and exits. The parser epilog carries the repository URL.

## Changelog
The changelog has its own conventions. Version headings follow the form ## v0.1.0 (2026-07-18), a lowercase v, the version, and the ISO date in parentheses. Newest entries first, always. An Unreleased section sits at the top, above the newest version. Every changelog bullet starts with one of Added, Changed, Fixed, or Removed, followed by a colon and the description. The changelog's top-level heading is Release history, not Changelog.
