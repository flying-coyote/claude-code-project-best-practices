# Troubleshooting Guide

**Purpose**: Common issues and recovery paths when using Claude Code best practices

---

## Table of Contents

- [CLAUDE.md Issues](#claudemd-issues)
- [Pattern Overwhelm](#pattern-overwhelm)
- [Team Adoption](#team-adoption)
- [Setup Issues](#setup-issues)
- [Hook Problems](#hook-problems)
- [Performance Issues](#performance-issues)
- [External Fetch Errors](#external-fetch-errors)

---

## CLAUDE.md Issues

### My CLAUDE.md keeps growing past 60 lines

**Symptom**: Started at 50 lines, now 120+ lines after several months

**Cause**: Adding context without removing, accumulating examples and edge cases

**Fix**:
1. **Apply The Big 3 Audit** (from FOUNDATIONAL-PRINCIPLES.md):
   - "Would removing this cause mistakes? If not, cut it."
   - Every line consumes context in every turn

2. **Move examples to separate files**:
   ```
   .claude/
     CLAUDE.md (~60 lines)
     docs/
       api-examples.md
       deployment-guide.md
       testing-notes.md
   ```
   Reference in CLAUDE.md: "See docs/ for examples"

3. **Delete sections Claude never asked about**:
   - Check your session history - what sections were actually referenced?
   - If Claude didn't need it in 10+ sessions, it doesn't belong

4. **Target structure** (~20 lines core):
   - Project purpose: 2 lines
   - Commands: 5 lines (only non-standard ones)
   - Known gotchas: 10 lines (things that caused 2+ mistakes)
   - Current focus: 2 lines

**Related**: [context-engineering.md](patterns/context-engineering.md)

---

### My CLAUDE.md feels too minimal - Claude makes mistakes

**Symptom**: Following 60-line rule but Claude lacks necessary context

**Root causes to check**:

1. **Missing critical gotchas**:
   - Are there repeated mistakes? Add those specific gotchas
   - Don't preemptively document - add after 2nd occurrence

2. **Context should be elsewhere**:
   - API documentation → Separate docs/ file or inline code comments
   - Architecture → ARCHITECTURE.md
   - Current work → PLAN.md
   - Testing procedures → Inline in test files

3. **Commands aren't clear**:
   - Claude needs actual commands, not descriptions
   - Bad: "Run tests - see package.json"
   - Good: "`npm test` - runs unit tests with coverage"

**Principle**: CLAUDE.md is for "what Claude needs to avoid mistakes", not comprehensive documentation.

---

## Pattern Overwhelm

### I'm overwhelmed by 34 patterns - where do I start?

**Quick Start Path** (3 patterns, 30 minutes reading):

1. **[context-engineering.md](patterns/context-engineering.md)** - Foundation for everything
2. **[spec-driven-development.md](patterns/spec-driven-development.md)** - The methodology (Specify→Plan→Tasks→Implement)
3. **[project-infrastructure.md](patterns/project-infrastructure.md)** - Setup patterns (Tier 1/2/3)

**Then choose by need**:
- Solo developer working on features → [long-running-agent.md](patterns/long-running-agent.md)
- Team lead setting standards → [evidence-tiers.md](patterns/evidence-tiers.md)
- Production/security focus → [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md)
- Need more guidance → See [PATTERN-LEARNING-PATH.md](PATTERN-LEARNING-PATH.md)

**Principle**: You don't need all 34 patterns. Start with 3, add as needed.

---

### Which patterns are actually critical?

**Tier 1 (Essential - read first)**:
- [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) - The Big 3
- [spec-driven-development.md](patterns/spec-driven-development.md) - Core methodology
- [context-engineering.md](patterns/context-engineering.md) - Context over prompts

**Tier 2 (High-value for most projects)**:
- [project-infrastructure.md](patterns/project-infrastructure.md) - Setup approach
- [long-running-agent.md](patterns/long-running-agent.md) - Multi-session work
- [progressive-disclosure.md](patterns/progressive-disclosure.md) - Skill architecture

**Tier 3 (Specialized - use when needed)**:
- Everything else in patterns/ directory

**Rule of thumb**: If you haven't hit the problem a pattern solves, you don't need that pattern yet.

---

## Team Adoption

### My team resists adopting these patterns

**Common objections + responses**:

#### "This is too much process"
**Response**: Start with Tier 1 only (5 minutes):
- 4 lines in settings.json for uncommitted/unpushed warnings
- That's it - no CLAUDE.md, no hooks, no complex setup
- Add more when value is proven

**Adoption path**: Tier 1 → Tier 2 after 1 week → Tier 3 as needed

---

#### "We already have our own way"
**Response**: Use patterns as reference, not mandate
- Patterns document what works - adapt to your context
- Cherry-pick: hooks without skills, CLAUDE.md without presets, etc.
- Framework Selection Guide helps choose orchestration approach

**Key**: Patterns are descriptive (what works), not prescriptive (what you must do)

---

#### "I don't want to learn Spec-Driven Development"
**Response**: Use just the infrastructure without SDD:
- Hooks for quality gates (formatting, linting)
- CLAUDE.md for project context
- settings.json for permissions
- No planning methodology required

**Separation**: Infrastructure ≠ methodology. Use what helps.

---

#### "The 60-line CLAUDE.md rule seems arbitrary"
**Response**: It's evidence-based, not arbitrary:
- Official Anthropic docs: "~60 lines recommended"
- Reason: Context rot - accuracy decreases with token count
- Every line in CLAUDE.md costs context in every turn
- Test it: Try 200-line CLAUDE.md vs 50-line. Measure mistake rate.

**Compromise**: Start with 100 lines if needed, audit monthly toward 60.

---

### How do we standardize across a team?

**Approach**:

1. **Start with shared principles** (not implementations):
   - Share FOUNDATIONAL-PRINCIPLES.md first
   - Discuss The Big 3 - get alignment on "why"
   - Let implementations vary by project

2. **Create team presets** (optional):
   - Fork presets/coding.md or presets/hybrid.md
   - Customize for your stack/tools
   - Teams share via internal repo or gist

3. **Standardize hooks + permissions** (high value):
   - Common hooks: Stop (uncommitted warning), PostToolUse (formatting)
   - Pre-approved permissions: test/build/lint commands
   - These reduce friction without enforcing methodology

4. **Let CLAUDE.md vary** (it should):
   - Every project is different
   - CLAUDE.md should be project-specific, not template-driven
   - Standardize the audit process, not the content

**Template** for team docs:
```markdown
# Our Team's Claude Code Standards

## Required (All Projects)
- Tier 1 infrastructure (Stop hook for uncommitted changes)
- Pre-approved permissions for `npm test`, `npm run build`

## Recommended
- CLAUDE.md under 80 lines (audit monthly)
- Use /plan for features >3 files

## Optional
- Skills (if helpful for your project)
- Presets (starting point, customize as needed)
```

---

## Setup Issues

### SETUP-PROJECT.md fetch fails with 404

**Symptom**: External fetch of setup prompt returns 404 error

**Common causes**:

1. **Wrong branch in URL**:
   - Check URL uses `master` branch (not `main`)
   - Correct: `...claude-code-project-best-practices/master/...`

2. **File moved or renamed**:
   - Check [repository](https://github.com/flying-coyote/claude-code-project-best-practices) for current structure
   - Prompts are in `prompts/` directory

3. **Network/GitHub issues**:
   - Try raw URL: `https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/prompts/SETUP-PROJECT.md`
   - If GitHub is down, clone repo locally and use file:// path

**Workaround**: Clone repository locally:
```bash
git clone https://github.com/flying-coyote/claude-code-project-best-practices.git
cd claude-code-project-best-practices
# Use local files
```

---

### Hooks don't run / settings.json not recognized

**Symptom**: Configured hooks in settings.json but they don't execute

**Check list**:

1. **File location** - Must be exactly `.claude/settings.json`:
   ```
   your-project/
     .claude/
       settings.json  ← here
       CLAUDE.md
   ```

2. **JSON syntax** - Validate with `cat .claude/settings.json | jq .`:
   - Common errors: trailing commas, unquoted keys, wrong brackets
   - Use [templates/settings.json.template](templates/settings.json.template) as reference

3. **Schema version** - Use current schema:
   ```json
   {
     "permissions": { ... },
     "hooks": { ... }
   }
   ```
   **NOT** old schema: `{ "allowedTools": ... }` (deprecated)

4. **Matcher syntax**:
   - Matchers use glob patterns
   - Stop hook: `"matcher": ""` (empty = always)
   - Specific tools: `"matcher": "Bash(git commit*)"` or `"matcher": "Write(**/*.ts)"`

5. **Claude Code version** - Hooks require Claude Code v2.0+:
   - Check version: `claude --version`
   - Update if needed

**Test hooks**:
```bash
# Make uncommitted change
echo "test" >> README.md

# Stop session - should see warning
# (Ctrl+C or /exit in Claude Code)
```

---

### Permission prompts keep interrupting

**Symptom**: Constantly prompted for permission despite pre-approving

**Causes + fixes**:

1. **Pattern too narrow**:
   - Bad: `"Bash(npm test)"` (only exact command)
   - Good: `"Bash(npm test*)"`  (includes flags/args)
   - Better: `"Bash(npm run test*)"` (all test scripts)

2. **Missing tool categories**:
   - Pre-approve common patterns:
   ```json
   "permissions": {
     "allow": [
       "Bash(git status*)",
       "Bash(git diff*)",
       "Bash(git log*)",
       "Bash(npm run test*)",
       "Bash(npm run build*)",
       "Bash(npm run lint*)"
     ]
   }
   ```

3. **Destructive operations** (by design):
   - `git push`, `rm -rf`, file deletions → Always prompt
   - This is a security feature - don't override
   - Pre-approve read operations, prompt for writes

**Balance**: Pre-approve frequent operations, keep prompts for destructive ones.

---

## Hook Problems

### PreToolUse hook blocks legitimate operations

**Symptom**: Hook rejects operation you want to allow

**Debug approach**:

1. **Check hook logs** - See what matched:
   - Hook output shows matcher that triggered
   - Verify the hook is catching what you intended

2. **Refine matcher**:
   - Too broad: `"matcher": "Bash(*)"` → blocks everything
   - Better: `"matcher": "Bash(rm*)"` → blocks only rm commands
   - Exceptions: Use multiple hooks with specific matchers

3. **Add escape hatch**:
   ```json
   {
     "matcher": "Bash(rm -rf*)",
     "hooks": [{
       "type": "command",
       "command": "echo '⚠️ Destructive operation - confirm first (y/n):'; read confirm; [ \"$confirm\" = \"y\" ]"
     }]
   }
   ```
   This prompts instead of blocking outright.

**Related**: [advanced-hooks.md](patterns/advanced-hooks.md)

---

### PostToolUse hook slows down sessions

**Symptom**: Every tool call takes extra time due to hook execution

**Optimization**:

1. **Make hooks fast**:
   - Bad: `npm run lint` (runs full lint on every write)
   - Good: `npx eslint --fix "$FILE"` (only file that changed)

2. **Use targeted matchers**:
   - Bad: `"matcher": "Write(*)"` → runs on every file write
   - Good: `"matcher": "Write(**/*.{ts,tsx})"` → only TypeScript files

3. **Async where possible**:
   - Formatting: sync (user expects formatted file)
   - Linting: can be async background job

4. **Consider removing hook**:
   - If faster to manually run `npm run format` after session
   - PostToolUse hooks best for auto-fixable issues (format, import sort)

**Rule**: Hooks should be <200ms. If slower, make async or remove.

---

## Performance Issues

### Claude Code feels slow / high latency

**Common causes**:

1. **MCP server latency** - MCP adds 300-800ms per call:
   - **Fix**: Use native tools where possible
   - Read files: Native Read tool (fast) vs MCP file server (slow)
   - See [mcp-vs-skills-economics.md](patterns/mcp-vs-skills-economics.md)

2. **Bloated CLAUDE.md** - Large context = slower processing:
   - **Fix**: Audit CLAUDE.md, target <60 lines
   - Use [progressive-disclosure.md](patterns/progressive-disclosure.md) for skills

3. **Too many skills loaded**:
   - **Fix**: Skills consume context when loaded
   - Remove unused skills from .claude/skills/
   - Use multi-workflow pattern for large skills

4. **Large file operations**:
   - **Fix**: Use pagination for large files
   - Read specific line ranges instead of full file

---

### Context window exhausted mid-session

**Symptom**: Claude says "I've run out of context" or quality degrades

**Recovery**:

1. **One feature at a time** (Principle #8):
   - Stop, commit current work
   - Start new session for next feature
   - External artifacts (git, specs) bridge sessions

2. **Externalize state**:
   - Move progress to PLAN.md or TODO.md
   - Commit work-in-progress to branch
   - New session can load state from files

3. **Reduce context overhead**:
   - Audit CLAUDE.md (trim to essentials)
   - Remove large skills not used this session
   - Close unrelated files

**Prevention**: Use [long-running-agent.md](patterns/long-running-agent.md) pattern

---

## External Fetch Errors

### "File not found" when fetching patterns from GitHub

**Symptom**: External fetch returns 404 for pattern files

**Checklist**:

1. **Verify branch name**: Use `master` not `main`
   - Correct: `.../master/patterns/...`

2. **Check file name case**: Filenames are case-sensitive
   - Correct: `spec-driven-development.md`
   - Wrong: `Spec-Driven-Development.md`

3. **Use raw.githubusercontent.com** for content:
   - Correct: `https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/patterns/spec-driven-development.md`
   - Wrong: `https://github.com/.../blob/master/...` (HTML page, not raw)

4. **Check repository status**: Visit repo to confirm file exists
   - Repository: https://github.com/flying-coyote/claude-code-project-best-practices

**Alternative**: Clone repo locally and use local paths (most reliable)

---

## Still Stuck?

### Resources

1. **Search existing patterns** - Problem might be documented:
   - Use INDEX.md or grep through patterns/ directory
   - Check [PATTERN-LEARNING-PATH.md](PATTERN-LEARNING-PATH.md)

2. **Check FOUNDATIONAL-PRINCIPLES.md** - Most issues trace to violating The Big 3

3. **Review examples/** - See complete working implementations:
   - [examples/coding-project/](examples/coding-project/)
   - [examples/writing-project/](examples/writing-project/)
   - [examples/research-project/](examples/research-project/)

4. **File an issue** - If problem isn't covered:
   - Repository: https://github.com/flying-coyote/claude-code-project-best-practices/issues
   - Include: Symptom, what you tried, your setup

---

**Last Updated**: February 2026
