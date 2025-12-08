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
- Move completed items to accomplishments
- Update current priorities
- Note any blockers

Commit: "📋 Weekly review [date]"
```

### /session:archive-and-update

`.claude/commands/session/archive-and-update.md`:
```markdown
Archive this session and prompt for documentation updates:

1. Summarize what was accomplished this session
2. Check if milestone was reached
3. If milestone: Update ARCHITECTURE.md and PLAN.md
4. If routine: Defer to weekly review
5. Archive session summary to .archive/conversations/
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
```

---

## Directory Structure

```
project/
├── ARCHITECTURE.md          # Strategic (manual)
├── PLAN.md                  # Tactical (manual)
├── INDEX.md                 # Structural (auto)
├── MAINTENANCE-GUIDE.md     # How to maintain docs
├── automation/
│   └── generate_index.py    # INDEX.md generator
└── .claude/
    └── commands/
        └── maintenance/
            ├── update-status.md
            └── weekly-review.md
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

## Related Patterns

- [Advanced Hooks](./advanced-hooks.md) - PostToolUse for INDEX.md automation
- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
