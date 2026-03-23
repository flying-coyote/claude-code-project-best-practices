# Plan

**Purpose**: Current priorities, immediate next actions, success metrics
**Last Updated**: March 23, 2026

---

## Current Focus

**Phase**: Post-v1.0 Maintenance + Pattern Expansion
**Goal**: Maintain documentation currency, address practical gaps

---

## Current Status

The repository is stable and production-ready. Key metrics achieved:

| Metric | Status |
|--------|--------|
| Patterns | 36 documented |
| Skills | 10 examples |
| Self-compliance | 88/100 (tracked in DOGFOODING-GAPS.md) |
| Source attribution | 100% |
| Total documents | 114 |

See [ARCHIVE.md](ARCHIVE.md) for completed milestones.

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Keep ARCHITECTURE.md current with directory structure | Low | 🔄 Ongoing |
| Monitor Anthropic Engineering Blog for new patterns | Low | 🔄 Weekly |
| Review community sources per cadence in SOURCES.md | Low | 🔄 Monthly |

### Medium Priority

| Item | Effort | Notes |
|------|--------|-------|
| Add troubleshooting/FAQ section | Medium | ✅ Done - TROUBLESHOOTING.md |
| Add "Which Entry Point?" decision table | Low | ✅ Done - Added to README.md |
| Add missing patterns to README | Low | ✅ Done - All 36 patterns in decision matrix + SDD tables |
| Create migration guide | Medium | ✅ Done - MIGRATION-GUIDE.md |
| Create pattern learning path | Medium | ✅ Done - PATTERN-LEARNING-PATH.md |
| Refresh example projects | Medium | ✅ Done - All 3 examples have 4-component setup |
| Add pattern quality checklist | Low | ✅ Done - PATTERN-QUALITY-CHECKLIST.md |

### Low Priority

| Item | Effort | Notes |
|------|--------|-------|
| Cross-project skill deployment docs | High | Gather use cases first |
| Consider MCP server for patterns | High | Needs design decisions |

---

## Backlog

Items to consider when capacity allows:

- [x] Troubleshooting guide for common setup issues (TROUBLESHOOTING.md)
- [x] Pattern quality checklist (PATTERN-QUALITY-CHECKLIST.md)
- [x] Refresh example projects to match current 36 patterns
- [ ] Document cross-project skill deployment (when use cases emerge)

---

## Deferred Items

These were evaluated and consciously deferred (see [ARCHIVE.md](ARCHIVE.md)):

| Item | Reason |
|------|--------|
| MCP server for pattern lookup | Prerequisites: transport protocol, operations, hosting |
| Video walkthrough | Out of scope (requires external infrastructure) |
| Fabric integration guide | Low priority (Tier C source) |

---

## Open Questions

| Question | Context |
|----------|---------|
| What should "pattern validation" mean? | Options: Markdown linting, link checking, human review checklist, or automated tests |
| What use cases exist for cross-project sync? | Need community feedback before designing |

---

## Review Cadence

| Source Type | Frequency | Next Review | Automation |
|-------------|-----------|-------------|------------|
| Anthropic Engineering Blog | Weekly | Ongoing | ✅ anthropic-blog-rss.yml (6-hourly) |
| awesome-claude-code lists | Monthly | Mar 2026 | ⏸️ Manual |
| SDD frameworks (Spec Kit, BMAD) | Quarterly | Apr 2026 | ⏸️ Manual |
| Tools/Plugins/MCP landscape | Daily | Ongoing | ✅ tools-evolution-tracker.yml |

**Automation Status** (as of Feb 2026):
- **Anthropic blog monitoring**: Automated via `.github/workflows/anthropic-blog-rss.yml` (runs every 6 hours)
- **Tools tracking**: Automated via `.github/workflows/tools-evolution-tracker.yml` (runs daily at 6am UTC)
- **Manual reviews**: Focus shifted from information gathering to editorial decisions
- **Issue creation**: Automation creates GitHub issues for human approval; no auto-commits to patterns

---

## Next Review

**When**: April 2026
**Focus**: Verify quality improvements, check for new Anthropic patterns, community feedback
