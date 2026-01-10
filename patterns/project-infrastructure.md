# Project Infrastructure Pattern

**Source**: [Boris Cherny Interview](https://paddo.dev/blog/how-boris-uses-claude-code/), Production validation across 12+ projects
**Evidence Tier**: A (Primary vendor/creator) + B (Production validated)

## Overview

Every project benefits from Claude Code infrastructure. The same patterns apply whether you're setting up a new project or improving an existing one - the only difference is how much infrastructure you add.

**Key insight**: There's no meaningful distinction between "new project setup" and "existing project audit" - both follow the same tiered approach.

---

## The Three Tiers

### Tier 1: Baseline (All Projects)

**Time to implement**: 5 minutes
**When**: Every project, no exceptions

| Component | Purpose | Required |
|-----------|---------|----------|
| `permissions.allow` | Pre-approve read-only commands | ✅ Yes |
| Stop hook | Uncommitted/unpushed reminders | ✅ Yes |

**Minimum settings.json**:

```json
{
  "permissions": {
    "allow": [
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git branch*)"
    ]
  },
  "hooks": {
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

**Why this is baseline**:
- Stop hooks prevent lost work (Boris Cherny: "avoid forgotten sessions")
- Pre-approved commands reduce friction for common operations
- Takes 5 minutes, zero ongoing maintenance

---

### Tier 2: Active Development (Projects You Work On Regularly)

**Time to implement**: 15-30 minutes
**When**: Projects with >1 session/week, complex enough to need context

| Component | Purpose | Required |
|-----------|---------|----------|
| Everything from Tier 1 | Baseline | ✅ Yes |
| CLAUDE.md | Project context and conventions | ✅ Yes |
| SessionStart hook | Load context at session start | Recommended |
| Project-specific permissions | Tools you use frequently | Recommended |

**Additional settings.json**:

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
    "Stop": [...]
  }
}
```

**CLAUDE.md structure**:

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

---

### Tier 3: Team/Production (Collaborative Projects)

**Time to implement**: 30-60 minutes
**When**: Multiple contributors, PRs, CI/CD

| Component | Purpose | Required |
|-----------|---------|----------|
| Everything from Tier 2 | Active development | ✅ Yes |
| GitHub Actions workflow | Automated @.claude reviews | Recommended |
| /commit-push-pr command | Streamlined git workflow | Recommended |
| PostToolUse formatting | Auto-format on Write/Edit | Optional |
| ARCHITECTURE.md | System design documentation | Recommended |

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

---

## Decision Framework

```
Is this a git repository?
│
├─► Yes → Apply Tier 1 (baseline)
│         │
│         ├─► Work on it weekly? → Apply Tier 2 (active)
│         │         │
│         │         └─► Has collaborators/PRs? → Apply Tier 3 (team)
│         │
│         └─► Rarely touch it? → Tier 1 is sufficient
│
└─► No → Consider if it should be
```

---

## Implementation Checklist

### Tier 1 (5 minutes)

- [ ] Create `.claude/settings.json` with permissions + Stop hook
- [ ] Verify: End a session and see the reminder

### Tier 2 (15-30 minutes)

- [ ] Complete Tier 1
- [ ] Create `.claude/CLAUDE.md` with project context
- [ ] Create `.claude/hooks/session-start.sh`
- [ ] Add SessionStart hook to settings.json
- [ ] Add project-specific permissions (npm, python3, docker, etc.)
- [ ] Verify: Start a session and see context loaded

### Tier 3 (30-60 minutes)

- [ ] Complete Tier 2
- [ ] Create `.github/workflows/claude-code.yml`
- [ ] Add ANTHROPIC_API_KEY to repository secrets
- [ ] Create `.claude/commands/commit-push-pr.md`
- [ ] (Optional) Add PostToolUse formatting hook
- [ ] Verify: Open a PR and see @.claude review option

---

## Upgrading Between Tiers

Projects naturally evolve. Common upgrade paths:

| Trigger | Action |
|---------|--------|
| "I keep forgetting context" | Tier 1 → Tier 2 (add CLAUDE.md) |
| "I want faster git workflow" | Add /commit-push-pr |
| "Team needs AI review" | Tier 2 → Tier 3 (add GitHub Actions) |
| "Code style inconsistent" | Add PostToolUse formatting |

---

## Anti-Patterns

### Starting at Tier 3

**Problem**: Over-engineering infrastructure before understanding needs
**Solution**: Start at Tier 1, upgrade as pain points emerge

### Skipping Tier 1

**Problem**: No baseline protection, lost work from forgotten commits
**Solution**: Always apply Tier 1, even for "quick" projects

### Different Patterns for New vs Existing

**Problem**: Maintaining two mental models, inconsistent infrastructure
**Solution**: Use this unified tiered approach for all projects

---

## Quick Commands

**Apply Tier 1 to current project**:
```bash
mkdir -p .claude && cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git branch*)"
    ]
  },
  "hooks": {
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
EOF
```

---

## Related Patterns

- [Advanced Hooks](./advanced-hooks.md) - Deep dive into hook patterns
- [Documentation Maintenance](./documentation-maintenance.md) - CLAUDE.md best practices
- [GitHub Actions Integration](./github-actions-integration.md) - CI/CD setup
- [Parallel Sessions](./parallel-sessions.md) - Multi-session workflows

---

## Sources

- [Boris Cherny Interview - Paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code/)
- [Anthropic Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- Production validation across 12+ projects

*Last updated: January 2026*
