---
evidence-tier: Mixed
measurement-claims:
  - claim: "Fable 5 in-harness probe (n=3/condition, effort medium): vague-descriptor and edge-case anti-patterns SOFTENED vs 4.7 expectation (4/5 and 3/4 target behaviors produced unprompted); adaptive verbosity present (~10x complex/simple, ~37% concision-directive cut)"
    source: "Controlled 64-agent probe session, this repo — raw record research/fable-probe-session-2026-07-16.md"
    date: "2026-07-16"
    revalidate: "2027-01-16"
  - claim: "Fable 5 in-harness soft-guideline literalization (effort medium, 4 audience-addressed genres, n=9/arm): emphatic MAX-3 cap on 'you' satisfied with large margin in all 9 reps (bare-'you' mean 1.0, max 2) and second-person family suppressed ~13x below baseline; advisory phrasing mean 2.67 with one exceedance; rank-sum on the pre-registered family metric p≈0.001 one-sided"
    source: "Round-two re-instrumented probe after adversarial refutation of round one — raw record research/fable-probe-session-2026-07-16.md"
    date: "2026-07-16"
    revalidate: "2027-01-16"
  - claim: "Fable 5 in-harness implicit-dispatch propensity (session effort xhigh, n=3/arm, small read-only task list): implicit phrasing produced 0/3 dispatch attempts with delegation demonstrably available on the same spawn path (explicit arm 9/9 telemetry-confirmed dispatches)"
    source: "Round-two re-instrumented probe (main-loop spawn path + transcript telemetry) — raw record research/fable-probe-session-2026-07-16.md"
    date: "2026-07-16"
    revalidate: "2027-01-16"
convergence: emerging  # ruled 2026-07-16: two independent external exemplars recorded in-doc — Willison per-release behavioral analyses + Vertrees audit framework (Vertrees provenance-only per the 2026-07-10 SOURCES pass: guidance stale, adoption evidence valid)
applies-to-signals: [model-version-fable-mythos, model-version-4-8, model-version-4-7, model-version-4-6, model-version-4-5, model-version-migration, model-version-unknown, claude-md-vague-descriptors, claude-md-emphatic-constraints]
last-verified: 2026-05-30
revalidate-by: 2026-11-30
status: PRODUCTION
---

# Model Migration Anti-Patterns

**Evidence Tier**: Mixed (A-B) — Anthropic migration guides + system cards (Tier A) + practitioner commentary (Tier B) + community observation (Tier C counter-signals)

## Purpose

This document is a **diagnostic checklist**, not a migration how-to. When a new Claude model ships, prompts and harnesses validated on the prior version can silently regress. The anti-patterns below map each failure mode to the model version that introduced or exacerbated it, the Tier A evidence, and a specific remediation.

The framing answers: *"Which of my existing prompts are likely to break, and why?"*

> **Currency note (2026-05-30)**: Opus 4.8 shipped 2026-05-28 (model ID `claude-opus-4-8`; the `[1m]` suffix is the 1M-context variant — 1M context is default on the Claude API, Bedrock, and Vertex, 200k on Microsoft Foundry). 4.8 is largely a *recovery* release relative to the 4.7 regressions catalogued below: better tool-triggering, better compaction/long-context recovery. The literal-interpretation posture from 4.7 carries forward — the six prompt anti-patterns below still apply — so this doc remains the migration checklist for 4.7→4.8 as well. See the [4.8 row in the matrix](#cross-version-anti-pattern-matrix) and the [4.8 behavioral deltas](#opus-48-net-deltas-vs-47-tier-a) section. Source: [What's New Claude 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8), [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) (Tier A, fetched 2026-05-30).
>
> **Currency note (2026-07-10, Fable-era delta)**: Claude Fable 5 / Mythos 5 (Mythos-class, above Opus; model ID `claude-fable-5`) released 2026-06-09, was suspended worldwide 2026-06-12 under a US export-control directive, and was **redeployed 2026-07-01** — it is back in production (this refresh ran on `claude-fable-5`), so a `fable` model pin is valid again and Fable is a legitimate migration target alongside Opus 4.8. Harness-relevant changes that shipped with or around the Fable cycle, each a checklist item for projects migrating from 4.x: adaptive thinking replaced fixed thinking budgets (v2.1.170) — prompts that set explicit thinking-budget parameters should drop them; Sonnet 5 became the default model (v2.1.197) — projects relying on an implicit default now get Sonnet 5, so pin explicitly if a different tier is assumed; the `[1m]` model-ID suffix is auto-stripped (v2.1.205) — suffix-pinned IDs no longer break but no longer select a variant either; and the permission mode formerly surfaced as "default" was renamed **Manual** (v2.1.200) — settings or docs that reference the old name should update. Bundled `/claude-api` now carries first-party migration guidance; this checklist stays the repo-side complement that audits *your* prompts. Source: [Claude Fable 5 / Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) (Tier A) + Claude Code changelog (Tier A; verified 2026-07-09 sweep).

---

## The Silent No-Op Problem

Opus 4.7's headline behavioral change is **literal instruction interpretation**. The Anthropic migration guide states, verbatim:

> "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make."
>
> — [Anthropic Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)

The practical consequence: prompts that worked on 4.6 because the model *helpfully inferred intent* now produce silent no-ops on 4.7. The prompt appears valid, the model returns a plausible response, but the actual instruction is never executed.

**This is not a "hot take."** Jason Vertrees's widely-shared [LinkedIn piece](https://www.linkedin.com/pulse/claude-47-quietly-break-your-prompts-harness-heres-how-jason-vertrees-mscpe/) operationalized this advisory into six anti-patterns. His contribution is the audit framework; the underlying claim is Anthropic's own.

---

## Cross-Version Anti-Pattern Matrix

| Anti-pattern | 4.5 | 4.6 | 4.7 | 4.8 | Primary source |
|---|---|---|---|---|---|
| Vague quality descriptors ("best practices," "idiomatic," "robust") | Tolerated | Tolerated | **Silent no-op** | Silent no-op (carries forward) | Anthropic migration guide |
| Edge-case gestures ("consider edge cases," "handle corner cases") | Works | Works | **Silent no-op** — model no longer infers *which* cases | Silent no-op (carries forward) | Anthropic migration guide |
| Unanchored triggers ("where applicable," "as needed," "if relevant") | Works | Works | **Silent no-op** — conditions never fire | Silent no-op (carries forward) | Anthropic migration guide |
| Implicit subagent dispatch ("execute the tasks," "dispatch the work") | Spawns liberally | Spawns liberally | **Fewer subagents by default** — dispatch must be explicit | Explicit dispatch still required | Anthropic migration guide (verbatim: "Fewer subagents spawned by default. Steerable through prompting.") |
| Missing verbosity directives (no length caps, no "no preamble") | Fixed default verbosity | Fixed default verbosity | **Adaptive verbosity** — response length calibrates to perceived complexity; add `"Provide concise, focused responses..."` | Adaptive verbosity (carries forward) | Anthropic migration guide |
| References without read-enforcement ("see rules/data-isolation.md for restrictions") | Often read | Often read | **Frequently not read** — mechanical enforcement required | **Better, not solved** — 4.8 "less likely to skip a required tool call," but enforce mechanically for 100% | Anthropic migration guide + [progressive-disclosure analysis](claude-md-progressive-disclosure.md) + [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) |
| Skipped required tool calls (model answers without calling the tool the task needs) | n/a | Occasional | **Reported issue** — users flagged tool calls being skipped on 4.7 | **Improved** — "less likely to skip a tool call the task required" | [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) |
| Extended-thinking token budgets (`thinking: {budget_tokens: N}`) | Supported | Supported | **400 error** — adaptive-only | **400 error** — adaptive is the *only* thinking mode; use `effort` (default `high`) | [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) |
| Soft-guideline / emphatic-constraint overcorrection (see [first-class anti-pattern below](#first-class-anti-pattern-soft-guideline-literalization)) | Mild | Mild | **Pronounced** — "MUST"/"max"/"ALWAYS" hard-capped literally | Pronounced (carries forward) | Practitioner observation (Tier B) + bias-overcorrection / over-refusal (Tier A, card) |

**Anti-patterns adapted from Vertrees (LinkedIn, April 2026). Version-severity columns are our own cross-reference to the Tier A migration guides and system cards.**

**Fable 5 (probed 2026-07-16, Tier B)**: the matrix keeps its Tier-A columns as-is, but five rows now have direct Fable measurements — the vague-descriptor and edge-case rows are *softened* on Fable (most target behaviors appear unprompted; explicit type-validation and resource limits still need enumeration), adaptive verbosity carries forward, implicit dispatch stays explicit-required (zero attempts with delegation demonstrably available), and emphatic-soft-cap over-enforcement is now supported by a controlled probe. See [Fable 5 probe measurements](#fable-5-probe-measurements-2026-07-16-tier-b--self-measured) for what was established, what was voided, and why.

---

## Opus 4.8 Net Deltas vs 4.7 (Tier A)

Opus 4.8 (2026-05-28) is a *recovery and calibration* release, not a posture shift. The literal-interpretation behavior introduced in 4.7 carries forward; what changed is reliability. From the [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) (Tier A, verbatim where quoted):

| Delta | What changed | Migration implication |
|---|---|---|
| **Better tool triggering** | "Less likely to skip a tool call the task required, an issue some users reported on Claude Opus 4.7." | The 4.7 "references without read-enforcement" failure mode is *softened* — but not eliminated. Keep mechanical enforcement (PreToolUse hook, explicit Read step) for 100%-adherence requirements; the model-side improvement is a reduction in frequency, not a guarantee. |
| **Better compaction handling and long-context quality** | "Long agentic traces stay on task with fewer derailments after compaction," plus "fewer compactions." | Long-running agentic harnesses can lean less on aggressive document-and-clear discipline (see [Harness Engineering](harness-engineering.md)). Re-test compaction-timing heuristics tuned on 4.7. |
| **Adaptive thinking is the only thinking mode** | "Setting `thinking: {type: enabled, budget_tokens: N}` returns a 400 error." Default `effort` is `high` on all surfaces (API and Claude Code). Adaptive existed on 4.7; 4.8's delta is per-turn efficiency/calibration ("fewer wasted thinking tokens at the same effort level"). | Any harness still passing `budget_tokens` will hard-fail with a 400. Migrate to `thinking: {type: "adaptive"}` + `effort` (`low`/`medium`/`high`/`xhigh`). This is the one *breaking* change in the set — the rest are behavioral, not API-breaking. |
| **Reasoning-effort calibration** | "More reliable behavior at each effort level across a range of domains." | The HN 47793411 "adaptive thinking under-triggers on reasoning-heavy tasks" counter-signal (4.7) may be partially addressed; re-test before relying on the `xhigh` workaround. |

**New first-class 4.8 behavioral caveat — grader-awareness / eval-speculation.** The Opus 4.8 system card flags a "growing tendency toward speculation about graders / reasoning about how outputs will be assessed" as the *most concerning trend observed during 4.8 training*, with only modest behavioral effects at deployment. For harness designers this matters because eval-driven workflows (rubric-scored evaluator agents, [agent-evaluation.md](agent-evaluation.md)) may interact with a model that reasons about *how it is being scored* rather than purely about the task. It does not invalidate evaluator-agent patterns, but it is a reason to keep rubrics implicit to the gradee where feasible and to watch for grader-gaming in long agentic traces. Source: [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) (Tier A). Behavioral effect is described as modest; treat as a watch-item, not a settled regression.

---

## Fable 5 Probe Measurements (2026-07-16, Tier B — self-measured)

The 4.7-era rows above rested on Anthropic's own migration advisory; the Fable currency note carried them forward by inference. This section replaces that inference with measurement where a probe could be built honestly, and records the probes that failed their own controls, because a voided probe with a known failure mode is worth more to the next re-runner than a silently dropped one.

**Method**: a 64-agent controlled session on `claude-fable-5` inside the Claude Code harness — paired vague-vs-explicit prompt conditions, 3 reps per condition, all probes at `effort: medium`, mechanical scoring where the dependent variable allowed it and LLM judges for behavior-presence counts in code, with every candidate finding passed through a three-lens adversarial verification (overclaim, method-confound, data-consistency) instructed to refute by default. Because the probes ran as subagents they inherit the harness system prompt and the user's global CLAUDE.md, so every result characterizes *Fable-in-harness* — which is the ecologically relevant measurand for this checklist, but not the bare model. Two probes voided in round one were re-instrumented and re-run the same day (dispatch on a spawn path where the positive control passes; literalization on an unlegislated token with a baseline arm and a 3-genre extension specified by the confound verifier), and their round-two findings were verified through the same default-refute process before entering the table above. Raw distributions and the full verification trail: [research/fable-probe-session-2026-07-16.md](../research/fable-probe-session-2026-07-16.md).

### Established (survived all three lenses)

| Anti-pattern | Fable result (in-harness, n=3) | vs 4.7 expectation |
|---|---|---|
| Vague quality descriptors | "Follow best practices / robust, clean code" produced 4 of 5 enumerated target behaviors at 3/3 unprompted (clear missing-file error, pathlib, type hints, invalid-JSON handling); the one 0/3 gap was explicit runtime path/type validation, which the explicit condition produced 3/3 — so the probe demonstrably separates conditions | **Softened** — vague asks are mostly expanded; genuine invariants (type checks) still need enumeration |
| Edge-case gestures | "Consider edge cases" handled empty string 3/3, None 3/3, unicode 2/3 — but produced no oversize-line/resource-limit handling in any rep (0/3 vs 3/3 enumerated) | **Softened, with a residual** — common defensive cases appear unprompted; *resource limits still require explicit enumeration* |
| Missing verbosity directives | Complex-topic answers ran ~10x simple ones without a directive (means ~693 vs ~69 words, ranges non-overlapping); "Provide concise, focused responses" cut complex answers ~37% | **Carries forward** — adaptive verbosity is present and the standard directive works; keep it |
| Implicit subagent dispatch (round-two instrument) | With delegation demonstrably available on the same spawn path (explicit arm: 9/9 successful telemetry-confirmed dispatches, no other tools), implicit phrasing ("execute the tasks") produced zero dispatch attempts in 3/3, executing inline — a default-choice propensity, not a capability limit; at this task scale inline is also the economically rational choice, so the probe cannot fully separate a default-posture explanation from a task-economics one | **Consistent with the 4.7 posture** — explicit dispatch still required (n=3/arm; these probes ran at session effort xhigh, unlike the medium-effort probes above) |
| Soft-guideline literalization (round-two instrument; see the [first-class section below](#first-class-anti-pattern-soft-guideline-literalization)) | Pooled n=9/arm across 4 audience-addressed genres: an emphatic MAX-3 cap on the word "you" was satisfied with large margin in all 9 reps (bare-"you" mean 1.0, never reaching the allowed 3) and suppressed the whole second-person family ~13x below baseline (mean 1.78 vs 22.6) though the rule named only one word; advisory phrasing of the same number produced mean 2.67 with one rep exceeding it; rank-sum on the pre-registered family metric p≈0.001 one-sided | **Supported** — emphatic syntax over-enforced beyond both letter and intent; advisory syntax treated as directional (Fable 5, in-harness, effort medium) |

The practical upshot for a 4.x→Fable migration audit: the grep-for-vague-descriptors steps below remain worth running, but on Fable the highest-yield targets narrow to *invariant-class* instructions (type validation, resource limits, compliance boundaries) rather than quality vocabulary generally, because Fable fills in the conventional quality behaviors unprompted at least in-harness, where the harness prompt may itself supply some of that expansion.

### Voided probes (recorded so the next attempt fixes the instrument, not the conclusion)

Round one voided four probes; two were re-instrumented and measured the same day (their findings now sit in the Established table above), which is exactly what this section is for.

- **Implicit subagent dispatch** — round-one void: the explicit-dispatch positive control also executed inline 3/3, and transcript telemetry traced the mechanism to tool availability (the workflow-spawned probes had no Agent tool — their explicit arms ran a failed ToolSearch for it). Re-instrumented same-day on the main-loop spawn path, where the control passes (9/9 dispatches); finding in the table above. Method note: Agent-tool availability differed by spawn path in this session (absent for workflow-spawned general-purpose subagents, present for main-loop-spawned ones); whether that is a fixed harness property is untested beyond this session — dispatch probes must use a spawn path where the positive control passes.
- **Soft-guideline literalization** — round-one void: contaminated dependent variable (the inherited global CLAUDE.md legislates the em-dash rate the probe measured). Re-instrumented same-day on an unlegislated token ("you" in audience-addressed copy) with a no-rule baseline arm, then extended to 4 genres / n=9 per arm on the confound verifier's spec; finding in the table above and in the first-class section below.
- **References without read-enforcement** — re-instrumented in a final round with transcript telemetry (counting actual Read calls on the fixture, replacing the failed token proxy): the reference-only arm read the fixture 4/4 without enforcement. Recorded as *descriptive only*, not a graded softening — the pair saturated (the explicit-Read arm was also 4/4, so zero within-study contrast), the 4.7-era "frequently not read" baseline is not methodologically commensurable, and a harness that generically reads visible absolute paths is an unexcluded mechanism. The 4.7-era row keeps its Tier-A basis and the mechanical-enforcement remediation stands. A graded re-run needs a condition expected to produce <4/4 (relative or buried references).
- **Unanchored triggers** — re-instrumented in a final round with a calibration stage (all four candidate behaviors confirmed absent at 0/3 baseline; timing selected): "add execution-time instrumentation where applicable" fired in 3/3 reps, instrumenting all three functions via a decorator, against the 0/3 baseline. Also *descriptive only* — the initial occurrence-count difference between arms proved to be a regex artifact (decorator telemetry shows both arms instrumented exactly 3 functions), with no demonstrably inapplicable site in the fixture "where applicable" may act as a plain instruction, and one behavior on one task cannot grade the 4.7 expectation. A graded re-run needs applicability heterogeneity in the fixture, distinct-site counting, and a second candidate behavior.
- **Context-fill retrieval** (attempted for the 60%-threshold gap) — the 2026-07-16 environmental void (harness safety classifier blocked all 9 probes on machine-generated filler) was SUPERSEDED by a 2026-07-17 fresh-session re-run on naturalistic repo-prose filler: the instrument now executes end-to-end (de-blocking factor unattributable between fresh session and filler change). The re-run also caught a **silent model fallback**: all workflow-spawned reading agents were served Opus 4.8 while requested-model fields showed Fable — voided as a Fable measurement and re-run same-day on the main-loop spawn path with per-turn served-model gating (new instrument rule: gate scoring on `message.model` per turn; run on a spawn path where a served-model control passes). Gated Fable result, descriptive ceiling only: 10/10 salient template-flagged facts retrieved at every depth (5–95%) through ~140k tokens (chars/4 estimate) of tool-result fill in every gated rep (R40 3/3, R100 2/2, R140 3/3; endpoints anchored 0/10 no-read, 10/10 low-fill) — easiest retrieval regime, no rung produced <10/10, window-fraction denominator unknown, so the 60%-threshold gap stays open. Full data + verification trail: [research/fable-probe-session-2026-07-16.md](../research/fable-probe-session-2026-07-16.md) (2026-07-17 addendum).

**Scope caveats on everything above**: n=3 per condition, one effort level (medium — the 4.7 advisory says literalism is strongest at *lower* effort, which this design did not vary), in-harness measurand, self-measured. These are observed-in-practice Tier B rows in the same category as the soft-guideline claim this doc already carries; none of them alters the Tier-A 4.7/4.8 rows.

---

## First-Class Anti-Pattern: Soft-Guideline Literalization

Promoted to a named anti-pattern as of 2026-05-30. 4.7 introduced it; 4.8 carries it forward. As of 2026-07-16 the claim carries controlled-probe support on Fable, not anecdote alone: a first probe attempt was voided by a contaminated dependent variable, and the same-day re-instrumented probe (unlegislated token, no-rule baseline arm, 4 audience-addressed genres, n=9/arm, effort medium, in-harness, Tier B self-measured) found the emphatic MAX-3 cap satisfied with large margin in every rep — bare-"you" never reached the allowed 3 — while the whole second-person family was suppressed ~13x below baseline although the rule named a single word, and advisory phrasing of the same number was treated as directional (mean 2.67, one rep exceeding it); rank-sum on the pre-registered family metric p≈0.001 one-sided. Full data and verification trail: [research/fable-probe-session-2026-07-16.md](../research/fable-probe-session-2026-07-16.md). The failure mode: **soft, advisory guidance written with emphatic syntax gets hard-capped or hard-enforced as if it were an invariant.** A house-style note like "cap em-dashes at ~1 per 200 words" or "keep responses concise (max 3 paragraphs)" is treated by the model as a compile-time assertion rather than a heuristic — the model over-restricts to satisfy the literal "max"/"MUST"/"ALWAYS," sometimes degrading output to honor a rule the author meant as directional.

**Dual attribution — read this carefully, the two halves are different tiers:**

| Component | Tier | Source | What is actually documented |
|---|---|---|---|
| Bias-overcorrection + over-refusal | **A** | Opus 4.7 system card | The card uses "overcorrection" in a *bias* context (BBQ eval — overcorrecting to *avoid the appearance of* bias) and tracks **over-refusal** as a metric (4.7 has *fewer* over-refusals than 4.6). This is the card-documented, measurable behavior. |
| Soft-rule / emphatic-constraint hard-capping | **B** | Practitioner observation (this project's own usage, 2026; corroborated across Opus 4.7 / 4.8 sessions) | The "MUST"/"max" → hard-cap over-literalization is **observed-in-practice**, *not* named in any Anthropic card. Label it as such. It is consistent with — but not proven by — the Tier-A literal-interpretation posture. |

**Do not over-claim.** The card does not name "over-literalization of soft constraints." Asserting Anthropic documented it would be a tier inflation. The honest framing: 4.7's documented literal-interpretation shift (Tier A) is the plausible *mechanism*; the soft-rule hard-capping is a practitioner-observed *symptom* (Tier B). Both point to the same remediation.

**Remediation:**

- Write advisory guidance in advisory syntax. Reserve "MUST" / "NEVER" / hard numeric caps for genuine invariants (secrets handling, destructive operations, compliance boundaries). For heuristics, say "aim for," "prefer," "as a rule of thumb ~N," and state explicitly that the number is directional.
- If a soft rule keeps getting hard-enforced, that is a signal the syntax mismatches the intent — fix the syntax, don't add a counter-rule.
- This mirrors the broader [MUST/MUST NOT tension](#the-mustmust-not-tension): Anthropic prefers positive enumeration over negative absolutes, and over-literalization is the cost of emphatic negatives applied to non-invariant guidance.

---

## Remediation Patterns (and One Tension)

### Preferred remediation per anti-pattern

| Anti-pattern | Positive-framed fix | Why positive |
|---|---|---|
| Vague quality descriptors | Point to specific standards doc or enumerate 3-5 rules inline | Gives the model concrete targets to hit |
| Edge-case gestures | Enumerate the cases that matter ("handle: null, empty, unicode, >10MB") | Names the work |
| Unanchored triggers | State explicit firing conditions ("when the caller passes `strict=true`, validate…") | Converts inference to control flow |
| Implicit subagent dispatch | Declare mechanism: "Use the Explore subagent to..." or "complete in-context without subagents" | Matches 4.7's explicit-dispatch default |
| Missing verbosity directives | Add concision directive + output format template | Aligns with adaptive verbosity |
| Unread references | Enforce via PreToolUse hook, explicit `Read tool` step in the instruction, or required-reading block at the top of CLAUDE.md | Moves enforcement from inference to mechanics |

### The MUST/MUST NOT tension

Vertrees's audit prescribes "MUST / MUST NOT rules" as a primary remediation. **This conflicts with Anthropic's stated preference in the same migration guide:**

> "Positive examples... tend to be more effective than negative examples or instructions that tell the model what not to do."

**Diagnostic guidance for this repo:** prefer positive enumeration (what *to do*, with examples) over MUST NOT lists. Reserve MUST NOT for genuine safety/compliance constraints where the negative framing is load-bearing (secrets handling, destructive operations). This matches the broader [Harness Engineering](harness-engineering.md) principle that enforcement should live in mechanics (hooks, sandboxes), not in exhortation.

---

## What Literalism Does *Not* Mean

Literalism is **selective, not uniform**. Simon Willison's [analysis of the leaked 4.7 system prompt](https://simonwillison.net/2026/Apr/18/opus-system-prompt/) surfaces a counter-signal: Anthropic explicitly tuned 4.7 to be *less* literal about clarifying questions.

> "The person typically wants Claude to make a reasonable attempt now, not to be interviewed first."
> — Opus 4.7 system prompt (leaked)

**Implication for prompt design**: 4.7 won't generalize across instructions, but it *will* generalize across conversation-turn intent (e.g., "just start working"). Audits that treat literalism as uniform will over-correct.

---

## Community Counter-Signals (Tier C)

Practitioner reports from the Opus 4.7 release window surface failure modes not yet documented by Anthropic:

| Report | Source | Implication |
|---|---|---|
| "Adaptive thinking chooses to not think when it should" — workaround = `xhigh` + explicit thinking-summary config | [HN 47793411](https://news.ycombinator.com/item?id=47793411) (1,955 points) | Default effort calibration may under-trigger thinking on reasoning-heavy tasks |
| 4.7 over-applies system-reminder instructions (e.g., malware check) to *every* file read | [HN 47814832](https://news.ycombinator.com/item?id=47814832) | Red-teamers report "close to unusable" for certain workflows — literalism can over-fire on reminders |

Both are single-thread observations without independent validation. Track for broader corroboration before acting on them.

---

## Benchmarked Case Study: Long-Context Regression Is Real and Version-Specific (4.6 → 4.7)

The clearest evidence that a model upgrade can *regress* a capability — not just shift prompt idioms — is the multi-needle long-context retrieval drop between Opus 4.6 and 4.7. This is a 4.6→4.7 finding, **not** a 4.8 number; included here because it is the best-documented case of a benchmarked, version-specific regression and it calibrates how much to trust long-context behavior across upgrades.

On OpenAI's MRCR v2 (Multi-Round Co-Reference Resolution, 8-needle variant):

| Context length | Opus 4.6 | Opus 4.7 | Source |
|---|---|---|---|
| 1M tokens | 78.3% | **32.2%** | OpenAI MRCR v2, 8-needle |
| 256k tokens | 91.9% | **59.2%** | OpenAI MRCR v2, 8-needle |

**Citation discipline — these live in the 4.7 system card's *chart images***, not its body text, so the numeric transcription is third-party: [Context Arena](https://contextarena.ai) and the dev.to write-up "I read all 232 pages [of the Opus 4.7 system card]" both transcribe the same figures. Cite as *card chart (Tier A, image) + third-party transcription (Tier B)*, not as a quotable card sentence.

**Framing — trade-off, not "tokenizer broke it."** A single Tier-C blog conjectured a tokenizer change caused the drop. That is *one blog's hypothesis*, not Anthropic's position; present it only as attributed third-party conjecture, if at all. Anthropic's own framing is a deliberate trade-off: 4.6's 64k extended-thinking mode dominates 4.7 on multi-needle retrieval, and 4.7 gave that up for other gains. The honest takeaway is not "4.7 is broken" but "multi-needle retrieval at very long context is a capability that moved *down* across this upgrade, by design-adjacent trade-off."

**Why this matters for migration audits**: long-context retrieval is exactly the kind of capability a harness silently depends on (large-codebase analysis, long agentic traces, document-set reasoning). A model upgrade can regress it without any prompt or harness change. 4.8's [docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) claim "better long-context handling" and "fewer compactions" vs 4.7 (Tier A) — directionally a recovery — but no public MRCR-v2 figure for 4.8 has been transcribed yet. **Do not assume 4.8 restored the 4.6 numbers; re-benchmark multi-needle retrieval on 4.8 before relying on it.**

Sources: OpenAI MRCR v2 (benchmark); Opus 4.7 system card chart images (Tier A); Context Arena + dev.to "I read all 232 pages" (Tier B transcription); tokenizer-cause claim is a single Tier-C blog conjecture, not adopted here.

---

## Audit Workflow

For a repository migrating from 4.6 → 4.7:

1. **grep for vague descriptors** — `grep -nE "best practices|idiomatic|robust|proper|clean" prompts/ skills/ CLAUDE.md`
2. **grep for unanchored triggers** — `grep -nE "where applicable|as needed|if relevant|consider" prompts/ skills/`
3. **grep for references without enforcement** — find every `.md` cross-reference in CLAUDE.md/skills and verify each has (a) an explicit `Read` step, (b) a PreToolUse hook, or (c) a required-reading block.
4. **Identify implicit subagent dispatch** — search for "dispatch," "execute the tasks," "handle X, Y, Z" without naming an agent mechanism.
5. **Add a verbosity directive** — CLAUDE.md or top-level prompt gets: `"Provide concise, focused responses unless asked otherwise."`
6. **Run side-by-side** — same prompt on 4.6 and 4.7 via Claude Code CLI; diff outputs for silent no-ops.

This repo's own audit (performed 2026-04-22) surfaced 16 Opus 4.5/4.6 references in `analysis/` that need revalidation framing. Tracked in [Evidence-Based Revalidation](evidence-based-revalidation.md).

---

## Related Analysis

This doc is cited by (inbound) and cites (outbound) the following. Use the bidirectional links to pivot between version-behavior (here) and the specific practice affected.

**Outbound — docs this one draws on**:

- [Behavioral Insights](behavioral-insights.md#prompt-sensitivity-across-model-versions) — version-by-version prompt sensitivity table
- [Harness Engineering](harness-engineering.md) — 4.7 pushes *prompt* complexity up even as *harness* simplifies
- [CLAUDE.md Progressive Disclosure](claude-md-progressive-disclosure.md) — references-without-read-enforcement is the 4.7 failure mode that most affects progressive-disclosure
- [Evidence-Based Revalidation](evidence-based-revalidation.md) — model migrations are a canonical revalidation trigger
- [Agent Evaluation](agent-evaluation.md) — implicit subagent dispatch as an evaluation anti-pattern

**Inbound — docs that cite this one**:

- [Behavioral Insights](behavioral-insights.md) — links here for the MUST-vs-positive tension and the six failure modes
- [Harness Engineering](harness-engineering.md) — links here from its 4.7 counter-signal row
- [CLAUDE.md Progressive Disclosure](claude-md-progressive-disclosure.md) — links here from the Opus 4.7 references-without-read-enforcement warning
- [Agent Evaluation](agent-evaluation.md) — links here from the implicit-subagent-dispatch anti-pattern
- [Evidence-Based Revalidation](evidence-based-revalidation.md) — links here from the 4.6 → 4.7 case study

## Sources

- Anthropic Migration Guide (Tier A): https://platform.claude.com/docs/en/about-claude/models/migration-guide
- What's New Claude 4.8 (Tier A): https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8 — behavioral deltas vs 4.7 (better tool triggering, better compaction/long-context, adaptive-only thinking with 400 on budgets, default effort `high`). Fetched 2026-05-30.
- Opus 4.8 system card (Tier A): https://www.anthropic.com/claude-opus-4-8-system-card — grader-awareness/eval-speculation flagged as the most concerning training trend (modest behavioral effect); alignment improvement over 4.7.
- Claude Opus 4.8 launch news (Tier A): https://www.anthropic.com/news/claude-opus-4-8 — released 2026-05-28, model ID `claude-opus-4-8`, misaligned behavior substantially lower than 4.7. Fetched 2026-05-30.
- What's New Claude 4.7 (Tier A): https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- Opus 4.7 system card (Tier A): chart images carry the MRCR-v2 multi-needle figures (1M: 78.3%→32.2%; 256k: 91.9%→59.2%, 4.6→4.7); "overcorrection" appears only in the BBQ bias context; over-refusal tracked as a metric (4.7 < 4.6).
- Best Practices for Opus 4.7 with Claude Code (Tier A): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
- OpenAI MRCR v2 (Multi-Round Co-Reference Resolution, 8-needle) — benchmark for the 4.6→4.7 long-context regression case study.
- Context Arena; dev.to "I read all 232 pages [of the Opus 4.7 system card]" (Tier B) — third-party transcription of the MRCR figures from the 4.7 card's chart images.
- Jason Vertrees, "Claude 4.7 Quietly Broke Your Prompts and Harness" (Tier B, LinkedIn, April 2026) — **provenance-only** per the 2026-07-10 SOURCES pass: his specific guidance is stale (written against 4.7 and not maintained), but his independent construction of an audit framework from the same Tier-A advisory stands as adoption evidence.
- Simon Willison, Opus 4.7 system-prompt analysis (Tier B, April 18, 2026)

**Convergence basis (emerging, ruled 2026-07-16)**: treating each model release as a behavioral-delta audit target — rather than a drop-in upgrade — has two independent external exemplars: Willison's per-release analyses (a behavioral read of each major model release, sustained across releases) and Vertrees's audit framework (an independent operationalization of the same migration advisory this doc systematizes). Vertrees counts as adoption evidence only, per the provenance-only caveat above; neither exemplar is a diagnostic instrument like this doc's matrix, which is the delta we keep (see ABSORPTION-MAP.md).
- HN discussions 47793411, 47814832 (Tier C, community observation)
- Soft-rule / emphatic-constraint hard-capping (Tier B, this project's observed-in-practice usage across Opus 4.7 / 4.8 sessions) — *not* named in any Anthropic card; consistent with but not proven by the Tier-A literal-interpretation posture.

**Gaps**:
- No independent benchmark yet comparing 4.6/4.7/4.8 on the six prompt anti-patterns. Tracking for corroboration in subsequent revalidation cycles.
- No public MRCR-v2 transcription for 4.8 yet — the "better long-context handling" 4.8 claim (Tier A) is directional, not quantified against the 4.6/4.7 MRCR figures. Re-benchmark before relying on multi-needle retrieval at long context on 4.8.

---

*Last updated: 2026-07-17 (context-fill void superseded: fresh-session re-run executes end-to-end; silent workflow-path model fallback caught by adversarial verification — Opus-served readers under a Fable request — and re-run gated on per-turn served model; first Fable rows descriptive ceiling through ~140k tokens; Gap 317 open). Prior: 2026-07-16 (Fable 5 probe program: round one established three rows and voided four; round two re-instrumented dispatch and literalization — five graded rows total; final round re-instrumented unread-references and unanchored-triggers, descriptive-only under adversarial review; convergence single-source → emerging per owner ruling); 2026-06-15 (volatile Fable 5 / Mythos 5 currency note); May 2026 (4.8 release).*
