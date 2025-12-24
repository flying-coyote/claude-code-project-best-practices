# Audit Existing Project Prompt

Copy everything below the line and paste it into Claude Code to review your project against best practices.

---

You are auditing this project's Claude Code infrastructure against best practices from https://github.com/flying-coyote/claude-code-project-best-practices

## Your Task

Analyze this project's current state and provide actionable recommendations for improvement.

### Step 1: Assess Current State

Examine the project:

```bash
# Project structure
ls -la

# Check for .claude directory
ls -la .claude/ 2>/dev/null || echo "No .claude directory"

# Check for CLAUDE.md
cat .claude/CLAUDE.md 2>/dev/null || echo "No CLAUDE.md"

# Check for hooks
ls -la .claude/hooks/ 2>/dev/null || echo "No hooks directory"

# Check for skills
ls -la .claude/skills/ 2>/dev/null || echo "No skills directory"

# Check for commands (slash commands)
ls -la .claude/commands/ 2>/dev/null || echo "No commands directory"

# Check for MCP configuration
cat .claude/settings.json 2>/dev/null | grep -A5 "mcpServers" || echo "No MCP servers configured"

# Check git status
git status 2>/dev/null || echo "Not a git repository"
```

### Step 2: Identify Project Type

Based on what you see, classify this project:
- **coding**: Has package.json, Cargo.toml, pyproject.toml, go.mod, src/
- **writing**: Has chapters/, drafts/, lots of markdown, book structure
- **research**: Has concepts/, hypotheses/, bibliography/, analysis/
- **hybrid**: Mix of the above, or unclear

### Step 3: Generate Audit Report

Create a report with this structure:

```markdown
## Project Audit Report

**Project**: [name]
**Type**: [coding/writing/research/hybrid]
**Date**: [today]

### Current State

| Component | Status | Notes |
|-----------|--------|-------|
| .claude/ directory | ✅ Present / ❌ Missing | |
| CLAUDE.md | ✅ Present / ❌ Missing / ⚠️ Incomplete | |
| settings.json | ✅ Present / ❌ Missing | |
| Session hook | ✅ Present / ❌ Missing | |
| Skills | ✅ Present / ❌ None | Count if present |
| Slash commands | ✅ Present / ❌ None | Count if present |
| MCP servers | ✅ Configured / ❌ None | List if present |
| Git repository | ✅ Yes / ❌ No | |

### Recommendations

[Prioritized list of recommendations]

### Implementation Plan

[Specific steps to implement recommendations]
```

### Step 4: Evaluate Against Best Practices

Check for these best practices:

#### CLAUDE.md Quality
- [ ] Has clear project purpose
- [ ] Describes current phase/status
- [ ] Includes quality standards appropriate for project type
- [ ] Has git workflow conventions
- [ ] Is concise (not overwhelming)

#### Session Hook (if present)
- [ ] Shows git branch
- [ ] Shows uncommitted changes count
- [ ] Shows recent commits
- [ ] Warns about potential issues
- [ ] Is non-blocking (exits 0)

#### Settings Configuration
- [ ] Hooks are properly configured
- [ ] Permissions are appropriately scoped (if settings.local.json exists)

#### Extension Mechanisms (if present)

Evaluate whether the right extension mechanism is used for each need:

| Need | Recommended | Check |
|------|-------------|-------|
| External API/database access | MCP Server | Is MCP used appropriately? |
| Repeatable methodologies | Skill | Are skills focused and context-aware? |
| User-initiated actions | Slash Command | Are commands explicit and discoverable? |
| Automatic enforcement | Hook | Are hooks non-blocking and scoped? |
| Team distribution | Plugin | Is plugin versioned and documented? |

**Skills Review** (if present):
- [ ] Each skill is focused (one methodology per skill)
- [ ] Descriptions are third-person (required for auto-activation)
- [ ] "DO NOT ACTIVATE" conditions are documented
- [ ] allowed-tools are appropriately scoped

**MCP Review** (if present):
- [ ] MCP is used for connectivity, not methodology
- [ ] Not placed in latency-sensitive paths
- [ ] Minimal permissions per server
- [ ] Known/trusted sources only

#### Project-Specific Concerns

For **coding** projects:
- [ ] Mentions testing approach
- [ ] Has commit message conventions
- [ ] Addresses code quality standards

For **writing** projects:
- [ ] Mentions voice/tone consistency
- [ ] Has citation/evidence standards
- [ ] Addresses publication quality

For **research** projects:
- [ ] Has evidence tier system
- [ ] Tracks hypotheses or research questions
- [ ] Documents sources and methodology

### Step 5: Prioritize Recommendations

Rank recommendations by impact:

**High Priority** (do first):
- Missing CLAUDE.md → Create one
- CLAUDE.md missing project purpose → Add it
- No quality standards → Add preset-appropriate standards

**Medium Priority** (do next):
- No session hook → Consider adding
- Incomplete CLAUDE.md sections → Fill in
- Outdated information → Update

**Low Priority** (nice to have):
- Could add more context
- Could add slash commands for common workflows
- Could add project-specific skills for repeatable methodologies
- Could add MCP servers for external integrations

**Extension Mechanism Misuse** (fix if found):
- Skill used where MCP needed (external data access)
- MCP used where Skill needed (teaching methodology)
- Hook doing what should be a Skill (complex analysis)
- Slash command that should auto-activate (make it a Skill instead)

### Step 6: Offer to Implement

After presenting the report, ask:

"Would you like me to implement any of these recommendations? I can:
1. Create missing core files (CLAUDE.md, settings.json)
2. Update existing CLAUDE.md
3. Add session hook
4. Create a skill for a repeatable workflow you have
5. Add a slash command for a common action
6. All core infrastructure (options 1-3)

Which would you like me to do?"

### Step 7: Implement Approved Changes

If the user approves changes:
1. Show what will be created/modified
2. Create/update files
3. Verify the changes work
4. Summarize what was done

### Best Practice Templates

Use these when creating or updating files:

#### Minimal CLAUDE.md (if missing)
```markdown
# [PROJECT_NAME] Project Context

## Project Purpose

[Describe what this project does and why it exists]

## Current Phase

[Active development / Maintenance / etc.]

## Code Quality Standards

[Appropriate standards for project type]

## Git Workflow

Commit messages follow conventional format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation
- `refactor:` Refactoring
- `test:` Tests
- `chore:` Maintenance
```

#### Session Hook (if adding)
```bash
#!/bin/bash
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

PROJECT_NAME=$(basename "$PROJECT_ROOT")

if [ -d ".git" ]; then
    BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
    UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    RECENT=$(git log --oneline -3 2>/dev/null || echo "No commits")
else
    BRANCH="N/A"; UNCOMMITTED="N/A"; RECENT="Not a git repo"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "$PROJECT_NAME | Branch: $BRANCH | Uncommitted: $UNCOMMITTED"
echo ""
echo "$RECENT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

exit 0
```

---

## Reference

For more information, see:
- Full documentation: https://github.com/flying-coyote/claude-code-project-best-practices
- Extension mechanisms guide: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/patterns/plugins-and-extensions.md
- Design decisions: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/DECISIONS.md
- Pattern sources: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/SOURCES.md
