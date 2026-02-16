# Migration Guide

**Purpose**: Adopt best practices from existing setups without starting from scratch

---

## Table of Contents

- [Scenario 1: Existing .claude/ Setup](#scenario-1-existing-claude-setup)
- [Scenario 2: Migrating from Cursor/.cursorrules](#scenario-2-migrating-from-cursorcursorrules)
- [Scenario 3: Migrating from Other AI Tools](#scenario-3-migrating-from-other-ai-tools)
- [Scenario 4: Team Standardization](#scenario-4-team-standardization)
- [Version Upgrades](#version-upgrades)

---

## Scenario 1: Existing .claude/ Setup

**You have**: Claude Code already configured with CLAUDE.md, maybe hooks/skills

**Goal**: Align with best practices without breaking what works

### Step 1: Audit Current Setup (15 minutes)

Use the audit prompt:
```
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/AUDIT-EXISTING-PROJECT.md and follow its instructions.
```

This generates a compliance report against The Big 3 principles.

### Step 2: Prioritize Improvements

**Critical gaps** (fix first):
- [ ] CLAUDE.md >100 lines → Ruthlessly trim to ~60 lines
- [ ] No Stop hook → Add uncommitted/unpushed warning (Tier 1)
- [ ] No /plan usage for non-trivial features → Start using EnterPlanMode

**Medium gaps** (next sprint):
- [ ] No ARCHITECTURE.md → Document system design
- [ ] Skills >500 lines → Split or use progressive disclosure
- [ ] No pre-approved permissions → Add common patterns

**Low priority gaps** (when convenient):
- [ ] Examples that should be in separate files
- [ ] Incomplete SOURCES.md attribution (if documenting patterns)

### Step 3: Incremental Migration

**Don't**: Delete everything and start over
**Do**: Keep what works, add missing pieces progressively

**Week 1 - Foundation**:
1. Read [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) (The Big 3)
2. Audit CLAUDE.md against "Would removing this cause mistakes?"
3. Add Tier 1 infrastructure (Stop hook) if missing

**Week 2 - Context Engineering**:
1. Move examples from CLAUDE.md to separate docs/ files
2. Create ARCHITECTURE.md if project is non-trivial
3. Trim CLAUDE.md to ~60 lines (target, not hard limit)

**Week 3 - Planning**:
1. Use /plan for next non-trivial feature
2. Create PLAN.md for current priorities
3. Add pre-approved permissions for common operations

**Week 4 - Quality Gates**:
1. Add PostToolUse hook for formatting/linting
2. Review and refine skills (progressive disclosure)
3. Final audit against best practices

### Step 4: Validation

After migration:
- [ ] CLAUDE.md is ~60 lines (80 max tolerable)
- [ ] Stop hook warns on uncommitted/unpushed changes
- [ ] Last feature used /plan before implementing
- [ ] Hooks run correctly on tool calls
- [ ] Sessions feel more productive (qualitative)

---

## Scenario 2: Migrating from Cursor/.cursorrules

**You have**: Cursor with `.cursorrules` file

**Goal**: Translate to Claude Code's `.claude/` structure

### Key Differences

| Concept | Cursor | Claude Code |
|---------|--------|-------------|
| Project context | `.cursorrules` | `.claude/CLAUDE.md` |
| Permissions | N/A (implicit) | `.claude/settings.json` (explicit) |
| Hooks | N/A | `.claude/settings.json` hooks |
| Skills | N/A | `.claude/skills/` directory |
| Planning | Composer agent | `/plan` or EnterPlanMode tool |

### Migration Process

#### 1. Translate .cursorrules to CLAUDE.md (30 minutes)

**Cursor's .cursorrules** is typically kitchen-sink documentation (200-500 lines).
**Claude Code's CLAUDE.md** is minimal (~60 lines) - only gotchas.

**Process**:
1. Open your `.cursorrules` file
2. Extract **only**:
   - Project purpose (1-2 sentences)
   - Non-standard commands
   - Known gotchas that cause repeated mistakes
   - Current focus (what you're working on now)
3. **Delete** from CLAUDE.md:
   - API documentation (put in code comments or separate docs/)
   - Testing procedures (put in test files)
   - Code examples (put in examples/ directory)
   - General best practices (put in ARCHITECTURE.md or omit)

**Example transformation**:

**.cursorrules** (300 lines):
```
This is a React + TypeScript project using Vite.

## Project Structure
src/
  components/ - React components
  utils/ - Helper functions
  ...

## API
Our API is at /api/v1. Endpoints:
- GET /users - List users
- POST /users - Create user
...

## Testing
We use Jest and React Testing Library.
Run tests with: npm test
...

## Code Style
- Use functional components
- Prefer const over let
- Always handle errors
...
```

**CLAUDE.md** (~40 lines):
```markdown
# React + TypeScript Project

## Commands
- `npm run dev` - Start dev server (port 5173)
- `npm test` - Run Jest tests
- `npm run build` - Production build

## Known Gotchas
- API base URL differs in dev vs prod (check .env)
- Test files must be *.test.tsx (not *.spec.tsx)
- Vite requires explicit .tsx extension in imports

## Current Focus
Refactoring auth flow to use React Context
```

**Principle**: If Cursor didn't repeatedly ask about it, it doesn't need to be in CLAUDE.md.

#### 2. Set Up Settings (15 minutes)

Create `.claude/settings.json`:
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run dev*)",
      "Bash(npm test*)",
      "Bash(npm run build*)",
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)"
    ]
  },
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi; if git status 2>/dev/null | grep -q \"ahead\"; then echo \"⚠️ Unpushed commits\"; fi'"
      }]
    }]
  }
}
```

This replicates Cursor's implicit "warn on uncommitted changes" behavior.

#### 3. Optional: Convert Cursor Docs to Claude Skills

If you had Cursor "rules" for specific workflows, convert to skills:

**Cursor rule** (in .cursorrules):
```
When I say "debug this", always:
1. Add console.log to relevant functions
2. Run the code
3. Analyze output
4. Remove console.logs
5. Suggest fix
```

**Claude Code skill** (`.claude/skills/debug-workflow.md`):
```markdown
# Debug Workflow Skill

When user says "debug this" or similar:

1. REPRODUCE
   - Add strategic console.log statements
   - Run code and capture output

2. ANALYZE
   - Identify unexpected values
   - Trace execution flow

3. FIX
   - Remove debug logs
   - Implement fix
   - Verify resolution
```

**Benefit**: Skills are reusable across projects, not tied to single `.cursorrules` file.

### Timeline

| Phase | Duration | Outcome |
|-------|----------|---------|
| Translate .cursorrules | 30 min | CLAUDE.md ~60 lines |
| Set up settings.json | 15 min | Permissions + hooks working |
| Optional: Create skills | 1-2 hours | Reusable workflow patterns |

---

## Scenario 3: Migrating from Other AI Tools

### From Aider

**Differences**:
- Aider: Git-centric, automatic commits
- Claude Code: Hooks for git workflow, manual commits

**Migration**:
1. Create CLAUDE.md with project context (Aider has none)
2. Add git hooks (Aider's auto-commit becomes optional Stop hook)
3. Pre-approve git operations in settings.json

**Advantage**: Claude Code's planning phase prevents Aider's "implement then realize wrong approach" issue.

### From GitHub Copilot

**Differences**:
- Copilot: Inline suggestions, no project context
- Claude Code: Full agent, requires explicit context

**Migration**:
1. Document what Copilot "just knew" → goes in CLAUDE.md or ARCHITECTURE.md
2. Create PLAN.md (Copilot has no concept of priorities)
3. Use /plan for features (Copilot has no planning phase)

**Advantage**: Claude Code's context engineering > Copilot's implicit context.

### From OpenHands (formerly OpenDevin)

**Differences**:
- OpenHands: Sandbox environment, web-based
- Claude Code: Local terminal, direct file access

**Migration**:
1. OpenHands' workspace becomes your local project directory
2. OpenHands' "agent loops" → Claude Code's /plan and long-running sessions
3. Sandbox restrictions → Claude Code uses native OS (add hooks for safety)

**Advantage**: Claude Code's local access is faster, no sandbox overhead.

---

## Scenario 4: Team Standardization

**You have**: 5 developers, each with different Claude Code setups

**Goal**: Consistent baseline without dictating everything

### Standardization Strategy

#### Level 1: Shared Principles (Required)
1. **Share FOUNDATIONAL-PRINCIPLES.md** with team
2. **Discuss The Big 3**:
   - CLAUDE.md minimal (~60 lines)
   - Plan before implementing (non-trivial work)
   - Context engineering (specs, ARCHITECTURE.md)
3. **Agree on compliance**: Monthly audit against principles

**Outcome**: Aligned on "why", flexible on "how"

#### Level 2: Common Infrastructure (Recommended)
Create team-shared templates:

**Team settings.json template**:
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test*)",
      "Bash(npm run build*)",
      "Bash(npm run lint*)",
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)"
    ]
  },
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi'"
      }]
    }],
    "PostToolUse": [{
      "matcher": "Write(**/*.{ts,tsx,js,jsx})",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write \"$FILE\" 2>/dev/null || true"
      }]
    }]
  }
}
```

**Team preset** (e.g., `team-typescript.md`):
```markdown
# Team TypeScript Preset

## Required
- CLAUDE.md under 80 lines (audit monthly)
- Stop hook for uncommitted changes
- Pre-approved test/build/lint commands

## Recommended
- Use /plan for features >3 files
- ARCHITECTURE.md for system design
- PLAN.md for current priorities

## Optional
- Skills (if helpful for repeated workflows)
- PostToolUse hook for formatting
- Presets as starting point (customize per project)
```

**Distribution**: Share via internal repo or gist.

#### Level 3: Project-Specific Customization (Always)
Each project customizes:
- CLAUDE.md content (project-specific gotchas)
- Additional permissions (project-specific commands)
- Project-specific skills

**Rule**: Standardize process, not content. CLAUDE.md should differ by project.

### Migration Timeline

**Week 1 - Alignment**:
- Team meeting: Discuss FOUNDATIONAL-PRINCIPLES.md
- Agree on standardization level (1, 2, or 3)

**Week 2 - Template Creation**:
- Create team settings.json template
- Create team preset (if desired)
- Document in internal wiki/repo

**Week 3 - Individual Migration**:
- Each dev applies templates to their projects
- Customize CLAUDE.md per project
- Test hooks work correctly

**Week 4 - Retrospective**:
- What's working? What needs adjustment?
- Refine templates based on feedback
- Plan quarterly audits

---

## Version Upgrades

### Upgrading from v1.0 → v1.3

**Breaking changes**: None (backward compatible)

**New features** (adopt incrementally):
1. **QUICK-REFERENCE-PRINCIPLES.md** - Printable 1-page reference for The Big 3
2. **14 new patterns** - Pattern count grew from 20 to 34
3. **Stop hook enhancement** - Now checks for unpushed commits too
4. **Pattern organization** - Organized by SDD phase (Specify/Plan/Tasks/Implement)

**Migration checklist**:
- [ ] Update Stop hook to check unpushed commits (optional, recommended)
- [ ] Review new patterns: PATTERN-LEARNING-PATH.md
- [ ] Print QUICK-REFERENCE-PRINCIPLES.md as desk reference
- [ ] Update INDEX.md if you maintain one (or regenerate)

**Timeline**: 30 minutes

### Upgrading Claude Code Tool (v2.x → v3.x)

**When new Claude Code versions release**:

1. **Check release notes** - Breaking changes in hooks/settings schema?
2. **Test in sandbox** - Clone project, test new version
3. **Update settings.json** - If schema changed
4. **Verify hooks** - Matchers or hook types may change
5. **Update patterns** - New official features may supersede workarounds

**Principle**: Don't upgrade immediately. Wait for community validation (1-2 weeks).

---

## Common Migration Pitfalls

### Pitfall 1: Trying to Migrate Everything at Once
**Problem**: Overwhelm, breaks existing workflow
**Solution**: Incremental adoption - Tier 1 this week, Tier 2 next week, Tier 3 when needed

### Pitfall 2: Copying Templates Without Customization
**Problem**: CLAUDE.md has generic content that doesn't help your project
**Solution**: Templates are starting points. Delete what doesn't apply, add project-specific gotchas.

### Pitfall 3: Over-Standardizing Across Team
**Problem**: Forcing identical setups frustrates developers
**Solution**: Standardize principles and infrastructure, let CLAUDE.md vary by project.

### Pitfall 4: Ignoring Existing Workflow Strengths
**Problem**: "Best practices" break what was already working well
**Solution**: Audit first (what's working?), adopt only what adds value.

### Pitfall 5: Skipping the "Why"
**Problem**: Team adopts infrastructure without understanding principles
**Solution**: Start with FOUNDATIONAL-PRINCIPLES.md discussion. Infrastructure follows principles.

---

## Success Criteria

After migration, you should see:

**Quantitative**:
- [ ] CLAUDE.md is 60-80 lines (from 100-500 before)
- [ ] Stop hook executes on session end
- [ ] Last 3 non-trivial features used /plan first
- [ ] Permission prompts reduced by 50%+ (via pre-approval)

**Qualitative**:
- [ ] Sessions feel more productive
- [ ] Fewer repeated mistakes (gotchas documented)
- [ ] Easier to onboard new contributors (clear CLAUDE.md)
- [ ] Team aligned on approach (shared principles)

---

## Rollback Plan

If migration causes issues:

1. **Keep old setup in branch**:
   ```bash
   git checkout -b migration-attempt
   # Try migration
   # If problems:
   git checkout main  # Back to working state
   ```

2. **Incremental rollback**:
   - Remove hooks that cause friction
   - Restore longer CLAUDE.md if too minimal
   - Keep what works, revert what doesn't

3. **Learn and retry**:
   - What specifically broke?
   - Read TROUBLESHOOTING.md for that issue
   - Try again with refined approach

**Principle**: Migration should improve workflow. If it doesn't, investigate why (maybe pattern doesn't apply to your context).

---

## Support Resources

- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common migration issues
- **[PATTERN-LEARNING-PATH.md](PATTERN-LEARNING-PATH.md)** - Which patterns to adopt first
- **[AUDIT-EXISTING-PROJECT.md](prompts/AUDIT-EXISTING-PROJECT.md)** - Compliance check
- **[FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md)** - The Big 3 principles

**Questions?** File an issue: https://github.com/flying-coyote/claude-code-project-best-practices/issues

---

**Last Updated**: February 2026
