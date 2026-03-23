# Make Project Recommendations Prompt

Copy everything below the line and paste it into Claude Code. This prompt analyzes your project and recommends appropriate infrastructure.

---

You are setting up AI-driven development infrastructure from https://github.com/flying-coyote/claude-code-project-best-practices

## The Setup

**Recommended for all projects** (15-30 minutes):
- CLAUDE.md (~60 lines project context)
- Stop hook (uncommitted work reminder)
- SessionStart hook (git status display)
- Permission rules (pre-approve safe commands)

**Advanced (optional)**:
- **GitHub Actions** (for teams with collaborators)
  - Enables `@.claude` PR review comments
  - Requires: ANTHROPIC_API_KEY in GitHub secrets

- **Version Tracking** (for docs projects tracking fast-moving tech)
  - Auto-tracks tool/version mentions
  - Monitors blog posts for ecosystem changes

**There's no difference between "new" and "existing" projects** - both use the same setup approach.

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

---

## Your Task

### Step 1: Assess Current State

Examine this project:
- Run `ls -la` to see the structure
- Check if `.claude/` exists and what's in it
- Check if it's a git repository (`git status`)
- Identify project type (package.json, chapters/, src/, etc.)

Report findings briefly.

### Step 2: Check Existing Infrastructure

Check what infrastructure exists:

| Component | Purpose | Status |
|-----------|---------|--------|
| `.claude/settings.json` with permissions | Pre-approve commands | Check if exists |
| Stop hook in settings.json | Uncommitted reminders | Check if configured |
| `.claude/CLAUDE.md` (under 80 lines) | Project context | Check if exists |
| SessionStart hook | Git status display | Check if configured |
| `.github/workflows/claude-code.yml` | GitHub Actions | Check if exists |

Report: "This project currently has: [list what's found, or 'no infrastructure']"

**Then, analyze project characteristics for advanced features:**

- Does .github/workflows/ exist OR multiple contributors (check git log)? → Will recommend GitHub Actions
- Is this a documentation-only project tracking tools/versions? → Will recommend Version Tracking
- Otherwise → Standard setup is sufficient

### Step 3: Gather Project Info

Ask the user:

1. "What is the project name?" (suggest directory name as default)
2. "In 1-2 sentences, what is this project's purpose?"
3. "What's the primary focus?
   - **coding** - Software development
   - **writing** - Content creation
   - **research** - Analysis projects
   - **hybrid** - Mixed purpose"

Tell the user: "I'll now set up the recommended infrastructure (CLAUDE.md + hooks + permissions). This takes 15-30 minutes and provides consistent project context across sessions."

### Step 4: Component Best Practices Overview

**Before creating infrastructure, understand the 8 critical components** that external projects ask about:

#### 1. CLAUDE.md - Project Instructions
**Principle**: Keep ruthlessly minimal (~60 lines, 80 max)
- Include ONLY: Purpose (1-2 sentences), key commands, known gotchas, current focus
- **Quick start**: Run `/init` to auto-generate a starter CLAUDE.md from your project
- **Import files**: Use `@path/to/file` syntax to reference external docs
- **File-scoped rules**: Use `.claude/rules/` with `paths` frontmatter for language-specific guidelines
- ❌ **Don't**: Add tutorials, explain patterns, list all possible commands
- 📚 **Full guidance**: The Big 3 principle above

#### 2. Skills - Domain Knowledge & Workflows
**When to use**: Repeatable methodologies Claude should apply automatically
- ✅ **Use for**: Research workflows, code review checklists, domain-specific practices
- ❌ **Don't use for**: One-off commands (use natural language instead)
- 📊 **Economics**: Skills are 50% cheaper than MCP for methodology guidance
- 📚 **Full guidance**: [skills-domain-knowledge.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/skills-domain-knowledge.md)

#### 3. MCP (Model Context Protocol) - External Integrations
**When to use**: Connecting Claude to databases, APIs, external systems
- ✅ **Use for**: Decision support, development assistance, background analysis
- ❌ **Don't use for**: Transaction paths, real-time operations (300-800ms latency)
- ⚠️ **Security**: ~43% of MCP servers have command injection vulnerabilities (use official servers only)
- 📚 **Full guidance**: [mcp-patterns.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/mcp-patterns.md)

#### 4. Marketplace & Plugins - Distribution
**Official marketplaces**:
- `claude-plugins-official` - ~50 vetted plugins (recommended: update weekly)
- `claude-code-plugins` - Anthropic demo plugins

**Commands**:
```bash
/plugin marketplace update claude-plugins-official  # Weekly
/plugin marketplace list  # View available
```

**Quality checklist** before installing community plugins:
- [ ] Version pinned, maintained (<6 months old)
- [ ] README with examples
- [ ] Security audit if accessing external systems
- 📚 **Full guidance**: [plugins-and-extensions.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/plugins-and-extensions.md)

#### 5. Slash Commands vs Natural Language
**Anthropic guidance**: "Avoid complex slash command lists; natural language works well"
- ✅ **Use natural language**: "commit and push my changes"
- ✅ **Use `/btw`**: Side questions that don't pollute your context window
- ✅ **Use `/effort`**: Control reasoning effort level for current task
- ⚠️ **Use slash commands only for**: Explicit, repeatable actions with specific names
- ❌ **Don't create**: Custom commands for one-off tasks
- 📚 **Full guidance**: [project-infrastructure.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/project-infrastructure.md)

#### 6. Prompts (MAKE-PROJECT-RECOMMENDATIONS.md, etc.)
**This file is a prompt** - analyzes projects and recommends infrastructure
- Store in `prompts/` directory for discoverability
- Keep atomic: one clear purpose per prompt
- Version control: track changes to prompts like code
- 📚 **This file**: Example of well-structured prompt

#### 7. Tools (Built-in) - Bash, Read, Edit, etc.
**Prefer specialized tools over bash commands**:
- ✅ `Read` tool for reading files (not `cat`)
- ✅ `Edit` tool for editing (not `sed`)
- ✅ `Grep` tool for searching (not `grep` command)
- Reserve bash for: git operations, npm/python commands, docker
- 📚 **Full guidance**: [tool-ecosystem.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/tool-ecosystem.md)

#### 8. Browser Automation - Claude in Chrome
**Updated recommendation (as of 2026-03)**:
- ✅ **Use**: [Claude in Chrome](https://code.claude.com/docs/en/chrome) extension for live web debugging
- ✅ **Use**: Playwright CLI (4x more token-efficient for scripted testing)
- **When to use Chrome**: Interactive UI verification, visual testing
- **When to use Playwright**: Automated test suites, CI pipelines
- 📚 **Full guidance**: [tool-ecosystem.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/tool-ecosystem.md)

#### 9. Custom Subagents (`.claude/agents/`)
Define specialized agents with their own tools, model, and skills:
- ✅ **Use for**: Security review, code audit, documentation generation
- Define in `.claude/agents/agent-name.md` with frontmatter (name, description, tools, model)
- 📚 **Full guidance**: [subagent-orchestration.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/subagent-orchestration.md)

---

**Quick Reference Decision Tree**:

```
Need to...
├─ Document project context → CLAUDE.md (~60 lines) + .claude/rules/ for file-scoped
├─ Embed domain expertise → Skills
├─ Connect to external systems → MCP servers (decision support only)
├─ Share configurations with team → Plugins from marketplace
├─ Run specific workflows → Natural language first, slash commands if complex
├─ Automate browser tasks → Claude in Chrome (interactive) or Playwright CLI (scripted)
├─ Coordinate parallel work → Agent teams (experimental) or subagents
├─ Push external events in → Channels (Telegram, Discord, webhooks)
├─ Reuse setup instructions → Prompts (like this file)
└─ Work with files/system → Built-in tools (Read, Edit, Bash)
```

**Most Common Mistake**: Over-engineering with custom commands, complex MCP setups, or elaborate skills when CLAUDE.md + natural language would suffice. Start minimal.

---

### Step 5: Create Standard Infrastructure

#### Create `.claude/settings.json`

Detect the main branch name first (`git branch` or check remote). Use that in the Stop hook.

Create complete settings.json with all four components (permissions, Stop hook, SessionStart hook, project-specific tools):

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

#### Create `.claude/hooks/session-start.sh`

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

---

### Step 6: Assess Advanced Needs

**Tell the user**: "Your project now has the recommended setup (CLAUDE.md + hooks + permissions)."

**Ask the user**: "Do you need advanced features?"

Present options based on your analysis from Step 2:

**Option 1: GitHub Actions** (if multiple collaborators OR .github/workflows/ exists)
- Enables `@.claude` PR review comments
- Requires: ANTHROPIC_API_KEY in GitHub secrets
- Time: Additional 15-30 minutes

**Option 2: Version Tracking** (if documentation project with version/tool mentions)
- Auto-tracks tool/version mentions
- Monitors blog posts for ecosystem changes
- Time: Additional 30 minutes

**My recommendation**:
- [If .github/workflows/ exists or git log shows multiple authors]: "I recommend adding GitHub Actions - your project appears to be collaborative."
- [If project has patterns/ or docs/ with version mentions]: "I recommend considering Version Tracking - you're documenting technology."
- [Otherwise]: "Standard setup is sufficient for your project. You can always add these later."

Let the user choose: "Which would you like to add? (1, 2, both, or neither)"

---

### Step 7: Install Advanced Features (If Requested)

#### If GitHub Actions Selected

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

#### If Version Tracking Selected

Follow the complete setup from [QUICKSTART.md Advanced: Version Tracking](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/QUICKSTART.md#for-docs-projects-version-tracking-add-30-min) section. This includes:
- TOOLS-TRACKER.md
- Scripts (generate-tools-tracker.py, check-measurement-expiry.py, check-anthropic-rss.py, analyze-blog-post.py)
- GitHub Actions workflows
- Skills for pattern version updating

---

### Step 8: Summary

After creating files, summarize:

| Component | Status | Purpose |
|-----------|--------|---------|
| permissions.allow | ✅ Created | Pre-approved commands |
| Stop hook | ✅ Created | Uncommitted/unpushed reminders |
| CLAUDE.md | ✅ Created | Project context (~60 lines target) |
| SessionStart | ✅ Created | Context at session start |
| GitHub Actions | [✅ if added / ⏭️ skipped] | @.claude PR reviews |
| Version Tracking | [✅ if added / ⏭️ skipped] | Tool/version monitoring |

"Your project now has recommended infrastructure in place."

### Step 9: Explain Next Steps

For all projects:
1. **Review `.claude/CLAUDE.md` and ruthlessly trim** - Target ~60 lines, remove anything not preventing mistakes
2. **Remember to plan first** - Use `/plan` before starting any non-trivial feature work
3. Start new session to see SessionStart hook in action
4. After 1-2 weeks, audit CLAUDE.md again - delete sections that weren't needed

If GitHub Actions was added:
1. Add `ANTHROPIC_API_KEY` to GitHub repository secrets
2. Test by opening a PR and commenting `@.claude review this`

**Key Principle Reminder**: "Would removing this cause mistakes? If not, cut it." - Anthropic Official Docs

### Step 8: Point to Additional Resources (Based on User Needs)

If the user needs specific guidance, recommend:

**Common Issues?** → See [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md)
- CLAUDE.md keeps growing
- Overwhelmed by patterns
- Team resistance to adoption
- Hook configuration problems

**Want to learn patterns progressively?** → See [PATTERN-LEARNING-PATH.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/PATTERN-LEARNING-PATH.md)
- Start Here path (3 core patterns)
- Role-specific paths (Solo Dev, Team Lead, Production/Security, Researcher)
- Use-case paths (new project, improve existing, multi-session work)

**Migrating from existing setup?** → See [MIGRATION-GUIDE.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/MIGRATION-GUIDE.md)
- From Cursor/.cursorrules
- From existing .claude/ setup
- Team standardization strategies

**Need a specific pattern?** → See [Pattern Decision Matrix](https://github.com/flying-coyote/claude-code-project-best-practices#pattern-decision-matrix)
- "I Need To..." → pattern mapping
- All 36 patterns categorized

**Want to see complete examples?** → Browse [example projects](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/examples)
- coding-project: TypeScript library with full hooks
- writing-project: Technical blog with evidence tiers
- research-project: Literature review with hypothesis tracking

---

## Advanced: Version Tracking Setup Details (Optional - For Documentation Projects)

**When to Use**: Projects documenting rapidly evolving technologies (AI tools, frameworks, ecosystems)
**Time**: 30-45 minutes setup
**Benefit**: Always-current recommendations with automated monitoring and version tracking

**Note**: This section provides detailed setup instructions. For quick setup, see [QUICKSTART.md Advanced: Version Tracking](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/QUICKSTART.md#for-docs-projects-version-tracking-add-30-min).

### What Version Tracking Adds

**The Problem**: Technology evolves faster than manual documentation can track. By the time you notice an Anthropic blog post or tool update, weeks have passed. External projects fetching your docs get patterns without knowing if they're current.

**The Solution**: Automated information gathering + human editorial control

**What Gets Automated**:
- ✅ Daily parsing of patterns for tool/version mentions
- ✅ 6-hourly Anthropic blog RSS monitoring with AI analysis
- ✅ Version requirement extraction and tracking
- ✅ Measurement claim expiry detection (flag claims >1 year old)
- ✅ EMERGING pattern promotion monitoring

**What Stays Manual**:
- ✅ Editorial decisions (promotion, deprecation)
- ✅ Evidence tier assignments
- ✅ Pattern quality standards
- ✅ Quarterly strategic reviews

**Key Deliverable**: `TOOLS-TRACKER.md` - Living document with tool recommendations, version dependencies, and measurement claims (auto-updated daily)

---

### Setup Steps

#### 1. Tools Landscape Tracking (10 min)

**Create Foundation Files**:

1. **TOOLS-TRACKER.md** - Auto-generated daily, tracks:
   - All tool/pattern recommendations with status (RECOMMENDED, CONSIDER, EMERGING, DEPRECATED)
   - Version dependency matrix (feature → Claude Code version)
   - Measurement claims registry with expiry dates
   - Component coverage (CLAUDE.md, prompts, skills, tools, MCP, sub-agents, slash commands, marketplaces)

2. **DEPRECATIONS.md** - Manual edits, permanent record of:
   - Active deprecations with migration paths
   - Historical pattern evolution (case studies)
   - Re-evaluation schedule for EMERGING patterns
   - Grace periods (default: 90 days)

**Example TOOLS-TRACKER.md Structure**:
```markdown
## Component 1: CLAUDE.md Patterns
| Pattern | Status | Min Version | Evidence Tier | Last Verified |
|---------|--------|-------------|---------------|---------------|
| Semantic highway design | ✅ RECOMMENDED | v2.0.0+ | A | 2026-02-16 |

## Component 5: MCP
| MCP Pattern | Status | Evidence Tier | Key Measurement |
|-------------|--------|---------------|-----------------|
| MCP for decision support | ✅ RECOMMENDED | A | 300-800ms latency |

## Measurement Claims Registry
| Claim | Value | Source | Date | Revalidate |
|-------|-------|--------|------|------------|
| Memory Tool improvement | 39% | Anthropic | 2025-11-24 | 2026-11-24 |
```

**Copy Template**:
```bash
# In your project root
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TOOLS-TRACKER.md
curl -O https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/DEPRECATIONS.md
```

#### 2. Source Monitoring with Analysis (15 min)

**Install Automation Scripts**:

```bash
mkdir -p scripts .github/workflows

# Core parsing script (generates TOOLS-TRACKER.md daily)
curl -o scripts/generate-tools-tracker.py \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/generate-tools-tracker.py

# Measurement expiry checker
curl -o scripts/check-measurement-expiry.py \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/check-measurement-expiry.py

# RSS monitoring
curl -o scripts/check-anthropic-rss.py \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/check-anthropic-rss.py

# AI-powered blog analysis (requires ANTHROPIC_API_KEY)
curl -o scripts/analyze-blog-post.py \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/scripts/analyze-blog-post.py

# Install dependencies
pip install pyyaml requests anthropic
```

**Setup GitHub Actions Workflows**:

```bash
# Daily pattern parsing → TOOLS-TRACKER.md
curl -o .github/workflows/tools-evolution-tracker.yml \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.github/workflows/tools-evolution-tracker.yml

# 6-hourly blog monitoring with AI analysis
curl -o .github/workflows/anthropic-blog-rss.yml \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.github/workflows/anthropic-blog-rss.yml
```

**Configure Secrets** (GitHub repository settings):
- Add `ANTHROPIC_API_KEY` for blog post analysis
- Workflows create issues automatically when changes detected

**Customize for Your Domain**:
```python
# In scripts/generate-tools-tracker.py, update tool names:
self.tool_names = [
    "Your Tool 1", "Your Framework", "Your MCP Server",
    # ... adapt to your ecosystem
]

# In scripts/check-anthropic-rss.py, update RSS URL:
DEFAULT_RSS_URL = "https://your-vendor.com/rss.xml"
```

#### 3. Version Dependency Tracking (10 min)

**Add YAML Frontmatter to Pattern Files**:

Every pattern documenting version-specific features should include:

```yaml
---
version-requirements:
  claude-code: "v2.1.30+"  # Minimum version for this pattern
  model: "Opus 4.6+"       # If model-specific
measurement-claims:
  - claim: "85% token reduction"
    source: "Anthropic blog"
    date: "2025-11-24"
    revalidate: "2026-11-24"  # 1 year for benchmarks
status: "PRODUCTION"  # or EMERGING, DEPRECATED
last-verified: "2026-02-16"
---
```

**Pattern Frontmatter Strategy**:
- Start with patterns that mention versions (20-30% of files)
- Add measurement claims where benchmarks cited
- Use scripts to extract: `python scripts/generate-tools-tracker.py`

**Install Pattern Maintenance Skills**:

```bash
mkdir -p .claude/skills

# Skill: Update versions when new releases happen
curl -o .claude/skills/pattern-version-updater/SKILL.md \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.claude/skills/pattern-version-updater/SKILL.md

# Skill: Monitor EMERGING patterns for promotion
curl -o .claude/skills/emerging-pattern-monitor/SKILL.md \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/.claude/skills/emerging-pattern-monitor/SKILL.md
```

**Usage**:
- "Update pattern versions for v2.2.0 release"
- "Review emerging patterns for promotion"

#### 4. Measurement Expiry System (5 min)

**Enhance evidence-tiers.md** (or create if not exists):

Add section on measurement expiry:

```markdown
## Evidence Tiers for Rapidly Evolving Topics

### Measurement Expiry Guidelines
| Claim Type | Expiry Period | Re-validation Method |
|------------|---------------|----------------------|
| Performance benchmarks | 1 year | Re-run with current version |
| Feature availability | Until next major version | Verify in release notes |
| Security audit results | 6 months | Check for new CVEs |
```

**Update Quarterly Audit Checklist** (in DOGFOODING-GAPS.md or similar):

```markdown
### Rapid Evolution Tracking (Quarterly)
- [ ] Review all EMERGING patterns for promotion
- [ ] Verify no measurement claims past expiry
- [ ] Check DEPRECATIONS.md for patterns to archive
- [ ] Audit version-requirements vs current version
- [ ] Review automation-generated issues
- [ ] Verify TOOLS-TRACKER.md accuracy
```

---

### What You Get

**Daily Automation**:
- TOOLS-TRACKER.md updated automatically
- Issues created for expired measurements
- Version dependency matrix stays current

**6-Hourly Monitoring**:
- New blog posts detected within 6 hours
- AI analyzes content for relevant changes
- Issues created with structured recommendations

**Human-in-the-Loop**:
- Review issues → approve/reject changes
- Make editorial decisions on promotions
- Validate AI analysis accuracy

**Time Savings**:
| Task | Before | After |
|------|--------|-------|
| Find tool recommendation | 5-10 min (search 4 files) | <30 sec (TOOLS-TRACKER.md) |
| Detect Anthropic blog post | 7-14 days (manual) | <24 hours (automated) |
| Track version dependencies | Manual spreadsheet | Automated extraction |
| Flag outdated benchmarks | Never (no system) | Automatic (expiry tracking) |

---

### External Projects: Adaptation Guide

**For projects fetching MAKE-PROJECT-RECOMMENDATIONS.md**:

**What to Copy** (12 files total):
```bash
# Core tracking files
TOOLS-TRACKER.md           # Template (customize components)
DEPRECATIONS.md            # Template

# Automation scripts
scripts/generate-tools-tracker.py
scripts/check-measurement-expiry.py
scripts/check-anthropic-rss.py
scripts/analyze-blog-post.py

# Workflows
.github/workflows/tools-evolution-tracker.yml
.github/workflows/anthropic-blog-rss.yml

# Skills
.claude/skills/pattern-version-updater/SKILL.md
.claude/skills/emerging-pattern-monitor/SKILL.md
```

**How to Customize** (15 minutes):

1. **Update Component List** in TOOLS-TRACKER.md:
   ```markdown
   # Replace Claude Code components with yours
   - CLAUDE.md → YOUR_CONFIG.md
   - skills → your extension mechanism
   - MCP → your integration layer
   ```

2. **Update RSS Feed** in `check-anthropic-rss.py`:
   ```python
   DEFAULT_RSS_URL = "https://your-vendor.com/rss.xml"
   ```

3. **Update Tool Names** in `generate-tools-tracker.py`:
   ```python
   self.tool_names = [
       "Your Tool", "Your Framework", "Your MCP Server"
   ]
   ```

4. **Configure API Key** (GitHub Secrets):
   - `ANTHROPIC_API_KEY` for blog analysis (or use your LLM API)

5. **Test Manually**:
   ```bash
   python scripts/generate-tools-tracker.py
   python scripts/check-measurement-expiry.py
   ```

**Total Adaptation Time**: 45 minutes for complete system

---

### When NOT to Use Version Tracking

**Skip version tracking if**:
- Technology is stable (not rapid evolution)
- Project is code-only (not documentation)
- Manual quarterly reviews are sufficient
- Team prefers manual control over automation

**Version tracking is designed for**:
- Documentation projects tracking fast-moving ecosystems
- Best practices repositories (like this one)
- Technology comparison sites
- Framework recommendation engines

---

### Integration with Standard Setup

**Version tracking builds on the recommended setup**:
- ✅ Standard setup: CLAUDE.md (~60 lines), hooks, permissions still apply
- ✅ GitHub Actions: Can coordinate with new workflows if added
- ➕ Version tracking: Adds automation for living documentation

**Key Principle Preserved**: "Automation structures information; humans make decisions."

---

## Reference

**Core Principles**:
- [FOUNDATIONAL-PRINCIPLES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/FOUNDATIONAL-PRINCIPLES.md) - The Big 3 (read first)

**Onboarding & Help**:
- [TROUBLESHOOTING.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/TROUBLESHOOTING.md) - Common issues (CLAUDE.md bloat, setup problems, team adoption)
- [PATTERN-LEARNING-PATH.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/PATTERN-LEARNING-PATH.md) - Guided learning paths by role/use-case (36 patterns)
- [MIGRATION-GUIDE.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/MIGRATION-GUIDE.md) - Migrate from Cursor/.cursorrules or existing setups

**Key Patterns** (4 of 36):
- [spec-driven-development.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/spec-driven-development.md) - Specify → Plan → Tasks → Implement
- [context-engineering.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/context-engineering.md) - Deterministic vs probabilistic context
- [project-infrastructure.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/project-infrastructure.md) - Infrastructure setup details
- [evidence-tiers.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/evidence-tiers.md) - Source evaluation framework

**Finding Patterns**: See [README Pattern Decision Matrix](https://github.com/flying-coyote/claude-code-project-best-practices#pattern-decision-matrix) - "I Need To..." → pattern lookup for all 36 patterns

**Complete Examples** (full .claude/ implementations):
- [coding-project](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/examples/coding-project) - TypeScript library (19-line CLAUDE.md, complete hooks)
- [writing-project](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/examples/writing-project) - Technical blog (markdown linting, evidence tiers)
- [research-project](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/examples/research-project) - Literature review (hypothesis tracking)

**Sources**:
- [SOURCES-QUICK-REFERENCE.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/SOURCES-QUICK-REFERENCE.md) - Top 20 Tier A/B sources (fast lookup)
- [SOURCES.md](https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/SOURCES.md) - Complete database (1,278 lines, all attributions)

**Full Repository**: https://github.com/flying-coyote/claude-code-project-best-practices (36 patterns, 114 documents)
