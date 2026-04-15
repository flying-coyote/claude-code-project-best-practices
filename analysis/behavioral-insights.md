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

### ~150 Instruction Cap (Convergent Evidence)

The ~150 instruction cap is now independently validated by multiple high-authority sources:

| Source | Authority | Basis |
|--------|-----------|-------|
| Boris Cherny (Claude Code creator) | 5/5 | Direct practitioner observation |
| Dexter Horthy (RPI/CRISPY creator) | 4/5 | Cites arXiv paper via Kyle's blog |

This upgrades the claim from single-source expert guidance to **convergent practitioner evidence** — different practitioners, different data sources, same conclusion. The cap appears to be a genuine behavioral boundary, not an artifact of one person's workflow.

**Recommendations**:
- Keep CLAUDE.md under 150 lines (60 lines optimal)
- Use progressive disclosure — reference files instead of inlining content
- Skills load ~2% of context budget each; budget accordingly
- 500-line cap on individual SKILL.md files
- Split mega-prompts with 85+ instructions into phases with <40 instructions each (see Design Rule below)

### Prompt Sensitivity (Opus 4.5/4.6)

Opus 4.5/4.6 models are more responsive to system prompts than earlier models. If prompts were tuned for older models:
- Dial back assertive/aggressive language
- Reduce "ALWAYS"/"NEVER" emphasis (model already more compliant)
- Watch for overtriggering on tool/skill invocation language

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
| ~150 instruction cap for CLAUDE.md | Boris Cherny + Dexter Horthy (convergent) | **High** (upgraded: convergent evidence) |
| Auto mode 93% approval rate | Anthropic blog (March 2026) | High (Tier A) |
| Extended thinking = 2-3x latency | Boris Cherny (March 2026) | High |
| Skills use ~2% context budget each | Anthropic docs | High (Tier A) |
| Jaggedness: verifiable domains improve, non-verifiable stagnate | Karpathy (March 2026) | Medium-High (Authority 4/5, conceptual framework) |
| Self-evaluation: identifies then rationalizes issues away | Anthropic engineering blog | High (Tier A, vendor self-disclosure) |
| Monitor tool requires explicit prompting for interrupt-based mode | Anthropic (April 2026) | High (Tier A) |
| Mega-prompts with 85+ instructions cause inconsistent adherence | Horthy (CRISPY creator) | Medium-High (Authority 4/5) |

---

## Sources

- Boris Cherny interviews: Lenny's Podcast, Pragmatic Engineer, Threads mega-posts (March 2026)
- Dexter Horthy (RPI/CRISPY creator): Vertical planning, control flow design rule, ~150 instruction convergent validation (via arXiv paper/Kyle's blog)
- Andrej Karpathy: No Priors podcast (March 2026) — Jaggedness principle, verifiable vs non-verifiable domain axis
- Nate B. Jones: Specification Gap, Agent Build Bible
- CAII (skribblez2718): Johari Window methodology
- RLM paper (Zhang, Kraska, Khattab): Context rot research
- Anthropic Engineering Blog: Auto mode, agent skills (March 2026), self-evaluation failure mode, Monitor tool (April 2026)

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — The ~80% CLAUDE.md adherence rate and 60% context threshold are primary motivators for harness enforcement design
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — Context budget framework and progressive disclosure patterns build directly on the thresholds documented here
- [Agent-Driven Development](./agent-driven-development.md) — Commit burst patterns and ~80% adherence rate motivating hook-based security enforcement in practice

---

*Merged from: johari-window-ambiguity.md, recursive-context-management.md*
*Last updated: April 2026*
