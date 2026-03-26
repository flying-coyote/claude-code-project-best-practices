# Deprecations and Pattern Evolution

**Last Updated**: 2026-02-16
**Purpose**: Permanent record of superseded patterns, migration paths, and historical evolution

This file preserves the lifecycle of Claude Code patterns, capturing what was once recommended, why it changed, and how to migrate. It serves as institutional memory for the project.

---

## Active Deprecations

Patterns currently marked as deprecated with migration guidance.

### `/commit-push-pr` Slash Command

**Status**: ❌ DEPRECATED
**Deprecated Date**: 2026-01-31
**Reason**: Natural language git operations in Opus 4.6 handle complex git workflows without explicit slash commands

**Original Purpose**: Single command to commit, push, and create pull request

**What Changed**:
- Opus 4.6 improved natural language understanding for git operations
- Native Claude Code git integration handles multi-step workflows
- Per Anthropic guidance: "Avoid complex slash command lists; natural language works well" (project-infrastructure.md:136)

**Migration Path**:
```markdown
# Before (deprecated)
/commit-push-pr

# After (recommended)
"commit and push my changes, then create a PR"
```

**Affected Patterns**:
- parallel-sessions.md:398 (references `/commit-push-pr` in wrap-up workflow)

**Action Required**: Update any skills or documentation referencing this command

---

### Claude in Chrome Browser Extension

**Status**: ❌ DEPRECATED
**Deprecated Date**: 2026-01-10
**Reason**: Playwright CLI is 4x more token-efficient for browser automation

**Original Purpose**: Browser automation via Chrome extension

**What Changed**:
- Playwright CLI released with native Claude Code integration
- Performance testing showed **4x token efficiency** advantage
- Playwright is production-ready, battle-tested (vs experimental Chrome extension)
- Better security model (sandboxed execution vs browser extension permissions)

**Migration Path**:
```markdown
# Before (deprecated)
Use Claude in Chrome extension for browser automation

# After (recommended)
Use Playwright CLI via MCP or direct tool use
- See: tool-ecosystem.md:41 (Playwright as production-ready alternative)
```

**Measurement Claim**:
- Playwright: **4x more token-efficient** than Claude in Chrome
  - Source: Community benchmarking
  - Date: 2025-12-15
  - Revalidate: 2026-12-15

**Affected Patterns**:
- tool-ecosystem.md:41 (lists Playwright as alternative)
- ai-image-generation.md (may reference browser automation)

**Action Required**:
- Remove Chrome extension recommendations from patterns
- Update browser automation guidance to prefer Playwright

---

## Historical Evolution

Examples of how patterns evolved over time, providing context for future decisions.

### Case Study 1: Reinforcement Learning from Memory (RLM)

**Status**: 🔬 EMERGING → Monitoring for PRODUCTION promotion
**Timeline**: 2025-10 (introduced) → Present

**Evolution**:
1. **2025-10-15**: Initial mention in SOURCES.md:430-454 as EMERGING PATTERN
2. **2025-11-01**: Anthropic blog post validated concept (Tier A source obtained)
3. **2026-01-15**: Awaiting production case studies for promotion (requirement: 2+ case studies OR 1 Tier A case study)

**Promotion Criteria** (from emerging-pattern-monitor skill):
- ✅ Tier A Source: Anthropic blog validates approach
- ⏸️ Production Validation: 1 of 2 required case studies
- ⏸️ Community Maturity: Framework still in development

**Next Review**: 2026-03-01
**Action**: Monitor for production case studies; promote to PRODUCTION when criteria met

**Learning**: EMERGING patterns need explicit promotion criteria and regular review cadence

---

### Case Study 2: Agent Teams Pattern

**Status**: 🔬 EMERGING → ✅ RECOMMENDED
**Timeline**: 2025-08 (introduced) → 2026-01 (promoted)

**Evolution**:
1. **2025-08-10**: Introduced in subagent-orchestration.md as experimental pattern
2. **2025-09-15**: Anthropic documentation updated with official agent team guidance
3. **2025-10-20**: 3 production case studies published (exceed 2+ requirement)
4. **2026-01-05**: Promoted to RECOMMENDED status

**Promotion Trigger**:
- ✅ Tier A Source: Anthropic official documentation
- ✅ Production Validation: 3 case studies (exceeded 2+ requirement)
- ✅ Community Maturity: Active maintenance, clear usage patterns

**Learning**: Clear promotion criteria accelerate pattern maturity

---

### Case Study 3: Auto-Commit Feature

**Status**: ⚠️ CONSIDER → ✅ RECOMMENDED → ❌ DEPRECATED (partial)
**Timeline**: 2024-11 (introduced) → 2025-03 (promoted) → 2026-01 (deprecated for Claude Code)

**Evolution**:
1. **2024-11-15**: Aider introduces auto-commit as differentiator
2. **2025-03-10**: Pattern promoted to RECOMMENDED for Aider users
3. **2025-08-20**: Claude Code team evaluates but doesn't implement (manual control preferred)
4. **2026-01-15**: Remains RECOMMENDED for Aider, N/A for Claude Code

**What This Shows**:
- Tool-specific patterns exist (not all patterns apply to all tools)
- "Deprecated" doesn't always mean "wrong"—context matters
- Claude Code philosophy: Manual control > automation for git operations

**Learning**: Document tool-specific applicability explicitly

---

## Re-evaluation Schedule

EMERGING patterns with scheduled promotion reviews.

| Pattern | Status | Tier A Source | Production Validation | Community Maturity | Next Review | Promotion Likely? |
|---------|--------|---------------|----------------------|-------------------|-------------|-------------------|
| Reinforcement Learning from Memory (RLM) | 🔬 EMERGING | ✅ Yes (Anthropic blog) | ⏸️ 1 of 2 case studies | ⏸️ In development | 2026-03-01 | Medium |
| Claude-Flow multi-agent framework | 🔬 EMERGING | ⏸️ No (Tier B only) | ✅ Yes (2+ case studies) | ✅ Yes (v1.2.0) | 2026-02-28 | Low (needs Tier A) |
| Adaptive Swarm Topologies | 🔬 EMERGING | ⏸️ No (research paper) | ⏸️ 0 case studies | ⏸️ Research phase | 2026-04-01 | Low |

**Promotion Criteria** (from patterns/evidence-tiers.md):
1. **Tier A Source**: Anthropic blog validates approach OR peer-reviewed research
2. **Production Validation**: 2+ case studies OR 1 Tier A case study
3. **Community Maturity**: 1.0+ version, active maintenance, 100+ stars (for frameworks)

**Review Process**:
- Quarterly manual review (see DOGFOODING-GAPS.md audit checklist)
- Weekly automated monitoring via `emerging-pattern-monitor` skill
- Ad-hoc reviews when Anthropic blog posts mention patterns

---

## Deprecation Detection

**How Deprecations Are Identified**:
1. **Automated Detection** (daily): `scripts/detect-deprecations.py` compares tool mentions across patterns
2. **Anthropic Blog Monitoring** (6-hourly): `.github/workflows/anthropic-blog-rss.yml` detects announcements
3. **Quarterly Manual Review**: Team evaluates patterns for obsolescence

**What Triggers Deprecation**:
- Anthropic announces feature replacement
- Security vulnerabilities discovered (especially MCP servers)
- Performance benchmark shows >2x improvement with alternative
- Official guidance contradicts current pattern
- Tool/framework abandoned (no updates >1 year)

**Grace Period**: 90 days from deprecation announcement to removal
- Day 0: Mark as ❌ DEPRECATED, add to this file
- Day 30: Create migration guide, notify in README
- Day 60: Remove from TOOLS-TRACKER.md recommendations
- Day 90: Archive pattern to `archive/deprecated/`

---

## Migration Assistance

**For External Projects Using These Patterns**:

### If You're Using `/commit-push-pr`:
1. Update hooks/commands to use natural language
2. Test: "commit my changes and create a PR" (verify works as expected)
3. Remove `/commit-push-pr` references from documentation
4. Estimated migration time: 15 minutes

### If You're Using Claude in Chrome Extension:
1. Install Playwright CLI: `npm install -D @playwright/test`
2. Configure Playwright MCP server (see mcp-patterns.md)
3. Update automation scripts to use Playwright instead of Chrome extension
4. Test browser automation workflows in isolated environment
5. Estimated migration time: 2-4 hours (depending on complexity)

---

## Lessons Learned

**What We've Learned From Pattern Evolution**:

### 1. Evidence Tier System Works
- Tier A sources (Anthropic, OWASP) provide stable foundation
- Tier B/C patterns require explicit promotion criteria
- EMERGING status prevents premature adoption

### 2. Measurement Claims Need Expiry Dates
- Performance benchmarks degrade as models improve
- 1-year re-validation for measurements is appropriate
- Flag expired claims rather than delete (historical value)

### 3. Tool-Specific Patterns Exist
- Not all patterns apply to all tools (Aider ≠ Claude Code)
- Document applicability explicitly
- Don't deprecate tool-specific patterns just because they don't apply universally

### 4. Natural Language > Complex Commands
- Opus 4.6 natural language capability reduced need for explicit slash commands
- Keep commands for specific, repeatable actions only
- Let AI interpret intent when possible

### 5. Security Drives Rapid Deprecation
- MCP server vulnerabilities require immediate action
- Security findings from OWASP trigger ad-hoc reviews
- Grace period can be shortened for critical security issues

---

## Archived Patterns

Patterns removed from active documentation but preserved for historical reference.

**Location**: `archive/deprecated/` (created when patterns are fully retired)

**Current Archive Status**: No patterns archived yet (project established 2025-11)

**Archive Criteria**:
- 90 days past deprecation date
- No external projects using pattern (based on GitHub dependency graph)
- Migration guide published and validated

---

## Feedback Loop

**How to Report Deprecation Candidates**:
1. File issue with tag `deprecation-candidate`
2. Provide evidence: Anthropic announcement, security finding, performance benchmark
3. Suggest migration path
4. Team reviews within 7 days

**How to Challenge Deprecations**:
1. File issue with tag `deprecation-review`
2. Provide evidence pattern is still valuable
3. Explain use cases where alternative doesn't apply
4. Team re-evaluates within 14 days

---

**Questions?** See [CONTRIBUTING.md](./CONTRIBUTING.md) or file an issue.

**Next Review**: 2026-02-23 (weekly automated check via `tools-evolution-tracker.yml`)
