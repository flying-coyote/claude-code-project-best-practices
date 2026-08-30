# Design: a ladder Fable 5 can actually fail

**Status**: design only — not built, not run. Written 2026-08-30 to discharge the residual
open item PLAN.md has carried since 2026-07-18 ("a Fable-failure-capable design:
conflicting/semantic rules, one-pass low-effort regime, distractor load, multiple renderings
per rung"), and to record what the 2026-08-30 Claude 5 arms taught about *why* the current
instrument ceilings.

## The problem, restated precisely

Across five rounds (2026-07-16 ×2, 2026-07-18, 2026-08-30 ×2 model arms), Fable 5 has never
failed this family of instrument: 12/12 at 1.0 through 200 realistic rules, twice. Opus 5
now joins it at ceiling. A sixth ceiling would discharge nothing.

The 2026-08-30 run is the first to give a *positive* clue rather than another null, because
**Sonnet 5 did fail** — and the character of its three shared-rule misses is diagnostic:

| Miss | Type |
|---|---|
| `content-four-decimals` | a required phrase simply absent |
| `term-cap-csv` | lowercase `csv` in prose |
| `md-filename-code` | `CHANGELOG.md` unbackticked in a README that backticks `` `lumen.py` `` |

All three are **surface** rules — exactly the kind the instrument is full of. So the
instrument's *reach* is not the binding constraint. What separates Sonnet 5 from the two
models that held ceiling is not rule sophistication; it is headroom. Which points at the
real ceiling-maker.

## The single highest-value change: kill the verify-and-fix loop

Every arm in every round has run at **`xhigh` effort with a verify-and-fix loop**. Agents
routinely re-read their own output and repaired it before finishing — several 2026-08-30
arms said so unprompted ("verified against every rule in GUIDE-50.md", "smoke-tested the
CLI, temp artifacts removed"). At that effort, the ladder measures *whether a model can
self-check 200 surface constraints given unlimited passes*, not whether it follows them.
The answer to the former is obviously yes, which is why it ceilings.

**Design change 1 — a one-pass low-effort regime.** Run the same fixture at `effort: low`
with an explicit single-pass instruction ("write the three files once; do not re-read or
revise them").

**The mechanism note that makes this actionable**: the Agent tool has *no* effort override —
that is why every round to date inherited `xhigh`, and it is the reason five rounds ceilinged.
Workflow's `agent()` **does** take `effort`. So this regime is reachable only on the
**workflow spawn path** — which is precisely the path with this repo's documented silent
model-fallback defect (2026-07-17: Opus-served readers under a Fable request). That is not a
blocker any more: `gate_ladder.py` as generalised on 2026-08-30 gates per-turn served model
and now records per-turn effort, so an arm that silently falls back *or* silently runs at the
wrong effort fails its gate instead of polluting the result. Effort must be added to the
gate's PASS condition, not merely reported, before this regime is trusted.

Expected effect: this alone may produce Fable failures without touching the rule bank. Run it
first, as a cheap single-variable change, before building anything below.

## Design change 2 — deliberate rule conflict, with a satisfiability oracle

The 2026-08-30 run found the bank's "conflict-free by construction" comment is **already
false in rendered form**: `content-gigabyte` requires the literal phrase *"files up to one
gigabyte"* while `term-source-table` requires the input be called *"the source table"
in all documentation*. Two of three Sonnet K200 reps resolved that tension by substituting
the mandated term into the mandated phrase — a defensible reading that the strict checker
scores VIOL.

That accident is the prototype. Make it deliberate and graded:

- **Tier 1 — jointly satisfiable but tempting** (what `content-gigabyte` is today): both
  rules *can* be satisfied at once, and the golden fixture proves it. Scores the model's
  care in noticing.
- **Tier 2 — genuinely contradictory**: no artifact can satisfy both. The measurand is not
  adherence but **conflict handling**: does the model detect and surface the contradiction,
  silently pick one, or thrash? Scored as a three-way categorical, never as adherence.

**Hard requirement**: every Tier-1 conflict must ship with a golden fixture satisfying both
rules. Without that oracle a "conflict" is indistinguishable from a bank bug — this session
could only classify `content-gigabyte` because golden demonstrably satisfies both.
Tier-2 rules must be **excluded from the adherence denominator by construction**, or they
manufacture a fake degradation curve that would look exactly like a located cap.

## Design change 3 — semantic rules with a non-regex checker

Every rule today is a regex or a small AST check, so every rule is satisfiable by pattern
matching. Add rules whose satisfaction requires understanding:

- *"The Options table rows are ordered by how often a user would reach for the flag."*
- *"The Development section explains **why** the issue-first rule exists, not just that it does."*
- *"No sentence in the README states something the code does not do."* (a consistency rule
  between artifacts — the only rule type here that can catch a confabulation)

These need an **LLM judge**, which imports its own failure modes. Non-negotiables, all
learned the expensive way in this repo: the judge must be served-model-gated like any other
arm; it must score blind to which arm produced the artifact; it must be validated against
the golden fixture and against the baseline arms *before* any treatment arm is scored
(a judge that cannot separate a compliant golden from a 79-violation baseline is not a
judge); and its verdicts must be reported separately from the mechanical ones, never pooled
into one adherence number.

## Design change 4 — multiple renderings per rung

Today each rung is **one seed-locked rendering**, so rung size is confounded with sentence
adjacency: K200's guide is a different document, not merely a longer one. Every result in
this program, including 2026-08-30's, carries that caveat unresolved.

Fix: generate **m ≥ 3 renderings per rung** from different shuffle seeds with the rule set
held fixed. Rendering becomes a crossed factor, and between-rendering variance at fixed K
gives, for the first time, an estimate of the noise floor a load effect must clear.

This is the cheapest structural fix in this document — `ladder_bank.py` already takes a seed
offset per rung — and it is what turns "Sonnet 5 missed one rule at K200" from suggestive
into testable.

## Design change 5 — distractor load

Add guide sections that are plausible, on-topic, and legislate **nothing** checkable
(architecture rationale, a contributor code of conduct, a release-process narrative).
Distractors raise token load and reading burden without adding rules, separating *guide
length* from *rule count* — currently perfectly confounded. A K100-rules/K200-length arm and
a K200-rules/K200-length arm answer which one the model is actually straining against.

## Power: the current n cannot see the effect it just found

The 2026-08-30 effect is roughly **1 miss per 100 shared rules**, at n=3 per cell. Three
reps cannot distinguish that from noise; it was only visible because the comparison cell was
a clean 3/3 sweep. Any design meant to *locate* a cap rather than notice one needs

- n ≥ 10 per (model × rung × rendering) cell, and
- a pre-registered effect size worth calling a cap (e.g. mean adherence < 0.95, or ≥50% of
  reps missing ≥1 rule), fixed before running.

Without a declared threshold, "a cap" is whatever the data happens to show — which is how
five ceilings became five non-results.

## Suggested order (cheapest discriminating experiment first)

1. **Low-effort one-pass regime on the existing fixture.** No new bank, no new checker.
   Add effort to the gate's PASS condition. If Fable fails here, the residual is discharged
   for a fraction of the cost of everything below.
2. **Multiple renderings per rung.** Establishes the noise floor that every later claim needs.
3. **Distractor arms.** Separates length from rule count.
4. **Tier-1 conflicts** (with golden oracles).
5. **Semantic rules + validated judge**, and **Tier-2 conflict handling** as a separate
   categorical measurand.

Steps 1–3 reuse the current instrument entirely and are the ones that most plausibly break
the ceiling. Steps 4–5 change what is being measured and should not be started until 1–3
have shown the instrument can move at all.

## What this design does not fix

The measurand stays *Claude-in-the-Claude-Code-harness on one small greenfield task*.
Agents inherit the ambient CLAUDE.md, so the informative set stays session-relative; a
greenfield CLI is not a large existing codebase; and none of this touches the two figures
that matter most — **~80% CLAUDE.md adherence** needs an ambient-CLAUDE.md instrument, and
the **60% context heuristic** needs a context-fill instrument. Both remain open, and no
amount of ladder work will close either.
