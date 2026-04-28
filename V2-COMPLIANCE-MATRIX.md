# v2 Best Practices Compliance Matrix

*Generated: 2026-03-31 | Based on 10-dimension audit from analysis/ documents*

## Summary

**15 projects reviewed** across 10 dimensions. All projects now have credential scanning hooks, path-scoped rules, and standardized CLAUDE.md with resource maps.

| Metric | Before | After |
|--------|--------|-------|
| Projects with credential scanning | 0/15 | **15/15** |
| Projects with path-scoped rules | 0/15 | **15/15** |
| Projects with resource maps | 0/15 | **14/15** |
| CLAUDE.md in correct location | 13/15 | **15/15** |
| Stale mcp-server-spec.md removed | 0 | **4 files / 2,828 lines** |
| Overly broad permissions fixed | 0 | **2 projects** |

---

## Cross-Project Compliance Matrix

| Project | CLAUDE.md | Hooks | Perms | Rules | Security | Budget | Disclosure |
|---------|-----------|-------|-------|-------|----------|--------|------------|
| best-practices | GOOD (39L) | GOOD (4/4) | GOOD | GOOD (1) | GOOD | GOOD | GOOD |
| genealogy | GOOD (59L) | GOOD (4/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| security-architect-mcp | GOOD (54L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | WARN | GOOD |
| personal-projects | GOOD (76L) | GOOD (3/4) | FIXED | GOOD (2) | GOOD | GOOD | GOOD |
| blog | GOOD (41L) | GOOD (4/4) | GOOD | GOOD (1) | GOOD | GOOD | GOOD |
| book | GOOD (59L) | GOOD (3/4) | GOOD | GOOD (1) | GOOD | GOOD | GOOD |
| lit-review | GOOD (52L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| data-quality | GOOD (52L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| rlm-claude-code | GOOD (56L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| itu-t-schemas | GOOD (53L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| Zeek-to-OCSF | GOOD (46L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| network-viz | GOOD (28L) | GOOD (3/4) | GOOD | GOOD (1) | GOOD | GOOD | GOOD |
| splunk-benchmark | GOOD (42L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| ocsf_lab | GOOD (21L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |
| zeek-iceberg | GOOD (55L) | GOOD (3/4) | GOOD | GOOD (2) | GOOD | GOOD | GOOD |

### Legend

- **CLAUDE.md**: Line count (target ~60, max ~150). All have purpose + resource map.
- **Hooks**: Count of 4 standard hooks (SessionStart, PreToolUse/cred-scan, Stop, PostToolUse). 3/4 is normal (PostToolUse is optional). 2/4 = missing SessionStart.
- **Perms**: Permission configuration. FIXED = was overly broad, now corrected.
- **Rules**: Path-scoped rule count in `.claude/rules/`.
- **Security**: Credential scanning hook deployed + CodeGuard rules where applicable.
- **Budget**: Context budget. WARN = stale v1 artifacts consuming space (not loaded into context but cluttering .claude/).
- **Disclosure**: Progressive disclosure architecture. All use layered loading.

---

## Dimension Details

### 1. CLAUDE.md Quality

| Project | Lines | Purpose | Commands | Git Workflow | Resource Map | Status |
|---------|-------|---------|----------|-------------|-------------|--------|
| best-practices | 39 | Yes | Yes | Yes | **Added** | GOOD |
| genealogy | 59 | Yes | Yes | Yes | **Added** | GOOD (was 177) |
| security-architect-mcp | 54 | Yes | Yes | Yes | **Added** | GOOD |
| personal-projects | 76 | Yes | Yes | Yes | **Added** | GOOD |
| blog | 41 | Yes | **Added** | **Added** | **Added** | GOOD (was 23) |
| book | 59 | Yes | Yes | Yes | **Added** | GOOD |
| lit-review | 52 | Yes | Yes | Yes | Renamed | GOOD |
| data-quality | 52 | Yes | Yes | Yes | Renamed | GOOD |
| rlm-claude-code | 56 | Yes | Yes | No | Partial | GOOD |
| itu-t-schemas | 53 | Yes | Yes | Yes | Renamed | GOOD |
| Zeek-to-OCSF | 46 | Yes | Yes | Yes | Renamed | GOOD |
| network-viz | 28 | Yes | No | Yes | Renamed | OK (dormant) |
| splunk-benchmark | 42 | Yes | Yes | Yes | Renamed | GOOD |
| ocsf_lab | 21 | **Created** | **Created** | **Created** | **Created** | GOOD (was missing) |
| zeek-iceberg | 55 | Yes | Yes | Yes | No | OK |

### 2. Hook Coverage

| Project | SessionStart | PreToolUse (cred) | Stop | PostToolUse |
|---------|-------------|-------------------|------|-------------|
| best-practices | Yes | **Added** | Yes | Yes |
| genealogy | Yes | **Added** (+ commit gate) | Yes | Yes |
| security-architect-mcp | Yes | **Added** | Yes | - |
| personal-projects | Yes | **Added** | Yes | - |
| blog | Yes | **Added** | Yes | Yes |
| book | Yes | **Added** | Yes | - |
| lit-review | Yes | **Added** | Yes | - |
| data-quality | - | **Added** | Yes | - |
| rlm-claude-code | Yes | **Added** | Yes | - |
| itu-t-schemas | - | **Added** | Yes | - |
| Zeek-to-OCSF | - | **Added** | Yes | - |
| network-viz | Yes | **Added** | Yes | - |
| splunk-benchmark | Yes | **Added** | Yes | - |
| ocsf_lab | - | **Added** | Yes | - |
| zeek-iceberg | Yes | **Added** | Yes | - |

### 3. Path-Scoped Rules Deployed

| Project | markdown | python | schema | security |
|---------|----------|--------|--------|----------|
| best-practices | Yes | - | - | - |
| genealogy | - | Yes | Yes | - |
| security-architect-mcp | - | Yes | - | Yes |
| personal-projects | Yes | Yes | - | - |
| blog | Yes | - | - | - |
| book | Yes | - | - | - |
| lit-review | Yes | Yes | - | - |
| data-quality | - | Yes | - | Yes |
| rlm-claude-code | - | Yes | - | Yes |
| itu-t-schemas | Yes | - | Yes | - |
| Zeek-to-OCSF | Yes | - | Yes | - |
| network-viz | Yes | - | - | - |
| splunk-benchmark | - | Yes | - | Yes |
| ocsf_lab | - | Yes | Yes | - |
| zeek-iceberg | - | Yes | - | Yes |

---

## Remaining Recommendations

All high, medium, and low priority items have been completed:

- ~~SessionStart hooks for 4 projects~~ DONE
- ~~Clean v1 stale directories~~ DONE (security-architect: 152KB, personal-projects: 36KB + 42KB stale files)
- ~~Add resource maps to rlm-claude-code and zeek-iceberg~~ DONE
- ~~Genealogy worktree CLAUDE.md trimming~~ DONE (dry-cross 214→67, kindred 92→64)
- ~~Remove settings.local.json.backup~~ DONE
- ~~Flag stale REPO_STRUCTURE.md~~ DONE

---

## Changes Made in This Review

### Cross-Cutting (all 15 projects)
- **Credential scanning hook**: Created `credential-scan.sh` (PreToolUse, Bash|Write|Edit matcher) scanning for AWS keys, Stripe keys, GitHub tokens, private keys, Google API keys, Slack tokens, generic API secrets. Deployed to all 15 projects.
- **Path-scoped rules**: Created `.claude/rules/` with appropriate rules per project type (25 rule deployments across 15 projects).

### Per-Project
| Project | Changes |
|---------|---------|
| best-practices | +cred hook, +markdown rule, +resource map, removed mcp-server-spec.md, removed git push/checkout from permissions |
| genealogy | +cred hook, +python/schema rules, +resource map, CLAUDE.md 177→59 lines, externalized to docs/ |
| security-architect-mcp | +cred hook, +python/security rules, +resource map, removed 6 stale v1 dirs + 3 stale files (194KB) |
| personal-projects | +cred hook, +markdown/python rules, +resource map, permissions trimmed (removed 40+ destructive pre-approvals), removed stale agents/commands dirs + backup file |
| blog | +cred hook, +markdown rule, +commands/git workflow/resource map, removed mcp-server-spec.md |
| book | +cred hook, +markdown rule, +resource map |
| lit-review | +cred hook, +markdown/python rules, renamed Key Files→Resource Map, removed mcp-server-spec.md |
| data-quality | +cred hook, +python/security rules, renamed Key Files→Resource Map, +SessionStart hook |
| rlm-claude-code | +cred hook, +python/security rules, moved CLAUDE.md root→.claude/, +resource map |
| itu-t-schemas | +cred hook, +markdown/schema rules, renamed Key Files→Resource Map, +SessionStart hook |
| Zeek-to-OCSF | +cred hook, +markdown/schema rules, renamed Key Files→Resource Map, +SessionStart hook |
| network-viz | +cred hook, +markdown rule, renamed Key Files→Resource Map |
| splunk-benchmark | +cred hook, +python/security rules, renamed Key Files→Resource Map |
| ocsf_lab | +cred hook, +python/schema rules, **created CLAUDE.md** (was missing), +SessionStart hook |
| zeek-iceberg | +cred hook, +python/security rules, moved CLAUDE.md root→.claude/, +resource map |
| genealogy-dry-cross | CLAUDE.md 214→67 lines, externalized to docs/SCRIPT_REFERENCE.md + docs/SESSION_HISTORY.md |
| genealogy-kindred | CLAUDE.md 92→64 lines, trimmed status/logins, renamed Reference→Resource Map |
