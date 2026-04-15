# One-Line Project Review Prompt

Copy-paste this prompt into Claude Code in **any project** to get authority-weighted
recommendations based on your recent work patterns and current best practices.

## The Prompt

```
Review this project: read the CLAUDE.md, analyze the last 14 days of git commits (git log --oneline --since="14 days ago" && git log --since="14 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head 20), then fetch https://raw.githubusercontent.com/JW-Corelight/claude-code-project-best-practices/main/SOURCES-QUICK-REFERENCE.md and cross-reference my commit patterns against those sources. Weight recommendations by the source authority tiers (5=Foundational like Anthropic docs, 2=Commentator like YouTube). Prioritize high-authority recent sources. Show what I'm doing well and what to improve, with specific source citations.
```

## What It Does

1. **Reads your CLAUDE.md** — Understands your project's current configuration
2. **Analyzes recent commits** — Identifies patterns in how work is being done
3. **Fetches best-practice sources** — Cross-references against 21 authority-weighted sources
4. **Produces weighted recommendations** — High priority (Foundational sources) vs worth noting (Commentator sources)
5. **Celebrates what works** — Not just criticism; identifies positive patterns to keep

## Expected Output

- Commit pattern summary (file types, AI co-authoring rate, change categories)
- 3-5 high-priority recommendations backed by Foundational/Authoritative sources
- 2-3 medium-priority recommendations backed by Practitioner sources
- "What's working well" section with evidence from commits
- Source citations with authority tier and effective weight for each recommendation

## Authority Weighting

The prompt uses a 0-5 authority scale:
- **5 (Foundational)**: Boris Cherny, Anthropic engineering blog — always relevant
- **4 (Authoritative)**: OWASP, peer-reviewed research, Apache PMC
- **3 (Practitioner)**: Named engineers with production metrics
- **2 (Commentator)**: YouTube creators, bloggers — useful signals but verify claims
- **1 (Unverified)**: Vendor marketing, speculation
- **0 (Rejected)**: Debunked claims

Foundational sources have a recency floor of 0.7 — a 6-month-old Anthropic
engineering blog post (weight 0.70) outweighs a fresh YouTube clickbait video
(weight 0.35) by 2x.

## Customization

Add to the prompt for specific focus areas:
- `...focus on security patterns` — Emphasizes OWASP MCP Top 10, sandboxing
- `...focus on agent architecture` — Emphasizes harness engineering, orchestration
- `...focus on MCP usage` — Emphasizes MCP vs Skills economics, plugin patterns
- `...compare against [other project]` — Cross-project pattern comparison
