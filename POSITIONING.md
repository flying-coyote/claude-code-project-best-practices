# Project Positioning: Claude Code Best Practices

This document defines how this repository positions itself relative to the broader ecosystem of AI coding tools, spec-driven development frameworks, and community resources.

---

## Core Identity

### What This Repository Is

**Claude Code-Native Patterns Repository**

This repository documents patterns that work **within Claude Code's native capabilities**:
- CLAUDE.md project context files
- Skills (methodology patterns)
- Hooks (event-driven automation)
- Slash commands (explicit user actions)
- Subagents (context isolation)
- MCP servers (external connectivity)

### What This Repository Is Not

1. **Not a spec-driven development framework** (like BMAD, Spec Kit, Kiro)
2. **Not a plugin/template marketplace** (like claude-code-templates)
3. **Not a curated list** (like awesome-claude-code)
4. **Not IDE-specific** (unlike Cursor rules, Windsurf rules)

---

## Positioning Relative to SDD Frameworks

### Complementary Relationship

```
┌─────────────────────────────────────────────────────────┐
│     SDD Frameworks (BMAD, Spec Kit, Agent OS, Kiro)    │
│                  Planning & Specification               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │     THIS REPOSITORY                             │   │
│   │     Claude Code-Native Execution Patterns       │   │
│   │                                                 │   │
│   │  • Skills       • Hooks       • MCP            │   │
│   │  • Context      • Memory      • Subagents      │   │
│   └─────────────────────────────────────────────────┘   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    Claude Code                          │
│                   Execution Engine                      │
└─────────────────────────────────────────────────────────┘
```

### Division of Concerns

| Concern | SDD Frameworks | This Repository |
|---------|---------------|-----------------|
| **Planning** | Structured specification phases | Lightweight, context-aware |
| **Methodology** | Multi-agent role simulation | Single-agent skill patterns |
| **Token Strategy** | Full spec upfront | Progressive disclosure |
| **Scope** | Full project lifecycle | Session/feature execution |
| **Team Size** | Enterprise/team focus | Individual + small team |

---

## Unique Value Proposition

### 1. Claude Code-Native Focus

Unlike cross-platform resources (ai-prompts, rules_template), this repository focuses exclusively on Claude Code's native extension mechanisms, documented with:
- Tier A/B evidence sources
- Production validation metrics
- Anthropic-aligned patterns

### 2. Pattern Depth Over Breadth

Unlike curated lists (awesome-claude-code), this repository provides:
- Complete pattern documentation with rationale
- Implementation examples with measured outcomes
- Trade-off analysis and failure mode coverage

### 3. Evidence-Based Documentation

Every pattern includes:
- Source attribution with evidence tier
- Production validation status
- Known limitations and anti-patterns

---

## Relationship to Other Resources

### Primary References (Monitor Weekly)

| Source | Relationship | Action |
|--------|-------------|--------|
| **Anthropic Engineering Blog** | Authority | Incorporate new patterns immediately |
| **Claude Code Documentation** | Authority | Align with official capabilities |
| **agentskills.io** | Specification | Follow open standard |

### Secondary References (Monitor Monthly)

| Source | Relationship | Action |
|--------|-------------|--------|
| **hesreallyhim/awesome-claude-code** | Discovery | Check for emerging patterns |
| **GitHub Spec Kit** | Adjacent | Document integration points |
| **BMAD Method** | Adjacent | Document integration points |
| **Simon Willison's Analysis** | Expert | Incorporate insights |

### Tertiary References (Monitor Quarterly)

| Source | Relationship | Action |
|--------|-------------|--------|
| **Cursor/Windsurf rules** | Cross-platform | Note transferable patterns |
| **Microsoft AutoGen** | Architecture | Reference for multi-agent patterns |
| **Community best practices repos** | Validation | Cross-check patterns |

---

## Content Strategy

### What We Document

1. **Patterns that work within Claude Code's native capabilities**
   - Even if SDD frameworks do something similar, if Claude Code skills/hooks can do it natively, document it

2. **Integration points with external frameworks**
   - How to use BMAD with Claude Code
   - How to integrate Spec Kit workflow

3. **Evidence-based best practices**
   - Measured outcomes from production use
   - Token efficiency metrics
   - Quality improvements

### What We Don't Document

1. **Framework-specific configurations**
   - BMAD agent definitions (link to their repo)
   - Kiro IDE setup (link to their docs)

2. **Cross-platform rules**
   - Cursor rules syntax (link to instructa/ai-prompts)
   - Windsurf workflows (link to their docs)

3. **Pre-built templates/components**
   - Use claude-code-templates for that
   - We document patterns, not ready-to-use configs

---

## Recommendations for Staying Current

### Weekly Tasks

1. Check Anthropic Engineering Blog for new Claude Code posts
2. Review GitHub releases for Claude Code SDK
3. Monitor Claude Code Discord/community for emerging patterns

### Monthly Tasks

1. Review awesome-claude-code for new high-star repositories
2. Check SDD framework changelogs (Spec Kit, BMAD)
3. Update SOURCES.md with new discoveries
4. Validate existing patterns still align with current Claude Code behavior

### Quarterly Tasks

1. Full review of community best practices repositories
2. Assess if any patterns need deprecation
3. Evaluate emerging frameworks for documentation
4. Update evidence tiers based on new validation

---

## Differentiation Summary

| Dimension | This Repository | Curated Lists | SDD Frameworks | Template Repos |
|-----------|-----------------|---------------|----------------|----------------|
| **Depth** | Deep patterns | Links/summaries | Methodology | Ready-to-use |
| **Focus** | Claude Code native | Discovery | Lifecycle | Implementation |
| **Evidence** | Tier A/B required | Varies | Varies | None required |
| **Maintenance** | Production-validated | Community-driven | Author-driven | Template-driven |

---

## Future Considerations

### Potential Additions

1. **Skill marketplace integration** - As agentskills.io matures
2. **Multi-agent patterns** - If Claude Code adds native support
3. **Visual spec patterns** - If demand for UI/UX specs grows

### Potential Deprecations

1. **Patterns superseded by Claude Code features**
2. **Patterns with no production validation after 6 months**
3. **Patterns where better alternatives emerge**

---

*Last updated: January 2026*
