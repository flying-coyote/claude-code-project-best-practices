# Prompt: Claude 5-era re-measurement program

Paste everything in the fenced block below into a fresh Claude Code session with
the working directory at the repo root. Written 2026-08-29 after a review pass
that found the evidence base sound in method and stale in fact.

---

```
Work the Claude 5 re-measurement program in this repo until it is done or you hit
something only a human can decide. Read this whole brief before starting.

## Why this exists

80% of this repo's measurement claims (50 of 62) are dated before Opus 5 shipped
on 2026-07-24. Every claim dated after it is a TOOLING or CORPUS measurement from
the last two days — not one is a behavioural threshold. So the behavioural
evidence base is effectively 100% pre-Claude-5, in a repo whose product is
evidence-graded advice about how to work with Claude.

`analysis/behavioral-insights.md:348` already declares this:
"Gap: no Claude 5-family re-measurement of any threshold (opened 2026-08-13).
None of the 80% adherence / 60% context / ~150-instruction figures has been
re-measured on Claude 5." PLAN.md now carries a row for it.

## What already exists — this is arms, not tooling

`research/artifacts/2026-07-18-realistic-ladder/` is a working, seeded,
provenance-checked instrument: ladder_bank.py (fixture generation, seed 718),
gate_ladder.py, score_ladder.py, aggregate_ladder.py, a golden/ fixture, and
GUIDE-{25,50,100,200}.md. PROVENANCE.md records that the regenerated guides were
verified byte-identical to what the agents actually read.

`gate_results.json` holds 33 arms and exactly three served-model strings:
`<synthetic>`, `claude-fable-5`, `claude-opus-4-8`. No Claude 5 arm exists
anywhere in the repo. Do NOT build a new instrument. Add arms to this one.

## The work, in priority order

1. An Opus 5 arm and a Sonnet 5 arm on the realistic-diversity ladder, same
   instrument, same fixtures, same gating. This is the single highest-value item:
   it moves the largest block of stale evidence at once.

2. Handle the tokenizer confound FIRST, before any percent-of-window comparison.
   `behavioral-insights.md:147` quotes Anthropic verbatim: "The same input text
   produces approximately 30% more tokens than on Claude Sonnet 4.6." Any
   threshold expressed as a percentage of the context window is therefore NOT
   comparable across that boundary. Re-baseline token counts per model and report
   absolute tokens alongside any percentage.

3. Record served model AND tokenizer generation with every single measurement.
   Per-turn served-model gating is already mandatory here: a 2026-07-17 probe
   caught a silent workflow-path model fallback (Opus-served readers under a Fable
   request) only because it gated. An ungated arm is not evidence.

4. The three headline figures, each with an open gap entry naming what would close
   it — read them at `behavioral-insights.md:344-348` before designing anything:
   - ~80% CLAUDE.md adherence (needs: same CLAUDE.md across N sessions, follow-rate
     per instruction TYPE)
   - ~150 instruction cap (needs: ablation varying count, measuring adherence.
     Two Fable rounds already hit ceiling and are descriptive only — the
     instruments never demonstrated they can DETECT degradation, so a third
     ceiling result discharges nothing)
   - 60% context threshold (already RECLASSIFIED 2026-05-30 as an intervention
     heuristic, not a degradation onset — do not re-litigate that; the open
     question is whether the heuristic still holds on Claude 5)

5. A Fable-failure-capable design. PLAN.md records this as the residual from
   2026-07-18: conflicting/semantic rules, one-pass low-effort regime, distractor
   load, multiple renderings per rung. Ceiling results without a positive control
   are why three prior rounds proved little.

## Traps — every one of these actually happened here

- VERIFY BY RUNNING, NOT BY READING. A review pass proposed `grep -qE` to fix a
  portability bug; executing the script found the pattern also began with `-----`
  and grep parsed it as options. Four fail-open bugs in one hook, and the fourth
  was only findable by execution.
- The corpus disagrees with itself. A claim was corrected in one doc on 2026-05-30
  and the sibling doc carried the pre-correction wording for three months. Before
  researching any figure, grep the whole corpus for it — the answer may already be
  here.
- Sources may not exist. "Jenova Research", cited as the source of a security
  statistic in two live docs, returns an unrelated AI product and a Final Fantasy
  VII character. Its missing SOURCES.md entry was the detectable symptom.
- Figures get inverted and mis-attributed. A prior pass found a token figure
  recorded backwards (-60% vs -37% actual), one claim half absent from its cited
  study, and two claims sourced to a YouTube video standing in for the studies it
  cited. Chase every figure to a primary.
- Dated record vs stale prose. A claim carrying a `date:` is HISTORY and stays;
  a claim phrased as "today" that isn't is a defect. `evidence-tiers.md`
  § "Expired but not invalid" governs. Fix tense, keep the date.
- Commit-stamp corpus-internal figures, not date-stamp them. A re-measurement
  stamped 2026-08-29 was wrong within hours because that day's own commits changed
  the lane it counted. Convention is in `evidence-tiers.md`.
- `revalidate: never` is ONLY for genuinely unrepeatable measurements, with the
  reason named. It is not a way to silence an aging claim.
- Interrupting a session kills its background workflows. Two research agents died
  mid-run that way and the workflow never completed.

## Conventions you must follow

- CONTRIBUTING.md § integration checklist is mandatory: a SOURCES.md entry with
  URL, date, tier, and pattern reference for every source. A missing entry is how
  the fabricated source above survived.
- Tiers A-D per `analysis/evidence-tiers.md`. Practitioner heuristics are Tier C
  even when the practitioner is authoritative.
- Every routable analysis doc carries `convergence:`; upgrades require verified
  external adoption recorded in the doc.
- Do not edit `archive/` — it is a tombstone lane.
- Emoji commit prefixes (📊 analysis, 📚 docs, 🔧 config). Develop on a branch,
  open a draft PR, never push to master.

## Verify before every push

npm run lint
python3 scripts/measure-link-reachability.py --links     # 0 dangling, both lanes
python3 scripts/check-measurement-expiry.py              # exit 0
node scripts/test-close-superseded-workflow.js           # 50/50
python3 scripts/test-measure-link-reachability.py        # 15/15, ~2m20s

## Done means

Each of the three headline figures either has a Claude 5 measurement with its
served model and tokenizer generation recorded, or an explicit written statement
of why it could not be measured and what would be needed — with the gap entry in
behavioral-insights.md updated either way, and PLAN.md's row reflecting reality.

A ceiling result that proves nothing is not done. Say so plainly if that is what
you got.
```
