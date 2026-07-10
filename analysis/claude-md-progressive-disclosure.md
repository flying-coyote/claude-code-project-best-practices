---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "CLAUDE.md sizes range from 42-209 lines across 6 repos, correlating with project complexity and domain sensitivity"
    source: "Direct analysis — 6 repository CLAUDE.md files"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "~150 instruction cap for CLAUDE.md validated by Boris Cherny; excessive instructions degrade adherence below 80%"
    source: "Boris Cherny interviews (March 2026) + behavioral-insights.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: A
applies-to-signals: [claude-md-size, claude-md-references, claude-md-missing, claude-md-vague-descriptors, session-edit-thrashing, session-repeated-instructions]
revalidate-by: 2026-10-22
---

# CLAUDE.md Progressive Disclosure: How Project Context Scales

> **Collapsed 2026-07-10 (Reduction Phase 4).** The prescription is now first-party (official CLAUDE.md guidance: include/exclude table, imports, child files, "prune ruthlessly"; /init). Kept delta: the portfolio's measured 42–209-line data and the ~150-line boundary evidence.

**Evidence Tier**: Mixed (A-B) — Direct observation across 6 repos (Tier A), validated by Boris Cherny ~150 instruction cap (Tier B)

## Purpose

This document tracks how CLAUDE.md size scales with project complexity, based on direct observation across 6 repositories. What remains here is the measured portfolio: the 42-209 line size range across six repos, and the ~150-instruction adherence boundary reported by Boris Cherny.

---

## Three Maturity Tiers

### Tier 1: Minimal (42-57 lines)

**Examples**: zeek-iceberg-demo (55 lines), network-visualization-services (42 lines), third-brain (57 lines)

**Sections**: Project overview, quick reference commands, key files, git workflow

**When appropriate**: Demos, reference implementations, lightweight services, knowledge management. The project has clear boundaries and the agent doesn't need extensive guardrails.

**Typical structure**:

```markdown
# Project Name
One-paragraph description.

## Commands
- `npm run build` — Build project
- `pytest tests/` — Run tests

## Key Files
- `src/main.py` — Entry point
- `config/settings.yaml` — Configuration

## Git Workflow
Commit prefixes: feat:, fix:, docs:
```

### Tier 2: Resource Map (99-112 lines)

**Examples**: health-inventory (112 lines)

**Sections**: Commands, critical query parameters, resource map (organized by directory: scripts/, lib/, config/, data/, tests/, docs/), environment variables, known gotchas, workflow

**When appropriate**: Data pipelines, monitoring systems, projects with multiple entry points and domain-specific conventions. The agent needs to know where things are and what conventions to follow, but doesn't handle sensitive data.

**Key addition over Tier 1**: The **resource map** — a structured directory of what's where, organized by function rather than alphabetically. This prevents the agent from spending tokens exploring the filesystem.

### Tier 3: Rules + Security (166-209 lines)

**Examples**: mndr-review-automation (166 lines), Splunk-db-connect-benchmark (209 lines)

**Sections**: Security boundaries (FIRST), architecture (pipeline steps, intake workflow, escalation triggers), key paths (extensive file list), relationship to other repos, rules, tests inventory

**When appropriate**: Production pipelines with sensitive data, complex multi-step architectures, projects with compliance requirements. The agent needs both domain context and hard constraints.

**Critical pattern**: mndr-review-automation opens with **"Security Boundaries — READ THIS FIRST"** before any other content. This front-loading ensures the agent encounters data isolation rules before it encounters any instructions that might tempt it to read raw customer data.

---

## Comparison Across 6 Repos

| Repository | Lines | Tier | First Section | Rules | Commands | Agents |
|-----------|-------|------|---------------|-------|----------|--------|
| network-visualization-services | 42 | 1 | Status + service framework | 0 | 1 | 0 |
| zeek-iceberg-demo | 55 | 1 | Project overview + OCSF pipeline | 0 | 4 | 0 |
| third-brain | 57 | 1 | Knowledge management lifecycle | 5 | 0 | 0 |
| health-inventory | 112 | 2 | Commands + critical parameters | 4 | 0 | 0 |
| mndr-review-automation | 166 | 3 | **Security Boundaries** | 4 | 0 | 1 |
| Splunk-db-connect-benchmark | 209 | 3 | Purpose + architecture | 0 | 4 | 0 |

### Disclosure Hierarchy Within Each File

Regardless of tier, a consistent ordering emerges:

1. **Lines 1-10**: Project identity + immediate action items (or security boundaries for sensitive projects)
2. **Lines 10-30**: Quick reference commands and critical parameters
3. **Lines 30-60**: Resource map (file organization, key modules)
4. **Lines 60+**: Specialized concerns (architecture detail, tests, integrations, gotchas)

---

## The ~150-Instruction Boundary

Boris Cherny's guidance (March 2026): Keep CLAUDE.md under ~150 instructions. Beyond this, adherence drops below the already-imperfect ~80% baseline.

---

## Sources

### Tier A (Direct Production Observation)

- 6-repository CLAUDE.md comparison (April 2026) — Line counts, section structures, tier classification across zeek-iceberg-demo, third-brain, mndr-review-automation, health-inventory, network-visualization-services, Splunk-db-connect-benchmark

### Tier B (Validated / Expert Practitioner)

- Boris Cherny (March 2026) — ~150 instruction cap, CLAUDE.md as advisory (~80% adherence), hooks for enforcement

### Related Analysis

- [Behavioral Insights](./behavioral-insights.md) — ~80% CLAUDE.md adherence rate, 60% context degradation threshold, ~150 instruction cap

---

*Last updated: July 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
