# Setup Project Prompt

Copy everything below the line and paste it into Claude Code to set up infrastructure.

---

You are setting up AI-driven development infrastructure using the **tiered approach** from https://github.com/flying-coyote/claude-code-project-best-practices

## The Three Tiers

| Tier | When | Time | What You Get |
|------|------|------|--------------|
| **Tier 1: Baseline** | All projects | 5 min | Stop hook + permissions |
| **Tier 2: Active** | Weekly work | 15 min | + CLAUDE.md + SessionStart |
| **Tier 3: Team** | Collaborators | 30 min | + GitHub Actions + /commit-push-pr |

**There's no difference between "new" and "existing" projects** - both use the same tiers.

## Your Task

### Step 1: Assess Current State

Examine this project:
- Run `ls -la` to see the structure
- Check if `.claude/` exists and what's in it
- Check if it's a git repository (`git status`)
- Identify project type (package.json, chapters/, src/, etc.)

Report findings briefly.

### Step 2: Determine Current Tier

Check what infrastructure exists:

| Component | Check | Tier |
|-----------|-------|------|
| `.claude/settings.json` with permissions | Required for Tier 1 |
| Stop hook in settings.json | Required for Tier 1 |
| `.claude/CLAUDE.md` | Required for Tier 2 |
| SessionStart hook | Recommended for Tier 2 |
| `.github/workflows/claude-code.yml` | Required for Tier 3 |
| `.claude/commands/commit-push-pr.md` | Recommended for Tier 3 |

Report: "This project is currently at Tier [0/1/2/3]"

### Step 3: Ask About Target Tier

Ask the user:

"Your project is currently at **Tier [X]**. Which tier would you like to reach?

1. **Tier 1: Baseline** (5 min) - Stop hook + permissions
   - Prevents lost work from forgotten commits
   - Pre-approves common read-only commands

2. **Tier 2: Active Development** (15 min) - Everything in Tier 1 plus:
   - CLAUDE.md with project context
   - SessionStart hook shows git status
   - Project-specific permissions

3. **Tier 3: Team/Production** (30 min) - Everything in Tier 2 plus:
   - GitHub Actions for @.claude PR reviews
   - /commit-push-pr slash command
   - (Optional) PostToolUse auto-formatting

**Recommendation**: [Based on project characteristics - suggest Tier 2 for active solo projects, Tier 3 for team projects]"

### Step 4: Gather Additional Info (for Tier 2+)

If targeting Tier 2 or higher:

1. "What is the project name?" (suggest directory name as default)
2. "In 1-2 sentences, what is this project's purpose?"
3. "What's the primary focus?
   - **coding** - Software development
   - **writing** - Content creation
   - **research** - Analysis projects
   - **hybrid** - Mixed purpose"

### Step 5: Create Infrastructure

#### Tier 1: Baseline (Always Create)

**Create or update `.claude/settings.json`**:

Detect the main branch name first (`git branch` or check remote). Use that in the Stop hook.

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
            "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi; UNPUSHED=$(git log origin/[BRANCH]..HEAD --oneline 2>/dev/null | wc -l); if [ \"$UNPUSHED\" -gt 0 ]; then echo \"⚠️ $UNPUSHED unpushed commit(s)\"; fi'"
          }
        ]
      }
    ]
  }
}
```

Add project-specific permissions based on what's detected:
- `package.json` → Add `"Bash(npm run *)"`
- `pyproject.toml` or `requirements.txt` → Add `"Bash(python3 *)"`
- `docker-compose.yml` → Add `"Bash(docker *)"`
- `Cargo.toml` → Add `"Bash(cargo *)"`

#### Tier 2: Active Development (If Requested)

**Add to settings.json** - SessionStart hook:

```json
{
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

**Create `.claude/hooks/session-start.sh`**:

```bash
#!/bin/bash
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

PROJECT_NAME=$(basename "$PROJECT_ROOT")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
RECENT=$(git log --oneline -3 2>/dev/null || echo "No commits yet")

cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$PROJECT_NAME - Session Context

Branch: $BRANCH
Uncommitted: $UNCOMMITTED files

Recent commits:
$RECENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

if [ "$UNCOMMITTED" -gt 0 ]; then
    echo "⚠️  $UNCOMMITTED uncommitted files - review before new work"
fi

exit 0
```

Make executable: `chmod +x .claude/hooks/session-start.sh`

**Create `.claude/CLAUDE.md`**:

```markdown
# [PROJECT_NAME]

## Purpose
[USER'S DESCRIPTION]

## Current Phase
Active development

## Recent Learnings (Team Memory)
Capture mistakes and insights as they happen. Update 2-3x per week.

### [DATE] - [Brief description]
**What happened**: [Description]
**Prevention**: [Rule to follow]

## Quality Standards
[PRESET-SPECIFIC - see below]

## Git Workflow
Commit prefixes: feat:, fix:, docs:, refactor:, test:, chore:
```

Quality standards by preset:
- **coding**: Clean code, TDD, conventional commits, avoid over-engineering
- **writing**: Evidence-based claims, consistent voice, source attribution
- **research**: Evidence tiers (A-D), hypothesis tracking, document limitations
- **hybrid**: Combine as appropriate

#### Tier 3: Team/Production (If Requested)

**Create `.github/workflows/claude-code.yml`**:

```yaml
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

permissions:
  contents: read
  pull-requests: write
  issues: write

jobs:
  claude-review:
    runs-on: ubuntu-latest
    if: |
      github.event_name == 'pull_request' ||
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@.claude'))
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
          context-files: |
            .claude/CLAUDE.md
```

**Create `.claude/commands/commit-push-pr.md`**:

```markdown
---
description: Commit, push, and create PR. Use when ready to submit work.
allowed-tools: Bash
---

# Commit, Push, and Create PR

1. Run `git status` and `git diff --stat`
2. Stage changes (skip .env, credentials)
3. Commit with conventional prefix (feat:, fix:, docs:, etc.)
4. Push to current branch
5. Create PR with Summary and Test Plan sections
6. Return PR URL
```

### Step 6: Summary

After creating files, summarize:

| Component | Status | Purpose |
|-----------|--------|---------|
| permissions.allow | ✅ Created | Pre-approved commands |
| Stop hook | ✅ Created | Uncommitted/unpushed reminders |
| CLAUDE.md | [✅/⏭️] | Project context |
| SessionStart | [✅/⏭️] | Context at session start |
| GitHub Actions | [✅/⏭️] | @.claude PR reviews |
| /commit-push-pr | [✅/⏭️] | Streamlined git workflow |

"Your project is now at **Tier [X]**."

### Step 7: Explain Next Steps

For Tier 2+:
1. Review `.claude/CLAUDE.md` and customize
2. Add specific conventions or rules
3. Start new session to see hook in action

For Tier 3:
1. Add `ANTHROPIC_API_KEY` to GitHub repository secrets
2. Test by opening a PR and commenting `@.claude review this`

---

## Reference

- Full documentation: https://github.com/flying-coyote/claude-code-project-best-practices
- Project Infrastructure Pattern: patterns/project-infrastructure.md
- Boris Cherny's workflow: SOURCES.md (Tier A source)
