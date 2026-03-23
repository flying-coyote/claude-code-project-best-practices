# Tools & Patterns Tracker
**Last Updated**: 2026-03-23
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
| CLAUDE.md | parallel-sessions, plugins-and-extensions, advanced-hooks, ... (19 more) | 22 |
| prompts | plugins-and-extensions, mcp-patterns, advanced-hooks, ... (12 more) | 15 |
| skills | plugins-and-extensions, progressive-disclosure, skills-domain-knowledge, ... (2 more) | 5 |
| tools | tool-ecosystem, subagent-orchestration, framework-selection-guide, ... (4 more) | 7 |
| mcp | mcp-patterns, mcp-vs-skills-economics, mcp-daily-essentials | 3 |
| sub-agents | plugins-and-extensions, subagent-orchestration, context-engineering | 3 |
| slash-commands | parallel-sessions, plugins-and-extensions, progressive-disclosure, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 381 | plugins-and-extensions, advanced-hooks, evidence-tiers (+13) |
| Skills | 237 | plugins-and-extensions, architecture-decision-records, progressive-disclosure (+20) |
| Subagent | 218 | plugins-and-extensions, advanced-hooks, agent-principles (+15) |
| Claude Code | 217 | plugins-and-extensions, architecture-decision-records, advanced-tool-use (+29) |
| CLAUDE.md | 107 | plugins-and-extensions, architecture-decision-records, progressive-disclosure (+19) |
| Playwright | 50 | plugins-and-extensions, evidence-tiers, mcp-daily-essentials (+2) |
| Opus 4.6 | 22 | evidence-tiers, subagent-orchestration, safety-and-sandboxing (+5) |
| /plugin | 21 | plugins-and-extensions, recursive-evolution, mcp-daily-essentials (+5) |
| Cursor | 18 | mcp-patterns, secure-code-generation, tool-ecosystem |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | tool-ecosystem, context-engineering |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | subagent-orchestration, tool-ecosystem |
| /rewind | 3 | context-engineering, project-infrastructure |
| /clear | 2 | advanced-hooks, context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| parallel-sessions | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| mcp-patterns | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # MCP su... |
| mcp-patterns | v2.1.0+ | ectories 4. **Development databases only** - Never connect t... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.1.76+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.1.32+ | unicate** | Subagents only report back to parent | Agent tea... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| github-actions-integration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   github-... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| spec-driven-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| planning-first-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| evidence-tiers | v2.1.30+ |  | **Feature availability** | Until next major version | Ver... |
| evidence-tiers | v1.2.0 | uction-validation: 1-of-2  # Have 1 case study, need 1 more ... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 10% | ogs go to files with machine-readable formatting (... | parallel-sessions | 432 |
| 4x | 0+"  # Skills auto-reload feature version-last-ver... | plugins-and-extensions | 6 |
| 50% | dated secondary - community + expert practitioner)... | plugins-and-extensions | 23 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 43% | Jones"     date: "2025-10-15"     revalidate: "202... | mcp-patterns | 10 |
| 43% | ervers-1-0/) (Evidence Tier A)  **Evidence Tier**:... | mcp-patterns | 31 |
| 84% | vent types, prompt/agent hook types version-last-v... | advanced-hooks | 7 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 849 |
| 100% | 0+" version-last-verified: "2026-02-27" measuremen... | agent-principles | 6 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 48 |
| 70% | 30+"  # Session memory feature version-last-verifi... | session-learning | 6 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 10 |
| 4x | 0+" version-last-verified: "2026-02-27" measuremen... | tool-ecosystem | 6 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 222 |
| 80% | 0+"  # Native subagent support version-last-verifi... | subagent-orchestration | 6 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 22 |
| 77% | 0+" version-last-verified: "2026-02-27" measuremen... | progressive-disclosure | 6 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 132 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 80% | 0+" version-last-verified: "2026-02-27" status: "P... | framework-selection-guide | 7 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 184 |
| 50% | 0+"  # Official skills support version-last-verifi... | skills-domain-knowledge | 6 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 10x | 30+"  # Session memory feature version-last-verifi... | memory-architecture | 6 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 247 |
| 20% | illustration" vs "flat design" | | **Include color... | ai-image-generation | 240 |
| 2x | oach | Improvement | |-----------|----------------... | recursive-context-management | 75 |
| 33% | -----------|-------------------|--------------|---... | recursive-context-management | 75 |
| 84% | Sandboxing | After Sandboxing | |--------|--------... | safety-and-sandboxing | 61 |
| 1x | 1x standard | Models after Feb 1, 2026 |  ### Conf... | safety-and-sandboxing | 161 |
| 10x | **Why it matters**: - 10x productivity gain for ex... | productivity-tooling | 29 |
| 5% | time** | < 5 seconds | Optimize shell config | | *... | productivity-tooling | 219 |
| 20% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |
| 60% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-03-23T14:49:34.486891
