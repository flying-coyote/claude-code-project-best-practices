# Progressive Disclosure for Skills

**Source**: Production-validated pattern from 12+ projects
**Evidence Tier**: B (Production validated with measured outcomes)

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

Production testing on 4 skills showed significant token savings:

| Skill | Before | After | Reduction |
|-------|--------|-------|-----------|
| contradiction-detector | 327 lines | 75 lines | **77%** |
| hypothesis-validator | 218 lines | 109 lines | **50%** |
| publication-quality-checker | 739 lines | 104 lines | **86%** |
| research-extractor | 542 lines | 121 lines | **78%** |

**Average reduction**: ~73% token savings per skill activation

**Additional benefits**:
- Faster skill activation (less context to process)
- Improved context management (only load what's needed)
- Clearer skill structure (separation of concerns)
- Better maintainability (workflows can be updated independently)

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

## Best Practices

### Workflow Naming
Use verb phrases: `search-contradictions.md`, not `contradictions-search.md`

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

**Good candidates** (high value):
- Skills with >200 lines
- Skills with multiple distinct operations
- Skills with reference databases

**Skip progressive disclosure** (low value):
- Skills under 100 lines
- Single-purpose skills
- Already concise skills

---

## Related Patterns

- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
- [Context Engineering](./context-engineering.md) - Semantic highways for discovery
