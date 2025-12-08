# Advanced Tool Use Patterns

**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/advanced-tool-use) (November 24, 2025)
**Beta Header**: `advanced-tool-use-2025-11-20`

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

## Evidence Quality

| Claim | Source | Tier |
|-------|--------|------|
| 85% token reduction (Tool Search) | Anthropic measurements | A |
| 37% token reduction (PTC) | Anthropic measurements | A |
| 72% → 90% accuracy (Examples) | Anthropic internal testing | A |

---

## Related Patterns

- [Context Engineering](./context-engineering.md) - Correctness over compression philosophy
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient skill architecture
