# Claude Skills

Skills are reusable AI behavior patterns that activate based on context. They're one of the most powerful features of mature Claude Code projects.

## What Are Skills?

A skill is a markdown file that teaches Claude:
- **When** to activate (trigger conditions)
- **What** to do (step-by-step methodology)
- **How** to output results (structured format)
- **When NOT** to activate (equally important)

## Skill Locations

```
~/.claude/skills/           # Personal skills (available in ALL projects)
└── my-skill/
    └── SKILL.md

your-project/.claude/skills/ # Project skills (this project only)
└── project-skill/
    └── SKILL.md
```

## Skill Structure

Every skill follows this pattern:

```markdown
---
name: Skill Name
description: When to trigger (keywords, contexts). Max 1024 chars. Third-person.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Skill Name

## IDENTITY
Who is Claude when using this skill?

## GOAL
What is the skill trying to achieve?

## TRIGGER CONDITIONS

**ACTIVATE when user:**
- [Specific trigger 1]
- [Keywords or contexts]

**DO NOT ACTIVATE when:**
- [Exclusion 1]
- [Edge cases to avoid]

## STEPS
[Step-by-step methodology]

## OUTPUT FORMAT
[Expected output structure]

## EXAMPLES
[Concrete usage examples]

## ANTI-PATTERNS
[What NOT to do]
```

## Key Design Principles

### 1. Third-Person Descriptions

The `description` field must be third-person for skill selection to work:

```yaml
# Good - third person
description: Apply debugging methodology when user reports errors or bugs.

# Bad - first person
description: I help you debug code when you have errors.
```

### 2. Explicit DO NOT ACTIVATE

Just as important as triggers. Prevents false positives:

```markdown
**DO NOT ACTIVATE when:**
- User is in design/planning phase (no code yet)
- Error is trivial and obvious (typo, missing import)
- User explicitly wants quick fix without analysis
```

### 3. Structured Output

Skills should produce consistent, scannable output:

```markdown
## OUTPUT FORMAT

### Phase 1 Output
```
Problem Identified:
- Location: [file:line]
- Type: [category]
- Evidence: [what was observed]
```
```

### 4. Integration Mapping

Document how skills work together:

```markdown
## INTEGRATION WITH OTHER SKILLS

**Works WITH:**
- **tdd-enforcer**: Add test during fix phase
- **git-workflow-helper**: Commit with clear message

**Sequence:**
1. This skill diagnoses problem
2. tdd-enforcer writes regression test
3. git-workflow-helper commits fix
```

## Example Skills

This repo includes sanitized examples of universal skills:

### Development Skills

#### [systematic-debugger](examples/systematic-debugger/SKILL.md)
4-phase debugging: REPRODUCE → ISOLATE → UNDERSTAND → FIX

#### [tdd-enforcer](examples/tdd-enforcer/SKILL.md)
Test-driven development: RED → GREEN → REFACTOR

#### [git-workflow-helper](examples/git-workflow-helper/SKILL.md)
Git best practices: commits, branches, PRs, and safe operations

### Analysis Skills

#### [ultrathink-analyst](examples/ultrathink-analyst/SKILL.md)
Deep analysis: FRAME → ANALYZE → SYNTHESIZE methodology

### Content & Research Skills

#### [content-reviewer](examples/content-reviewer/SKILL.md)
Publication quality: evidence tiers, intellectual honesty, professional voice, balanced perspective

#### [research-extractor](examples/research-extractor/SKILL.md)
Research synthesis: systematic extraction of concepts, evidence, hypotheses from sources

### Security Skills

#### [threat-model-reviewer](examples/threat-model-reviewer/SKILL.md)
Threat modeling: UNDERSTAND → IDENTIFY (STRIDE) → ASSESS → MITIGATE

#### [detection-rule-reviewer](examples/detection-rule-reviewer/SKILL.md)
Detection engineering: accuracy, performance, evasion resistance, operational quality

## Creating Your Own Skills

### Step 1: Identify the Pattern
What repetitive workflow do you want to codify?

### Step 2: Define Triggers
When should this skill activate? Be specific.

### Step 3: Write the Methodology
Step-by-step process with clear phases.

### Step 4: Add Examples
Concrete examples showing the skill in action.

### Step 5: Document Anti-Patterns
What should the skill NOT do?

## Personal vs. Project Skills

| Type | Location | Scope | Use For |
|------|----------|-------|---------|
| **Personal** | `~/.claude/skills/` | All projects | Universal patterns (debugging, TDD) |
| **Project** | `.claude/skills/` | This project | Domain-specific (SIEM queries, blog publishing) |

## Best Practices

### Keep Skills Focused
One skill = one pattern. Don't combine debugging + testing + deployment.

### Progressive Disclosure
- SKILL.md: Core methodology (~300-500 lines)
- workflows/: Extended procedures (separate files)
- references/: Supporting materials

### Read-Only by Default
Most skills should guide, not automatically change things:
```yaml
allowed-tools: Read, Grep, Glob  # Safe, read-only
```

Add write tools only when needed:
```yaml
allowed-tools: Read, Grep, Glob, Bash, Write, Edit  # Can modify
```

### Version Your Skills
```markdown
---
**Version**: 2.0
**Created**: 2025-10-17
**Updated**: 2025-12-08
**Source**: Community best practices
```

## Common Skill Categories

### Development Skills
- Debugging methodology
- Test-driven development
- Code review patterns
- Git workflow conventions

### Content Skills
- Voice consistency
- Citation management
- Publication quality checks
- Evidence tier classification

### Research Skills
- Hypothesis validation
- Literature synthesis
- Contradiction detection
- Evidence assessment

### Communication Skills
- Expert outreach
- Documentation standards
- Presentation patterns

## Further Reading

- [Anthropic Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Example Skills in this repo](examples/)
- [DECISIONS.md](../DECISIONS.md) for design rationale
