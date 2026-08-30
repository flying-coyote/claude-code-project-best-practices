# Provenance — Claude 5 arms on the realistic-diversity ladder (2026-08-30)

## What this directory is

Added arms on the **2026-07-18 instrument**, not a new instrument. The rule bank, seed,
renderer, checker and pre-registered aggregate are the 2026-07-18 files, copied unchanged.

## Fixture identity, established BEFORE any arm ran

`ladder_bank.py` (seed 718) was re-run into `guides/` and each generated guide compared
byte-for-byte with the committed 2026-07-18 file:

```
GUIDE-25 identical   GUIDE-50 identical   GUIDE-100 identical   GUIDE-200 identical
```

The golden fixture was then re-scored under the copied checker and still returns
**199 SAT + 1 NA** (`md-ordered-paren`, conditional on an ordered list the fixture lacks) —
the same result PROVENANCE.md records for 2026-07-18. The instrument is intact, verified by
running it rather than by reading its record.

The frozen 2026-07-18 informative set was independently **recomputed** from that run's own
scored artifacts (`agent-outputs.tar.gz`) rather than assumed: 78 informative rules of 200,
24 of 25 core25 — matching the figures in `research/probe-session-2026-07-18.md`. Stored as
`informative_2026-07-18.json`.

## The prompt gap this run inherited, and closed

The 2026-07-18 run **did not preserve its prompt text**; the record describes it only in
summary. Prompt identity with that run therefore cannot be established, and no claim here
rests on it. Two consequences, both deliberate:

1. `PROMPT.md` records this run's prompts **verbatim**, so the gap is not repeated.
2. This run carries its own **same-session Fable 5 anchor arm**, re-running the 2026-07-18
   reference model under this run's exact prompt. Cross-date comparison rests on that
   re-run, not on an assumption.

This is the same class of lesson as the 2026-07-18 guide-regeneration note: freeze what the
agents actually read, or record the identity check.

## Gates

`gate_ladder.py` here is a generalised version of the 2026-07-18 gate, which hard-coded one
machine's transcript path (`/tmp/claude-1000/-home-jerem-...`) and could not run anywhere
else, and which knew only two model strings. Changes:

- transcript directory from `--tasks` / `$CLAUDE_TASKS_DIR`;
- `EXPECT` extended with the Claude 5 model strings;
- per-turn **effort** recorded (this run and 2026-07-18 both ran `xhigh`);
- **deliverable completeness** added as a gate field;
- **compaction detection rewritten and given a positive control.** The 2026-07-18 gate
  scanned the first 300 characters of each event's JSON for the substring `compact`, which
  false-positives on a deliverable that merely uses the word and misses a marker past
  character 300. A structural-field check alone would have been worse — a clean transcript
  carries only `user`/`attachment`/`assistant` types, so a type-only test can never fire,
  which is a gate that fails open. The replacement checks named compaction flags *and* the
  event envelope, and `gate_ladder.py --selftest` proves it fires on each marker shape and
  stays silent on a README containing the word "compact".

**Every arm reported here passed**: expected served model on *every* assistant turn, effort
`xhigh` on every turn, correct rung guide Read (and no guide Read at all in baseline arms),
zero compaction markers, all three deliverables present.

## Scoring: two readings, both published

`score_ladder.py` is the 2026-07-18 checker, unmodified — the **strict** reading.
`score_ladder_adjudicated.py` is that file plus **four** prose-faithful amendments, each of
the same class as one the 2026-07-18 run already made, each applied symmetrically to every
arm, all arms re-scored under the final version:

- **A1 sentence-initial capitalisation.** `content-issue-first`'s regex is case-sensitive on
  `open an issue`, so a README opening the sentence *"Open an issue before submitting a pull
  request."* — which satisfies the rule's prose exactly — scored VIOL for the capital O. The
  rule's own second branch already spells `[Bb]efore`, so the bank intended capitalisation
  tolerance and applied it to one clause only. Only the pattern's first character is made
  case-flexible; required-content capitalisation (e.g. "MIT License") is untouched, and
  prose capitalisation stays enforced by the separate `term-cap-*` ban rules.
- **A2/A3 named-constant indirection.** `cli-delimiter-default` requires the parser's default
  comma be "set explicitly"; `DEFAULT_DELIMITER = ','` passed as `default=DEFAULT_DELIMITER`
  does set it explicitly, through a name. `py-prog-lumen` fails identically with
  `prog=PROGRAM_NAME`. Amended as a **class** — any `<key>='<value>'` requirement satisfied
  through a named constant — rather than per-rule, because narrowing it to the rule that
  happened to fail first would be fitting the adjudication to the data. Accepted exactly as
  the 2026-07-18 run accepted an epilog-URL constant and a round-to-4 constant.
- **A4 private constant in `exit_two`.** That checker *already* accepts constant indirection,
  but its constant pattern is `^[A-Z][A-Z0-9_]*`, which rejects `_EXIT_MISSING = 2`. Found by
  **running** the artifact, not reading it: `sonnet5-K200-r3/lumen.py` exits 2 on a missing
  file, 1 on a malformed table, 0 on success. A grep-only review scores it a miss.

**Blast radius, measured rather than asserted**: across all 45 arms the four amendments
change **10 arms**, of which 5 are baseline arms. Baseline violation counts move only from
67–82 to 67–81 per run, so the positive control stays far from ceiling and remains healthy;
the golden fixture stays at 199 SAT + 1 NA under both checkers. Amendments rescue arms in
**all three model arms**, not one — symmetry in effect, not just in letter.

After A1–A4, four rules remain violated, all in Sonnet 5 arms, all at K200. Three are
genuine misses on inspection and one (`content-gigabyte`) is adjudication-dependent and held
to the strict reading; each is adjudicated individually in `ADJUDICATION.md`.

Both readings are reported side by side in `ADJUDICATION.md` and in the analysis doc. The
adjudicated reading is never published in place of the strict one.

## Reproduction

```
python3 ladder_bank.py guides                      # seed 718, regenerates the fixtures
python3 rescore_all.py                             # scores every arm under both checkers
python3 gate_ladder.py --tasks <transcript dir>    # served model / effort / hygiene gates
python3 gate_ladder.py --selftest                  # compaction detector positive control
python3 aggregate_c5.py --gated-only               # three pre-registered informative views
python3 tok_measure.py --tasks <transcript dir>    # per-model tokenizer re-baselining
```

Raw deliverables for all 45 arms are packed in `agent-outputs.tar.gz` (`tar xzf` restores
`out/`, which the scripts above expect), following the 2026-07-18 precedent. Every per-arm
verdict under both checkers is also flattened into `per_arm_scores.json`, so scores stay
greppable without unpacking. `tokfix/` holds the tokenizer fixtures **as read**, frozen at
run time — the 2026-07-18 lesson applied rather than re-learned.
