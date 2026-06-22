---
evidence-tier: B
applies-to-signals: [intent-undocumented, goal-drift-unmeasured, loop-without-rethink, typed-memory-no-registry]
last-verified: 2026-06-21
revalidate-by: 2026-09-21
status: EMERGING
---

# Intent-Alignment Audit: the RETHINK / outer-loop layer

**Evidence Tier**: B — generalizes Daniel Miessler's 16 "Fable" intent prompts (the same set the 2026-06-21 self-audit ran against this repo) and is modeled on the five-question Coaching-Kata cadence already running in production in project1's `karen-evaluator` skill. Method is validated by reuse, not by a controlled study, so the doc is held lightly (EMERGING) pending audit runs that show it catching drift on other projects.

## Purpose

This doc adds the layer the rest of the audit lacks. The signal-routing audit (`AUDIT-CONTEXT.md` + `ONE-LINE-PROMPT.md`) inspects what a project **has** — does a `CLAUDE.md` exist, how many `.md` files, is `.mcp.json` present, is cron disabled — and routes to the analysis docs that fit those facts. Every Signal Collection command is a presence/absence or count check, so the audit is excellent at telling a project which conventions it is missing and weak at telling it whether the conventions it has still serve what the project is *for*. This doc is the **why** pass: a small bank of portable intent questions, each with a re-ask cadence, a decay rule, and a promotion rule, that a project runs on a schedule to catch goal drift before it shows up as a broken mechanism.

It is deliberately framed as a **standing instrument, not a one-time audit**. A project that re-asks "what is this for" only once, at setup, has answered the question for the version of itself that existed at setup — and the gap between that answer and the current mechanism is exactly where drift lives.

## Why presence-based auditing misses intent-drift

The self-audit that produced this doc (`research/self-audit-2026-06/AUDIT-FINDINGS.md`) found that the best-practices repo fails its own checks on itself in a single recurring way: a mechanism the project no longer *intends* to use still mechanically points somewhere. The freshness gate scans a `patterns/` directory archived in the v2.0 reposition and reports all-clear while verifying the empty set; `ARCHITECTURE.md` asserts a doc count the repo's actual structure outgrew two versions ago; a CI workflow holds a `contents: write` permission nobody decided it should hold. None of these is a wrong *claim* — every one is a mechanism that came apart from the reason it was added.

A presence-based audit cannot catch this, because drift is precisely the case where what a project *has* (a `patterns/` glob, a "26 documents" line, a write-scoped permission) has decoupled from *why it has it*. Presence is still true; intent has moved. The fix is not another signal — you cannot grep for "this glob points at the directory the project no longer means to use." It is a different *kind* of check: for each load-bearing mechanism, ask what it is for, then test the mechanism against that stated intent rather than only confirming the mechanism exists.

This pairs with two existing docs and does not replace either:

- [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md) supplies the **fire-on-a-cadence machinery** (`/loop`, `/goal`, cloud Routines, Desktop scheduled tasks, the Ralph lineage) this instrument runs on, and the operational risk an unattended loop carries. That doc detects the loop; this doc supplies the RETHINK step the loop should *run*.
- [`harness-engineering.md`](harness-engineering.md) is the inner-loop anchor: completion loops, self-verification, doom-loop detection, reasoning-effort allocation across plan/build/verify. Its diagnostic table asks "what's wrong with my harness?" mechanism by mechanism. This doc asks the orthogonal question the harness's own diagnostics never ask: are these still the right mechanisms for what the project is now trying to do?

## The strong-Act / stale-Orient failure mode

Boyd's OODA loop names the failure this instrument exists to catch. A project running unattended (`/loop`, a cloud Routine, a Ralph-style `while`-loop) is a strong **Act** leg: it observes, decides, and acts at machine cadence, and the verification property that makes coding safe to loop on — "tests pass or fail, programs run or crash, diffs can be inspected" (Tier B — Karpathy, [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30) — keeps each *action* honest. What that verification does **not** check is whether the goal the loop is serving is still the right goal. The inner loop verifies "did this action succeed"; nothing verifies "is this still the work we should be doing." That second question is the **Orient** step, and an unattended loop with no instrument that re-asks it has a strong Act leg driving on a stale Orient.

Goal-drift is the canonical symptom and it is *emergent with no error code* — there is no exception, no failing test, no red badge, because every individual action is succeeding. The only thing that catches it is restating the goal and re-deriving whether current work still serves it; log-monitoring never will. (This is the same finding project1's question-quality cadence is built on — see the prior art below.) So a project that has scheduled/looping primitives but no intent/question-quality RETHINK step is the precise pathology this doc names `loop-without-rethink`: the machinery to act unattended is present, the machinery to re-check the *aim* is absent.

The corollary is that running this instrument is cheap insurance exactly when the project is most autonomous. The more of the Act leg is delegated to loops, the more load the Orient step has to carry, and the less likely a human is watching the moment the goal quietly stops being served.

## The portable intent question bank

Nine project-agnostic "why" questions, generalized from the 16 Fable prompts the self-audit applied to this repo. For each: what it asks, how to detect a project has never answered it, a **re-ask cadence**, a **decay rule** (when the last answer goes stale and must be re-derived rather than recalled), and a **promotion rule** (when a repeated answer has earned the right to become a standing policy the project enforces rather than a question it keeps re-asking).

Cadences are advisory defaults, not hard schedules — tune them to how fast the project changes. The decay rules matter more than the cadences: a calendar tick with no decay trigger becomes a freshness stamp nobody acts on. Re-derive from the current state of the project, never recall last cycle's answer, or the instrument becomes theatre.

### Q1 — Goal (Fable #1)

**Asks**: What is this project *for*, in one sentence, and does the current mechanism serve that and only that? **Never-answered detection**: no charter/`THESIS`/`README` goal line, or the goal stated incompatibly across surfaces (the self-audit found three different answers across `README`/`ARCHITECTURE.md`/`package.json`). **Re-ask cadence**: quarterly, and on any major reposition. **Decay rule**: the answer is stale the moment a load-bearing file states a different goal than the canonical one, or a mechanism exists that the one-sentence goal doesn't explain. **Promotion rule**: once the one-sentence goal is stable across two cycles, promote it to a single canonical "what this is" line that every other surface defers to (a router/charter), so drift becomes a diff against one source instead of a judgment call. This is the `intent-undocumented` signal's remediation.

### Q2 — Self-model (Fable #3)

**Asks**: Does the project hold an accurate model of itself — its real size, layout, dependencies, and current phase? **Never-answered detection**: a self-describing doc (`ARCHITECTURE.md`, status doc) whose counts/URLs/versions contradict the live tree. **Re-ask cadence**: quarterly, plus on every structural change. **Decay rule**: stale as soon as a self-description's count or path no longer matches what's on disk — the self-audit's `ARCHITECTURE.md` claimed 26 docs against a 42-doc reality. **Promotion rule**: when a hand-maintained self-model has drifted twice, promote it to a *generated* surface (point the prose at an auto-regenerated `INDEX.md` rather than restating counts) so it can't drift a third time. Pairs with the existing `generated-docs-no-drift-gate` signal.

### Q3 — What "better" means (Fable #5)

**Asks**: How would the project know it is improving rather than just changing? What's the eval, and does anything model-free check the project's own output? **Never-answered detection**: no regression fixture, no golden-answer comparison, no eval harness for the artifact the project produces. **Re-ask cadence**: monthly, or whenever the core artifact's shape changes. **Decay rule**: stale once the project ships a change with no way to tell whether the change helped — the self-audit's expiry gate "passed" while verifying nothing, which is worse than no eval because it reads as a healthy signal. **Promotion rule**: when the same quality check is run by hand twice, promote it to a committed deterministic fixture (model-free where possible) and wire it into the merge gate, so "is it better" stops being a recurring judgment and becomes a blocking check.

### Q4 — Autonomy boundary (Fable #6)

**Asks**: How much is the project allowed to do unattended, and is each granted capability on the rung it should be (read-only / escalate-to-human / write-scoped / fully autonomous)? **Never-answered detection**: a `contents: write` CI agent, a no-permission-prompt cloud Routine, or a Desktop task that commits against uncommitted state, with no recorded decision that it *should* hold that rung. **Re-ask cadence**: quarterly, and on any new scheduled/looping primitive. **Decay rule**: stale the moment a mechanism sits a rung higher than its job needs — the self-audit found a tracker-generating workflow holding `contents: write` while building from an empty scan. **Promotion rule**: once the right rung for a class of work is decided twice the same way, promote it to a standing policy (the budget-ceiling-as-blast-radius rule, an `--allowedTools` allowlist, an author-association gate) enforced in config rather than re-litigated. This is where the [`safety-and-sandboxing.md`](safety-and-sandboxing.md) blast-radius controls attach.

### Q5 — Where most wrong (Fable #10)

**Asks**: If one current belief or mechanism is wrong, which is it most likely to be, and what would show it? **Never-answered detection**: no stated falsifier anywhere — no "this claim is wrong if…", no gap statements on the load-bearing claims. **Re-ask cadence**: monthly. **Decay rule**: stale once the project's most-load-bearing claim has gone a cycle with no attempt to break it; corroboration is not the same as a falsification attempt, and a string of confirmations should *lower* confidence that the question is still being asked honestly. **Promotion rule**: when a "where am I most wrong" answer recurs, promote it to an explicit Gap statement (per [CANONICAL-DOC-TEMPLATE.md](CANONICAL-DOC-TEMPLATE.md)'s Gap format) with a named test that would close it, so the soft worry becomes a tracked, falsifiable item.

### Q6 — The one constraint (Fable #13)

**Asks**: What single thing most limits the project's usefulness right now — the one bottleneck whose fix dominates everything else? **Never-answered detection**: a backlog with no ranking, or polish-work proceeding while the dominant constraint is untouched. **Re-ask cadence**: monthly, or whenever a major piece of work lands (the constraint usually moves when you fix it). **Decay rule**: stale the moment work is flowing to anything other than the named constraint — the self-audit named "the audit has never been run end-to-end" as the one constraint, and every doc-count or license fix is downstream of it. **Promotion rule**: when the same constraint survives two cycles unaddressed, promote it from a noted gap to the project's single highest-priority committed item with an owner, so "the one thing" can't keep losing to easier work.

### Q7 — What compounds (Fable #4 — memory that compounds)

**Asks**: Does the project's knowledge accumulate, or is each session/cycle starting from scratch? Is there typed, durable memory, and is it retrievable? **Never-answered detection**: no progress/decision log, no memory file, *or* — the sharper case — typed memory (`type:` frontmatter across notes) with **no canonical type registry and no drift guard**, which lets the type vocabulary sprawl until retrieval stops working (one production vault reached 127 distinct types, 86 used once; project1's own `_type-registry.md` was created after exactly this finding). **Re-ask cadence**: quarterly, and whenever the corpus grows past a scale band. **Decay rule**: stale once new knowledge is being written in a shape the existing memory can't retrieve — untyped, unregistered, or unlinked. **Promotion rule**: when an ad-hoc type or note-shape recurs, promote it into the registry (one line + rationale) *before* using it, so the registry stays the inventory instead of drifting behind the corpus. This is the `typed-memory-no-registry` signal — the OKF hygiene pattern — and it routes to [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) §A1b for the registry + pre-commit-guard + coverage-metric remediation.

### Q8 — Decisions → policy (Fable #12)

**Asks**: When the project makes the same call repeatedly, does that decision get promoted into an enforced policy, or is it re-decided by whoever happens to be present? **Never-answered detection**: no `DECISIONS.md`/append-only log, or a log that records decisions but never graduates the recurring ones into hooks/config/gates. **Re-ask cadence**: quarterly. **Decay rule**: stale once a decision has been made the same way three times and still lives only in someone's head or in prose advice (which has ~80% adherence, not 100% — [`behavioral-insights.md`](behavioral-insights.md)). **Promotion rule** — this question *is* the promotion mechanism for every other question in the bank: a thrice-repeated decision graduates from advisory prose (CLAUDE.md) to mechanical enforcement (a hook, a CI gate, a settings invariant) so it holds at 100% regardless of who's driving. The whole bank's promotion rules feed this one.

### Q9 — Bus-factor (Fable #14)

**Asks**: If the one person who holds the project's working model stepped away, what breaks first — and is the correctness of any load-bearing mechanism resting on a human remembering a checklist? **Never-answered detection**: an invariant maintained by hand across many files (the self-audit's signal→doc sync, six manual steps per new doc) with no linter enforcing it; tribal knowledge with no written form. **Re-ask cadence**: quarterly. **Decay rule**: stale the moment a hand-maintained invariant grows past what one person reliably remembers — and it grows silently, so the cadence tick is the only thing that surfaces it. **Promotion rule**: when a manual checklist is followed twice, promote the deterministic part of it to a linter/CI gate (the self-audit's highest-leverage single change was committing the documented-but-unwritten sync linter), moving correctness from "the maintainer remembers" to "the merge blocks." Bus-factor reduction *is* the promotion of memory-held invariants into enforced ones.

The four Fable prompts not in the bank are intentionally out of scope: #2 (bitter-lesson) and #8 (attack-surface) are already covered as full analysis docs ([`harness-engineering.md`](harness-engineering.md)'s Bitter-Lesson section, [`safety-and-sandboxing.md`](safety-and-sandboxing.md)); #9 (big-picture/ikigai) folds into Q1; #15 (dev-loop) and #16 (content-consolidation) are surface-coherence checks the presence-based audit already routes. The bank is the **intent** subset, the questions a grep can't answer.

## Prior art: project1's Coaching-Kata cadence (reuse, don't reinvent)

This instrument is modeled directly on a discipline already running in production, not invented here. project1's `karen-evaluator` skill carries a **question-quality audit** workflow (`/home/jerem/project1/.claude/skills/karen-evaluator/workflows/question-quality-audit.md`) that runs *monthly, or when ≥5 benches have landed since the last run* and asks "the outer-loop question the inner loop never asks itself — are these the right questions, and is test→asset→rethink actually compounding?" It is explicitly the cadence-driven sibling of an event-driven `reprioritization-check.md` in the same skill, and it instruments question quality **separately** from throughput because "a robust inner loop" (benches landing, commits flowing) masks "a healthy outer loop" (the questions are still the right ones).

Its core mechanism is the **five Coaching-Kata questions**, run as a scripted pass rather than prose:

1. **Target condition** — what does a healthy state look like?
2. **Actual condition** — where is it now (re-derived from the current filesystem, not recalled)?
3. **Obstacles** — what's blocking the gap, and which *one* are we addressing this cycle?
4. **Next step** — the single highest-leverage thing to attack next, and what we expect.
5. **What we'll learn / by when** — the falsifiable outcome and the cadence checkpoint.

Two of its house rules transfer directly and are the reason the cadences above lean on decay rather than the calendar. First, **re-derive, don't recall** — "Don't recall last month's grid — re-derive, or the instrument becomes theatre (a freshness stamp nobody updates)." Second, **corroboration is not progress** — "17 inbox clusters that 'changed no priorities' is the warning sign, not a clean portfolio." Both rules exist because goal-drift has no error code and only restating the goal catches it; that is the same justification the strong-Act/stale-Orient section gives above. The nine-question bank here is the project-agnostic generalization of that five-question pass: the Coaching-Kata five are the *running* shape, and the Fable-derived nine are the *intent dimensions* a portable version should cover across any project, not just a benchmark portfolio.

## Wiring it as a recurring tick

The instrument is only useful if it *fires* on a cadence rather than waiting for a human to think to ask. The scheduling machinery already exists and is documented in [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md) — pick the rung that matches how autonomous the project is:

- A **cloud Routine** (`/schedule`, 1-hour minimum) for a project that runs largely unattended — the RETHINK step runs server-side on the same cadence as the work it's checking.
- A **Desktop scheduled task** that starts a fresh session monthly to run the question bank against the current tree — fresh context is a feature here, since the point is to re-derive, not recall.
- A `/loop` with a long interval, or simply a calendar reminder, for a project where a human is still in the cadence.

Whatever the rung, the tick should produce the same shape as project1's instrument: re-derive the actual condition from the current filesystem, run the scripted question pass, diff against the last recorded answers, and **emit any drift as a signal**, not a freshness stamp. A finding that warrants a priority shift (a constraint that survived another cycle, a mechanism a rung above its job, a memory shape the registry can't retrieve) becomes a tracked item with an owner, the same way the question-quality audit writes to a loop-start surface that the prioritization loop reads.

The one rule that makes this not-theatre: the tick that finds nothing is a finding too. A run that "changed no priorities" cycle after cycle is the corroboration-is-not-progress warning, not a clean bill of health — it usually means the instrument is recalling instead of re-deriving. The cadence catches drift only if each run genuinely re-derives the answers from scratch.

## Counter-Evidence / What This Does *Not* Mean

This is not a claim that intent questions should replace the presence-based audit — they sit on top of it. The signal-routing audit is the right tool for "which conventions is this project missing," and most of its value is there; the intent pass only earns its place on the load-bearing mechanisms, not every file. Running the full nine-question bank against a throwaway script is the same over-engineering the harness docs warn against.

It is also not a claim that more cadence is better. A RETHINK tick that fires too often, or that recalls instead of re-derives, degrades into the freshness-stamp failure mode the prior-art doc names explicitly — and an instrument nobody acts on is worse than none, because it reads as coverage. The decay rules, not the cadences, are what make the instrument honest; a project with slow change should re-ask slowly and lean entirely on the decay triggers.

Finally, the strong-Act/stale-Orient framing is a diagnosis, not a measurement. There is no published figure for how often unattended loops drift off-goal, because goal-drift has no error code to count — the evidence is the self-audit's own finding that a presence-based audit missed exactly this class on this repo (Tier B, single observation), plus the convergent design of project1's question-quality cadence. Treat the pathology as a named risk to instrument against, not a quantified base rate.

## Gaps

- **Gap: drift-catch rate unmeasured.** This instrument is justified by reuse (project1's running cadence) and by the self-audit's finding that presence-based auditing missed intent-drift on this repo — not by a measured rate of drift caught versus missed on external projects. **Needs**: the instrument run on its own cadence against ≥2 external projects, recording which findings a presence-based audit would have missed, to upgrade from "structurally sound by analogy" to a measured catch rate.
- **Gap: cadence/decay calibration.** The re-ask cadences (monthly/quarterly) are inherited from project1's question-quality audit and the harness revalidation defaults, not derived for the general case. **Needs**: evidence on how cadence interacts with project change-rate — a fast-moving project may need monthly on every question; a stable one may decay almost entirely on triggers with no calendar tick.
- **Gap: signal detection is partial by construction.** Three of the four declared signals are greppable for *absence* (`intent-undocumented`, `typed-memory-no-registry`) but `goal-drift-unmeasured` and `loop-without-rethink` are *absence-of-an-instrument* signals — like the cloud-Routine blind spot in [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md), you can detect that scheduling primitives are present and a RETHINK step is not, but you cannot prove a pure-cloud RETHINK Routine isn't running off-disk. **Needs**: phrase these findings "verify" and ask the operator, exactly as the cloud-Routine and generated-docs-drift signals already do.

## Related Analysis

- [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md) — the fire-on-a-cadence machinery this instrument runs on, and the operational risk of an unattended loop with no RETHINK step.
- [`harness-engineering.md`](harness-engineering.md) — the inner-loop anchor; its diagnostic table asks "what's wrong with my harness," this doc asks the orthogonal "is it still the right harness for the goal."
- [`safety-and-sandboxing.md`](safety-and-sandboxing.md) — the blast-radius controls the autonomy-boundary question (Q4) attaches to.
- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — §A1b, the typed-memory registry + drift-guard remediation the what-compounds question (Q7) routes to.
- [`evidence-based-revalidation.md`](evidence-based-revalidation.md) — the claim-half-life discipline the decay rules generalize from facts to intent.
- [CANONICAL-DOC-TEMPLATE.md](CANONICAL-DOC-TEMPLATE.md) — the Gap-statement format the where-most-wrong question (Q5) promotes answers into.

## Sources

### Tier A (Primary / Vendor)

- Anthropic Claude Code docs: ["Run prompts on a schedule"](https://code.claude.com/docs/en/scheduled-tasks) — the `/loop` / `/schedule` / Desktop-scheduled-task primitives this instrument can be wired onto. (Detail and currency carried by [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md), Tier A.)

### Tier B (Validated / Expert Practitioner)

- Daniel Miessler — the 16 "Fable" intent prompts, applied to this repo across the six self-audit lenses (`research/self-audit-2026-06/lens-1`…`lens-6`, 2026-06-21). The nine-question bank is the project-agnostic generalization of the intent subset (#1, #3, #4, #5, #6, #10, #12, #13, #14).
- project1 `karen-evaluator` skill — `/home/jerem/project1/.claude/skills/karen-evaluator/workflows/question-quality-audit.md` — the running Coaching-Kata cadence (monthly / ≥5-benches, re-derive-don't-recall, corroboration-is-not-progress) this instrument is modeled on; its sibling `reprioritization-check.md` is the event-driven counterpart. Prior art, reused not reinvented.
- Andrej Karpathy — ["Sequoia Ascent 2026"](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (2026-04-30) — coding's built-in verification keeps each *action* of an unattended loop honest; the gap it does not close (is the goal still right) is the Orient step this instrument supplies.
- John Boyd's OODA loop — the strong-Act / stale-Orient framing for an unattended loop with no RETHINK step. Conceptual framing, not a measured result.

### Tier C (Community)

- The "loop engineering" commentary cloud (June 2026) is attributed and bias-flagged in [`scheduled-and-looping-primitives.md`](scheduled-and-looping-primitives.md); this doc relies on the primary primitives, not the commentary.

---

*Last updated: 2026-06-21 (new EMERGING doc — the intent/"why" RETHINK layer the presence-based audit lacked; nine-question portable bank generalized from the 16 Fable prompts, modeled on project1's running Coaching-Kata question-quality cadence; four new signals declared: `intent-undocumented`, `goal-drift-unmeasured`, `loop-without-rethink`, `typed-memory-no-registry`).*
