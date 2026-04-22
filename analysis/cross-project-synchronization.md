---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "4-phase enrichment cascade in mndr-review-automation: Inspector MCP → Investigator API → TME Playbook MCP → Config Assessment"
    source: "Direct analysis — mndr-review-automation/scripts/run_review.py lines 1348-1364"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Scheduled cross-repo dependency monitoring runs weekday mornings checking corelight-inspector for breaking changes"
    source: "Direct analysis — third-brain/.claude/scheduled_tasks.json"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Dynamic module import from health-inventory to mndr-review-automation via Python importlib (HumioClient, HealthEvaluator, BestPracticesEvaluator)"
    source: "Direct analysis — mndr-review-automation/lib/data_loader.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [commit-cross-repo, project-type-multi-repo]
revalidate-by: 2026-10-06
---

# Cross-Project Synchronization: How Changes Cascade Across Repos

**Evidence Tier**: A — Direct observation of dependency chains across 7 repositories

## Purpose

This document analyzes how changes in one repository cascade to others in an agent-driven development portfolio — the dependency tracking, integration patterns, and synchronization mechanisms that prevent silent breakage when upstream repos change. The key insight: without explicit synchronization mechanisms, cross-repo dependencies become invisible until they break during a customer engagement.

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

## Three Synchronization Mechanisms

### 1. Scheduled Dependency Monitoring

third-brain runs a cron task (`17 9 * * 1-5` — weekday mornings at 9:17 AM) that checks corelight-inspector for upstream changes:

```json
{
  "cron": "17 9 * * 1-5",
  "prompt": "Pull the latest corelight-inspector changes and check for updates
             that affect the MNDR automation integration.
             Check: src/tools/ (tool signatures), src/lib/schemas/ (log type schemas),
             src/lib/helpers/router.ts (MCP transport protocol), package.json (version bumps).
             If any changed, summarize impact on lib/inspector_client.py in mndr-review-automation."
}
```

**What this catches**: Tool signature changes in corelight-inspector that would break `InspectorClient.profile_entity()` or `get_alert_context()` calls. Without this monitoring, the breakage would only be discovered when the MNDR pipeline runs during a customer review.

**Design choice**: 9:17 AM (not :00 or :30) to avoid coinciding with fleet-level scheduled tasks.

### 2. Dynamic Module Import

mndr-review-automation imports core modules from health-inventory at runtime via `importlib`:

```python
# lib/data_loader.py
def _load_module_from_health_inventory(module_name, filename):
    # Uses PS_HEALTH_INVENTORY_PATH from .env
    # Fallback: ~/Git projects/health-inventory
```

**Modules imported**: `HumioClient`, `HealthEvaluator`, `BestPracticesEvaluator`, NDJSON parsers, unified CSV loader

**Why dynamic import instead of fork**: Changes to health-inventory (new collectors, threshold calibration, evaluator improvements) flow automatically to mndr-review-automation. No merge, no sync — the next pipeline run uses the updated code.

**Trade-off**: A breaking change in health-inventory breaks mndr-review-automation immediately. This is acceptable because both repos are single-developer and the breakage is visible (test failure) rather than silent (stale fork).

### 3. Hub-Spoke Progress Tracking

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

## The Enrichment Cascade

The most complex cross-repo dependency is mndr-review-automation's 4-phase enrichment pipeline, where each phase calls a different external service or repo:

### Phase 1: Inspector MCP Enrichment

- **Source**: corelight-inspector (TypeScript MCP server)
- **Client**: `lib/inspector_client.py` (JSON-RPC 2.0, localhost-only)
- **Data**: Entity profiles, alert context, log searches
- **Injection**: `<!-- INSPECTOR CONTEXT -->` HTML comment blocks in findings markdown

### Phase 2: Investigator API Enrichment

- **Source**: Corelight Investigator (GraphQL API, cloud service)
- **Client**: `lib/investigator_client.py`
- **Data**: Alert metadata, detection matches, log job results
- **Injection**: `<!-- INVESTIGATOR CONTEXT -->` blocks

### Phase 3: TME Playbook MCP Enrichment

- **Source**: tme-mcp-server (Python MCP server)
- **Client**: `lib/tme_playbook_client.py` (JSON-RPC 2.0, localhost-only, retry with backoff)
- **Data**: Matched investigation playbooks, execution results
- **Injection**: `<!-- TME PLAYBOOK ENRICHMENT -->` blocks

### Phase 4: Config Assessment Enrichment

- **Source**: health-inventory (Python, dynamic import)
- **Client**: `lib/config_assessment/` (direct Python call)
- **Data**: Sensor configuration deviations, compliance scores
- **Injection**: `<!-- CONFIG ASSESSMENT -->` blocks

### Context Aggregation

The LLM step extracts all enrichment blocks via regex:

```python
_tme = re.search(
    r"<!-- TME PLAYBOOK ENRICHMENT -->(.*?)<!-- END TME PLAYBOOK ENRICHMENT -->",
    finding_text, re.DOTALL
)
```

**Critical design property**: Each enrichment phase is optional. If Inspector MCP is down, the pipeline continues without entity profiles. If tme-mcp-server is unavailable, playbook enrichment is skipped. The LLM receives whatever enrichment was available — degraded quality, not pipeline failure.

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
| Upstream tool signature change | Scheduled cron task (weekday mornings) | Auto-check corelight-inspector changes |
| health-inventory breaking change | mndr-review-automation test failure | 1,216 tests catch import breakage immediately |
| MCP server unavailable | InspectorClient returns `None` | Graceful degradation; enrichment is optional |
| Cross-repo state drift | cross-repo-progress.json staleness | Refreshed at session start |
| New spoke repo added | Hub doesn't know about it | Manual addition to cross-repo-progress.json |

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Forking instead of importing | Upstream improvements don't flow; maintenance doubles | Dynamic import via importlib with fallback path |
| No upstream monitoring | Breaking changes discovered during customer engagement | Scheduled dependency checks (cron task) |
| Hard dependency on enrichment | Pipeline fails when MCP server is down | Optional enrichment with graceful degradation |
| Implicit cross-repo dependencies | New developer doesn't know repos are connected | Explicit cross-project context in CLAUDE.md |
| Hub without state tracking | Every session re-discovers portfolio state | cross-repo-progress.json with recent commit counts |

---

## Sources

### Tier A (Direct Production Observation)

- mndr-review-automation enrichment cascade (April 2026) — 4-phase enrichment with HTML comment injection pattern (`scripts/run_review.py` lines 1348-1364)
- Dynamic module import pattern (April 2026) — `lib/data_loader.py` importing from health-inventory via importlib
- Scheduled dependency monitoring (April 2026) — `third-brain/.claude/scheduled_tasks.json` checking corelight-inspector
- Hub-spoke progress tracking (April 2026) — `cross-repo-progress.json` tracking 4 repos with 120 recent commits

### Related Analysis

- [Agent-Driven Development](./agent-driven-development.md) — Hub-spoke model and cross-repo coordination patterns
- [MCP Client Integration](./mcp-client-integration.md) — InspectorClient and TmePlaybookClient patterns used in enrichment
- [Local+Cloud LLM Orchestration](./local-cloud-llm-orchestration.md) — Pipeline context where enrichment feeds LLM analysis

---

*Last updated: April 2026*
