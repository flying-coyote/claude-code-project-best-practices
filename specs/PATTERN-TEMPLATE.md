# Pattern Specification Template

Use this template to specify requirements for a new pattern before implementation.

---

## Pattern: [Pattern Name]

### Metadata

| Field | Value |
|-------|-------|
| **Proposed by** | [Author] |
| **Date** | [YYYY-MM-DD] |
| **Status** | Draft / In Review / Approved / Implemented |
| **Target file** | patterns/[pattern-name].md |

---

### 1. Problem Statement

**What problem does this pattern solve?**

[Describe the specific problem, pain point, or gap this pattern addresses]

**Who experiences this problem?**

- [ ] Claude Code users
- [ ] AI-assisted developers generally
- [ ] Team leads / project managers
- [ ] Other: [specify]

**Evidence the problem exists:**

- [Link to discussion, issue, or observation]
- [Production experience description]

---

### 2. Proposed Solution

**High-level approach:**

[Brief description of the solution]

**Key components:**

1. [Component 1]
2. [Component 2]
3. [Component 3]

**SDD Phase alignment:**

- [ ] Specify - Context/specification artifacts
- [ ] Plan - Architecture/design artifacts
- [ ] Tasks - Task breakdown/tracking
- [ ] Implement - Execution/quality gates
- [ ] Cross-phase - Applies to multiple phases

---

### 3. Source Requirements

**Primary source (Tier A-B required):**

| Field | Value |
|-------|-------|
| Source name | [e.g., Anthropic Engineering Blog] |
| URL | [link] |
| Evidence Tier | A / B / C |
| Date accessed | [YYYY-MM-DD] |

**Supporting sources (optional):**

- [Source 2]
- [Source 3]

**Production validation:**

- [ ] Validated in production project
- [ ] Project: [name/description]
- [ ] Outcome: [measured results]

---

### 4. Content Requirements

**Must include:**

- [ ] Problem statement with evidence
- [ ] Solution with implementation guidance
- [ ] Code examples (if applicable)
- [ ] Anti-Patterns section (4+ anti-patterns minimum)
- [ ] Related Patterns section
- [ ] Last updated footer

**Should include:**

- [ ] Decision matrices or comparison tables
- [ ] When to use / when not to use guidance
- [ ] Integration with other patterns
- [ ] SDD phase context

**May include:**

- [ ] Advanced variations
- [ ] Tool-specific implementations
- [ ] Performance considerations

---

### 5. Acceptance Criteria

**Pattern is complete when:**

1. [ ] Passes pattern-reviewer skill validation
2. [ ] Evidence Tier A or B source cited
3. [ ] Anti-Patterns section has 4+ items
4. [ ] All Related Patterns links valid
5. [ ] Added to SOURCES.md
6. [ ] INDEX.md regenerated
7. [ ] Reviewed for self-compliance (repo practices what it teaches)

---

### 6. Related Patterns

**Patterns this will reference:**

- [pattern-1.md] - [relationship]
- [pattern-2.md] - [relationship]

**Patterns that should reference this:**

- [pattern-3.md] - [why]

---

### 7. Open Questions

- [ ] [Question 1]
- [ ] [Question 2]

---

### Review History

| Date | Reviewer | Decision | Notes |
|------|----------|----------|-------|
| | | | |

---

*Template version: 1.0*
*Based on: spec-driven-development.md, GitHub Spec Kit*
