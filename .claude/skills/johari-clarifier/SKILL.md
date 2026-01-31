---
name: johari-clarifier
description: |
  Surfaces hidden assumptions before complex tasks using Johari Window methodology.
  Trigger: "clarify", "what am I missing", or tasks involving 3+ files.
allowed-tools: Read, Grep, Glob, AskUserQuestion
---

# Johari Window Clarifier

Surface assumptions before implementation to prevent "we don't know what we don't know" problems.

## When to Activate

- Implementation involving 3+ files
- User says "clarify", "what am I missing"
- Complex features without detailed specs

**Skip when**: Simple bug fix, single-file change, user says "just do it"

## The Four Quadrants

| Quadrant | Description | Action |
|----------|-------------|--------|
| **Arena** | Known to both | State your understanding |
| **Hidden** | User knows, you don't | Ask about conventions, prior decisions |
| **Blind Spot** | You know, user doesn't | Share security/perf considerations |
| **Unknown** | Neither knows | Flag for investigation |

## SAAE Protocol

1. **Share**: State what you understand about the task
2. **Ask**: "What team conventions apply? Any prior decisions that constrain this?"
3. **Acknowledge**: Share technical considerations user might not know
4. **Explore**: List unknowns, propose investigation, note assumptions

## Output Format

```markdown
## Clarification: [Task]

**Arena**: [Shared understanding]
**Hidden**: [What user revealed]
**Blind Spots**: [Technical considerations I shared]
**Unknowns**: [To investigate, with assumptions]

Ready to proceed? [Yes/conditions]
```

## Don't

- Skip to implementation without surfacing assumptions
- Ask endless questions (focus on high-impact unknowns)
- Treat unknowns as blockers (note them, proceed with documented assumptions)
