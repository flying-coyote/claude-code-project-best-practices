---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "Memory system active in 5 of 7 repos, with file counts ranging from 2 (minimal) to 13 (comprehensive hub)"
    source: "Direct analysis — ~/.claude/projects/*/memory/ directories"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Four memory types observed: user (role/preferences), project (active work), reference (external pointers), feedback (corrections/validations)"
    source: "Direct analysis — memory file frontmatter across 5 project directories"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Memory sizing correlates with project type: knowledge hubs (13 files), pipelines (2-3 files), simple projects (0 files)"
    source: "Direct analysis — 7 repository memory directories"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [project-type-docs, project-type-research]
revalidate-by: 2026-10-06
---

# Memory System Patterns: Cross-Session Context Persistence

**Evidence Tier**: A — Direct observation of memory systems across 5 project directories

## Purpose

This document analyzes how Claude Code's auto-memory system works in practice across a portfolio of projects — what gets saved, how memory files are structured, when memory is useful vs. when it creates stale assumptions, and how memory sizing correlates with project complexity. The key insight: memory is **opt-in by project**, not universal, and the right amount of memory depends on how much context is lost between sessions.

---

## Memory Architecture

### Storage Location

```
~/.claude/projects/{encoded-repo-path}/memory/
├── MEMORY.md           # Index file (always loaded into context)
├── user_role.md        # Who the user is
├── project_*.md        # Active work context
├── reference_*.md      # External system pointers
└── feedback_*.md       # Corrections and validated approaches
```

**Key property**: MEMORY.md is always loaded into conversation context. Individual memory files are loaded on demand when relevant. This is itself a progressive disclosure pattern — the index is cheap, the detail is loaded only when needed.

### Four Memory Types

| Type | Purpose | When to Save | Example |
|------|---------|-------------|---------|
| **user** | Role, goals, expertise, preferences | When you learn details about the user | "Corelight PS engineer, Suricata/Zeek/YARA security engineering" |
| **project** | Active work, goals, decisions, dependencies | When work context would be lost between sessions | "H-CONFIG-01 hypothesis, YAML baseline, deviation engine" |
| **reference** | Pointers to external systems | When external resources are discovered | "400 repos across 64 GitLab subgroups, 6 cloned locally" |
| **feedback** | Corrections and validated approaches | When the user corrects or validates behavior | "Analysis docs must be diagnostic and actionable, not just descriptive" |

### File Format

Each memory file uses YAML frontmatter:

```markdown
---
name: User Role
description: Corelight PS engineer focused on security engineering
type: user
---

Content here — for feedback/project types, structure as:
rule/fact, then **Why:** and **How to apply:** lines.
```

---

## Memory Sizing by Project Type

### Comprehensive Hub: third-brain (13 files, ~220 lines total)

The knowledge management hub needs the most memory because it coordinates across multiple projects and maintains strategic context:

| File | Type | Lines | Content |
|------|------|-------|---------|
| user_role.md | user | 13 | Corelight, security engineering role |
| project_mndr_automation.md | project | 44 | Pipeline architecture, 10 steps, Inspector MCP, revision flow |
| project_mcp_contribution.md | project | 19 | Contribute to TME MCP (Python), not Inspector (TS) |
| project_config_intelligence.md | project | 11 | H-CONFIG-01 hypothesis, YAML baseline |
| project_agent_components.md | project | 17 | 7 agent personas, 80+ atomic components |
| project_ai_forum.md | project | 15 | Weekly cross-team AI meeting context |
| project_hypothesis_structure.md | project | 11 | 19 hypotheses graduated to H-XXX-evidence.md |
| reference_gitlab_org.md | reference | 17 | 400 repos across 64 subgroups |
| reference_flying_coyote_repos.md | reference | — | 3 private repos + ocsflab.com |
| reference_inspector_mcp.md | reference | 11 | MCP server for Corelight log analysis |
| reference_mndr_standards.md | reference | 10 | Quality standards for deliverables |
| feedback_litellm_security.md | feedback | 11 | No LLM proxy libraries (supply chain risk) |

**Why this much**: third-brain is the coordination hub ([Agent-Driven Development](./agent-driven-development.md) hub-spoke pattern). Without memory, every session would start by re-discovering which projects exist, what their current state is, and what decisions have been made.

### Pipeline Projects: mndr-review-automation (2 files), health-inventory (1 file)

Production pipelines need minimal memory because:

1. The code itself is the primary context (CLAUDE.md + rules cover conventions)
2. Pipeline behavior is deterministic — no strategic decisions between sessions
3. Test suites validate correctness independent of memory

**mndr-review-automation**:

- `project_intake_workflow.md` — Google Form → work_order.yaml pipeline
- `project_investigator_test_tenant.md` — Test tenant ID + API key location

**health-inventory**:

- `project_config_assessment_backport.md` — Phase of porting deviation engine from third-brain

### Operational State: ps-health-inventory (1 large file, 126 lines)

An alternative pattern — instead of multiple small files, one comprehensive state document covering all architectural decisions, gotchas, key metrics, and deleted files. This works when the project is a single-developer data pipeline where all context is related.

### No Memory: tme-mcp-server, zeek-iceberg-demo, network-visualization-services

Simple projects don't need memory. The project context is fully captured by CLAUDE.md and the code itself. Memory would add stale assumptions without benefit.

---

## What to Save vs. What to Derive

### Save in Memory

| Category | Examples | Why |
|----------|---------|-----|
| **User role and expertise** | "Deep Go expertise, new to React" | Tailors explanation level across sessions |
| **Active project context** | "H-CONFIG-01 at Phase 4, confidence 4.7/5" | Prevents re-exploring settled decisions |
| **External system references** | "Bugs tracked in Linear project INGEST" | Points to information not in the codebase |
| **Validated approaches** | "Single bundled PR was right for this refactor" | Prevents re-debating settled preferences |
| **Corrections** | "Don't mock the database in integration tests" | Prevents repeating past mistakes |

### Derive from Code (Do NOT Save)

| Category | Why Not | Better Source |
|----------|---------|---------------|
| Code patterns and architecture | Changes with every commit | Read the code |
| Git history and recent changes | Stale within hours | `git log` / `git blame` |
| File paths and project structure | Files get renamed/moved | `ls`, `find`, Glob tool |
| Debugging solutions | Fix is in the code; commit has context | `git log --grep` |
| Ephemeral task state | Only useful in current session | Task tools |

### The Staleness Problem

Memory files are point-in-time snapshots. The ps-health-inventory memory includes timestamps ("refactored 2026-03-17", "calibrated 2026-03-24") and Claude automatically flags stale memory (>6 days). But stale markers don't prevent acting on outdated information.

**Diagnostic**: If you find yourself correcting the agent because it assumed something from memory that's no longer true, the memory needs updating or removing. Memory that's wrong is worse than no memory — it creates confident incorrect behavior.

---

## Memory and Other Persistence Mechanisms

Memory is one of several ways context persists. Use the right mechanism:

| Need | Mechanism | Scope |
|------|-----------|-------|
| Context that spans conversations | **Memory** | Cross-session |
| Alignment on implementation approach | **Plan** (plan mode) | Current conversation |
| Tracking work steps | **Tasks** | Current conversation |
| Domain conventions | **Rules files** | Per-file-pattern |
| Project context | **CLAUDE.md** | Per-session (always loaded) |
| Operational workflows | **Commands** | On invocation |
| Cross-repo state | **cross-repo-progress.json** | Custom (hub-spoke) |

---

## External Memory Systems (April 2026)

Beyond Claude Code's built-in auto-memory, external memory systems are emerging that provide cross-session persistence through different mechanisms:

### MemPalace (Local-First via MCP)

- **Repository**: https://github.com/memorylake-ai/mempalace
- **Architecture**: ChromaDB (vector search) + SQLite (structured storage), fully local
- **Integration**: `claude mcp add mempalace` — exposes 19 MCP tools for memory operations
- **Stars**: 43k+ (April 2026)
- **Maturity**: Active development, macOS ARM64 segfault reported in some configurations

**Trade-offs vs built-in auto-memory**:

| Dimension | Claude Auto-Memory | MemPalace |
|-----------|-------------------|-----------|
| Setup | Zero (built-in) | Install + MCP configuration |
| Persistence | File-based MEMORY.md | ChromaDB + SQLite |
| Search | Index scanning | Semantic vector search |
| Scope | Per-project | Cross-project (shared DB) |
| Privacy | Local files | Local (no cloud) |
| Dependencies | None | Python, ChromaDB, SQLite |

**Best for**: Users who need semantic search across large knowledge bases or cross-project memory sharing. The built-in auto-memory remains sufficient for most project-scoped workflows.

### Honcho (Server-Based, Multi-Agent)

- **Repository**: https://github.com/plastic-labs/honcho
- **Architecture**: FastAPI + PostgreSQL + pgvector, background "deriver" worker
- **Version**: v3.0.6 (production, 2.2k stars)
- **Deployment**: Docker, Fly.io, or self-hosted

**Key differentiator**: The "peer paradigm" treats all participants (human and AI) uniformly in the data model, and a background deriver generates cross-session insights asynchronously. This makes Honcho more suited to multi-agent systems with shared state than to single-developer workflows.

**Assessment**: Honcho requires PostgreSQL infrastructure, making it heavier than either MemPalace or built-in memory. It's most relevant for teams building multi-agent systems that need shared persistent state across many sessions and participants — not for individual developer workflows where Claude Code's auto-memory is sufficient.

### Choosing a Memory Approach

| Scenario | Recommended Approach |
|----------|---------------------|
| Single developer, project-scoped context | Claude Code auto-memory (built-in) |
| Cross-project knowledge, semantic search | MemPalace via MCP |
| Multi-agent shared state, team workflows | Honcho (PostgreSQL-backed) |
| Domain-specific coaching cache | File-based archive (MNDR pattern) |

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Saving code patterns to memory | Memory contradicts refactored code; agent follows stale pattern | Derive from code; only save decisions that motivated the pattern |
| No memory for hub projects | Every session re-discovers project state and dependencies | Add project + reference memories for coordination context |
| Memory for simple projects | Stale assumptions about straightforward code | No memory needed; CLAUDE.md + code is sufficient |
| Single large memory file | Hard to update; partial staleness | One file per topic; update/remove individually |
| Saving debugging solutions | Memory recommends fix for bug that's already fixed | Let git history be the record; save only the "why" if surprising |
| Never updating memory | Corrections accumulate but memories stay stale | Review and prune when correcting agent behavior |

---

## Sources

### Tier A (Direct Production Observation)

- 5-project memory directory analysis (April 2026) — third-brain (13 files), mndr-review-automation (2 files), health-inventory (1 file), ps-health-inventory (1 file, 126 lines), claude-code-project-best-practices (2 files)
- Memory type distribution: user (3 instances), project (8), reference (5), feedback (2)
- Memory absence analysis: 3 repos with no memory (tme-mcp-server, zeek-iceberg-demo, network-visualization-services)

### Tier B (Validated / Expert Practitioner)

- Anthropic Claude Code auto-memory documentation — Type taxonomy, frontmatter format, MEMORY.md index
- Boris Cherny (March 2026) — "CLAUDE.md is advisory (~80% adherence)" applies to memory instructions equally

### Related Analysis

- [CLAUDE.md Progressive Disclosure](./claude-md-progressive-disclosure.md) — Memory is one layer of the progressive disclosure stack
- [Behavioral Insights](./behavioral-insights.md) — Context thresholds affecting how much memory can be loaded effectively
- [Agent-Driven Development](./agent-driven-development.md) — Hub-spoke model where hub memory enables cross-repo coordination

---

*Last updated: April 2026*
