# Probe session 2026-08-30 — Claude 5 re-measurement

**Method**: 45 gated ladder arms + 8 tokenizer probes, run as main-loop Agent spawns inside
the Claude Code harness. Every arm gated on **per-turn served model**; every arm's effort
recorded; scoring mechanical under two checkers (strict and prose-faithful-adjudicated),
both published. Pre-registration written before any arm ran:
[`research/artifacts/2026-08-30-claude5-ladder/PREREG.md`](artifacts/2026-08-30-claude5-ladder/PREREG.md).

Consumers of these numbers: [`analysis/behavioral-insights.md`](../analysis/behavioral-insights.md)
(~150-cap section, Gaps, tokenizer confound).

---

## Why this session existed

80% of this repo's measurement claims (50 of 62) predated Opus 5 (2026-07-24), and every
claim dated after it was a tooling or corpus measurement — **not one was behavioural**. The
behavioural evidence base was effectively 100% pre-Claude-5, in a repo whose product is
evidence-graded advice about working with Claude.
`gate_results.json` from 2026-07-18 held 33 arms and exactly three served-model strings:
`<synthetic>`, `claude-fable-5`, `claude-opus-4-8`. No Claude 5 arm existed anywhere.

## Part 1 — Instrument, verified by running it

The 2026-07-18 realistic-diversity ladder was reused unchanged — **arms were added, no new
instrument was built**. Before any arm ran:

- `ladder_bank.py` (seed 718) regenerated all four guides **byte-identical** (`cmp`) to the
  committed 2026-07-18 files;
- the golden fixture re-scored to **199 SAT + 1 NA**, matching that run's record;
- the frozen 2026-07-18 informative set was **recomputed** from that run's own scored
  artifacts rather than assumed — 78 of 200 informative, 24 of 25 core25, reproducing the
  published figures exactly. That reproduction is the evidence that this session
  reconstructed the prior analysis correctly.

**Three instrument defects were found and fixed, each by execution rather than reading:**

1. **The gate could not run anywhere.** `gate_ladder.py` hard-coded one machine's transcript
   path (`/tmp/claude-1000/-home-jerem-…`) and knew only two model strings. Generalised to
   `--tasks`/`$CLAUDE_TASKS_DIR` with the Claude 5 strings added.
2. **The compaction gate failed open.** The original scanned the first 300 characters of
   each event's JSON for the substring `compact` — which false-positives on a deliverable
   that merely uses the word, and misses a marker past character 300. The obvious
   replacement (checking `type`/`subtype`) is *worse*: a clean transcript carries only
   `user`/`attachment`/`assistant`, so a type-only test can never fire. Replaced with a
   named-flag + envelope check and given a **positive control** (`--selftest`) that proves
   it fires on each marker shape and stays silent on a README containing "compact".
3. **`exit_two` rejects private constants.** Its constant-indirection branch matches
   `^[A-Z][A-Z0-9_]*`, so `_EXIT_MISSING = 2` scores VIOL. Found only by **running** the
   artifact: it exits 2 on a missing file, 1 on a malformed table, 0 on success.

**The prompt-provenance gap.** The 2026-07-18 run did not preserve its prompt text; the
record describes it only in summary. Prompt identity with that run therefore **cannot** be
established. Two responses: this run records its prompts verbatim (`PROMPT.md`), and it
carries a **same-session Fable 5 anchor arm** so cross-date comparison rests on re-running
the reference model under this run's exact prompt rather than on an assumption.

## Part 2 — Arms and gates

45 arms: 3 models × {baseline, K25, K50, K100, K200} × 3 reps.

| Arm | Requested | Served (every turn) | Effort |
|---|---|---|---|
| `opus5-*` | `opus` | `claude-opus-5` | `xhigh` |
| `sonnet5-*` | `sonnet` | `claude-sonnet-5` | `xhigh` |
| `fable5-*` | `fable` | `claude-fable-5` | `xhigh` |

**All 45 arms passed all gates — zero exclusions.** Expected served model on every assistant
turn, `xhigh` on every turn (matching 2026-07-18's conditions), correct rung guide Read,
no guide Read at all in any baseline arm, zero compaction markers, all deliverables present.
The 2026-07-18 run lost three arms to a usage limit; this one lost none.

**Positive control healthy**: the nine unguided baseline runs violate **67–82 of 200 rules**
each under strict scoring (67–81 adjudicated), bracketing the ~79/run the 2026-07-18
baselines produced.

Opus 4.8 could not be re-run — the Agent tool's model selector resolves `opus` to the
current Opus (Opus 5), so the 2026-07-18 Opus 4.8 rows remain a historical comparison.

## Part 3 — Results

Adherence on the pre-registered primary metric (informative set A, session-relative,
gated arms only), **adjudicated** scoring:

| Model | K25 | K50 | K100 | K200 |
|---|---|---|---|---|
| Fable 5 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 |
| Opus 5 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 |
| Sonnet 5 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | **0.971, 1.0, 0.985** |

Under **strict** (unamended) scoring the same table reads Opus 5 K200 = 0.985, 1.0, 0.985 and
Sonnet 5 K200 = 0.956, 0.985, 0.955; every other cell is 1.0. Full per-violation adjudication:
[`ADJUDICATION.md`](artifacts/2026-08-30-claude5-ladder/ADJUDICATION.md).

**Fable 5 replicated its 2026-07-18 result exactly** — 12/12 gated reps at 1.0 through 200
rules, under this session's independently written prompt. That replication is what licenses
comparing the other two arms to the prior run at all.

**Opus 5 is at ceiling** — 12/12 at 1.0 at every rung. Its three strict-scoring violation
instances (two reps, two distinct rules) were all checker artifacts: a sentence-initial
capital `O`, and a named constant. Both were adjudicated on evidence — the regex was read,
and the artifact was inspected — not on preference.

**Sonnet 5 — the Claude Code default — is the first model in this program to fall below
ceiling on a surviving violation.** Sub-ceiling in 2 of 3 K200 reps under the pre-registered
metric, clean at every lower rung.

### The rung-membership control (post hoc)

Rungs are nested, so a rule missed at K200 is only load-informative if it was **also present
and satisfied at K100**. Four of the strict-scoring violations turned out to be
**K200-exclusive rules**, which say nothing about load. Restricted to the 100 rules common
to K100 and K200:

| Model | K100 (3 reps) | K200 (3 reps) |
|---|---|---|
| Fable 5 | 0, 0, 0 violations | 0, 0, 0 violations |
| Opus 5 | 0, 0, 0 violations | 0, 0, 0 violations |
| Sonnet 5 | 0, 0, 0 violations | **1, 1, 1** — a *different* rule each rep |

The three rules are `content-four-decimals` (the required phrase is simply absent),
`term-cap-csv` (lowercase `csv` in CHANGELOG prose), and `md-filename-code` (`CHANGELOG.md`
unbackticked in a README that backticks `` `lumen.py` `` fourteen lines earlier). Each is a
genuine miss on inspection; none is rescued by any prose-faithful reading.

**This comparison is post hoc** — the pre-registration fixed the informative-set metric, and
the shared-rule control was added after seeing which rules failed. It is reported as
exploratory. Both analyses point the same way, which is why it is recorded.

**A filter effect worth naming**: two of the three shared-rule misses (`term-cap-csv`,
`md-filename-code`) are satisfied by **9 of 9 unguided baselines**, so the pre-registered
informative filter drops them. The filter is conservative against precisely this effect — a
guided arm missing a rule every *unguided* arm satisfies did worse than its own control.

### Strictest surviving wording

1. **Not a ceiling result, and not a located cap.** Sonnet 5 fell below 1.0 only at the
   largest rung, by one rule per rep out of 100 shared rules. That is a detectable
   load-associated effect on this instrument, **not** the ~150-instruction cap: the effect
   appears between 100 and 200 rules, is ~1%, and n=3 per cell.
2. **Rung size stays confounded with rendering** (inherited from 2026-07-18): each rung is
   one seed-locked rendering, so K200's guide is a longer document in which the same rule
   sentence sits among different neighbours. "Load" is not cleanly separated from "this
   particular rendering."
3. **Opus 5 and Fable 5 remain ceiling results and discharge nothing about the cap.** Two
   more ceilings on an instrument that has now produced five is descriptive only.
4. **Conditions**: `xhigh` effort with verify-and-fix behaviour in all arms, surface-checkable
   rules, one small greenfield task, guides read in a single Read (≈4.5k tokens at K200 —
   this is an in-context adherence measure, not a long-context one).

## Part 4 — Tokenizer re-baselining (the confound, handled before any percentage)

No tokenizer library or `count_tokens` endpoint is reachable from this session, so token
counts were recovered from the harness's own accounting: `cache_creation_input_tokens` on
the turn following a Read prices that file plus a small per-turn overhead. Two independent
replications per model, four fixtures (English prose and Python, 8 KB and 48 KB), served
model verified on every turn.

| Model | EN 48 KB | PY 48 KB | EN paired (Δ40 KB) | PY paired (Δ40 KB) |
|---|---|---|---|---|
| Opus 5 | 19,573 | 24,921 | 15,412 | 20,823 |
| Sonnet 5 | 19,308 | 24,937 | 14,649 | 20,805 |
| Fable 5 | 19,280 | 24,921 | 15,131 | 20,823 |
| Haiku 4.5 | 14,291 | 21,604 | 10,756 | 17,982 |

**Finding 1 — Opus 5, Sonnet 5 and Fable 5 share one tokenizer generation.** Max spread
across the three: **0.06% on Python**, 1.5% on English (the English spread is assistant-text
noise, not tokenization). Token-denominated comparisons *within* the Claude 5 family are
therefore like-for-like, and the ladder's three model arms are directly comparable.

**Finding 2 — the cross-generation gap is real and material.** Against Haiku 4.5, the only
4.x-generation model this harness can serve: **+35% to +43% tokens for English**, **+15.4%
to +15.8% for Python**, on identical bytes, consistent across both estimators and both
replications. This corroborates Anthropic's Tier A "approximately 30% more tokens"
(Sonnet 5 vs Sonnet 4.6) in direction and rough magnitude, and shows the effect is much
smaller for code than for prose — which the single "~30%" figure does not convey.

**Caveat, stated plainly**: Haiku 4.5 is a **proxy** for the 4.x tokenizer. Anthropic's
published claim is Sonnet 5 vs Sonnet 4.6 specifically, and Sonnet 4.6 cannot be served
here. This measures a Claude-5-vs-Haiku-4.5 gap and reads it as generational.

**Finding 3 — `chars/4` understates Claude 5 token cost by about a third.** The 2026-07-18
record estimates the guides at ~750/1,084/1,824/3,370 tokens using `chars/4`. Measured on
Claude 5 models, GUIDE-200 costs ≈4,540 tokens (13,481 chars → ~3.0 chars/token, not 4.0).
Any repo figure still using a `chars/4` estimator on Claude 5 text is low by ~32–35%.

**Consequence for the 60% figure**: percent-of-window thresholds measured before this
boundary are not comparable after it, and the direction is now measured rather than assumed
— the same text fills a token-denominated budget materially faster on Claude 5. Absolute
token counts are reported alongside every percentage above.

## Part 5 — What was NOT measured

- **The ~80% CLAUDE.md adherence figure was not re-measured.** This instrument measures
  adherence to a *contributor guide read on demand*, not to a CLAUDE.md loaded ambiently
  across N sessions, and it reports per-rule verdicts rather than the per-instruction-TYPE
  follow rate the gap asks for. The gap's stated need — same CLAUDE.md across N sessions,
  follow-rate per instruction type — remains open and is untouched by this session.
- **The 60% context heuristic was not re-measured.** Only its tokenizer denominator was
  re-baselined. The fill-vs-quality correlation study the gap asks for needs a context-fill
  instrument, not this one; the guides here occupy <1% of the window.
- **The ~150 cap was not located.** The one sub-ceiling signal sits between 100 and 200
  rules and is ~1% in size — it neither confirms nor refutes a cap near 150.
- **The Fable-failure-capable design was not built.** Fable 5 hit ceiling again (12/12).
  The residual from 2026-07-18 — conflicting/semantic rules, one-pass low-effort regime,
  distractor load, multiple renderings per rung — stands unchanged. This session did add
  one relevant datum: `content-gigabyte` shows the bank's "conflict-free by construction"
  claim is not quite true in rendered form (two rules pull against each other, though the
  golden fixture proves they remain jointly satisfiable), which is a starting point for the
  conflicting-rule design rather than a substitute for it.

## Raw artifacts

[`research/artifacts/2026-08-30-claude5-ladder/`](artifacts/2026-08-30-claude5-ladder/) —
45 arms' deliverables under `out/`, per-arm strict and adjudicated verdicts, `gate_results.json`,
`aggregate_results.json` / `aggregate_results_adjudicated.json`, `tokenizer_results.json`,
`PREREG.md`, `PROMPT.md`, `ADJUDICATION.md`, `PROVENANCE.md`, and the reproduction commands.
