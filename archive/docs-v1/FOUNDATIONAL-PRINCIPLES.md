# Foundational Principles for Claude Code

**Purpose**: Core advisories from thought leaders that should be repeated early and often

**Sources**: Boris Cherny (creator), Anthropic Official Docs, IndyDevDan, Aniket Panjwani, Nate B. Jones

---

## The Big 3: Non-Negotiable Principles

### 1. Keep CLAUDE.md Ruthlessly Minimal (~60 Lines)

**Sources**:
- Boris Cherny (SOURCES.md:18)
- Official Docs (SOURCES.md:63): "CLAUDE.md should be concise (~60 lines recommended)"

**Why It Matters**:
- Context rot: accuracy decreases as token count increases
- Every line in CLAUDE.md consumes context in every turn
- "Would removing this cause mistakes? If not, cut it." - Official docs

**Anti-Patterns**:
- ❌ Documenting every edge case
- ❌ Including examples that could be in separate files
- ❌ Writing essays about project philosophy
- ❌ Listing all possible commands/workflows

**Correct Approach**:
- ✅ Project purpose (1-2 sentences)
- ✅ Key commands that vary from standard
- ✅ Known gotchas that cause repeated mistakes
- ✅ Current focus (what are we working on now?)

**Rule of Thumb**: If Claude didn't ask about it, and it hasn't caused 2+ mistakes, it doesn't belong in CLAUDE.md.

---

### 2. Plan First, Always (For Non-Trivial Work)

**Sources**:
- Boris Cherny (SOURCES.md:19): "Plan Mode First: Always for non-trivial work"
- IndyDevDan (SOURCES.md:646): "Great Planning is Great Prompting"
- Aniket Panjwani (SOURCES.md:696): "Use /plan" as #1 tip
- Anthropic SDD: Specify → Plan → Tasks → Implement

**Why It Matters**:
- Planning effort directly improves output quality
- Prevents "works but wrong" implementations
- Catches architectural issues before code is written
- 2-3x quality improvement when done right

**When to Plan**:
- ✅ Any feature >2-3 files
- ✅ Multiple valid approaches exist
- ✅ Architectural decisions required
- ✅ Unfamiliar codebase area
- ✅ When you'd use AskUserQuestion to clarify approach

**When to Skip Planning**:
- Bug fixes with clear root cause
- Typos and formatting
- Copy-paste implementations
- Tasks with very specific, detailed instructions

**How to Plan**:
1. Use `/plan` or EnterPlanMode tool
2. Explore codebase first (Glob, Grep, Read)
3. Design approach with alternatives
4. Get user approval via ExitPlanMode
5. **Then** implement

**Key Quote**: "Yesterday it was Cursor, today it's Windsurf, tomorrow it'll be something else... learn to endure change with principle." - IndyDevDan (SOURCES.md:647)

---

### 3. Context Engineering > Prompt Engineering

**Sources**:
- Anthropic Engineering (SOURCES.md:97): "Context engineering supersedes prompt engineering for agents"
- Nate B. Jones (SOURCES.md:755): "Correctness trumps compression"
- IndyDevDan (SOURCES.md:640): Context = first pillar of "The Big Three"

**Why It Matters**:
- Agents need persistent, deterministic context
- External artifacts (specs, docs, git history) = agent memory
- Context rot is real: 84% token reduction improved performance

**Core Concepts**:
- **Deterministic Context** (user-controlled): Specs, ARCHITECTURE.md, CLAUDE.md
- **Probabilistic Context** (AI-discovered): Code exploration, web search
- **Lifecycle-Aware**: PERMANENT → EVERGREEN → PROJECT-SCOPED → SESSION-SCOPED

**Implementation**:
- ✅ Write specs before code (spec-driven development)
- ✅ ARCHITECTURE.md for system design
- ✅ PLAN.md for current priorities
- ✅ Git history as recovery mechanism
- ✅ One feature at a time (prevent context exhaustion)

**Anti-Pattern**: Trying to fit everything into prompts instead of using external artifacts

---

## The 7 Secondary Principles

### 4. Skills Should Be Minimal

**Source**: Official Docs (SOURCES.md:64): "Would removing this cause mistakes? If not, cut it."

- Skills consume context every time they're loaded
- Progressive disclosure: show less, reference more
- ~300 lines per skill file maximum
- Use multi-workflow pattern for complex skills

### 5. Verification = 2-3x Quality

**Source**: Boris Cherny (SOURCES.md:24): "Verification = 2-3x Quality: Subagent verification before finalizing"

- Use subagents to verify work
- Run tests/linters before considering done
- Official docs list verification as "highest-leverage practice"
- PostToolUse hooks for auto-formatting

### 6. Skip Exotic Customization

**Source**: Boris Cherny (SOURCES.md:27): "Skip Exotic Customization: Standard patterns over novel approaches"

- Official docs (SOURCES.md:65): "Avoid long lists of custom slash commands (anti-pattern)"
- Natural language works: "commit and push" (Boris SOURCES.md:20)
- Standard patterns > novel approaches
- Resist urge to over-engineer

### 7. Pre-Approve Permissions

**Source**: Boris Cherny (SOURCES.md:22): "Pre-Allow Permissions: `/permissions` to allow `bun run build:*`, `bun run test:*`"

- Official docs (SOURCES.md:67): "Use hooks sparingly; prefer pre-approved permissions"
- Reduces friction for repeated operations
- Use wildcard patterns: `bun run build:*`
- Balance security with velocity

### 8. One Feature at a Time

**Source**: Anthropic Engineering (SOURCES.md:42): "One feature at a time to prevent context exhaustion"

- Long-running agents need focus
- Context window is finite
- Prevents "works but wrong" cascade
- External artifacts track progress across sessions

### 9. External Artifacts as Memory

**Sources**:
- Anthropic Engineering (SOURCES.md:40): "External artifacts become the agent's memory"
- Nate B. Jones (SOURCES.md:749): Lifecycle-Aware Context model

- Specs persist across sessions
- Git history = recovery mechanism
- PLAN.md = current state
- Progress files bridge session boundaries

### 10. Use Native Tools First, Then MCP

**Source**: Boris Cherny (SOURCES.md:23): "MCP for External Tools: When native tools insufficient"

- MCP adds 300-800ms latency (Nate B. Jones SOURCES.md:764)
- ~43% of MCP servers have vulnerabilities
- Native tools are faster and more reliable
- MCP for external integrations only

---

## Implementation Checklist

Use this to audit any Claude Code project:

### CLAUDE.md Audit
- [ ] Under 60 lines?
- [ ] No examples that could be in separate files?
- [ ] Only things that prevent repeated mistakes?
- [ ] Current focus clearly stated?

### Planning Audit
- [ ] Non-trivial work goes through plan mode?
- [ ] Specs written before complex implementations?
- [ ] User approval obtained for approaches?

### Context Audit
- [ ] ARCHITECTURE.md exists and current?
- [ ] PLAN.md tracks priorities?
- [ ] Specs for complex features?
- [ ] One feature at a time?

### Skills Audit
- [ ] Each skill under ~300 lines?
- [ ] Progressive disclosure used?
- [ ] "Would removing this cause mistakes?" test applied?

### Verification Audit
- [ ] Tests run before considering done?
- [ ] Linters configured?
- [ ] PostToolUse hooks for formatting?

### Customization Audit
- [ ] Avoid long slash command lists?
- [ ] Use natural language when possible?
- [ ] Standard patterns over exotic approaches?

### Permissions Audit
- [ ] Pre-approved permissions for frequent operations?
- [ ] Wildcard patterns used appropriately?
- [ ] Hooks used sparingly?

---

## When to Repeat These Principles

### Always
- **CLAUDE.md audit**: Every time you add a line, ask "Is this necessary?"
- **Planning**: Before starting any non-trivial implementation
- **One feature at a time**: When tempted to "just quickly add..."

### Periodically
- **Full audit**: Monthly or when project feels "off"
- **Skills review**: When skills exceed ~300 lines
- **Permissions review**: When too many prompts interrupt flow

### When Onboarding
- **New team members**: Share this document first
- **New projects**: Apply checklist during initial setup
- **New patterns**: Evaluate against these principles

---

## Red Flags (You're Violating These Principles)

🚩 **CLAUDE.md is >100 lines** → Ruthlessly cut
🚩 **Implementing without planning** → Stop, use /plan
🚩 **Skills >500 lines** → Split or use multi-workflow
🚩 **Custom slash commands list is long** → Delete most, use natural language
🚩 **Context feels exhausted** → One feature at a time
🚩 **No verification step** → Add tests/linters
🚩 **Permission prompts interrupt constantly** → Pre-approve patterns
🚩 **Exotic hooks/customization** → Simplify to standard patterns

---

## Quotes to Remember

> "CLAUDE.md should be concise (~60 lines recommended)" - Anthropic Official Docs

> "Would removing this cause mistakes? If not, cut it." - Anthropic Official Docs

> "Great Planning is Great Prompting" - IndyDevDan

> "Plan Mode First: Always for non-trivial work" - Boris Cherny

> "Context engineering supersedes prompt engineering for agents" - Anthropic Engineering

> "One feature at a time to prevent context exhaustion" - Anthropic Engineering

> "Verification = 2-3x Quality" - Boris Cherny

> "Skip Exotic Customization: Standard patterns over novel approaches" - Boris Cherny

> "Principles over tools... learn to endure change with principle" - IndyDevDan

> "Correctness trumps compression" - Nate B. Jones

---

## Further Reading

- **Boris Cherny's Workflow**: SOURCES.md:7-30
- **Official Best Practices**: SOURCES.md:57-72
- **IndyDevDan Framework**: SOURCES.md:626-673
- **Aniket's 5 Tips**: SOURCES.md:692-700
- **Nate B. Jones Context Engineering**: SOURCES.md:740-768
- **Spec-Driven Development**: patterns/spec-driven-development.md
- **Context Engineering Pattern**: patterns/context-engineering.md
- **Long-Running Agent Pattern**: patterns/long-running-agent.md

---

**Last Updated**: February 2026
**Status**: FOUNDATIONAL - These principles should be referenced in every setup guide, tutorial, and onboarding document
