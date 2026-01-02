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

## Context Rot

From Anthropic's research:

> "As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases."

**Implications**:
- Longer context ≠ better context
- Recency bias affects recall
- Position in context matters (needle-in-haystack problem)

**Mitigations**:
1. **Progressive disclosure**: Load information on-demand, not up-front
2. **Document sharding**: Break large specs into focused chunks
3. **Context summarization**: Compress historical context before it rots
4. **Strategic placement**: Put critical info at context boundaries

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

## Related Patterns

- [Long-Running Agent Patterns](./long-running-agent.md) - External artifacts as memory
- [Advanced Tool Use](./advanced-tool-use.md) - Token-efficient tool integration
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient methodology loading
- [Memory Architecture](./memory-architecture.md) - Lifecycle-based information management

---

## Sources

- [Anthropic - Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (September 2025)
- [Nate B. Jones - Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive)

*Last updated: January 2026*
