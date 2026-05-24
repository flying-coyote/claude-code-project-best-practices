---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-03-30"
measurement-claims:
  - claim: "Frontier models score 90%+ on benchmarks but only 24% on real professional tasks"
    source: "Prompt Engineering YouTube - The AI Model Doesn't Matter Anymore"
    date: "2026-02-01"
    revalidate: "2026-08-01"
  - claim: "Vercel text-to-SQL: removing 80% of tools improved accuracy from 80% to 100%"
    source: "Prompt Engineering YouTube (citing Vercel experiment)"
    date: "2026-02-01"
    revalidate: "2026-08-01"
  - claim: "everything-claude-code: 136+ skills, 30 subagents, 119K+ stars"
    source: "GitHub repository analysis"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "superpowers: 294K+ installs, 7-stage mandatory workflow"
    source: "Claude plugin directory + GitHub repository"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "NLH representation: 30.4% to 47.2% performance, 1200 to 34 LLM calls"
    source: "Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723"
    date: "2026-03-26"
    revalidate: "2026-09-26"
  - claim: "Verifiers hurt performance: -0.8 SWE-bench, -8.4 OS World"
    source: "Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723"
    date: "2026-03-26"
    revalidate: "2026-09-26"
  - claim: "Meta-Harness: Rank 1 TerminalBench 2 with Haiku 4.5 via harness optimization"
    source: "Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), arXiv:2603.28052"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "6x performance gap from harness changes alone on the same benchmark"
    source: "Lee et al., Meta-Harness, arXiv:2603.28052 (paper's headline quote)"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "Independent 6x corroboration: Opus 4.5 scores 12% on Cursor vs 2% on OpenCode"
    source: "Tian et al., SWE-Bench Mobile, arXiv:2602.09540"
    date: "2026-02-10"
    revalidate: "2026-08-10"
  - claim: "v2 DAW built in 4 hours for $125 after harness simplification"
    source: "Anthropic engineering blog"
    date: "2026-04-01"
    revalidate: "2026-10-01"
status: PRODUCTION
last-verified: "2026-04-15"
evidence-tier: Mixed
applies-to-signals: [harness-hooks, harness-minimal, harness-comprehensive, commit-bursts, session-error-loop]
revalidate-by: 2026-10-22
---

# Harness Engineering: Diagnostic Framework for Agent Infrastructure

**Evidence Tier**: Mixed (A-B) — Anthropic engineering blog, expert practitioners, production-validated community frameworks

## Purpose

This document evaluates **harness engineering** — the emerging discipline of designing infrastructure around AI coding agents. It defines the concept, compares competing philosophies, and provides a **diagnostic framework** for assessing what's wrong with your agent's harness and how to fix it.

For domain-heavy projects (complex rule ecosystems, specialized tooling), see the companion document: [Domain Knowledge Architecture](./domain-knowledge-architecture.md).

---

## The Harness Thesis

> "The model is not the bottleneck; the harness is."
> — Prompt Engineering, "The AI Model Doesn't Matter Anymore" (February 2026)

The central claim: in 2026, raw model capability is becoming commoditized. The infrastructure wrapped around the model — what it can see, what tools it can use, how it recovers from mistakes, how it tracks progress — determines whether an agent actually works.

### The Evidence Gap Between Benchmarks and Reality

| Metric | Score | Source |
|--------|-------|--------|
| Frontier models on standard benchmarks | 90%+ | Industry benchmarks |
| Frontier models on real professional tasks (1-2 hours) | **24%** | Research study cited in video |
| Same models after 8 attempts | **~40%** | Same study |

**Why the gap?** Researchers found failures were not about model intelligence. The models had the knowledge and could reason through problems. Failures were execution and orchestration:

- Agents got lost after too many steps
- They looped back to approaches already tried and failed
- They lost track of their original objective

These are harness problems, not model problems.

### The Smartphone Analogy

In early smartphones, the processor was the whole story. Eventually processors became fast enough that raw power commoditized. Value migrated to the infrastructure layer: the OS, the camera software, the ecosystem.

The same migration is happening in AI. OpenAI, Anthropic, and Manus all published harness engineering guidance independently in 2025-2026 — converging on the same conclusion from different starting points.

---

## What IS a Harness?

An agent harness is the infrastructure that wraps around the AI model. It manages what the agent sees, what it can do, how it recovers, and how it tracks progress.

### The 6-Layer Harness Stack

| Layer | Components | Purpose | Diagnostic Question |
|-------|-----------|---------|-------------------|
| **Context configuration** | CLAUDE.md, rules/, skills | Shape what the agent knows | "Is the agent working with the right context?" |
| **Behavioral enforcement** | Hooks, permissions, sandboxing | Control what the agent does | "Are critical constraints enforced at 100%?" |
| **Orchestration** | Subagents, agent teams, state files | Coordinate multi-step work | "Does the agent get lost after too many steps?" |
| **Memory & continuity** | Progress files, git, file system | Bridge context boundaries | "Can the agent pick up where it left off?" |
| **Quality gates** | TDD, review patterns, formatters | Ensure output correctness | "How do you know the output is right?" |
| **Domain knowledge** | Resource maps, lookup mechanisms | Make domain expertise findable | "Does the LLM know what resources exist?" |

For deep analysis of the domain knowledge layer, see [Domain Knowledge Architecture](./domain-knowledge-architecture.md).

---

## Three Properties of a Good Harness

Source: "The AI Model Doesn't Matter Anymore" (Tier B — multiple cited studies, detailed analysis)

| Property | Definition | Why It Matters |
|----------|-----------|----------------|
| **Deterministic Replay** | Identical inputs produce comparable action sequences across runs | Without this, debugging an agent is nearly impossible |
| **Observable Boundaries** | Every tool call, API interaction, and decision point is instrumented | You must see exactly where an agent branches or fails |
| **Behavioral Contracts** | Explicit invariants that hold regardless of model temperature or prompt variations | Ensures reliability across model updates and prompt changes |

**Counterintuitive finding**: Developers expect failures to happen in agent logic (bad prompts, hallucinations). In practice, most reliability failures happen in the harness itself — flaky tool mocks, test inputs that don't cover real-world distribution, and the gap between hermetic test environments and production.

**Implication**: Harness-first development — define your behavioral test suite before implementing agent logic. Your harness should act as your specification.

---

## Harness Representation and Optimization

Recent research (March 2026) reveals that **how** a harness is expressed and optimized matters independently of what it does.

### Natural Language Harness (NLH) Representation Gains

Migrating OS Symfony's native code harness into a Natural Language Harness representation produced dramatic improvements:

| Metric | Native Code Harness | NLH Representation | Change |
|--------|--------------------|--------------------|--------|
| Performance | 30.4% | **47.2%** | +55% relative |
| Runtime | 361 min | **141 min** | -61% |
| LLM calls | 1,200 | **34** | -97% |

The harness did the same thing in both cases — the representation changed. This suggests that expressing harness logic in natural language (closer to the model's native reasoning) is a distinct optimization axis from harness design itself.

Source: Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology), ["Natural-Language Agent Harnesses"](https://arxiv.org/abs/2603.25723), 2026-03-26. *(Previously cited in this doc as "Tingua NLH" — corrected to Tsinghua after locating the underlying paper 2026-05-24.)*

### Ablation Evidence: Verifiers Hurt, Self-Evolution Helps

The same Tsinghua/Harbin paper (Pan et al., arXiv:2603.25723) ran ablation studies on harness modules:

| Module | SWE-bench Impact | OS World Impact | Net Effect |
|--------|-----------------|-----------------|------------|
| Verifiers | **-0.8** | **-8.4** | Hurt performance |
| Multi-candidate search | **-2.4** | **-5.6** | Hurt performance |
| Self-evolution (narrowing the agent's own attempt loop) | **+4.8** | **+2.7** | **Only consistently helpful module** |

**Key nuance for harness design**: This challenges the "Quality gates" layer in the harness stack. Explicit verifier modules — separate components that check the agent's work — actively degraded performance. The agent's own iterative refinement (self-evolution) was the only module that consistently helped.

**Caveat**: This is benchmark evaluation, not production deployment. Production environments with real consequences may benefit from verification that benchmarks don't reward. But the default assumption should be: let the agent self-correct rather than bolting on external verifiers.

Source: Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723, 2026-03-26.

### Meta-Harness: Automated Harness Optimization

Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT) treat the harness itself as an optimization target:

- An agentic proposer reads failed execution traces
- It diagnoses breakages and writes a complete new harness
- Cost: ~10M tokens per iteration, 82 files read per round
- Result: **76.4% on TerminalBench-2 with Opus 4.6** (rank 2 among Opus agents) and **37.6% with Haiku 4.5** (rank 1 among Haiku agents, outperforming Goose at 35.5%) — a smaller, cheaper model outranking larger ones through harness optimization alone

**Cross-model transfer**: A harness optimized on one model transferred to five others, improving all of them (+7.7 points on text classification using 4× fewer context tokens; +4.7 points on IMO-level math across five held-out models). This is strong evidence that harness quality is model-independent — good infrastructure helps any model.

**Convergence note**: Andrej Karpathy (Authority 4/5) independently described the same concept — meta-optimization of program.md — without referencing the Stanford+MIT work. Two high-authority sources arriving at the same idea from different directions.

Source: Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), ["Meta-Harness: End-to-End Optimization of Model Harnesses"](https://arxiv.org/abs/2603.28052), 2026-03-30.

### 6× Performance Gap from Harness Changes Alone

The Meta-Harness paper states it as the headline finding: *"Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark."* No model changes, no prompt changes — purely orchestration code.

**Specific replication with full citation**: LangChain's terminal-bench-2 submission moved from outside the top 30 to rank 5 by changing only the harness code. LangChain published the work as ["Improving Deep Agents with Harness Engineering"](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) (2026-02-17): deepagents-cli went **52.8% → 66.5% on TerminalBench-2** (13.7 points) holding gpt-5.2-codex constant. Five specific harness changes were documented: (1) self-verification loop with `PreCompletionChecklistMiddleware`, (2) `LocalContextMiddleware` that maps directory structure and tooling at agent startup, (3) loop-detection middleware tracking per-file edit counts to catch "doom loops," (4) reasoning-budget allocation in a "reasoning sandwich" (xhigh-high-xhigh) across plan/build/verify phases, (5) time-budget warnings injected to encourage completion within timeout. The team published their full TerminalBench traces publicly. Direct quote on what harness engineering is for: *"the purpose of the harness engineer: prepare and deliver context so agents can autonomously complete work."*

**Independent benchmark corroboration**: Tian et al. *SWE-Bench Mobile* ([arXiv:2602.09540](https://arxiv.org/abs/2602.09540), 2026-02-10) reports the same model (Opus 4.5) scoring **12% on Cursor vs 2% on OpenCode** across 22 agent-model configurations — exactly 6×, in a separate venue, on a separate benchmark, from scaffold differences alone. The figure is now replicated, not just cited.

Source: Lee et al., Meta-Harness, arXiv:2603.28052 (primary); Tian et al., SWE-Bench Mobile, arXiv:2602.09540 (independent corroboration).

---

## The "Less Is More" Evidence

The strongest and most counterintuitive finding across all sources.

### The Vercel Experiment

Vercel built a text-to-SQL agent with specialized tools: one for understanding database schemas, one for writing queries, one for validation. Complex error handling. It worked about 80% of the time.

Then they removed 80% of the agent's tools. They gave it basic capabilities — bash, grep, cat.

| Metric | Specialized Tools | General-Purpose Tools | Change |
|--------|------------------|----------------------|--------|
| Accuracy | 80% | **100%** | +25% |
| Token usage | Baseline | **40% of original** | -60% |
| Speed | Baseline | **3.5x faster** | +250% |

### The Manus Experience

Manus (acquired by Meta) rebuilt their agent framework five times in six months. Their biggest performance gains came from **removing features** — ripping out complex document retrieval and fancy routing logic, replacing them with general-purpose shell executions and structured handoffs.

They also solved a critical memory problem: tasks requiring ~50 tool calls caused performance degradation even with large context windows (signal drowned by noise). Solution: treat the file system as external memory. Write important information to markdown files; read when needed.

### Claude Code's Own Design

Claude Code uses just **four core tools**: read, write, edit, run bash. Extensibility comes through MCP protocol, not tool proliferation. This minimal harness with maximum model autonomy aligns with the evidence.

### The Bitter Lesson (Richard Sutton, Applied to Agents)

Sutton's core argument: approaches that scale with computational power always beat approaches relying on human-engineered domain knowledge.

Applied to agent harnesses: **as models get smarter, your harness should get simpler**. If you are adding hand-coded logic and specialized routing with every model upgrade, you are swimming against the current.

> "Every piece of your harness should be built for deletion — ready to be removed when the model no longer needs it."

### v2 Harness Simplification (Anthropic, April 2026)

Anthropic's Claude Code v2 with Opus 4.6 provides concrete evidence for "harness should simplify as models improve":

- **Removed**: Sprints, contract negotiation, context resets
- **Replaced with**: Single build session with evaluator at the end only
- **Result**: DAW built in 4 hours for $125

This is a vendor demonstrating the Bitter Lesson on their own product — stripping orchestration complexity because the model no longer needs it. The evaluator-at-the-end pattern also aligns with the ablation evidence above: self-evolution during work, verification only at completion.

**Caveat — vendor-side regression in the same window**: The same vendor shipped a quality regression spanning March 4 – April 20, 2026 ([April 23 postmortem](https://www.anthropic.com/engineering/april-23-postmortem)) — reasoning-effort default flipped to `medium`, an extended-thinking-block caching bug, and a system-prompt verbosity cap that hurt coding quality. None of these invalidate the v2 simplification thesis (the orchestration changes were a separate workstream), but they demonstrate that "trust the vendor's defaults" is the wrong reading. Harness designers should pin effort levels explicitly and treat vendor-side defaults as version-anchored. See [Behavioral Insights — April 2026 Postmortem](behavioral-insights.md#vendor-side-quality-regression-case-study-the-april-2026-postmortem) for the full analysis.

Source: Anthropic engineering blog, April 2026. Authority 5/5.

### Harness Toolkit Additions (Q2 2026)

Concrete harness-layer primitives shipped in Claude Code changelog v2.1.117 → v2.1.150 (verified 2026-05-24) that change what's expressible in the harness without requiring custom code:

| Primitive | Version | What it enables | Pattern impact |
|---|---|---|---|
| `/goal` command (research preview) | v2.1.140 | Set a completion condition; a fast-model checker evaluates after every turn, Claude loops until it holds. Works in interactive, `-p`, and Remote Control. | Replaces ad-hoc "did we finish? check it" prompts and external loop scripts with a first-class completion-loop primitive. |
| Hooks invoke MCP tools directly via `type: "mcp_tool"` | v2.1.118 | A hook can call an MCP tool without spawning a subprocess. | Eliminates the process-spawn overhead that made MCP-from-hook patterns expensive; closes a gap that previously pushed users toward custom subagents. |
| `continueOnBlock` PostToolUse option | v2.1.136 | When a PostToolUse hook rejects, feed the rejection reason back to Claude and continue the turn (instead of failing the turn). | Hooks become advisory-corrective, not just terminating; aligns with the "self-evolution > verifiers" finding from Pan et al. (arXiv:2603.25723) by letting the agent recover from rejections rather than aborting. |
| `worktree.bgIsolation` setting | v2.1.143 | Background sessions auto-isolate into git worktrees under `.claude/worktrees/`; `"none"` opts out. | Replaces manual worktree juggling; pairs with the `claude agents` TUI (see [Orchestration Comparison](orchestration-comparison.md)). |
| Per-category `/usage` breakdown | v2.1.144 | Cost breakdown by category: skills, subagents, plugins, MCP servers. | Makes the MCP-vs-Skills economic comparison ([MCP vs Skills Economics](mcp-vs-skills-economics.md)) measurable in your own project without external instrumentation. |
| `${CLAUDE_EFFORT}` in skills, `effort.level` in hooks | v2.1.120, v2.1.128 | Skills and hooks can read the current effort level. | Effort becomes a first-class signal; enables conditional skill/hook behavior without parsing `/effort` state externally. |

These are toolkit additions, not architectural shifts. They reduce the gap between "what the harness can express natively" and "what users were patching in with bash scripts and brittle parsing." None of them change the H-HARNESS-01 thesis; all of them lower the marginal cost of building a competent harness.

Source: [Anthropic Claude Code changelog](https://code.claude.com/docs/en/changelog), v2.1.117 → v2.1.150. Tier A.

### Counter-signal: Opus 4.7 Pushes *Prompt* Complexity Up (April 2026)

The Bitter Lesson predicts monotonic simplification as models improve. Opus 4.7 complicates the picture: the *harness* continues to simplify (Anthropic's migration guide confirms "fewer subagents spawned by default," "fewer tool calls by default"), but the *prompt* may need to be **more explicit**, not less.

4.7's literal interpretation (see [Model Migration Anti-Patterns](model-migration-anti-patterns.md)) means instructions that 4.6 successfully generalized now fail silently. Remediation per the Anthropic migration guide: enumerate cases, anchor triggers, declare dispatch mechanism, add verbosity directives. These are prompt-side additions, not harness-side.

**Diagnostic split for 4.7**:

| Layer | Direction | Evidence |
|---|---|---|
| Harness (orchestration, tooling, subagent wiring) | ↓ Simpler | Anthropic migration guide: fewer default subagents, fewer tool calls |
| Prompt (instructions, CLAUDE.md, skill bodies) | ↑ More explicit | Anthropic migration guide: literal interpretation, no silent generalization |

This does not invalidate the Bitter Lesson — the *orchestration* around the model is still simplifying. But the prompt itself is a joint product of human intent and model inference, and 4.7 shifts the inference burden back to the human. Treat this as version-scoped: a future model that re-adds intent inference would reverse the prompt-complexity pressure.

Source: Anthropic migration guide (April 2026), [Model Migration Anti-Patterns](model-migration-anti-patterns.md). Authority 5/5 (Tier A).

### Convergence of Architectures

Three leading systems arrived at the same insight from different starting points:

| System | Architecture | Core Philosophy |
|--------|-------------|----------------|
| **OpenAI Codex** | 3-layer (Orchestrator, Executor, Recovery) | Robust layering with clear separation |
| **Claude Code** | 4 core tools + MCP extensibility | Minimal harness, maximum model autonomy |
| **Manus** | "Reduce, offload, isolate" + file system memory | Simplification as the primary optimization |

---

## Three Harness Philosophies in Practice

The Claude Code ecosystem offers three competing approaches. Comparing them reveals trade-offs, not a single right answer.

| Dimension | Maximal (ECC) | Disciplined (Superpowers) | Minimal (Anthropic) |
|-----------|---------------|---------------------------|---------------------|
| **Philosophy** | Batteries-included | Methodology-enforced | Principle-guided |
| **Scale** | 136+ skills, 30 subagents, 60+ commands | 7-stage workflow, ~14 skills | 2-agent architecture + external artifacts |
| **Enforcement** | Runtime profiles (minimal/standard/strict) | Mandatory stages (deletes code written before tests) | Guidelines + conventions |
| **Context strategy** | Continuous learning pipeline (instincts → skills) | Fresh context per subagent with structured review | One feature at a time + progress files |
| **Memory model** | SQLite state store + instinct pipeline | Fresh per subagent (no accumulation) | File system as external memory |
| **Failure mode** | Context bloat, hook storms, over-engineering | Ceremony overhead for small tasks | Drift without enforcement |
| **Setup cost** | High (full plugin install + configuration) | Medium (plugin install, workflow automatic) | Low (CLAUDE.md + progress file) |
| **Bitter Lesson alignment** | Low (adds complexity with each release) | Medium (enforces process, not implementation) | High (minimal, built for deletion) |
| **Domain knowledge approach** | 136+ skills load domain-specific knowledge | Skills enforce methodology per domain | CLAUDE.md + progress files |
| **Evidence tier** | B (119K+ stars, Anthropic hackathon winner) | B (294K+ installs, cross-platform) | A (Anthropic engineering blog) |
| **Best for** | Teams wanting comprehensive tooling out of the box | Teams wanting enforced discipline without building infrastructure | Greenfield or minimal-dependency projects |

**Measurement note**: GitHub stars (ECC) and plugin installs (Superpowers) are different metrics measuring different things. They should not be compared directly.

**Key observation**: ECC's comprehensive approach works against the "Less Is More" evidence but provides value through runtime profiles that let you dial complexity up or down (`ECC_HOOK_PROFILE=minimal`). Superpowers enforces process without adding tools, aligning better with the Vercel/Manus findings. Anthropic's minimal approach most closely matches the convergence pattern.

---

## Diagnostic Framework: What's Wrong With My Harness?

Use this table to diagnose common agent reliability problems. Each symptom maps to a likely root cause and a specific remediation.

| Symptom | Likely Diagnosis | Root Cause | Recommended Action | Reference |
|---------|-----------------|------------|-------------------|-----------|
| Agent gets lost after many steps | Missing state persistence | No external memory, context rot | Add progress file + document-and-clear pattern | [Behavioral Insights](./behavioral-insights.md) — 60% threshold |
| Agent loops on failed approaches | No error recovery mechanism | Harness doesn't track what's been tried | Implement failure tracking in progress file | [Anthropic harness blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| Agent ignores project conventions | Over-reliance on CLAUDE.md | ~80% adherence rate, no enforcement | Move critical rules to hooks (100% enforcement) | [Behavioral Insights](./behavioral-insights.md) — CLAUDE.md adherence |
| Agent overwhelmed by tools | Tool proliferation | Too many specialized tools | Strip to general-purpose tools (Vercel pattern) | "Less Is More" evidence above |
| Quality degrades mid-session | Context rot | Working beyond 60% context capacity | Implement Document & Clear, subagent delegation | [Behavioral Insights](./behavioral-insights.md) — context thresholds |
| Slow, expensive sessions | Context bloat from plugins/skills | Too many skills loaded (~2% context each) | Audit skill count, use path-scoped rules | [Plugins & Extensions](./plugins-and-extensions.md) |
| Works in test, fails in production | Hermetic/production gap | Test harness differs from production | Layered testing: hermetic for units, production-like for integration | Three properties above |
| Small tasks take too long | Ceremony overhead | Overly rigid workflow enforcement | Scale harness to task size (see decision tree below) | Superpowers pattern analysis |
| Inconsistent across runs | Missing behavioral contracts | No explicit invariants | Define harness-level contracts independent of model | Three properties above |
| Can't debug agent failures | Missing observability | Tool calls and decisions not instrumented | Add observable boundaries at each harness layer | Three properties above |
| Team gets different results | Configuration drift | No enforcement, relying on advisory CLAUDE.md | Standardize via hooks + shared settings.json | [Plugins & Extensions](./plugins-and-extensions.md) |
| LLM reinvents instead of reusing | Domain knowledge not discoverable | No resource map or lookup mechanism | See [Domain Knowledge Architecture](./domain-knowledge-architecture.md) | Companion document |
| Context overwhelmed by domain docs | Domain knowledge not progressive | Everything loaded at once, no disclosure layers | See [Domain Knowledge Architecture](./domain-knowledge-architecture.md) | Companion document |

---

## Decision Tree: How Much Harness Do You Need?

```
START: What is your task complexity?
│
├─ Simple (single file, <30 min)
│   → MINIMAL HARNESS
│   CLAUDE.md + permissions only
│   Resource: Anthropic best practices blog
│
├─ Medium (multi-file, 1-4 hours)
│   → DISCIPLINED HARNESS
│   Add: hooks for enforcement, progress file, TDD workflow
│   Resource: superpowers plugin, Anthropic harness blog
│
├─ Complex (multi-session, days)
│   → STRUCTURED HARNESS
│   Add: subagent orchestration, state persistence, quality gates
│   Resource: orchestration-comparison.md, framework-selection-guide.md
│
├─ Domain-heavy (specialized ecosystems, complex rule languages)
│   → STRUCTURED + DOMAIN LAYER
│   Add: resource maps, path-scoped rules, domain methodology skills
│   Resource: domain-knowledge-architecture.md
│
└─ Enterprise (team-wide, ongoing)
    → COMPREHENSIVE HARNESS
    Add: runtime profiles, continuous learning, plugin governance
    Resource: everything-claude-code, plugins-and-extensions.md
    WARNING: Start here only with evidence. Most projects over-engineer.
```

**Critical principle**: Start minimal. Add complexity only when you have evidence that the current harness is failing. The Vercel and Manus experiences show that removing harness complexity often improves outcomes.

---

## The "Model Doesn't Matter" Thesis: Evaluation

### Evidence Supporting the Thesis

| Evidence | Source | Tier |
|----------|--------|------|
| Harness design was the breakthrough for long-running agents | Anthropic engineering blog (Nov 2025) | A |
| 90%+ on benchmarks / 24% on real tasks — the gap is harness | Research study cited in video | B |
| Removing tools improved accuracy, speed, and cost (Vercel) | Vercel experiment cited in video | B |
| Removing features was the primary optimization (Manus) | Manus context engineering (5 rebuilds) | B |
| Same harness works across Claude Code, Cursor, OpenCode, Codex | everything-claude-code cross-platform support | B |
| Boris Cherny's success depends on parallel sessions, hooks, permissions — all harness | Boris Cherny interviews (March 2026) | A |
| NLH representation: same harness logic, 30.4% → 47.2% perf + 1200 → 34 LLM calls | Pan et al. (Tsinghua + Harbin IT), [arXiv:2603.25723](https://arxiv.org/abs/2603.25723) (March 2026) | B |
| Meta-Harness: Haiku 4.5 ranks #1 among Haiku agents on TerminalBench-2 via harness optimization alone | Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), [arXiv:2603.28052](https://arxiv.org/abs/2603.28052) (March 2026) | B |
| **"Changing the harness around a fixed LLM can produce a 6× performance gap on the same benchmark"** (paper's headline quote) | Lee et al., Meta-Harness, [arXiv:2603.28052](https://arxiv.org/abs/2603.28052) (March 2026) | B |
| Independent corroboration: Opus 4.5 scores 12% on Cursor vs 2% on OpenCode — exactly 6×, scaffold-only | Tian et al., SWE-Bench Mobile, [arXiv:2602.09540](https://arxiv.org/abs/2602.09540) (Feb 2026) | B |
| v2 harness simplification: removed sprints/negotiation, DAW in 4h/$125 | Anthropic engineering blog (April 2026) | A |
| **1000+ PRs in 3 weeks** with ~5 manual IDE edits — review-loop development | Nick Schrock, Dagster founder (Dec 2025) | B |
| **3x velocity** with agents handling commits, changelogs, docs, releases — org transformation | Matthias Vallentin, Tenzir CEO (Dec 2025) | B |
| Grep with a good harness ≥ vector retrieval on LongMemEval across 4 harnesses; scores depend strongly on harness regardless of retrieval choice | Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US), [arXiv:2605.15184](https://arxiv.org/abs/2605.15184) (May 2026) | B |

### Production-Scale Agent-Driven Development (New Evidence, April 2026)

Two high-credibility practitioners independently validated that agent-driven development achieves transformational velocity when the harness is right:

**Nick Schrock (Dagster)** — Merged 1,000+ PRs in 3 weeks with approximately 5 manual IDE edits. His workflow: local dev -> cloud code review -> one command -> agent applies feedback. CI errors: downloads logs, agent fixes automatically. Key quote: "This isn't vibe coding. The process is still software engineering forward." The IDE becomes a read-only interface; code review in the browser is the primary editing surface.

**Matthias Vallentin (Tenzir)** — Achieved 3x velocity improvement with agents handling commits, changelogs, docs, and releases. Framed as engineering org transformation, not individual productivity. This is the same team whose MCP vs Skills production data (see [MCP vs Skills Economics](./mcp-vs-skills-economics.md)) showed 50% cost reduction through architecture choices.

**What makes this harness evidence**: Both practitioners emphasize that the velocity gains came from the review-loop workflow (harness) not from model improvements. Schrock's one-command CI fix cycle and Vallentin's agent-managed release process are harness engineering — giving agents the right tools, permissions, and recovery mechanisms.

### Evidence Nuancing the Thesis

| Evidence | Source | Tier |
|----------|--------|------|
| Lower-tier models (Haiku, Flash) still need more structured tooling | Video acknowledgment | B |
| Model version changes (Opus 4.5→4.6) require harness retuning | Behavioral Insights — prompt sensitivity | A |
| Opus 4.7 literalism pushes *prompt* complexity up while harness simplifies | Anthropic migration guide (April 2026) | A |
| 1M context window fundamentally changes context management strategies | Anthropic model release | A |
| Specification gap: model architecture determines task feasibility | Nate B. Jones (2026) | B |
| Explicit verifier modules hurt benchmark performance (-0.8 SWE, -8.4 OS World) | Pan et al. (Tsinghua + Harbin IT), [arXiv:2603.25723](https://arxiv.org/abs/2603.25723) (March 2026) | B |

**Practical implication of the nuancing evidence**: The "harness simplifies as models improve" thesis holds, but three specific decisions should be hedged:

1. **Don't strip harness for lower-tier models.** If your project routes some tasks to Haiku for cost reasons, the harness those tasks need is *not* the same as the harness Opus needs. Keep fallback scaffolding for cheaper models rather than optimizing for the top tier only.
2. **Retune prompts on every model release, even if the harness is unchanged.** Opus 4.6 → 4.7 is the canonical case: the harness did not need to change, but prompt idioms that assumed inferred intent silently regressed. See [model-migration-anti-patterns.md](model-migration-anti-patterns.md).
3. **Don't add verifier modules prophylactically.** The Pan et al. ablation (arXiv:2603.25723) is narrow but pointed: explicit verifiers hurt benchmark performance. Reserve verification for where you have evidence the agent is getting it wrong, not as a default safety layer.

### Verdict

**The model is necessary but not sufficient. The harness is the multiplier.**

As models improve, the optimal harness gets simpler — but the *need* for harness engineering increases, not decreases. The smartphone analogy holds: when processors commoditized, the OS and ecosystem became the differentiator, not irrelevant.

**Confidence**: Medium-High. The "Less Is More" evidence is strong and convergent across independent sources. The nuancing evidence is real but addresses edge cases rather than undermining the core thesis.

---

## Hypothesis Status and Falsifiability

This document's thesis is tracked across repositories as **H-HARNESS-01: Harness Engineering Yields Larger Gains Than Model Upgrades**. Consolidating the evidence in one place lets future revalidations check the claim systematically rather than re-deriving it from scattered sources.

### Consolidated Claim

> Investing in agent harness architecture (orchestration, memory, verification, state management) yields larger, faster, and more reliable performance gains than waiting for the next model upgrade.

**Current evidence-tier**: B+ leaning A. The Meta-Harness primary source ([arXiv:2603.28052](https://arxiv.org/abs/2603.28052), Lee/Nair/Zhang/Lee/Khattab/Finn, Stanford+MIT, 2026-03-30) and the Tsinghua NLH paper ([arXiv:2603.25723](https://arxiv.org/abs/2603.25723), Pan et al., 2026-03-26) are now both located and registered (resolution: 2026-05-24). The 6× orchestration-only figure is the Meta-Harness paper's headline quote and is independently corroborated by SWE-Bench Mobile ([arXiv:2602.09540](https://arxiv.org/abs/2602.09540), Opus 4.5: 12% Cursor / 2% OpenCode). Karpathy's independent convergence on meta-optimization (Authority 4/5) and Anthropic's v2 simplification with Opus 4.6 (Authority 5/5, Tier A) remain the strongest practitioner corroboration.

### Falsifiability

The claim is falsifiable in a single test:

> **Find a benchmark where a model upgrade (e.g., Sonnet → Opus) holding harness constant provides >6× improvement.**

Such a result would invalidate the "harness is the multiplier" framing — if a pure model swap can match the Stanford-reported 6× orchestration-only delta, then the harness-vs-model trade-off collapses to a routine optimization rather than a structural shift. As of 2026-05-24, no such benchmark has surfaced; the dominant cross-model deltas reported in 2026 (TerminalBench 2, SWE-bench, OSWorld) sit well below 6× even across major version jumps.

### Outstanding Provenance Gaps — Resolved 2026-05-24

All three previously-tracked provenance gaps were closed by an academic-source sweep on 2026-05-24:

- **~~Stanford 6×-orchestration figure~~** — **RESOLVED**. The figure originates from the Meta-Harness paper itself (Lee et al., [arXiv:2603.28052](https://arxiv.org/abs/2603.28052), 2026-03-30) where it appears verbatim: *"Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark."* The earlier "Stanford researchers via synthesis transcript" attribution and the "Meta-Harness paper" tracking item resolve to the same single source. The figure is independently corroborated by SWE-Bench Mobile (Tian et al., [arXiv:2602.09540](https://arxiv.org/abs/2602.09540), 2026-02-10), which reports Opus 4.5 scoring 12% on Cursor vs 2% on OpenCode — exactly 6×, scaffold-only.
- **~~Meta-Harness paper~~** — **RESOLVED**. Full citation: Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT). "Meta-Harness: End-to-End Optimization of Model Harnesses." [arXiv:2603.28052](https://arxiv.org/abs/2603.28052), 2026-03-30. Result quantification corrected: 76.4% with Opus 4.6 (rank 2 among Opus agents) and 37.6% with Haiku 4.5 (rank 1 among Haiku agents, beating Goose at 35.5%).
- **~~Tingua NLH ablation~~** — **RESOLVED with attribution correction**. "Tingua" was a misspelling of Tsinghua. Full citation: Pan, Zou, Guo, Ni, Zheng (Tsinghua University, Shenzhen International Graduate School + Harbin Institute of Technology). "Natural-Language Agent Harnesses." [arXiv:2603.25723](https://arxiv.org/abs/2603.25723), 2026-03-26. All ablation numbers in this doc (verifiers -0.8 SWE / -8.4 OSWorld; multi-candidate search -2.4 / -5.6; self-evolution +4.8 / +2.7) match the paper exactly.

**Net effect on hypothesis strength**: H-HARNESS-01 moves from "B+ with three outstanding gaps" to "B+ with primary sources verified." The headline 6× figure is no longer transcript-only; it is the paper's published claim, independently replicated.

### Cross-Repository Tracking

The hypothesis is mirrored in a personal hypothesis tracker (`project1/01-knowledge-base/hypotheses/relocated-out-of-scope.md`) that aggregates evidence across the author's portfolio (security data, MCP prototypes, second-brain). Findings flow into this document; tracker-side updates do not propagate automatically — revalidation should consult both. The tracker also lists adjacent cross-brain evidence (Splunk benchmark, CAII Johari Window) that supports the thesis indirectly via the workflows the harness optimizes for, not the harness mechanics themselves; those references are deliberately not duplicated here.

---

## Where Failure Actually Lives

The most counterintuitive finding: developers expect failures in agent logic (bad prompts, hallucinations). In practice, **most reliability failures happen in the harness itself**.

| Failure Location | Expected | Actual |
|-----------------|----------|--------|
| Agent logic (prompts, reasoning) | Primary source | Secondary |
| **Harness infrastructure** | Secondary | **Primary** |

### Common Harness Failures

- **Flaky tool mocks** that differ from production environments
- **Test inputs** that don't cover real-world data distribution
- **Hermetic/production gap** — isolated tests are fast and reproducible, but the gap between them and production is where the worst bugs hide

### Recommended Testing Strategy

1. **Hermetic testing** for unit-level agent behaviors (fast, reproducible)
2. **Production-like testing** for integration behaviors (catches the real bugs)
3. **Harness-first development** — define behavioral test suite before implementing agent logic

---

## Anti-Patterns

| Anti-Pattern | Source | Symptom | Fix |
|-------------|--------|---------|-----|
| Tool proliferation | Vercel experiment | Low accuracy despite many specialized tools | Strip to general-purpose tools |
| Context stuffing | Manus experience | Performance degrades at 50+ tool calls | File system as external memory |
| Hook storms | ECC patterns | Excessive token consumption from cascading hooks | Runtime profiles (`ECC_HOOK_PROFILE=minimal`) |
| Ceremony overhead | Superpowers pattern | Small tasks take disproportionate time | Scale harness to task complexity |
| Configuration drift | Anthropic minimal | Team members get inconsistent results | Hooks for enforcement + shared settings.json |
| Swimming against the current | Bitter Lesson | Harness complexity grows with each model upgrade | Build every component for deletion |
| Harness-as-specification neglect | Video thesis | Building agent first, retrofitting tests later | Define harness (behavioral tests) before agent logic |

---

## Resource Map: Where to Go for What

| Need | Resource | Type |
|------|----------|------|
| Understand context behavior and thresholds | [Behavioral Insights](./behavioral-insights.md) | This project |
| Choose between extension mechanisms | [Plugins & Extensions](./plugins-and-extensions.md) | This project |
| Compare orchestration approaches | [Orchestration Comparison](./orchestration-comparison.md) | This project |
| Select a framework for your project | [Framework Selection Guide](./framework-selection-guide.md) | This project |
| Structure domain knowledge for LLMs | [Domain Knowledge Architecture](./domain-knowledge-architecture.md) | This project |
| Assess cost trade-offs (MCP vs Skills) | [MCP vs Skills Economics](./mcp-vs-skills-economics.md) | This project |
| Implement a maximal harness | [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | External |
| Implement a disciplined workflow | [superpowers](https://github.com/obra/superpowers) | External |
| Implement a minimal long-running harness | [Anthropic harness blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | External |
| Harden security layer | [Safety & Sandboxing](./safety-and-sandboxing.md) + [Secure Code Generation](./secure-code-generation.md) | This project |
| See harness concepts operationalized with 7-repo evidence | [Agent-Driven Development](./agent-driven-development.md) | This project |

---

## Sources

### Tier A (Primary Vendor)

- Anthropic: ["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (November 2025) — Two-part architecture, external artifacts as memory, one feature at a time
- Anthropic: v2 harness simplification with Opus 4.6 (April 2026) — Removed sprints/negotiation/resets, single build session, evaluator-at-the-end pattern
- Anthropic: [Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) (April 2026) — Opus 4.7 literal interpretation, fewer default subagents, adaptive verbosity; pushes prompt complexity up while harness simplifies
- Boris Cherny: Interviews and posts (March 2026) — Parallel sessions, hooks, permissions pre-configuration, Document-and-Clear pattern

### Tier B (Validated / Expert Practitioner)

- Prompt Engineering: ["The AI Model Doesn't Matter Anymore"](https://www.youtube.com/watch?v=1Ohf2aeSPFA) (February 2026) — Full transcript analyzed. Middleware era thesis, three harness properties, Vercel experiment, Manus analysis, Bitter Lesson application
- Vercel: Text-to-SQL experiment (as cited in video) — Removing specialized tools improved all metrics
- Manus: Context engineering lessons (as cited in video, acquired by Meta) — 5 rebuilds, file system as memory
- Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology): ["Natural-Language Agent Harnesses"](https://arxiv.org/abs/2603.25723) — arXiv:2603.25723, 2026-03-26. NLH representation gains (30.4% → 47.2%, 1,200 → 34 LLM calls), verifier/multi-candidate ablation, self-evolution as only consistently helpful module. *(Previously cited as "Tingua NLH" — attribution corrected 2026-05-24.)*
- Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT): ["Meta-Harness: End-to-End Optimization of Model Harnesses"](https://arxiv.org/abs/2603.28052) — arXiv:2603.28052, 2026-03-30. Agentic proposer reads failed traces, writes new harness. 76.4% Opus 4.6 / 37.6% Haiku 4.5 on TerminalBench-2 (rank 1 among Haiku agents). Cross-model harness transfer (+7.7 text-classification, +4.7 IMO math across five held-out models). **Source for "6× performance gap from harness changes alone" headline figure.**
- Tian, Wang, Yang et al.: ["SWE-Bench Mobile: Can LLM Agents Develop Industry-Level Mobile Apps?"](https://arxiv.org/abs/2602.09540) — arXiv:2602.09540, 2026-02-10. Independent corroboration: same Opus 4.5 model scores 12% on Cursor vs 2% on OpenCode (exactly 6×, scaffold-only) across 22 agent-model configurations.
- Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US): ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — arXiv:2605.15184, May 2026. 116-question LongMemEval study across Chronos, Claude Code, Codex, Gemini CLI. Two findings cited here: (1) grep generally yields higher accuracy than vector retrieval; (2) "overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same" — direct empirical support for harness-as-multiplier across retrieval strategies. Tier B preprint, not yet peer-reviewed.
- Andrej Karpathy: Meta-optimization of program.md (March 2026, No Priors podcast) — Independent convergence with Stanford meta-harness concept. Authority 4/5.
- LangChain DeepAgents team: ["Improving Deep Agents with Harness Engineering"](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) (2026-02-17) — deepagents-cli moved 52.8% → 66.5% on TerminalBench-2 (outside Top 30 → Top 5) holding gpt-5.2-codex constant; five specific middleware changes documented; full TerminalBench traces published. Practitioner replication of the harness-as-multiplier effect with a public reproducible artifact. Authority 4/5.
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — 119K+ stars, Anthropic hackathon winner, maximal harness approach
- [superpowers](https://github.com/obra/superpowers) — 294K+ installs, disciplined methodology approach
- Richard Sutton: "The Bitter Lesson" — Approaches scaling with compute beat hand-engineered knowledge

### Related Analysis

- [Behavioral Insights](./behavioral-insights.md) — Context thresholds, CLAUDE.md adherence, prompt sensitivity
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — Companion document for domain-heavy projects
- [Plugins & Extensions](./plugins-and-extensions.md) — The harness toolkit (8 extension mechanisms)
- [Orchestration Comparison](./orchestration-comparison.md) — Orchestration layer analysis
- [Framework Selection Guide](./framework-selection-guide.md) — Framework decision trees
- [Agent Principles](./agent-principles.md) — Persistent memory, unpredictability, monitoring
- [Model Migration Anti-Patterns](./model-migration-anti-patterns.md) — Six prompt anti-patterns that break on Opus 4.7; split between harness (simpler) and prompt (more explicit)

---

*Last updated: April 2026*
