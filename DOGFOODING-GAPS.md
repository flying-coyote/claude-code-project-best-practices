# Dogfooding Gaps & Action Plan

**Last Audit**: 2026-02-08
**Next Audit**: 2026-05-08 (quarterly)

This document tracks gaps between what this project documents and what it implements. Dogfooding builds credibility.

---

## Compliance Summary

| Category | Score | Status |
|----------|-------|--------|
| **Hooks** | 3/3 | ✅ Complete |
| **Memory Architecture** | 4/4 | ✅ Complete |
| **Context Engineering** | 4/4 | ✅ Complete |
| **Documentation Standards** | 5/5 | ✅ Complete |
| **Skills Framework** | 4/5 | ✅ Improved (was 1/5) |
| **SDD 4-Phase Model** | 3/4 | ⚠️ Tasks phase underused |
| **MCP Integration** | 0/2 | ⏸️ Deferred (intentional) |

---

## Resolved Gaps (2026-01-27)

### ✅ Skills Framework (1/5 → 4/5)

**Problem**: Only `pattern-reviewer` skill existed despite documenting progressive disclosure and skill architecture.

**Resolution**: Added 3 project-specific skills:
- `johari-clarifier` - SAAE protocol from johari-window-ambiguity.md
- `sources-updater` - Evidence tier enforcement from evidence-tiers.md
- `index-regenerator` - Documentation maintenance automation

**Commit**: `43479e8`

### ✅ PostToolUse Hook Formatting

**Problem**: Audit noted formatting wasn't working.

**Resolution**: Formatting was already implemented in `post-tool-use.sh` (lines 16-49). Issue was missing formatters on dev machine, not missing implementation.

**Action**: Install formatters as needed: `npm install -g prettier`, `pip install black`, etc.

### ⏸️ MCP Server Spec (Deferred)

**Problem**: 593-line specification with zero implementation.

**Decision**: Defer indefinitely. Rationale:
1. **Skills are cheaper**: Per `mcp-vs-skills-economics.md`, skills approach is 50% cheaper
2. **Scope mismatch**: MCP best for execution; this project needs knowledge management (skills domain)
3. **Effort vs benefit**: 4-6 week implementation for a documentation project
4. **Manual workflow sufficient**: Current pattern extraction via skills works fine

**Status**: Spec retained in `.claude/mcp-server-spec.md` with DEFERRED status for future reference.

---

## Open Gaps

### ✅ Anthropic Guidance Alignment (Resolved 2026-01-31)

**Problem**: Some patterns recommended complexity exceeding official Anthropic guidance.

**Evidence Found**:
- Skill examples averaged 320 lines vs Anthropic's ~60 line recommendation
- SKILL-TEMPLATE.md was 250+ lines (template larger than recommended skill)
- Progressive disclosure pattern encouraged elaborate 3-tier structures
- Project infrastructure recommended obsolete `/commit-push-pr` pattern

**Actions Completed**:
1. ✅ Trimmed project CLAUDE.md from 121 to 28 lines (77% reduction)
2. ✅ Trimmed project skills from 904 to 232 lines (74% reduction)
3. ✅ Deleted redundant slash commands (commit-push-pr, update-status, end-session)
4. ✅ Set up markdown linting verification loop (`npm run lint`)
5. ✅ Added canonical URL `code.claude.com/docs` to SOURCES.md as Tier A
6. ✅ Added warning to progressive-disclosure.md about Anthropic guidance
7. ✅ Updated project-infrastructure.md to remove obsolete Tier 3 advice
8. ✅ Added minimal ~60 line template option to SKILL-TEMPLATE.md

**Source**: [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)

---

### ⚠️ SDD Tasks Phase Underused

**Problem**: `claude-tasks.json` exists but barely used. TodoWrite not actively employed during development.

**Evidence**: Tasks file has placeholder entries; most work done without formal task tracking.

**Impact**: Medium - doesn't affect documentation quality, but fails to demonstrate own methodology.

**Action Plan**:
1. Use TodoWrite for all multi-step tasks (this session demonstrated correct usage)
2. Update `claude-tasks.json` with real project milestones
3. Reference task tracking in session workflows

**Owner**: Ongoing practice
**Target**: Next audit (2026-05-08)

### ⚠️ Missing Patterns in CLAUDE.md Index

**Problem**: CLAUDE.md patterns list doesn't include recent additions (GSD, CAII, Johari, RLM, etc.)

**Evidence**: Patterns Directory section lists ~15 patterns; actual count is 31.

**Impact**: Low - INDEX.md is accurate; CLAUDE.md is a summary.

**Action Plan**:
1. Add "Cross-Phase" section entries for new orchestration patterns
2. Or simplify to "See INDEX.md for complete list"

**Owner**: Next CLAUDE.md update
**Target**: 2026-02-08 (addressed by INDEX.md auto-generation)

---

## Deferred Items (Not Gaps)

### MCP Server Implementation

**Status**: Intentionally deferred
**Rationale**: See "Resolved Gaps" section above
**Revisit When**:
- Skills approach proves insufficient for pattern monitoring
- MCP tooling matures for knowledge management use cases
- Implementation effort justified by new requirements

### PreToolUse Security Hook

**Status**: Not implemented (documented as optional)
**Rationale**:
- Security gates not critical for documentation project
- Permission gates in settings.json provide sufficient control
**Revisit When**: Project handles sensitive data or external integrations

---

## Audit Checklist (Quarterly)

Run this checklist every quarter:

### Infrastructure
- [ ] All 3 hook types present and functional (SessionStart, PostToolUse, Stop)
- [ ] Skills directory has 3+ project-specific skills
- [ ] settings.json uses current schema (permissions.allow)
- [ ] Formatters installed and working (prettier, black, etc.)

### Documentation
- [ ] CLAUDE.md < 150 lines (progressive disclosure)
- [ ] Recent Learnings updated in last 2 weeks
- [ ] INDEX.md matches actual file count
- [ ] SOURCES.md has entries for all pattern sources

### Methodology
- [ ] TodoWrite used for multi-step tasks
- [ ] Atomic commits (one task = one commit)
- [ ] New patterns have cross-references updated

### Quality
- [ ] No broken links in patterns/
- [ ] All patterns have Evidence Tier labels
- [ ] Anti-Patterns sections present and complete

### Rapid Evolution Tracking (Quarterly)
- [ ] Review all EMERGING patterns for promotion eligibility (use `emerging-pattern-monitor` skill)
- [ ] Verify no measurement claims past expiry date without re-validation
- [ ] Check DEPRECATIONS.md for patterns ready to archive (90 days past grace period)
- [ ] Audit version-requirements in patterns vs current Claude Code version
- [ ] Review automation-generated issues from last quarter (GitHub Issues with `automation` label)
- [ ] Update SOURCES.md with any missed Anthropic blog posts (check anthropic.com/engineering)
- [ ] Verify TOOLS-TRACKER.md accuracy against manual spot-check (5 random patterns)
- [ ] Check automation workflows running successfully (last 5 runs in GitHub Actions)
- [ ] Validate RSS cache is current (.cache/anthropic-rss.json exists and updated)
- [ ] Review promotion proposals created by automation (accept/reject with rationale)

---

## Metrics

| Metric | 2026-01-27 | 2026-02-08 | Target |
|--------|------------|------------|--------|
| Skills implemented | 4 | 4 | 5+ |
| Hooks functional | 3/3 | 3/3 | 3/3 |
| Patterns with Evidence Tier | 100% | 100% | 100% |
| Pattern count | 31 | 33 | — |
| SOURCES.md entries (Tier A blog posts) | 8 | 16 | — |
| Recent Learnings freshness | 17 days | 0 days | <14 days |
| INDEX.md accuracy | 100% | Pending regen | 100% |

---

*This document is part of the project's self-compliance practice. Update after each quarterly audit.*
