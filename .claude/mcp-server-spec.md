# Claude Code Best Practices MCP Server Specification

**Version**: 1.0.0
**Date**: January 20, 2026
**Status**: DEFERRED - Specification only, implementation not prioritized
**Related**: H-MCP-CONTEXT-01 (validated >80% context reduction)
**Location**: Second Brain Project (project1)

> **Decision (2026-01-27)**: This specification is deferred indefinitely. Rationale:
> 1. 593-line spec without implementation = documentation clutter
> 2. Skills approach (per mcp-vs-skills-economics.md) is 50% cheaper for this use case
> 3. Manual pattern extraction + existing skills workflow is sufficient
> 4. Implementation effort (4-6 weeks) exceeds benefit for a documentation project
>
> This spec is retained for reference if MCP implementation becomes valuable later.
> See DOGFOODING-GAPS.md for full rationale.

---

## Executive Summary

MCP server specification for maintaining Claude Code best practices documentation across the Second Brain ecosystem. This server monitors thought leader sources, tracks Claude Code updates, extracts patterns, and ensures documentation stays current with the rapidly evolving AI-assisted development landscape.

**Core Problem**: Best practices documents become stale without regular refresh. Manual extraction of patterns from thought leaders (GitHub, blogs, social media) is time-consuming and inconsistent. No automated validation that documented patterns still work with current Claude Code behavior.

**Solution**: 4 workflow-based MCP tools that systematically monitor sources, extract patterns, validate recommendations, and synthesize learnings into actionable documentation updates.

---

## Token Reduction Targets

| Scenario | Without MCP | With MCP | Reduction |
|----------|-------------|----------|-----------|
| Source monitoring | ~20K tokens (manual browsing) | ~3K tokens | 85% |
| Pattern extraction | ~15K tokens (full doc reads) | ~2K tokens | 87% |
| Validation testing | ~25K tokens (manual testing) | ~3K tokens | 88% |
| Weekly synthesis | ~30K tokens (aggregation) | ~4K tokens | 87% |

---

## Architecture Design

### Design Principles (H-MCP-CONTEXT-01 Compliant)

1. **Workflow-based tools** - 4 high-level operations for end-to-end management
2. **Tool Output Schemas** - Structured extraction and classification
3. **Evidence tier assignment** - All patterns classified A/B/C/D per hypothesis system
4. **Change detection** - Track what's new vs. what's changed vs. what's deprecated
5. **Cross-project awareness** - Patterns applicable across 9-project ecosystem

### Tool Architecture

```
┌────────────────────────────────────────────────────────────┐
│           Claude Code Best Practices MCP Server            │
├────────────────────────────────────────────────────────────┤
│ Workflow Tools (4)                                          │
│ ├── extraction_workflow     # Extract patterns from sources │
│ ├── changelog_workflow      # Track Claude Code updates     │
│ ├── validation_workflow     # Test documented patterns      │
│ └── synthesis_workflow      # Aggregate and synthesize      │
├────────────────────────────────────────────────────────────┤
│ Resources                                                   │
│ ├── source://registry       # Thought leader sources        │
│ ├── pattern://catalog       # Extracted patterns database   │
│ ├── changelog://history     # Claude Code release tracking  │
│ └── validation://results    # Pattern test results          │
├────────────────────────────────────────────────────────────┤
│ Sub-tools (loaded on-demand)                                │
│ ├── github_monitor          # Track GitHub repos/releases   │
│ ├── blog_fetcher            # Extract from blog posts       │
│ ├── social_scanner          # Monitor X/LinkedIn/Mastodon   │
│ ├── pattern_classifier      # Classify by category/tier     │
│ └── doc_updater             # Generate documentation diffs  │
└────────────────────────────────────────────────────────────┘
```

---

## Tool Specifications

### Tool 1: extraction_workflow

**Purpose**: Monitor thought leader sources and extract Claude Code patterns

**Input Schema**:
```json
{
  "action": {
    "type": "string",
    "enum": ["scan", "extract", "classify", "add_source", "list_sources"]
  },
  "params": {
    "source_type": {
      "type": "string",
      "enum": ["github", "blog", "social", "documentation", "all"]
    },
    "source_id": "string | null",
    "time_range": {
      "type": "string",
      "enum": ["24h", "7d", "30d", "all"]
    },
    "categories": {
      "type": "array",
      "items": {"enum": ["prompting", "mcp", "tools", "agents", "context", "memory", "performance"]}
    }
  }
}
```

**Output Schema**:
```json
{
  "action": "string",
  "extraction_result": {
    "sources_scanned": "integer",
    "new_content_found": "integer",
    "patterns_extracted": [
      {
        "id": "string (UUID)",
        "title": "string",
        "source": {
          "type": "enum(github, blog, social, docs)",
          "url": "string",
          "author": "string",
          "date": "timestamp"
        },
        "category": "enum(prompting, mcp, tools, agents, context, memory, performance)",
        "evidence_tier": "enum(A, B, C, D)",
        "summary": "string",
        "key_insight": "string",
        "code_example": "string | null",
        "applicability": {
          "projects": ["string"],
          "contexts": ["string"]
        },
        "related_patterns": ["string (pattern IDs)"],
        "status": "enum(new, updated, confirmed, deprecated)"
      }
    ],
    "contradictions_detected": [
      {
        "pattern_1": "string (pattern ID)",
        "pattern_2": "string (pattern ID)",
        "conflict_type": "string",
        "resolution_needed": "boolean"
      }
    ]
  }
}
```

**Evidence Tier Classification**:

| Tier | Criteria | Example Sources |
|------|----------|-----------------|
| A | Production validation, published results | Anthropic engineering blog, major company case studies |
| B | Expert practitioner, repeated success | Simon Willison, Daniel Miessler, established GitHub repos |
| C | Community consensus, multiple confirmations | Popular threads, widely-adopted patterns |
| D | Single source, unvalidated | Individual blog posts, tweets without corroboration |

**Priority Thought Leaders**:

| Source | Type | Focus Area |
|--------|------|------------|
| Anthropic Engineering Blog | Blog | Official patterns, MCP updates |
| Simon Willison | Blog/GitHub | LLM tooling, practical patterns |
| Daniel Miessler | Blog/GitHub | AI workflows, Fabric patterns |
| Harper Reed | Social/GitHub | Developer experience |
| Speakeasy Engineering | Blog | MCP optimization, token reduction |
| Joe Njenga (Medium) | Blog | Claude Code specific |
| Matt Shumer | Social | Prompting techniques |

**Example Usage**:
```
User: "What new Claude Code patterns emerged this week?"
MCP: extraction_workflow(action="scan", params={
  source_type="all",
  time_range="7d",
  categories=["mcp", "tools", "context"]
})
→ Returns: 8 new patterns extracted, 2 contradictions detected, 3 require validation
```

---

### Tool 2: changelog_workflow

**Purpose**: Track Claude Code updates and identify documentation impacts

**Input Schema**:
```json
{
  "action": {
    "type": "string",
    "enum": ["check_updates", "analyze_impact", "flag_outdated", "get_history"]
  },
  "params": {
    "version_range": {
      "from": "string | null",
      "to": "string | null"
    },
    "component": {
      "type": "string",
      "enum": ["core", "mcp", "tools", "memory", "all"]
    },
    "include_breaking": "boolean"
  }
}
```

**Output Schema**:
```json
{
  "action": "string",
  "changelog_result": {
    "current_version": "string",
    "updates_found": [
      {
        "version": "string",
        "release_date": "timestamp",
        "type": "enum(major, minor, patch)",
        "changes": [
          {
            "category": "string",
            "description": "string",
            "breaking": "boolean",
            "migration_notes": "string | null"
          }
        ]
      }
    ],
    "documentation_impacts": [
      {
        "document": "string (path)",
        "section": "string",
        "impact_type": "enum(outdated, deprecated, needs_update, breaking_change)",
        "affected_pattern": "string",
        "suggested_action": "string"
      }
    ],
    "outdated_recommendations": [
      {
        "pattern_id": "string",
        "current_recommendation": "string",
        "issue": "string",
        "suggested_replacement": "string | null"
      }
    ]
  }
}
```

**Monitored Components**:

| Component | Update Source | Check Frequency |
|-----------|---------------|-----------------|
| Claude Code CLI | GitHub releases | Daily |
| MCP Protocol | Anthropic MCP repo | Weekly |
| SDK Updates | npm/pip registries | Weekly |
| API Changes | Anthropic API changelog | Weekly |

**Example Usage**:
```
User: "Are there any Claude Code updates affecting MCP documentation?"
MCP: changelog_workflow(action="check_updates", params={
  component="mcp",
  include_breaking=true
})
→ Returns: MCP tool search feature added (June 2025), 3 docs need update, 1 pattern deprecated
```

---

### Tool 3: validation_workflow

**Purpose**: Test documented patterns against current Claude Code behavior

**Input Schema**:
```json
{
  "action": {
    "type": "string",
    "enum": ["validate_pattern", "batch_validate", "measure_tokens", "test_example"]
  },
  "params": {
    "pattern_ids": {
      "type": "array",
      "items": "string"
    },
    "validation_type": {
      "type": "string",
      "enum": ["syntax", "functionality", "token_reduction", "full"]
    },
    "test_context": {
      "project": "string | null",
      "scenario": "string | null"
    }
  }
}
```

**Output Schema**:
```json
{
  "action": "string",
  "validation_result": {
    "patterns_tested": "integer",
    "results": [
      {
        "pattern_id": "string",
        "status": "enum(valid, degraded, broken, improved)",
        "tests_run": [
          {
            "test_type": "string",
            "passed": "boolean",
            "details": "string"
          }
        ],
        "token_metrics": {
          "documented_reduction": "float (percentage)",
          "measured_reduction": "float (percentage)",
          "variance": "float",
          "still_effective": "boolean"
        },
        "behavior_changes": [
          {
            "aspect": "string",
            "expected": "string",
            "actual": "string",
            "severity": "enum(breaking, significant, minor)"
          }
        ],
        "recommendation": "enum(keep, update, deprecate, investigate)"
      }
    ],
    "summary": {
      "valid": "integer",
      "needs_update": "integer",
      "broken": "integer",
      "improved": "integer"
    }
  }
}
```

**Validation Types**:

| Type | Checks | Automation Level |
|------|--------|-----------------|
| Syntax | Pattern syntax still valid | Fully automated |
| Functionality | Pattern produces expected result | Semi-automated |
| Token Reduction | Claimed reduction still achieved | Automated measurement |
| Full | All checks combined | Mixed automation |

**Example Usage**:
```
User: "Validate our MCP context reduction patterns still achieve >80% reduction"
MCP: validation_workflow(action="batch_validate", params={
  pattern_ids=["mcp-lazy-load", "mcp-tool-search", "mcp-output-schemas"],
  validation_type="token_reduction"
})
→ Returns: 2/3 valid (>80%), 1 degraded (now 72%), update recommended
```

---

### Tool 4: synthesis_workflow

**Purpose**: Aggregate learnings and generate documentation updates

**Input Schema**:
```json
{
  "action": {
    "type": "string",
    "enum": ["generate_summary", "update_document", "detect_contradictions", "create_recommendation"]
  },
  "params": {
    "time_range": {
      "type": "string",
      "enum": ["weekly", "monthly", "quarterly"]
    },
    "target_document": "string | null",
    "include_categories": {
      "type": "array",
      "items": "string"
    },
    "synthesis_type": {
      "type": "string",
      "enum": ["diff", "full_rewrite", "append_only"]
    }
  }
}
```

**Output Schema**:
```json
{
  "action": "string",
  "synthesis_result": {
    "period": "string",
    "patterns_analyzed": "integer",
    "summary": {
      "new_patterns": "integer",
      "updated_patterns": "integer",
      "deprecated_patterns": "integer",
      "contradictions_resolved": "integer"
    },
    "key_insights": [
      {
        "insight": "string",
        "evidence_tier": "enum(A, B, C, D)",
        "supporting_patterns": ["string (pattern IDs)"],
        "actionable": "boolean"
      }
    ],
    "documentation_updates": [
      {
        "document": "string (path)",
        "update_type": "enum(add, modify, remove)",
        "section": "string",
        "current_content": "string",
        "proposed_content": "string",
        "rationale": "string",
        "confidence": "float"
      }
    ],
    "contradictions": [
      {
        "topic": "string",
        "position_1": {"source": "string", "claim": "string"},
        "position_2": {"source": "string", "claim": "string"},
        "resolution": "string | null",
        "add_to_contradictions_doc": "boolean"
      }
    ],
    "recommendations": [
      {
        "priority": "enum(high, medium, low)",
        "recommendation": "string",
        "effort": "enum(low, medium, high)",
        "impact": "string"
      }
    ]
  }
}
```

**Synthesis Outputs**:

| Output | Frequency | Target Document |
|--------|-----------|-----------------|
| Weekly Summary | Weekly | claude-progress.md |
| Pattern Updates | On extraction | mcp-2025-best-practices-implementation-patterns.md |
| Contradiction Detection | Continuous | documented-contradictions.md |
| Quarterly Review | Quarterly | ARCHITECTURE.md |

**Example Usage**:
```
User: "Generate weekly Claude Code best practices summary"
MCP: synthesis_workflow(action="generate_summary", params={
  time_range="weekly",
  include_categories=["mcp", "context", "tools"]
})
→ Returns: 5 new patterns (3 Tier A), 2 contradictions detected, 8 doc updates proposed
```

---

## Resources

### Resource 1: source://registry

**Purpose**: Tracked thought leader sources for pattern extraction

**Schema**:
```json
{
  "sources": [
    {
      "id": "anthropic-engineering",
      "name": "Anthropic Engineering Blog",
      "type": "blog",
      "url": "https://www.anthropic.com/engineering",
      "rss_feed": "https://www.anthropic.com/rss.xml",
      "priority": 1,
      "categories": ["mcp", "tools", "performance"],
      "last_checked": "timestamp",
      "reliability_score": 1.0
    }
  ]
}
```

### Resource 2: pattern://catalog

**Purpose**: Database of extracted patterns with full metadata

**Schema**:
```json
{
  "patterns": [
    {
      "id": "mcp-tool-search-001",
      "title": "Dynamic Tool Search for Context Reduction",
      "category": "mcp",
      "evidence_tier": "A",
      "source_url": "https://...",
      "extracted_date": "2026-01-15",
      "last_validated": "2026-01-20",
      "validation_status": "valid",
      "token_reduction_claim": 0.469,
      "token_reduction_measured": 0.465,
      "applicable_projects": ["security-architect-mcp", "genealogy"],
      "related_hypothesis": "H-MCP-CONTEXT-01"
    }
  ]
}
```

### Resource 3: changelog://history

**Purpose**: Claude Code version history and change tracking

### Resource 4: validation://results

**Purpose**: Pattern validation test results over time

---

## Implementation Phases

### Phase 1: Source Monitoring (Week 1)
- [ ] Create MCP server skeleton
- [ ] Implement extraction_workflow with RSS/API fetching
- [ ] Add GitHub release monitoring
- [ ] Configure priority source list

### Phase 2: Pattern Classification (Week 2)
- [ ] Implement pattern classifier
- [ ] Add evidence tier assignment logic
- [ ] Create contradiction detection
- [ ] Build pattern catalog schema

### Phase 3: Validation Engine (Week 3)
- [ ] Implement validation_workflow
- [ ] Add token measurement tooling
- [ ] Create test harness for patterns
- [ ] Build validation result tracking

### Phase 4: Synthesis & Updates (Week 4)
- [ ] Implement synthesis_workflow
- [ ] Add document diff generation
- [ ] Create automated update proposals
- [ ] Build weekly summary generator

---

## Integration Points

### With Second Brain (project1)

| Document | Integration |
|----------|-------------|
| `mcp-2025-best-practices-implementation-patterns.md` | Primary update target |
| `documented-contradictions.md` | Contradiction additions |
| `hypotheses/` | Pattern → hypothesis linkage |
| `claude-progress.md` | Weekly summary integration |

### With Project Ecosystem

All 9 projects benefit from updated best practices:
- Security Architect MCP Server: MCP patterns
- Genealogy: Workflow patterns
- Book: Documentation patterns
- Blog: Content generation patterns

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Source coverage | 15+ thought leaders | Sources tracked |
| Pattern extraction rate | 5-10/week | New patterns extracted |
| Validation currency | <7 days | Time since last validation |
| Documentation freshness | <14 days | Time since doc updates |

---

## References

- [H-MCP-CONTEXT-01](../01-knowledge-base/hypotheses/extended-hypotheses.md) - Context reduction validation
- [MCP Best Practices Doc](../01-knowledge-base/concepts/mcp-2025-best-practices-implementation-patterns.md) - Primary update target
- [Documented Contradictions](../01-knowledge-base/concepts/documented-contradictions.md) - Contradiction tracking

---

## Tags

`#mcp` `#best-practices` `#thought-leaders` `#documentation` `#automation` `#context-efficiency`
