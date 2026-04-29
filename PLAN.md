# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: April 28, 2026

---

## Current Focus

**Phase**: v2.1 — Production Evidence Integration
**Goal**: Maintain focused, evidence-based analysis that complements ECC and superpowers

---

## Current Status

| Metric | Status |
|--------|--------|
| Analysis documents | 38 |
| Archived v1 patterns | 24 |
| Source database entries | 85+ |
| Source attribution | 100% |

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Monitor Tier A sources for new insights | Low | Ongoing |
| Keep SOURCES.md current (biweekly) | Low | Ongoing |
| Update analysis docs when new evidence emerges | Medium | Ongoing |
| Revalidate 4.6-era claims on Opus 4.7 (side-by-side output diff) | Medium | Open — see [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) |
| CI regression tests for prompt anti-patterns (Vertrees proposal) | Medium | Deferred — out of scope until Anthropic publishes guidance |

### Medium Priority

| Item | Effort | Notes |
|------|--------|-------|
| Update internal cross-references in analysis/ docs | Low | Completed April 2026 |
| Review CONTRIBUTING.md for v2.1 alignment | Low | Completed April 2026 |

### Low Priority

| Item | Effort | Notes |
|------|--------|-------|
| Consider consolidated "key findings" summary page | Medium | Single-page executive summary |

---

## Review Cadence

| Source Type | Frequency | Automation |
|-------------|-----------|------------|
| Anthropic Engineering Blog | Weekly | anthropic-blog-rss.yml |
| Boris Cherny interviews/posts | Monthly | Manual |
| Nate B. Jones publications | Monthly | Manual |
| IndyDevDan repos/content | Monthly | Manual |
| ECC major releases | Monthly | Manual |

---

## Recent Activity

### April 22, 2026 — One-Prompt Realignment: Routing-Based Advisory Fetch (complete)
- Added `AUDIT-CONTEXT.md`: routing map from observed project signals (CLAUDE.md state, harness layout, commit patterns, session diagnostics, model version, project type) to the specific analysis docs that apply. Typical audit now fetches 4–8 docs, not 28, and not the source index alone.
- Rewrote `ONE-LINE-PROMPT.md` as a 4-step flow (collect signals → fetch routing map → conditionally fetch advisories → produce audit). Every recommendation in the structured output must cite the analysis doc and its evidence tier.
- Updated README Quick Start with the new prompt and the "4–8 of 28 docs" framing.
- Added Anthropic Opus 4.7 migration guide (#27, Authority 5), Willison counter-signal (#28, Authority 3), Vertrees operationalization (#29, Authority 2 with Karen note) to `SOURCES-QUICK-REFERENCE.md`. Count bumped 26 → 29.
- Design rationale: prior prompt was blind to applicability (library projects got federated-query advice because the source was high-authority), blind to model version (no 4.7 migration signal), and lacked audit trail (recommendations did not carry doc+tier citations). Routing via `AUDIT-CONTEXT.md` fixes all three.

### April 28, 2026 — Memory & knowledge stack archetype split + Pass-2 testbed (complete)

- Split `analysis/memory-systems-archetype-recommendations.md` into 7 per-archetype docs (`memory-systems-archetype-{a..g}-*.md`) following the project's one-pattern-per-file convention
- Added `analysis/memory-systems-recommendation-methodology.md` with the 200/500/6k scale-band math, 8 challengeable assumptions, and applied corrections
- Added `analysis/memory-systems-graphify-vs-understand-anything.md` — direct A/B comparison after running both LLM-driven graph builders on this repo as testbed
- Empirical findings folded back into the recommendations:
  - Graphify Pass 1 (Tree-sitter) indexed 0 of 38 prose docs; Pass 2 (LLM extraction) produced 1187 nodes / 1651 edges / 67 communities / 88% EXTRACTED but with a measured ~25% hallucination rate on EXTRACTED edges (n=8 spot-check)
  - Lum1104 `/understand-knowledge` skill gates on lowercase `index.md` + `raw/` + `log.md` Karpathy layout — falls back to `/understand-anything:understand` for repos that don't match
- Wired up the audit's signal vocabulary: added `md-corpus-{small,design-target,large,very-large}`, `vault-obsidian`, `vault-karpathy`, `corpus-sensitive` to `AUDIT-CONTEXT.md`. Without these, the new archetype docs were unreachable from the audit
- Added helper scripts as documented patterns for downstream consumers: `scripts/graphify_footer_inject.py` (file-level edge aggregation, schema-tolerant), `scripts/graphify_contradiction_lint.py`
- Doc count: 28 → 38; SOURCES.md changelog updated

### April 22, 2026 — Opus 4.7 Migration Integration (complete)
- Added `analysis/model-migration-anti-patterns.md`: cross-version anti-pattern matrix (4.5 → 4.6 → 4.7), six Vertrees anti-patterns mapped to Anthropic migration guide, documented MUST-vs-positive-examples tension
- Updated `behavioral-insights.md`: prompt sensitivity table across model versions; Willison and HN counter-signals
- Updated `harness-engineering.md`: 4.7 counter-signal — harness simplifies while prompts need more explicit wording
- Updated `claude-md-progressive-disclosure.md`: references-without-read-enforcement is a 4.7 failure mode; enforcement options (PreToolUse hook, explicit Read, required-reading block)
- Updated `agent-evaluation.md` + `agent-principles.md`: implicit subagent dispatch anti-pattern, single-model eval baselines
- Updated `evidence-based-revalidation.md`: 4.6 → 4.7 as canonical revalidation trigger case study
- Updated SOURCES.md: registered Anthropic migration guide, What's New 4.7, Best Practices 4.7 blog (Tier A); Vertrees, Willison (Tier B); HN 47793411/47814832 (Tier C)
- Internal consistency fixes: added evidence-tier declaration to `evidence-tiers.md` meta-doc; updated `evidence-tiers.md` pedagogical examples to reference 4.7 shift; added explicit "Gap:" statements to `session-quality-tools.md`
- Bumped doc count 27 → 28 across README, PLAN, CLAUDE.md

### April 2026 Review (complete)
- Added production-scale agent-driven development evidence to `analysis/harness-engineering.md`:
  - Nick Schrock (Dagster): 1,000+ PRs merged in 3 weeks with Claude Code
  - Matthias Vallentin (Tenzir): 3x development velocity claim
- Updated SOURCES.md with Schrock and Vallentin agent-driven development entries
- Cross-referenced from third-brain concept imports (agent-driven-development-patterns)
- Added `analysis/agent-driven-development.md`: Agent-driven development patterns with quantified evidence from 7 production repos (infrastructure maturity model, cross-repo coordination, security boundaries, velocity data)
- Updated cross-references in 5 existing analysis docs
- Updated SOURCES.md with 7-repo portfolio analysis evidence (Tier A)
- Added 9 additional analysis documents covering all 10 identified gaps:
  - `local-cloud-llm-orchestration.md`: Hybrid MLX+Claude architecture from mndr-review-automation
  - `mcp-client-integration.md`: MCP client patterns from InspectorClient + TmePlaybookClient
  - `federated-query-architecture.md`: 15/15 benchmarks, 86-99% cost savings, TCO calculator
  - `automated-config-assessment.md`: Baseline-deviation-remediation, 3,816+ sensors, 100% detection
  - `claude-md-progressive-disclosure.md`: 3-tier CLAUDE.md evolution across 6 repos
  - `memory-system-patterns.md`: Auto-memory sizing by project type across 5 projects
  - `evidence-based-revalidation.md`: Hypothesis confidence tracking and demo prep
  - `security-data-pipeline.md`: Zeek → OCSF → Parquet → Iceberg pipeline case study
  - `cross-project-synchronization.md`: Dependency cascading across 7 repos
- Synced SOURCES.md: added Internal Methodology section for 3 meta-framework docs (behavioral-insights, confidence-scoring, evidence-tiers)
- Fixed stale line count references in SOURCES.md and SOURCES-QUICK-REFERENCE.md (1,278 → 1,579)
- Committed auto-regenerated INDEX.md (115 → 123 documents, added templates section)

---

## Next Review

**When**: May 2026
**Focus**: Complete April review cycle, monitor for new Tier A sources, check SDD framework updates (quarterly)
