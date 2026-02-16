---
version-requirements:
  claude-code: "v2.1.30+"  # Session memory feature
  model: "Opus 4.6+"       # Think tool and fast mode
measurement-claims:
  - claim: "Prompt represents only 0.1% of total context processed"
    source: "Anthropic Engineering Blog"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "Memory Tool + Context Editing: 39% improvement in agent search performance"
    source: "Anthropic internal testing"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "Context editing alone: 29% improvement"
    source: "Anthropic internal testing"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "Token consumption in 100-round search: 84% reduction"
    source: "Anthropic internal testing"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "HNSW Vector Memory: 150x-12,500x faster pattern retrieval"
    source: "Claude-Flow framework"
    date: "2025-10-15"
    revalidate: "2026-10-15"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Context Engineering

**Sources**:
- [Anthropic - Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Evidence Tier A)
- [Nate B. Jones - Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive) (Evidence Tier B)

**Evidence Tier**: A (Primary vendor documentation)

**SDD Phase**: Specify (context as specification artifacts)

## The Core Insight

> "Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of 'what configuration of context is most likely to generate our model's desired behavior?'"
> — Anthropic Engineering Blog

Traditional prompt engineering focuses on what you *tell* the AI. Context engineering focuses on what the AI *discovers* and how context is curated throughout inference.

When Claude researches a topic, your prompt may represent only 0.1% of the total context it actually processes. This fundamentally shifts how we should design AI systems.

## Two-Layer Architecture

### Deterministic Context (User-Controlled)
- System prompts and instructions
- CLAUDE.md project files
- Uploaded documents
- Explicit tool definitions

### Probabilistic Context (AI-Discovered)
- Information found through tool use
- Web search results
- File exploration
- MCP server responses

**Design Principle**: Structure your deterministic context to guide probabilistic discovery. Don't try to pre-load everything—create "semantic highways" for the AI to find what it needs.

## Correctness Over Compression

**Counter to industry focus on token optimization:**

Context failures cost exponentially more than token expenses:
- A wrong answer wastes hours of human time
- A missed context costs rework cycles
- Token savings of 10% mean nothing if accuracy drops 5%

**Prioritize**:
1. Semantic relevance (right information)
2. Accuracy (correct information)
3. Clarity (unambiguous information)
4. Efficiency (minimal tokens) — *last priority*

## Semantic Highway Design

Structure project contexts to guide Claude toward useful information:

```markdown
# Project Context (CLAUDE.md)

## Key Documentation Files
- ARCHITECTURE.md - System design decisions
- PLAN.md - Current priorities and next actions
- INDEX.md - Automated document inventory

## Where to Find Things
- API specs: /docs/api/
- Test patterns: /tests/fixtures/
- Configuration: /config/
```

The goal: When Claude needs to understand the auth system, it should find `docs/auth.md` through your signposts, not by randomly exploring.

## Security Considerations

Context engineering creates new attack surfaces:

### Prompt Injection via MCP
- MCP channels can carry malicious content
- Tools that fetch external data are injection vectors
- Audit all content entering context

### Defensive Measures
1. **VPC Deployments**: Isolate MCP servers
2. **Role-Based Access**: Limit tool capabilities per context
3. **Audit Logging**: Track all context sources
4. **Content Validation**: Sanitize external data

### Cross-Tenant Risks
- In multi-tenant systems, context contamination is possible
- Session isolation is critical
- Clear context boundaries between users

## Implementation Pattern

### Phase 1: Context Consolidation
- Gather all relevant project knowledge
- Structure in discoverable hierarchy
- Create CLAUDE.md as entry point

### Phase 2: Dynamic Integration
- Add session hooks for runtime context
- Configure MCP servers for tool access
- Set up semantic signposts

### Phase 3: Autonomous Management
- Let AI discover what it needs
- Measure context quality, not token quantity
- Iterate based on failure modes

## Server-Side Compaction API

**Source**: [Anthropic Platform Documentation](https://platform.claude.com/docs/en/build-with-claude/compaction)

When context approaches limits, the Compaction API provides server-side automatic summarization. This is the production-grade version of the manual compaction described below.

### How It Works

```
[Full conversation: 180K tokens]
        ↓ Threshold trigger
[API call: POST /v1/messages with compaction strategy]
        ↓
[Compressed summary: ~20K tokens] + [Recent messages preserved]
        ↓
[Fresh working context continues]
```

### Strategies

| Strategy | Behavior | Best For |
|----------|----------|----------|
| `clear_tool_uses_20250919` | Clears oldest tool results chronologically | Tool-heavy agentic workflows |
| Default | Summarizes full conversation | General long-running sessions |

**Key Insight**: The `clear_tool_uses_20250919` strategy is specifically designed for agentic coding workflows where tool call/result pairs consume the bulk of context. It preserves the conversation flow while dropping verbose tool outputs.

### Claude Code Integration

Claude Code uses compaction automatically when context approaches limits. You can also trigger it:
- `/clear` — Starts fresh (no summary)
- `/rewind` > "Summarize from here" — Partial conversation summarization (v2.1.30+)

---

## Adaptive Thinking (Opus 4.6+)

**Source**: [Opus 4.6 Release](https://www.anthropic.com/claude/opus)

Opus 4.6 introduces an adaptive reasoning `effort` parameter that replaces the older `budget_tokens` approach for controlling thinking depth.

### Effort Levels

| Level | Behavior | Use Case |
|-------|----------|----------|
| `low` | Quick responses, minimal deliberation | Simple file lookups, straightforward edits |
| `medium` | Balanced reasoning | Standard development tasks |
| `high` | Deep reasoning and verification | Architecture decisions, security reviews |
| `max` | Maximum deliberation | Complex multi-file refactoring, critical debugging |

### Context Engineering Implication

Adaptive thinking interacts with context management: lower effort levels consume fewer thinking tokens, preserving more context for tool results and conversation history. For long-running sessions, using `low` effort for routine operations extends the useful life of the context window.

**Tip**: Claude Code's `/fast` toggle is the user-facing control for this — it uses the same Opus 4.6 model but with faster output optimized for simpler tasks.

---

## 1M Token Context Window (Beta)

Opus 4.6 extends the context window to 1M tokens (beta), previously only available on Sonnet models.

### Implications for Context Engineering

| Factor | 200K Context | 1M Context |
|--------|-------------|------------|
| Context rot risk | Moderate | Higher — more tokens = more n² attention degradation |
| Compaction urgency | High | Lower — more room before hitting limits |
| MCP budget headroom | Tight (~15 tools max) | More flexible (~50+ tools feasible) |
| Sub-agent necessity | Often required | May be avoidable for medium-complexity tasks |

**Warning**: Larger context does not eliminate context rot. The n² relationship between tokens and attention still applies. Use the additional capacity for breadth (more tools, more files), not as a substitute for good context hygiene.

### Long-Context Pricing

1M context is available in beta via `context-1m-2025-08-07` header. Long-context pricing applies for inputs exceeding standard limits.

---

## Context Rot

> "Context rot is the degradation of model accuracy as context windows fill up."

As more tokens are added, the transformer architecture struggles to track relationships between all tokens. The number of relationships grows as n² for n tokens—with a limited "attention budget," LLMs quickly get overwhelmed.

**Implications**:
- Longer context ≠ better context
- Recency bias affects recall
- Position in context matters (needle-in-haystack problem)
- Performance degrades before you hit the technical limit

### Three Mitigation Strategies (Anthropic Official)

#### 1. Compaction (Auto-Summarization)
The Claude Agent SDK's compact feature automatically summarizes previous messages when the context limit approaches.

```
[Full conversation history: 180K tokens]
        ↓ Compaction trigger
[Compressed summary: 20K tokens] + [Recent context: 30K tokens]
        ↓
[Fresh working context: 50K tokens]
```

**When to use**: Long-running tasks, multi-hour sessions, research workflows

#### 2. Structured Notes (External Memory)
Save persistent information outside the context window. Files like `claude-progress.md` and `STATE.md` serve as external memory that can be reloaded fresh.

```markdown
# claude-progress.md
## Completed
- [x] Implemented auth module (commit: abc123)
- [x] Fixed race condition in queue

## In Progress
- [ ] Migration script for v2 schema

## Blocked
- Waiting on API spec from team
```

**When to use**: Multi-session projects, handoffs between sessions

#### 3. Sub-Agent Architectures (Fresh Contexts)
Assign specialized agents to focused tasks. The main agent only receives condensed summaries, not full context.

```
Orchestrator (light context)
├── [Subagent 1: Fresh 200K] → Research task → Summary
├── [Subagent 2: Fresh 200K] → Code task → Diff
└── [Subagent 3: Fresh 200K] → Review task → Report
        ↓
Orchestrator receives only summaries (~2K total)
```

**When to use**: Complex multi-step tasks, parallel workstreams

### Measured Improvements

From Anthropic's internal testing:
- **Memory Tool + Context Editing**: 39% improvement in agent search performance
- **Context editing alone**: 29% improvement
- **Token consumption in 100-round search**: 84% reduction

### Progressive Disclosure Integration

Context rot makes progressive disclosure essential, not optional:

| Approach | Context Cost | Rot Risk |
|----------|--------------|----------|
| Load everything upfront | High | High—degrades quickly |
| Load on-demand | Low | Low—fresh context per operation |
| Subagent delegation | Minimal | Minimal—isolated contexts |

## Iterative Context Curation

Unlike static prompt engineering, context engineering is iterative:

```
[Initial Context] → [Model Response] → [New Information]
        ↑                                       |
        └──────── [Curated Context] ←──────────┘
```

Each inference cycle:
1. Generates new potentially-relevant data
2. Requires curation decisions (what to keep/discard)
3. Must prevent context from exceeding useful limits

**This is why specs matter**: External artifacts (specs/, ARCHITECTURE.md) provide stable reference points that don't rot, unlike accumulated conversation context.

## Quality Metrics

Track context effectiveness, not just efficiency:

| Metric | Traditional | Context Engineering |
|--------|-------------|---------------------|
| Focus | Token count | Task completion accuracy |
| Optimization | Compression | Relevance |
| Failure mode | Too expensive | Wrong answer |

## Application to Claude Code

For Claude Code projects, context engineering means:

1. **CLAUDE.md**: Your deterministic context entry point
2. **Hooks**: Dynamic context injection at session start
3. **Skills**: Structured behavior patterns
4. **MCP Servers**: Controlled probabilistic discovery

The goal isn't to tell Claude everything—it's to help Claude find the right things.

---

## Context Strategy Frameworks

Different orchestration patterns take different approaches to context management:

### GSD: Fresh Context Per Subagent

**Source**: [GSD Orchestration](./gsd-orchestration.md)

The GSD pattern gives each executor a **fresh 200K token context window** with zero accumulated garbage from previous tasks. This prevents "context rot"—quality degradation from filled context windows.

```
Orchestrator
├── [Executor 1: Fresh 200K] → Task 1
├── [Executor 2: Fresh 200K] → Task 2
└── [Executor 3: Fresh 200K] → Task 3

Each executor receives ONLY:
- Task specification (XML)
- Minimal necessary context from STATE.md
- No conversation history
```

**Key Principle**: The orchestrator never implements directly. It spawns agents, waits, and integrates results—preserving its own context for coordination.

**State Externalization**: All project state persists in files (STATE.md, .planning/), not in context. Any new agent can read STATE.md and understand the project without explanation.

### CAII: On-the-Fly Context Injection

**Source**: [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md)

CAII uses **7 fixed cognitive agents** that receive context on-the-fly, adapting to any domain without modification.

```
Domain Context Injection:
┌─────────────────────────────────────────┐
│        Cognitive Agent (fixed)          │
│   + Domain Context (injected at runtime)│
│   = Domain-Adapted Behavior             │
└─────────────────────────────────────────┘
```

**Philosophy**: Instead of creating domain-specific agents, inject domain knowledge into general-purpose cognitive agents. This maintains constant complexity regardless of project scope.

### Claude-Flow: Vector Memory + Swarm

**Source**: [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) (reference architecture - see [Framework Selection Guide](./framework-selection-guide.md#claude-flow-reference-only))

Enterprise-scale approach using vector memory for pattern retrieval:

- **HNSW Vector Memory**: 150x-12,500x faster pattern retrieval
- **ReasoningBank**: Trajectory storage with semantic matching
- **6 Swarm Topologies**: Hierarchical, Mesh, Ring, Star, Hybrid, Adaptive

**Scale**: 60+ specialized agents, 42 pre-built skills, 170+ MCP tools

### Marimo: Tool-Agnostic CLAUDE.md

**Source**: YouTube Short (January 2026)

Marimo notebooks demonstrate CLAUDE.md adoption spreading beyond Claude Code:

```
Project Root
├── CLAUDE.md ← Detected by Marimo
└── notebook.py

When Marimo interacts with AI:
1. Detects CLAUDE.md in project root
2. Automatically injects contents into AI context
3. Enables project-aware AI assistance within notebooks
```

**Significance**: The CLAUDE.md pattern is becoming tool-agnostic. Data science tools are adopting developer tooling patterns.

### RLM: Model-Managed Context (Emerging)

**Source**: [Recursive Language Models](./recursive-context-management.md)

RLM represents an **emerging paradigm** where the model manages its own context through a Python REPL environment:

```
RLM Context Management:
[Query + REPL Access to Context Variable]
              ↓
[Model decides: peek, grep, partition, summarize]
              ↓
[Spawns sub-LLM calls on chunks as needed]
              ↓
[Combines results iteratively]
```

**Key distinction from other frameworks**: RLM inverts control. Instead of external systems (orchestrators, vector DBs) managing what context the model sees, the model learns to manage its own context through reinforcement learning.

**Relationship to GSD**: RLM provides the theoretical foundation for why GSD's fresh context approach works—both avoid context rot through decomposition, but RLM automates the decomposition decision.

> **Status**: Emerging pattern. Monitor for Claude-specific validation before production adoption.

### Framework Comparison

| Framework | Context Strategy | Agent Model | State Management |
|-----------|-----------------|-------------|------------------|
| **GSD** | Fresh per subagent | ~5 workflow agents | STATE.md + .planning/ |
| **CAII** | On-the-fly injection | 7 cognitive agents | Task-specific memories |
| **Claude-Flow** | Vector retrieval | 60+ specialized | ReasoningBank |
| **RLM** | REPL variable + recursive | Model-managed | Sub-call outputs |
| **Marimo** | CLAUDE.md injection | Tool-integrated | Project files |
| **Standard Claude Code** | Accumulating | Single agent | Conversation history |

### When to Use Each

| Scenario | Recommended Framework |
|----------|----------------------|
| **Multi-phase projects with sessions** | GSD |
| **Scalable, maintainable architecture** | CAII |
| **Enterprise scale (60+ agents)** | Claude-Flow |
| **Data science workflows** | Marimo pattern |
| **Simple tasks** | Standard Claude Code |

---

## Context Extraction Tools

While context engineering focuses on architecture and principles, these tools help automate context preparation:

### repomix (formerly repopack)

**Repository**: https://github.com/yamadashy/repomix

Packs an entire repository into a single, AI-friendly file optimized for use as context.

```bash
# Install
npm install -g repomix

# Generate context file
repomix

# With options
repomix --output context.txt --ignore "node_modules,dist"
```

**Use Case**: Initial project onboarding, comprehensive codebase analysis, when you need the AI to understand the full project structure.

**Trade-off**: Generates large context files. Use judiciously—not every task needs full repo context.

### code2prompt

**Repository**: https://github.com/mufeedvh/code2prompt

Converts codebases into token-optimized prompts with intelligent filtering.

```bash
# Install
cargo install code2prompt

# Generate prompt
code2prompt --path /path/to/project
```

**Use Case**: Creating focused context for specific tasks, stripping unnecessary files/comments.

**Trade-off**: More aggressive optimization may lose context that matters.

### When to Use Context Tools

| Scenario | Tool | Rationale |
|----------|------|-----------|
| New project onboarding | repomix | Need full structure understanding |
| Focused code review | code2prompt | Targeted context, minimal tokens |
| Architecture discussion | repomix | Broad understanding required |
| Bug fixing | Neither | Use Claude's file reading directly |
| Routine development | Neither | CLAUDE.md + on-demand discovery |

**Key Insight**: These tools are for **initial context loading**, not ongoing development. Once Claude Code is in a session, its native file reading and exploration is more effective than pre-generated context files.

### Integration with Claude Code

```bash
# Generate context, then reference in prompt
repomix --output .context/repo-overview.txt

# In CLAUDE.md
## Project Overview
For full codebase context, see `.context/repo-overview.txt`
```

**Anti-pattern**: Don't regenerate context files constantly. They're for bootstrapping, not session maintenance.

---

## Related Patterns

- [GSD Orchestration](./gsd-orchestration.md) - Fresh context per subagent pattern
- [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) - On-the-fly context injection
- [Long-Running Agent Patterns](./long-running-agent.md) - External artifacts as memory
- [Advanced Tool Use](./advanced-tool-use.md) - Token-efficient tool integration
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient methodology loading
- [Memory Architecture](./memory-architecture.md) - Lifecycle-based information management
- [Agentic Retrieval](./agentic-retrieval.md) - Semantic highways for document exploration
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) - Cost-aware context architecture
- [Agent Evaluation](./agent-evaluation.md) - Evaluating context strategy effectiveness

---

## Anti-Patterns

### ❌ Optimizing Tokens Over Correctness
**Problem**: Compressing context aggressively to save tokens
**Symptom**: Wrong answers, missed context, wasted human time on rework
**Solution**: Prioritize semantic relevance and accuracy; efficiency is last priority

### ❌ Preloading Everything
**Problem**: Stuffing all possible context into system prompt upfront
**Symptom**: Context window exhaustion, needle-in-haystack retrieval failures
**Solution**: Create semantic highways; let AI discover what it needs on-demand

### ❌ Trusting External MCP Content
**Problem**: Accepting MCP-fetched content without validation
**Symptom**: Prompt injection vulnerabilities, corrupted reasoning
**Solution**: Audit all content entering context; sanitize external data

### ❌ Regenerating Context Files Constantly
**Problem**: Running repomix/code2prompt on every session
**Symptom**: Stale context files, wasted setup time, context drift
**Solution**: Generate context files for bootstrapping only; use native file reading during sessions

---

## Sources

- [Anthropic - Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) (Canonical - 2025)
- [Anthropic - Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (September 2025)
- [Anthropic - Compaction API](https://platform.claude.com/docs/en/build-with-claude/compaction) (2026)
- [Anthropic - Opus 4.6 Announcement](https://www.anthropic.com/claude/opus) (February 2026)
- [Nate B. Jones - Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive)

*Last updated: February 2026*
