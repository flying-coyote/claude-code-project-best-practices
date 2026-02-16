# Coding Project Example

**Type**: TypeScript library project (software development)

**Demonstrates**: Complete `.claude/` setup following best practices

---

## What This Example Shows

### Tier 1 Infrastructure (5 minutes)
✅ **Stop hook** - Warns about uncommitted/unpushed changes on session end
- Most critical safety feature
- Prevents losing work between sessions
- See `.claude/settings.json` lines 13-22

### Tier 2 Infrastructure (15 minutes)
✅ **Pre-approved permissions** - Common operations don't require prompts
- `npm test`, `npm run build`, `npm run lint`
- `git status`, `git diff`, `git log`
- See `.claude/settings.json` lines 2-11

✅ **Minimal CLAUDE.md** - 19 lines (target ~60)
- Project purpose: 1 line
- Commands: 4 lines (only non-standard ones)
- Known gotchas: 4 lines (things that caused actual bugs)
- Current focus: 1 line
- See `.claude/CLAUDE.md`

### Tier 3 Infrastructure (30 minutes)
✅ **PostToolUse hook** - Auto-formats TypeScript files on write
- Runs `prettier --write` after every file modification
- Only targets .ts/.tsx/.js/.jsx files (not all writes)
- Fails gracefully if prettier not installed
- See `.claude/settings.json` lines 23-32

✅ **SessionStart hook** - Shows git context on session start
- Current branch, uncommitted files, recent commits
- Helps orient at start of session
- See `.claude/hooks/session-start.sh`

---

## File Structure

```
coding-project/
  .claude/
    CLAUDE.md              # Minimal project context (19 lines)
    settings.json          # Hooks + permissions
    hooks/
      session-start.sh     # SessionStart hook implementation
  README.md               # This file (explains the example)
```

---

## Key Principles Demonstrated

### 1. CLAUDE.md Ruthlessly Minimal (~60 lines)
**Before** (typical anti-pattern):
```markdown
# Project

## Architecture
[200 lines explaining system design]

## Code Standards
- Write clean code
- Follow best practices
- Use TypeScript
[50 more generic guidelines]

## API Documentation
[500 lines of API details]
```

**After** (this example):
```markdown
# Project

## Purpose
[1 line - what does this project do?]

## Commands
[4 lines - only commands that differ from standard]

## Known Gotchas
[4 lines - things that caused actual repeated mistakes]

## Current Focus
[1 line - what are we working on now?]
```

**Rule**: "Would removing this cause mistakes? If not, cut it."

---

### 2. Hooks for Quality Gates

**Stop hook** (Tier 1 - always include):
- Runs when session ends (Ctrl+C or /exit)
- Warns if uncommitted changes or unpushed commits
- Prevents losing work between sessions

**PostToolUse hook** (Tier 2/3 - optional):
- Runs after every file write
- Auto-formats with prettier (or eslint --fix, etc.)
- Should be fast (<200ms) or targeted to specific file types

**SessionStart hook** (Tier 3 - optional):
- Shows context at session start
- Useful for git status, recent activity
- Non-blocking (informational only)

---

### 3. Pre-Approved Permissions

**Without pre-approval**:
```
Claude: I'll run npm test now
User: [Approve] or [Deny]?
Claude: Tests passed. Running npm run build
User: [Approve] or [Deny]?
```
Friction on every command.

**With pre-approval** (this example):
```
Claude: Running npm test && npm run build
[No prompts - operations pre-approved]
```

**Balance**: Pre-approve read operations, prompt for destructive writes.

---

## Usage

### Quick Start (Copy this setup)
```bash
# In your TypeScript project
mkdir -p .claude/hooks
cp examples/coding-project/.claude/CLAUDE.md .claude/
cp examples/coding-project/.claude/settings.json .claude/
cp examples/coding-project/.claude/hooks/session-start.sh .claude/hooks/
chmod +x .claude/hooks/session-start.sh

# Customize CLAUDE.md with your project-specific gotchas
# Test hooks work:
# 1. Make uncommitted change
# 2. Exit Claude Code session
# 3. Should see "⚠️ Uncommitted changes" warning
```

### Customize for Your Project

1. **CLAUDE.md**:
   - Replace "TypeScript Library" with your project name
   - Update commands to match your package.json scripts
   - Replace gotchas with YOUR project's repeated mistakes
   - Update "Current Focus" to what you're working on now

2. **settings.json**:
   - Adjust permissions to match your commands
   - Remove PostToolUse hook if you don't use prettier
   - Add hooks for your linter/formatter

3. **Hooks**:
   - session-start.sh works for any git project (keep as-is)
   - Add custom hooks for your workflow

---

## Common Adaptations

### For Python Projects
**settings.json**:
```json
"permissions": {
  "allow": [
    "Bash(pytest*)",
    "Bash(python -m*)",
    "Bash(pip install*)",
    "Bash(git status*)",
    "Bash(git diff*)",
    "Bash(git log*)"
  ]
}
```

**PostToolUse hook**:
```json
{
  "matcher": "Write(**/*.py)",
  "hooks": [{
    "type": "command",
    "command": "black \"$FILE\" 2>/dev/null || true"
  }]
}
```

### For Frontend Projects (React/Vue/etc.)
**Add permissions**:
```json
"Bash(npm run dev*)",
"Bash(npm run start*)",
"Bash(npx vite*)"
```

**PostToolUse for multiple formatters**:
```json
{
  "matcher": "Write(**/*.{ts,tsx,js,jsx,css,scss})",
  "hooks": [{
    "type": "command",
    "command": "npx prettier --write \"$FILE\" 2>/dev/null || true"
  }]
}
```

---

## Validation Checklist

After setting up:
- [ ] CLAUDE.md is under 60 lines (this example: 19 lines)
- [ ] Stop hook executes when you exit Claude Code
- [ ] Pre-approved commands don't trigger permission prompts
- [ ] PostToolUse hook formats files after writes (if enabled)
- [ ] SessionStart hook shows git context on session start
- [ ] Hooks are executable (`chmod +x .claude/hooks/*.sh`)

---

## Related Patterns

- [project-infrastructure.md](../../patterns/project-infrastructure.md) - Tiered infrastructure approach
- [advanced-hooks.md](../../patterns/advanced-hooks.md) - Hook patterns and examples
- [context-engineering.md](../../patterns/context-engineering.md) - Minimal CLAUDE.md principles
- [FOUNDATIONAL-PRINCIPLES.md](../../FOUNDATIONAL-PRINCIPLES.md) - The Big 3

---

## Notes

- This is a **reference example**, not a real project
- No actual source code included (focus on .claude/ structure)
- Customize for your project - don't copy blindly
- Start with Tier 1 (Stop hook), add Tier 2/3 as needed

**Last Updated**: February 2026
