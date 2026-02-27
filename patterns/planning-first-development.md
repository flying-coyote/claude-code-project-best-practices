---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "Planning effort increases from ~20% to ~60%+ in AI-assisted development"
    source: "IndyDevDan - Principled AI Coding"
    date: "2025-10-01"
    revalidate: "2026-10-01"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Planning-First Development: Great Planning is Great Prompting

**Source**: [IndyDevDan - Principled AI Coding](https://agenticengineer.com/principled-ai-coding), aligned with [GitHub Spec Kit](https://github.com/github/spec-kit)
**Evidence Tier**: A (Practitioner methodology + industry standard)

## Overview

Planning-first development is the principle that **investment in planning directly improves AI output quality**. This pattern synthesizes IndyDevDan's "Great Planning is Great Prompting" insight with spec-driven development methodology.

> "The crucial skill and real engineering differentiator today lies in your ability to craft the perfect package to effectively command vast compute power through AI Coding tools."
> — IndyDevDan

**Core Insight**: The quality of AI-generated code is proportional to the quality of the specification provided. Planning isn't overhead—it's the primary leverage point.

---

## The Principle

### Why Planning Matters More with AI

| Traditional Development | AI-Assisted Development |
|------------------------|------------------------|
| Planning reduces rework | Planning determines output quality |
| Specs communicate to humans | Specs **are** the prompt |
| Ambiguity resolved through conversation | Ambiguity causes hallucination |
| Planning is ~20% of effort | Planning becomes ~60%+ of effort |

**The Shift**: In AI-assisted development, most engineering effort moves from implementation to specification. The AI handles implementation; you handle specification.

### The Context-Prompt-Model Framework

IndyDevDan's "Big Three" pillars for effective AI coding:

```
┌─────────────────────────────────────────────────────────────┐
│                    EFFECTIVE AI CODING                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────┐     ┌─────────┐     ┌─────────┐              │
│   │ CONTEXT │ ──→ │ PROMPT  │ ──→ │  MODEL  │              │
│   └─────────┘     └─────────┘     └─────────┘              │
│       ↑               ↑               ↑                     │
│       │               │               │                     │
│   What the AI     How you ask     Which tool               │
│   needs to know   for results     you choose               │
│                                                              │
│   = SDD Specify   = SDD Tasks     = SDD Implement          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## The Plan → Spec → Build Workflow

### Traditional Workflow (Prone to Failure)

```
Idea → Prompt → (Hope for the best) → Code
```

**Problems**:
- AI guesses at requirements
- Sprawling, tangential code dumps
- Constant correction loops
- Context exhaustion from back-and-forth

### Planning-First Workflow

```
Idea → Plan → Spec → Prompt → Code → Verify
  ↑      ↓      ↓       ↓        ↓       ↓
  │    What   How    Single    High   Matches
  │    to     to     focused  quality  spec?
  │    build  build  request  output
  │                                      │
  └──────────────────────────────────────┘
         (Iterate spec, not code)
```

**Benefits**:
- AI has complete context before starting
- Single comprehensive prompt replaces many small ones
- Reduced token usage from fewer iterations
- Output matches intent because intent is explicit

---

## Implementing Planning-First in Claude Code

### Phase 1: Gather Context (Before Any Prompt)

Before asking Claude to build anything, assemble:

```markdown
## Context Checklist

- [ ] What problem are we solving? (User perspective)
- [ ] What does success look like? (Acceptance criteria)
- [ ] What constraints exist? (Tech stack, patterns, style)
- [ ] What files/modules are involved? (Scope boundary)
- [ ] What should NOT change? (Explicit exclusions)
- [ ] What examples exist? (Reference implementations)
```

### Phase 2: Create the Spec (Before Any Code)

Write the specification as if it were the prompt:

```markdown
## Feature: [Name]

### Requirements
[What it must do - user stories with acceptance criteria]

### Technical Approach
[How it should be implemented - architecture, patterns]

### Scope
- Files to modify: [explicit list]
- Files NOT to modify: [explicit exclusions]

### Acceptance Criteria
- [ ] [Specific, testable criteria]
- [ ] [Specific, testable criteria]

### Examples
[Reference code, similar features, or pseudocode]
```

### Phase 3: Single Focused Prompt

Transform the spec into a prompt:

```
Implement the following feature according to this specification:

[Paste spec]

Before writing code:
1. Confirm you understand the requirements
2. Outline your implementation approach
3. Wait for approval before proceeding
```

### Phase 4: Verify Against Spec

After implementation, verify:

```
Review the implementation against the original spec:

[Paste spec]

Check:
- [ ] All acceptance criteria met
- [ ] No scope creep (only specified files modified)
- [ ] Follows stated technical approach
- [ ] Tests cover requirements
```

---

## Question-Driven Specification

Before writing specs, systematically gather requirements through structured questioning. This technique uses Claude's AskUserQuestion tool to surface requirements, constraints, and edge cases that might otherwise be missed.

### The Pattern

```
┌─────────────────────────────────────────────────────────────┐
│               QUESTION-DRIVEN SPECIFICATION                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   1. Enter Plan Mode                                         │
│          ↓                                                   │
│   2. Claude asks structured questions (scaled to complexity) │
│          ↓                                                   │
│   3. User answers → Requirements crystallize                 │
│          ↓                                                   │
│   4. Generate spec from answers                              │
│          ↓                                                   │
│   5. User approves spec → Exit plan mode → Implement         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Question Count by Complexity

| Task Complexity | Question Count | Examples |
|-----------------|----------------|----------|
| **Simple** | 3-5 questions | Bug fix, styling change, add field |
| **Medium** | 8-12 questions | New feature, refactoring, API endpoint |
| **Complex** | 15-25 questions | Architecture change, multi-component feature |

**Principle**: Thorough questioning prevents downstream errors, but over-questioning simple tasks wastes time.

### Question Categories

Structure questions across these domains:

**1. Requirements & Goals**
- What problem are we solving?
- Who is the user?
- What does success look like?

**2. Constraints & Boundaries**
- What cannot change?
- What patterns must we follow?
- What dependencies exist?

**3. Technical Approach**
- What files are involved?
- What's the preferred architecture?
- What third-party tools/libraries?

**4. Edge Cases & Error Handling**
- What happens when X fails?
- What are the boundary conditions?
- What validation is required?

**5. Verification & Testing**
- How do we know it works?
- What tests are needed?
- Who approves completion?

### Implementation in Claude Code

Use plan mode (Shift+Tab) with explicit questioning phase:

```markdown
## Before Implementing [Feature]

Enter plan mode and systematically ask about:

### Phase 1: Requirements (3-5 questions)
- Problem definition
- Success criteria
- User perspective

### Phase 2: Technical (3-5 questions)
- Files/modules involved
- Patterns to follow
- Dependencies

### Phase 3: Edge Cases (2-4 questions)
- Failure modes
- Validation rules
- Error handling

### Phase 4: Verification (2-3 questions)
- Test requirements
- Approval process
- Definition of done

After gathering answers, generate specification for approval.
```

### Integration with Spec Files

Answers should flow into persistent artifacts:

| Question Domain | Artifact Destination |
|-----------------|---------------------|
| Requirements & Goals | `specs/[feature].md` |
| Technical Approach | `ARCHITECTURE.md` or spec file |
| Key Decisions | `DECISIONS.md` |
| Session Context | `CLAUDE.md` (if reusable) |

**Anti-Pattern**: Keeping all answers in ephemeral chat. Persist valuable context for future sessions.

### When to Use This Pattern

**Use When:**
- Starting a new feature (greenfield or brownfield)
- Requirements are ambiguous
- Multiple valid approaches exist
- Stakeholder alignment is critical

**Skip When:**
- Bug fix with clear reproduction steps
- Trivial changes with obvious requirements
- Following an existing, approved spec

---

## Practical Patterns

### Pattern 1: The Planning Prompt

Before implementation, ask Claude to plan:

```
I need to implement [feature]. Before writing any code:

1. Read the relevant files: [list files]
2. Understand the current architecture
3. Create a detailed implementation plan including:
   - Files to modify
   - Functions to add/change
   - Data structures needed
   - Edge cases to handle
4. Present the plan for my approval

Do NOT write any code yet.
```

### Pattern 2: Massive Spec Prompts

For complex features, create comprehensive specs that enable single-prompt implementation:

```markdown
# Feature Specification: [Name]

## Context
[Everything the AI needs to know - paste relevant CLAUDE.md sections,
existing code patterns, API contracts, etc.]

## Requirements
[Detailed requirements with acceptance criteria]

## Implementation Guide
[Step-by-step approach, file-by-file changes]

## Validation
[How to verify correctness]

---

Implement this feature following the specification exactly.
```

**Result**: Features that would require 10+ prompts via conversation can be completed in 1-2 prompts with proper specs.

### Pattern 3: Context Priming with Journaling

IndyDevDan's approach: maintain a journal for context continuity:

```markdown
# Session Journal

## Date: [Today]

### Completed
- [What was done]

### Current State
- [Where things stand]

### Next Session
- [What to pick up]

### Patterns Discovered
- [Bugs encountered and fixed - prevents repeat issues]
```

**Benefit**: When encountering repeat bugs, point to the journal. Claude recognizes the pattern and fixes immediately rather than tunnel-visioning.

---

## Anti-Patterns to Avoid

### ❌ Vibe Coding Without Specs

```
"Make a login page"
```

**Problem**: AI guesses at requirements, style, validation, error handling...

### ✅ Specified Request

```
Create a login page with:
- Email and password fields (use our TextField component from src/components)
- Validation: email format, password min 8 chars
- Error states: inline field errors + toast for API errors
- Submit calls POST /api/auth/login
- Success redirects to /dashboard
- Match the existing auth page styling in src/pages/auth
```

### ❌ Iterative Micro-Prompting

```
"Add a button"
"Make it blue"
"Move it to the right"
"Add hover state"
"Actually, make it green"
```

**Problem**: Each prompt adds context overhead. 5 small prompts use more tokens than 1 good prompt.

### ✅ Single Comprehensive Prompt

```
Add a primary action button to the form:
- Position: right-aligned below the form fields
- Style: matches our Button component's "primary" variant
- Text: "Submit"
- Hover: darken 10%, slight scale up
- Loading state: show spinner, disable button
```

---

## Measuring Planning Effectiveness

### Metrics to Track

| Metric | Target | Why |
|--------|--------|-----|
| Prompts per feature | <5 | Good specs reduce back-and-forth |
| First-attempt accuracy | >80% | AI output matches intent |
| Scope creep incidents | 0 | Explicit boundaries prevent drift |
| Context resets | <1/session | Good context management |

### Signs You Need More Planning

- Saying "no, I meant..." frequently
- AI modifying files you didn't mention
- Multiple iterations to get basic output right
- Features working but not matching your mental model

### Signs Your Planning is Working

- Single prompts produce complete features
- AI asks clarifying questions about edge cases (not basics)
- Output matches your vision without major corrections
- You spend more time reviewing than correcting

---

## Integration with SDD Phases

Planning-first development maps directly to SDD:

| SDD Phase | Planning-First Activity | Artifact |
|-----------|------------------------|----------|
| **Specify** | Gather context, define requirements | Requirements doc |
| **Plan** | Technical design, file scope | Design doc |
| **Tasks** | Break into prompts, define acceptance criteria | Task list |
| **Implement** | Execute with single focused prompts | Code |

**Key Insight**: The Specify and Plan phases ARE the planning. By the time you reach Implement, you should know exactly what to ask for.

---

## Claude Code Implementation

### CLAUDE.md Integration

Add planning-first principles to your CLAUDE.md:

```markdown
## Development Approach

This project follows planning-first development:

1. Before implementing features, create a specification
2. Get spec approval before writing code
3. Use single comprehensive prompts over iterative micro-prompts
4. Verify output against specification

For complex features, use `/plan` command before implementation.
```

### Slash Command: /plan

Create `.claude/commands/plan.md`:

```markdown
---
description: Create implementation plan before coding
---

Before implementing $ARGUMENTS, create a detailed plan:

## Requirements Analysis
- What problem does this solve?
- What are the acceptance criteria?
- What constraints exist?

## Technical Approach
- What files need modification?
- What patterns should be followed?
- What are the edge cases?

## Implementation Steps
1. [Numbered steps]

## Verification
- How will we know it works?
- What tests are needed?

Present this plan for approval before writing any code.
```

---

## Related Patterns

- [Spec-Driven Development](./spec-driven-development.md) - The 4-phase model this pattern implements
- [Context Engineering](./context-engineering.md) - Deterministic vs probabilistic context
- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory

---

## Sources

**Primary (Tier A/B)**:
- [IndyDevDan - Principled AI Coding](https://agenticengineer.com/principled-ai-coding) - "Great Planning is Great Prompting" principle
- [GitHub Spec Kit](https://github.com/github/spec-kit) - 4-phase SDD model
- [Anthropic - Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) - Context and prompting guidance

**Community Patterns (Tier C)**:
- Question-Driven Specification - Structured requirements elicitation via AskUserQuestion (EngineerPrompt methodology)

*Last updated: January 2026*
