# Behavioral Insights: How Claude Code Actually Works

**Evidence Tier**: Mixed (A-B) — Quantified claims from Boris Cherny, Anthropic engineering blog, and practitioner observation

## Purpose

This document collects **quantified behavioral observations** about Claude Code that aren't obvious from documentation alone. These are the "gotchas" and calibration points that distinguish effective usage from naive usage.

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

**Key insight**: Quality degrades *before* the context window fills. The 60% mark is where Boris recommends proactive intervention.

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

Boris Cherny reports CLAUDE.md instructions are followed approximately 80% of the time. This means:
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

### ~150 Instruction Cap

Boris Cherny's observation: Claude Code performance degrades beyond approximately 150 instructions in CLAUDE.md. This aligns with the broader finding that more context doesn't always mean better results.

**Recommendations**:
- Keep CLAUDE.md under 150 lines (60 lines optimal)
- Use progressive disclosure — reference files instead of inlining content
- Skills load ~2% of context budget each; budget accordingly
- 500-line cap on individual SKILL.md files

### Prompt Sensitivity (Opus 4.5/4.6)

Opus 4.5/4.6 models are more responsive to system prompts than earlier models. If prompts were tuned for older models:
- Dial back assertive/aggressive language
- Reduce "ALWAYS"/"NEVER" emphasis (model already more compliant)
- Watch for overtriggering on tool/skill invocation language

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

## Auto Mode Behavior (v2.1.84+)

### Two-Stage Classifier

Auto mode uses a Sonnet 4.6 classifier to pre-approve or pre-deny tool calls:
- **93% approval rate** in production
- Classifier runs *before* the main model sees the tool call
- Non-interactive mode: aborts (doesn't skip) when approval would be needed

**Implication**: Auto mode is viable for most workflows. The 7% denial rate covers genuinely risky operations (file deletion, force push, etc.).

---

## Quantified Claims Summary

| Claim | Source | Confidence |
|-------|--------|------------|
| CLAUDE.md followed ~80% of the time | Boris Cherny (March 2026) | High (Tier A practitioner) |
| Auto-compaction at ~83.5% context | Boris Cherny (March 2026) | High |
| 60% context = quality decline threshold | Boris Cherny (March 2026) | High |
| ~150 instruction cap for CLAUDE.md | Boris Cherny (March 2026) | Medium (observation, not measured) |
| Auto mode 93% approval rate | Anthropic blog (March 2026) | High (Tier A) |
| Extended thinking = 2-3x latency | Boris Cherny (March 2026) | High |
| Skills use ~2% context budget each | Anthropic docs | High (Tier A) |

---

## Sources

- Boris Cherny interviews: Lenny's Podcast, Pragmatic Engineer, Threads mega-posts (March 2026)
- Nate B. Jones: Specification Gap, Agent Build Bible
- CAII (skribblez2718): Johari Window methodology
- RLM paper (Zhang, Kraska, Khattab): Context rot research
- Anthropic Engineering Blog: Auto mode, agent skills (March 2026)

*Merged from: johari-window-ambiguity.md, recursive-context-management.md*
*Last updated: March 2026*
