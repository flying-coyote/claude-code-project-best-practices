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

## Core Principles (Read These First)

Before setting up infrastructure, understand the foundational principles that make these mechanics effective:

### The Big 3: Non-Negotiable Principles

1. **Keep CLAUDE.md Ruthlessly Minimal (~60 Lines)**
   - Target: ~60 lines (80 max tolerable)
   - Rule: "Would removing this cause mistakes? If not, cut it."
   - Include ONLY: Project purpose (1-2 sentences), key commands, known gotchas, current focus
   - See: [FOUNDATIONAL-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/FOUNDATIONAL-PRINCIPLES.md)

2. **Plan First, Always (For Non-Trivial Work)**
   - Use `/plan` before implementing features, architectural changes, or multi-file work
   - Planning effort directly improves output quality (2-3x improvement)
   - When to plan: Any feature >2-3 files, multiple valid approaches, architectural decisions
   - When to skip: Bug fixes, typos, copy-paste implementations

3. **Context Engineering > Prompt Engineering**
   - External artifacts (specs, docs, git history) = agent memory
   - Deterministic context (user-controlled) beats probabilistic context (AI-discovered)
   - One feature at a time to prevent context exhaustion

**Quick Reference**: Print and keep visible: [QUICK-REFERENCE-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/QUICK-REFERENCE-PRINCIPLES.md)

---

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
| `.claude/settings.json` with permissions | Required | Tier 1 |
| Stop hook in settings.json | Required | Tier 1 |
| `.claude/CLAUDE.md` (under 80 lines) | Required | Tier 2 |
| SessionStart hook | Recommended | Tier 2 |
| `.github/workflows/claude-code.yml` | Required | Tier 3 |

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
   - (Optional) PostToolUse auto-formatting
   - Note: Natural language "commit and push" works - custom commands rarely needed

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

⚠️ **CRITICAL**: Target ~60 lines. This template shows structure but YOUR file should be much shorter. Only include what prevents repeated mistakes.

```markdown
# [PROJECT_NAME]

## Purpose
[USER'S DESCRIPTION - 1-2 sentences ONLY]

## Commands
[ONLY commands that vary from standard - 3-5 max]

## Current Focus
[What are you working on NOW - 1-2 sentences]

## Known Gotchas
[ONLY issues that caused 2+ mistakes]

### [Issue name]
**Problem**: [Brief description]
**Fix**: [How to avoid]

## Quality Standards
[PRESET-SPECIFIC - see below, keep to 3-5 bullets]

## Git Workflow
Commit prefixes: feat:, fix:, docs:, refactor:, test:, chore:
```

Quality standards by preset (pick 3-5 most critical):
- **coding**: Clean code, TDD, conventional commits, avoid over-engineering
- **writing**: Evidence-based claims, consistent voice, source attribution
- **research**: Evidence tiers (A-D), hypothesis tracking, document limitations
- **hybrid**: Combine as appropriate

**After creating**: Review ruthlessly. If Claude didn't ask about it, and it hasn't caused 2+ mistakes, delete it.

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

**Optional - Custom commands** (usually not needed):

Note: Claude Code understands natural language like "commit and push these changes". Custom slash commands are rarely necessary and add maintenance burden.

If the project has complex, repetitive workflows, consider `.claude/commands/` files. See [plugins-and-extensions.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/plugins-and-extensions.md) for guidance.

### Step 6: Summary

After creating files, summarize:

| Component | Status | Purpose |
|-----------|--------|---------|
| permissions.allow | ✅ Created | Pre-approved commands |
| Stop hook | ✅ Created | Uncommitted/unpushed reminders |
| CLAUDE.md | [✅/⏭️] | Project context (~60 lines target) |
| SessionStart | [✅/⏭️] | Context at session start |
| GitHub Actions | [✅/⏭️] | @.claude PR reviews |

"Your project is now at **Tier [X]**."

### Step 7: Explain Next Steps

For Tier 2+:
1. **Review `.claude/CLAUDE.md` and ruthlessly trim** - Target ~60 lines, remove anything not preventing mistakes
2. **Remember to plan first** - Use `/plan` before starting any non-trivial feature work
3. Start new session to see SessionStart hook in action
4. After 1-2 weeks, audit CLAUDE.md again - delete sections that weren't needed

For Tier 3:
1. Add `ANTHROPIC_API_KEY` to GitHub repository secrets
2. Test by opening a PR and commenting `@.claude review this`

**Key Principle Reminder**: "Would removing this cause mistakes? If not, cut it." - Anthropic Official Docs

---

## Reference

**Core Principles**:
- [FOUNDATIONAL-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/FOUNDATIONAL-PRINCIPLES.md) - The Big 3 (read first)
- [QUICK-REFERENCE-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/QUICK-REFERENCE-PRINCIPLES.md) - 1-page printable reference

**Key Patterns**:
- [spec-driven-development.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/spec-driven-development.md) - Specify → Plan → Tasks → Implement
- [context-engineering.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/context-engineering.md) - Deterministic vs probabilistic context
- [project-infrastructure.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/project-infrastructure.md) - Tiered setup details
- [evidence-tiers.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/evidence-tiers.md) - Source evaluation framework

**Full Repository**:
- https://github.com/flying-coyote/claude-code-project-best-practices
- [SOURCES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/SOURCES.md) - All source attributions (Tier A-D)
