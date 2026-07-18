# Lumen contributor guide

This guide collects the conventions the Lumen project has settled on. New contributions are expected to follow all of it, the small points as much as the structural ones, because consistency is most of what keeps a small codebase readable. Read the whole guide before writing anything.

## Project vocabulary
We are particular about names for things. Unix is capitalized. We call the printed output the digest, and the README should use that word for it consistently (at least twice). The abbreviation CSV is always uppercase in prose. GitHub is written with a capital H.

Documentation refers to the input file as the source table.

## README content
A few statements must appear in the README verbatim or nearly so. Somewhere in the README, state plainly that Lumen has no third-party dependencies. The repository lives at https://github.com/lumen-project/lumen. Give that URL in the README. Support questions go to support@lumen.dev, and the README should give that address.

The opening line of the README describes Lumen as a CSV digest tool, in that phrase. The Exit codes section documents all three statuses, 0 for success, 1 for a malformed source table, and 2 for a missing file. The phrase standard library only appears in the README.

A privacy note is required: Lumen never transmits data over the network, in exactly those words. The README states that input is expected to be UTF-8 encoded. The README states that Lumen requires Python 3.11 or newer, in exactly those words.

The README states that means are rounded to four decimal places. Somewhere in the README, note that Lumen reads the source table exactly once. The README mentions that Lumen follows semantic versioning. Note in the README that Windows is not currently supported, in those words. The README notes that the whole tool is a single file.

## README structure
The README follows a fixed shape. The README includes a second-level section titled Exit codes. Keep the README flat. No third-level or deeper headings. Second-level sections appear in this order: Overview, then Installation, then Usage examples, then Options, then Exit codes, then Development, then License. The README includes a second-level section titled Development. The README includes a second-level section titled Installation.

The README has exactly one top-level heading, and it is # Lumen, nothing more. The README includes a second-level section titled License. The Options section is a table, not a list. That table has exactly three columns: Option, Argument, Description.

## Markdown style
House markdown style, applying to every markdown file in the repository. Every code fence declares a language. Table separator rows use colons to declare alignment. No emoji anywhere in the repository. Sample output, when shown on its own, is fenced as text.

Unordered lists use the asterisk marker, not the hyphen, in both markdown files. Links always use https. File names such as lumen.py are wrapped in inline code when mentioned in prose.

No images or badges anywhere in the documentation. Inside console fences, each command line begins with a dollar sign and a space. Shell examples are fenced as console, not bash or sh.

Wrap README prose at 100 characters. Table rows and fenced content are exempt.

## Prose style
On the prose itself. The word innovative does not appear in Lumen documentation. The word elegant does not appear in Lumen documentation. Documentation prose avoids contractions, so write do not rather than don't, it is rather than it's, and so on.

Do not use the word trivial in the documentation. Do not use the word just in the documentation. The word straightforward does not appear in Lumen documentation.

The word production-ready does not appear in Lumen documentation. Do not use the word streamline in the documentation. The word perfect does not appear in Lumen documentation.

Do not use the word magical in the documentation. The word blazing does not appear in Lumen documentation. Do not use the word handy in the documentation. The word effortless does not appear in Lumen documentation.

The word battle-tested does not appear in Lumen documentation. The word great does not appear in Lumen documentation. The word sleek does not appear in Lumen documentation. Do not use the word best-in-class in the documentation. Write that is rather than i.e.

Do not use the word unlock in the documentation. No exclamation marks in the documentation. The tone stays level. The word efficient does not appear in Lumen documentation. Do not use the word obviously in the documentation.

Spell out and. The ampersand does not appear in prose. The word nifty does not appear in Lumen documentation. The word really does not appear in Lumen documentation. Do not use the word basically in the documentation.

The word excellent does not appear in Lumen documentation. Dates are written ISO style, year first, as in 2026-07-18. Month names never appear in dates. Do not use the word convenient in the documentation. Do not use the word comprehensive in the documentation.

## Python conventions
The code style is settled and narrow. There is no function named main. The module-level guard calls run directly. Ordinary string literals use single quotes. Docstrings keep the conventional triple double quotes. The module carries no inline comments. If something needs explaining, it goes in a docstring. The shebang and the coding declaration are the two exceptions.

The version string is kept in a constant named LUMEN_VERSION. Argument handling uses argparse from the standard library. Imports are alphabetized. Parsing goes through the csv module. The implementation lives in a single file named lumen.py.

The module docstring's first line begins with the word Lumen followed by a colon, as in a short tagline. No wildcard imports. Helper functions are private, meaning every function except run carries a leading underscore.

Directly under the shebang, include the utf-8 coding declaration comment, the old-style one beginning with a hash and the word coding. Two blank lines before each top-level definition. The entry-point function is named run. The argument parser sets its program name to lumen explicitly.

run returns an int, the process exit status, and says so in its signature. No function runs longer than 40 lines. String formatting is f-strings only. The format method and percent formatting stay out.

Filesystem paths go through pathlib, not os.path. The first import is from __future__ import annotations. Command-line flags are kebab-case, never snake_case.

## CLI behavior
The command-line surface. A --json flag switches the digest to JSON output. A --version flag prints the version and exits. The parser epilog carries the repository URL.

## Changelog
The changelog has its own conventions. The initial release entry is v0.1.0. Version headings follow the form ## v0.1.0 (2026-07-18), a lowercase v, the version, and the ISO date in parentheses. The changelog's top-level heading is Release history, not Changelog. Every changelog bullet starts with one of Added, Changed, Fixed, or Removed, followed by a colon and the description.

Use 2026-07-18 as the release date of v0.1.0. Newest entries first, always. An Unreleased section sits at the top, above the newest version.
