#!/usr/bin/env python3
"""Realistic-prose adherence ladder — rule bank + guide renderer + nested selection.

Instrument for the behavioral-insights re-measure (realistic rule diversity,
no numbered scaffolding, baseline positive control, Opus comparison arm).
Seeded; regenerates deterministically. Seed 718 (2026-07-18).
"""
import json
import random
import sys
from pathlib import Path

SEED = 718
RELEASE_DATE = "2026-07-18"

# Each rule: id, rtype (category), section (guide section), prose (phrasing
# variants; seeded pick), check (kind + params, implemented in score_ladder.py).
# Rules are conflict-free by construction: each targets a distinct token or
# structural aspect, and required-content lines avoid banned punctuation/words.

R = []


def rule(rid, rtype, section, prose, check):
    R.append({"id": rid, "rtype": rtype, "section": section,
              "prose": prose if isinstance(prose, list) else [prose],
              "check": check})


# ---------------------------------------------------------------- vocabulary
rule("term-digest", "terminology", "Project vocabulary",
     ["We call the printed output the digest, and the README should use that word for it consistently (at least twice).",
      "The tool's printed report is called the digest. Use that term in the README, at least twice."],
     {"kind": "prose_requires_regex", "file": "README.md", "pattern": r"\bdigest\b", "min": 2})
rule("term-source-table", "terminology", "Project vocabulary",
     ["The input CSV is referred to as the source table in all documentation.",
      "Documentation refers to the input file as the source table."],
     {"kind": "prose_requires_regex", "file": "README.md", "pattern": r"\bsource table\b", "min": 1})
rule("term-numeric-fields", "terminology", "Project vocabulary",
     ["Columns that hold numbers are called numeric fields in prose, and the README should use that phrase.",
      "In prose we say numeric fields, so the README should contain that phrase."],
     {"kind": "prose_requires_regex", "file": "README.md", "pattern": r"\bnumeric fields?\b", "min": 1})
rule("term-cap-lumen", "terminology", "Project vocabulary",
     ["The project name is written Lumen, capitalized, whenever it appears in prose. Lowercase lumen is reserved for the command itself in code spans.",
      "Write the project name as Lumen in prose. The lowercase form belongs only in code spans that show the command."],
     {"kind": "custom", "fn": "cap_lumen"})
rule("term-cap-csv", "terminology", "Project vocabulary",
     ["The abbreviation CSV is always uppercase in prose.",
      "Always write CSV in capitals in prose."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?<![\w./-])csv(?![\w.-])"})
rule("term-cap-json", "terminology", "Project vocabulary",
     ["JSON is likewise always uppercase in prose."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?<![\w./-])json(?![\w.-])"})
rule("term-cap-python", "terminology", "Project vocabulary",
     ["Python is capitalized in prose, every time."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?<![\w./-])python(?![\w.-])"})
rule("term-macos", "terminology", "Project vocabulary",
     ["Apple's operating system is written macOS, never MacOS and never Mac OS."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"\bMacOS\b|\bMac OS\b"})

# ---------------------------------------------------------- required content
CONTENT = [
    ("content-mit", r"\bMIT License\b",
     ["Lumen is released under the MIT License, and the README must say so.",
      "State in the README that Lumen is released under the MIT License."]),
    ("content-py311", r"\bPython 3\.11 or newer\b",
     ["The README states that Lumen requires Python 3.11 or newer, in exactly those words."]),
    ("content-support-email", r"support@lumen\.dev",
     ["Support questions go to support@lumen.dev, and the README should give that address."]),
    ("content-copyright", r"Copyright 2026 The Lumen Project",
     ["The copyright line reads Copyright 2026 The Lumen Project."]),
    ("content-no-deps", r"[Nn]o third-party dependencies",
     ["Somewhere in the README, state plainly that Lumen has no third-party dependencies."]),
    ("content-pip", r"pip install lumen-csv",
     ["Installation is via pip install lumen-csv, and the README shows that exact command."]),
    ("content-status-alpha", r"Status: alpha",
     ["Near the top of the README include the line Status: alpha."]),
    ("content-repo-url", r"https://github\.com/lumen-project/lumen",
     ["The repository lives at https://github.com/lumen-project/lumen. Give that URL in the README."]),
    ("content-tested-on", r"Tested on Linux and macOS",
     ["The README carries the sentence Tested on Linux and macOS."]),
    ("content-windows", r"Windows is not currently supported",
     ["Note in the README that Windows is not currently supported, in those words."]),
    ("content-reads-once", r"reads the source table exactly once",
     ["Somewhere in the README, note that Lumen reads the source table exactly once."]),
    ("content-stdlib", r"standard library only",
     ["The phrase standard library only appears in the README."]),
    ("content-no-network", r"Lumen never transmits data over the network",
     ["A privacy note is required: Lumen never transmits data over the network, in exactly those words."]),
    ("content-issue-first",
     r"open an issue [^.]{0,60}(?:before|prior to) submitting a pull request"
     r"|[Bb]efore submitting a pull request[^.]{0,60}open an issue",
     ["The Development section asks contributors to open an issue before submitting a pull request."]),
    ("content-gigabyte", r"files up to one gigabyte",
     ["The README mentions that Lumen comfortably handles files up to one gigabyte."]),
    ("content-utf8", r"UTF-8",
     ["The README states that input is expected to be UTF-8 encoded."]),
]
for rid, pat, prose in CONTENT:
    rule(rid, "required-content", "README content", prose,
         {"kind": "prose_requires_regex", "file": "README.md", "pattern": pat, "min": 1})

# --------------------------------------------------------- README structure
rule("struct-one-h1", "readme-structure", "README structure",
     ["The README has exactly one top-level heading, and it is # Lumen, nothing more."],
     {"kind": "custom", "fn": "one_h1_lumen"})
rule("struct-h1-first-line", "readme-structure", "README structure",
     ["That heading is the very first line of the file."],
     {"kind": "custom", "fn": "h1_first_line"})
rule("struct-section-order", "readme-structure", "README structure",
     ["Second-level sections appear in this order: Overview, then Installation, then Usage examples, then Options, then Exit codes, then Development, then License."],
     {"kind": "custom", "fn": "section_order"})
for sec in ["Overview", "Installation", "Usage examples", "Options", "Exit codes", "Development", "License"]:
    sid = sec.lower().replace(" ", "-")
    rule(f"struct-has-{sid}", "readme-structure", "README structure",
         [f"The README includes a second-level section titled {sec}."],
         {"kind": "custom", "fn": "has_h2", "arg": sec})
rule("struct-no-h3", "readme-structure", "README structure",
     ["Keep the README flat. No third-level or deeper headings."],
     {"kind": "prose_bans_regex", "file": "README.md", "pattern": r"^###", "raw": True})
rule("struct-ends-license", "readme-structure", "README structure",
     ["The License section closes the file. Nothing comes after it except the license text itself."],
     {"kind": "custom", "fn": "ends_license"})
rule("struct-options-table", "readme-structure", "README structure",
     ["The Options section is a table, not a list."],
     {"kind": "custom", "fn": "options_is_table"})
rule("struct-options-3col", "readme-structure", "README structure",
     ["That table has exactly three columns: Option, Argument, Description."],
     {"kind": "custom", "fn": "options_3col"})
rule("struct-usage-3ex", "readme-structure", "README structure",
     ["Usage examples shows at least three distinct invocations of lumen."],
     {"kind": "custom", "fn": "three_invocations"})

# ------------------------------------------------------------ markdown style
rule("md-bullets-star", "markdown-style", "Markdown style",
     ["Unordered lists use the asterisk marker, not the hyphen, in both markdown files.",
      "Bullet lists are written with asterisks rather than hyphens, in the README and the changelog alike."],
     {"kind": "custom", "fn": "bullets_star"})
rule("md-fence-lang", "markdown-style", "Markdown style",
     ["Every code fence declares a language."],
     {"kind": "custom", "fn": "fences_have_lang"})
rule("md-fence-console", "markdown-style", "Markdown style",
     ["Shell examples are fenced as console, not bash or sh.",
      "Fence shell examples with the console language tag rather than bash."],
     {"kind": "custom", "fn": "fences_console"})
rule("md-prompt-marker", "markdown-style", "Markdown style",
     ["Inside console fences, each command line begins with a dollar sign and a space."],
     {"kind": "custom", "fn": "prompt_marker"})
rule("md-output-text", "markdown-style", "Markdown style",
     ["Sample output, when shown on its own, is fenced as text."],
     {"kind": "custom", "fn": "output_text_fence"})
rule("md-no-html", "markdown-style", "Markdown style",
     ["No raw HTML in the markdown files."],
     {"kind": "custom", "fn": "no_html"})
rule("md-no-images", "markdown-style", "Markdown style",
     ["No images or badges anywhere in the documentation."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"!\[", "raw": True})
rule("md-filename-code", "markdown-style", "Markdown style",
     ["File names such as lumen.py are wrapped in inline code when mentioned in prose."],
     {"kind": "custom", "fn": "filenames_backticked"})
rule("md-table-align", "markdown-style", "Markdown style",
     ["Table separator rows use colons to declare alignment."],
     {"kind": "custom", "fn": "table_align_colons"})
rule("md-line-length", "markdown-style", "Markdown style",
     ["Wrap README prose at 100 characters. Table rows and fenced content are exempt."],
     {"kind": "custom", "fn": "line_length_100"})
rule("md-ordered-paren", "markdown-style", "Markdown style",
     ["If you write an ordered list, use the 1) numbering style rather than 1. followed by a period."],
     {"kind": "custom", "fn": "ordered_paren"})
rule("md-https-only", "markdown-style", "Markdown style",
     ["Links always use https."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"http://", "raw": True})

# --------------------------------------------------------------- prose style
rule("prose-no-exclaim", "prose-style", "Prose style",
     ["No exclamation marks in the documentation. The tone stays level.",
      "Documentation never uses an exclamation mark."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"!"})
rule("prose-no-question", "prose-style", "Prose style",
     ["No rhetorical questions in the README, which in practice means no question marks."],
     {"kind": "prose_bans_regex", "file": "README.md", "pattern": r"\?"})
rule("prose-iso-dates", "prose-style", "Prose style",
     ["Dates are written ISO style, year first, as in 2026-07-18. Month names never appear in dates."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md",
      "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}"})
rule("prose-no-eg", "prose-style", "Prose style",
     ["Write for example rather than e.g."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"\be\.g\."})
rule("prose-no-ie", "prose-style", "Prose style",
     ["Write that is rather than i.e."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"\bi\.e\."})
rule("prose-no-ampersand", "prose-style", "Prose style",
     ["Spell out and. The ampersand does not appear in prose."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"&"})
rule("prose-no-contractions", "prose-style", "Prose style",
     ["Documentation prose avoids contractions, so write do not rather than don't, it is rather than it's, and so on."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md",
      "pattern": r"\b(don't|can't|won't|isn't|aren't|doesn't|didn't|it's|you're|we're|that's|there's|hasn't|haven't|wouldn't|couldn't|shouldn't|let's)\b"})

# ---------------------------------------------------------- python naming
rule("py-file-name", "python-naming", "Python conventions",
     ["The implementation lives in a single file named lumen.py."],
     {"kind": "custom", "fn": "file_lumen_py"})
rule("py-entry-run", "python-naming", "Python conventions",
     ["The entry-point function is named run."],
     {"kind": "py_requires_regex", "pattern": r"^def run\("})
rule("py-no-main-def", "python-naming", "Python conventions",
     ["There is no function named main. The module-level guard calls run directly."],
     {"kind": "py_bans_regex", "pattern": r"^def main\("})
rule("py-prog-lumen", "python-naming", "Python conventions",
     ["The argument parser sets its program name to lumen explicitly."],
     {"kind": "py_requires_regex", "pattern": r"prog\s*=\s*['\"]lumen['\"]"})
rule("py-version-const", "python-naming", "Python conventions",
     ["The version string is kept in a constant named LUMEN_VERSION."],
     {"kind": "py_requires_regex", "pattern": r"^LUMEN_VERSION\s*="})
rule("py-version-010", "python-naming", "Python conventions",
     ["The current version is 0.1.0, in the code and in the changelog alike."],
     {"kind": "custom", "fn": "version_010_consistent"})
rule("py-private-helpers", "python-naming", "Python conventions",
     ["Helper functions are private, meaning every function except run carries a leading underscore."],
     {"kind": "custom", "fn": "helpers_underscore"})
rule("py-no-classes", "python-naming", "Python conventions",
     ["The style is procedural. No classes."],
     {"kind": "py_bans_regex", "pattern": r"^class\s"})
rule("py-kebab-flags", "python-naming", "Python conventions",
     ["Command-line flags are kebab-case, never snake_case."],
     {"kind": "py_bans_regex", "pattern": r"add_argument\(\s*['\"]--[a-z0-9]+_[a-z0-9_]+['\"]"})
rule("py-no-data-var", "python-naming", "Python conventions",
     ["Choose descriptive variable names. In particular, nothing is ever named data."],
     {"kind": "py_bans_regex", "pattern": r"^\s*data\s*="})

# ----------------------------------------------------------- python idiom
rule("py-fstrings", "python-idiom", "Python conventions",
     ["String formatting is f-strings only. The format method and percent formatting stay out."],
     {"kind": "py_bans_regex", "pattern": r"\.format\(|%\s*\("})
rule("py-pathlib", "python-idiom", "Python conventions",
     ["Filesystem paths go through pathlib, not os.path."],
     {"kind": "custom", "fn": "pathlib_not_ospath"})
rule("py-argparse", "python-idiom", "Python conventions",
     ["Argument handling uses argparse from the standard library."],
     {"kind": "py_requires_regex", "pattern": r"import argparse"})
rule("py-type-hints", "python-idiom", "Python conventions",
     ["Every function is fully type annotated, parameters and return type both."],
     {"kind": "custom", "fn": "all_defs_hinted"})
rule("py-docstrings", "python-idiom", "Python conventions",
     ["Every function has a docstring."],
     {"kind": "custom", "fn": "all_defs_docstring"})
rule("py-module-doc", "python-idiom", "Python conventions",
     ["The module docstring's first line begins with the word Lumen followed by a colon, as in a short tagline."],
     {"kind": "custom", "fn": "module_doc_lumen"})
rule("py-single-quotes", "python-idiom", "Python conventions",
     ["Ordinary string literals use single quotes. Docstrings keep the conventional triple double quotes."],
     {"kind": "custom", "fn": "single_quotes"})
rule("py-main-guard", "python-idiom", "Python conventions",
     ["The module ends with the standard import guard."],
     {"kind": "py_requires_regex", "pattern": r"if __name__ =="})
rule("py-future-annotations", "python-idiom", "Python conventions",
     ["The first import is from __future__ import annotations."],
     {"kind": "py_requires_regex", "pattern": r"^from __future__ import annotations"})
rule("py-shebang", "python-idiom", "Python conventions",
     ["Line one is the env shebang for python3."],
     {"kind": "custom", "fn": "shebang_first"})
rule("py-no-wildcard", "python-idiom", "Python conventions",
     ["No wildcard imports."],
     {"kind": "py_bans_regex", "pattern": r"^from\s+\S+\s+import\s+\*"})
rule("py-imports-top", "python-idiom", "Python conventions",
     ["Imports sit at the top of the module, never inside a function."],
     {"kind": "custom", "fn": "imports_top"})
rule("py-stderr", "python-idiom", "Python conventions",
     ["Error messages go to standard error, not standard output."],
     {"kind": "py_requires_regex", "pattern": r"sys\.stderr|stderr"})
rule("py-encoding-comment", "python-idiom", "Python conventions",
     ["Directly under the shebang, include the utf-8 coding declaration comment, the old-style one beginning with a hash and the word coding."],
     {"kind": "py_requires_regex", "pattern": r"coding[:=]\s*utf-8"})

# --------------------------------------------------------- python structure
rule("py-fn-40", "python-structure", "Python conventions",
     ["No function runs longer than 40 lines."],
     {"kind": "custom", "fn": "fn_max_40"})
rule("py-module-250", "python-structure", "Python conventions",
     ["The whole module stays under 250 lines."],
     {"kind": "custom", "fn": "module_max_250"})
rule("py-one-file", "python-structure", "Python conventions",
     ["One module only. No packages, no second file of helpers."],
     {"kind": "custom", "fn": "one_py_file"})
rule("py-const-first", "python-structure", "Python conventions",
     ["Constants are defined before the first function definition."],
     {"kind": "custom", "fn": "const_before_defs"})

# ----------------------------------------------------------------- CLI rules
rule("cli-delimiter", "cli-behavior", "CLI behavior",
     ["The tool accepts a delimiter option, long form --delimiter with short form -d, defaulting to the comma."],
     {"kind": "py_requires_regex", "pattern": r"['\"]-d['\"].{0,40}['\"]--delimiter['\"]|['\"]--delimiter['\"]"})
rule("cli-delimiter-default", "cli-behavior", "CLI behavior",
     ["That default comma is set explicitly in the parser."],
     {"kind": "py_requires_regex", "pattern": r"default\s*=\s*['\"],['\"]"})
rule("cli-json-flag", "cli-behavior", "CLI behavior",
     ["A --json flag switches the digest to JSON output."],
     {"kind": "py_requires_regex", "pattern": r"['\"]--json['\"]"})
rule("cli-json-dumps", "cli-behavior", "CLI behavior",
     ["JSON output goes through the json module, not hand-built strings."],
     {"kind": "py_requires_regex", "pattern": r"json\.dumps"})
rule("cli-version-flag", "cli-behavior", "CLI behavior",
     ["A --version flag prints the version and exits."],
     {"kind": "py_requires_regex", "pattern": r"['\"]--version['\"]"})
rule("cli-exit-2", "cli-behavior", "CLI behavior",
     ["A missing or unreadable source table exits with status 2."],
     {"kind": "custom", "fn": "exit_two"})
rule("cli-desc-digest", "cli-behavior", "CLI behavior",
     ["The parser description mentions the digest by name."],
     {"kind": "py_requires_regex", "pattern": r"description\s*=\s*['\"][^'\"]*digest"})
rule("cli-epilog-url", "cli-behavior", "CLI behavior",
     ["The parser epilog carries the repository URL."],
     {"kind": "custom", "fn": "epilog_url"})

# ------------------------------------------------------------------ changelog
rule("chg-title", "changelog", "Changelog",
     ["The changelog's top-level heading is Release history, not Changelog."],
     {"kind": "custom", "fn": "chg_title"})
rule("chg-version-format", "changelog", "Changelog",
     ["Version headings follow the form ## v0.1.0 (2026-07-18), a lowercase v, the version, and the ISO date in parentheses."],
     {"kind": "custom", "fn": "chg_version_format"})
rule("chg-unreleased", "changelog", "Changelog",
     ["An Unreleased section sits at the top, above the newest version."],
     {"kind": "custom", "fn": "chg_unreleased"})
rule("chg-initial", "changelog", "Changelog",
     ["The initial release entry is v0.1.0."],
     {"kind": "prose_requires_regex", "file": "CHANGELOG.md", "pattern": r"v0\.1\.0", "min": 1})
rule("chg-date-today", "changelog", "Changelog",
     ["Use 2026-07-18 as the release date of v0.1.0."],
     {"kind": "prose_requires_regex", "file": "CHANGELOG.md", "pattern": r"2026-07-18", "min": 1})
rule("chg-verb-prefix", "changelog", "Changelog",
     ["Every changelog bullet starts with one of Added, Changed, Fixed, or Removed, followed by a colon and the description."],
     {"kind": "custom", "fn": "chg_verb_prefix"})
rule("chg-bullets-only", "changelog", "Changelog",
     ["Under the headings, the changelog is bullets only. No prose paragraphs."],
     {"kind": "custom", "fn": "chg_bullets_only"})
rule("chg-newest-first", "changelog", "Changelog",
     ["Newest entries first, always."],
     {"kind": "custom", "fn": "chg_newest_first"})

# ---------------------------------------------------------- repo hygiene
rule("inv-three-files", "file-inventory", "Repository hygiene",
     ["Deliverables are exactly three files. Do not create anything beyond the module, the README, and the changelog."],
     {"kind": "custom", "fn": "exactly_three_files"})
rule("inv-no-license-file", "file-inventory", "Repository hygiene",
     ["No separate LICENSE file. The license text lives in the README's License section."],
     {"kind": "custom", "fn": "no_license_file"})
rule("inv-no-tests-dir", "file-inventory", "Repository hygiene",
     ["No tests directory in this deliverable."],
     {"kind": "custom", "fn": "no_tests"})

# --------------------------------------------------------------- word bans
BAN_INTRO = {
    "simply": "The docs never call anything simple, so the word simply is out",
    "easy": "easy is out",
    "easily": "so is easily",
    "just": "just as a softener is out",
    "powerful": "powerful is marketing and is out",
    "robust": "robust is out",
    "blazing": "blazing is out",
    "straightforward": "straightforward is out",
    "obviously": "obviously is out",
    "very": "very is out",
    "really": "really is out",
    "great": "great is out",
    "awesome": "awesome is out",
    "perfect": "perfect is out",
    "elegant": "elegant is out",
    "quick": "quick is out",
    "quickly": "quickly is out",
    "trivial": "trivial is out",
    "basically": "basically is out",
    "comprehensive": "comprehensive is out",
    "effortless": "effortless is out",
    "lightweight": "lightweight is out",
    "user-friendly": "user-friendly is out",
    "feature-rich": "feature-rich is out",
    "cutting-edge": "cutting-edge is out",
    "state-of-the-art": "state-of-the-art is out",
    "utilize": "write use, never utilize",
    "leverage": "leverage as a verb is out",
    "performant": "performant is out",
    "intuitive": "intuitive is out",
    "seamless": None, "modern": "modern is out", "flexible": "flexible is out",
    "efficient": "efficient is out", "convenient": "convenient is out",
    "handy": "handy is out", "nifty": "nifty is out", "amazing": "amazing is out",
    "incredibly": "incredibly is out", "extremely": "extremely is out",
    "essentially": "essentially is out", "delightful": "delightful is out",
}
BAN_WORDS = [w for w, v in BAN_INTRO.items() if v is not None]  # 'seamless' excluded: adjacent to a globally-legislated token family
for w in BAN_WORDS:
    esc = w.replace("-", r"\-")
    rule(f"ban-{w}", "word-ban", "Prose style",
         [f"Do not use the word {w} in the documentation.",
          f"The word {w} does not appear in Lumen documentation."],
         {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md",
          "pattern": rf"\b{esc}\b"})

# ------------------------------------------------------- second tranche
rule("term-cap-github", "terminology", "Project vocabulary",
     ["GitHub is written with a capital H."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"\bGithub\b"})
rule("term-cap-unix", "terminology", "Project vocabulary",
     ["Unix is capitalized."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?<![\w./-])unix(?![\w./-])"})
rule("term-filepath-two-words", "terminology", "Project vocabulary",
     ["Write file path as two words, never filepath."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?i)\bfilepath\b"})
rule("term-cli-hyphen", "terminology", "Project vocabulary",
     ["Hyphenate command-line when it modifies a noun, as in command-line tool."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"\bcommand line (tool|interface|option|options|flag|flags|argument|arguments)\b"})
rule("term-readme-caps", "terminology", "Project vocabulary",
     ["The file is the README, in capitals, when mentioned in prose."],
     {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md", "pattern": r"(?<![\w./-])readme(?![\w./-])"})

CONTENT2 = [
    ("content-changelog-mention", r"CHANGELOG\.md",
     ["The README points readers to CHANGELOG.md for release notes."]),
    ("content-pure-python", r"pure Python",
     ["Describe Lumen as written in pure Python."]),
    ("content-single-file", r"a single file",
     ["The README notes that the whole tool is a single file."]),
    ("content-no-stdin", r"standard input",
     ["Note in the README that Lumen reads a file path argument and does not read from standard input."]),
    ("content-header-row", r"header row",
     ["The README explains that the first row of the source table is treated as the header row."]),
    ("content-empty-cells", r"[Ee]mpty cells are ignored",
     ["State that empty cells are ignored when computing statistics, in those words."]),
    ("content-four-decimals", r"four decimal places",
     ["The README states that means are rounded to four decimal places."]),
    ("content-semver", r"semantic versioning",
     ["The README mentions that Lumen follows semantic versioning."]),
    ("content-tagline", r"CSV digest tool",
     ["The opening line of the README describes Lumen as a CSV digest tool, in that phrase."]),
]
for rid, pat, prose in CONTENT2:
    rule(rid, "required-content", "README content", prose,
         {"kind": "prose_requires_regex", "file": "README.md", "pattern": pat, "min": 1})
rule("content-exit-codes-listed", "required-content", "README content",
     ["The Exit codes section documents all three statuses, 0 for success, 1 for a malformed source table, and 2 for a missing file."],
     {"kind": "custom", "fn": "exit_codes_listed"})

rule("md-no-emoji", "markdown-style", "Markdown style",
     ["No emoji anywhere in the repository."],
     {"kind": "custom", "fn": "no_emoji"})
rule("md-no-hr", "markdown-style", "Markdown style",
     ["No horizontal rules in the markdown files."],
     {"kind": "custom", "fn": "no_hr"})
rule("md-backtick-flags", "markdown-style", "Markdown style",
     ["Command-line flags such as --json are wrapped in inline code when they appear in prose."],
     {"kind": "custom", "fn": "flags_backticked"})

rule("py-round-4", "python-idiom", "Python conventions",
     ["Means are rounded with round to four decimal places in the code."],
     {"kind": "custom", "fn": "round_four"})
rule("py-csv-module", "python-idiom", "Python conventions",
     ["Parsing goes through the csv module."],
     {"kind": "py_requires_regex", "pattern": r"import csv"})
rule("py-no-dictreader", "python-idiom", "Python conventions",
     ["Use csv.reader, not DictReader."],
     {"kind": "py_bans_regex", "pattern": r"DictReader"})
rule("py-run-returns-int", "python-idiom", "Python conventions",
     ["run returns an int, the process exit status, and says so in its signature."],
     {"kind": "py_requires_regex", "pattern": r"def run\([^)]*\)[^:\n]*->\s*int"})
rule("py-no-typing-import", "python-idiom", "Python conventions",
     ["With annotations imported from __future__, the typing module is not imported at all. Builtin generics cover our needs."],
     {"kind": "py_bans_regex", "pattern": r"from typing import|^import typing"})
rule("py-sorted-imports", "python-structure", "Python conventions",
     ["Imports are alphabetized."],
     {"kind": "custom", "fn": "sorted_imports"})
rule("py-two-blank-lines", "python-structure", "Python conventions",
     ["Two blank lines before each top-level definition."],
     {"kind": "custom", "fn": "two_blank_lines"})
rule("py-no-comments", "python-structure", "Python conventions",
     ["The module carries no inline comments. If something needs explaining, it goes in a docstring. The shebang and the coding declaration are the two exceptions."],
     {"kind": "custom", "fn": "no_comments"})

rule("chg-no-links", "changelog", "Changelog",
     ["The changelog contains no links."],
     {"kind": "custom", "fn": "chg_no_links"})

BAN2 = ["innovative", "sleek", "superb", "fantastic", "excellent", "wonderful",
        "beautiful", "supercharge", "streamline", "streamlined", "empower",
        "unlock", "unleash", "revolutionary", "game-changing", "next-generation",
        "world-class", "best-in-class", "enterprise-grade", "production-ready",
        "battle-tested", "rock-solid", "plug-and-play", "hassle-free", "painless",
        "frictionless", "magical"]
for w in BAN2:
    esc = w.replace("-", r"\-")
    rule(f"ban-{w}", "word-ban", "Prose style",
         [f"Do not use the word {w} in the documentation.",
          f"The word {w} does not appear in Lumen documentation."],
         {"kind": "prose_bans_regex", "file": "README.md,CHANGELOG.md",
          "pattern": rf"\b{esc}\b", "ci": True})

# mark first-tranche word bans case-insensitive too
for r_ in R:
    if r_["rtype"] == "word-ban":
        r_["check"]["ci"] = True

# ------------------------------------------------------------------------
# Core-25: expected-informative rules spanning types; nested selection seeds
# from these so every rung shares them (the pre-registered load-effect set).
CORE25 = [
    "term-digest", "term-source-table", "content-py311", "content-no-network",
    "content-repo-url", "struct-one-h1", "struct-section-order",
    "struct-options-3col", "md-bullets-star", "md-fence-console",
    "md-prompt-marker", "prose-no-contractions", "py-entry-run",
    "py-no-main-def", "py-version-const", "py-private-helpers",
    "py-single-quotes", "py-future-annotations", "py-encoding-comment",
    "py-module-doc", "cli-epilog-url", "chg-title", "chg-version-format",
    "chg-unreleased", "chg-verb-prefix",
]

RUNGS = [25, 50, 100, 200]


def select_nested():
    rng = random.Random(SEED)
    by_id = {r["id"]: r for r in R}
    assert len(by_id) == len(R), "duplicate rule ids"
    for cid in CORE25:
        assert cid in by_id, f"missing core rule {cid}"
    rest = [r["id"] for r in R if r["id"] not in CORE25]
    rng.shuffle(rest)
    sets = {}
    sets[25] = list(CORE25)
    sets[50] = sets[25] + rest[:25]
    sets[100] = sets[50] + rest[25:75]
    sets[200] = sets[100] + rest[75:175]
    return sets


SECTION_ORDER = ["Project vocabulary", "README content", "README structure",
                 "Markdown style", "Prose style", "Python conventions",
                 "CLI behavior", "Changelog", "Repository hygiene"]

INTRO = (
    "# Lumen contributor guide\n\n"
    "This guide collects the conventions the Lumen project has settled on. New "
    "contributions are expected to follow all of it, the small points as much as "
    "the structural ones, because consistency is most of what keeps a small "
    "codebase readable. Read the whole guide before writing anything.\n"
)

SECTION_LEAD = {
    "Project vocabulary": "We are particular about names for things.",
    "README content": "A few statements must appear in the README verbatim or nearly so.",
    "README structure": "The README follows a fixed shape.",
    "Markdown style": "House markdown style, applying to every markdown file in the repository.",
    "Prose style": "On the prose itself.",
    "Python conventions": "The code style is settled and narrow.",
    "CLI behavior": "The command-line surface.",
    "Changelog": "The changelog has its own conventions.",
    "Repository hygiene": "Finally, on what ships.",
}


def render_guide(rule_ids, seed_offset=0):
    rng = random.Random(SEED + 1000 + seed_offset)
    by_id = {r["id"]: r for r in R}
    chosen = [by_id[i] for i in rule_ids]
    out = [INTRO]
    for sec in SECTION_ORDER:
        sec_rules = [r for r in chosen if r["section"] == sec]
        if not sec_rules:
            continue
        rng.shuffle(sec_rules)
        out.append(f"\n## {sec}\n")
        out.append(SECTION_LEAD[sec] + " ")
        sentences = []
        for r in sec_rules:
            t = rng.choice(r["prose"])
            if not t.endswith("."):
                t += "."
            sentences.append(t)
        # paragraphs of 3-5 sentences, flowing, unnumbered
        para, paras = [], []
        target = rng.randint(3, 5)
        for s in sentences:
            para.append(s)
            if len(para) >= target:
                paras.append(" ".join(para))
                para, target = [], rng.randint(3, 5)
        if para:
            paras.append(" ".join(para))
        out.append(("\n\n".join(paras)) + "\n")
    return "".join(out)


def main():
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("guides")
    outdir.mkdir(parents=True, exist_ok=True)
    sets = select_nested()
    key = {"seed": SEED, "release_date": RELEASE_DATE, "core25": CORE25,
           "rungs": {}, "bank_size": len(R),
           "rules": {r["id"]: {"rtype": r["rtype"], "check": r["check"]} for r in R}}
    for k, ids in sets.items():
        g = render_guide(ids, seed_offset=k)
        p = outdir / f"GUIDE-{k}.md"
        p.write_text(g)
        key["rungs"][str(k)] = {"ids": ids, "guide": str(p.resolve()),
                                "guide_lines": g.count("\n") + 1,
                                "guide_chars": len(g)}
        print(f"GUIDE-{k}.md: {len(ids)} rules, {len(g)} chars, ~{len(g)//4} tokens")
    (outdir / "ladder_key.json").write_text(json.dumps(key, indent=1))
    types = {}
    for rid in sets[200]:
        t = key["rules"][rid]["rtype"]
        types[t] = types.get(t, 0) + 1
    print(f"bank={len(R)} selected200 types: {json.dumps(types)}")


if __name__ == "__main__":
    main()
