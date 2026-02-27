---
version-requirements:
  claude-code: "v2.1.30+"  # Session memory feature
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "AI compression with ~10x token savings for long-term storage"
    source: "Nate B. Jones Memory Prompts methodology"
    date: "2025-10-01"
    revalidate: "2026-10-01"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Memory Architecture

**Source**: Nate B. Jones Memory Prompts methodology + production validation
**Evidence Tier**: B (Production validated)

## The Core Problem

AI assistants have no persistent memory between sessions. Each conversation starts from zero. Users waste time re-establishing context.

**Solution**: Structured memory architecture with lifecycle-based information management.

---

## Four Lifecycle Categories

### 1. PERMANENT - Set Once, Rarely Changes

**What it includes**:
- Work style and preferences
- Quality standards
- Communication tone
- Recurring constraints

**Storage**: `~/.claude/profile-and-preferences.md` (global) or project CLAUDE.md
**Update frequency**: Rarely (set once, minor tweaks)
**Retrieval**: Always loaded (SessionStart hook or CLAUDE.md)

**Example content**:
```markdown
## Work Style
- Intellectual honesty over marketing claims
- Evidence-based assertions with citations
- Conversational authority (use "I" not passive voice)

## Quality Standards
- Claims require evidence tier classification (A/B/C)
- No false certainty ("may" not "definitely")
- Surface contradictions, don't hide them
```

### 2. EVERGREEN - Updates Monthly/Quarterly

**What it includes**:
- Work playbooks and methodologies
- Reference library (domain knowledge)
- Decision history
- Terminology definitions

**Storage**: Project knowledge base, skills, reference files
**Update frequency**: Monthly or as domain evolves
**Retrieval**: On-demand (load when relevant)

**Example locations**:
- `.claude/skills/` - Work playbooks
- `docs/concepts/` - Domain knowledge
- `DECISIONS.md` - Decision history

### 3. PROJECT-SCOPED - Active Project Duration

**What it includes**:
- Project requirements
- Current phase and status
- Active priorities
- Stakeholder context

**Storage**: Project-specific CLAUDE.md and PLAN.md
**Update frequency**: Weekly during active development
**Retrieval**: Auto-loaded when in project directory

**Example content in CLAUDE.md**:
```markdown
## Current Phase
Week 3 - Expert validation

## Active Priorities
1. Complete interviews with Jake, Lisa, Paul
2. Draft blog posts 1-2
3. Finalize partnership proposal
```

### 4. SESSION-SCOPED - Conversation Only

**What it includes**:
- Temporary working context
- In-progress decisions
- Exploratory analysis

**Storage**: Conversation memory (not persisted)
**Update frequency**: Per conversation
**Retrieval**: Native to Claude (no action needed)

**Note**: Archive valuable session insights to EVERGREEN storage before session ends. See [Session Learning](./session-learning.md) for systematic capture of corrections and preferences.

---

## Storage Map

| Information Type | Lifecycle | Location | Retrieval |
|-----------------|-----------|----------|-----------|
| Profile & Preferences | PERMANENT | `~/.claude/` or CLAUDE.md | Always |
| Work Playbooks | EVERGREEN | `.claude/skills/` | On skill activation |
| Reference Library | EVERGREEN | `docs/` or knowledge base | On-demand |
| Decision History | EVERGREEN | DECISIONS.md or tracker | On-demand |
| Project Context | PROJECT | CLAUDE.md, PLAN.md | Always (in project) |
| Session State | SESSION | Conversation memory | Automatic |

---

## Retrieval Patterns

### Automatic Retrieval (No User Action)

**When**: Session starts, skill activates
**What**: Profile, project context, relevant skills

**Implementation**:
- SessionStart hook loads project context
- Skills auto-activate based on trigger conditions
- CLAUDE.md always available

### On-Demand Retrieval (User Triggers)

**When**: User asks, task requires
**What**: Reference library, decision history, detailed workflows

**Implementation**:
- User asks about past decision → Load DECISIONS.md
- User needs domain knowledge → Reference skill workflows
- User makes claim → Check contradiction database

### Proactive Retrieval (Claude Suggests)

**When**: Claude detects relevant context
**What**: Contradictions, related decisions, applicable standards

**Implementation**:
- Skills surface relevant information
- UserPromptSubmit hook hints at skill activation
- Contradiction-detector activates on absolute claims

---

## Implementation Checklist

### Phase 1: Profile Setup
- [ ] Create `~/.claude/profile-and-preferences.md`
- [ ] Document work style and quality standards
- [ ] Reference from project CLAUDE.md files

### Phase 2: Project Context
- [ ] Create CLAUDE.md for each project
- [ ] Include current phase and priorities
- [ ] Set up SessionStart hook to load context

### Phase 3: Knowledge Organization
- [ ] Organize reference library (concepts, specs, terminology)
- [ ] Create skills for work playbooks
- [ ] Establish decision tracking (DECISIONS.md or tracker)

### Phase 4: Retrieval Automation
- [ ] Implement SessionStart hook
- [ ] Configure skill triggers
- [ ] Set up Stop hook for archival reminders

---

## High-Stakes Information

For information where errors cause real problems:

**Requirements**:
1. **Original source links** for verification
2. **Version history** (git commits)
3. **Evidence tier classification** (A/B/C/D)
4. **Cross-reference contradictions** (prevent confirmation bias)

**Examples**:
- Expert quotes → Include source and date
- Technical specs → Link to official documentation
- Vendor claims → Classify as Tier C/D until validated

---

## Example: Complete Memory Setup

```
~/.claude/
├── profile-and-preferences.md    # PERMANENT (global)
└── skills/                       # EVERGREEN (universal skills)
    ├── systematic-debugger/
    └── tdd-enforcer/

project/
├── .claude/
│   ├── CLAUDE.md                 # PROJECT (context)
│   ├── settings.json             # Hooks configuration
│   ├── hooks/
│   │   └── session-start.sh      # Loads context
│   └── skills/                   # EVERGREEN (project skills)
├── ARCHITECTURE.md               # PROJECT (strategic)
├── PLAN.md                       # PROJECT (tactical)
├── DECISIONS.md                  # EVERGREEN (history)
└── docs/
    └── concepts/                 # EVERGREEN (reference)
```

---

## Anti-Patterns

### Avoid: Everything in CLAUDE.md
- Problem: Bloated context, token waste
- Solution: Use progressive disclosure, reference external files

### Avoid: No Memory Structure
- Problem: Re-explain context every session
- Solution: Implement SessionStart hook, maintain CLAUDE.md

### Avoid: Session-Only Important Decisions
- Problem: Insights lost when conversation ends
- Solution: Archive decisions to EVERGREEN storage

---

## Production Implementation: claude-mem

For teams seeking automated memory management, **[claude-mem](https://github.com/thedotmack/claude-mem)** provides a production-ready implementation of the memory architecture concepts documented here.

### Key Features

| Feature | Implementation | Benefit |
|---------|---------------|---------|
| **5 Lifecycle Hooks** | SessionStart → UserPromptSubmit → PostToolUse → Summary → SessionEnd | Complete conversation capture |
| **AI Compression** | Automatic summarization with ~10x token savings | Efficient long-term storage |
| **Vector Search** | Chroma-based semantic retrieval | Find relevant past context |
| **Privacy Controls** | `<private>` tags exclude content from storage | Protect sensitive information |
| **Web Viewer** | localhost:37777 dashboard | Browse and search past sessions |

### Integration with This Pattern

| Memory Lifecycle | claude-mem Implementation |
|-----------------|---------------------------|
| PERMANENT | Profile stored in vector database |
| EVERGREEN | Skills and reference content indexed |
| PROJECT | Project context auto-captured per session |
| SESSION | Real-time conversation logging with compression |

### When to Use claude-mem

**Good fit**:
- Teams with many Claude Code sessions to track
- Projects requiring historical context lookup
- Need for automatic conversation archiving
- Privacy requirements (selective capture with `<private>`)

**Overkill**:
- Single-user, single-project workflows
- Projects with simple, self-contained tasks
- When manual CLAUDE.md maintenance is sufficient

### Setup

```bash
# Install via npm
npm install -g claude-mem

# Initialize in project
claude-mem init

# Start web viewer
claude-mem serve
```

For full documentation, see [claude-mem GitHub](https://github.com/thedotmack/claude-mem).

---

## Related Patterns

- [Context Engineering](./context-engineering.md) - Deterministic vs probabilistic context
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient skill loading
- [Documentation Maintenance](./documentation-maintenance.md) - Keeping memory current
- [Long-Running Agent](./long-running-agent.md) - External artifacts for context bridging
- [Session Learning](./session-learning.md) - Cross-session preference capture from corrections

*Last updated: January 2026*
