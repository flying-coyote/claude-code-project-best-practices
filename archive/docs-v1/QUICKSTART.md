# Quick Setup: Claude Code Best Practices

**Goal**: Get recommended project infrastructure running in 15-30 minutes.

---

## Recommended Setup (15-30 minutes)

All projects should have these four components:

### 1. Create Directory Structure

```bash
mkdir -p .claude .claude/hooks
```

### 2. Create `.claude/settings.json`

```bash
cat > .claude/settings.json <<'EOF'
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
            "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi; UNPUSHED=$(git log origin/master..HEAD --oneline 2>/dev/null | wc -l); if [ \"$UNPUSHED\" -gt 0 ]; then echo \"⚠️ $UNPUSHED unpushed commit(s)\"; fi'"
          }
        ]
      }
    ]
  }
}
EOF
```

**Customize permissions** (auto-detect your stack):

```bash
# If you have package.json
jq '.permissions.allow += ["Bash(npm run *)"]' .claude/settings.json > tmp.json && mv tmp.json .claude/settings.json

# If you have Python
jq '.permissions.allow += ["Bash(python3 *)", "Bash(pip *)"]' .claude/settings.json > tmp.json && mv tmp.json .claude/settings.json
```

### 3. Create `.claude/hooks/session-start.sh`

```bash
cat > .claude/hooks/session-start.sh <<'EOF'
#!/bin/bash
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

PROJECT_NAME=$(basename "$PROJECT_ROOT")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
RECENT=$(git log --oneline -3 2>/dev/null || echo "No commits")

cat <<BANNER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$PROJECT_NAME - Session Context

Branch: $BRANCH
Uncommitted: $UNCOMMITTED files

Recent commits:
$RECENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BANNER

[ "$UNCOMMITTED" -gt 0 ] && echo "⚠️ $UNCOMMITTED uncommitted files - review before new work"
exit 0
EOF

chmod +x .claude/hooks/session-start.sh
```

### 4. Create `.claude/CLAUDE.md`

**CRITICAL: Keep ~60 lines (80 max tolerable)**

```bash
cat > .claude/CLAUDE.md <<'EOF'
# [Your Project Name]

## Purpose
[1-2 sentences describing what this project does]

## Commands
- `npm test` - Run test suite
- `npm run build` - Build for production

## Current Focus
[What you're working on NOW - 1 sentence]

## Known Gotchas
### [Issue that caused 2+ mistakes]
**Problem**: [Brief description]
**Fix**: [How to avoid]

## Git Workflow
Commit prefixes: feat:, fix:, docs:, refactor:, test:, chore:
EOF
```

**Review and trim CLAUDE.md**:
- Delete anything not preventing repeated mistakes
- Target: ~60 lines (80 max tolerable)
- Rule: "Would removing this cause mistakes? If not, cut it."

**Done!** Restart Claude Code to see hooks in action.

---

## Advanced Setup (Optional)

### For Teams: GitHub Actions (Add 15-30 min)

**When**: Multiple collaborators, pull request workflow

**What you get**: `@.claude` PR review comments

#### Setup

1. **Create `.github/workflows/claude-code.yml`**:

```bash
mkdir -p .github/workflows
cat > .github/workflows/claude-code.yml <<'EOF'
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
EOF
```

2. **Add `ANTHROPIC_API_KEY` to GitHub Secrets**:
   - Go to repo Settings → Secrets → Actions
   - Add new secret: `ANTHROPIC_API_KEY` with your API key

3. **Test**:
   - Open a PR
   - Comment: `@.claude review this`

**Done!** Team can now use @.claude in PRs.

---

### For Docs Projects: Version Tracking (Add 30 min)

**When**: Documentation projects tracking fast-moving tech (AI tools, frameworks)

**What you get**: Automated tool/version tracking + AI-powered blog monitoring

#### Setup

1. **Install automation files**:

```bash
# Core tracking documents
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TOOLS-TRACKER.md
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/DEPRECATIONS.md

# Scripts
mkdir -p scripts
cd scripts
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/generate-tools-tracker.py
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/check-measurement-expiry.py
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/check-anthropic-rss.py
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/analyze-blog-post.py
cd ..

# Workflows
mkdir -p .github/workflows
cd .github/workflows
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.github/workflows/tools-evolution-tracker.yml
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.github/workflows/anthropic-blog-rss.yml
cd ../..

# Skills
mkdir -p .claude/skills/pattern-version-updater .claude/skills/emerging-pattern-monitor
curl -o .claude/skills/pattern-version-updater/SKILL.md \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.claude/skills/pattern-version-updater/SKILL.md
curl -o .claude/skills/emerging-pattern-monitor/SKILL.md \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.claude/skills/emerging-pattern-monitor/SKILL.md

# Dependencies
pip install pyyaml requests anthropic
```

2. **Customize for your domain**:

**Edit `TOOLS-TRACKER.md`** - Replace components:
```markdown
## Component 1: CLAUDE.md Patterns → Your Config Patterns
## Component 5: MCP → Your Integration Layer
## Component 8: Marketplaces → Your Distribution Channels
```

**Edit `scripts/generate-tools-tracker.py`** - Update tool names (line 35):
```python
self.tool_names = [
    "Your Tool", "Your Framework", "Your Server",
    # ... your ecosystem tools
]
```

**Edit `scripts/check-anthropic-rss.py`** - Update RSS URL (line 33):
```python
DEFAULT_RSS_URL = "https://your-vendor.com/rss.xml"
```

3. **Configure GitHub Secrets**:
   - Add `ANTHROPIC_API_KEY` for blog analysis (or use your LLM API)

4. **Test locally**:

```bash
python scripts/generate-tools-tracker.py
python scripts/check-measurement-expiry.py
```

**Done!** Push to GitHub to enable automated workflows.

---

## What You Get

### Recommended Setup
- ✅ Stop hook (uncommitted warnings)
- ✅ Pre-approved git commands
- ✅ CLAUDE.md project context (~60 lines)
- ✅ SessionStart hook (git status display)

### Advanced: GitHub Actions
- ✅ `@.claude` PR review comments
- ✅ Automated code analysis on pull requests

### Advanced: Version Tracking
- ✅ Automated tool/version tracking
- ✅ AI-powered blog monitoring
- ✅ Version dependency tracking
- ✅ Measurement expiry system

---

## Next Steps

**After setup, learn the patterns**:
- 📚 **All 36 patterns**: https://github.com/flying-coyote/claude-code-project-best-practices
- 🎯 **Pattern Decision Matrix**: "I Need To..." → pattern lookup
- 📖 **Detailed setup guide**: [MAKE-PROJECT-RECOMMENDATIONS.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/MAKE-PROJECT-RECOMMENDATIONS.md)

**Key principles** (read these first):
- [FOUNDATIONAL-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/FOUNDATIONAL-PRINCIPLES.md) - The Big 3

**Common issues**:
- [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md) - CLAUDE.md bloat, setup problems, team adoption

---

## FAQ

**Q: Do I need all four components?**
Yes - they work together and take 15-30 minutes total. The Stop hook prevents lost work, SessionStart provides context awareness, CLAUDE.md maintains consistency, and permissions reduce friction.

**Q: Can I add components gradually?**
Yes, but the core four are so quick (~15 min) that it's better to install all at once. You get immediate benefits from the complete system.

**Q: What if I only want minimal overhead?**
The recommended setup IS minimal (~60 lines in CLAUDE.md). If you absolutely need less, you can skip SessionStart hook, but you'll lose session context awareness. Boris Cherny (Claude Code creator) uses this setup in all projects.

**Q: What if CLAUDE.md keeps growing past 60 lines?**
- See [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md#claudemd-bloat)
- Rule: "Would removing this cause mistakes? If not, cut it."
- Delete anything not preventing repeated mistakes

**Q: Do I need all 8 components (skills, MCP, etc)?**
No! Start with CLAUDE.md + natural language. Add components only when needed.
- See [MAKE-PROJECT-RECOMMENDATIONS.md Step 4](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/MAKE-PROJECT-RECOMMENDATIONS.md) for component guidance.

**Q: Can I use this with other AI coding tools (Cursor, Aider)?**
Principles apply across tools. See [tool-ecosystem.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/tool-ecosystem.md) for guidance.

**Q: When should I add GitHub Actions?**
Add when you have multiple collaborators and use pull requests. It enables `@.claude` review comments that help with code quality and consistency.

**Q: When should I add Version Tracking?**
Add for documentation projects tracking rapidly evolving tech. If you're documenting AI tools, frameworks, or APIs that change frequently, version tracking helps keep docs current.

---

**Need help?** File an issue: https://github.com/flying-coyote/claude-code-project-best-practices/issues
