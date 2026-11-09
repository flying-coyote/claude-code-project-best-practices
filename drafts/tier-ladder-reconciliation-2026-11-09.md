---
status: proposal
convergence: single-source
---

# Proposal: reconcile the A–D source-tier ladder (staged for an owner ruling, 2026-11-09)

Nothing in this file is applied. It records a taxonomy question the 2026-11-09 evidence-and-method pass raised, with options and a recommended default, so the owner can rule on it.

## The problem

[`analysis/evidence-tiers.md`](../analysis/evidence-tiers.md) § Source Quality Tiers ranks sources this way:

- Tier A, "Primary Sources": direct observation, production data, official documentation, including "Anthropic's own engineering blog posts", "Your own production implementation results" and "Official vendor documentation".
- Tier B, "Peer-Reviewed & Expert": "Peer-reviewed academic papers", expert interviews, conference proceedings.
- Tier C, "Industry & Analysis": industry reports, "vendor documentation", vendor whitepapers, practitioner blog posts.

Three consequences follow for a reader trying to judge whether one method works better than another.

1. **Self-report outranks peer review.** A vendor blog post measuring its own agent (Vercel's n=5 tool-removal post, A in `harness-engineering.md`) sits above a peer-reviewed benchmark paper (SWE-Bench Mobile, KDD '26, B). An interview figure ("CLAUDE.md is followed ~80% of the time") is labelled "High (Tier A practitioner)" in `behavioral-insights.md`.
2. **Vendor documentation appears in two tiers** (A as "official vendor documentation", C as "vendor documentation"), so the same source type can be cited at either level.
3. **It disagrees with the maintainer's other public research repo.** The literature review at `flying-coyote/security-data-literature-review` uses A for peer-reviewed research and official standards, B for practitioners, talks and expert interviews, and C for blog posts and vendor marketing, and splits vendor product documentation: B for what a feature does, C with the bias flagged for how well it works, how fast it is or how it compares (ruling of 2026-11-03).

`SOURCES.md` already flags the strain once: the SWE-Bench Mobile entry says "Tier decision flagged for a human", because peer review holds it at B while the Agentic Context Engineering paper was promoted to A on the strength of ICLR.

There is a defensible reason for the current ladder: for questions about what Claude Code itself does, Anthropic is the authority on its own product, and this repo is mostly about that product. The split ruling in option 2 below keeps that reason while removing the inversion for performance claims.

## Options

1. **Keep the ladder, publish the mapping.** Add a short table to `evidence-tiers.md` mapping each tier here to the literature-review ladder, and fix the vendor-documentation duplicate. Cheapest; leaves self-report above peer review for performance claims.
2. **Split by claim type (recommended default).** Keep vendor and first-party sources at A for *what a feature does or how the product is configured*, and grade every claim about *how well something works, how fast, or how it compares* by the source's method: peer-reviewed or published-method measurements first, vendor self-measurement at C with the bias flagged. This mirrors the 2026-11-03 literature-review ruling and needs a pass over the `Tier A` performance claims in the evidence tables (the Vercel row, the auto-mode classifier rates, the 80% adherence figure, the 50% skills-vs-MCP figure).
3. **Adopt the literature-review ladder outright.** Most consistent across the two repos; the largest re-tiering pass, and it moves first-party mechanism documentation to B, which reads oddly in a repo about one vendor's product.

## What a ruling should record

The option chosen, the date, and, if option 2 or 3, which docs the re-tier pass touches, as a decision in `DECISIONS.md` and an owner exception entry if the pass lands before the change has converged.
