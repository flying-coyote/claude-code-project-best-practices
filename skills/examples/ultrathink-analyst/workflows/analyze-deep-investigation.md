# ANALYZE: Deep Investigation Workflow

**Purpose**: Explore solution space, identify risks and benefits, understand trade-offs. Use this workflow after FRAME is complete to investigate alternatives systematically.

---

## A - ALTERNATIVES: Other Approaches

**Explore:**
- Competing solutions and methodologies
- Different vendor approaches or frameworks
- Alternative architectural patterns
- Edge cases and variations

**Questions:**
- What other approaches exist?
- How do competitors solve this?
- What patterns have we not considered?
- What's the null option (do nothing)?

---

## N - NEGATIVES: Failure Modes

**Identify:**
- Failure modes and edge cases
- Unintended consequences
- Hidden costs (technical debt, opportunity cost)
- Worst-case scenarios

**Questions:**
- How might this fail?
- What could go wrong?
- What are we sacrificing?
- What's the downside risk?

---

## A - ADVANTAGES: Benefits

**Document:**
- Primary benefits and value proposition
- Competitive advantages
- ROI and efficiency gains
- Strategic positioning

**Questions:**
- Why would we choose this?
- What do we gain?
- How does this create value?
- What's the upside potential?

---

## L - LIMITATIONS: Constraints

**Acknowledge:**
- Technical limitations
- Resource constraints (time, budget, skills)
- Scaling boundaries
- Feasibility barriers

**Questions:**
- What can't this do?
- What constraints apply?
- Where are the hard limits?
- What's non-negotiable?

---

## Y - YIELD: Expected Results

**Predict:**
- Quantitative outcomes (metrics, KPIs)
- Qualitative improvements
- Timeline and milestones
- Success indicators

**Questions:**
- What results do we expect?
- How long will this take?
- What metrics matter?
- How do we measure success?

---

## Z - ZONES: Scope and Applicability

**Define:**
- Applicable contexts and use cases
- Scope boundaries
- Scaling characteristics
- Transfer potential to other domains

**Questions:**
- Where does this apply?
- What's in/out of scope?
- How does this scale?
- Can we reuse this elsewhere?

---

## E - EVOLUTION: Change Over Time

**Consider:**
- How this changes over time
- Adaptability to future needs
- Maintenance requirements
- Upgrade/migration paths

**Questions:**
- How will this evolve?
- Can we adapt as needs change?
- What's the maintenance burden?
- What's the exit strategy?

---

## Output Format for ANALYZE Phase

```markdown
## ANALYZE: Deep Investigation

### Alternatives
1. **[Option 1]**: [Brief description, key differentiator]
2. **[Option 2]**: [Brief description, key differentiator]
3. **[Option 3]**: [Brief description, key differentiator]

### Negatives (Risks/Costs)
- Failure modes: [how it could fail]
- Unintended consequences: [what we didn't plan for]
- Hidden costs: [technical debt, opportunity cost]
- Worst-case: [bad scenario]

### Advantages (Benefits)
- Primary value: [main benefit]
- Competitive edge: [what makes this better]
- ROI: [quantified if possible]
- Strategic fit: [alignment with goals]

### Limitations
- Technical: [what it can't do]
- Resource: [constraints on time/budget/skills]
- Scaling: [boundaries]
- Feasibility: [hard blockers]

### Yield (Expected Outcomes)
- Quantitative: [metrics, numbers]
- Qualitative: [improvements]
- Timeline: [milestones]
- KPIs: [success measures]

### Zones (Scope)
- Applicable: [where this works]
- Out of scope: [where it doesn't]
- Scaling: [growth characteristics]
- Transfer: [reusability]

### Evolution
- Future changes: [how needs might evolve]
- Adaptability: [flexibility to change]
- Maintenance: [ongoing effort]
- Exit strategy: [how to change course]
```

---

## Trade-Off Analysis Template

For each major decision point, document the trade-off:

```markdown
### Trade-Off: [Decision]

**Option A**:
- Gains: [what we get]
- Loses: [what we give up]

**Option B**:
- Gains: [what we get]
- Loses: [what we give up]

**Recommendation**: [Choice] because [reasoning based on priorities]
```

---

## Anti-Patterns for ANALYZE Phase

**DON'T:**
- ❌ Only consider one alternative (need options for comparison)
- ❌ Ignore risks and failure modes (optimism bias)
- ❌ Use generic benefits ("it's better") - be specific
- ❌ Forget to check scalability
- ❌ Skip the "do nothing" option

**DO:**
- ✅ Consider 3-5 alternatives minimum
- ✅ Document specific failure scenarios
- ✅ Quantify benefits where possible
- ✅ Acknowledge all limitations honestly
- ✅ Include null hypothesis (do nothing) as option

---

**Workflow Version**: 1.0
**Next Phase**: After completing ANALYZE, proceed to SYNTHESIZE workflow (`workflows/synthesize-integration.md`)
**Previous Phase**: FRAME workflow (`workflows/frame-problem-definition.md`)
