# Context Engineering

**Source**: [Nate B. Jones - Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive)
**Evidence Tier**: B (Validated secondary - expert practitioner)

## The Core Insight

Traditional prompt engineering focuses on what you *tell* the AI. Context engineering focuses on what the AI *discovers*.

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
