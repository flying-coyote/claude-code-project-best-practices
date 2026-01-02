# Bootstrap New Project Prompt

Copy everything below the line and paste it into Claude Code to set up your project.

---

You are setting up AI-driven development infrastructure for this project using best practices from https://github.com/flying-coyote/claude-code-project-best-practices

This setup implements:
1. **Spec-driven development (SDD)** - The 4-phase model (Specify→Plan→Tasks→Implement)
2. **Claude Code infrastructure** - CLAUDE.md, hooks, skills
3. **Cross-platform patterns** - agentskills.io compliant where applicable

## Your Task

Create appropriate project infrastructure based on complexity. Follow these steps:

### Step 1: Assess the Project

First, examine this project:
- Run `ls -la` to see the structure
- Check if `.claude/` already exists
- Identify project type indicators (package.json, chapters/, src/, etc.)
- Check if it's a git repository

Report your findings briefly.

### Step 2: Ask About Project Type

Based on your assessment, recommend one of these presets and ask the user to confirm:

1. **coding** - Software development (libraries, tools, applications)
   - Quality focus: Clean code, TDD, conventional commits
   - Best for: Projects with package.json, Cargo.toml, pyproject.toml, go.mod

2. **writing** - Content creation (books, blogs, documentation)
   - Quality focus: Voice consistency, evidence-based claims, citations
   - Best for: Projects with chapters/, drafts/, markdown content

3. **research** - Analysis projects (studies, literature reviews)
   - Quality focus: Evidence tiers, hypothesis tracking, source attribution
   - Best for: Projects with concepts/, hypotheses/, bibliography/

4. **hybrid** - Mixed-purpose projects
   - Quality focus: Combined standards from above
   - Best for: Projects with src/ + docs/, or unclear categorization

Ask: "I recommend the **[preset]** preset for this project. Does that fit, or would you prefer a different one?"

### Step 3: Gather Project Information

Ask the user:

**Basic Info:**
1. "What is the name of this project?" (suggest the directory name as default)
2. "In 1-2 sentences, what is this project's purpose?"

**Complexity Assessment (determines SDD rigor):**
3. "How complex is this project?
   - **Simple**: Bug fixes, small features (<1 day) → Minimal setup
   - **Medium**: Features 1-3 days, few files → Lightweight SDD
   - **Complex**: Multi-day, multi-file, team project → Full SDD with specs/"

**SDD Artifacts (for medium/complex):**
4. "Do you want SDD artifacts?
   - `specs/` directory for feature requirements
   - `ARCHITECTURE.md` for system design
   - `DECISIONS.md` for rationale
   [Recommended for complex projects: Yes]"

**Claude Code Infrastructure:**
5. "Do you want a session-start hook? Shows git status and recent commits. [Recommended: Yes]"
6. "Do you have repeatable workflows? (e.g., debugging, code review, deployment) [If yes, we'll create agentskills.io-compliant skills]"
7. "Are there complex tasks that could run in parallel? (e.g., research, analysis) [If yes, we'll set up subagent definitions]"

### Step 4: Create the Infrastructure

Based on the answers, create:

#### For Complex Projects: SDD Artifacts

**Create `specs/README.md`** (if SDD artifacts requested):
```markdown
# Specifications

This directory contains feature specifications following the SDD Specify phase.

## Structure

```
specs/
├── README.md           # This file
├── feature-name/       # One directory per feature
│   ├── requirements.md # What to build and why
│   └── acceptance.md   # How to verify it's done
```

## Template

When adding a new feature, create `specs/<feature-name>/requirements.md`:

```markdown
# [Feature Name]

## Summary
[1-2 sentence description]

## User Stories
- As a [role], I want [capability] so that [benefit]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Out of Scope
- [What this does NOT include]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```
```

**Create `ARCHITECTURE.md`** (if SDD artifacts requested):
```markdown
# Architecture

## Overview
[High-level system description]

## Key Components
- **Component 1**: [Description]
- **Component 2**: [Description]

## Technology Choices
| Area | Choice | Rationale |
|------|--------|-----------|
| Language | [X] | [Why] |
| Framework | [X] | [Why] |

## Constraints
- [Constraint 1]
- [Constraint 2]
```

**Create `DECISIONS.md`** (if SDD artifacts requested):
```markdown
# Design Decisions

## Decision 1: [Title]

### Context
[What prompted this decision]

### Options Considered
| Option | Pros | Cons |
|--------|------|------|
| A | ... | ... |
| B | ... | ... |

### Decision
[What we chose and why]

### Consequences
[What this means going forward]
```

#### Always Create: `.claude/CLAUDE.md`

Use this structure, customized for the preset:

**Note**: The template below uses placeholder syntax for clarity. Replace `[PLACEHOLDER]` values with actual content when creating the file.

```markdown
# [PROJECT_NAME] Project Context

## Project Purpose

[USER'S DESCRIPTION]

## Current Phase

Active development

## Code Quality Standards

[PRESET-SPECIFIC STANDARDS - see below]

## Thinking Methodology

For deep analysis, use the FRAME-ANALYZE-SYNTHESIZE approach:
- **FRAME**: Define problem, identify assumptions, clarify success criteria
- **ANALYZE**: Evaluate alternatives, identify failure modes, assess trade-offs
- **SYNTHESIZE**: Recommend approach, document rationale, plan implementation

## Git Workflow

Commit messages follow conventional format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks
```

**Preset-specific quality standards:**

For **coding**:
```
- Write clean, maintainable code with clear intent
- Test-driven development where applicable
- Meaningful commit messages following conventional format
- No premature optimization
- Avoid over-engineering - only make requested changes
```

For **writing**:
```
- Evidence-based claims with documented sources
- Balanced perspective acknowledging trade-offs
- Consistent voice and tone throughout
- Intellectual honesty over marketing claims
```

For **research**:
```
- Evidence tier classification for all claims (Tier A-D)
- Hypothesis tracking with confidence levels
- Source attribution and citation
- Document contradictions and limitations
```

For **hybrid**:
```
- Clean code with clear intent
- Evidence-based claims with sources
- Balanced perspective on trade-offs
- Meaningful commit messages
```

#### If Session Hook Requested: Create `.claude/settings.json`

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
    ]
  }
}
```

#### If Session Hook Requested: Create `.claude/hooks/session-start.sh`

```bash
#!/bin/bash
# Session start hook - shows project context
# Based on Anthropic's "verify before work" pattern

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

PROJECT_NAME=$(basename "$PROJECT_ROOT")

# Git context
if [ -d ".git" ]; then
    BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
    UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    RECENT=$(git log --oneline -3 2>/dev/null || echo "No commits yet")
else
    BRANCH="N/A"
    UNCOMMITTED="N/A"
    RECENT="Not a git repository"
fi

cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$PROJECT_NAME - Session Context

Branch: $BRANCH
Uncommitted: $UNCOMMITTED files

Recent commits:
$RECENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Warn about uncommitted changes
if [ "$UNCOMMITTED" != "N/A" ] && [ "$UNCOMMITTED" -gt 0 ]; then
    echo ""
    echo "⚠️  $UNCOMMITTED uncommitted files - review before new work"
fi

exit 0
```

Make the hook executable: `chmod +x .claude/hooks/session-start.sh`

### Step 5: Explain What Was Created

After creating the files, explain:
1. What each file does
2. How Claude will use them
3. How to customize further if needed

### Step 6: Suggest Next Steps

Recommend:
1. Review `.claude/CLAUDE.md` and add any project-specific context
2. Start a new Claude Code session to see the hook in action (if installed)
3. Consider adding a `.claude/settings.local.json` for tool permissions

### Step 7: Explain Extension Options

Briefly explain the extension mechanisms available for future customization:

"As your project evolves, you can extend Claude Code with:

| Need | Solution | Location |
|------|----------|----------|
| Repeatable methodologies | **Skill** | `.claude/skills/` |
| User-initiated actions | **Slash Command** | `.claude/commands/` |
| External API/database access | **MCP Server** | Configure in `settings.json` |
| Automatic enforcement | **Hook** | `.claude/hooks/` |
| Team distribution | **Plugin** | Package all of the above |

**Quick decision**: If it's a *methodology* Claude should follow → Skill. If it needs *external data* → MCP."

---

## Reference

For more information, see:
- Full documentation: https://github.com/flying-coyote/claude-code-project-best-practices
- Extension mechanisms guide: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/patterns/plugins-and-extensions.md
- Design decisions: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/DECISIONS.md
- Pattern sources: https://github.com/flying-coyote/claude-code-project-best-practices/blob/main/SOURCES.md
