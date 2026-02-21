# Tools & Patterns Tracker
**Last Updated**: 2026-02-21
**Auto-generated**: By `scripts/generate-tools-tracker.py`
**Purpose**: Single source of truth for all Claude Code tool/pattern recommendations

---

## Status Definitions

| Status | Meaning |
|--------|----------|
| ✅ RECOMMENDED | Production-ready with Tier A/B evidence |
| ⚠️ CONSIDER | Conditional use cases, trade-offs apply |
| 🔬 EMERGING | Promising pattern, needs validation |
| ❌ DEPRECATED | Superseded or obsolete |

---

## Component Coverage

| Component | Pattern Files | Count |
|-----------|---------------|-------|
| CLAUDE.md | tool-ecosystem, progressive-disclosure, documentation-maintenance, ... (17 more) | 20 |
| prompts | progressive-disclosure, framework-selection-guide, context-engineering, ... (10 more) | 13 |
| skills | progressive-disclosure, mcp-vs-skills-economics, plugins-and-extensions, ... (2 more) | 5 |
| tools | tool-ecosystem, framework-selection-guide, skills-domain-knowledge, ... (2 more) | 5 |
| mcp | mcp-vs-skills-economics, mcp-patterns | 2 |
| sub-agents | context-engineering, plugins-and-extensions, subagent-orchestration | 3 |
| slash-commands | progressive-disclosure, documentation-maintenance, architecture-decision-records, ... (7 more) | 10 |
| marketplaces | mcp-vs-skills-economics, plugins-and-extensions | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 294 | safety-and-sandboxing, tool-ecosystem, evidence-tiers (+10) |
| Skills | 225 | context-engineering, skills-domain-knowledge, memory-architecture (+18) |
| Subagent | 200 | safety-and-sandboxing, tool-ecosystem, agent-evaluation (+15) |
| Claude Code | 196 | context-engineering, gsd-orchestration, skills-domain-knowledge (+27) |
| CLAUDE.md | 96 | context-engineering, skills-domain-knowledge, project-infrastructure (+17) |
| Playwright | 29 | tool-ecosystem, plugins-and-extensions, mcp-patterns (+1) |
| Opus 4.6 | 20 | safety-and-sandboxing, tool-ecosystem, evidence-tiers (+4) |
| Cursor | 18 | secure-code-generation, tool-ecosystem, mcp-patterns |
| /plugin | 12 | tool-ecosystem, recursive-evolution, plugins-and-extensions (+3) |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | tool-ecosystem, context-engineering |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | tool-ecosystem, subagent-orchestration |
| /rewind | 3 | context-engineering, project-infrastructure |
| /fast | 1 | context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| documentation-maintenance | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # PostTo... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| context-engineering | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| context-engineering | v2.1.30+ | Starts fresh (no summary) - `/rewind` > "Summarize from here... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| github-actions-integration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   github-... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| parallel-sessions | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| evidence-tiers | v2.1.30+ |  | **Feature availability** | Until next major version | Ver... |
| evidence-tiers | v1.2.0 | uction-validation: 1-of-2  # Have 1 case study, need 1 more ... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.0.45+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| mcp-patterns | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # MCP su... |
| mcp-patterns | v2.1.0+ | ectories 4. **Development databases only** - Never connect t... |
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| spec-driven-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 4x | 0+" measurement-claims:   - claim: "Playwright CLI... | tool-ecosystem | 5 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 221 |
| 77% | 0+" measurement-claims:   - claim: "Token savings:... | progressive-disclosure | 5 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 131 |
| 3 times | " > — Boris Cherny, Claude Code Creator  ### Multi... | documentation-maintenance | 231 |
| 3x | md  ## Project Context [Standard project-specific ... | documentation-maintenance | 281 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 80% | 0+" status: "PRODUCTION" last-verified: "2026-02-1... | framework-selection-guide | 6 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 183 |
| 70% | 30+"  # Session memory feature measurement-claims:... | session-learning | 5 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 9 |
| 50% | 0+" measurement-claims:   - claim: "Skills are 50%... | mcp-vs-skills-economics | 5 |
| 38% | 78 per task)"     source: "Tenzir production data"... | mcp-vs-skills-economics | 9 |
| 1% | 1% of total context processed"     source: "Anthro... | context-engineering | 6 |
| 39% | xt processed"     source: "Anthropic Engineering B... | context-engineering | 10 |
| 4x | 0+"  # Skills auto-reload feature measurement-clai... | plugins-and-extensions | 5 |
| 4x | net/2025/Oct/16/claude-skills/)  This principle is... | plugins-and-extensions | 130 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 50% | 0+"  # Official skills support measurement-claims:... | skills-domain-knowledge | 5 |
| 20% | illustration" vs "flat design" | | **Include color... | ai-image-generation | 240 |
| 10x | 30+"  # Session memory feature measurement-claims:... | memory-architecture | 5 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 246 |
| 85% | ource Type) Source: [Name/Title] URL: [if applicab... | evidence-tiers | 85 |
| 10x | **Be transparent** - Acknowledge uncertainty in yo... | evidence-tiers | 100 |
| 85% | 0+"   beta-header: "advanced-tool-use-2025-11-20" ... | advanced-tool-use | 6 |
| 37% | 7K tokens)"     source: "Anthropic Engineering Blo... | advanced-tool-use | 10 |
| 84% | 45+"  # PermissionRequest hook measurement-claims:... | advanced-hooks | 6 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 786 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 43% | Jones"     date: "2025-10-15"     revalidate: "202... | mcp-patterns | 9 |
| 43% | abilities **Symptom**: Security nightmares, confus... | mcp-patterns | 60 |
| 2x | oach | Improvement | |-----------|----------------... | recursive-context-management | 75 |
| 33% | -----------|-------------------|--------------|---... | recursive-context-management | 75 |
| 100% | 0+" measurement-claims:   - claim: "AI will never ... | agent-principles | 5 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 47 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-02-21T06:32:22.750547
