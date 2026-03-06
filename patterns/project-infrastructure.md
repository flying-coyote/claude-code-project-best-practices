---
version-requirements:
  claude-code: "v2.0.0+"  # Checkpoints and rewind feature
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "CLAUDE.md target: ~60 lines (80 max tolerable)"
    source: "Anthropic official guidance"
    date: "2025-11-15"
    revalidate: "2026-11-15"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Project Infrastructure Pattern

**Source**: [Boris Cherny Interview](https://paddo.dev/blog/how-boris-uses-claude-code/), Production validation across 12+ projects
**Evidence Tier**: A (Primary vendor/creator) + B (Production validated)

## Overview

Every project benefits from Claude Code infrastructure. The same patterns apply whether you're setting up a new project or improving an existing one - the only difference is how much infrastructure you add.

**Key insight**: There's no meaningful distinction between "new project setup" and "existing project audit" - both follow the same tiered approach.

---

## Recommended Setup for All Projects

**Time**: 15-30 minutes
**When**: Every project (provides consistent baseline)

| Component | Purpose | Status |
|-----------|---------|--------|
| CLAUDE.md | Project context (~60 lines) | Required |
| Stop hook | Uncommitted work reminder | Required |
| SessionStart hook | Branch + uncommitted count | Required |
| Permission rules | Pre-approve safe commands | Required |

**Complete settings.json**:

```json
{
  "permissions": {
    "allow": [
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git branch*)",
      "Bash(npm run *)",
      "Bash(python3 *)",
      "Bash(docker *)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/session-start.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi; UNPUSHED=$(git log origin/main..HEAD --oneline 2>/dev/null | wc -l); if [ \"$UNPUSHED\" -gt 0 ]; then echo \"⚠️ $UNPUSHED unpushed commit(s)\"; fi'"
          }
        ]
      }
    ]
  }
}
```

**CLAUDE.md structure** (~60 lines):

```markdown
# Project Name

## Purpose
[What this project does]

## Current Phase
[What you're working on now]

## Recent Learnings
[Mistakes and insights - update 2-3x/week]

## Conventions
[Project-specific patterns]
```

**SessionStart hook** (`.claude/hooks/session-start.sh`):

```bash
#!/bin/bash
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "$(basename $(pwd)) - Session Context"
echo ""
echo "Branch: $(git branch --show-current 2>/dev/null || echo 'not a git repo')"
UNCOMMITTED=$(git status --short 2>/dev/null | wc -l | xargs)
echo "Uncommitted: $UNCOMMITTED files"
echo ""
echo "Recent commits:"
git log --oneline -3 2>/dev/null || echo "No git history"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
```

**Why these four components**:
- **CLAUDE.md**: Boris Cherny (Claude Code creator) uses in all projects
- **Stop hook**: Prevents forgotten uncommitted work (Boris: "avoid forgotten sessions")
- **SessionStart**: Context awareness across sessions
- **Permissions**: Friction reduction for common operations

---

## Advanced Patterns (Optional)

### Collaborative Projects

**When**: Multiple contributors, pull request workflow

Add:
- `.github/workflows/claude-code.yml` (enables `@.claude` PR reviews)
- `ARCHITECTURE.md` (shared understanding of system design)

**Time**: Additional 15-30 minutes
**See**: [GitHub Actions Pattern](github-actions-integration.md)

> **Note**: Per [Anthropic guidance](https://code.claude.com/docs/en/best-practices), avoid complex slash command lists. Natural language ("commit and push my changes") works well. Use hooks sparingly—prefer pre-approved permissions via `/permissions`.

**GitHub Actions workflow**:

```yaml
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize]
  issue_comment:
    types: [created]

jobs:
  claude-review:
    if: |
      github.event_name == 'pull_request' ||
      contains(github.event.comment.body, '@.claude')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Fast-Moving Ecosystems

**When**: Documentation projects tracking tools/versions

Add:
- `TOOLS-TRACKER.md` (auto-generated, tracks versions)
- `scripts/check-anthropic-rss.py` (monitors blog posts)
- Measurement expiry system (flags outdated benchmarks)

**Time**: Additional 30 minutes
**See**: [Evolution Tracking Pattern](documentation-maintenance.md#rapid-evolution)

---

## Decision Framework

```
Is this a project you work on?
│
├─► Yes → Apply Recommended Setup (15-30 min)
│         │
│         ├─► Has collaborators/PRs? → Add GitHub Actions
│         │
│         └─► Tracks fast-moving tech? → Add version tracking
│
└─► No → Skip infrastructure setup
```

---

## Implementation Checklist

### Recommended Setup (15-30 minutes)

- [ ] Create `.claude/settings.json` with permissions, Stop hook, and SessionStart hook
- [ ] Create `.claude/CLAUDE.md` with project context (~60 lines)
- [ ] Create `.claude/hooks/session-start.sh`
- [ ] Verify: End a session and see uncommitted changes warning
- [ ] Verify: Start a new session and see git status displayed

### Advanced: GitHub Actions (Additional 15-30 minutes)

- [ ] Complete Recommended Setup
- [ ] Create `.github/workflows/claude-code.yml`
- [ ] Add ANTHROPIC_API_KEY to repository secrets
- [ ] Verify: Open a PR and see @.claude review option

### Advanced: Version Tracking (Additional 30 minutes)

- [ ] Complete Recommended Setup
- [ ] Create `TOOLS-TRACKER.md` with version mentions
- [ ] Create `scripts/check-anthropic-rss.py`
- [ ] Set up measurement expiry system
- [ ] Verify: See outdated versions flagged

---

## Built-In Features (No Setup Required)

These Claude Code features enhance project infrastructure without any configuration:

### Checkpoints and /rewind (v2.0.0+)

Claude Code automatically creates session-level snapshots before each file edit, allowing code and conversation restoration.

```
/rewind
├── View list of checkpoints
├── Restore code to any previous state
├── "Summarize from here" — partial conversation summarization
└── Conversation context restored alongside code
```

**Limitations**:
- Bash commands are not tracked (rm, mv, cp are permanent)
- Checkpoints are session-scoped, not persistent across sessions
- Git remains essential for durable version control

### Session Memory (v2.1.30+)

Claude Code automatically records and recalls learnings across sessions. Stored in `~/.claude/projects/<project>/memory/`.

- No manual setup required
- Claude records project-specific preferences and patterns
- Recalled automatically at session start
- Complements (does not replace) CLAUDE.md

### Data Residency (Opus 4.6+, Enterprise)

For organizations with compliance requirements, the `inference_geo` parameter controls where model inference runs.

```json
{
  "inference_geo": "us"
}
```

| Setting | Behavior | Pricing |
|---------|----------|---------|
| Default | Standard routing | Standard |
| `"us"` | US-only inference | 1.1x standard pricing |

**Availability**: Models released after February 1, 2026. Workspace-level configuration via `allowed_inference_geos` and `default_inference_geo`.

---

## Adding Advanced Features

Projects may need additional features. Common additions:

| Trigger | Action |
|---------|--------|
| "Team needs AI PR reviews" | Add GitHub Actions workflow |
| "Tracking outdated docs" | Add version tracking system |
| "Want faster git workflow" | Use natural language: "commit and push" |

---

## Anti-Patterns

### Over-Engineering Upfront

**Problem**: Adding GitHub Actions and version tracking before understanding needs
**Solution**: Start with recommended setup, add advanced features as pain points emerge

### Skipping Recommended Setup

**Problem**: No baseline protection, lost work from forgotten commits, no context across sessions
**Solution**: Always apply recommended setup (15-30 min), even for "quick" projects

### Different Patterns for New vs Existing

**Problem**: Maintaining two mental models, inconsistent infrastructure
**Solution**: Use this unified approach for all projects

---

## Quick Commands

**Apply recommended setup to current project**:

See [QUICKSTART.md](../QUICKSTART.md) for complete bash commands to set up:
- `.claude/settings.json` (permissions, hooks)
- `.claude/CLAUDE.md` (project context)
- `.claude/hooks/session-start.sh` (git status display)

---

## Related Patterns

- [Advanced Hooks](./advanced-hooks.md) - Deep dive into hook patterns
- [Documentation Maintenance](./documentation-maintenance.md) - CLAUDE.md best practices
- [GitHub Actions Integration](./github-actions-integration.md) - CI/CD setup
- [Parallel Sessions](./parallel-sessions.md) - Multi-session workflows
- [Safety and Sandboxing](./safety-and-sandboxing.md) - Security infrastructure

---

## Sources

- [Boris Cherny Interview - Paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code/)
- [Anthropic Best Practices](https://code.claude.com/docs/en/best-practices) (Canonical)
- [Data Residency Documentation](https://platform.claude.com/docs/en/build-with-claude/data-residency) (February 2026)
- Production validation across 12+ projects

*Last updated: February 2026*
