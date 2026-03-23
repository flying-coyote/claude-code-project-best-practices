# Version Tracking

**Last Updated**: 2026-03-23

This document tracks current versions of Claude Code and models to support version requirement validation across patterns.

---

## Current Versions (as of March 2026)

### Claude Code

**Current Version**: **v2.1.81**

**Source**: [Anthropic Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

**Key Features in v2.1.81**:
- `--bare` flag for scripted `-p` calls (skips hooks, LSP, plugin sync)
- `--channels` permission relay for tool approval forwarding
- MCP OAuth Client ID Metadata Document support

**Recent Version History**:
- v2.1.81 (current) - March 20, 2026
- v2.1.80 - March 19, 2026: Channels (`--channels`), `effort` frontmatter for skills, `rate_limits` in statusline
- v2.1.79 - March 18, 2026: `--console` flag, `/remote-control` for VSCode, AI-generated session titles
- v2.1.78 - March 17, 2026: `StopFailure` hook, `effort`/`maxTurns`/`disallowedTools` frontmatter, `${CLAUDE_PLUGIN_DATA}`
- v2.1.77 - March 17, 2026: Opus 4.6 output limits to 64k tokens, `allowRead` sandbox, `/copy N`, `--worktree` perf
- v2.1.76 - March 14, 2026: MCP elicitation, `Elicitation`/`ElicitationResult` hooks, `/effort`, `-n`/`--name` flag, `worktree.sparsePaths`
- v2.1.37 - February 2026: Agent teams (experimental), session memory, PDF page ranges
- v2.1.3 - January 2026
- v2.1.0 - January 2026
- v2.0.76 - December 2025
- v2.0.60 - November 2025

### Models

**Current Models** (as of March 2026):

| Model | Version | Context | Release Date | Key Features |
|-------|---------|---------|--------------|--------------|
| **Opus 4.6** | `claude-opus-4-6` | 1M tokens | February 5, 2026 | Agent teams, adaptive reasoning, 64k output (v2.1.77+) |
| **Sonnet 4.6** | `claude-sonnet-4-6` | 200K tokens | January 2026 | Production workhorse |
| **Haiku 4.5** | `claude-haiku-4-5-20251001` | 200K tokens | October 2025 | Extended thinking, 1/3 cost of Sonnet |

**Pricing** (as of Mar 2026):
- Opus 4.6: $5 input / $25 output per million tokens (67% reduction from Opus 4.5)
- Sonnet 4.6: Standard pricing
- Haiku 4.5: ~1/3 cost of Sonnet 4.6

---

## Beta Headers (Current Status)

Tracking beta headers referenced in patterns to identify graduation or updates.

| Feature | Beta Header | Announced | Status | Last Checked |
|---------|-------------|-----------|--------|--------------|
| **Advanced Tool Use** | `advanced-tool-use-2025-11-20` | Nov 24, 2025 | ⚠️ Unknown (4+ months old) | 2026-03-23 |
| **1M Context** | `context-1m-2025-08-07` | Aug 2025 | ⚠️ Unknown (7+ months old) | 2026-03-23 |

**Action Required**: Verify current status with [Anthropic Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

## New Features Since v2.1.37 (Highlights)

| Feature | Version | Category |
|---------|---------|----------|
| **Channels** (`--channels`) | v2.1.80 | Push events into sessions (Telegram, Discord, webhooks) |
| **MCP Elicitation** | v2.1.76 | MCP servers request structured user input |
| **`/effort` command** | v2.1.76 | Control reasoning effort level |
| **`/remote-control`** | v2.1.79 | Drive local sessions from claude.ai or mobile |
| **`StopFailure` hook** | v2.1.78 | Handle API errors in hooks |
| **`prompt` hook type** | v2.1.76+ | Single-turn LLM evaluation hooks |
| **`agent` hook type** | v2.1.76+ | Subagent-powered verification hooks |
| **Opus 4.6 64k output** | v2.1.77 | Increased output limit |
| **Plugin persistent state** | v2.1.78 | `${CLAUDE_PLUGIN_DATA}` for plugin data |
| **`--bare` flag** | v2.1.81 | Scripted `-p` calls skip hooks/LSP |
| **`worktree.sparsePaths`** | v2.1.76 | Git sparse checkout for worktrees |
| **Skill `effort` frontmatter** | v2.1.80 | Control effort per skill |
| **24 hook event types** | v2.1.76-80 | Up from ~8 documented types |

---

## Version Requirement Validation

### When to Update Version Requirements

**Trigger events**:
1. New Claude Code major/minor release (e.g., v2.2.0)
2. New model release (e.g., Opus 4.7)
3. Feature graduation from beta to stable
4. Deprecation announcements

### Pattern Files with Version Requirements

Patterns with `version-requirements:` frontmatter:

```bash
# Find all patterns with version requirements
grep -l "version-requirements:" patterns/*.md
```

**Common version references** (as of Mar 2026):
- `v2.0.0+` - MCP support (baseline)
- `v2.0.45+` - PermissionRequest hooks
- `v2.0.60+` - Background agent support
- `v2.1.0+` - Skill hot-reload, wildcard permissions
- `v2.1.30+` - Session memory feature
- `v2.1.32+` - Agent teams (experimental)
- `v2.1.76+` - MCP elicitation, `/effort`, 24 hook events
- `v2.1.77+` - Opus 4.6 64k output
- `v2.1.80+` - Channels (research preview)
- `Opus 4.6+` - 1M context, agent teams

### Validation Process

**Quarterly Review** (Q1: Mar 31, Q2: Jun 30, Q3: Sep 30, Q4: Dec 31):

1. **Check for new releases**:
   ```bash
   # Visit Anthropic changelog
   open https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
   ```

2. **Update this file**:
   - Update "Current Versions" section
   - Update "Recent Version History"
   - Check beta header status

3. **Audit pattern version requirements**:
   ```bash
   # Find patterns with outdated version requirements
   grep -r "v2\.0\." patterns/
   grep -r "v2\.1\." patterns/
   ```

4. **Update patterns if needed**:
   - If feature is now baseline, update to current version
   - Add `version-last-verified` field to frontmatter
   - Document any breaking changes

---

## Version-Last-Verified Field

Starting February 2026, patterns with version requirements should include:

```yaml
---
version-requirements:
  claude-code: "v2.1.0+"  # Skills auto-reload
  model: "Opus 4.6+"      # Agent teams
version-last-verified: "2026-02-27"  # Date version requirements checked
---
```

**Purpose**: Track when version requirements were last validated against current releases.

**Update trigger**: Quarterly review or when Claude Code version changes.

---

## Breaking Changes History

Track breaking changes that require pattern updates.

### Claude Code v2.1.76-81 (March 2026)

**Breaking changes**: None
**New features**: MCP elicitation, channels (research preview), 24 hook event types, `/effort` command, `/remote-control`, `StopFailure` hook, `prompt` and `agent` hook types, Opus 4.6 64k output, `--bare` flag, `worktree.sparsePaths`, plugin persistent state

### Claude Code v2.1.0 (January 2026)

**Breaking changes**: None
**New features**: Skill hot-reload, wildcard permissions, context forking

### Claude Code v2.0.60 (November 2025)

**Breaking changes**: None
**New features**: Background agent support

### Opus 4.6 (February 5, 2026)

**Breaking changes**: None
**New features**: 1M context (beta), agent teams, adaptive reasoning

---

## Related Documentation

- [SOURCES.md - Claude Code Changelog](SOURCES.md#claude-code-changelog) - Detailed feature list
- [AUDIT-2026-02-27.md](AUDIT-2026-02-27.md) - Version tracking audit findings
- [Anthropic Releases](https://github.com/anthropics/claude-code/releases) - Official release notes

---

## Maintenance Schedule

**Update frequency**: Quarterly + ad-hoc for major releases

**Next scheduled update**: **June 30, 2026** (Q2 2026 review)

**Owner**: Maintenance team (see CONTRIBUTING.md)

---

*Last verified: March 23, 2026*
