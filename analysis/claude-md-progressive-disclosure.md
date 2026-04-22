---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "CLAUDE.md sizes range from 42-209 lines across 6 repos, correlating with project complexity and domain sensitivity"
    source: "Direct analysis — 6 repository CLAUDE.md files"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Progressive disclosure across 4 mechanisms: CLAUDE.md tiers, rules/ files, commands/ files, and skills/ directories"
    source: "Direct analysis — 7 repository .claude/ directories"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "~150 instruction cap for CLAUDE.md validated by Boris Cherny; excessive instructions degrade adherence below 80%"
    source: "Boris Cherny interviews (March 2026) + behavioral-insights.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: "PRODUCTION"
last-verified: "2026-04-06"
---

# CLAUDE.md Progressive Disclosure: How Project Context Scales

**Evidence Tier**: Mixed (A-B) — Direct observation across 6 repos (Tier A), validated by Boris Cherny ~150 instruction cap (Tier B)

## Purpose

This document analyzes how CLAUDE.md evolves as projects grow — from minimal project overview to comprehensive resource map with security boundaries, domain rules, and operational commands. The key insight from [Behavioral Insights](./behavioral-insights.md): CLAUDE.md adherence is ~80%, and context degrades above ~150 instructions. Progressive disclosure solves this by keeping CLAUDE.md lean and pushing domain-specific detail into rules, commands, and skills files that load only when relevant.

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

## Four Disclosure Mechanisms

CLAUDE.md is only the first layer. Progressive disclosure distributes domain knowledge across four mechanisms, each loaded at different times:

### 1. CLAUDE.md (Always Loaded)

Loaded at session start. Counts against the ~150 instruction budget. Must be lean enough for the agent to absorb fully. Front-load critical constraints (security boundaries, data isolation) because later content has lower adherence probability.

**Opus 4.7 failure mode — references without read-enforcement.** On Opus 4.6 and earlier, a CLAUDE.md line like `"See rules/data-isolation.md for restrictions"` would often cause the agent to read that file before proceeding. On Opus 4.7, the [Anthropic migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) confirms the model "will not infer requests you didn't make" — a reference is just a reference. If the read isn't explicitly demanded, it may not happen.

Remediation (any one is sufficient, listed by enforcement strength):

1. **PreToolUse hook** — block the risky operation until the referenced file is read. 100% enforcement. Appropriate for security boundaries.
2. **Explicit Read step in the instruction** — `"Before editing files in data/, Read rules/data-isolation.md first."` Names the tool, names the file, states the trigger.
3. **Required-reading block at the top of CLAUDE.md** — inline the content rather than referencing it, for constraints small enough to fit the instruction budget.

Advisory-style references remain fine for context (resource maps, conventions) — just not for constraints where bypass is unsafe. See [Model Migration Anti-Patterns](model-migration-anti-patterns.md) for the full inventory of 4.7 failure modes.

### 2. Rules Files (Path-Triggered)

Loaded when the agent works with files matching the rule's path pattern. Each rule file is narrow (500-700 bytes) and domain-specific:

| Repository | Rules Files | Examples |
|-----------|-------------|---------|
| third-brain | 5 | `corelight-analysis.md` (Zeek field names), `daily-notes.md` (date format), `inbox-processing.md` (weekly clearing) |
| mndr-review-automation | 4 | `data-isolation.md` (BLOCKED/SAFE file lists), `tests.md` (1,216 tests, mock patterns), `lib-conventions.md` (no proxy libraries) |
| health-inventory | 4 | `sensor-inventory.md` (CSV naming), `lib.md` (collector patterns, health scores), `config.md` (threshold behavior) |

**Design principle**: Rules enforce what CLAUDE.md describes. CLAUDE.md says "don't read customer data"; `data-isolation.md` specifies exactly which paths are blocked and which are safe. This separation keeps CLAUDE.md readable while providing enforcement detail when needed.

### 3. Commands (User-Invoked)

Loaded when the user invokes a slash command. Commands are procedural runbooks with checklists, preconditions, and step-by-step workflows:

| Repository | Commands | Examples |
|-----------|----------|---------|
| zeek-iceberg-demo | 4 | `/demo` (20-min demo flow), `/status` (Docker + data check), `/setup-minio`, `/reflections` |
| Splunk-db-connect-benchmark | 4 | `/validate` (5 health checks), `/status` (quick Docker check), `/benchmark` (30-min suite), `/cleanup` |
| network-visualization-services | 1 | `/activate-engagement` (customer engagement checklist) |

**Design principle**: Commands contain operational knowledge that doesn't belong in CLAUDE.md because it's only needed during specific workflows. A 92-line validation command loaded at invocation time is better than 92 lines permanently in CLAUDE.md.

### 4. Skills (Task-Triggered)

More complex than commands — skills can have their own tools, model preferences, and execution logic:

| Repository | Skills | Examples |
|-----------|--------|---------|
| claude-code-project-best-practices | 6 | `pattern-reviewer`, `sources-updater`, `emerging-pattern-monitor`, `index-regenerator` |
| network-visualization-services | 6 (personal) | `voice-consistency-enforcer`, `ultrathink-analyst`, `systematic-debugger` |

---

## When to Add Each Mechanism

| Signal | Action | Mechanism |
|--------|--------|-----------|
| Agent keeps asking "what is this project?" | Add project overview | CLAUDE.md Tier 1 |
| Agent keeps exploring filesystem to find files | Add resource map | CLAUDE.md Tier 2 |
| Agent violates the same convention repeatedly | Add domain rule | Rules file (path-targeted) |
| Agent handles sensitive data without guardrails | Add security boundaries + PreToolUse hook | CLAUDE.md Tier 3 + Hook |
| You need repeatable operational workflows | Add slash command | Commands file |
| You need complex automation with model preferences | Add skill | Skills directory |
| CLAUDE.md exceeds ~150 instructions | Move domain detail to rules/commands | Progressive disclosure refactor |

### The ~150 Instruction Budget

Boris Cherny's guidance (March 2026): Keep CLAUDE.md under ~150 instructions. Beyond this, adherence drops below the already-imperfect ~80% baseline.

**Practical test**: If you can't read your CLAUDE.md in under 2 minutes, it's too long. Move the excess into:

- **Rules** if it's path-specific convention enforcement
- **Commands** if it's procedural workflow
- **Skills** if it's complex automation
- **Companion docs** (ARCHITECTURE.md, DECISIONS.md) if it's reference material the agent can read on demand

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Everything in CLAUDE.md | File exceeds 200 lines; agent ignores later sections | Progressive disclosure: rules for conventions, commands for workflows |
| Security buried in middle | Agent reads data before encountering security boundaries | Front-load: "Security Boundaries — READ THIS FIRST" as first section |
| No CLAUDE.md at all | 10% co-authoring rate (tme-mcp-server) | Even Tier 1 (42 lines) dramatically improves agent effectiveness |
| Rules without CLAUDE.md context | Agent follows rules but doesn't understand project structure | Rules complement CLAUDE.md; they don't replace it |
| Commands for infrequent operations | Command bloat; commands never invoked | Only create commands for workflows used at least weekly |

---

## Sources

### Tier A (Direct Production Observation)

- 6-repository CLAUDE.md comparison (April 2026) — Line counts, section structures, tier classification across zeek-iceberg-demo, third-brain, mndr-review-automation, health-inventory, network-visualization-services, Splunk-db-connect-benchmark
- Rules directory analysis (April 2026) — 13 rules files across 3 repos, path-targeted domain enforcement
- Commands directory analysis (April 2026) — 9 commands across 3 repos, procedural runbooks

### Tier B (Validated / Expert Practitioner)

- Boris Cherny (March 2026) — ~150 instruction cap, CLAUDE.md as advisory (~80% adherence), hooks for enforcement
- Anthropic Claude Code best practices — Progressive disclosure recommendation

### Related Analysis

- [Behavioral Insights](./behavioral-insights.md) — ~80% CLAUDE.md adherence rate, 60% context degradation threshold, ~150 instruction cap
- [Agent-Driven Development](./agent-driven-development.md) — Infrastructure maturity model showing CLAUDE.md as foundation for all levels
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — Context budget framework and progressive disclosure for domain-heavy projects
- [Harness Engineering](./harness-engineering.md) — CLAUDE.md as part of the broader harness stack

---

*Last updated: April 2026*
