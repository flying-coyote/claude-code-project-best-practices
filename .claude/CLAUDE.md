# Claude Code Project Best Practices - Meta-Project

## Project Purpose

Develop, document, and validate patterns for Claude Code projects. This repository serves as:
- **Reference implementation** of patterns described within
- **Teaching resource** for Claude Code users
- **Validation testbed** for pattern effectiveness

## Current Phase

**Status**: Post-v1.0 (Maintenance + Pattern Expansion)
**Focus**: Adding mature patterns from production validation

## Quality Standards

All content must:
- Be backed by authoritative sources (see SOURCES.md)
- Include evidence tier classification where claims are made
- Be validated in production before documenting
- Follow patterns it teaches (this repo practices what it preaches)

## Key Files

| File | Purpose |
|------|---------|
| README.md | Project overview and getting started |
| SOURCES.md | All sources with evidence tiers |
| DECISIONS.md | Design rationale and trade-offs |
| patterns/ | Core implementation patterns |
| skills/ | Skill documentation and examples |
| templates/ | Ready-to-use configuration templates |
| examples/ | Complete project examples |
| presets/ | Quick-start configurations by project type |

## Patterns Directory

- `long-running-agent.md` - External artifacts, verify before work
- `context-engineering.md` - Deterministic vs probabilistic context
- `agent-principles.md` - 6 production AI principles
- `mcp-failure-modes.md` - 7 failure modes + 3 production patterns
- `advanced-tool-use.md` - Tool search and programmatic calling
- `evidence-tiers.md` - Citation quality classification

## Skills Directory

- `README.md` - Comprehensive skills guide
- `SKILL-TEMPLATE.md` - Template for creating skills
- `examples/` - 8 production-validated example skills

## Development Guidelines

When adding new patterns:
1. Identify authoritative source (Tier A or B required)
2. Document in patterns/ with source attribution
3. Create example in examples/ if applicable
4. Update SOURCES.md with new reference
5. Test in at least one production project

## Git Workflow

Commit message prefixes:
- `📚` - Documentation and patterns
- `🔧` - Configuration and infrastructure
- `✅` - Validation and testing
- `📊` - Research and analysis
