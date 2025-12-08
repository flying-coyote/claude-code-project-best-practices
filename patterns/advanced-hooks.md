# Advanced Hook Patterns

**Source**: Production-validated patterns from 12+ projects
**Evidence Tier**: B (Production validated with measured outcomes)

## Beyond SessionStart

Most Claude Code users only implement SessionStart hooks. Advanced patterns leverage other hook types for powerful automation.

---

## Hook Priority Matrix

| Hook | Value | Effort | Best For |
|------|-------|--------|----------|
| **SessionStart** | HIGH | LOW | Context loading, environment setup |
| **PostToolUse** | HIGH | MEDIUM | Auto-regeneration, validation |
| **Stop** | MEDIUM | LOW | Documentation reminders |
| **UserPromptSubmit** | MEDIUM | HIGH | Skill activation hints |
| **PreToolUse** | LOW | LOW | Security gates |

---

## Hook 1: PostToolUse - Auto-Regenerate Documentation

**Purpose**: Automatically update documentation when file structure changes

**When it fires**: After Write, Edit, Bash, or NotebookEdit operations

**Use cases**:
- Regenerate INDEX.md after file changes
- Update dependency lists after package changes
- Rebuild documentation indexes

### Implementation

`.claude/hooks/post-tool-use-index.sh`:
```bash
#!/bin/bash
# Auto-regenerate INDEX.md when file structure changes

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# Read hook input (JSON from stdin)
read -r input
TOOL=$(echo "$input" | jq -r '.tool // "unknown"')
EXIT_CODE=$(echo "$input" | jq -r '.result.exitCode // 0')

# Only proceed if tool succeeded
if [ "$EXIT_CODE" -ne 0 ]; then
    exit 0
fi

# Check if file structure changed
STRUCTURE_CHANGED=false

case "$TOOL" in
    "Write"|"NotebookEdit")
        STRUCTURE_CHANGED=true
        ;;
    "Bash")
        COMMAND=$(echo "$input" | jq -r '.parameters.command // ""')
        if [[ "$COMMAND" =~ ^(mkdir|mv|cp|rm) ]]; then
            STRUCTURE_CHANGED=true
        fi
        ;;
esac

# Regenerate if needed
if [ "$STRUCTURE_CHANGED" = true ]; then
    python3 automation/generate_index.py > /dev/null 2>&1

    if ! git diff --quiet INDEX.md 2>/dev/null; then
        echo "✅ INDEX.md automatically regenerated"
    fi
fi

exit 0  # Non-blocking
```

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Bash|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-tool-use-index.sh"
          }
        ]
      }
    ]
  }
}
```

**Benefits**:
- Never manually regenerate documentation
- Always-current file indexes
- Silent when no changes

---

## Hook 2: Stop - Documentation Currency Check

**Purpose**: Remind about stale documentation before session ends

**When it fires**: When Claude finishes responding

**Use cases**:
- Weekly documentation maintenance reminders
- Prevent documentation drift
- Prompt for architecture updates

### Implementation

`.claude/hooks/stop-doc-check.sh`:
```bash
#!/bin/bash
# Check documentation currency before session end

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# Check recent activity
RECENT_COMMITS=$(git log --since="7 days ago" --oneline 2>/dev/null | wc -l)

if [ "$RECENT_COMMITS" -eq 0 ]; then
    exit 0  # No recent activity
fi

# Check last modification of key docs
ARCH_AGE=$(find ARCHITECTURE.md -mtime +7 2>/dev/null | wc -l)
PLAN_AGE=$(find PLAN.md -mtime +7 2>/dev/null | wc -l)

if [ "$ARCH_AGE" -gt 0 ] || [ "$PLAN_AGE" -gt 0 ]; then
    cat <<EOF

⚠️  Documentation Currency Check

Recent activity: $RECENT_COMMITS commits in past 7 days
Key docs may be stale (>7 days since update)

Consider: /maintenance:update-status

EOF
fi

exit 0  # Non-blocking reminder
```

### Configuration

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/stop-doc-check.sh"
          }
        ]
      }
    ]
  }
}
```

**Benefits**:
- Automated maintenance reminders
- Non-blocking (just a reminder)
- Prevents documentation drift

---

## Hook 3: UserPromptSubmit - Skill Activation Hints

**Purpose**: Suggest skill activation based on prompt patterns

**When it fires**: Before every user prompt is processed

**Use cases**:
- Hint when contradiction-detector should activate
- Suggest hypothesis validation
- Recommend publication checklist

### Implementation

`.claude/hooks/user-prompt-submit.py`:
```python
#!/usr/bin/env python3
import json
import sys
import re

try:
    hook_input = json.load(sys.stdin)
    prompt = hook_input.get('prompt', '')
except:
    sys.exit(0)

suggestions = []

# Absolute claims → contradiction-detector
if re.search(r'\b(always|never|definitely|best practice)\b', prompt, re.I):
    suggestions.append("💡 Absolute claim → contradiction-detector may activate")

# Hypothesis language → hypothesis-validator
if re.search(r'\b(I hypothesize|validate this claim)\b', prompt, re.I):
    suggestions.append("💡 Hypothesis → hypothesis-validator may activate")

# Publication intent → publication-quality-checker
if re.search(r'\b(publish|blog post|review for publication)\b', prompt, re.I):
    suggestions.append("💡 Publication → publication-quality-checker may activate")

if suggestions:
    hook_input['prompt'] += "\n\n" + "\n".join(suggestions)

print(json.dumps(hook_input))
sys.exit(0)
```

### Configuration

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/user-prompt-submit.py"
          }
        ]
      }
    ]
  }
}
```

**Note**: This is optional and higher effort. Only implement if skill activation needs are complex.

---

## Hook 4: PreToolUse - Security Gate

**Purpose**: Block dangerous operations before execution

**When it fires**: Before any tool is executed

**Use cases**:
- Block `rm -rf /` and similar
- Prevent accidental force pushes
- Gate sensitive operations

### Implementation

`.claude/hooks/pre-tool-use-security.sh`:
```bash
#!/bin/bash
# Security gate for dangerous commands

read -r input
TOOL=$(echo "$input" | jq -r '.tool // "unknown"')

if [ "$TOOL" = "Bash" ]; then
    COMMAND=$(echo "$input" | jq -r '.parameters.command // ""')

    # Block dangerous patterns
    if [[ "$COMMAND" =~ "rm -rf /" ]] || \
       [[ "$COMMAND" =~ "git push --force" ]] || \
       [[ "$COMMAND" =~ "> /dev/sd" ]]; then
        echo "🛑 Blocked dangerous command: $COMMAND"
        exit 2  # Block tool execution
    fi
fi

exit 0  # Allow
```

---

## Combined Configuration

Full `settings.json` with all hooks:

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
    "PostToolUse": [
      {
        "matcher": "Write|Bash|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-tool-use-index.sh"
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
            "command": "bash .claude/hooks/stop-doc-check.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Implementation Priority

1. **Start with SessionStart** - Immediate value, low effort
2. **Add PostToolUse** - High value for documentation automation
3. **Add Stop** - Medium value for maintenance reminders
4. **Consider UserPromptSubmit** - Only if needed (high effort)
5. **Add PreToolUse** - Only for security-sensitive projects

---

## Related Patterns

- [Long-Running Agent](./long-running-agent.md) - Verify before work startup protocol
- [Documentation Maintenance](./documentation-maintenance.md) - Three-document system
