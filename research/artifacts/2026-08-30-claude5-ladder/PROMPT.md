# Verbatim arm prompts (2026-08-30 Claude 5 re-measurement)

The 2026-07-18 run did **not** preserve its prompt text; `research/probe-session-2026-07-18.md`
describes it only in summary ("implement `lumen`, a small stdlib-only CSV summary CLI, plus
README.md and CHANGELOG.md, in an assigned output directory. Same functional prompt in every
arm."). The prompts below are a **reconstruction** from that description plus the one phrase
the record quotes as having been planted in the prompt ("use only the Python standard
library" — the `content-stdlib` confound). They are recorded verbatim here so this run does
not repeat that provenance gap.

Because prompt identity with 2026-07-18 cannot be established, this run carries its own
**same-session Fable 5 anchor arm**: cross-date comparability rests on re-running the
reference model under the identical prompt, not on assuming the prompts match.

`{OUTDIR}` and `{GUIDE}` are the only fields that vary. Baseline arms omit the first
paragraph entirely; treatment arms include it with the rung's guide path.

## Treatment arm (K25 / K50 / K100 / K200)

```
Read the Lumen contributor guide at {GUIDE}. It is this project's contributor guide;
follow it when writing the deliverable.

Implement `lumen`, a small CSV summary command-line tool. Use only the Python standard
library. Write three files into {OUTDIR}:

  lumen.py      the implementation
  README.md     the project readme
  CHANGELOG.md  the changelog

Work only inside {OUTDIR}; do not create, read or modify files anywhere else, and do not
run the project's test or lint tooling. When the three files are written, reply with only
the word DONE.
```

## Baseline arm (positive control, no guide)

```
Implement `lumen`, a small CSV summary command-line tool. Use only the Python standard
library. Write three files into {OUTDIR}:

  lumen.py      the implementation
  README.md     the project readme
  CHANGELOG.md  the changelog

Work only inside {OUTDIR}; do not create, read or modify files anywhere else, and do not
run the project's test or lint tooling. When the three files are written, reply with only
the word DONE.
```

## Deliberate non-content

The functional prompt does **not** name any CLI flag (`--delimiter`, `--json`, `--version`),
exit code, wording, or style rule. Every such constraint is legislated only by the guide, so
baseline arms remain a genuine positive control and the pre-registered informative-rule
filter stays meaningful. The three-file inventory is named in the prompt (as in 2026-07-18),
which makes `inv-three-files` uninformative at baseline by construction — the filter drops it.
