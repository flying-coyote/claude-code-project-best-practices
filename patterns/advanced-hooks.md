# Advanced Hook Patterns

**Source**: Production-validated patterns + [Claude Code Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
**Evidence Tier**: A (Primary vendor documentation) + B (Production validated)

## SDD Phase Alignment

**Phase**: Implement (quality gates, automation)

Hooks enforce quality at implementation time:
- **PreToolUse**: Validate/modify inputs before execution
- **PostToolUse**: Verify/format outputs after execution
- **Stop**: Ensure documentation/checkpoints before session end

---

## Hook Events Overview

| Hook | When Fires | Can Block | Can Modify | Min Version |
|------|-----------|-----------|------------|-------------|
| **SessionStart** | Session begins | No | Context | - |
| **PreToolUse** | Before tool execution | ✅ Yes | ✅ Inputs (v2.0.10+) | - |
| **PostToolUse** | After tool completion | No | Output display | - |
| **UserPromptSubmit** | User submits prompt | No | Prompt text | - |
| **PermissionRequest** | Permission needed | ✅ Yes | Response | v2.0.45+ |
| **Stop** | Agent finishes turn | ✅ Continue | - | - |
| **SubagentStop** | Subagent finishes | No | - | v1.0.41+ |
| **SessionEnd** | Session terminates | No | - | - |

---

## Hook Priority Matrix

| Hook | Value | Effort | Best For |
|------|-------|--------|----------|
| **SessionStart** | HIGH | LOW | Context loading, environment setup |
| **PostToolUse** | HIGH | MEDIUM | Auto-regeneration, validation |
| **PreToolUse** | HIGH | MEDIUM | Input modification, security gates (v2.0.10+) |
| **Stop** | MEDIUM | LOW | Documentation reminders |
| **UserPromptSubmit** | MEDIUM | HIGH | Skill activation hints |

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

## Hook 4: PreToolUse - Security Gate and Input Modification

**Purpose**: Block dangerous operations OR modify inputs before execution

**When it fires**: Before any tool is executed

**Capabilities** (v2.0.10+):
- **Block**: Return exit code 2 to prevent execution
- **Modify**: Return JSON with `updatedInput` to change tool parameters
- **Allow**: Return exit code 0 to proceed unchanged

**Use cases**:
- Block `rm -rf /` and similar dangerous commands
- Prevent accidental force pushes
- Auto-add `--dry-run` flags to destructive operations
- Enforce commit message conventions
- Redirect file paths to sandboxed locations

### Implementation: Security Gate (Block)

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

### Implementation: Input Modification (v2.0.10+)

`.claude/hooks/pre-tool-use-modify.py`:
```python
#!/usr/bin/env python3
"""
PreToolUse hook that modifies tool inputs before execution.
Requires Claude Code v2.0.10+
"""
import json
import sys

try:
    hook_input = json.load(sys.stdin)
    tool = hook_input.get('tool', '')
    params = hook_input.get('parameters', {})
except:
    sys.exit(0)  # Allow on parse error

modified = False

# Example: Auto-add dry-run to destructive git commands
if tool == 'Bash':
    command = params.get('command', '')

    # Add --dry-run to git clean
    if 'git clean' in command and '--dry-run' not in command:
        params['command'] = command.replace('git clean', 'git clean --dry-run')
        modified = True

    # Enforce commit message format
    if 'git commit -m' in command:
        # Ensure conventional commit prefix
        if not any(p in command for p in ['feat:', 'fix:', 'docs:', 'refactor:', 'test:', 'chore:']):
            # Could block or auto-prefix - here we just warn
            pass

if modified:
    # Return modified input
    print(json.dumps({
        "decision": "approve",
        "reason": "Input modified for safety",
        "updatedInput": {"parameters": params}
    }))
else:
    # Allow unchanged
    print(json.dumps({"decision": "approve"}))

sys.exit(0)
```

### JSON Output Format

Hooks can return JSON to control behavior:

```json
{
  "decision": "approve|block|allow|deny",
  "reason": "Explanation shown to Claude",
  "updatedInput": {
    "parameters": { "modified": "params" }
  }
}
```

| Field | Purpose |
|-------|---------|
| `decision` | `approve`/`allow` to proceed, `block`/`deny` to stop |
| `reason` | Message shown to Claude when blocked |
| `updatedInput` | Modified tool parameters (v2.0.10+) |

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/pre-tool-use-modify.py"
          }
        ]
      }
    ]
  }
}
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

## Anti-Patterns

### ❌ Over-Engineering Hooks Early
**Problem**: Adding complex hooks before understanding needs
**Symptom**: Maintenance burden, hooks that don't provide value
**Solution**: Start with SessionStart only; add others based on actual pain points

### ❌ Blocking Hooks for Non-Critical Checks
**Problem**: Making hooks synchronous when async would suffice
**Symptom**: Slow AI interactions, user frustration
**Solution**: Use non-blocking checks unless action must be prevented

### ❌ Silent Hook Failures
**Problem**: Hooks that fail without user awareness
**Symptom**: Quality gates bypassed without notice
**Solution**: Output hook status clearly; fail loudly for critical hooks

### ❌ Hooks Without Documentation
**Problem**: Complex hook logic without explanation
**Symptom**: Team members disable hooks they don't understand
**Solution**: Comment purpose and behavior in hook scripts

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
- [Subagent Orchestration](./subagent-orchestration.md) - SubagentStop hook usage

---

## Sources

- [Claude Code Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Blog: How to Configure Hooks](https://claude.com/blog/how-to-configure-hooks)
- Production validation from 12+ projects

*Last updated: January 2026*
