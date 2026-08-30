# Lumen contributor guide

This guide collects the conventions the Lumen project has settled on. New contributions are expected to follow all of it, the small points as much as the structural ones, because consistency is most of what keeps a small codebase readable. Read the whole guide before writing anything.

## Project vocabulary
We are particular about names for things. The file is the README, in capitals, when mentioned in prose. The tool's printed report is called the digest. Use that term in the README, at least twice. Hyphenate command-line when it modifies a noun, as in command-line tool.

Write the project name as Lumen in prose. The lowercase form belongs only in code spans that show the command. Apple's operating system is written macOS, never MacOS and never Mac OS. Write file path as two words, never filepath. GitHub is written with a capital H.

JSON is likewise always uppercase in prose. Unix is capitalized. Columns that hold numbers are called numeric fields in prose, and the README should use that phrase.

The abbreviation CSV is always uppercase in prose. Python is capitalized in prose, every time. The input CSV is referred to as the source table in all documentation.

## README content
A few statements must appear in the README verbatim or nearly so. The Exit codes section documents all three statuses, 0 for success, 1 for a malformed source table, and 2 for a missing file. Somewhere in the README, state plainly that Lumen has no third-party dependencies. State that empty cells are ignored when computing statistics, in those words. The README points readers to CHANGELOG.md for release notes. The README explains that the first row of the source table is treated as the header row.

The README mentions that Lumen comfortably handles files up to one gigabyte. A privacy note is required: Lumen never transmits data over the network, in exactly those words. Somewhere in the README, note that Lumen reads the source table exactly once. Describe Lumen as written in pure Python.

The README notes that the whole tool is a single file. The README states that input is expected to be UTF-8 encoded. The README states that Lumen requires Python 3.11 or newer, in exactly those words. The README carries the sentence Tested on Linux and macOS. Support questions go to support@lumen.dev, and the README should give that address.

Note in the README that Windows is not currently supported, in those words. The copyright line reads Copyright 2026 The Lumen Project. The opening line of the README describes Lumen as a CSV digest tool, in that phrase.

The Development section asks contributors to open an issue before submitting a pull request. Installation is via pip install lumen-csv, and the README shows that exact command. The README states that means are rounded to four decimal places. The phrase standard library only appears in the README.

Note in the README that Lumen reads a file path argument and does not read from standard input. Lumen is released under the MIT License, and the README must say so. Near the top of the README include the line Status: alpha. The README mentions that Lumen follows semantic versioning.

The repository lives at https://github.com/lumen-project/lumen. Give that URL in the README.

## README structure
The README follows a fixed shape. The README includes a second-level section titled Development. That heading is the very first line of the file. The README includes a second-level section titled Overview.

The README has exactly one top-level heading, and it is # Lumen, nothing more. Keep the README flat. No third-level or deeper headings. The README includes a second-level section titled Usage examples. The README includes a second-level section titled Options.

That table has exactly three columns: Option, Argument, Description. Usage examples shows at least three distinct invocations of lumen. The README includes a second-level section titled Installation. The README includes a second-level section titled Exit codes. The README includes a second-level section titled License.

The Options section is a table, not a list. Second-level sections appear in this order: Overview, then Installation, then Usage examples, then Options, then Exit codes, then Development, then License. The License section closes the file. Nothing comes after it except the license text itself.

## Markdown style
House markdown style, applying to every markdown file in the repository. No horizontal rules in the markdown files. Links always use https. Sample output, when shown on its own, is fenced as text.

If you write an ordered list, use the 1) numbering style rather than 1. followed by a period. File names such as lumen.py are wrapped in inline code when mentioned in prose. Table separator rows use colons to declare alignment. No emoji anywhere in the repository. Inside console fences, each command line begins with a dollar sign and a space.

Every code fence declares a language. Command-line flags such as --json are wrapped in inline code when they appear in prose. Wrap README prose at 100 characters. Table rows and fenced content are exempt. No raw HTML in the markdown files. No images or badges anywhere in the documentation.

Fence shell examples with the console language tag rather than bash. Unordered lists use the asterisk marker, not the hyphen, in both markdown files.

## Prose style
On the prose itself. The word amazing does not appear in Lumen documentation. Do not use the word supercharge in the documentation. Do not use the word great in the documentation. The word easily does not appear in Lumen documentation.

The word extremely does not appear in Lumen documentation. The word obviously does not appear in Lumen documentation. The word quickly does not appear in Lumen documentation. Write that is rather than i.e. Do not use the word superb in the documentation.

The word world-class does not appear in Lumen documentation. Do not use the word comprehensive in the documentation. Do not use the word quick in the documentation.

Do not use the word simply in the documentation. Do not use the word lightweight in the documentation. The word sleek does not appear in Lumen documentation. Do not use the word painless in the documentation.

The word unleash does not appear in Lumen documentation. Write for example rather than e.g. Do not use the word delightful in the documentation. Dates are written ISO style, year first, as in 2026-07-18. Month names never appear in dates. The word awesome does not appear in Lumen documentation.

The word innovative does not appear in Lumen documentation. Do not use the word perfect in the documentation. Documentation prose avoids contractions, so write do not rather than don't, it is rather than it's, and so on. Do not use the word powerful in the documentation. The word intuitive does not appear in Lumen documentation.

Do not use the word excellent in the documentation. Do not use the word convenient in the documentation. Do not use the word utilize in the documentation. The word user-friendly does not appear in Lumen documentation. Do not use the word leverage in the documentation.

No rhetorical questions in the README, which in practice means no question marks. Documentation never uses an exclamation mark. Do not use the word handy in the documentation. The word just does not appear in Lumen documentation.

The word efficient does not appear in Lumen documentation. The word magical does not appear in Lumen documentation. Do not use the word plug-and-play in the documentation. Do not use the word streamlined in the documentation.

Do not use the word very in the documentation. Do not use the word incredibly in the documentation. The word best-in-class does not appear in Lumen documentation. Do not use the word empower in the documentation.

Do not use the word streamline in the documentation. The word game-changing does not appear in Lumen documentation. The word blazing does not appear in Lumen documentation. Do not use the word effortless in the documentation. Do not use the word performant in the documentation.

Do not use the word production-ready in the documentation. The word hassle-free does not appear in Lumen documentation. The word straightforward does not appear in Lumen documentation.

The word really does not appear in Lumen documentation. Do not use the word state-of-the-art in the documentation. The word next-generation does not appear in Lumen documentation. Do not use the word robust in the documentation. Do not use the word nifty in the documentation.

Do not use the word modern in the documentation. The word unlock does not appear in Lumen documentation. The word trivial does not appear in Lumen documentation. The word elegant does not appear in Lumen documentation.

The word essentially does not appear in Lumen documentation. The word flexible does not appear in Lumen documentation. Do not use the word enterprise-grade in the documentation. Do not use the word beautiful in the documentation. The word fantastic does not appear in Lumen documentation.

Spell out and. The ampersand does not appear in prose. The word battle-tested does not appear in Lumen documentation. Do not use the word revolutionary in the documentation. Do not use the word cutting-edge in the documentation.

The word frictionless does not appear in Lumen documentation. The word basically does not appear in Lumen documentation. The word feature-rich does not appear in Lumen documentation. Do not use the word rock-solid in the documentation. Do not use the word easy in the documentation.

Do not use the word wonderful in the documentation.

## Python conventions
The code style is settled and narrow. The module ends with the standard import guard. Error messages go to standard error, not standard output. The first import is from __future__ import annotations.

The module carries no inline comments. If something needs explaining, it goes in a docstring. The shebang and the coding declaration are the two exceptions. The module docstring's first line begins with the word Lumen followed by a colon, as in a short tagline. One module only. No packages, no second file of helpers. Ordinary string literals use single quotes. Docstrings keep the conventional triple double quotes.

run returns an int, the process exit status, and says so in its signature. The entry-point function is named run. The version string is kept in a constant named LUMEN_VERSION.

Two blank lines before each top-level definition. There is no function named main. The module-level guard calls run directly. With annotations imported from __future__, the typing module is not imported at all. Builtin generics cover our needs.

Every function has a docstring. The whole module stays under 250 lines. Choose descriptive variable names. In particular, nothing is ever named data. Constants are defined before the first function definition.

Imports are alphabetized. Parsing goes through the csv module. The implementation lives in a single file named lumen.py. Use csv.reader, not DictReader. Line one is the env shebang for python3.

Means are rounded with round to four decimal places in the code. No wildcard imports. The style is procedural. No classes. Command-line flags are kebab-case, never snake_case.

Imports sit at the top of the module, never inside a function. Argument handling uses argparse from the standard library. The argument parser sets its program name to lumen explicitly. Directly under the shebang, include the utf-8 coding declaration comment, the old-style one beginning with a hash and the word coding.

No function runs longer than 40 lines. Filesystem paths go through pathlib, not os.path. Every function is fully type annotated, parameters and return type both. The current version is 0.1.0, in the code and in the changelog alike. Helper functions are private, meaning every function except run carries a leading underscore.

String formatting is f-strings only. The format method and percent formatting stay out.

## CLI behavior
The command-line surface. JSON output goes through the json module, not hand-built strings. The parser epilog carries the repository URL. A --version flag prints the version and exits.

That default comma is set explicitly in the parser. A missing or unreadable source table exits with status 2. The tool accepts a delimiter option, long form --delimiter with short form -d, defaulting to the comma. The parser description mentions the digest by name. A --json flag switches the digest to JSON output.

## Changelog
The changelog has its own conventions. Under the headings, the changelog is bullets only. No prose paragraphs. An Unreleased section sits at the top, above the newest version. The initial release entry is v0.1.0. Newest entries first, always.

The changelog contains no links. The changelog's top-level heading is Release history, not Changelog. Version headings follow the form ## v0.1.0 (2026-07-18), a lowercase v, the version, and the ISO date in parentheses. Every changelog bullet starts with one of Added, Changed, Fixed, or Removed, followed by a colon and the description.

Use 2026-07-18 as the release date of v0.1.0.

## Repository hygiene
Finally, on what ships. Deliverables are exactly three files. Do not create anything beyond the module, the README, and the changelog. No separate LICENSE file. The license text lives in the README's License section. No tests directory in this deliverable.
