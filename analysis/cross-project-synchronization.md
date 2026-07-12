---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: A
convergence: single-source
applies-to-signals: [commit-cross-repo, project-type-multi-repo]
revalidate-by: 2026-10-06
---

# Cross-Project Synchronization: How Changes Cascade Across Repos

> **Collapsed 2026-07-10 (Reduction Phase 4).** The multi-session mechanics are now first-party (agent teams v2 + worktrees docs). Kept delta: the hub-spoke portfolio evidence.

**Evidence Tier**: A — Direct observation of dependency chains across 7 repositories

## Purpose

This document is evidence of a hub-spoke portfolio structure in an agent-driven development environment: which repos are the hub, which are spokes, how the dependency graph is shaped, and how much of it a spoke's CLAUDE.md documents explicitly. The mechanics that used to hold this together by hand — scheduled dependency checks, dynamic module imports, a multi-phase enrichment pipeline — are now covered by first-party agent teams v2 and worktrees. What survives here is the measured portfolio state those mechanics were built to protect: which repos exist, what role each plays, and how active each one is.

Convergence status is single-source (this portfolio's own observation, no verified external adoption evidence), so adopting the tracking patterns below as new infrastructure requires converged status or an explicit owner exception.

---

## The Dependency Graph

```
corelight-inspector (upstream, external)
        │
        │ tool signatures, schemas, protocol
        ▼
third-brain (hub) ◄──────────────────────────────────────┐
    │           │                                          │
    │ hypotheses│ evidence, coordination                   │ cross-repo-progress.json
    │           │                                          │
    ▼           ▼                                          │
mndr-review-automation ◄── health-inventory                │
    │   │   │   │              │                           │
    │   │   │   │  HumioClient,│HealthEvaluator,           │
    │   │   │   │  BPEvaluator │via importlib              │
    │   │   │   │              │                           │
    │   │   │   └──────────────┘                           │
    │   │   │                                              │
    │   │   └── tme-mcp-server (MCP enrichment)            │
    │   │                                                  │
    │   └── corelight-inspector (MCP enrichment)           │
    │                                                      │
    └──────────────────────────────────────────────────────┘
                evidence flows back to hub

network-visualization-services (reads from all spokes)
zeek-iceberg-demo (independent pipeline, referenced by hub)
Splunk-db-connect-benchmark (independent, referenced by hub)
```

---

## Hub-Spoke Progress Tracking

third-brain maintains `cross-repo-progress.json` with real-time state across the portfolio:

```json
{
  "repos": {
    "third-brain": { "role": "hub", "recent_commits_14d": 22 },
    "mndr-review-automation": { "role": "spoke", "recent_commits_14d": 74 },
    "behavior-analytics": { "role": "spoke", "recent_commits_14d": 3 },
    "claude-code-project-best-practices": { "role": "spoke", "recent_commits_14d": 21 }
  },
  "summary": { "total_repos": 4, "total_recent_commits": 120 }
}
```

**What this enables**: Session-start awareness of portfolio activity. High-velocity spokes (74 commits in 14 days) get attention; low-activity spokes (3 commits) are deprioritized.

---

## Cross-Project CLAUDE.md References

network-visualization-services explicitly documents cross-project dependencies in its CLAUDE.md:

```
## Cross-Project Context
This repo's frameworks are validated by active work in:
- health-inventory: Config assessment engine (data quality module source)
- third-brain: H-CONFIG-01 hypothesis, baseline YAML spec
- zeek-llm-detect: AI traffic detection (MCP analysis complement)
- zeek-iceberg-demo: Iceberg pipeline reference (DuckDB validation)
- mndr-review-automation: MCP client patterns (Streamable HTTP, localhost enforcement)
- tme-mcp-server: MCP server architecture patterns
```

This makes the dependency graph explicit in the agent's context — the agent knows which repos validate which capabilities.

---

## Failure Modes and Detection

| Failure Mode | How Detected | Prevention |
|-------------|-------------|------------|
| Cross-repo state drift | cross-repo-progress.json staleness | Refreshed at session start |
| New spoke repo added | Hub doesn't know about it | Manual addition to cross-repo-progress.json |

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Implicit cross-repo dependencies | New developer doesn't know repos are connected | Explicit cross-project context in CLAUDE.md |
| Hub without state tracking | Every session re-discovers portfolio state | cross-repo-progress.json with recent commit counts |

---

## Sources

### Tier A (Direct Production Observation)

- Hub-spoke progress tracking (April 2026) — `cross-repo-progress.json` tracking 4 repos with 120 recent commits

### Related Analysis

- [Agent-Driven Development](./agent-driven-development.md) — Hub-spoke model and cross-repo coordination patterns

---

*Last updated: July 2026*

<!-- graphify-footer:start -->

## Related (from graph)

<!-- graphify-footer:end -->
