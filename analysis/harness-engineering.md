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
status: "PRODUCTION"
last-verified: "2026-03-30"
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
| **1000+ PRs in 3 weeks** with ~5 manual IDE edits — review-loop development | Nick Schrock, Dagster founder (Dec 2025) | B |
| **3x velocity** with agents handling commits, changelogs, docs, releases — org transformation | Matthias Vallentin, Tenzir CEO (Dec 2025) | B |

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
| 1M context window fundamentally changes context management strategies | Anthropic model release | A |
| Specification gap: model architecture determines task feasibility | Nate B. Jones (2026) | B |

### Verdict

**The model is necessary but not sufficient. The harness is the multiplier.**

As models improve, the optimal harness gets simpler — but the *need* for harness engineering increases, not decreases. The smartphone analogy holds: when processors commoditized, the OS and ecosystem became the differentiator, not irrelevant.

**Confidence**: Medium-High. The "Less Is More" evidence is strong and convergent across independent sources. The nuancing evidence is real but addresses edge cases rather than undermining the core thesis.

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
- Boris Cherny: Interviews and posts (March 2026) — Parallel sessions, hooks, permissions pre-configuration, Document-and-Clear pattern

### Tier B (Validated / Expert Practitioner)

- Prompt Engineering: ["The AI Model Doesn't Matter Anymore"](https://www.youtube.com/watch?v=1Ohf2aeSPFA) (February 2026) — Full transcript analyzed. Middleware era thesis, three harness properties, Vercel experiment, Manus analysis, Bitter Lesson application
- Vercel: Text-to-SQL experiment (as cited in video) — Removing specialized tools improved all metrics
- Manus: Context engineering lessons (as cited in video, acquired by Meta) — 5 rebuilds, file system as memory
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

---

*Last updated: March 2026*
