---
convergence: single-source
---

# Architecture

**Purpose**: System design, directory structure, and current phase status
**Last Updated**: July 16, 2026 (absorption wave: de-snapshotted per Decision 9 — file inventories defer to INDEX.md, ecosystem positioning defers to README § Where This Sits)

---

## Project Purpose

This repository provides an **evidence-based analytical layer** for Claude Code. It evaluates claims, compares approaches, and surfaces quantified behavioral insights — the "Consumer Reports" for Claude Code tooling.

The audit engine has two passes that work together. The **INSPECT** pass is the presence/absence and count routing in `AUDIT-CONTEXT.md` — it asks what a project *has* and fetches the docs that match those signals, so it is strong at finding missing conventions and blind to whether the conventions a project already has still serve their purpose. The **RETHINK** pass is the intent-alignment layer that closes that blind spot: for each central mechanism the project already has, it asks what the mechanism is *for* and checks it against that stated intent, which is what catches intent-mechanism drift (a glob still pointing at a moved directory, a doc count the structure has outgrown, a write permission nobody decided to keep). RETHINK is first-class in the engine, not a follow-on, because this repo's own self-audit found that exact drift in itself; the per-mechanism intent checks live in [`analysis/intent-alignment-audit.md`](analysis/intent-alignment-audit.md) alongside the routing map in `AUDIT-CONTEXT.md`.

**What we are**:

- Evidence assessor (A-D tier system for claims + the HIGH/MEDIUM/LOW confidence framework, merged 2026-07-16)
- Comparative analyst (tools, frameworks, approaches)
- Behavioral insight aggregator (quantified observations from expert practitioners)
- Intent-alignment auditor (RETHINK: each mechanism checked against its stated *why*, not only its presence)

**What we are NOT**: the other six lanes of the ecosystem — first-party baseline, tooling ([ECC](https://github.com/affaan-m/everything-claude-code)), methodology ([superpowers](https://github.com/obra/superpowers)), mechanics documentation, standards, and thought-leader canons. The full lanes table with our relationship to each is README § Where This Sits; the per-doc ledger of who absorbs what is [ABSORPTION-MAP.md](ABSORPTION-MAP.md).

---

## Current Phase

**Phase**: v2.1 — the evidence-graded-audit lane
**Status**: Active

**Milestones**:

- v1.0: Initial patterns from Anthropic (Nov 2025)
- v1.1-v1.4: Pattern expansion to 36 patterns (Nov 2025 - Mar 2026)
- v2.0: Repositioned as analytical layer; 36 patterns → 14 analysis documents (Mar 2026)
- v2.1: Expanded to 26 docs with 7-repo portfolio evidence (Apr 2026); grew to 44 files, then the 2026-07-10 reduction collapsed to delta vs first-party (44→27, Decision 11); the 2026-07-16 absorption wave ran the first third-party sweep (27→25 files, Decision 12: absorption map + follow lane + one retirement + two merges)

---

## Directory Structure

Top-level layout only — the per-file inventory is auto-generated in [INDEX.md](INDEX.md) and was repeatedly stale here when hand-maintained (the 2026-06 self-audit caught this file frozen at an April snapshot, which is why the tree now defers).

```text
claude-code-project-best-practices/
├── .claude/          # Meta-project infrastructure (CLAUDE.md, settings, hooks, skills, commands)
├── analysis/         # Core content — routable analysis docs + CANONICAL-DOC-TEMPLATE.md (count: see INDEX.md)
├── archive/          # Prior v1 content + retired/merged doc snapshots (tombstone banners point at successors)
├── automation/       # Scripts (generate_index.py)
├── drafts/           # Scan artifacts (REDUCTION-PROPOSAL, ABSORPTION-SCAN)
├── research/         # Research inputs (self-audit-2026-06/)
├── ABSORPTION-MAP.md # Per-doc external-absorber ledger (derived; frontmatter canonical)
├── AUDIT-CONTEXT.md  # Signal → advisory routing map (fetched by the audit prompt + sibling /fleet-audit)
├── DECISIONS.md      # Design rationale
├── INDEX.md          # Auto-generated inventory (canonical file listing)
├── PLAN.md           # Current priorities
├── README.md         # Project overview + Where This Sits (canonical positioning)
├── SOURCES.md        # Comprehensive source database
└── SOURCES-QUICK-REFERENCE.md # Authority-weighted top sources
```

---

## Ecosystem Position

Canonical statement: README § Where This Sits (seven lanes; this repo is the evidence-graded-audit lane, sole occupant, temporary by charter). The unique-value list previously duplicated here is carried by README's "What You Get" table and the ABSORPTION-MAP's `none found` rows — the docs whose delta no external lane publishes (portfolio measurements, the RETHINK instrument, the evidence-grading system itself).

---

## Key Design Decisions

### 1. Analysis Over Implementation

We evaluate and compare rather than providing implementation guides. This keeps the project maintainable and avoids duplication.

### 2. Evidence-Based Claims

All claims must include source, evidence tier, and date. Measurements require revalidation dates (`scripts/check-measurement-expiry.py`).

### 3. Narrow Focus, Shrinking by Design

Depth over breadth, and the corpus is designed to shrink: collapse-to-delta against first-party coverage (Decision 11), follow/retire lanes against third-party coverage (Decision 12). Shrinking coverage is success, not decay (CONTRIBUTING § Retiring a Doc).

---

## Maintenance

| Document | Update Trigger | Frequency |
|----------|---------------|-----------|
| analysis/ docs | New source material from Tier A/B sources | Monthly |
| SOURCES.md | New publications from tracked sources | Biweekly |
| ABSORPTION-MAP.md | Absorption sweeps (judgment) + weekly-review 5b (consistency) | Quarterly / weekly |
| ARCHITECTURE.md | Structure changes | As needed |
| INDEX.md | File changes | Automated |

See [PLAN.md](PLAN.md) for current priorities.
