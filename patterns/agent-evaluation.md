# Agent Evaluation Patterns

**Sources**:
- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Evidence Tier A)
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/designing-ai-resistant-technical-evaluations) (Evidence Tier A)
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/quantifying-infrastructure-noise-in-agentic-coding-evals) (Evidence Tier A)

**Evidence Tier**: A (Three primary vendor blog posts)

**SDD Phase**: Cross-phase (evaluation informs all phases)

## The Core Problem

Building AI agents without evaluations is like deploying software without tests. You can't improve what you can't measure, and you can't trust what you haven't verified.

Yet most teams skip evals because they seem complex. Anthropic's guidance shows they don't have to be.

---

## When to Start Evaluating

Start with **20-50 tasks derived from real failures**. Don't wait for a comprehensive eval suite — begin with cases where your agent actually failed.

### Task Sources

| Source | Example | Priority |
|--------|---------|----------|
| **Production failures** | "Agent deleted wrong file" | HIGH |
| **User complaints** | "Took 5 retries to get right answer" | HIGH |
| **Edge cases discovered** | "Fails on monorepos with symlinks" | MEDIUM |
| **Regression candidates** | "Fixed bug that could recur" | MEDIUM |
| **Capability probes** | "Can it handle X?" | LOW |

### Minimum Viable Eval

```markdown
## Eval: [Task Name]

**Input**: [Exact prompt or scenario]
**Expected**: [What should happen]
**Pass criteria**: [How to verify — automated if possible]
**Category**: [correctness | safety | efficiency | style]
```

---

## Eight Evaluation Patterns

From Anthropic's "Demystifying Evals for AI Agents":

### 1. Golden Answer Comparison

Compare agent output to a known-correct answer.

**Best for**: Factual tasks, code generation with test suites
**Limitation**: Doesn't capture valid alternative approaches

### 2. Rubric-Based Scoring

Score outputs against a multi-dimensional rubric.

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Correctness | 40% | Produces expected output |
| Efficiency | 20% | Minimal unnecessary operations |
| Safety | 25% | No destructive actions |
| Style | 15% | Follows project conventions |

**Best for**: Open-ended tasks with multiple valid solutions

### 3. Pairwise Comparison

Compare two agent outputs (or agent vs human) side by side.

**Best for**: Evaluating model upgrades, prompt changes
**Tool**: Use an LLM judge to compare outputs

### 4. Task Completion Rate

Binary: did the agent complete the task or not?

**Best for**: Baseline capability assessment
**Metric**: Pass rate across N attempts (account for non-determinism)

### 5. Human Evaluation

Human reviewers score agent outputs.

**Best for**: Subjective quality, user experience, safety review
**Limitation**: Expensive, slow, inconsistent between reviewers

### 6. Regression Testing

Re-run known-good tasks after changes to verify no degradation.

**Best for**: Model upgrades, prompt modifications, tool changes
**Implementation**: Maintain a suite of golden tasks

### 7. Adversarial Testing

Deliberately try to make the agent fail.

**Best for**: Safety evaluation, edge case discovery
**Examples**: Ambiguous instructions, conflicting requirements, large inputs

### 8. Cost/Latency Tracking

Measure resource consumption alongside quality.

| Metric | Baseline | Target |
|--------|----------|--------|
| Tokens per task | X | X ± 20% |
| Time to completion | Y sec | Y ± 30% |
| API cost | $Z | $Z ± 25% |

**Best for**: Production monitoring, optimization decisions

---

## Infrastructure Noise

**Source**: [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/quantifying-infrastructure-noise-in-agentic-coding-evals)

A critical insight: **infrastructure noise is a significant confounder in agentic coding evaluations**. Non-deterministic environments (network latency, filesystem state, tool availability) can make eval results unreliable.

### Sources of Noise

| Source | Impact | Mitigation |
|--------|--------|------------|
| **Network latency** | Variable API response times | Run evals in consistent network environments |
| **Filesystem state** | Leftover files from previous runs | Clean state before each eval run |
| **Tool versioning** | Different tool versions produce different results | Pin all tool versions |
| **Model non-determinism** | Same prompt → different outputs | Multiple runs + statistical analysis |
| **Resource contention** | CPU/memory affects execution | Dedicated eval infrastructure |

### Best Practices for Reliable Evals

1. **Isolate eval environments** — Containers or VMs with consistent state
2. **Run multiple times** — 3-5 runs minimum, report median + variance
3. **Control for infrastructure** — Same hardware, same network, same tool versions
4. **Separate model noise from infra noise** — Run identical prompts with fixed seeds when possible
5. **Report confidence intervals** — Not just point scores

---

## Designing AI-Resistant Evaluations

**Source**: [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/designing-ai-resistant-technical-evaluations)

As AI capabilities improve rapidly, evaluations must be designed to remain valid. Key principles:

### Avoid Benchmark Saturation

If your eval maxes out quickly, it stops providing signal. Design evaluations with:
- **Difficulty gradients** — Easy, medium, hard tasks in known ratios
- **Open-ended components** — Tasks where "better" has no ceiling
- **Evolving benchmarks** — Add new tasks periodically

### Measure Genuine Capability

- Test understanding, not pattern matching
- Include novel scenarios not in training data
- Require multi-step reasoning, not single-shot answers
- Verify the agent can explain its approach, not just produce output

---

## Practical Eval Checklist

For teams building agent evaluations:

### Getting Started (Week 1)
- [ ] Collect 20 real failure cases from production/testing
- [ ] Write pass/fail criteria for each
- [ ] Run baseline evaluation and record results
- [ ] Identify top 3 failure categories

### Building the Suite (Week 2-4)
- [ ] Expand to 50 tasks across multiple categories
- [ ] Add automated verification where possible
- [ ] Set up reproducible eval environment (container or VM)
- [ ] Run 3+ times to establish variance baseline

### Ongoing (Monthly)
- [ ] Add new failure cases as they're discovered
- [ ] Re-run full suite after model/prompt changes
- [ ] Track metrics over time (pass rate, cost, latency)
- [ ] Review and retire outdated evals

---

## Application to Claude Code

For teams using Claude Code with custom CLAUDE.md, skills, and hooks:

| What to Evaluate | How |
|-------------------|-----|
| **CLAUDE.md effectiveness** | Does adding/removing lines change task success rate? |
| **Skill quality** | Do skills improve output vs no-skill baseline? |
| **Hook reliability** | Do hooks fire correctly? Do they catch what they should? |
| **Model upgrades** | Does switching Opus versions change outcomes? |
| **Prompt changes** | A/B test prompt modifications |

---

## Anti-Patterns

### ❌ Evaluating Only Happy Paths
**Problem**: Testing only cases where the agent should succeed
**Symptom**: High pass rate but frequent production failures
**Solution**: Include adversarial, edge case, and failure-mode tasks

### ❌ Single-Run Evaluation
**Problem**: Running each eval once and treating the result as definitive
**Symptom**: Flaky results, "it worked on my machine"
**Solution**: Multiple runs with statistical analysis

### ❌ Ignoring Infrastructure Noise
**Problem**: Attributing infrastructure issues to model capability
**Symptom**: Inconsistent results across environments
**Solution**: Controlled environments, noise measurement, confidence intervals

### ❌ Evaluating Too Late
**Problem**: Building evals only after the agent is "done"
**Symptom**: Discovering fundamental issues late in development
**Solution**: Start with 20 tasks from real failures on day one

---

## Related Patterns

- [Subagent Orchestration](./subagent-orchestration.md) - Evaluating multi-agent coordination
- [Context Engineering](./context-engineering.md) - Context quality affects eval results
- [Evidence Tiers](./evidence-tiers.md) - Applying evidence standards to eval results
- [Confidence Scoring](./confidence-scoring.md) - Scoring methodology applicable to evals

---

## Sources

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (January 2026)
- [Designing AI-Resistant Technical Evaluations](https://www.anthropic.com/engineering/designing-ai-resistant-technical-evaluations) (January 2026)
- [Quantifying Infrastructure Noise in Agentic Coding Evals](https://www.anthropic.com/engineering/quantifying-infrastructure-noise-in-agentic-coding-evals) (February 2026)

*Last updated: February 2026*
