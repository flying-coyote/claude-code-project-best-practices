# Adjudication log — every violation, and why it did or did not survive

The strict checker is the 2026-07-18 `score_ladder.py`, unmodified. The adjudicated checker
adds four amendments, each of the same class as an amendment the 2026-07-18 run already
made, each applied **symmetrically to all 45 arms**, all arms re-scored under the final
version. Both readings are published; the adjudicated one never replaces the strict one.

`PREREG.md` committed in advance to exactly this step: *"a sub-ceiling score is
interpretable only if … the specific violated rule survives an adjudication check against
the rule's prose, not the regex's literalism."*

## The amendments

| # | Rule class | Why the strict verdict is wrong | 2026-07-18 precedent |
|---|---|---|---|
| **A1** | sentence-initial capitalisation | `content-issue-first`'s regex is case-sensitive on `open an issue`. A README opening *"Open an issue before submitting a pull request."* satisfies the prose exactly and scores VIOL for the capital O. The rule's **own second branch already spells `[Bb]efore`**, so the bank intended capitalisation tolerance and applied it to one clause only. Only the pattern's first character is made case-flexible. | amendment 6 (same rule, different literalism) |
| **A2/A3** | named-constant indirection | `cli-delimiter-default` wants `default=','`; the artifact writes `DEFAULT_DELIMITER = ','` then `default=DEFAULT_DELIMITER`. `py-prog-lumen` fails identically with `prog=PROGRAM_NAME`. Amended as a **class**, not per-rule — narrowing it to the rule that happened to fail first would be fitting the adjudication to the data. | amendments 4 and 5 (epilog-URL and round-to-4 constants) |
| **A4** | private constant in `exit_two` | `exit_two` *already* accepts constant indirection, but its constant pattern is `^[A-Z][A-Z0-9_]*`, which rejects `_EXIT_MISSING = 2`. **Found by running the program, not reading it**: `sonnet5-K200-r3/lumen.py` returns exit status 2 on a missing file, 1 on a malformed table, 0 on success — verified by execution. A grep-only review reads this as a miss. | extends `exit_two`'s own stated intent |

**Blast radius, measured:** 10 of 45 arms change, 5 of them baseline arms. Baseline
violation counts move from 67–82 to 67–81 per run — the positive control is essentially
unchanged and remains far from ceiling. The golden fixture stays at 199 SAT + 1 NA under
both checkers. Amendments rescue arms in **all three model arms**, not one: symmetry in
effect, not just in letter.

## Every surviving violation, adjudicated individually

After A1–A4, four distinct rules remain violated, all in Sonnet 5 arms, all at K200.

| Rule | Arm(s) | Evidence | Verdict |
|---|---|---|---|
| `content-four-decimals` | sonnet5-K200-r1 | The README contains no occurrence of "decimal" or "rounded" at all. The guide requires *"The README states that means are rounded to four decimal places."* The requirement is simply absent. | **GENUINE MISS** |
| `term-cap-csv` | sonnet5-K200-r2 | CHANGELOG prose reads *"source table parsing through the standard library csv module"* — lowercase `csv` outside a code span, which the guide bans (*"The abbreviation CSV is always uppercase in prose"*). The identifier belonged in a code span. | **GENUINE MISS** (pedantic but unambiguous) |
| `md-filename-code` | sonnet5-K200-r3 | The same README backticks `` `lumen.py` `` on line 10 and writes bare `CHANGELOG.md` on line 24. Inconsistent application **within one file** is strong evidence of a slip rather than a checker artifact. | **GENUINE MISS** |
| `content-gigabyte` | sonnet5-K200-r1, r3 | Both wrote *"source tables up to one gigabyte"* where the rule requires the literal *"files up to one gigabyte"* — substituting the guide's own mandated term (`term-source-table`: *"The input CSV is referred to as the source table in all documentation"*). **The golden fixture proves the two are jointly satisfiable**: it writes "comfortably handles files up to one gigabyte" and still uses "source table" six times. So this is not a hard rule conflict — but the sentence does pull two rules against each other. | **ADJUDICATION-DEPENDENT**, held to the strict reading, per the 2026-07-18 `content-stdlib` precedent. Both readings reported. |

`content-gigabyte` is excluded from the K100-vs-K200 controlled comparison because it is a
**K200-exclusive rule** — it is not in the K100 rung at all, so missing it says nothing
about load.

## What the rung-membership check changed

Rungs are nested (25 ⊂ 50 ⊂ 100 ⊂ 200), so a rule missed at K200 is only load-informative
if it was also *present and satisfied* at K100. Checking this was decisive:

- `content-gigabyte`, `content-issue-first`, `cli-exit-2`, `cli-delimiter-default` are
  **K200-exclusive** — uninformative about load.
- `content-four-decimals`, `term-cap-csv`, `md-filename-code` are present in **both** K100
  and K200.

Restricted to the 100 rules common to K100 and K200, adjudicated:

| model | K100 (r1, r2, r3) | K200 (r1, r2, r3) |
|---|---|---|
| Fable 5 | 0, 0, 0 violations | 0, 0, 0 violations |
| Opus 5 | 0, 0, 0 violations | 0, 0, 0 violations |
| Sonnet 5 | 0, 0, 0 violations | 1, 1, 1 — `content-four-decimals`, `term-cap-csv`, `md-filename-code` |

**This comparison is post hoc.** `PREREG.md` fixed the informative-set metric as primary;
the shared-rule control was added after seeing which rules failed. It is reported as
exploratory, and the pre-registered metric is reported as primary. Both point the same way,
which is why the finding is worth recording at all.

## A methodological note the pre-registered filter would have hidden

Two of the three load-informative misses — `term-cap-csv` and `md-filename-code` — are
satisfied by **9 of 9 unguided baseline runs**. The pre-registered informative filter
(SAT in ≤2 of the baselines) therefore **drops them as uninformative**, and under the
primary metric only `content-four-decimals` counts.

That filter is doing its job — it removes rules a model satisfies anyway — but it is
**conservative against exactly this effect**. A guided run at K200 missing a rule that every
unguided run satisfies spontaneously is not a weaker signal than a normal adherence dip; it
is a stronger one, because the guided arm did *worse than the no-guide control* on that
rule. Recorded here rather than folded into the headline, because changing the primary
metric after seeing the data is the failure mode the pre-registration exists to prevent.
