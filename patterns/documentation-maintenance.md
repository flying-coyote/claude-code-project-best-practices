# Documentation Maintenance System

**Source**: Production-validated pattern from 12+ projects
**Evidence Tier**: B (Production validated)

## The Core Problem

Documentation becomes stale during intensive work periods. CLAUDE.md files drift out of sync with reality. Manual maintenance is forgotten.

**Solution**: Three-document system with different update triggers and automated reminders.

---

## Three-Document Architecture

### 1. ARCHITECTURE.md - Strategic Context

**Purpose**: System design, directory structure, current phase
**Update Trigger**: Phase transitions, major milestones, infrastructure changes
**Owner**: Manual (requires human judgment)

**Contents**:
- Project structure and folder organization
- Key architectural decisions
- Current phase and status
- Integration patterns

**Update frequency**: Monthly or at major milestones

### 2. PLAN.md - Tactical Context

**Purpose**: Current priorities, immediate next actions, success metrics
**Update Trigger**: Weekly priority shifts, milestone completions
**Owner**: Manual (requires human judgment)

**Contents**:
- Current sprint/week focus
- Immediate next actions (prioritized)
- Success metrics
- Blockers and dependencies

**Update frequency**: Weekly

### 3. INDEX.md - Structural Context

**Purpose**: Automated document inventory with counts
**Update Trigger**: File structure changes
**Owner**: Automated via script

**Contents**:
- Directory listing with file counts
- Document categories
- Quick navigation

**Update frequency**: After every file change (automated)

---

## Implementation

### INDEX.md Automation

Create `automation/generate_index.py`:
```python
#!/usr/bin/env python3
"""Generate INDEX.md from current file structure."""

import os
from pathlib import Path
from datetime import datetime

def generate_index(root_dir: str, output_file: str):
    """Generate markdown index of directory structure."""

    content = [
        "# Project Index",
        "",
        f"*Auto-generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
    ]

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden and archive directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        if filenames:
            rel_path = os.path.relpath(dirpath, root_dir)
            md_files = [f for f in filenames if f.endswith('.md')]

            if md_files:
                content.append(f"## {rel_path}")
                content.append(f"*{len(md_files)} documents*")
                content.append("")
                for f in sorted(md_files):
                    content.append(f"- [{f}]({rel_path}/{f})")
                content.append("")

    with open(output_file, 'w') as f:
        f.write('\n'.join(content))

if __name__ == "__main__":
    generate_index(".", "INDEX.md")
```

### PostToolUse Hook

Auto-regenerate INDEX.md when files change (see [Advanced Hooks](./advanced-hooks.md)):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Bash|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 automation/generate_index.py"
          }
        ]
      }
    ]
  }
}
```

---

## Slash Commands for Maintenance

Create maintenance slash commands to prompt updates at natural checkpoints.

### /maintenance:update-status

`.claude/commands/maintenance/update-status.md`:
```markdown
Review the current state of documentation:

1. Read ARCHITECTURE.md - is the phase status current?
2. Read PLAN.md - do priorities reflect this week's focus?
3. Check git log for recent activity

If updates needed:
- Update phase status in ARCHITECTURE.md
- Refresh priorities in PLAN.md
- Commit changes with message: "📚 Documentation status update"

If current, confirm: "Documentation is current as of [date]"
```

### /maintenance:weekly-review

`.claude/commands/maintenance/weekly-review.md`:
```markdown
Conduct weekly maintenance review:

1. **Accomplishments**: What was completed this week?
2. **Blockers**: What's blocking progress?
3. **Next Week**: What are the priorities?

Update PLAN.md with:
- Add completed items to "Completed This Cycle" section
- Update current priorities
- Note any blockers
- Update "Last Updated" date

Commit: "📋 Weekly review [date]"
```

### /maintenance:archive-completed

`.claude/commands/maintenance/archive-completed.md`:
```markdown
Promote completed items from PLAN.md to ARCHIVE.md:

1. Review "Completed This Cycle" section in PLAN.md
2. Determine archive scope (version bump, feature, monthly rollup)
3. Add milestone section to ARCHIVE.md with dates and items
4. Clear PLAN.md "Completed This Cycle" table
5. Update metrics in both files
6. Commit and push: "📚 Archive completed work: [milestone]"
```

### /maintenance:end-session

`.claude/commands/maintenance/end-session.md`:
```markdown
End-of-session checklist:

Required:
- [ ] Completed items added to PLAN.md "Completed This Cycle"
- [ ] PLAN.md "Last Updated" date current
- [ ] Changes committed with emoji prefix

Recommended:
- [ ] Push to remote: git push origin master
- [ ] If milestone reached, run /maintenance:archive-completed
```

---

## Maintenance Philosophy

| Document | Staleness Risk | Mitigation |
|----------|---------------|------------|
| INDEX.md | None | Auto-generated |
| ARCHITECTURE.md | High | Monthly review, milestone triggers |
| PLAN.md | Medium | Weekly review, slash commands |

**Key insight**: Accept that manual docs will drift during intensive work. Use slash commands to prompt updates at natural checkpoints rather than expecting constant maintenance.

---

## Team CLAUDE.md Pattern

### Boris Cherny's Team Approach

> "Anytime we see Claude do something incorrectly we add it [to CLAUDE.md]... It's like team memory."
> — Boris Cherny, Claude Code Creator

### Multi-Weekly Update Cadence

**Recommended frequency**: 2-3 times per week (not just weekly)

**When to update CLAUDE.md**:
- After Claude makes a mistake → Document the correction immediately
- After a PR review catches an AI-generated issue → Add prevention rule
- After discovering a pattern works well → Codify it
- Before major feature work → Ensure context is current

### Mistake Capture Workflow

```markdown
## Mistakes to Avoid (Team Learning)

### [Date] - [Brief description]
**What happened**: Claude did X when it should have done Y
**Prevention**: [Rule to add to CLAUDE.md]

Example:
### 2026-01-08 - Import path confusion
**What happened**: Claude used relative imports (`../utils`) instead of absolute (`@/utils`)
**Prevention**: Always use absolute imports with `@/` prefix for src/ directory
```

### @.claude PR Tagging

For teams using GitHub Actions with Claude Code:

1. Tag PRs with `@.claude` in description or comments
2. Claude Code GitHub Action triggers review
3. Findings added to CLAUDE.md if significant

```markdown
## From PR Reviews

- **PR #142**: Don't use `any` type - prefer `unknown` with type guards
- **PR #156**: Always add loading states to async operations
- **PR #163**: Database queries need explicit timeouts
```

### Team CLAUDE.md Structure

```markdown
# CLAUDE.md

## Project Context
[Standard project-specific context]

## Team Conventions
[Coding standards, agreed patterns]

## Recent Learnings (Updated 2-3x/week)
[Mistakes captured as they happen]

## From PR Reviews
[Patterns discovered during code review]

## Integration Notes
[How this project connects to others]
```

### Best Practices

1. **Capture immediately** - Don't wait for weekly review
2. **Be specific** - Include the exact pattern/anti-pattern
3. **Date entries** - Track when learning occurred
4. **Prune regularly** - Move stable rules to conventions section

---

## Stop Hook Reminder

Add documentation currency check at session end:

```bash
#!/bin/bash
# Check if documentation needs updates

RECENT_COMMITS=$(git log --since="7 days ago" --oneline | wc -l)
ARCH_AGE=$(find ARCHITECTURE.md -mtime +7 2>/dev/null | wc -l)

if [ "$RECENT_COMMITS" -gt 0 ] && [ "$ARCH_AGE" -gt 0 ]; then
    echo "⚠️ Documentation may be stale. Consider: /maintenance:update-status"
fi

# Check for uncommitted changes
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
    UNCOMMITTED=$(git status --short 2>/dev/null | wc -l)
    echo "⚠️ $UNCOMMITTED uncommitted change(s) - consider committing"
fi

# Check for unpushed commits
UNPUSHED=$(git log origin/master..HEAD --oneline 2>/dev/null | wc -l)
if [ "$UNPUSHED" -gt 0 ]; then
    echo "⚠️ $UNPUSHED unpushed commit(s) - consider: git push origin master"
fi
```

---

## Directory Structure

```
project/
├── ARCHITECTURE.md          # Strategic (manual)
├── PLAN.md                  # Tactical (manual, with "Completed This Cycle" section)
├── ARCHIVE.md               # Historical milestones (promoted from PLAN.md)
├── INDEX.md                 # Structural (auto-generated)
├── automation/
│   └── generate_index.py    # INDEX.md generator
└── .claude/
    ├── hooks/
    │   └── stop-doc-check.sh    # Currency + uncommitted/unpushed reminders
    └── commands/
        └── maintenance/
            ├── update-status.md     # Ad-hoc documentation check
            ├── weekly-review.md     # Weekly cadence review
            ├── archive-completed.md # Promote to ARCHIVE.md
            └── end-session.md       # Session end checklist
```

---

## When to Use

**Good fit**:
- Projects with >20 documents
- Multi-week projects
- Projects with changing priorities
- Team projects needing shared context

**Overkill**:
- Small, stable projects
- Single-purpose utilities
- Short-term projects

---

## Anti-Patterns

### ❌ Manual INDEX.md Maintenance
**Problem**: Manually updating document indexes after file changes
**Symptom**: INDEX.md constantly out of sync, maintenance fatigue
**Solution**: Automate with PostToolUse hook and `generate_index.py` script

### ❌ Expecting Real-Time Doc Updates
**Problem**: Demanding documentation updates during intensive work periods
**Symptom**: Interruption fatigue, documentation updates abandoned
**Solution**: Accept drift during work; use slash commands at natural checkpoints

### ❌ Single Monolithic Doc
**Problem**: Maintaining one large document for all project context
**Symptom**: Information hard to find, staleness spread throughout
**Solution**: Three-document system (ARCHITECTURE, PLAN, INDEX) with different update triggers

### ❌ No Staleness Alerts
**Problem**: Letting documentation drift without any notification
**Symptom**: Outdated docs discovered only when causing problems
**Solution**: Stop hook reminder for docs older than 7 days with recent activity

---

## Related Patterns

- [Advanced Hooks](./advanced-hooks.md) - PostToolUse for INDEX.md automation
- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
- [Architecture Decision Records](./architecture-decision-records.md) - Decision history complements ARCHITECTURE.md

*Last updated: January 2026*
