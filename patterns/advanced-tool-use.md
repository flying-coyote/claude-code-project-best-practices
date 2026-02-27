---
version-requirements:
  claude-code: "v2.0.0+"
  beta-header: "advanced-tool-use-2025-11-20"
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "Tool Search: 85% token reduction (77K → 8.7K tokens)"
    source: "Anthropic Engineering Blog"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "Programmatic Tool Calling: 37% token reduction"
    source: "Anthropic Engineering Blog"
    date: "2025-11-24"
    revalidate: "2026-11-24"
  - claim: "Tool Examples: 72% → 90% accuracy improvement"
    source: "Anthropic internal testing"
    date: "2025-11-24"
    revalidate: "2026-11-24"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Advanced Tool Use Patterns

**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/advanced-tool-use) (November 24, 2025)
**Evidence Tier**: A (Primary vendor documentation)
**Beta Header**: `advanced-tool-use-2025-11-20`

> ⚠️ **Status Inconsistency**: Pattern marked as "PRODUCTION" but references beta header from Nov 2025 (3+ months old). Verify: Has this feature graduated from beta? Is beta header still required? Check [Anthropic Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) for graduation date or updated header.

## The Problem Space

Traditional tool calling has three fundamental bottlenecks:

### 1. Context Bloat from Tool Definitions

| Server | Tools | Tokens |
|--------|-------|--------|
| GitHub | 35 | ~26K |
| Slack | 11 | ~21K |
| Jira | - | ~17K |
| **Total** | 58+ | **~72K** |

### 2. Context Pollution from Intermediate Results

Example: Analyzing 10MB log file
- Traditional: Entire file enters context window
- Optimized: Only summary of error frequencies

### 3. Schema vs. Usage Gap

JSON Schema defines structural validity but cannot express:
- When to include optional parameters
- Which parameter combinations make sense
- API conventions and format expectations

## Three-Part Solution

### 1. Tool Search Tool

**Problem**: 50K+ tokens in tool definitions before conversation starts

**Solution**: Mark tools with `defer_loading: true` - Claude discovers on-demand via search

**Results**:
- Traditional: ~77K tokens before work begins
- With Tool Search: ~8.7K tokens **(85% reduction)**
- Accuracy: 79.5% → 88.1% (Opus 4.5)

**When to use**:
- Tool definitions >10K tokens
- 10+ tools available
- MCP systems with multiple servers

### 2. Programmatic Tool Calling

**Problem**: Each tool invocation requires full inference pass

**Solution**: Claude writes orchestration code that runs in sandboxed environment

```python
# Claude writes this code
team = await get_team_members("engineering")

# Parallel fetch all expenses
expenses = await asyncio.gather(*[
    get_expenses(m["id"], "Q3") for m in team
])

# Process in code, return only summary
exceeded = []
for member, exp in zip(team, expenses):
    total = sum(e["amount"] for e in exp)
    if total > budget_limit:
        exceeded.append({"name": member["name"], "spent": total})

print(json.dumps(exceeded))  # Only this enters Claude's context
```

**Results**: Token usage reduced by **37%**

**When to use**:
- Processing large datasets needing aggregates
- Multi-step workflows (3+ dependent calls)
- Filtering/transforming results before Claude sees them
- Parallel operations across many items

### 3. Tool Use Examples (input_examples)

**Problem**: JSON Schema can't express usage patterns

**Solution**: Provide concrete invocations

```json
{
  "name": "create_ticket",
  "input_examples": [
    {
      "title": "Login page returns 500 error",
      "priority": "critical",
      "labels": ["bug", "authentication", "production"]
    },
    {
      "title": "Add dark mode support",
      "labels": ["feature-request", "ui"]
    }
  ]
}
```

**What Claude learns from examples**:
- Format conventions (dates, IDs)
- Nested structure patterns
- Optional parameter correlations

**Results**: Accuracy improved from **72% → 90%**

## Application to Skills

Skills that would benefit from input examples:

### High Priority (complex invocation patterns)

1. **contradiction-detector**
   - Gap: "absolute statements" is ambiguous
   - Examples needed: Strong claim vs. hedged claim vs. established fact

2. **hypothesis-validator**
   - Gap: Passive reading vs. active formulation unclear
   - Examples needed: Research claim vs. hypothesis proposal

3. **publication-quality-checker**
   - Gap: Draft review vs. quality gate vs. casual feedback
   - Examples needed: Publication request vs. internal review

### Medium Priority

4. **cybersecurity-concept-analyzer** - "Analyze" vs. "quick summary"
5. **expert-communication-writer** - Composing vs. reviewing vs. discussing

## Implementation Recommendations

1. **For Skills**: Add explicit activation examples in SKILL.md
2. **For MCP Servers**: Consider `defer_loading` for specialized tools
3. **For Research Workflows**: Use programmatic calling for batch operations

---

## LSP Tool (December 2025)

Claude Code includes a Language Server Protocol (LSP) tool providing IDE-like code intelligence capabilities.

### Available Operations

| Operation | Purpose | Use Case |
|-----------|---------|----------|
| **Go-to-definition** | Navigate to where symbol is defined | Understanding function/class implementation |
| **Find references** | Locate all usages of a symbol | Impact analysis before refactoring |
| **Hover documentation** | Get type info and docs for symbol | Quick reference without leaving context |

### When LSP Excels

| Scenario | Why LSP Helps |
|----------|---------------|
| **Refactoring prep** | Find all usages before renaming |
| **Understanding unfamiliar code** | Jump to definitions, see type signatures |
| **API exploration** | Hover for documentation without searching |
| **Impact analysis** | Find references before modifying |

### LSP vs. Traditional Search

| Task | LSP | Grep/Glob |
|------|-----|-----------|
| Find function definition | ✅ Precise (language-aware) | ⚠️ May find false positives |
| Find all usages | ✅ Semantic (knows imports, aliases) | ⚠️ String matching only |
| Type information | ✅ Available | ❌ Not available |
| Cross-file navigation | ✅ Handles imports correctly | ⚠️ Requires manual tracing |

### Limitations

- **Language support varies**: TypeScript/JavaScript excellent, others may be limited
- **Project setup required**: LSP needs proper project configuration (tsconfig, etc.)
- **Not for text search**: Use Grep for pattern matching, LSP for semantic operations

### Best Practice: Combine Tools

```
1. Grep/Glob: Find candidate files by pattern
2. LSP: Navigate precisely within those files
3. Read: Examine full context when needed
```

## Evidence Quality

| Claim | Source | Tier |
|-------|--------|------|
| 85% token reduction (Tool Search) | Anthropic measurements | A |
| 37% token reduction (PTC) | Anthropic measurements | A |
| 72% → 90% accuracy (Examples) | Anthropic internal testing | A |

---

## Anti-Patterns

### ❌ Always Loading All Tools
**Problem**: Including all tool definitions in every context
**Symptom**: 50K+ tokens consumed before conversation starts, context exhaustion
**Solution**: Use `defer_loading: true` for specialized tools, enable tool search

### ❌ Ignoring Context Pollution
**Problem**: Letting full tool results enter context without summarization
**Symptom**: Large files (logs, data) consume entire context window
**Solution**: Use programmatic tool calling to filter/aggregate before results enter context

### ❌ Schema-Only Tool Definitions
**Problem**: Relying solely on JSON Schema without usage examples
**Symptom**: 72% accuracy when examples would yield 90%
**Solution**: Add `input_examples` showing correct parameter patterns

### ❌ Excessive Sequential Calls
**Problem**: Making tool calls one at a time when parallelization is possible
**Symptom**: Slow responses, unnecessary inference passes
**Solution**: Use programmatic calling for batch operations (asyncio.gather pattern)

---

## Related Patterns

- [Context Engineering](./context-engineering.md) - Correctness over compression philosophy
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient skill architecture

*Last updated: January 2026*
