---
name: Your Skill Name
description: Brief description of when this skill activates. Include trigger keywords. Write in third person. Max 1024 characters.
allowed-tools: Read, Grep, Glob
---

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

*This template structure (IDENTITY/GOAL/STEPS/OUTPUT) is adapted from [Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric) pattern format.*
