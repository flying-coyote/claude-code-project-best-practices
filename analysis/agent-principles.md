---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "AI will never be 100% predictable"
    source: "Nate B. Jones - Agent Build Bible"
    date: "2025-09-01"
    revalidate: "2026-09-01"
status: PRODUCTION
last-verified: "2026-02-16"
notes: "Foundational principles - validated across 100+ production AI builds"
evidence-tier: B
applies-to-signals: [harness-custom-agents, audit-always-fetch]
revalidate-by: 2026-10-22
---

# AI Agent Principles for Production

**Source**: [Nate B. Jones - 2025 Agent Build Bible](https://natesnewsletter.substack.com/p/why-your-ai-breaks-in-production)
**Evidence Tier**: B (Validated secondary - expert practitioner with 100+ production builds)

## The Core Problem

AI violates principles so fundamental we don't realize we're assuming them. Success requires designing *around* these realities rather than treating them as bugs to fix.

---

## Principle 1: Persistent Memory Requirement

**Traditional Assumption**: Stateless services scale better
**AI Reality**: Stateless AI produces inconsistent, context-free responses

### Why It Matters
- Each session starts from zero without memory
- Users repeat context every conversation
- AI can't learn from prior interactions
- Cross-session workflows break

### Production Solution
- External artifacts as memory (CLAUDE.md, task files)
- Git commits as checkpoints
- Session hooks to restore context
- Structured knowledge bases

---

## Principle 2: Inherent Unpredictability

**Traditional Assumption**: Same input → same output
**AI Reality**: AI will never be 100% predictable

### Why It Matters
- Temperature introduces randomness by design
- Model updates change behavior silently
- Context variations produce different responses
- Edge cases multiply unpredictably

### Production Solution
- Design for "good enough" not "exact"
- Human-in-the-loop for critical decisions
- Graceful degradation paths
- Explicit confidence thresholds

---

## Principle 3: Monitoring Limitations

**Traditional Assumption**: Metrics tell you system health
**AI Reality**: Traditional monitoring will lie to you

### Why It Matters
- Latency doesn't indicate quality
- Success codes don't mean correct answers
- Error rates miss semantic failures
- Standard dashboards are blind to AI issues

### Production Solution
- Semantic evaluation (is the answer *right*?)
- Human review sampling
- Output quality metrics
- Hallucination detection

---

## Principle 4: Hybrid Architecture

**Traditional Assumption**: New tech replaces old tech
**AI Reality**: You're not replacing traditional systems with AI

### What Stays Traditional
- Authentication and authorization
- Billing and payments
- Audit logging
- Data persistence
- Security controls

### What Goes AI
- Customer interactions
- Content analysis
- Pattern recognition
- Natural language interfaces
- Decision support

### Production Solution
- Clear boundaries between layers
- Traditional systems handle trust
- AI systems handle intelligence
- Never AI-only for critical paths

---

## Principle 5: Persistent State Management

**Traditional Assumption**: Databases handle state
**AI Reality**: AI needs externalized, readable state

### The Problem
- In-context state evaporates
- Database state isn't AI-readable
- Session state doesn't persist
- Memory is limited by context window

### Production Solution
```
project/
├── .claude/
│   ├── CLAUDE.md          # Project context (persistent)
│   └── tasks/
│       └── current.json   # Task state (readable)
├── docs/
│   └── decisions/         # Decision log (auditable)
└── .git/                  # Recovery mechanism
```

Key pattern: File-based memory that survives sessions

---

## Principle 6: Semantic Validation

**Traditional Assumption**: Tests verify correctness
**AI Reality**: Traditional testing breaks with AI

### Why Traditional Tests Fail
- Exact match testing fails with creative output
- Unit tests can't evaluate "good" vs "bad" writing
- Integration tests miss semantic regressions
- Coverage metrics are meaningless

### Production Solution

| Traditional | AI-Native |
|-------------|-----------|
| Assert equals | Assert semantically similar |
| Mock responses | Evaluate response quality |
| Coverage % | Human review sample % |
| Pass/fail | Confidence score |

**Eval-Driven Development**:
1. Define evaluation criteria (rubrics)
2. Create golden examples
3. Score outputs against criteria
4. Track quality over time

---

## Implementation Checklist

For each AI integration, verify:

- [ ] **Memory**: How does state persist between sessions?
- [ ] **Unpredictability**: What happens when AI gives unexpected output?
- [ ] **Monitoring**: How do you know the answers are *right*?
- [ ] **Boundaries**: What stays traditional? What goes AI?
- [ ] **State**: Where does AI-readable state live?
- [ ] **Validation**: How do you test semantic correctness?

---

## When These Principles Break

These six principles are framed as axioms but are not universal. Known exceptions:

| Principle | Exception | Why |
|---|---|---|
| **1. Persistent Memory** | Stateless batch jobs (one-shot code generation, single-file transforms) | Cross-session memory adds no value when the session has no "after." Externalizing state is pure overhead. |
| **2. Inherent Unpredictability** | Deterministic-mode runs with temperature=0, seed pinned, tool whitelist fixed | Claude Code doesn't expose temperature=0 for end users, but the Claude Agent SDK does; production pipelines may approach near-determinism. |
| **3. Monitoring Limitations** | Non-semantic workflows (pure syntactic transforms, lint-only tasks) | Traditional metrics (pass/fail, exit codes) remain informative for non-semantic output. Semantic evaluation matters where the output *has* semantic content. |
| **4. Hybrid Architecture** | Pure-content workflows where there is no trust boundary (private note-taking, personal research) | Not every use case has a "trust infrastructure" to keep traditional. Principle 4 is load-bearing for multi-tenant and regulated contexts. |
| **5. Persistent State** | Ephemeral experiments, throwaway prototypes | File-based memory is overhead for sessions that end in a discard. |
| **6. Semantic Validation** | Code with comprehensive traditional test suites (unit + integration + property-based) | When `pytest` passes and covers intent, semantic validation is redundant. The principle matters most where traditional testing is structurally inadequate (creative writing, open-ended research, UI/UX). |

The principles are **load-bearing for agentic systems in production**. Most exceptions live at the edges: pure-batch, pure-deterministic, pure-syntactic, or pure-personal. When the principle's context obtains, follow it; when it doesn't, don't retrofit infrastructure you won't use.

**Source for exception analysis** (Tier A — this repo's 7-repo portfolio): repos that operate mostly in the principle-holds regime (mndr-review-automation, health-inventory) versus repos at the edge (research prototypes, one-shot analysis scripts). See [agent-driven-development.md](agent-driven-development.md).

---

## Application to Claude Code

These principles manifest in Claude Code patterns:

| Principle | Claude Code Implementation |
|-----------|---------------------------|
| Memory | CLAUDE.md, task files, git history |
| Unpredictability | Human approval for significant changes |
| Monitoring | Session summaries, diff reviews |
| Hybrid | Traditional: git, files / AI: code generation |
| State | External artifacts pattern |
| Validation | User review before commit |

---

## Anti-Patterns

### ❌ Expecting Deterministic Output
**Problem**: Assuming AI will always produce identical output for same input
**Symptom**: Flaky tests, inconsistent behavior across sessions
**Solution**: Design for "good enough" responses, use semantic similarity not exact match

### ❌ Trusting Traditional Metrics
**Problem**: Relying on latency/uptime to indicate AI system health
**Symptom**: Fast, successful responses that are semantically wrong
**Solution**: Implement semantic evaluation, human review sampling, output quality metrics

### ❌ AI-Only Critical Paths
**Problem**: Routing authentication, payments, or security through AI without fallback
**Symptom**: Security vulnerabilities, unpredictable failures in critical flows
**Solution**: Keep trust infrastructure traditional; use AI for intelligence, not gatekeeping

### ❌ Stateless AI Design
**Problem**: Treating AI like stateless microservices
**Symptom**: Users repeat context every session, cross-session workflows break
**Solution**: External artifacts (CLAUDE.md, task files, git) as persistent memory

### ❌ Implicit Subagent Dispatch (Opus 4.7 regression)
**Problem**: Instructions like "execute the tasks in parallel" or "dispatch the work" relied on pre-4.7 models spawning subagents on their own initiative. The [Anthropic Opus 4.7 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) confirms 4.7 spawns "fewer subagents by default" and is "steerable through prompting" — dispatch must now be explicit.
**Symptom**: Workflows that achieved parallelism on 4.6 collapse to sequential in-context work on 4.7; throughput and cost both regress silently.
**Solution**: Name the subagent mechanism in the prompt. For parallel work: "Use three Explore subagents in parallel, one per directory." For in-context work: "Handle all three tasks in this session without spawning subagents." See [Model Migration Anti-Patterns](model-migration-anti-patterns.md).

---

## Related Patterns
- [Long-Running Agent](../archive/patterns-v1/long-running-agent.md) - External artifacts as memory
- [Context Engineering](./behavioral-insights.md) - Deterministic vs probabilistic context
- [Session Learning](./behavioral-insights.md) - Implements Principle 1 (Persistent Memory)
- [Subagent Orchestration](./orchestration-comparison.md) - Applies principles in subagent design
- [Agent-Driven Development](./agent-driven-development.md) - Production validation of these 6 principles across 7 agent-driven repos
- [Model Migration Anti-Patterns](./model-migration-anti-patterns.md) - Opus 4.7 changes to subagent defaults and prompt literalism

*Last updated: April 2026*
