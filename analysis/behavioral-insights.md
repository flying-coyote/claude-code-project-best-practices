---
evidence-tier: Mixed
measurement-claims:
  - claim: "Fable 5 in-harness adherence ladder: 1.0 adherence at 10/40/80/150 synthetic token-inclusion rules (n=3 per rung, zero variance) — ceiling bound only, does not locate the cap for realistic instructions"
    source: "Controlled probe session, this repo — raw record research/fable-probe-session-2026-07-16.md"
    date: "2026-07-16"
    revalidate: "2027-01-16"
  - claim: "Fable 5 realistic-prose adherence ladder (descriptive ceiling): 12/12 served-model-gated reps at 1.0 informative-rule adherence at 25/50/100/200 realistic-diversity rules rendered as unnumbered flowing guide prose (baseline positive control: ~79 rules/run violated with no guide; golden fixture 199 SAT). Same-instrument Opus 4.8 arm (n=3 gated per rung after evening replacement reps): 1.0 everywhere except two morning K100 reps at 46/47 — one verbatim-phrase rule paraphrased (fable rendered it literally 6/6, opus 4/6): an interpretation-dependent literalization-propensity difference (the rule sentence is ambiguous) that is checker-artifact-robust; not a cap observation, not a ranking. Conditions: xhigh effort, verify-and-fix behavior, surface-checkable rules, one greenfield task, opus-only evening wave"
    source: "Controlled probe session, this repo — raw record research/probe-session-2026-07-18.md Part 3"
    date: "2026-07-18"
    revalidate: "2027-01-18"
  - claim: "Fable 5 in-harness context-fill retrieval (descriptive ceiling, not a degradation onset): 10/10 salient template-flagged facts at 5-95% depth through ~40k/~100k/~140k tokens of tool-result fill in every served-model-gated rep (R40 3/3, R100 2/2, R140 3/3; endpoints anchored 0/10 no-read, 10/10 low-fill) — easiest retrieval regime; the 60%-gap correlation study stays open"
    source: "Controlled probe session, this repo — raw record research/fable-probe-session-2026-07-16.md (2026-07-17 addendum)"
    date: "2026-07-17"
    revalidate: "2027-01-17"
applies-to-signals: [audit-always-fetch, model-version-migration, model-version-4-8, model-version-opus-5, model-version-sonnet-5]
convergence: single-source
last-verified: 2026-08-29
revalidate-by: 2027-02-13
status: PRODUCTION
follows: "ClaudeLog (claudelog.com, community Claude Code mechanics documentation by InventorBlack — Anthropic Developer Ambassador; Tier C with author-authority note, verified 2026-08-29: site ALIVE — changelog current through 2026-08-23 and v2.1.2xx features covered, but the foundational Mechanics pillar pages this lane leans on are stale at Jan–Feb 2026, not yet rewritten for the Claude 5 era) — the 'how Claude Code behaves' mechanics-explainer lane. Bar status: fails Supported-as-replacement (docs site, no release discipline; uneven update cadence between changelog/FAQ and Mechanics pillars). Delta kept here: the quantified measurements — 80% CLAUDE.md adherence, 60% context threshold, ~150-instruction budget (all Opus-4.x-era; first bounded Fable data point 2026-07-16, realistic-diversity re-measure delivered 2026-07-18, and no Claude 5-family — Opus 5 / Sonnet 5 — arm run at all). Advance trigger: ClaudeLog or Anthropic publishing measured adherence/threshold data — re-checked 2026-08-29, NOT fired (still no percentages/thresholds anywhere on the site)."
---

# Behavioral Insights: How Claude Code Actually Works

> **Re-measure flag (2026-07-10; re-framed 2026-08-13)**: the quantified thresholds below (80% CLAUDE.md adherence, the 60% context-quality boundary, the capacity bands) were measured in the Opus 4.x era, against a model lineup that no longer exists. The lineup as of 2026-08-13 is **Fable 5** (top widely-released tier) > **Opus 5** (`claude-opus-5`, released 2026-07-24, Anthropic's recommended starting model) > **Sonnet 5** (`claude-sonnet-5`, the Claude Code default model) > **Haiku 4.5**, with **Opus 4.8 moved to "Legacy models"** (Tier A, [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) + [What's new — Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5), fetched 2026-08-13). Treat the current figures as Opus-4.x-calibrated until re-measured. *First bounded Fable data point recorded 2026-07-16*: a synthetic-rule adherence ladder found zero degradation through 150 rules (a ceiling result on an artificial instrument — see the ~150-cap section), so the Opus-era figures are now flagged stale for Fable while the realistic-diversity re-measure stays open. *Second Fable data point 2026-07-17*: salient-needle context-fill retrieval was clean through ~140k tokens of tool-result fill (descriptive ceiling on the easiest retrieval regime — see the 60%-gap entry in Gaps); the fill-vs-quality correlation study the 60% figure needs stays open. *Third Fable data point 2026-07-18*: the realistic-diversity re-measure this flag demanded was delivered — a 200-rule realistic-prose ladder with a baseline positive control and a same-instrument Opus 4.8 arm ran clean 12/12 for Fable at every rung through 200 rules (descriptive ceiling; the cap for realistic instructions remains unlocated), and produced the program's first same-instrument between-model score difference, an interpretation-dependent literalization gap on one verbatim-phrase rule — fable 6/6 literal vs opus 4/6 at full n (see the ~150-cap section; raw record research/probe-session-2026-07-18.md). ***The debt now spans two newer generations, not one (2026-08-13)***: the Fable arms above discharge nothing for the Claude 5 model family — Opus 5 (2026-07-24) and Sonnet 5 both post-date every measurement in this doc *and* every probe in the Fable arms, so the thresholds are one generation stale for Fable and two for the model most Claude Code sessions actually run. Sonnet 5 also introduces a confound the Fable re-measure never faced: its new tokenizer emits "approximately 30% more tokens" for the same input text than Sonnet 4.6 (Tier A, [What's new — Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5), fetched 2026-08-13), so any threshold denominated in tokens — or in percent-of-window fill, whose denominator is tokens — is not comparable across the tokenizer boundary without re-baselining.

**Evidence Tier**: Mixed (A-B) — Quantified claims from Boris Cherny, Anthropic engineering blog, and practitioner observation

> **Following ClaudeLog since 2026-07-16.** New coverage effort on behavior-mechanics explanation goes to tracking the canon (claudelog.com), not growing this doc. Delta kept: the quantified measurements, which ClaudeLog does not publish.

## Purpose

This document collects **quantified behavioral observations** about Claude Code that aren't obvious from documentation alone. These are the "gotchas" and calibration points that distinguish effective usage from naive usage.

**Convergence note**: the frontmatter rates this doc's function `single-source`; where a recommendation here would drive new infrastructure adoption rather than calibrating native Claude Code usage, adoption requires converged status or an explicit owner exception.

---

## Context Window Behavior

### Capacity Thresholds (Boris Cherny, March 2026)

| Context Usage | Behavior | Recommendation |
|--------------|----------|----------------|
| 0-20% | Optimal performance | Normal operation |
| 20-40% | Good performance, slight degradation | Monitor context |
| 40-60% | Noticeable quality decline | Consider Document & Clear |
| 60-80% | Significant degradation | Document & Clear recommended |
| 80%+ | Near-failure zone | Start new session |
| ~83.5% | Auto-compaction triggers | System intervenes automatically |

**Key insight**: Quality degrades *before* the context window fills. The 60% mark is where Boris recommends proactive intervention (pre-Fable measurement, March 2026 — re-measure open).

> **Revalidation (2026-05-30) — "60%" is an intervention heuristic, not a measured degradation onset.** The 60% figure is a Claude-Code *usage-intervention* rule of thumb (Tier C; the originally-cited source page now 403s), not a benchmarked degradation threshold. Published long-context benchmarks put the *onset* much earlier and make it model-specific: arXiv:2601.15300 finds Qwen2.5-7B degrades at 40–50% of max context (F1 0.55→0.30); Fiction.liveBench shows deep-comprehension sliding "closer to 32k"; NoLiMa (ICML 2025) shows most models drop below half their short-input score by 32k tokens. The defensible claim is: **degradation onset is model-specific and typically begins far below the advertised window — roughly 16–64k tokens, ≈20–50% on a 1M-context model. Treat 60% as a practical "intervene now" trigger, not as the point where quality starts to fall.** 4.8's "better long-context handling / fewer compactions" (Tier A, [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8)) shifts this favorably vs 4.7, but by an unquantified amount — re-measure on 4.8 rather than assuming the threshold moved. Sources: arXiv:2601.15300, Fiction.liveBench, NoLiMa (ICML 2025), arXiv:2510.05381.

### Context Rot (RLM Research, Zhang et al.)

"Context rot" = performance degradation as context fills, *beyond what benchmarks capture*. Standard benchmarks test needle-in-haystack retrieval, not holistic reasoning over accumulated context.

**Observable symptoms**:
- Long Claude Code sessions where quality degrades
- Extended conversations that lose coherence
- Large codebase analysis that misses obvious patterns

**Mitigation approaches** (ranked by validation):
1. **Fresh sessions** — Most validated (GSD pattern, Anthropic guidance)
2. **Document & Clear** — Externalize findings, then start fresh (Boris Cherny)
3. **Subagent delegation** — Offload work to fresh-context subagents
4. **Recursive decomposition** — Process context in partitioned chunks (RLM-inspired, not yet Claude-validated)

### CLAUDE.md Adherence (~80%)

Boris Cherny reports CLAUDE.md instructions are followed approximately 80% of the time (pre-Fable measurement, March 2026 — re-measure open). This means:
- Don't rely on CLAUDE.md for safety-critical constraints
- Use hooks for enforcement where compliance must be 100%
- Keep instructions under ~150 lines to maximize adherence
- Repetition and emphasis can increase compliance on critical rules

---

## Ambiguity and Assumptions

### The Johari Window Problem

AI conversations suffer from four knowledge quadrants (adapted from CAII/skribblez2718):

| Quadrant | Description | Risk |
|----------|-------------|------|
| **Arena** (Both know) | Shared understanding | Low — explicit |
| **Hidden** (User knows, AI doesn't) | Team conventions, prior decisions, unstated constraints | High — AI proceeds with wrong assumptions |
| **Blind Spot** (AI knows, user doesn't) | Security implications, performance trade-offs, alternative approaches | Medium — user makes uninformed decisions |
| **Unknown** (Neither knows) | Scaling behavior, edge cases, integration issues | High — discovered too late |

**Practical implication**: For complex tasks (3+ files, architecture decisions), explicitly surface assumptions *before* implementation. The SAAE protocol (Share-Ask-Acknowledge-Explore) reduces "that's not what I meant" rework.

### Specification Gap (Nate B. Jones, January 2026)

| AI Tool Type | Strength | Weakness |
|-------------|----------|----------|
| **Colleague-shaped** (Claude Code) | Ambiguous tasks, creative solutions, exploratory work | Unpredictable, harder to evaluate |
| **Tool-shaped** (Codex, CI agents) | Well-specified tasks, deterministic output | Requires clear specifications |

> "Codex is better when you can define correctness. Claude Code is better when you can't."

**Implication**: Choose your AI tool based on how well you can specify the task, not just which tool is "better."

---

## Instruction Processing

### ~150 Instruction Cap (Convergent Evidence)

The ~150 instruction cap is now independently validated by multiple high-authority sources (pre-Fable measurement — re-measure open):

| Source | Authority | Basis |
|--------|-----------|-------|
| Boris Cherny (Claude Code creator) | 5/5 | Direct practitioner observation |
| Dexter Horthy (RPI/CRISPY creator) | 4/5 | Cites arXiv paper via Kyle's blog |

This upgrades the claim from single-source expert guidance to **convergent practitioner evidence** — different practitioners, different data sources, same conclusion. The cap appears to be a genuine behavioral boundary, not an artifact of one person's workflow.

> **First Fable 5 data point (2026-07-16, Tier B, self-measured — a bound, not a replication).** A 12-run in-harness ladder (10/40/80/150 mechanically checkable token-inclusion rules, n=3 per rung, `effort: medium`, probes on `claude-fable-5` inside the Claude Code harness) measured **100% adherence at every rung with zero variance**. Read this narrowly: synthetic token rules are easier to satisfy than the heterogeneous prose instructions of a real CLAUDE.md, and the instrument never entered a degradation region, so it cannot certify the cap is gone — and because the instrument has never demonstrated it can detect degradation at all (no positive control), even "bounds the onset above 150" overstates it; the defensible reading is descriptive: no failures observed through 150 synthetic rules. A same-day heterogeneous ladder (10 mechanically checkable style rules + 3 constructive rule families, N=40/80/150/250, 3 reps each) also ran clean at 12/12 reps — with the same no-positive-control caveat, plus two more from adversarial review: ~13 rule *types* repeated carry far less informational load than 250 independent constraints, and a numbered rule block is near-optimal scaffolding compared to real CLAUDE.md prose spread across competing sections. What it does establish is that the Opus-era figures should be treated as stale for Fable pending a re-measure with realistic rule diversity, rungs past 150, and a same-instrument Opus comparison arm. Raw distributions and the adversarial-verification record: [research/fable-probe-session-2026-07-16.md](../research/fable-probe-session-2026-07-16.md).
>
> **Second Fable 5 data point (2026-07-18, Tier B, self-measured — realistic-diversity ladder, still descriptive).** The re-measure the paragraph above demanded was delivered: 200 mechanically-checkable rules across 12 types, rendered as unnumbered flowing prose in a contributor-guide fixture (no numbered-block scaffolding), nested rungs 25/50/100/200, a baseline positive control (the six no-guide runs violate a mean of ~79 rules, so the checker demonstrably reads low — the failure-capability the earlier ladders lacked), a golden compliant fixture (199 SAT + 1 conditional NA), per-turn served-model gating, and a same-instrument Opus 4.8 arm. **Fable: 12/12 gated reps at 1.0 at every rung through 200 rules** — a descriptive ceiling again; no Fable failure was observed, so the cap for realistic instructions remains unlocated. The Opus arm produced the program's first same-instrument between-model score difference, and its character matters more than its size: under the strict-verbatim interpretation of one ambiguous phrase rule ("The phrase standard library only appears in the README", no exactness rider), the three morning-wave Opus K100 reps paraphrased while all twelve Fable reps rendered the phrase literally; the single evening replacement rep rendered it literally (a word-order variant, from the arm's heaviest verify-and-fix rep), leaving gated literal rendering at fable 6/6 vs opus 4/6 — an interpretation-dependent *literalization-propensity* difference that is nonetheless checker-artifact-robust (within the strict reading, no prose-faithful amendment can rescue a missing phrase), consistent in direction with the 2026-07-16 emphatic-literalization finding, and explicitly not a cap observation (one rule, one rung, wave confounded, n tiny) and not a model ranking. Conditions bounding the ceiling: xhigh session effort with verify-and-fix loops in both arms, surface-checkable rules on one small greenfield task, single seed-locked rendering per rung. Residual open item: a design Fable can actually fail — conflicting/semantic rules, one-pass low-effort regimes, multiple renderings, distractor load. Raw record and two-lens verification trail: [research/probe-session-2026-07-18.md](../research/probe-session-2026-07-18.md).

**Recommendations**:
- Keep CLAUDE.md under 150 lines (60 lines optimal)
- Use progressive disclosure — reference files instead of inlining content
- Skills load ~2% of context budget each; budget accordingly
- 500-line cap on individual SKILL.md files
- Split mega-prompts with 85+ instructions into phases with <40 instructions each (see Design Rule below)

### Prompt Sensitivity Across Model Versions

Prompt sensitivity is not uniform across the Opus family — what works on one version can silently degrade on the next, and one release's remediation can become the next release's defect. Cross-version diagnostic table:

| Version | Sensitivity pattern | Implication for existing prompts |
|---|---|---|
| **Opus 4.5 / 4.6** | More responsive to system prompts than earlier models; infers intent liberally from loose phrasing | Dial back "ALWAYS"/"NEVER" emphasis; watch for overtriggering on tool/skill invocation language |
| **Opus 4.7** (April 16, 2026) | **Literal interpretation** — will not silently generalize instructions; fewer default subagents; adaptive verbosity | 4.6-validated prompts with vague descriptors, edge-case gestures, or unanchored triggers may silently no-op |
| **Opus 4.8** (May 28, 2026) | Literal interpretation **carries forward**; *recovery* on reliability — better tool triggering (fewer skipped required tool calls), better compaction/long-context recovery, more reliable effort calibration. Adaptive thinking is the **only** thinking mode (extended-thinking budgets now 400), default effort `high` | Most 4.7 remediations still apply. The one breaking change: any harness passing `thinking: {budget_tokens: N}` hard-fails — migrate to `thinking: {type: "adaptive"}` + `effort`. The 4.7 "skipped tool call" and "references not read" failure modes are *softened* but not eliminated — keep mechanical enforcement for 100% adherence |
| **Opus 5** (July 24, 2026) | Literal-interpretation posture **carries forward** — the migration guide retains the 4.7 literalism advisory and recommends a prompt/harness review for the Opus 5 migration. Four first-party behavioral deltas: default user-facing responses and written deliverables run **longer**; the model **narrates progress more often** in agentic sessions; it **delegates to subagents more readily** (a *reversal* of the 4.7/4.8 fewer-subagents posture); and it **verifies its own work without being told to**. Thinking is on by default; effort ladder is `low`–`max` (`max` new) | **Delete carried-over verification instructions** — first-party guidance is explicit that they "cause over-verification on Claude Opus 5." This is a removal, not a rewrite, and it inverts the usual self-check advice. **Cap subagent delegation explicitly** — any "delegate more" guidance written for 4.8 now compounds. **Prompt for response length explicitly**: lowering effort "can reduce thinking volume without reliably shortening the visible response," so effort is not the verbosity lever. Prefer positive examples to negative instructions, and do **not** instruct the model not to think (raises tag leakage when thinking is disabled). Breaking: `thinking: disabled` + effort `xhigh`/`max` returns 400 |

**Sonnet 5 note (Tier A)** — Sonnet 5 (`claude-sonnet-5`) is the Claude Code default model and is priced $2/$10 per MTok permanently as of 2026-08-10. Two items bear on *this* doc rather than on prompt phrasing:

1. **New tokenizer, ~30% more tokens.** Verbatim: "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6." This shifts every token-denominated threshold — including the 60% context-fill heuristic, whose denominator is tokens — so percent-of-window figures measured before the tokenizer change are not like-for-like with figures measured after it. Source: [What's new — Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) (Tier A, fetched 2026-08-13); independently corroborated by Willison's own counts (~1.4x English, 1.33x Spanish, 1.28x Python — Tier B, [simonwillison.net, 2026-06-30](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/)).
2. **Sampling parameters locked.** Non-default `temperature` / `top_p` / `top_k` return 400. A harness that tuned determinism or variety through `temperature` must steer by prompt instead.

**Harness-side note (Tier A, Claude Code v2.1.219, 2026-07-24)** — the release that made Opus 5 the default Opus model also raised **nested subagent depth from 1 to 3 by default**. The readier-delegation behavior in the Opus 5 row therefore compounds with a harness that now lets subagents spawn subagents two levels deeper than before: state the delegation cap in prompt text *and* check it against the harness setting.

The Anthropic migration guide states explicitly:

> "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6... It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make."

The [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) describe 4.8 as targeting "better tool triggering" ("less likely to skip a tool call the task required, an issue some users reported on Claude Opus 4.7") and "better compaction handling and long-context quality" ("long agentic traces stay on task with fewer derailments after compaction"). 4.8 is a calibration release on top of the 4.7 posture, not a reversal of it.

**Selective literalism caveat** (Willison, April 18, 2026): 4.7 is tuned to be *less* literal about clarifying-question behavior — the leaked system prompt instructs Claude to "make a reasonable attempt now, not... be interviewed first." Audits that treat literalism as uniform will over-correct.

**Sycophancy on 4.8 — direction is contested, and the tiers point opposite ways.** Launch-day user reports (Reddit / AI-newsletter anecdote) flagged *sharper* sycophancy on 4.8 (Tier C, anecdotal, no benchmark). Anthropic's own evals report the **opposite** direction: 4.8 is "an improvement over Opus 4.7 on most alignment measures," honesty in agentic settings "markedly improved," and in the third-party Petri 3.0 run it was "the best-aligned publicly accessible model by nearly all these metrics" (Tier A, Opus 4.8 system card; the launch news adds that misaligned behavior is "substantially lower than Opus 4.7"). The *only* "up" signal in Anthropic's own material is a qualitative pilot-feedback line noting "Mild sycophancy," which the card explicitly flags as **not consistent with the quantitative trends**. Net: do **not** assert a numeric sycophancy increase on 4.8. The honest statement is "launch-day user reports flagged sharper sycophancy (Tier C, anecdotal); Anthropic's own evals report the opposite direction (Tier A)." **Opus 5 direction resolved from the card (read 2026-08-29, Tier A)**: the automated behavioral audit's governing statement is *"Claude Opus 5 misleads the user at rates similar to or lower than Opus 4.8, Mythos 5, and Sonnet 5"* (§6.4.3, p. 98 — sycophancy is a named metric in that dishonesty group; per-metric numerics live in a figure image, so only the direction is quotable). Two card-body nuances keep this from being a clean "improved": when pushed on something it knows is incorrect, Opus 5 *"resorts to agreeing with the user more than Sonnet 5 and Mythos Preview, but less than all other recent models"* (p. 83), and the card's headline alignment finding is **overconfidence**, not sycophancy — *"the model hallucinates factual claims slightly more than Opus 4.8, despite being more accurate overall"* (p. 4/§6.5.1), which for a harness reads as a calibration risk in the opposite social direction. Extraction record: [research/opus5-system-card-extraction-2026-08-29.md](../research/opus5-system-card-extraction-2026-08-29.md).

**New 4.8 behavioral watch-item (Tier A)**: the Opus 4.8 system card flags a "growing tendency toward speculation about graders / reasoning about how outputs will be assessed" as the *most concerning trend during 4.8 training* — with only modest behavioral effects at deployment. Relevant to rubric-scored evaluator-agent workflows (see [Agent Evaluation](agent-evaluation.md) and the self-evaluation failure mode below).

**Community counter-signals (Tier C)**: [HN 47793411](https://news.ycombinator.com/item?id=47793411) reports adaptive thinking under-triggering on reasoning-heavy tasks (workaround: `xhigh` effort) — 4.8's "more reliable effort calibration" claim may partially address this; re-test before relying on the workaround. [HN 47814832](https://news.ycombinator.com/item?id=47814832) reports system-reminder over-application to every file read.

See [Model Migration Anti-Patterns](model-migration-anti-patterns.md) for the prompt anti-patterns, the 4.8 net-deltas table, the promoted soft-guideline-literalization anti-pattern, the 4.6→4.7 MRCR long-context regression case study, and the MUST-vs-positive-examples tension (Vertrees's MUST/MUST NOT framing conflicts with Anthropic's stated preference for positive examples).

### Vertical Planning Principle (Horthy, Authority 4/5)

Models default to **horizontal plans**: all DB schema, then all services, then all API endpoints, then all frontend components. This produces 1200+ lines of untestable code before anything can be verified.

**Vertical plans** create testable checkpoints at each stage:
1. Mock API -> frontend (verify UI works with mocked data)
2. Real services -> API (verify backend works)
3. Database -> services (verify data layer)
4. Integration (verify everything together)

**Harness implication**: If your agent produces large untestable blocks, the issue may be plan orientation, not model capability. Instruct vertical slicing explicitly.

Source: Dexter Horthy (RPI/CRISPY creator), Authority 4/5.

### Design Rule: Control Flow, Not Prompts

> "Don't use prompts for control flow; use control flow for control flow."

Mega-prompts with 85+ instructions cause inconsistent adherence and require "magic words" to trigger specific behaviors. The failure mode: the agent follows some instructions reliably but ignores others unpredictably.

**Fix**: Split into discrete phases with <40 instructions each. Use actual control flow (hooks, scripts, staged prompts) to sequence the phases rather than hoping the model will self-sequence through a long instruction list.

This aligns with the ~150 instruction cap above — the cap isn't just about total count but about cognitive load per decision point.

Source: Dexter Horthy (RPI/CRISPY creator), Authority 4/5.

### Monitor Tool (Anthropic, April 2026)

New built-in tool for background process observation. Uses **interrupt-based notification** instead of polling loops — the agent no longer wastes tokens repeatedly checking subprocess status.

**Key behavioral note**: The Monitor tool requires explicit prompting. Without instruction, the agent defaults to polling patterns (run command, check output, wait, check again). With instruction ("use the monitor tool to observe for errors"), it switches to an event-driven pattern that is both cheaper and more responsive.

Source: Anthropic, April 2026.

---

## Thinking and Reasoning

### Extended Thinking Trade-offs (Boris Cherny)

> "I use [Opus with extended thinking] for everything. It's slower but because it's more reliable there's less course correcting."

| Factor | With Extended Thinking | Without |
|--------|----------------------|---------|
| Latency | 2-3x higher | Standard |
| Quality | Higher | Good |
| Steering corrections needed | Fewer | More frequent |
| **Total time to completion** | Often lower (fewer retries) | Higher if steering needed |

**Rule of thumb**: Extended thinking saves net time on tasks that would otherwise require 2+ steering corrections.

### Writer/Reviewer Pattern (Boris Cherny, March 2026)

Split implementation and review into separate sessions:
1. **Writer session**: Implement the feature
2. **Reviewer session**: Review the implementation with fresh context

This exploits fresh context to catch issues the writer session became "blind" to after accumulating implementation context.

---

## Multi-Agent Behavior

### Subagent Context Isolation

Subagents have **zero** access to parent conversation history. Common mistakes:
- Referencing "the code we discussed" in subagent prompts (it has no conversation history)
- Expecting subagents to ask clarifying questions (they execute and return)
- Assuming subagents know project conventions (include them in the prompt)

### Custom Subagent Gatekeeping Anti-Pattern (Boris Cherny)

Custom subagents (`.claude/agents/`) can **"gatekeep context"** and force rigid human workflows onto the agent. Instead of defining many custom subagents:
- Give the main agent context in CLAUDE.md
- Let it use native Task/Explore features for delegation
- Reserve custom agents for truly specialized roles (security review, domain-specific validation)

### Agent Teams vs Subagents (v2.1.32+)

| Need | Use Subagents | Use Agent Teams |
|------|--------------|-----------------|
| Task duration | Minutes | Hours to days |
| Communication | Report-back only | Agents communicate directly |
| Cost | Lower | Higher |
| Stability | Production-ready | Experimental |

---

## Agent Capability Boundaries

### Jaggedness Principle (Karpathy, Authority 4/5)

Agent capability is not uniformly distributed — it is **domain-structured**. Agents excel in verifiable domains and stagnate in non-verifiable ones:

| Domain Type | Examples | Agent Performance | Why |
|-------------|----------|-------------------|-----|
| **Verifiable** | Code, tests, structured data, SQL, math | Rapidly improving | RL can optimize against clear correctness signals |
| **Non-verifiable** | Design taste, writing style, judgment calls, UX decisions | Stagnating | No ground truth to train against |

The unpredictability of agent performance is not random — it follows this verifiable/non-verifiable axis. This has direct harness design implications:

- **Route to agents**: Tasks with verifiable outputs (write a function, fix a test, generate SQL, refactor code)
- **Keep for humans**: Tasks requiring subjective judgment (API design, naming conventions, UX flow, architectural trade-offs)
- **Hybrid**: Agent drafts, human evaluates on subjective dimensions

Source: Andrej Karpathy, No Priors podcast, March 2026. Authority 4/5.

### Poor Self-Evaluation Failure Mode (Anthropic, Authority 5/5)

Anthropic disclosed a specific failure pattern in Claude's self-evaluation: the model identifies legitimate issues then **rationalizes them away**.

> Claude "talked itself into deciding they weren't a big deal and approved the work anyway."

The failure mode is NOT "misses issues." The model *sees* the problems. The failure mode is "identifies then rationalizes" — a motivated reasoning pattern where the model talks itself out of its own correct assessment.

**Mitigation**: Independent evaluator agents with weighted rubrics. The evaluator must be context-isolated from the builder (fresh session, no shared conversation history) to prevent the same rationalization pattern. Structured rubrics with explicit scoring prevent narrative self-persuasion.

This aligns with Boris Cherny's Writer/Reviewer pattern: the review session catches what the writer session rationalized away, because it has fresh context and no sunk cost in the implementation.

Source: Anthropic engineering blog, Authority 5/5.

### Vendor-Side Quality Regression Case Study: The April 2026 Postmortem

Anthropic published a postmortem ([engineering blog, 2026-04-23](https://www.anthropic.com/engineering/april-23-postmortem)) acknowledging that Claude Code, Claude Agent SDK, and Claude Cowork users were experiencing real intelligence degradation starting in early March 2026 — across Sonnet 4.6, Opus 4.6, and Opus 4.7. The API itself was unaffected; only the Claude Code surface and adjacent products. Three independent bugs were identified and all reverted by April 20 (v2.1.116).

| Bug | Date introduced | What happened | What it teaches harness designers |
|---|---|---|---|
| Reasoning-effort default change | March 4 | Default switched from `high` to `medium` to address UI freezing; sacrificed intelligence. Reverted April 7 after user complaints. | Effort-level defaults are a load-bearing harness setting, not a cosmetic one. Surface `${CLAUDE_EFFORT}` in your skills (v2.1.120+) so degradations like this are detectable from inside the harness, not just from output quality. |
| Caching bug with extended thinking blocks | March 26 | A prompt-caching optimization continuously cleared extended thinking blocks from sessions idle over one hour, rather than clearing once. Claude effectively lost mid-session reasoning context across turns. | Caching layers can silently amputate context the harness assumed was retained. Any "trust the cache to hold reasoning" assumption is fragile against vendor-side cache behavior changes. |
| System prompt verbosity instruction | April 16 | Instruction limiting text-between-tool-calls to ≤25 words and final responses to ≤100 words "hurt coding quality" when combined with other prompt changes. | **Counter-evidence** to a naive "less is more" reading of harness/prompt minimalism. Brevity constraints applied at the wrong layer (system prompt for code work) can degrade output even when the same brevity is harmless or helpful at the user-prompt layer. |

**Anthropic's own remediation list** (announced in the postmortem): broader per-model evaluations for system-prompt changes, stricter code-review process using the improved Code Review tool, soak periods and gradual rollouts for intelligence-affecting changes, expanded repository context for code reviews.

**What this changes about the rest of this doc**: the practitioner-observed quality thresholds elsewhere in this document (60% context decline, ~80% CLAUDE.md adherence, ~150 instruction cap; all pre-Fable, re-measure open) were collected by users observing aggregate behavior — but vendor-side defaults sit *upstream* of all of those observations. A revalidation against a degraded default measures the degraded default, not the underlying behavior. Date-anchor practitioner-observed claims to a specific Claude Code version, and re-run them after major vendor-side changes.

Source: [Anthropic Engineering — April 23 Postmortem](https://www.anthropic.com/engineering/april-23-postmortem) (2026-04-23). Tier A. Confirmed via WebFetch 2026-05-24.

### Principle-Teaching Reduces Agentic Misalignment (Anthropic Research, May 2026)

Anthropic published research on a training-data design choice: teaching models the *principles* behind ethical behavior — not just labeled examples of compliant vs. non-compliant outputs — substantially changes how models behave in agentic-misalignment scenarios.

| Training data approach | Blackmail-scenario rate | Token efficiency |
|---|---|---|
| Synthetic honeypot dataset (labeled examples) | 22% | Baseline |
| "Difficult advice" dataset (reasoning about *why*) | ~3% | ~28× more efficient |

**Implication for harness designers**: As alignment training pushes the model toward internalizing *why* certain actions are problematic — rather than pattern-matching labeled don'ts — heavy `MUST NOT do X` scaffolding in CLAUDE.md becomes less load-bearing per unit of safety. The training-time effect is the more reliable lever; the CLAUDE.md prohibition is a backstop, not a substitute.

**Caveats**:
- This is a single Anthropic publication; "MUST NOT" rules in CLAUDE.md should not be removed on the basis of this research alone.
- The 22% → 3% figure is for a specific blackmail-scenario evaluation, not a general agentic-safety metric. Don't extrapolate to "principle-teaching reduces all misalignment 7×."
- The "28× token efficiency" is a training-data efficiency claim, not an inference-time efficiency claim. It does not mean prompts get shorter.

Source: Anthropic Research, ["Teaching Claude why"](https://www.anthropic.com/research/teaching-claude-why), 2026-05-08. Authority 5/5 for the alignment-training claim; Authority 4/5 when extrapolating to harness-design implications.

---

## Auto Mode Behavior (v2.1.84+)

### Two-Stage Classifier

Auto mode uses a Sonnet 4.6 classifier to pre-approve or pre-deny tool calls:
- **93% approval rate** in production
- Classifier runs *before* the main model sees the tool call
- Non-interactive mode: aborts (doesn't skip) when approval would be needed

**Implication**: Auto mode is viable for most workflows. The 7% denial rate covers genuinely risky operations (file deletion, force push, etc.).

---

## Gaps

Several widely-cited thresholds in this doc are load-bearing but carry single-source confidence. Explicit gap statements:

**Currency (2026-08-13)**: every quantified threshold below was measured in the Opus 4.x era. The lineup is now Fable 5 > Opus 5 (recommended start, released 2026-07-24) > Sonnet 5 (Claude Code default) > Haiku 4.5, with Opus 4.8 in legacy — so the "pre-Fable" markers on the individual gaps should be read as **"pre-Fable *and* pre-Claude-5-family."**

- **Gap: 60% context quality threshold.** ⚠️ **REVALIDATED 2026-05-30 — reclassified.** Boris Cherny reports proactive intervention at 60% context; this is a practitioner *intervention heuristic* (Tier C), not a measured degradation onset, and the originally-cited source page now 403s. Independent benchmarks put the *onset* far earlier and model-specific: arXiv:2601.15300 (Qwen2.5-7B degrades at 40–50% of max context, F1 0.55→0.30), Fiction.liveBench (deep-comprehension slide "closer to 32k"), NoLiMa/ICML 2025 (most models <½ short-input score by 32k). Restated claim: onset begins far below the advertised window (~16–64k tokens, ≈20–50% on 1M-context models); 60% is the "intervene now" trigger, not the degradation point. **Still needs**: per-model correlation study between context fill and a measurable output-quality metric on current models. Do not re-run on a 4.7 baseline and call it current. (Pre-Fable measurement; re-measure open.) *First Fable data point (2026-07-17, descriptive)*: a salient-needle probe (10 template-flagged registry facts at 5–95% depth in naturalistic filler) retrieved 10/10 at ~40k/~100k/~140k tokens of in-harness tool-result fill in every served-model-gated rep on Fable 5, endpoints anchored (0/10 no-read, 10/10 low-fill) — a ceiling on the easiest retrieval regime that neither locates an onset nor tests semantic (NoLiMa-style) retrieval, so the correlation study this gap asks for remains open; the same probe caught a silent workflow-path model fallback (Opus-served under a Fable request), and any future fill measurement must gate on per-turn served model. Raw record: research/fable-probe-session-2026-07-16.md (2026-07-17 addendum).
- **Gap: ~80% CLAUDE.md adherence.** Cited ubiquitously in this repo. Source is Boris Cherny's direct observation; no public methodology for the 80% figure. **Needs**: controlled study running the same CLAUDE.md across N sessions, measuring instruction-follow rate per instruction type. (Pre-Fable measurement, March 2026 — re-measure open; the 2026-07-16 synthetic ladder is single-instruction-type and hit ceiling, so it does not discharge this gap.)
- **Gap: ~150 instruction cap.** Convergent evidence (Cherny + Horthy) upgrades confidence, but both sources reach it by observation, not measurement. **Needs**: ablation study varying CLAUDE.md instruction count and measuring adherence. (Pre-Fable measurement; re-measure open. First Fable ablations 2026-07-16: 1.0 adherence at 10/40/80/150 synthetic token rules AND 12/12 reps clean on a heterogeneous ladder through 250 checkable rules — ceiling results, descriptive only (the instruments never demonstrated they can detect degradation), so the cap for realistic prose instructions remains unlocated; see the ~150-cap section. Second Fable ablation 2026-07-18: the realistic-diversity ladder — this time WITH a demonstrated-failure-capable checker (baseline arms violate ~79 rules/run) and a same-instrument Opus 4.8 arm — still ran 12/12 clean for Fable through 200 realistic rules, while Opus paraphrased one ambiguously-worded verbatim-phrase rule in its morning K100 reps (46/47 twice at full n=3; interpretation-dependent, checker-artifact-robust); the instrument now registers model-level differences, but a Fable cap needs a design Fable can fail: conflicting/semantic rules, one-pass low-effort regimes, distractor load. Raw record research/probe-session-2026-07-18.md.)
- **Gap: Opus 4.7 literalism rate.** Anthropic states 4.7 "will not silently generalize," but does not quantify *how often* 4.6 was generalizing. **Needs**: side-by-side prompt-running on 4.6 vs 4.7 against a corpus of vague prompts; measure the silent-no-op rate delta.
- **Gap: no Claude 5-family re-measurement of any threshold (opened 2026-08-13).** None of the 80% adherence / 60% context / ~150-instruction figures has been re-measured on any Claude 5-family model. The 2026-07-16/17/18 probes cover Fable 5 with an Opus 4.8 comparison arm and predate both Opus 5 (2026-07-24) and the Sonnet 5 Claude Code default, so the most-used model in the fleet has zero coverage. **Needs**: a same-instrument Opus 5 arm on the realistic-diversity ladder (the instrument already exists and already demonstrates failure capability via the baseline control), plus a Sonnet 5 arm. **New confound for cross-era comparison**: Sonnet 5's tokenizer emits ~30% more tokens than Sonnet 4.6 for the same text (Tier A), so token-denominated and percent-of-window thresholds — the 60% figure and the ~83.5% auto-compaction band most directly — are not comparable across the tokenizer boundary. Re-baseline token counts per model before comparing eras, and record served model *and* tokenizer generation with every future measurement (the 2026-07-17 probe already established that served-model gating is mandatory; tokenizer generation is now a second required field).

These gaps do not invalidate the claims — they scope them. Practitioner-observed thresholds are still the best available evidence for these behaviors.

---

## Quantified Claims Summary

**Currency (2026-08-13)**: rows marked pre-Fable are Opus-4.x-era measurements. They have not been re-run on Fable 5 (partially probed 2026-07-16/18), on Opus 5 (released 2026-07-24, Anthropic's recommended starting model), or on Sonnet 5 (the Claude Code default) — the re-measure debt spans two generations, and Sonnet 5's tokenizer change makes any token-denominated row non-comparable across that boundary. Opus 4.8 is now a legacy model.

| Claim | Source | Confidence |
|-------|--------|------------|
| CLAUDE.md followed ~80% of the time | Boris Cherny (March 2026, pre-Fable) | High (Tier A practitioner) |
| Auto-compaction at ~83.5% context | Boris Cherny (March 2026) | High |
| 60% context = *intervention heuristic* (not measured degradation onset) | Boris Cherny (March 2026, pre-Fable); benchmarks put onset earlier & model-specific | Medium (reclassified 2026-05-30 — see Gaps) |
| ~150 instruction cap for CLAUDE.md | Boris Cherny + Dexter Horthy (convergent, pre-Fable) | **High** (upgraded: convergent evidence) |
| Auto mode 93% approval rate | Anthropic blog (March 2026) | High (Tier A) |
| Extended thinking = 2-3x latency | Boris Cherny (March 2026) | High |
| Skills use ~2% context budget each | Anthropic docs | High (Tier A) |
| Jaggedness: verifiable domains improve, non-verifiable stagnate | Karpathy (March 2026) | Medium-High (Authority 4/5, conceptual framework) |
| Self-evaluation: identifies then rationalizes issues away | Anthropic engineering blog | High (Tier A, vendor self-disclosure) |
| Monitor tool requires explicit prompting for interrupt-based mode | Anthropic (April 2026) | High (Tier A) |
| Mega-prompts with 85+ instructions cause inconsistent adherence | Horthy (CRISPY creator) | Medium-High (Authority 4/5) |
| Opus 4.7 interprets instructions literally; no silent generalization | Anthropic migration guide (April 2026) | High (Tier A, vendor docs) |
| Opus 4.7 literalism is selective — less literal on clarifying-question behavior | Willison (April 18, 2026) | Medium (Tier B, leaked system prompt analysis) |
| Opus 4.8 (May 28, 2026): better tool triggering, better compaction/long-context recovery, adaptive-only thinking (budgets 400), default effort `high` | Anthropic 4.8 docs | High (Tier A, vendor docs) |
| Opus 4.8 alignment improved over 4.7; sycophancy *up* claim is Tier-C anecdote, contradicted by Tier-A evals | Opus 4.8 system card + launch news (Tier A) vs launch-day user reports (Tier C) | A-vs-C conflict — favor Tier A (no numeric increase asserted) |
| Opus 4.8: "speculation about graders" flagged as most concerning training trend (modest behavioral effect) | Opus 4.8 system card | High (Tier A, vendor self-disclosure) |
| Opus 5 (July 24, 2026): longer default responses and deliverables, more progress narration, readier subagent delegation, self-verification without instruction — carried-over verification instructions now cause over-verification | Anthropic "What's new — Opus 5" + Opus 5 prompting guide | High (Tier A, vendor docs) |
| Opus 5: effort is not a reliable verbosity lever — prompt for response length explicitly | Anthropic Opus 5 prompting guide | High (Tier A, vendor docs) |
| Sonnet 5 tokenizer emits ~30% more tokens than Sonnet 4.6 for the same input text | Anthropic "What's new — Sonnet 5" (Tier A); Willison independent counts ~1.4x EN / 1.33x ES / 1.28x Python (Tier B) | High (Tier A vendor docs + Tier B corroboration) |
| Claude Code v2.1.219 (2026-07-24): Opus 5 becomes default Opus model; nested subagent depth default 1 → 3 | Claude Code changelog | High (Tier A, vendor release notes) |
| Opus 5 sycophancy direction | Card §6.4.3 (read 2026-08-29): misleading-the-user *"similar to or lower than"* 4.8/Sonnet 5/Mythos 5; agreement-when-pushed better than all recent models except Sonnet 5/Mythos Preview | **Tier A (direction only** — per-metric numerics are figure-image-bound); watch **overconfidence** instead, the card's actual headline finding |

---

## Sources

- Boris Cherny interviews: Lenny's Podcast, Pragmatic Engineer, Threads mega-posts (March 2026)
- Dexter Horthy (RPI/CRISPY creator): Vertical planning, control flow design rule, ~150 instruction convergent validation (via arXiv paper/Kyle's blog)
- Andrej Karpathy: No Priors podcast (March 2026) — Jaggedness principle, verifiable vs non-verifiable domain axis
- Nate B. Jones: Specification Gap, Agent Build Bible
- CAII (skribblez2718): Johari Window methodology
- RLM paper (Zhang, Kraska, Khattab): Context rot research
- Anthropic Engineering Blog: Auto mode, agent skills (March 2026), self-evaluation failure mode, Monitor tool (April 2026)
- Anthropic Engineering Blog: ["April 23 Postmortem"](https://www.anthropic.com/engineering/april-23-postmortem) (2026-04-23) — Three bugs cumulatively degraded Claude Code intelligence March 4 – April 20: reasoning-effort default high→medium, caching bug clearing extended thinking blocks every check, system prompt verbosity cap hurting code quality. All reverted by v2.1.116. Affects Sonnet 4.6, Opus 4.6, Opus 4.7 on Claude Code / Agent SDK / Cowork; API unaffected. Authority 5/5 vendor self-disclosure. Tier A.
- Anthropic Research: ["Teaching Claude why"](https://www.anthropic.com/research/teaching-claude-why) (May 8, 2026) — Principle-teaching reduces blackmail-scenario rate 22% → 3% at 28× token efficiency vs. honeypot datasets. Authority 5/5 for the training-data claim. Tier A.
- Anthropic Migration Guide (April 2026): Opus 4.7 literal interpretation, fewer default subagents, adaptive verbosity
- Anthropic, ["What's New Claude 4.8"](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) (Tier A, fetched 2026-05-30): Opus 4.8 (released 2026-05-28, model ID `claude-opus-4-8`) behavioral deltas vs 4.7 — better tool triggering, better compaction/long-context recovery, more reliable effort calibration; adaptive thinking is the only thinking mode (extended-thinking budgets return 400); default effort `high`.
- Anthropic, [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) (Tier A): improvement over 4.7 on most alignment measures, honesty in agentic settings markedly improved, Petri 3.0 "best-aligned publicly accessible model"; qualitative pilot "Mild sycophancy" note flagged as inconsistent with quantitative trends; "speculation about graders" flagged as most concerning training trend (modest behavioral effect).
- Anthropic, [Claude Opus 4.8 launch news](https://www.anthropic.com/news/claude-opus-4-8) (Tier A): misaligned behavior substantially lower than 4.7.
- Launch-day user reports of sharper 4.8 sycophancy (Tier C, anecdotal, no benchmark) — contradicted by Anthropic's own evals; no numeric increase asserted here.
- Anthropic, [Claude Opus 5 launch news](https://www.anthropic.com/news/claude-opus-5) + [What's New — Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) (Tier A, fetched 2026-08-13): Opus 5 released 2026-07-24 (`claude-opus-5`, $5/$25 per MTok, 1M context default and max, 128k output, May 2026 cutoff); Anthropic's recommended starting model; a "step-change improvement over Claude Opus 4.8, with the largest gains in deep reasoning, agentic and long-horizon tasks, and test-time compute scaling." Behavioral deltas (verbatim): "Default user-facing responses and written deliverables run longer. In agentic sessions, the model narrates its progress to the user more often. In multi-agent frameworks, it delegates to subagents more readily. It also verifies its own work without being told to, so remove verification instructions carried over from earlier models…; they cause over-verification on Claude Opus 5." Thinking on by default; effort ladder `low`–`max` (`max` new); `thinking: disabled` + effort `xhigh`/`max` returns 400.
- Anthropic, [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) (Tier A, fetched 2026-08-13): avoid carried-over verification/re-check instructions; "lowering effort can reduce thinking volume without reliably shortening the visible response. To control response length, prompt for it explicitly"; positive examples beat negative instructions; cap subagent delegation explicitly; do not instruct the model not to think (increases tag leakage at disabled thinking).
- Anthropic, [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (Tier A, fetched 2026-08-13): current lineup Fable 5 > Opus 5 > Sonnet 5 > Haiku 4.5; Opus 4.8 listed under "Legacy models"; Fable 5 remains the top widely-released tier ("frontier intelligence… at half the price" framing for Opus 5).
- Anthropic, [What's New — Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) (Tier A, fetched 2026-08-13): `claude-sonnet-5`, the Claude Code default model since v2.1.197; $2/$10 per MTok permanent as of 2026-08-10; new tokenizer — "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6"; non-default sampling params (`temperature`/`top_p`/`top_k`) return 400.
- Simon Willison, ["Claude Sonnet 5"](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/) (Tier B, 2026-06-30): independent tokenizer measurements corroborating the ~30% figure — ~1.4x English, 1.33x Spanish, 1.28x Python.
- Claude Code changelog v2.1.219 (2026-07-24, Tier A): Opus 5 becomes the default Opus model; subagents can spawn nested subagents to depth 3 by default (previously 1) — relevant to every subagent-dispatch row above.
- Anthropic, ["Redeploying Claude Fable 5"](https://www.anthropic.com/news/redeploying-fable-5) (Tier A): the June 2026 Fable/Mythos suspension was a US export-control action (2026-06-12), lifted 2026-06-30 — context for why Fable-arm probes cluster after 2026-07-01.
- Anthropic, Claude Opus 5 system card (PDF dated 2026-07-24; revision incl. the 2026-08-19 update) — **read in full 2026-08-29** (Tier A): sourced here for the sycophancy/misleading direction (§6.4.3 p. 98), agreement-when-pushed nuance (p. 83), and the overconfidence headline finding (p. 4, §6.5.1). Extraction record: [research/opus5-system-card-extraction-2026-08-29.md](../research/opus5-system-card-extraction-2026-08-29.md).
- Long-context degradation onset benchmarks (re-validating the "60%" heuristic): arXiv:2601.15300 (Qwen2.5-7B 40–50% onset), Fiction.liveBench (deep-comprehension ~32k), NoLiMa/ICML 2025 (<½ short-input score by 32k), arXiv:2510.05381.
- Simon Willison (April 18, 2026): Opus 4.7 system-prompt analysis — selective literalism
- Hacker News 47793411, 47814832: Community observation of 4.7 thinking-calibration and system-reminder over-application

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — The ~80% CLAUDE.md adherence rate and 60% context threshold are primary motivators for harness enforcement design
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — Context budget framework and progressive disclosure patterns build directly on the thresholds documented here
- [Agent-Driven Development](./agent-driven-development.md) — Commit burst patterns and ~80% adherence rate motivating hook-based security enforcement in practice
- [Model Migration Anti-Patterns](./model-migration-anti-patterns.md) — Six prompt anti-patterns that break on Opus 4.7 (vague descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement)

---

*Merged from: johari-window-ambiguity.md, recursive-context-management.md*
*Last updated: 2026-08-29, second entry (Opus 5 system card read in full — the sycophancy Unknown row resolved to a Tier A direction: misleading-the-user similar-or-lower vs 4.8/Sonnet 5/Mythos 5 per §6.4.3, with the agreement-when-pushed nuance and the card's actual headline finding — overconfidence — recorded alongside; per-metric audit numerics remain figure-image-bound, so direction only; extraction record research/opus5-system-card-extraction-2026-08-29.md). Same day, first entry (ClaudeLog canon liveness re-sweep — the leg deferred from the 2026-08-13 refresh: site ALIVE (changelog mirrored through 2026-08-23, news through 2026-08-14; v2.1.216 `prompt-audit` and v2.1.219 depth-3/Opus-5-default both covered; Sonnet-5-default and Fable 5 covered) but the followed Mechanics pillar pages are stale at Jan–Feb 2026 — claude-md-supremacy last updated 2026-02-28, the context/memory mechanics pages 2026-01-16, and the fast-mode FAQ still describes the Opus-4.6-era product — and the site's own homepage still names Opus 4.6 as flagship; advance trigger re-checked and NOT fired (no measured adherence/threshold data anywhere — qualitative language only on the pillar pages), so the quantified delta and the follow lane both hold; `follows:` verified date advanced to 2026-08-29; no measurement or body-content changes.) Prior: 2026-08-13 (Claude 5-family currency pass — no new measurements, framing only: re-measure flag re-framed to the current lineup (Fable 5 > Opus 5, released 2026-07-24 and Anthropic's recommended start > Sonnet 5, the Claude Code default > Haiku 4.5; Opus 4.8 to legacy) and to a re-measure debt that now spans TWO newer generations; Opus 5 row added to the prompt-sensitivity table (longer responses, more narration, readier subagent delegation reversing the 4.7/4.8 posture, self-verification without instruction — carried-over verification instructions now actively harmful; literalism carried forward per the migration guide) with a Sonnet 5 tokenizer/sampling note and a v2.1.219 nested-subagent-depth harness note; sycophancy row scoped to 4.8 with an explicit no-Opus-5-statement-found record (system card exists, unread this pass, nothing attributed); new gap row for the absent Claude 5-family re-measurement plus the tokenizer confound on token-denominated thresholds; Gaps + Quantified Claims currency language updated; frontmatter signals +model-version-opus-5/+model-version-sonnet-5, last-verified 2026-08-13, revalidate-by 2027-02-13. All historical measured values unchanged.) Prior: 2026-07-18 (realistic-prose adherence ladder executed — the realistic-diversity re-measure delivered with baseline positive control, golden fixture, and same-instrument Opus arm: Fable 12/12 descriptive ceiling through 200 rules, first between-model score difference recorded as adjudication-dependent literalization discrimination; measurement-claims +1, revalidate 2027-01-18; raw record research/probe-session-2026-07-18.md). Prior: 2026-07-17 (second Fable data point: context-fill retrieval descriptive ceiling through ~140k tokens on the salient-needle instrument, served-model-gated; 60%-gap correlation study stays open; measurement-claims +1); 2026-07-16 (follows: ClaudeLog added — doc now tracks the mechanics-explainer canon, keeps the quantified-measurement delta; local pre-Fable currency caveats added at each 80%/60%/~150 claim site); May 2026 (Opus 4.8 deltas + sycophancy nuance + 60%-threshold revalidation); April 2026.*

<!-- graphify-footer:start -->

## Related (from graph)

- [`AUDIT-CONTEXT.md`](../AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](../INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
