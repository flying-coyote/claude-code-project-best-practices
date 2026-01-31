# Progressive Disclosure for Skills

**Source**: Production-validated pattern from 12+ projects
**Evidence Tier**: B (Production validated with measured outcomes)

## ⚠️ Important: Anthropic Guidance First

**Anthropic's official recommendation**: Skills should be ~60 lines and concise.

> "Keep it concise. For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"
> — [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)

**This pattern is for exceptional cases only.** Apply progressive disclosure ONLY when:
1. A skill genuinely exceeds 200 lines of essential content
2. The skill serves multiple distinct operations rarely used together
3. Token savings from conditional loading outweigh maintenance complexity

**Default approach**: Start with a single concise SKILL.md (~60 lines). Only refactor to multi-workflow when demonstrably necessary.

---

## The Core Problem

Large skill files (300-700+ lines) waste tokens on every activation. Most of that content isn't needed for every interaction.

**Typical waste**:
- Full 6,000-word skill loaded for simple query
- Same detailed protocols loaded repeatedly
- Reference databases always in context

**Solution**: Three-tier progressive disclosure architecture that loads only what's needed.

---

## Three-Tier Architecture

### Tier 1: System Prompt (SKILL.md) - Always Loaded

**Purpose**: Minimal context for skill activation and routing
**Target size**: ~500 words max

Contains:
- Trigger conditions (when to activate)
- **Workflow Routing section** - Maps user intents to workflow files
- Quick reference (essential frameworks/checklists only)
- Integration with other skills
- Security classification

### Tier 2: Workflow Files - Loaded on Demand

**Purpose**: Detailed protocols for specific operations
**Target size**: 1,000-2,000 words per workflow
**Location**: `workflows/` subdirectory

Contains:
- Step-by-step procedures
- Examples and decision trees
- Quality standards
- Output formats

### Tier 3: Reference Files - Just-in-Time Lookup

**Purpose**: Databases and frameworks for quick lookup
**Target size**: 500-1,500 words per reference
**Location**: `references/` subdirectory

Contains:
- Quick-lookup databases
- Evidence tier frameworks
- Checklists and matrices

---

## Directory Structure

```
.claude/skills/[skill-name]/
├── SKILL.md                    # Tier 1: System prompt (500 words max)
├── workflows/                  # Tier 2: Detailed protocols
│   ├── [operation-1].md
│   ├── [operation-2].md
│   └── ...
└── references/                 # Tier 3: Quick-lookup databases
    ├── [framework-1].md
    └── ...
```

---

## Key Innovation: Workflow Routing Section

The critical addition that makes progressive disclosure work is an explicit routing section in SKILL.md:

```markdown
## WORKFLOW ROUTING (SYSTEM PROMPT)

**User Intent** → **Workflow File** → **Action**

"Validate this hypothesis" → `workflows/validation-methodology.md` → 4-step validation
"What contradictions exist?" → `references/known-contradictions.md` → Database lookup
"Help me document this" → `workflows/documentation.md` → Template + process
```

**Why this matters**: Without explicit routing, Claude won't know when to load which workflow. The routing section acts as a dispatch table.

**Note**: The "(SYSTEM PROMPT)" label indicates this section is loaded with every skill activation and serves as the routing logic for on-demand workflow loading.

---

## Measured Results

### Single-File to Multi-File Refactoring

Production testing on 4 skills showed significant token savings:

| Skill | Before | After | Reduction |
|-------|--------|-------|-----------|
| contradiction-detector | 327 lines | 75 lines | **77%** |
| hypothesis-validator | 218 lines | 109 lines | **50%** |
| publication-quality-checker | 739 lines | 104 lines | **86%** |
| research-extractor | 542 lines | 121 lines | **78%** |

**Average reduction**: ~73% token savings per skill activation

### Multi-Workflow Structure (Advanced Pattern)

Production refactoring of 3 large personal skills (Dec 2025):

| Skill | Single-File | Multi-Workflow | Workflows | Avg per Workflow |
|-------|-------------|----------------|-----------|------------------|
| ultrathink-analyst | 748 lines | 957 lines (4 files) | 3 | 203 lines |
| git-workflow-helper | 587 lines | 2,216 lines (6 files) | 5 | 383 lines |
| academic-citation-manager | 534 lines | 1,503 lines (5 files) | 4 | 345 lines |

**Key Insight**: Total content increased (more comprehensive), but **conditional loading** means only relevant workflow loaded per interaction.

**Example**: git-workflow-helper
- **Before**: 587 lines loaded for every git operation
- **After**: 269 lines (routing) + ~350 lines (specific workflow) = ~620 lines for operation
- **Benefit**: Each workflow <500 lines (maintainability), clear separation of concerns

**Additional benefits**:
- Faster skill activation (less context to process)
- Improved context management (only load what's needed)
- Clearer skill structure (separation of concerns)
- Better maintainability (workflows can be updated independently)
- Enables skill expansion without bloat (add workflows without affecting base size)

---

## SKILL.md Template (Tier 1)

```markdown
---
name: [Skill Name]
description: [Concise description with trigger keywords]
allowed-tools: [Tool1, Tool2, Tool3]
---

# [Skill Name]

## When to Activate

**ACTIVATE when user:**
- [Trigger condition 1]
- [Trigger condition 2]

**DO NOT activate when:**
- [False positive 1]
- [False positive 2]

## WORKFLOW ROUTING (SYSTEM PROMPT)

**User Intent** → **Workflow File** → **Action**

"[phrase pattern 1]" → `workflows/[file-1].md` → [outcome]
"[phrase pattern 2]" → `workflows/[file-2].md` → [outcome]

## QUICK REFERENCE

**[Essential Framework]**:
- [Element 1]: [Brief description]
- [Element 2]: [Brief description]

**[Critical Checklist]**:
1. ✅ [Item 1]
2. ✅ [Item 2]

## Integration with Other Skills

**Works WITH:**
- **[skill-1]**: [Integration point]

## Security

**Risk Level**: 🟢 ZERO RISK

---

**For detailed [operation]**: See `workflows/[file].md`
```

---

## Implementation Checklist

### Analysis (15 min)
- [ ] Read current SKILL.md completely
- [ ] Identify distinct workflows (3-7 typical)
- [ ] Identify reference databases (1-3 typical)
- [ ] Note current line count

### Setup (2 min)
```bash
mkdir -p .claude/skills/[skill-name]/workflows
mkdir -p .claude/skills/[skill-name]/references
```

### Compression (30 min)
- [ ] Create Workflow Routing section
- [ ] Extract detailed protocols to workflows/
- [ ] Move databases to references/
- [ ] Add footer links
- [ ] Target ~500 words

### Validation (15 min)
- [ ] All workflows referenced in routing
- [ ] All footer links work
- [ ] ~70% token reduction achieved
- [ ] SKILL.md alone is clear

---

## Multi-Workflow Pattern (Advanced)

For complex skills with multiple distinct operations, use **multi-workflow structure** instead of simple 3-tier:

### Structure

```
.claude/skills/git-workflow-helper/
├── SKILL.md                           # Routing document (~270 lines)
└── workflows/
    ├── commit.md                      # Commit workflow (~340 lines)
    ├── branch.md                      # Branch management (~340 lines)
    ├── push.md                        # Push operations (~330 lines)
    ├── pull-request.md                # PR workflow (~470 lines)
    └── conflict-resolution.md         # Merge conflicts (~470 lines)
```

### Routing Table Format

Use table format for multi-workflow skills:

```markdown
## WORKFLOW ROUTING

**This skill uses multi-workflow structure**. Choose the appropriate workflow based on operation:

| Workflow | File | When to Use |
|----------|------|-------------|
| **Commit** | `workflows/commit.md` | Creating commits, message guidance, pre-commit checks |
| **Branch** | `workflows/branch.md` | Creating/managing branches, worktrees, naming |
| **Push** | `workflows/push.md` | Pushing to remote, force push, upstream tracking |
| **Pull Request** | `workflows/pull-request.md` | Creating PRs, code review, merging |
| **Conflict Resolution** | `workflows/conflict-resolution.md` | Resolving merge conflicts, aborting operations |

**Common Sequences**:
- **New Feature**: branch.md → commit.md → push.md → pull-request.md
- **Hotfix**: branch.md → commit.md → push.md → pull-request.md (expedited)
- **Conflict Handling**: push.md (pull fails) → conflict-resolution.md → push.md
```

### Example: ultrathink-analyst

Phase-based routing for analysis methodology:

```markdown
## WORKFLOW ROUTING

**This skill uses multi-workflow structure**. Choose workflow based on analysis phase:

| Workflow | File | When to Use |
|----------|------|-------------|
| **FRAME: Problem Definition** | `workflows/frame-problem-definition.md` | Starting analysis, understand problem before solutions |
| **ANALYZE: Deep Investigation** | `workflows/analyze-deep-investigation.md` | After FRAME, exploring alternatives and trade-offs |
| **SYNTHESIZE: Integration** | `workflows/synthesize-integration.md` | After ANALYZE, generating insights and recommendations |

**Standard Sequence**: FRAME → ANALYZE → SYNTHESIZE (complete all three for full analysis)

**Partial Workflows**: Can execute single phase if user requests specific step, but recommend full 3-phase for complex problems.
```

### When to Use Multi-Workflow

**Use multi-workflow when**:
- Skill has 5+ distinct operations (e.g., git: commit, branch, push, PR, conflicts)
- Operations rarely used together (commit vs conflict resolution)
- Each operation >200 lines of methodology
- Skill serves multiple user intents that don't overlap

**Use simple 3-tier when**:
- Skill has single workflow with reference data
- Operations frequently used together
- Each piece <200 lines
- Linear progression through steps

### Workflow Size Guidelines

**Target**: 200-500 lines per workflow
- **Under 200 lines**: Consider merging workflows
- **200-500 lines**: Optimal (maintainable, comprehensible)
- **Over 500 lines**: Consider splitting into sub-workflows

**Example from production**:
- git-workflow-helper: 5 workflows, average 383 lines ✅
- ultrathink-analyst: 3 workflows, average 203 lines ✅
- academic-citation-manager: 4 workflows, average 345 lines ✅

---

## Best Practices

### Workflow Naming

**Use kebab-case** (Daniel Miessler PAI pattern):
- ✅ `commit.md`, `branch.md`, `push.md`
- ✅ `frame-problem-definition.md`
- ✅ `conflict-resolution.md`
- ❌ `Commit.md`, `create_branch.md`, `pushToRemote.md`

**Use verb phrases or operation names**:
- ✅ `search-contradictions.md` (verb phrase)
- ✅ `commit.md` (operation name)
- ❌ `contradictions-search.md` (noun-first)

### Reference vs Workflow
- **References**: Databases, frameworks, checklists (lookup)
- **Workflows**: Protocols, procedures, processes (action)

### Examples Placement
- 1-2 quick examples in SKILL.md
- Detailed examples in workflows

### Footer Pattern
Always end SKILL.md with:
```markdown
**For detailed [X]**: See `workflows/[file].md`
**For [database]**: See `references/[file].md`
```

---

## When to Use Progressive Disclosure

### Decision Matrix

| Skill Characteristics | Pattern | Example |
|----------------------|---------|---------|
| **Under 60 lines** | Single SKILL.md **(Anthropic recommended)** | Most skills |
| **60-200 lines, cohesive** | Single-file SKILL.md | systematic-debugger |
| **200-500 lines, distinct operations** | Consider 3-tier (exceptional) | hypothesis-validator |
| **500+ lines, many operations** | Multi-workflow (rare cases only) | git-workflow-helper |

### Good Candidates (High Value)

**Single-file SKILL.md (default)**:
- Skills under 200 lines (most skills)
- Cohesive workflows without distinct phases
- Skills where all content is typically needed together

**Simple 3-tier (exceptional)**:
- Skills with >200 lines AND separable reference data
- Research/analysis skills with lookup databases

**Multi-workflow (rare)**:
- Skills with 5+ truly distinct operations
- Complex skills where users need one operation at a time
- Skills that would be >1000 lines as single file

### Skip Progressive Disclosure (Low Value)

- Skills under 100 lines
- Single-purpose skills
- Already concise skills
- Skills where all content needed together

---

## Anti-Patterns

### ❌ Monolithic Skill Files
**Problem**: Keeping all skill content in a single 500+ line SKILL.md
**Symptom**: 100% of tokens loaded for every activation, even simple queries
**Solution**: Extract workflows to `workflows/`, references to `references/`

### ❌ Missing Workflow Routing
**Problem**: Multi-file structure without explicit routing section in SKILL.md
**Symptom**: Claude doesn't know when to load which workflow file
**Solution**: Add explicit "WORKFLOW ROUTING" section mapping user intents to files

### ❌ Over-Splitting Simple Skills
**Problem**: Applying progressive disclosure to skills under 200 lines
**Symptom**: Maintenance overhead exceeds token savings
**Solution**: Only split skills >200 lines with distinct operations

### ❌ Orphaned Workflows
**Problem**: Workflow files not referenced in SKILL.md routing or footer
**Symptom**: Workflows never loaded, wasted content
**Solution**: Every workflow must appear in routing table and footer links

---

## Related Patterns

- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
- [Context Engineering](./context-engineering.md) - Semantic highways for discovery
- [Skills for Domain Knowledge](./skills-domain-knowledge.md) - What content goes into skills
- [Advanced Tool Use](./advanced-tool-use.md) - Complementary token reduction via tool search

*Last updated: January 2026*
