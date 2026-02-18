# Tools & Patterns Tracker
**Last Updated**: 2026-02-18
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
| CLAUDE.md | agent-principles, plugins-and-extensions, memory-architecture, ... (17 more) | 20 |
| prompts | plugins-and-extensions, memory-architecture, progressive-disclosure, ... (10 more) | 13 |
| skills | plugins-and-extensions, skills-domain-knowledge, progressive-disclosure, ... (2 more) | 5 |
| tools | skills-domain-knowledge, project-infrastructure, tool-ecosystem, ... (2 more) | 5 |
| mcp | mcp-vs-skills-economics, mcp-patterns | 2 |
| sub-agents | plugins-and-extensions, subagent-orchestration, context-engineering | 3 |
| slash-commands | plugins-and-extensions, architecture-decision-records, project-infrastructure, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 294 | framework-selection-guide, plugins-and-extensions, safety-and-sandboxing (+10) |
| Skills | 225 | spec-driven-development, plugins-and-extensions, recursive-evolution (+18) |
| Subagent | 200 | gsd-orchestration, agent-principles, framework-selection-guide (+15) |
| Claude Code | 196 | spec-driven-development, agent-principles, plugins-and-extensions (+27) |
| CLAUDE.md | 96 | spec-driven-development, agent-principles, plugins-and-extensions (+17) |
| Playwright | 29 | evidence-tiers, plugins-and-extensions, tool-ecosystem (+1) |
| Opus 4.6 | 20 | safety-and-sandboxing, parallel-sessions, evidence-tiers (+4) |
| Cursor | 18 | mcp-patterns, secure-code-generation, tool-ecosystem |
| /plugin | 12 | plugins-and-extensions, mcp-patterns, github-actions-integration (+3) |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | context-engineering, tool-ecosystem |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | subagent-orchestration, tool-ecosystem |
| /rewind | 3 | project-infrastructure, context-engineering |
| /fast | 1 | context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| project-infrastructure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Checkp... |
| project-infrastructure | v2.0.0+ | de features enhance project infrastructure without any confi... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| documentation-maintenance | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # PostTo... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.0.45+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| planning-first-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.0.60+ |  Result: Independent verification without implementation bia... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| spec-driven-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| parallel-sessions | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| context-engineering | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| context-engineering | v2.1.30+ | Starts fresh (no summary) - `/rewind` > "Summarize from here... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 100% | 0+" measurement-claims:   - claim: "AI will never ... | agent-principles | 5 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 47 |
| 4x | 0+"  # Skills auto-reload feature measurement-clai... | plugins-and-extensions | 5 |
| 4x | net/2025/Oct/16/claude-skills/)  This principle is... | plugins-and-extensions | 130 |
| 10x | 30+"  # Session memory feature measurement-claims:... | memory-architecture | 5 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 246 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 50% | 0+"  # Official skills support measurement-claims:... | skills-domain-knowledge | 5 |
| 3x | oject Name  ## Purpose [What this project does]  #... | project-infrastructure | 129 |
| 1x | 1x standard pricing |  **Availability**: Models re... | project-infrastructure | 262 |
| 77% | 0+" measurement-claims:   - claim: "Token savings:... | progressive-disclosure | 5 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 131 |
| 70% | 30+"  # Session memory feature measurement-claims:... | session-learning | 5 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 9 |
| 3 times | " > — Boris Cherny, Claude Code Creator  ### Multi... | documentation-maintenance | 231 |
| 3x | md  ## Project Context [Standard project-specific ... | documentation-maintenance | 281 |
| 84% | 45+"  # PermissionRequest hook measurement-claims:... | advanced-hooks | 6 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 786 |
| 4x | 0+" measurement-claims:   - claim: "Playwright CLI... | tool-ecosystem | 5 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 221 |
| 20% | 0+" measurement-claims:   - claim: "Planning effor... | planning-first-development | 5 |
| 60% | 0+" measurement-claims:   - claim: "Planning effor... | planning-first-development | 5 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 80% | 0+"  # Native subagent support measurement-claims:... | subagent-orchestration | 5 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 18 |
| 80% | 0+" status: "PRODUCTION" last-verified: "2026-02-1... | framework-selection-guide | 6 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 183 |
| 85% | 0+"   beta-header: "advanced-tool-use-2025-11-20" ... | advanced-tool-use | 6 |
| 37% | 7K tokens)"     source: "Anthropic Engineering Blo... | advanced-tool-use | 10 |
| 40% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 64 |
| 20% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 65 |
| 2x | oach | Improvement | |-----------|----------------... | recursive-context-management | 75 |
| 33% | -----------|-------------------|--------------|---... | recursive-context-management | 75 |
| 84% | Sandboxing | After Sandboxing | |--------|--------... | safety-and-sandboxing | 61 |
| 1x | 1x standard | Models after Feb 1, 2026 |  ### Conf... | safety-and-sandboxing | 161 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-02-18T06:52:49.385885
