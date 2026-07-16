---
evidence-tier: A
convergence: emerging  # Husain/Shankar evals canon recorded in-doc 2026-07-16 (one credible external exemplar cluster for the evals-methodology function)
applies-to-signals: [harness-custom-agents, revalidation-trigger, model-version-migration]
last-verified: 2026-07-16
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

**SDD Phase**: Cross-phase (evaluation informs all phases)

---

## First-Party Eval Methodology (pointer, not a digest)

The methodology walkthrough this doc used to carry — when to start, grader and pattern selection, infrastructure controls, saturation-resistant design, skill success metrics, eval-awareness risk — restated the posts below, so go to them first-party:

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Anthropic Engineering, 2026-01-09, Tier A) — start with 20-50 simple tasks drawn from real failures; three grader types (code-based, model-based, human); `pass@k` / `pass^k` for non-deterministic agents; per-agent-type eval mapping
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) (Anthropic Engineering, 2026-01-21, Tier A) — saturation-resistant design via problem novelty, reduced realism, longer time horizons, and insight over code volume
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/infrastructure-noise) (Anthropic Engineering, 2026-02-05, Tier A) — resource configuration as a first-class experimental variable; infra error rate falls 5.8% to 0.5% from strict enforcement to uncapped resources
- [Eval Awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp) (Anthropic Engineering, 2026-03-06, Tier A) — an eval-aware agent located and decrypted the benchmark answer key; unintended solutions ran 3.7x higher in multi-agent (0.87%) than single-agent (0.24%) configurations
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (Anthropic, January 2026, Tier A) — skill-specific quantitative and qualitative success metrics plus the with/without-skill baseline-comparison template

The commentary layer above those posts — error analysis before infrastructure, binary judgments over Likert scales, annotation tooling as the highest-return investment — is the followed Husain/Shankar canon (Tier B entries in Sources below), and per the follow lane it grows there, not here.

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
- Hamel Husain & Shreya Shankar, ["LLM Evals: Everything You Need to Know"](https://hamel.dev/blog/posts/evals-faq/) (2026-01-15, Tier B) - Followed canon: error analysis before infrastructure (~20-50 outputs reviewed per significant change, ~100+ traces for saturation); binary evaluations over Likert scales; the custom annotation tool as the single most impactful investment
- Hamel Husain, ["Evals Skills for Coding Agents"](https://hamel.dev/blog/posts/evals-skills/) (2026-03-02, Tier B) - Followed canon: six-skill eval toolkit (error-analysis, generate-synthetic-data, write-judge-prompt, validate-evaluator, evaluate-rag, build-review-interface); action hallucination vs factual hallucination
- Shreya Shankar, [papers list](https://sh-reya.com/papers/) (2026, Tier A for the papers list) - CHI 2026 Best Paper "RAG Without the Lag"; co-author with Husain of the O'Reilly "Evals for AI Engineers" book
- [Opus 4.7 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) (Tier A) - Subagent-dispatch default change underpinning the regression eval

*Last updated: 2026-07-16*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
