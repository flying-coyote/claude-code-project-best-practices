# Pattern Specification Template

> **ARCHIVED — not current guidance, and only partly succeeded.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Partially superseded. CONTRIBUTING.md carries the archived §3 Source Requirements (its [Analysis Proposal] issue stub: Source tier/URL, Production Validation) and supersedes the §5 Acceptance Criteria with a stricter Integration + Validation checklist; analysis/CANONICAL-DOC-TEMPLATE.md carries part of §4 as a required frontmatter schema, section order, and citation/counter-evidence/gap standards. Not carried anywhere live: the proposal Metadata block (proposer, date, Draft/In Review/Approved/Implemented state — CANONICAL's `status:` is a doc-lifecycle axis, not a review state), §1's audience taxonomy and "evidence the problem exists", §2 Proposed Solution and its SDD phase alignment, §4's concrete thresholds (the "4+ anti-patterns minimum" exists nowhere in the live lane, including the retargeted reviewer skill), §7 Open Questions (CANONICAL's "Gaps" covers evidentiary gaps in published claims, not open design questions), and the Review History table. More broadly, both successors are a different genre — a contribution process and a finished-doc shape — so the pre-implementation fill-in spec artifact itself has no live replacement. Its target (patterns/[name].md, the pattern-reviewer gate) predates the analysis/ corpus and no longer exists. Read the archive for the proposal-form material. Its v1-era specifics and dates are a snapshot, preserved as recorded — do not treat them as current. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

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
