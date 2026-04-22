---
evidence-tier: Mixed
applies-to-signals: [model-version-4-7, model-version-4-6, model-version-4-5, model-version-migration, model-version-unknown, claude-md-vague-descriptors]
last-verified: 2026-04-22
revalidate-by: 2026-10-22
status: PRODUCTION
---

# Model Migration Anti-Patterns

**Evidence Tier**: Mixed (A-B) — Anthropic migration guide (Tier A) + practitioner commentary (Tier B) + community observation (Tier C counter-signals)

## Purpose

This document is a **diagnostic checklist**, not a migration how-to. When a new Claude model ships, prompts and harnesses validated on the prior version can silently regress. The six anti-patterns below map each failure mode to the model version that introduced or exacerbated it, the Tier A evidence, and a specific remediation.

The framing answers: *"Which of my existing prompts are likely to break, and why?"*

---

## The Silent No-Op Problem

Opus 4.7's headline behavioral change is **literal instruction interpretation**. The Anthropic migration guide states, verbatim:

> "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make."
>
> — [Anthropic Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)

The practical consequence: prompts that worked on 4.6 because the model *helpfully inferred intent* now produce silent no-ops on 4.7. The prompt appears valid, the model returns a plausible response, but the actual instruction is never executed.

**This is not a "hot take."** Jason Vertrees's widely-shared [LinkedIn piece](https://www.linkedin.com/pulse/claude-47-quietly-break-your-prompts-harness-heres-how-jason-vertrees-mscpe/) operationalized this advisory into six anti-patterns. His contribution is the audit framework; the underlying claim is Anthropic's own.

---

## Cross-Version Anti-Pattern Matrix

| Anti-pattern | 4.5 | 4.6 | 4.7 | Primary source |
|---|---|---|---|---|
| Vague quality descriptors ("best practices," "idiomatic," "robust") | Tolerated | Tolerated | **Silent no-op** | Anthropic migration guide |
| Edge-case gestures ("consider edge cases," "handle corner cases") | Works | Works | **Silent no-op** — model no longer infers *which* cases | Anthropic migration guide |
| Unanchored triggers ("where applicable," "as needed," "if relevant") | Works | Works | **Silent no-op** — conditions never fire | Anthropic migration guide |
| Implicit subagent dispatch ("execute the tasks," "dispatch the work") | Spawns liberally | Spawns liberally | **Fewer subagents by default** — dispatch must be explicit | Anthropic migration guide (verbatim: "Fewer subagents spawned by default. Steerable through prompting.") |
| Missing verbosity directives (no length caps, no "no preamble") | Fixed default verbosity | Fixed default verbosity | **Adaptive verbosity** — response length calibrates to perceived complexity; add `"Provide concise, focused responses..."` | Anthropic migration guide |
| References without read-enforcement ("see rules/data-isolation.md for restrictions") | Often read | Often read | **Frequently not read** — mechanical enforcement required | Anthropic migration guide + [progressive-disclosure analysis](claude-md-progressive-disclosure.md) |

**Anti-patterns adapted from Vertrees (LinkedIn, April 2026). Version-severity column is our own cross-reference to the Tier A migration guide.**

---

## Remediation Patterns (and One Tension)

### Preferred remediation per anti-pattern

| Anti-pattern | Positive-framed fix | Why positive |
|---|---|---|
| Vague quality descriptors | Point to specific standards doc or enumerate 3-5 rules inline | Gives the model concrete targets to hit |
| Edge-case gestures | Enumerate the cases that matter ("handle: null, empty, unicode, >10MB") | Names the work |
| Unanchored triggers | State explicit firing conditions ("when the caller passes `strict=true`, validate…") | Converts inference to control flow |
| Implicit subagent dispatch | Declare mechanism: "Use the Explore subagent to..." or "complete in-context without subagents" | Matches 4.7's explicit-dispatch default |
| Missing verbosity directives | Add concision directive + output format template | Aligns with adaptive verbosity |
| Unread references | Enforce via PreToolUse hook, explicit `Read tool` step in the instruction, or required-reading block at the top of CLAUDE.md | Moves enforcement from inference to mechanics |

### The MUST/MUST NOT tension

Vertrees's audit prescribes "MUST / MUST NOT rules" as a primary remediation. **This conflicts with Anthropic's stated preference in the same migration guide:**

> "Positive examples... tend to be more effective than negative examples or instructions that tell the model what not to do."

**Diagnostic guidance for this repo:** prefer positive enumeration (what *to do*, with examples) over MUST NOT lists. Reserve MUST NOT for genuine safety/compliance constraints where the negative framing is load-bearing (secrets handling, destructive operations). This matches the broader [Harness Engineering](harness-engineering.md) principle that enforcement should live in mechanics (hooks, sandboxes), not in exhortation.

---

## What Literalism Does *Not* Mean

Literalism is **selective, not uniform**. Simon Willison's [analysis of the leaked 4.7 system prompt](https://simonwillison.net/2026/Apr/18/opus-system-prompt/) surfaces a counter-signal: Anthropic explicitly tuned 4.7 to be *less* literal about clarifying questions.

> "The person typically wants Claude to make a reasonable attempt now, not to be interviewed first."
> — Opus 4.7 system prompt (leaked)

**Implication for prompt design**: 4.7 won't generalize across instructions, but it *will* generalize across conversation-turn intent (e.g., "just start working"). Audits that treat literalism as uniform will over-correct.

---

## Community Counter-Signals (Tier C)

Practitioner reports from the Opus 4.7 release window surface failure modes not yet documented by Anthropic:

| Report | Source | Implication |
|---|---|---|
| "Adaptive thinking chooses to not think when it should" — workaround = `xhigh` + explicit thinking-summary config | [HN 47793411](https://news.ycombinator.com/item?id=47793411) (1,955 points) | Default effort calibration may under-trigger thinking on reasoning-heavy tasks |
| 4.7 over-applies system-reminder instructions (e.g., malware check) to *every* file read | [HN 47814832](https://news.ycombinator.com/item?id=47814832) | Red-teamers report "close to unusable" for certain workflows — literalism can over-fire on reminders |

Both are single-thread observations without independent validation. Track for broader corroboration before acting on them.

---

## Audit Workflow

For a repository migrating from 4.6 → 4.7:

1. **grep for vague descriptors** — `grep -nE "best practices|idiomatic|robust|proper|clean" prompts/ skills/ CLAUDE.md`
2. **grep for unanchored triggers** — `grep -nE "where applicable|as needed|if relevant|consider" prompts/ skills/`
3. **grep for references without enforcement** — find every `.md` cross-reference in CLAUDE.md/skills and verify each has (a) an explicit `Read` step, (b) a PreToolUse hook, or (c) a required-reading block.
4. **Identify implicit subagent dispatch** — search for "dispatch," "execute the tasks," "handle X, Y, Z" without naming an agent mechanism.
5. **Add a verbosity directive** — CLAUDE.md or top-level prompt gets: `"Provide concise, focused responses unless asked otherwise."`
6. **Run side-by-side** — same prompt on 4.6 and 4.7 via Claude Code CLI; diff outputs for silent no-ops.

This repo's own audit (performed 2026-04-22) surfaced 16 Opus 4.5/4.6 references in `analysis/` that need revalidation framing. Tracked in [Evidence-Based Revalidation](evidence-based-revalidation.md).

---

## Related Analysis

This doc is cited by (inbound) and cites (outbound) the following. Use the bidirectional links to pivot between version-behavior (here) and the specific practice affected.

**Outbound — docs this one draws on**:

- [Behavioral Insights](behavioral-insights.md#prompt-sensitivity-across-model-versions) — version-by-version prompt sensitivity table
- [Harness Engineering](harness-engineering.md) — 4.7 pushes *prompt* complexity up even as *harness* simplifies
- [CLAUDE.md Progressive Disclosure](claude-md-progressive-disclosure.md) — references-without-read-enforcement is the 4.7 failure mode that most affects progressive-disclosure
- [Evidence-Based Revalidation](evidence-based-revalidation.md) — model migrations are a canonical revalidation trigger
- [Agent Evaluation](agent-evaluation.md) — implicit subagent dispatch as an evaluation anti-pattern

**Inbound — docs that cite this one**:

- [Behavioral Insights](behavioral-insights.md) — links here for the MUST-vs-positive tension and the six failure modes
- [Harness Engineering](harness-engineering.md) — links here from its 4.7 counter-signal row
- [CLAUDE.md Progressive Disclosure](claude-md-progressive-disclosure.md) — links here from the Opus 4.7 references-without-read-enforcement warning
- [Agent Evaluation](agent-evaluation.md) — links here from the implicit-subagent-dispatch anti-pattern
- [Agent Principles](agent-principles.md) — links here from the 4.7 regression anti-pattern
- [Evidence-Based Revalidation](evidence-based-revalidation.md) — links here from the 4.6 → 4.7 case study
- [Session Quality Tools](session-quality-tools.md) — relevant for distinguishing 4.7 silent-no-op sessions from normal low-signal sessions

## Sources

- Anthropic Migration Guide (Tier A): https://platform.claude.com/docs/en/about-claude/models/migration-guide
- What's New Claude 4.7 (Tier A): https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- Best Practices for Opus 4.7 with Claude Code (Tier A): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
- Jason Vertrees, "Claude 4.7 Quietly Broke Your Prompts and Harness" (Tier B, LinkedIn, April 2026)
- Simon Willison, Opus 4.7 system-prompt analysis (Tier B, April 18, 2026)
- HN discussions 47793411, 47814832 (Tier C, community observation)

**Gap**: No independent benchmark yet comparing 4.6 vs 4.7 on the six anti-patterns. Tracking for corroboration in subsequent revalidation cycles.

---

*Last updated: April 2026*
