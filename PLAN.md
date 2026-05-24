# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: May 24, 2026

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

## Completed Work

Dated activity log for all completed work has moved to [ARCHIVE.md](ARCHIVE.md) — see "Detailed Activity Log" section.

## Next Review

**When**: Mid-June 2026 (next biweekly cadence, ~3 weeks from 2026-05-24)
**Focus**: Biweekly Tier A sweep (Anthropic Engineering Blog, Claude Code changelog, NIST/standards); revisit the unverified 2026-04-23 "claude-code-quality-reports" post if a working URL surfaces; track ICLR 2026 / ICML 2026 papers building on Agentic Context Engineering and Meta-Harness; watch for primary peer-reviewed publication of the four 2026 arXiv preprints now registered.
