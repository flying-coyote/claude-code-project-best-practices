# Prompt: Rethink the Memory/Knowledge Stack Recommendations

**Use after**: Conversation compaction, fresh session, or when revisiting recommendations after new evidence lands.
**Audience**: Claude (running in this repo).
**Expected runtime**: 15–30 minutes of analysis.

---

## How to invoke

Paste the section below labelled `## PROMPT TO PASTE` into a fresh Claude Code session in this repo. Do not include the rest of this file in the prompt — Claude will read the reference docs itself.

---

## What this prompt does

Drives a from-scratch architectural rethink of memory/knowledge system recommendations across project archetypes, evaluating these tools individually and in hybrid combinations:

- Karpathy LLM Wiki (paradigm)
- Graphify (safishamsi)
- Pratiyush/llm-wiki
- MehmetGoekce/llm-wiki (L1/L2 cache)
- Lum1104/Understand-Anything
- zilliztech/claude-context
- OpenBrain (justSteve)
- Rowboat (Avi Chawla, for temporal knowledge)

The output is a revised set of recommendations, opinionated, with hybrid combinations explicitly considered per archetype.

---

## Constraints to honor

These are user-stated constraints that any recommendation must respect:

1. **Graph feeds wiki** — graphify-style structural output should be promoted into wiki content, not sit as a parallel artifact only.
2. **Wiki must not contradict graph** — when the wiki asserts a structural claim, it must align with the graph's confidence level (EXTRACTED / INFERRED / AMBIGUOUS or equivalent).
3. **Evidence tiers** — match this project's A/B/C tiering. Most April 2026 tools are Tier C until reproduced.
4. **Augments-not-generates** preferred for prose-rich projects (this repo's `analysis/` style).
5. **Local-first** preferred over cloud-egress where viable.
6. **Markdown substrate** preferred for long-lived knowledge.

---

## PROMPT TO PASTE

```
You are doing a from-scratch architectural review of memory/knowledge system
choices for second-brain and knowledge-base projects. Do this fresh — do
not rely on prior conversation context. Work from the reference documents.

Read these three reference documents in order before doing anything else:

1. research/memory-systems-tools-inventory.md
   (factual catalog of 8 tools/paradigms with capabilities, licenses, sources)

2. research/memory-systems-architecture-axes.md
   (8 architectural axes that distinguish these tools)

3. research/memory-systems-project-archetypes.md
   (7 project archetypes A–G with axis profiles and starting hybrid suggestions)

User-stated constraints to honor in every recommendation:

- Graphify-style graph output should FEED the wiki (promote findings into
  pages), not sit as a parallel artifact only.
- Wiki must NOT contradict the graph: where the wiki asserts a structural
  claim, that claim must align with the graph's confidence level
  (EXTRACTED / INFERRED / AMBIGUOUS or equivalent).
- Match this project's evidence-tier system (A / B / C). Most April 2026
  tools are Tier C until reproduced.
- Prefer augments-not-generates for prose-rich projects.
- Prefer local-first over cloud-egress where viable.
- Prefer markdown substrate for long-lived knowledge.

For each of the 7 archetypes (A through G in the archetypes doc), produce:

1. PRIMARY STACK — the recommended tool or combination.
   - Name the tools.
   - State which tool owns which architectural layer.
   - Cite which axes drove the choice (use axis numbers from the axes doc).
   - State the evidence tier and why.

2. HYBRID ALTERNATIVES — at least two, ideally three.
   - Each must be a real combination, not a hedge.
   - State what each hybrid optimizes for that the primary stack does not.
   - State when to pick the hybrid over the primary.

3. ANTI-PATTERNS — at least two specific to this archetype.
   - Be concrete: "running X alongside Y on Z-shape repo causes [specific
     failure]."
   - Distinguish from generic anti-patterns.

4. ADOPTION ORDER — sequenced steps to roll out the primary stack.
   - First three steps must be reversible / low-cost.
   - Note where to stop if value isn't yet apparent.
   - Do NOT recommend installing more than two tools simultaneously in
     step 1.

5. CONSTRAINT CHECK — confirm the recommendation satisfies all six
   user-stated constraints, or flag explicitly which it doesn't and why
   that's acceptable for this archetype.

After all 7 archetypes, produce these cross-cutting sections:

A. MIGRATION PATHS — for each pair of archetypes that might evolve into
   each other (e.g., A → D when the analytical KB becomes a portfolio),
   state what migrates and what gets rebuilt.

B. NEVER-COMBINE LIST — specific tool combinations that should not run
   together, with reasoning.

C. LICENSE / COST GOTCHAS — flag every non-MIT license and every cloud
   egress in the stack. State the implication for commercial reuse.

D. BUILD-VS-BORROW DECISIONS — for each archetype's primary stack,
   identify which pieces are missing from off-the-shelf tools and would
   require local custom work (e.g., contradiction lint, footer-injection,
   adapters).

E. EVIDENCE GAPS — list the top five claims in the recommendations that
   are currently Tier C and would benefit most from independent
   reproduction. State what experiment would move them to Tier B.

OUTPUT FORMAT:

- Use clear hierarchical markdown headings.
- Use tables wherever a comparison is being made.
- Cite source URLs from the inventory doc when stating tool capabilities.
- Do not exceed ~3000 words total. Cut filler over coverage if forced to
  choose.
- End with a "What I would do this week" section: 3–5 concrete actions
  the user can take in the next 7 days to start adoption, with explicit
  bash/install commands and a stop-condition for each.

DO NOT:

- Re-summarize the inventory or axes docs. Reference them by name.
- Give every archetype the same primary stack. Differences should be
  visible.
- Hedge into "it depends" without naming what it depends on.
- Recommend tools whose licenses you have not checked against the
  constraint list.
```

---

## After Claude completes the rethink

Suggested follow-ups for refinement:

1. Ask Claude to **run the constraint check inversely**: for each of the 6 user-stated constraints, list which archetype's recommendation is most at-risk of violating it.

2. Ask Claude to **identify the single highest-value piece of custom work** across all archetypes (the thing that would unlock the most of these stacks at once).

3. Ask Claude to **propose two new archetypes** not in the current list that are worth tracking for future revision.

4. Ask Claude to **score each tool's roadmap risk** — what features are advertised but not yet shipped (e.g., OpenBrain's compilation agent, graphify's MCP for some configs).

5. If a specific portfolio repo is in scope, ask Claude to **map that repo to one or more archetypes** and run the recommendation procedure for that specific case, including reading the repo's actual `README.md`, `INDEX.md`, and a sample of `analysis/` content first.

---

## Maintenance

Update this prompt and its reference docs when:

- A new tool ships that meaningfully fills an archetype gap (especially
  if it ships the missing write-back loop or a true hybrid).
- An axis becomes obsolete or a new one emerges (e.g., if the
  topology-vs-embeddings split disappears because all tools become
  hybrid).
- Production evidence elevates any current Tier C claim to Tier B.

Last revised: 2026-04-27.
