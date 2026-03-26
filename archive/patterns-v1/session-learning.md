---
version-requirements:
  claude-code: "v2.1.30+"  # Session memory feature
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "Self-training reduced safety refusal rates by 70% (safety drift risk)"
    source: "Academic research on misevolution"
    date: "2025-09-01"
    revalidate: "2026-09-01"
  - claim: "Reflection-based learning bumped pass@1 from GPT-4 baseline 91% up"
    source: "Coding benchmarks research"
    date: "2025-09-01"
    revalidate: "2026-09-01"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Session Learning Pattern

**Source**: Claude Diary (Lance Martin), Generative Agents paper, Yohei Nakajima research
**Evidence Tier**: B (Expert practitioner implementations + academic research)

## Overview

Session learning captures durable preferences from corrections and approvals during coding sessions, then proposes updates to persistent configuration (CLAUDE.md, skills). This creates a **feedback loop** that reduces repeated corrections over time.

**SDD Phase**: Cross-phase (enhances all phases through accumulated context)

> "Every tasklist is analyzed alongside the output to generate a 'reflection' that is stored alongside the objective. This mimics the ability to improve through repetition."
> — Yohei Nakajima, BabyAGI Creator

---

## The Problem

| Issue | Impact |
|-------|--------|
| Corrections don't persist | User repeats same feedback across sessions |
| Implicit preferences invisible | CLAUDE.md only captures explicit instructions |
| Session insights lost | Valuable patterns forgotten when conversation ends |
| Manual memory maintenance | Users rarely update CLAUDE.md proactively |

**Solution**: Systematic capture of corrections → pattern detection → human-reviewed updates.

---

## Core Concept: Three-Tier Architecture

Based on the [Generative Agents paper](https://arxiv.org/abs/2304.03442) (Stanford, 2023):

```
┌─────────────────────────────────────────────────────────────┐
│                    SESSION LEARNING                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐ │
│  │ OBSERVATION  │ ──► │  REFLECTION  │ ──► │  RETRIEVAL   │ │
│  │              │     │              │     │              │ │
│  │ Capture      │     │ Detect       │     │ Apply in     │ │
│  │ corrections  │     │ patterns     │     │ future       │ │
│  │ during       │     │ (2+ occur-   │     │ sessions     │ │
│  │ session      │     │ rences)      │     │              │ │
│  └──────────────┘     └──────────────┘     └──────────────┘ │
│        │                     │                    │         │
│        ▼                     ▼                    ▼         │
│   /diary or hook       /reflect             CLAUDE.md      │
│                     (human review)           updates        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Signal Detection

### What to Capture

| Signal Type | Priority | Examples |
|-------------|----------|----------|
| **Corrections** | Highest | "No, use X instead of Y", "Actually, we do it this way" |
| **Repeated patterns** | High | Same feedback given 2+ times |
| **Explicit markers** | High | "Remember:", "Always:", "Never:" |
| **Approvals** | Supporting | "Yes, that's right", "Perfect" |

### What NOT to Capture

| Signal Type | Why Exclude |
|-------------|-------------|
| One-off context | Applies only to current task |
| Universal best practices | Already in Claude's training |
| Framework conventions | Standard patterns, not project-specific |
| Ambiguous feedback | Too unclear to be actionable |
| Contradictory signals | Conflicting guidance in same session |

### Quality Filter (4 Questions)

Before proposing any update, verify:

1. **Repeated or general?** — Was this stated as a rule, not a one-time preference?
2. **Future applicability?** — Would this apply to future sessions?
3. **Specific enough?** — Is it actionable, not vague?
4. **Genuinely new?** — Not already known or standard practice?

---

## Reference Implementations

### Claude Diary (Lance Martin) — Recommended

**Tier**: B (Expert practitioner — LangChain founder)
**Repository**: [github.com/rlancemartin/claude-diary](https://github.com/rlancemartin/claude-diary)

**Architecture**:
- `/diary` — Captures session summary (manual or PreCompact hook)
- `/reflect` — Analyzes diary entries for patterns, proposes CLAUDE.md updates
- Human review required before any modifications

**Why Recommended**:
- Separates capture from apply (safe by default)
- Based on academic research (Generative Agents)
- Human-in-the-loop for all writes
- Git-based rollback via commits

**Setup**:
```bash
git clone https://github.com/rlancemartin/claude-diary
cp commands/*.md ~/.claude/commands/
cp hooks/pre-compact.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/pre-compact.sh
```

### Claude Reflect (Bayram Annakov)

**Tier**: C (Community implementation)
**Repository**: [github.com/BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect)

**Architecture**:
- Hook-based automatic correction detection
- Detects patterns: "no, use X", tool rejections, "remember:" markers
- `/reflect` reviews queued learnings before applying

### Autoskill (AI-Unleashed)

**Tier**: C (Community, minimal documentation)
**Repository**: [github.com/AI-Unleashed/Claude-Skills](https://github.com/AI-Unleashed/Claude-Skills)

**Architecture**:
- Meta-skill that updates other skill files
- Signal detection with quality filter
- Confidence levels (HIGH/MEDIUM) for proposals

**Caution**: Updates skill files directly — higher risk than CLAUDE.md-only approaches.

### Claude-mem (thedotmack)

**Tier**: C (Community, production-focused)
**Repository**: [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

**Architecture**:
- Biomimetic memory with AI compression
- 5 lifecycle hooks for complete capture
- Vector search for semantic retrieval

**Note**: Focuses on memory capture, not preference learning. Complementary to session learning.

---

## Safety Requirements

### Critical: Human-in-the-Loop

> "Keep a human-in-the-loop failsafe for critical updates."
> — [OpenAI Cookbook: Self-Evolving Agents](https://cookbook.openai.com/examples/partners/self_evolving_agents/autonomous_agent_retraining)

**Non-negotiable**: All writes to persistent configuration (CLAUDE.md, skills) MUST require human approval.

### The Misevolution Risk

Research has identified **misevolution** — where self-improvement processes drift into unsafe behaviors:

| Risk Pathway | Description | Mitigation |
|--------------|-------------|------------|
| **Memory misevolution** | Accumulated experience biases future behavior | Periodic review of accumulated rules |
| **Semantic corruption** | Errors in stored preferences distort all future plans | Version control, rollback capability |
| **Safety drift** | Self-training reduced safety refusal rates by 70% in studies | Never auto-apply without review |
| **Overfitting** | Agent becomes too specialized to user's quirks | Cross-project pattern detection |

**Source**: [Research on self-evolving agents](https://medium.com/@huguosuo/your-agent-may-misevolve-emergent-risks-in-self-evolving-llm-agents-2f364a6de72e)

### Required Safeguards

| Safeguard | Implementation |
|-----------|----------------|
| **Human review** | Preview all changes before applying |
| **Git-based rollback** | Commit all changes for reversal |
| **Rate limiting** | Max N updates per day/week |
| **Confidence thresholds** | Only HIGH confidence shown by default |
| **Audit log** | Track all modifications with timestamps |
| **Contradiction detection** | Flag when new learning conflicts with existing |

---

## Implementation Checklist

### Minimal Safe Implementation

- [ ] Install Claude Diary commands (`/diary`, `/reflect`)
- [ ] Configure PreCompact hook for automatic diary capture
- [ ] Review `/reflect` output before approving changes
- [ ] Commit CLAUDE.md changes to git after updates

### Enhanced Implementation

- [ ] Add rate limiting (weekly review cadence)
- [ ] Create audit log for all preference updates
- [ ] Implement contradiction detection vs. existing CLAUDE.md
- [ ] Set up monthly review of accumulated preferences

---

## Workflow Example

### Session with Corrections

```
User: Generate the API endpoint
Claude: [Generates with snake_case]
User: No, we use camelCase for all API responses
Claude: [Regenerates with camelCase]
...
User: /diary
```

### Diary Captures

```markdown
# Session 2026-01-11-session-1

## Corrections Received
- API responses should use camelCase, not snake_case

## Decisions Made
- Implemented user authentication endpoint

## Patterns Noted
- User prefers explicit error messages over generic ones
```

### Reflection Identifies Pattern

```
User: /reflect last 10 entries
```

```markdown
## Proposed CLAUDE.md Updates

### HIGH Confidence (3+ occurrences)
1. **API Naming Convention**
   - Signal: "use camelCase" (found in 4 sessions)
   - Proposed addition to CLAUDE.md:
     ```
     ## API Standards
     - Use camelCase for all JSON response fields
     ```
   - [Approve] [Skip] [Edit]

### MEDIUM Confidence (2 occurrences)
2. **Error Message Style**
   - Signal: "be more explicit about errors" (2 sessions)
   - [Approve] [Skip] [Edit]
```

---

## Integration with Memory Architecture

Session learning extends the [Memory Architecture](./memory-architecture.md) pattern:

| Memory Lifecycle | Session Learning Role |
|-----------------|----------------------|
| **PERMANENT** | Session learning populates preferences over time |
| **EVERGREEN** | `/reflect` can update skills, not just CLAUDE.md |
| **PROJECT** | Project-specific corrections stay in project CLAUDE.md |
| **SESSION** | Corrections captured during session, persisted via `/diary` |

**Key Insight**: Session learning provides the **mechanism** for moving valuable SESSION-scoped insights to PERMANENT storage.

---

## Anti-Patterns

### DON'T: Auto-Apply Without Review

```json
// DANGEROUS - Never do this
{
  "hooks": {
    "SessionEnd": [{
      "command": "auto-update-claude-md.sh"  // No human review!
    }]
  }
}
```

### DON'T: Capture Everything

Capturing one-off corrections leads to:
- Bloated CLAUDE.md
- Conflicting rules
- Overfitting to edge cases

### DON'T: Skip Rollback Mechanism

Without git commits for changes:
- No way to undo bad updates
- No audit trail
- Semantic corruption compounds silently

### DO: Separate Capture from Apply

```
/diary → Capture (automatic, safe)
/reflect → Review (human required)
[Approve] → Apply (explicit action)
```

---

## Expert Perspectives

### Yohei Nakajima (BabyAGI Creator)

> "What stood out was the ability to learn over time. When running a new objective, it performs a vector search to find similar past objectives, pulls in reflection notes... This has worked in giving BabyAGI the ability to create better tasklists over time."

**Key insight**: Tie reflection to **outcomes**, not just corrections.

### Lance Martin (LangChain)

> "I kept reflection manual because it updates CLAUDE.md directly. I wanted to review the proposed updates."

**Key insight**: Human review is essential for persistent configuration.

### Academic Research (Reflexion Paper)

> "Reflexion lets an LLM agent solve a task, see that it failed, write a natural-language critique of its own attempt, store that 'reflection,' and try again. On coding benchmarks, this bumped pass@1 from GPT-4 baseline to ~91%."

**Key insight**: Self-critique improves performance when structured properly.

---

## Related Patterns

- [Memory Architecture](./memory-architecture.md) — Lifecycle-based information management
- [Documentation Maintenance](./documentation-maintenance.md) — Keeping CLAUDE.md current
- [Long-Running Agent](./long-running-agent.md) — External artifacts as memory
- [Recursive Evolution](./recursive-evolution.md) — Judge feedback loops (similar concept)
- [Agent Principles](./agent-principles.md) — Addresses Principle 1 (Persistent Memory)

---

## Sources

- [Claude Diary](https://github.com/rlancemartin/claude-diary) — Lance Martin (Tier B)
- [Generative Agents Paper](https://arxiv.org/abs/2304.03442) — Stanford, 2023 (Tier B)
- [Yohei Nakajima: Self-Improving Agents](https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/) (Tier B)
- [Misevolution Research](https://medium.com/@huguosuo/your-agent-may-misevolve-emergent-risks-in-self-evolving-llm-agents-2f364a6de72e) (Tier B)
- [OpenAI Cookbook: Self-Evolving Agents](https://cookbook.openai.com/examples/partners/self_evolving_agents/autonomous_agent_retraining) (Tier A)
- [Claude Reflect](https://github.com/BayramAnnakov/claude-reflect) (Tier C)
- [Autoskill](https://github.com/AI-Unleashed/Claude-Skills) (Tier C)

*Last updated: January 2026*
