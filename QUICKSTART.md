# Quick Start: Claude Code Best Practices

**Goal**: Get project-specific Claude Code infrastructure running in 5-45 minutes.

**Choose your starting point**:
- 🚀 **5 minutes**: [Tier 1 - Baseline](#tier-1-baseline-5-minutes) (All projects)
- ⚡ **15 minutes**: [Tier 2 - Active Development](#tier-2-active-development-15-minutes) (Weekly work)
- 👥 **30 minutes**: [Tier 3 - Team/Production](#tier-3-teamproduction-30-minutes) (Collaborators)
- 📊 **45 minutes**: [Tier 4 - Rapid Evolution Tracking](#tier-4-rapid-evolution-tracking-45-minutes) (Documentation projects)

---

## Tier 1: Baseline (5 minutes)

**What you get**: Stop hook warnings for uncommitted changes, pre-approved git commands.

### Quick Setup

1. **Create `.claude/settings.json`**:

```bash
mkdir -p .claude
cat > .claude/settings.json <<'EOF'
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
            "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi; UNPUSHED=$(git log origin/master..HEAD --oneline 2>/dev/null | wc -l); if [ \"$UNPUSHED\" -gt 0 ]; then echo \"⚠️ $UNPUSHED unpushed commit(s)\"; fi'"
          }
        ]
      }
    ]
  }
}
EOF
```

2. **Add project-specific permissions** (auto-detect):

```bash
# If you have package.json
jq '.permissions.allow += ["Bash(npm run *)"]' .claude/settings.json > tmp.json && mv tmp.json .claude/settings.json

# If you have Python
jq '.permissions.allow += ["Bash(python3 *)", "Bash(pip *)"]' .claude/settings.json > tmp.json && mv tmp.json .claude/settings.json
```

**Done!** Exit Claude Code session and restart to see Stop hook in action.

---

## Tier 2: Active Development (15 minutes)

**What you get**: Tier 1 + CLAUDE.md project context + SessionStart hook.

### Quick Setup

1. **Complete Tier 1** (5 min)

2. **Create `.claude/hooks/session-start.sh`**:

```bash
mkdir -p .claude/hooks
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

3. **Add SessionStart hook to settings.json**:

```bash
jq '.hooks.SessionStart = [{"matcher": "", "hooks": [{"type": "command", "command": "bash .claude/hooks/session-start.sh"}]}]' .claude/settings.json > tmp.json && mv tmp.json .claude/settings.json
```

4. **Create `.claude/CLAUDE.md`** (CRITICAL: Keep ~60 lines):

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

5. **Review and trim CLAUDE.md**:
   - Delete anything not preventing repeated mistakes
   - Target: ~60 lines (80 max tolerable)

**Done!** Restart Claude Code to see SessionStart hook.

---

## Tier 3: Team/Production (30 minutes)

**What you get**: Tier 1 + Tier 2 + GitHub Actions for PR reviews with @.claude.

### Quick Setup

1. **Complete Tier 2** (20 min)

2. **Create `.github/workflows/claude-code.yml`**:

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

3. **Add `ANTHROPIC_API_KEY` to GitHub Secrets**:
   - Go to repo Settings → Secrets → Actions
   - Add new secret: `ANTHROPIC_API_KEY` with your API key

4. **Test**:
   - Open a PR
   - Comment: `@.claude review this`

**Done!** Team can now use @.claude in PRs.

---

## Tier 4: Rapid Evolution Tracking (45 minutes)

**What you get**: Tier 1-3 + automated tool/version tracking + AI-powered blog monitoring.

**When to use**: Documentation projects tracking rapidly evolving ecosystems (AI tools, frameworks).

### Quick Setup

1. **Complete Tier 2** (20 min) - Tier 3 optional

2. **Install automation files** (5 min):

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

3. **Customize for your domain** (15 min):

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

4. **Configure GitHub Secrets**:
   - Add `ANTHROPIC_API_KEY` for blog analysis (or use your LLM API)

5. **Test locally** (5 min):

```bash
python scripts/generate-tools-tracker.py
python scripts/check-measurement-expiry.py
```

**Done!** Push to GitHub to enable automated workflows.

---

## What You Get at Each Tier

| Feature | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---------|--------|--------|--------|--------|
| Stop hook (uncommitted warnings) | ✅ | ✅ | ✅ | ✅ |
| Pre-approved git commands | ✅ | ✅ | ✅ | ✅ |
| CLAUDE.md project context | - | ✅ | ✅ | ✅ |
| SessionStart hook | - | ✅ | ✅ | ✅ |
| GitHub Actions PR reviews | - | - | ✅ | ✅ |
| Automated tool tracking | - | - | - | ✅ |
| AI-powered blog monitoring | - | - | - | ✅ |
| Version dependency tracking | - | - | - | ✅ |
| Measurement expiry system | - | - | - | ✅ |

---

## Next Steps

**After setup, learn the patterns**:
- 📚 **All 34 patterns**: https://github.com/flying-coyote/claude-code-project-best-practices
- 🎯 **Pattern Decision Matrix**: "I Need To..." → pattern lookup
- 📖 **Detailed setup guide**: [SETUP-PROJECT.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/SETUP-PROJECT.md)

**Key principles** (read these first):
- [FOUNDATIONAL-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/FOUNDATIONAL-PRINCIPLES.md) - The Big 3
- [QUICK-REFERENCE-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/QUICK-REFERENCE-PRINCIPLES.md) - 1-page printable

**Common issues**:
- [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md) - CLAUDE.md bloat, setup problems, team adoption

---

## FAQ

**Q: Which tier should I use?**
- **Tier 1**: All projects (5 min, no downside)
- **Tier 2**: Weekly active development (minimal CLAUDE.md helps consistency)
- **Tier 3**: Team projects with PRs (enables @.claude reviews)
- **Tier 4**: Documentation projects tracking rapidly evolving tech

**Q: Can I skip tiers?**
- Yes! Tiers are additive, not required. Jump to Tier 3 if you want team features.

**Q: What if CLAUDE.md keeps growing past 60 lines?**
- See [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md#claudemd-bloat)
- Rule: "Would removing this cause mistakes? If not, cut it."

**Q: Do I need all 8 components (skills, MCP, etc)?**
- No! Start with CLAUDE.md + natural language. Add components only when needed.
- See [SETUP-PROJECT.md Step 4](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/SETUP-PROJECT.md) for component guidance.

**Q: Can I use this with other AI coding tools (Cursor, Aider)?**
- Principles apply across tools. See [tool-ecosystem.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/tool-ecosystem.md) for guidance.

---

**Need help?** File an issue: https://github.com/flying-coyote/claude-code-project-best-practices/issues
