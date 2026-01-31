# Skill Templates

## Minimal Template (Anthropic Recommended)

Per [Anthropic guidance](https://code.claude.com/docs/en/best-practices), skills should be ~60 lines and concise. Use this template for most skills.

```markdown
---
name: your-skill-name
description: Brief description with trigger keywords. Max 1024 chars.
allowed-tools: Read, Grep, Glob
---

# Skill Name

Brief description of what this skill does.

## When to Activate

- Trigger condition 1
- Trigger condition 2

**Skip when**: [conditions to not activate]

## Steps

1. First step
2. Second step
3. Third step

## Output Format

\`\`\`markdown
## Result
[template]
\`\`\`

## Don't

- Anti-pattern 1
- Anti-pattern 2
```

---

## Extended Template (For Complex Skills Only)

Use this template only when a skill genuinely requires 200+ lines. See [Progressive Disclosure](../patterns/progressive-disclosure.md) for when this is appropriate.

---
# Agent Skills Standard (agentskills.io) - REQUIRED FIELDS
name: your-skill-name   # Required: lowercase, hyphens for spaces
description: |          # Required: Complete description of what skill does and when to use it
  Brief description of when this skill activates. Include trigger keywords.
  Write in third person (for auto-activation). Max 1024 characters.
  Example: "Guides debugging with systematic REPRODUCE-ISOLATE-UNDERSTAND-FIX methodology"

# OPTIONAL FIELDS (Claude Code specific)
allowed-tools: Read, Grep, Glob  # Restrict available tools (security)
# model: sonnet                  # Override model for this skill
# version: 1.0                   # Skill version
---

<!--
AGENT SKILLS STANDARD COMPLIANCE (agentskills.io)

This template follows the Agent Skills open standard for cross-platform compatibility.
Skills using this format work in: Claude Code, Cursor, VS Code Copilot, Codex CLI, and other
adopting platforms.

REQUIRED:
- SKILL.md file with YAML frontmatter (name + description)
- Markdown instructions body

OPTIONAL STRUCTURE:
your-skill/
├── SKILL.md           # Required: frontmatter + instructions
├── scripts/           # Optional: executable code
├── references/        # Optional: docs loaded on-demand (progressive disclosure)
└── assets/            # Optional: templates, data files

See: https://agentskills.io/specification
-->

# Your Skill Name

## IDENTITY

You are a [role] who [core capability]. Your role is to [primary function]. You are [key characteristics].

## GOAL

[Clear statement of what this skill achieves. One or two sentences.]

## TRIGGER CONDITIONS

**ACTIVATE when user:**
- [Specific trigger 1]
- [Specific trigger 2]
- [Keywords or phrases that should trigger]
- [Context that suggests this skill]

**DO NOT ACTIVATE when:**
- [Exclusion 1 - important edge case]
- [Exclusion 2 - common false positive]
- [When user explicitly wants different approach]

## WORKFLOW ROUTING (SYSTEM PROMPT)

For skills using [progressive disclosure](../patterns/progressive-disclosure.md), choose routing format based on complexity:

### Simple Routing (For skills with 1-3 workflows)

**User Intent** → **Workflow File** → **Action**

"[phrase pattern 1]" → `workflows/[operation-1].md` → [outcome]
"[phrase pattern 2]" → `workflows/[operation-2].md` → [outcome]
"[phrase pattern 3]" → `references/[database-1].md` → [quick lookup]

### Multi-Workflow Routing (For skills with 4+ workflows)

**This skill uses multi-workflow structure**. Choose the appropriate workflow based on [operation/phase/task]:

| Workflow | File | When to Use |
|----------|------|-------------|
| **[Operation 1]** | `workflows/[file-1].md` | [When to use this workflow] |
| **[Operation 2]** | `workflows/[file-2].md` | [When to use this workflow] |
| **[Operation 3]** | `workflows/[file-3].md` | [When to use this workflow] |

**Standard Sequence**: [workflow-1] → [workflow-2] → [workflow-3]
**Common Patterns**: [Pattern 1], [Pattern 2], [Pattern 3]

*(Remove this section if skill is <100 lines and doesn't need progressive disclosure)*

## QUICK REFERENCE

**[Key Framework/Concept]**:
- Element 1: Brief description
- Element 2: Brief description
- Element 3: Brief description

**[Critical Checklist/Matrix]**:
1. ✅ Item 1
2. ✅ Item 2
3. ✅ Item 3

*(Include 1-2 essential frameworks or checklists that are needed frequently. Keep concise.)*

## STEPS

### Phase 1: [Name]

**Goal**: [What this phase achieves]

**Execution:**
```
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

**Questions to answer:**
- [Key question 1]
- [Key question 2]

---

### Phase 2: [Name]

**Goal**: [What this phase achieves]

**Execution:**
```
1. [Step 1]
2. [Step 2]
```

---

### Phase 3: [Name]

**Goal**: [What this phase achieves]

**Execution:**
```
1. [Step 1]
2. [Step 2]
```

## OUTPUT FORMAT

### Phase 1 Output
```
[Template for phase 1 output]
- Key: [value]
- Key: [value]
```

### Phase 2 Output
```
[Template for phase 2 output]
```

### Final Output
```
[Template for final deliverable]
✅ [Checklist item 1]
✅ [Checklist item 2]
```

## EXAMPLES

### Example 1: [Scenario Name]

**User**: "[Example user input]"

**Skill Response**:
```
[Example of how skill responds]
```

### Example 2: [Scenario Name]

**User**: "[Example user input]"

**Skill Response**:
```
[Example of how skill responds]
```

## ANTI-PATTERNS

**DON'T:**
- ❌ [Anti-pattern 1]
- ❌ [Anti-pattern 2]
- ❌ [Anti-pattern 3]

**DO:**
- ✅ [Best practice 1]
- ✅ [Best practice 2]
- ✅ [Best practice 3]

## INTEGRATION WITH OTHER SKILLS

**Works WITH:**
- **[skill-name]**: [How they work together]
- **[skill-name]**: [How they work together]

**Sequence:**
1. **[Skill 1]**: [What it does]
2. **[Skill 2]**: [What it does]
3. **[Skill 3]**: [What it does]

## SECURITY

See [SECURITY-GUIDELINES.md](./SECURITY-GUIDELINES.md) for full security framework.

**Risk Level**: 🟢 ZERO RISK | 🟡 LOW RISK | 🟠 MEDIUM RISK | 🔴 HIGH RISK

**Scope**: [What this skill processes - e.g., "Git-controlled project files only"]

**Controls** (if MEDIUM/HIGH RISK):
1. [Control 1 - e.g., "User confirmation required"]
2. [Control 2 - e.g., "Provenance tracking enabled"]

**Security Assumption**: [Trust model - e.g., "All processed files are version-controlled"]

---

**Version**: 1.0
**Created**: [Date]
**Source**: [Where methodology came from]
**Applies to**: [What project types]

---

## Cross-Platform Compatibility

This skill follows the [Agent Skills open standard](https://agentskills.io/specification):

| Platform | Support | Notes |
|----------|---------|-------|
| Claude Code | ✅ Full | Native support |
| Cursor | ✅ Full | Via skills directory |
| VS Code Copilot | ✅ Full | Via agent skills |
| Codex CLI | ✅ Full | OpenAI adoption |
| Other platforms | 🔄 Varies | Check platform docs |

**Portability requirements**:
- YAML frontmatter with `name` and `description` only
- Markdown body with instructions
- Scripts in `scripts/` must be self-contained
- No platform-specific tool references in core instructions

---

*This template structure (IDENTITY/GOAL/STEPS/OUTPUT) is adapted from [Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric) pattern format.*

*Agent Skills format: [agentskills.io](https://agentskills.io) | [Anthropic Skills Repository](https://github.com/anthropics/skills)*
