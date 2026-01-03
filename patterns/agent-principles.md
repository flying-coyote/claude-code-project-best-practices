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

---

## Related Patterns
- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
- [Context Engineering](./context-engineering.md) - Deterministic vs probabilistic context

*Last updated: January 2026*
