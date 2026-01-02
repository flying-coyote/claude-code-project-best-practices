# Audit Existing Project Prompt

Copy everything below the line and paste it into Claude Code to review your project against AI-driven development best practices.

---

You are auditing this project against AI-driven development best practices from https://github.com/flying-coyote/claude-code-project-best-practices

This audit evaluates:
1. **Spec-driven development (SDD)** alignment with the 4-phase model
2. **Claude Code infrastructure** (CLAUDE.md, hooks, skills, MCP)
3. **Cross-platform compatibility** (agentskills.io, tool-agnostic patterns)
4. **Security posture** (MCP security, hook safety)

## Your Task

Analyze this project's current state and provide actionable recommendations for improvement.

### Step 1: Assess Current State

Examine the project for both SDD artifacts and Claude Code infrastructure:

```bash
# === SDD ARTIFACTS (Specify/Plan/Tasks phases) ===

# Check for specs directory (Specify phase)
ls -la specs/ 2>/dev/null || echo "No specs/ directory"

# Check for architecture/design docs (Plan phase)
ls ARCHITECTURE.md DECISIONS.md 2>/dev/null || echo "No architecture docs"

# Check for task tracking (Tasks phase)
ls PLAN.md tasks.json 2>/dev/null || echo "No task tracking files"

# === CLAUDE CODE INFRASTRUCTURE ===

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

# Check for subagent definitions
ls -la .claude/agents/ 2>/dev/null || echo "No subagent definitions"

# Check for MCP configuration
cat .claude/settings.json 2>/dev/null | grep -A10 "mcpServers" || echo "No MCP servers configured"

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
**Complexity**: [simple/medium/complex] - determines SDD rigor needed

### SDD Phase Alignment

| Phase | Artifacts | Status | Notes |
|-------|-----------|--------|-------|
| **Specify** | specs/, CLAUDE.md, requirements | ✅/⚠️/❌ | |
| **Plan** | ARCHITECTURE.md, DECISIONS.md | ✅/⚠️/❌ | |
| **Tasks** | PLAN.md, task files, TodoWrite | ✅/⚠️/❌ | |
| **Implement** | Skills, hooks, git commits | ✅/⚠️/❌ | |

**SDD Recommendation**: [Full 4-phase / Lightweight / Minimal based on complexity]

### Claude Code Infrastructure

| Component | Status | Notes |
|-----------|--------|-------|
| .claude/ directory | ✅ Present / ❌ Missing | |
| CLAUDE.md | ✅ Present / ❌ Missing / ⚠️ Incomplete | |
| settings.json | ✅ Present / ❌ Missing | |
| Session hook | ✅ Present / ❌ Missing | |
| Skills | ✅ [count] / ❌ None | agentskills.io compliant? |
| Slash commands | ✅ [count] / ❌ None | |
| Subagents | ✅ Defined / ❌ None | Parallelization opportunities? |
| MCP servers | ✅ [count] / ❌ None | Security reviewed? |
| Git repository | ✅ Yes / ❌ No | |

### Security Assessment

| Check | Status | Notes |
|-------|--------|-------|
| MCP servers from trusted sources | ✅/❌ | |
| No hardcoded credentials | ✅/❌ | |
| Hooks validate inputs | ✅/❌ | |
| Skills have allowed-tools scoped | ✅/❌ | |

### Recommendations

[Prioritized list of recommendations]

### Implementation Plan

[Specific steps to implement recommendations]
```

### Step 4: Evaluate Against Best Practices

Check for these best practices:

#### SDD Phase Alignment (NEW)

**Determine project complexity first:**
- **Simple** (bug fixes, small features <1 day): Minimal SDD needed
- **Medium** (features 1-3 days): Lightweight SDD (combine Specify+Plan)
- **Complex** (multi-day, multi-file, team): Full 4-phase SDD

**For complex projects, check:**
- [ ] Has specs/ or requirements documentation (Specify phase)
- [ ] Has ARCHITECTURE.md or design docs (Plan phase)
- [ ] Has PLAN.md or task tracking (Tasks phase)
- [ ] Follows one-feature-at-a-time pattern (Implement phase)
- [ ] Uses git commits as checkpoints

#### Subagent Readiness (NEW)
- [ ] Complex tasks identified that could benefit from parallelization
- [ ] Context isolation opportunities considered
- [ ] Subagent definitions present (if applicable)
- [ ] Non-destructive tasks (research, analysis) use subagents

#### CLAUDE.md Quality
- [ ] Has clear project purpose
- [ ] Describes current phase/status
- [ ] References SDD phase if applicable
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
- [ ] **NEW**: Follows agentskills.io format (SKILL.md with YAML frontmatter)
- [ ] **NEW**: Instructions under 5000 tokens (recommended)
- [ ] **NEW**: Scripts in scripts/ are self-contained

**MCP Security Review** (if present) - Based on OWASP guidance:
- [ ] MCP is used for connectivity, not methodology
- [ ] Not placed in latency-sensitive paths
- [ ] **Security checks:**
  - [ ] Servers from known/trusted sources only
  - [ ] No hardcoded credentials in config (use env vars)
  - [ ] Minimal permissions per server (least privilege)
  - [ ] Human-in-the-loop for sensitive operations
  - [ ] No exposed API keys in settings.json
  - [ ] Consider sandboxing for local MCP servers

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

**Critical** (security issues):
- MCP servers with hardcoded credentials → Move to env vars
- MCP servers from untrusted sources → Remove or verify
- Hooks that don't validate inputs → Add validation

**High Priority** (do first):
- Missing CLAUDE.md → Create one
- CLAUDE.md missing project purpose → Add it
- No quality standards → Add preset-appropriate standards
- **NEW**: Complex project without SDD artifacts → Add specs/, ARCHITECTURE.md

**Medium Priority** (do next):
- No session hook → Consider adding
- Incomplete CLAUDE.md sections → Fill in
- Outdated information → Update
- **NEW**: Skills not agentskills.io compliant → Update format
- **NEW**: Parallelizable tasks not using subagents → Add subagent definitions

**Low Priority** (nice to have):
- Could add more context
- Could add slash commands for common workflows
- Could add project-specific skills for repeatable methodologies
- Could add MCP servers for external integrations
- **NEW**: Could add DECISIONS.md for architectural rationale

**Extension Mechanism Misuse** (fix if found):
- Skill used where MCP needed (external data access)
- MCP used where Skill needed (teaching methodology)
- Hook doing what should be a Skill (complex analysis)
- Slash command that should auto-activate (make it a Skill instead)

**SDD Rigor Mismatch** (fix if found):
- Complex project with no specs → Add specs/ directory
- Simple project over-specified → Simplify, remove overhead
- Missing Plan phase for team project → Add ARCHITECTURE.md

### Step 6: Offer to Implement

After presenting the report, ask:

"Would you like me to implement any of these recommendations? I can:

**SDD Artifacts:**
1. Create specs/ directory with template
2. Create ARCHITECTURE.md
3. Create DECISIONS.md with initial decisions
4. Create PLAN.md for task tracking

**Claude Code Infrastructure:**
5. Create missing core files (CLAUDE.md, settings.json)
6. Update existing CLAUDE.md
7. Add session hook
8. Create a skill for a repeatable workflow (agentskills.io compliant)
9. Add a slash command for a common action
10. Define subagents for parallelizable tasks

**Quick Options:**
- **A**: All SDD artifacts (1-4)
- **B**: All Claude Code infrastructure (5-7)
- **C**: Full setup (A + B)

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

**This Repository:**
- Full documentation: https://github.com/flying-coyote/claude-code-project-best-practices
- SDD methodology: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/patterns/spec-driven-development.md
- Extension mechanisms: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/patterns/plugins-and-extensions.md
- Design decisions: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/DECISIONS.md

**Industry Standards:**
- GitHub Spec Kit (SDD reference): https://github.com/github/spec-kit
- Agent Skills specification: https://agentskills.io/specification
- OWASP MCP Security Guide: https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/

**Claude Code Docs:**
- Subagents: https://code.claude.com/docs/en/sub-agents
- Hooks: https://code.claude.com/docs/en/hooks-guide
