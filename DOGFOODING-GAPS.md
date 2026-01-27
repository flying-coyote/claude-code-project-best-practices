# Dogfooding Gaps & Action Plan

**Last Audit**: 2026-01-27
**Next Audit**: 2026-04-27 (quarterly)

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

### ⚠️ SDD Tasks Phase Underused

**Problem**: `claude-tasks.json` exists but barely used. TodoWrite not actively employed during development.

**Evidence**: Tasks file has placeholder entries; most work done without formal task tracking.

**Impact**: Medium - doesn't affect documentation quality, but fails to demonstrate own methodology.

**Action Plan**:
1. Use TodoWrite for all multi-step tasks (this session demonstrated correct usage)
2. Update `claude-tasks.json` with real project milestones
3. Reference task tracking in session workflows

**Owner**: Ongoing practice
**Target**: Next audit (2026-04-27)

### ⚠️ Missing Patterns in CLAUDE.md Index

**Problem**: CLAUDE.md patterns list doesn't include recent additions (GSD, CAII, Johari, RLM, etc.)

**Evidence**: Patterns Directory section lists ~15 patterns; actual count is 31.

**Impact**: Low - INDEX.md is accurate; CLAUDE.md is a summary.

**Action Plan**:
1. Add "Cross-Phase" section entries for new orchestration patterns
2. Or simplify to "See INDEX.md for complete list"

**Owner**: Next CLAUDE.md update
**Target**: 2026-02-01

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

---

## Metrics

| Metric | 2026-01-27 | Target |
|--------|------------|--------|
| Skills implemented | 4 | 5+ |
| Hooks functional | 3/3 | 3/3 |
| Patterns with Evidence Tier | 100% | 100% |
| Recent Learnings freshness | 17 days | <14 days |
| INDEX.md accuracy | 100% | 100% |

---

*This document is part of the project's self-compliance practice. Update after each quarterly audit.*
