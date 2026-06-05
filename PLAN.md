# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: June 4, 2026 (first-party introspection registered; session-quality-tools.md → RETIRING via /insights; Dapr routing + count reconciliation)

---

## Current Focus

**Phase**: v2.1 — Production Evidence Integration
**Goal**: Maintain focused, evidence-based analysis that complements ECC and superpowers

---

## Current Status

| Metric | Status |
|--------|--------|
| Analysis documents | 41 |
| Archived v1 patterns | 24 |
| Source database entries | 141+ (Tier A sweep 2026-05-24 added: Meta-Harness arXiv:2603.28052, Pan et al./Tsinghua arXiv:2603.25723 — attribution corrected from "Tingua", Agentic Context Engineering arXiv:2510.04618 ICLR 2026, SWE-Bench Mobile arXiv:2602.09540, Memanto arXiv:2604.22085, LongMemEval-V2 arXiv:2605.12493, Teaching Claude why, agent-view/ultrareview/`/goal` Anthropic docs) |
| Source attribution | 100% (16 docs backfilled with `## Sources` footers on 2026-05-24) |

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Monitor Tier A sources for new insights | Low | Ongoing |
| Keep SOURCES.md current (biweekly) | Low | Ongoing |
| Update analysis docs when new evidence emerges | Medium | Ongoing |
| Opus 4.8 release re-validation (model-coupled docs) | Medium | **Done 2026-05-30** — 4.8 deltas, sycophancy nuance, injection regression §5.2, 60%-threshold revalidation, MRCR case study, soft-guideline anti-pattern, `model-version-4-8` routing. See model-migration-anti-patterns / behavioral-insights / safety-and-sandboxing / harness-engineering |
| Benchmark multi-needle long-context retrieval (MRCR-v2) on Opus 4.8 | Medium | Open — no public 4.8 MRCR transcription yet; "better long-context" 4.8 claim is directional (Tier A), not quantified |
| Revalidate 4.7-era claims on Opus 4.8 (side-by-side output diff) | Medium | Open — see [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) |
| CI regression tests for prompt anti-patterns (Vertrees proposal) | Medium | Deferred — out of scope until Anthropic publishes guidance |
| Monitor first-party feature convergence for retirement (replacement-readiness) | Low | **Ongoing** — obsolescence sweep 2026-06-04 registered `/insights`, `/usage`, `/doctor` (Tier A). `session-quality-tools.md` → RETIRING (defers to `/insights`). Watch list: MCP/skills economics ← `/usage` per-category; install-health ← `/doctor`. Tracked via `emerging-pattern-monitor` retirement lane + CONTRIBUTING § Retiring a doc |
| Obsolescence sweep + routing/count hygiene | Low | **Done 2026-06-04** — core (static evidence-tiered routing, model-migration detection, memory archetypes) has no first-party equivalent as of June 2026; only session-diagnostics commoditized (→ `/insights`). Wired previously-unreachable `dapr-durable-agents.md` into routing (`project-type-agent-infra`); reconciled stale doc counts (28/38 → 41) and backfilled 3 missing docs in the README Core Analysis table |

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

## Completed Work

Dated activity log for all completed work has moved to [ARCHIVE.md](ARCHIVE.md) — see "Detailed Activity Log" section.

## Next Review

**When**: Mid-June 2026 (next biweekly cadence, ~2 weeks from 2026-05-30)
**Focus**: Biweekly Tier A sweep (Anthropic Engineering Blog, Claude Code changelog, NIST/standards); benchmark MRCR-v2 multi-needle retrieval on Opus 4.8 to quantify the "better long-context" claim and check whether the 4.6→4.7 regression recovered; watch for a 4.7→4.8 migration guide expansion and any Petri 3.0 / injection-robustness follow-ups; revisit the unverified 2026-04-23 "claude-code-quality-reports" post if a working URL surfaces; track ICLR 2026 / ICML 2026 papers building on Agentic Context Engineering and Meta-Harness; watch for primary peer-reviewed publication of the four 2026 arXiv preprints now registered.
