---
evidence-tier: A
convergence: emerging  # Husain/Shankar evals canon recorded in-doc 2026-07-16 (one credible external exemplar cluster for the evals-methodology function)
applies-to-signals: [harness-custom-agents, revalidation-trigger, model-version-migration, model-version-opus-5]
last-verified: 2026-08-13
revalidate-by: 2026-10-22
status: PRODUCTION
follows: "Husain/Shankar evals canon — 'LLM Evals: Everything You Need to Know' (hamel.dev/blog/posts/evals-faq/) and 'Evals Skills for Coding Agents' (hamel.dev/blog/posts/evals-skills/) (Tier B, verified 2026-07-16) — the evals-methodology commentary layer. Bar status: fails Supported (blog-form canon). Delta kept here: per-version eval baselines, the implicit-subagent-dispatch regression eval, the application table. Advance trigger: a Supported eval harness ships per-repo agent-eval baselines for Claude Code."
---

# Agent Evaluation Patterns

**Sources**:

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Evidence Tier A)
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) (Evidence Tier A)
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/infrastructure-noise) (Evidence Tier A)
- [Eval Awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp) (Evidence Tier A)
- Hamel Husain & Shreya Shankar — followed evals canon (Evidence Tier B; see Sources below)

**Evidence Tier**: A (first-party Anthropic engineering posts), with a Tier B followed practitioner canon

> **Collapsed 2026-07-16 (Absorption Scan 2026-07 §1).** The generic eval-methodology walkthrough restated first-party Anthropic engineering posts and is cut — consult those posts directly (named below). Retained: per-version eval baselines, the implicit-subagent-dispatch regression eval, the application table.
>
> **Following the Husain/Shankar evals canon since 2026-07-16.** New coverage effort on eval methodology goes to tracking the canon, not growing this doc. Delta kept: per-version baselines, the subagent-dispatch regression eval, the application table.
>
> **Canon liveness re-checked 2026-08-13 — alive, with an asymmetry worth recording.** **Hamel Husain is active**: the flagship FAQ was *modified* 2026-07-18 with a substantial new agentic-systems section (below), and he published ["AI Product Engineering Notes"](https://hamel.dev/notes/llm/ai-product-engineering/) on 2026-08-12 — a 13-session index whose thesis line is "Nearly every improvement in these notes starts with good evals." **Shreya Shankar solo is quiet**: nothing published under her own byline since 2026-05-21, though she co-authors the 2026-07-18 FAQ update, so the *joint* canon is live even while the solo output is dormant. Verdict: keep following; no advance trigger fired (still no Supported eval harness shipping per-repo agent-eval baselines for Claude Code). One first-party addition below (Anthropic verification loops, 2026-07-22) and one model-delta update to the regression eval (Opus 5). No successor to the flagship first-party "Demystifying evals for AI agents" (2026-01-09) appeared June–August 2026.

**SDD Phase**: Cross-phase (evaluation informs all phases)

---

## First-Party Eval Methodology (pointer, not a digest)

The methodology walkthrough this doc used to carry — when to start, grader and pattern selection, infrastructure controls, saturation-resistant design, skill success metrics, eval-awareness risk — restated the posts below, so go to them first-party:

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Anthropic Engineering, 2026-01-09, Tier A) — start with 20-50 simple tasks drawn from real failures; three grader types (code-based, model-based, human); `pass@k` / `pass^k` for non-deterministic agents; per-agent-type eval mapping
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) (Anthropic Engineering, 2026-01-21, Tier A) — saturation-resistant design via problem novelty, reduced realism, longer time horizons, and insight over code volume
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/infrastructure-noise) (Anthropic Engineering, 2026-02-05, Tier A) — resource configuration as a first-class experimental variable; infra error rate falls 5.8% to 0.5% from strict enforcement to uncapped resources
- [Eval Awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp) (Anthropic Engineering, 2026-03-06, Tier A) — an eval-aware agent located and decrypted the benchmark answer key; unintended solutions ran 3.7x higher in multi-agent (0.87%) than single-agent (0.24%) configurations
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (Anthropic, January 2026, Tier A) — skill-specific quantitative and qualitative success metrics plus the with/without-skill baseline-comparison template
- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) (Anthropic, Delba de Oliveira, 2026-07-22, **Tier A source, mirror-verified 2026-08-13 — direct fetch blocked**) — the workflow-pattern companion to the eval posts: "A verification loop is a workflow where Claude inspects its own work before responding, and if there is a problem, it goes back to fix it." Four patterns: **one-off** (ad-hoc check), **embedded** (the check lives inside the skill that does the work), **chained** (one skill's output feeds the next skill's check), **permanent PR fixtures** (the loop runs as repo infrastructure on every pull request). This is the in-harness sibling of an eval suite — evals grade a change *offline* against a fixed task set, a verification loop gates work *inline* on every run — so an audit finding "no eval suite" should check for verification loops before recording an absence, and vice versa. ⚠️ **Sourcing caveat**: `claude.com/blog` was unreachable directly on 2026-08-13 (login-wall redirect); content and quote were confirmed via a third-party mirror. Treat as Tier A by publisher, mirror-verified by retrieval — **do not cite as direct-fetch-verified**, and re-verify against the canonical URL when the login wall lifts.

The commentary layer above those posts — error analysis before infrastructure, binary judgments over Likert scales, annotation tooling as the highest-return investment — is the followed Husain/Shankar canon (Tier B entries in Sources below), and per the follow lane it grows there, not here. **Canon update (2026-07-18)**: the FAQ gained a substantial agentic-systems section proposing a **two-phase eval** for agents — phase one grades **black-box task success** (did the run achieve the goal), phase two runs **step-level diagnostics via a transition failure matrix** (which state-to-state transition the run failed on), so scoring and root-causing stay separate concerns. It references Claude Code's agentic search as a worked case. That is the sharpest external addition to this doc's subject since the follow lane opened, and per the lane it stays cited here rather than restated.

**Adoption gate**: this doc's function carries `convergence: emerging` in the frontmatter, and the binding rule is that standing up dedicated eval infrastructure (isolated eval environments, custom annotation tooling) on its recommendation requires converged status or an explicit owner exception.

---

## Application to Claude Code

For teams using Claude Code with custom CLAUDE.md, skills, and hooks:

| What to Evaluate | How |
|-------------------|-----|
| **CLAUDE.md effectiveness** | Does adding/removing lines change task success rate? |
| **Skill quality** | Do skills improve output vs no-skill baseline? |
| **Hook reliability** | Do hooks fire correctly? Do they catch what they should? |
| **Model upgrades** | Does switching Opus versions change outcomes? |
| **Prompt changes** | A/B test prompt modifications |

---

## Anti-Patterns (retained delta)

The generic anti-patterns (happy-path-only suites, single-run evaluation, ignoring infrastructure noise, evaluating too late) are covered by the first-party posts above; what stays here is the version-migration pair the posts don't carry.

### ❌ Implicit Subagent Dispatch (Opus 4.7 regression risk)

**Problem**: Prompts that assume the model will autonomously spawn subagents ("execute the tasks," "dispatch the work") were implicitly tuned to 4.6's liberal default. The [Opus 4.7 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) confirms 4.7 "spawns fewer subagents by default" and requires explicit steering.
**Symptom**: Evals that passed on 4.6 now return a single in-context response instead of parallel subagent work. Performance regresses silently — the output is plausible but the dispatch never happened.
**Solution**: Name the mechanism in the prompt ("Use the Explore subagent to..." or "complete in-context without subagents"). Add regression evals that count subagent invocations, not just output quality. See [Model Migration Anti-Patterns](model-migration-anti-patterns.md).

**⚠️ Reversed on Opus 5 (appended 2026-08-13, Tier A)**: the 4.7-era posture above is now the *previous* regime, and the eval concern inverts. First-party guidance for Opus 5 (released 2026-07-24) states the model "delegates to subagents more readily" ([What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5), with the prompting guidance in [Prompting Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/prompting-claude-opus-5)), undoing the 4.7 explicit-dispatch-required requirement — and Claude Code v2.1.219 raised the **default nested-subagent depth to 3** (was 1) per the [changelog](https://code.claude.com/docs/en/changelog), so a single top-level dispatch can now fan out three levels deep by default. The new anti-pattern is therefore **uncapped delegation**, not absent delegation: what used to be a *too-few-subagents* silent-regression eval (count invocations, assert they happened) becomes a *too-many-subagents / depth-3 cost* eval — assert an upper bound on invocation count and nesting depth, and cap delegation explicitly in the prompt or agent definition rather than relying on a conservative default that no longer exists. A prompt carrying 4.7-era "Use the Explore subagent to…" steering onto Opus 5 is now additive to a model that would have delegated anyway. **Grader-relevant delta on the same model**: Opus 5 "verifies its own work without being told to," and carried-over verification instructions "cause over-verification on Claude Opus 5" (same source, verbatim) — so a per-version baseline re-run on Opus 5 should expect both higher subagent counts and higher self-verification token spend from prompts that were tuned to compensate for their absence, and should not read that spend as a capability gain.

### ❌ Single-Model Eval Baselines

**Problem**: Eval suite validated against one Opus version (commonly 4.6); results carried forward without re-running on new releases.
**Symptom**: Silent capability regressions or unexpected cost shifts after a model upgrade. Especially problematic for prompts with vague descriptors, edge-case gestures, or unanchored triggers — 4.7's literal interpretation exposes what 4.6 had been silently generalizing.
**Solution**: Re-run the eval suite on each major model version; treat version migration as a revalidation trigger ([Evidence-Based Revalidation](evidence-based-revalidation.md)). Track per-version pass rates, not just a single headline number.

---

## Related Patterns

- [Subagent Orchestration](./orchestration-comparison.md) - Evaluating multi-agent coordination
- [Context Engineering](./behavioral-insights.md) - Context quality affects eval results
- [Evidence Tiers](./evidence-tiers.md) - Applying evidence standards to eval results
- [Evidence Tiers — Confidence Assessment](./evidence-tiers.md) - Scoring methodology applicable to evals (confidence framework merged in 2026-07-16)

---

## Sources

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Anthropic Engineering, 2026-01-09, Tier A)
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) (Anthropic Engineering, 2026-01-21, Tier A)
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/infrastructure-noise) (Anthropic Engineering, 2026-02-05, Tier A)
- [Eval Awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp) (Anthropic Engineering, 2026-03-06, Tier A) - Eval awareness phenomenon, multi-agent amplification
- [Anthropic: The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (January 2026, Tier A) - Skill success metrics framework
- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) (Anthropic, Delba de Oliveira, 2026-07-22) - **Tier A source, mirror-verified 2026-08-13 (direct fetch blocked by a `claude.com/blog` login-wall redirect; content confirmed via third-party mirror — not direct-fetch-verified).** Four verification-loop patterns (one-off, embedded, chained, permanent PR fixtures); the inline-gating sibling of an offline eval suite
- Hamel Husain & Shreya Shankar, ["LLM Evals: Everything You Need to Know"](https://hamel.dev/blog/posts/evals-faq/) (2026-01-15, **modified 2026-07-18**, Tier B) - Followed canon: error analysis before infrastructure (~20-50 outputs reviewed per significant change, ~100+ traces for saturation); binary evaluations over Likert scales; the custom annotation tool as the single most impactful investment. **2026-07-18 modification** (verified 2026-08-13): a substantial agentic-systems section adding the two-phase eval — black-box task-success grading first, then step-level diagnostics via a transition failure matrix — referencing Claude Code's agentic search. Co-authored, so it also serves as the liveness evidence for Shankar's half of the canon
- Hamel Husain, ["Evals Skills for Coding Agents"](https://hamel.dev/blog/posts/evals-skills/) (2026-03-02, Tier B) - Followed canon: six-skill eval toolkit (error-analysis, generate-synthetic-data, write-judge-prompt, validate-evaluator, evaluate-rag, build-review-interface); action hallucination vs factual hallucination. The plugin teaches a coding agent to audit an eval pipeline; its thesis line — "improving the infrastructure around the agent mattered more than improving the model" — is the canon's core claim
- Hamel Husain, ["AI Product Engineering Notes"](https://hamel.dev/notes/llm/ai-product-engineering/) (2026-08-12, Tier B) - Liveness evidence for the followed canon: a 13-session index, "Nearly every improvement in these notes starts with good evals"
- Shreya Shankar, [papers list](https://sh-reya.com/papers/) (2026, Tier A for the papers list) - CHI 2026 Best Paper "RAG Without the Lag"; co-author with Husain of the O'Reilly "Evals for AI Engineers" book. **Liveness (checked 2026-08-13): solo output quiet — nothing under her own byline since 2026-05-21.** The canon stays alive through the co-authored 2026-07-18 FAQ update; if the joint output also stalls, re-run the follow-lane check before the next revalidation
- [Opus 4.7 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) (Tier A) - Subagent-dispatch default change underpinning the regression eval (superseded on Opus 5 — see below)
- [What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) + [Prompting Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/prompting-claude-opus-5) + [Claude Code changelog](https://code.claude.com/docs/en/changelog) (Tier A, verified 2026-08-13) - Opus 5 (2026-07-24) "delegates to subagents more readily" and "verifies its own work without being told to" (carried-over verification instructions "cause over-verification on Claude Opus 5"); Claude Code v2.1.219 raised default nested-subagent depth 1 → 3. Together these invert the 4.7-era dispatch regression eval into an uncapped-delegation cost eval

*Last updated: 2026-08-13 (followed-canon liveness refresh + Opus 5 delta — Husain active through 2026-08-12 and the joint FAQ modified 2026-07-18 with the agentic two-phase eval section (black-box task success, then transition-failure-matrix step diagnostics); Shankar solo quiet since 2026-05-21, canon still alive via the co-authored update, follow lane held with no advance trigger fired. Added the Anthropic verification-loops post (2026-07-22, four patterns, mirror-verified with the direct-fetch caveat recorded) as the inline-gating sibling of offline evals. Appended the Opus 5 reversal to the implicit-subagent-dispatch anti-pattern: 4.7's too-few-subagents regression risk inverts to uncapped delegation and depth-3 cost, plus the grader-relevant self-verification-without-instruction delta. Frontmatter: `model-version-opus-5` added to `applies-to-signals` — the doc already carried `model-version-migration`. Retained delta and PRODUCTION status unchanged.) Prior: 2026-07-16*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
