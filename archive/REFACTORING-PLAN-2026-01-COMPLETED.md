# Claude Code Best Practices Refactoring Plan

**Created**: January 26, 2026
**Status**: Planning
**Triggered By**: Gap analysis from Second Brain LinkedIn captures and web research

---

## Executive Summary

Analysis of recent thought leader content (January 10-26, 2026) identified **7 missing patterns** and **2 patterns needing enhancement** in the Claude Code Best Practices project. This plan documents the gaps and prioritizes implementation.

---

## Gap Analysis Summary

### Missing Patterns (Priority Order)

| # | Pattern | Source | Priority | Effort |
|---|---------|--------|----------|--------|
| 1 | GSD (Get Shit Done) Orchestration | glittercowboy/get-shit-done | HIGH | Medium |
| 2 | Johari Window / SAAE Protocol | skribblez2718/caii | HIGH | Low |
| 3 | CAII Cognitive Agent Infrastructure | skribblez2718/caii | MEDIUM | Medium |
| 4 | MCP vs Skills Economics | Tenzir Blog (Vallentin) | MEDIUM | Low |
| 5 | Claude-Flow Enterprise Patterns | ruvnet/claude-flow | LOW | High |
| 6 | Rodriguez Threat Hunter Skills | Open Threat Research | LOW | Medium |
| 7 | Marimo CLAUDE.md Pattern | YouTube Short | LOW | Low |

### Patterns Needing Enhancement

| Pattern | Current State | Enhancement Needed |
|---------|---------------|-------------------|
| context-engineering.md | Basic coverage | Add GSD, Claude-Flow, Marimo frameworks |
| subagent-orchestration.md | General patterns | Add GSD fresh-context-per-task model |

---

## Detailed Gap Specifications

### 1. GSD (Get Shit Done) Orchestration Pattern

**Source**: https://github.com/glittercowboy/get-shit-done
**Evidence Tier**: B (open source, production-validated)
**Priority**: HIGH - Addresses core orchestration gap

**Key Elements to Document**:
- Orchestrator agent spawns specialized subagents
- Fresh context window per subagent (prevents context rot)
- `STATE.md` for state externalization across sessions
- `.planning/` directory structure:
  ```
  .planning/
  ├── STATE.md           # Current project state
  ├── phases/            # Phase definitions
  ├── tasks/             # XML task specifications
  └── research/          # Research artifacts
  ```
- Atomic commits (one git commit per task)
- Workflow: Initialize → Discuss → Plan → Execute (parallel) → Verify → Complete
- XML task formatting optimized for Claude parsing

**File to Create**: `patterns/gsd-orchestration.md`

**Integration Points**:
- Link from subagent-orchestration.md
- Link from context-engineering.md
- Add to SOURCES.md

---

### 2. Johari Window / SAAE Protocol

**Source**: https://github.com/skribblez2718/caii
**Evidence Tier**: B (production implementation)
**Priority**: HIGH - Addresses ambiguity surfacing gap

**Key Elements to Document**:
- Four quadrants framework:
  - **ARENA (OPEN)**: Known to both Claude and user
  - **BLIND SPOT**: Known to Claude, unknown to user
  - **HIDDEN**: Known to user, unknown to Claude
  - **UNKNOWN**: Unknowns for both
- SAAE Protocol: SHARE → ASK → ACKNOWLEDGE → EXPLORE
- When to use:
  - Complex implementations (3+ files)
  - Architecture decisions
  - Expert interviews
  - Multi-step workflows with unclear requirements
- Anti-pattern: Proceeding without surfacing assumptions

**File to Create**: `patterns/johari-window-ambiguity.md`

**Skill Example to Create**: `skills/examples/johari-window-clarifier/SKILL.md`

---

### 3. CAII Cognitive Agent Infrastructure

**Source**: https://github.com/skribblez2718/caii
**Author**: Kristoffer Sketch
**Evidence Tier**: B (documented implementation)
**Priority**: MEDIUM - Alternative architecture approach

**Key Elements to Document**:
- 7 Cognitive Agents (vs domain-specific proliferation):
  1. Clarification
  2. Research
  3. Analysis
  4. Synthesis
  5. Generation
  6. Validation
  7. Memory/Metacognition
- Philosophy: "As capabilities grow, domain-specific agent count becomes unsustainable"
- Python orchestration enforces deterministic step ordering
- Learning & Memory system:
  - Task-specific memories: `{task_id}-{agent}-memory.md`
  - Indexed learnings referenced before future tasks
  - System becomes "more autonomous over time"

**File to Create**: `patterns/cognitive-agent-infrastructure.md`

**Comparison Table to Add**:
| Approach | Agent Count | Maintenance | Context Strategy |
|----------|-------------|-------------|------------------|
| Domain-specific | N (grows) | High | Specialized |
| CAII Cognitive | 7 (fixed) | Low | On-the-fly context |
| GSD | ~5 | Medium | Fresh per subagent |

---

### 4. MCP vs Skills Economics

**Source**: Tenzir Blog - "We Did MCP Wrong" (Matthias Vallentin, January 2026)
**Evidence Tier**: B (production data)
**Priority**: MEDIUM - Cost optimization guidance

**Key Data to Document**:

| Metric | MCP | Skills | Winner |
|--------|-----|--------|--------|
| Duration | 6.2 min | 8.6 min | MCP (38% faster) |
| Tool calls | 61 | 52 | Skills (15% fewer) |
| **Cost** | $20.78 | $10.27 | **Skills (50% cheaper)** |
| Cached tokens | 8.8M | 4.0M | Skills (55% less) |

**Philosophy Shift to Document**:
- **Before**: Force-feed structured context
- **After**: Provide capabilities and documentation

**Decision Framework**:
- **Use MCP for**: Sandboxed execution, deterministic validation, pipeline orchestration, persistent connections
- **Use Skills for**: Cloud workflows, portable instructions, cost-sensitive tasks

**File to Create**: `patterns/mcp-vs-skills-economics.md`

---

### 5. Claude-Flow Enterprise Patterns

**Source**: https://github.com/ruvnet/claude-flow
**Evidence Tier**: B (production-focused documentation)
**Priority**: LOW - Enterprise-scale, complex to implement

**Key Elements to Document**:
- Scale: 60+ specialized agents, 42 pre-built skills, 170+ MCP native tools
- SONA Self-Learning: <0.05ms adaptation, EWC++ prevents knowledge loss
- Vector Memory (HNSW): 150x-12,500x faster pattern retrieval
- 6 Swarm Topologies:
  1. Hierarchical
  2. Mesh
  3. Ring
  4. Star
  5. Hybrid
  6. Adaptive
- ReasoningBank: Trajectory storage with semantic pattern matching
- Performance claims: 250% Claude Code usage extension

**File to Create**: `patterns/claude-flow-enterprise.md`

**Note**: Complex system, document as reference architecture rather than implementation guide.

---

### 6. Rodriguez Threat Hunter Playbook Agent Skills

**Source**: Roberto Rodriguez (Open Threat Research)
**LinkedIn**: January 12, 2026
**Evidence Tier**: B (domain-specific, production implementation)
**Priority**: LOW - Security domain-specific

**Key Elements to Document**:
- 5 Hunt Planning Skills:
  1. hunt-research-system-and-tradecraft
  2. hunt-focus-definition
  3. hunt-data-source-identification
  4. hunt-analytics-generation
  5. hunt-blueprint-generation
- Progressive disclosure for threat hunting
- MCP integration: Tavily (web search), MS Sentinel (semantic discovery)
- Hunt Lifecycle: Plan → Execute → Report

**Files to Create**:
- Add to SOURCES.md
- `skills/examples/threat-hunter-skills/` directory with example skills

---

### 7. Marimo CLAUDE.md Pattern

**Source**: YouTube Short (January 26, 2026)
**Evidence Tier**: C (community adoption signal)
**Priority**: LOW - Narrow use case, but signals pattern spread

**Key Elements to Document**:
- Marimo notebooks auto-detect CLAUDE.md in project root
- Contents injected into AI context during notebook interaction
- Significance: CLAUDE.md pattern spreading beyond Claude Code
- Data science tools adopting developer tooling patterns

**File to Update**: `patterns/context-engineering.md` (add as subsection)

---

## Enhancement Specifications

### context-engineering.md Updates

**Current State**: Basic coverage of context management
**Enhancement**: Add frameworks section with:

1. **GSD Pattern** - Fresh context per subagent
2. **Claude-Flow** - Vector memory and swarm topologies (reference)
3. **Marimo** - Tool-agnostic CLAUDE.md adoption
4. **Comparison table** of approaches

### subagent-orchestration.md Updates

**Current State**: General subagent patterns
**Enhancement**: Add section on:

1. **Fresh Context Model** (GSD) - Why and how to spawn with clean context
2. **Orchestrator responsibilities** - Task distribution, not generation
3. **State externalization** - `STATE.md` pattern

---

## Implementation Order

### Phase 1: High Priority (Week of Jan 27)
1. `patterns/gsd-orchestration.md` - Core orchestration pattern
2. `patterns/johari-window-ambiguity.md` - Ambiguity surfacing
3. Update SOURCES.md with new sources

### Phase 2: Medium Priority (Week of Feb 3)
4. `patterns/mcp-vs-skills-economics.md` - Cost optimization
5. `patterns/cognitive-agent-infrastructure.md` - Alternative architecture
6. Update `patterns/context-engineering.md` with new frameworks
7. Update `patterns/subagent-orchestration.md` with GSD model

### Phase 3: Low Priority (Week of Feb 10)
8. `patterns/claude-flow-enterprise.md` - Enterprise reference
9. `skills/examples/johari-window-clarifier/SKILL.md` - Skill example
10. Add Rodriguez sources and examples
11. Regenerate INDEX.md

---

## Source References

### Primary Sources (Tier A)
- Anthropic Engineering Blog (existing)
- Boris Cherny interviews (existing)

### New Sources to Add (Tier B)
| Source | URL | Key Contribution |
|--------|-----|------------------|
| GSD | github.com/glittercowboy/get-shit-done | Orchestrator pattern |
| CAII | github.com/skribblez2718/caii | Johari Window, Cognitive agents |
| Claude-Flow | github.com/ruvnet/claude-flow | Enterprise patterns |
| Tenzir Blog | blog.tenzir.com | MCP vs Skills economics |
| Roberto Rodriguez | LinkedIn, Open Threat Research | Threat hunter skills |

### Community Sources (Tier C)
| Source | Platform | Key Contribution |
|--------|----------|------------------|
| Kristoffer Sketch | LinkedIn (Jan 14) | CAII announcement |
| Marimo | YouTube Short | CLAUDE.md tool adoption |

---

## Success Criteria

- [ ] All 7 missing patterns documented
- [ ] 2 existing patterns enhanced
- [ ] SOURCES.md updated with all new references
- [ ] INDEX.md regenerated
- [ ] Cross-links established between related patterns
- [ ] At least 1 new skill example (johari-window-clarifier)

---

## Notes

- GSD and Johari Window are highest value additions - address core gaps
- Claude-Flow is reference material (too complex for direct implementation)
- Rodriguez skills are domain-specific but demonstrate progressive disclosure well
- MCP vs Skills economics provides actionable cost guidance

---

*This plan was generated from gap analysis of Second Brain captures (January 10-26, 2026)*
