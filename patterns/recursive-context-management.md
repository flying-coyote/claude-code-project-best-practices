# Recursive Context Management (RLM)

**Source**: [alexzhang13/rlm](https://github.com/alexzhang13/rlm) (Alex Zhang, MIT CSAIL)
**Paper**: [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) (Zhang, Kraska, Khattab)
**Industry Analysis**: [Prime Intellect - "The Paradigm of 2026"](https://www.primeintellect.ai/blog/rlm)
**Evidence Tier**: B (Academic research + industry recognition, no Claude-specific validation)

> **Status: EMERGING PATTERN** - Monitor for Claude-specific validation before production adoption.

## Overview

Recursive Language Models (RLM) represent an inference paradigm where models **programmatically examine, decompose, and recursively call themselves** over context stored as a variable. Instead of fitting everything into a single forward pass, the model decides how to explore, partition, and process its input.

Prime Intellect calls RLM "the paradigm of 2026" because it addresses context rot through learned behavior rather than external orchestration.

**SDD Phase**: Cross-phase (theoretical foundation for context management)

---

## The Problem: Context Rot

> "If I split the context into two model calls, then combine them in a third model call, I'd avoid this degradation issue."
> — Alex Zhang

**Context rot** = performance degradation as context window fills, beyond what benchmarks capture. This is observable in:
- Long Claude Code sessions where quality degrades
- Extended conversations that lose coherence
- Large codebase analysis that misses obvious patterns

Standard benchmarks (like RULER) don't capture this phenomenon because they test specific needle-in-haystack retrieval, not holistic reasoning over accumulated context.

---

## How RLM Works

### Traditional vs RLM Inference

```
TRADITIONAL LLM:
[Full Context (100K+ tokens)] → [Single Forward Pass] → [Answer]
                                      ↓
                              (context rot degrades quality)

RLM:
[Query + REPL Access to Context Variable]
              ↓
[Model decides: peek, grep, partition, summarize]
              ↓
[Spawns sub-LLM calls on chunks as needed]
              ↓
[Combines results, refines iteratively]
              ↓
[FINAL(answer)]
```

### Key Innovation: Model-Managed Context

Instead of external systems (orchestrators, vector DBs) managing what context the model sees, RLM gives the model a Python REPL where context exists as a variable. The model learns to:

1. **Peek**: Examine initial portions to understand structure
2. **Grep**: Use regex patterns to narrow relevant sections
3. **Partition + Map**: Chunk context and launch recursive sub-calls
4. **Summarize**: Create digests for higher-level reasoning

These behaviors emerge through reinforcement learning, not explicit prompting.

---

## Benchmark Results

| Benchmark | Standard Approach | RLM Approach | Improvement |
|-----------|-------------------|--------------|-------------|
| **OOLONG** (132K tokens) | GPT-5: baseline | RLM(GPT-5-mini): 2x correct answers | >33% |
| **CodeQA** | GPT-5: 24% accuracy | RLM: 62% accuracy | **158%** |
| **BrowseComp-Plus** (1000 docs) | Degradation at scale | Perfect performance | Maintained at 10M+ tokens |

**Cost efficiency**: RLM(GPT-5-mini) outperformed GPT-5 while maintaining comparable per-query costs.

---

## Relationship to Existing Patterns

### RLM vs GSD vs CAII

| Pattern | Context Strategy | Who Manages Context | Requires Training |
|---------|------------------|---------------------|-------------------|
| **GSD** | Fresh per subagent | Human/orchestrator specifies tasks | No |
| **CAII** | On-the-fly injection | Orchestrator injects domain context | No |
| **Claude-Flow** | Vector retrieval | External system retrieves | No |
| **RLM** | REPL variable + recursive calls | **Model decides what to examine** | **Yes (RL)** |

### Why This Matters

RLM provides the **theoretical foundation** for why GSD's fresh context approach works:

1. **Fresh context = avoiding context rot**: GSD intuitively addressed this; RLM proves it empirically
2. **Recursive decomposition**: GSD's executors are manual RLM; RLM automates the decomposition
3. **Context as external state**: Both externalize context, but RLM makes it programmatically accessible

**Key distinction**: RLM inverts control. Instead of external systems managing context (like GSD's orchestrator), the model learns to manage its own context.

---

## Applicability to Claude Code

### What Works Now (Without RLM Training)

Even without RL training, RLM concepts inform better Claude Code patterns:

1. **Encourage recursive exploration**:
   ```
   "First examine the structure of this codebase, then dive into
   specific areas. Don't try to hold everything in context at once."
   ```

2. **Explicit context partitioning**:
   ```
   "Process these files in batches of 3, synthesizing findings
   between batches rather than loading all at once."
   ```

3. **Programmatic filtering prompts**:
   ```
   "Search for authentication-related code first, then examine
   only those files in detail."
   ```

### What Requires Future Development

Full RLM benefits require:
- RL training for context management (not available for Claude)
- REPL environment integration (Claude Code has Bash, but not the RLM REPL pattern)
- Model checkpointing for recursive calls (not currently exposed)

---

## Two Implementation Approaches

### Approach A: Skill-Based RLM (Prompting + Native Subagents)

**What it is**: A Claude Code skill that implements RLM operations (peek, grep, partition, synthesize) through prompting and native subagent orchestration.

**Example implementation**: See `project1/.claude/skills/recursive-context-query/`

**Advantages**:
- Zero external dependencies
- Works with stock Claude Code
- No API key configuration needed
- Transparent, auditable routing

**Limitations**:
- No learned optimization (fixed routing rules)
- Single-pass synthesis (no iteration)
- Manual partition strategy selection

**Best for**: 15-50 file queries, knowledge base synthesis, hypothesis cross-referencing

**Evaluation**: 7.5/10 for RLM implementation completeness; prevents context rot but doesn't optimize routing.

**Validated Test (January 26, 2026)**: Literature query on "security analytics architecture"
- Search space: 92 potentially relevant files
- Partition strategy: 3 parallel subagents (hypotheses, concepts, contradictions)
- Results: 15 hypotheses + 4 concept docs + 5 contradictions synthesized
- Quality: Fresh context per subagent maintained coherence; no observable degradation
- Synthesis: Cost (130-227x SIEM premium), Architecture (hybrid optimal), Market (pipeline lock-in)

---

### Approach B: External Integration (rand/rlm-claude-code)

**What it is**: Full RLM implementation with REPL environment, learned routing, and recursive sub-calls.

**Repository**: [rand/rlm-claude-code](https://github.com/rand/rlm-claude-code)

**Advantages**:
- True REPL with context as Python variables
- RL-trained routing decisions
- 71% token reduction demonstrated
- Depth-limited recursion (max depth=2)
- Optional Rust acceleration (10-50x with rlm-core)

**Limitations**:
- Complex setup (Python 3.12+, 127 packages)
- Requires API key configuration
- Higher latency for small queries
- Crossover point ~50KB (below that, overhead exceeds benefit)

**Best for**: >50KB contexts, long-running sessions, cost-sensitive production workloads

**Verified components** (January 2026):
- Context manager: 25 tests passing
- REPL environment: 168 tests passing
- Security sandboxing: Validated

---

### Choosing Between Approaches

| Factor | Skill-Based | External Integration |
|--------|-------------|---------------------|
| **Setup time** | 0 (native) | 30-60 min |
| **Query size** | 15-50 files | 50KB+ |
| **Token efficiency** | Moderate | 71% reduction |
| **Latency** | Lower | Higher |
| **Learning** | None | RL-trained |
| **Maintenance** | Low | Medium |

**Recommendation**: Start with skill-based for immediate value. Graduate to external integration when:
1. Sessions regularly exceed 50KB
2. Token costs become significant concern
3. Quality degradation observable in long sessions

---

## Implementation Guidance

### For Claude Code Users Today

Apply RLM principles through explicit prompting:

```markdown
## RLM-Inspired Prompt Pattern

Instead of: "Analyze this entire codebase"

Try: "1. First, list the top-level directory structure
      2. Identify the 3 most relevant directories for [goal]
      3. Examine those directories in detail
      4. Synthesize findings before proceeding to related areas"
```

### For Agent Architects

If building orchestration systems, RLM suggests:

1. **Give agents programmatic context access** rather than pre-loaded context
2. **Let agents decide exploration strategy** rather than prescribing it
3. **Support recursive sub-calls** for decomposition
4. **Cap sub-call output** to force intelligent filtering (RLM uses 8,192 char limit)

---

## Caveats and Limitations

### 1. Requires RL Training

> "Early experiments show RLMs underperform standard LLMs on math-python without training."
> — Prime Intellect

The scaffolding introduces overhead that only reinforcement learning overcomes. Without training, RLM patterns may add latency without quality improvement.

### 2. No Claude-Specific Validation

All published results use GPT-5/GPT-5-mini. Claude's behavior with RLM patterns is untested.

### 3. Cost Considerations

Multiple sub-calls increase API costs. The paper shows cost-efficiency at scale, but small tasks may see overhead.

### 4. Implementation Complexity

Full RLM requires:
- REPL environment setup
- Sub-LLM spawning infrastructure
- Result aggregation logic

---

## RLM Testing Roadmap

> **Thesis**: RLM represents a potential inflection point where proper scaffolding transforms "nearly AGI" models into "effectively AGI" systems for specific domains like cybersecurity. This warrants serious, rapid testing.

### Phase 1: Environment Setup (Week 1)

**Goal**: Establish isolated testing environment for RLM + Claude

| Task | Tool/Resource | Success Criteria |
|------|---------------|------------------|
| Clone [rand/rlm-claude-code](https://github.com/rand/rlm-claude-code) | Git | Working local copy |
| Install dependencies (Python 3.12+, uv) | Shell | `uv sync --all-extras` succeeds |
| Configure Claude API access | Environment | API calls complete |
| Set up isolated test directory | Filesystem | No production data exposure |

**Verified Installation (January 26, 2026)**:
```bash
# Clone and install
mkdir -p ~/rlm-testing && cd ~/rlm-testing
git clone https://github.com/rand/rlm-claude-code.git
cd rlm-claude-code
uv sync --all-extras  # Installs 127 packages including torch, transformers

# Verify with tests (193 tests for core REPL + context manager)
uv run pytest tests/unit/test_context_manager.py tests/unit/test_repl_environment.py -v
# Expected: 193 passed

# Configure API key
cp .env.example .env
# Edit .env with ANTHROPIC_API_KEY

# Optional: Install as Claude plugin
claude plugins install . --scope user
```

**Key Dependencies Installed**:
- pydantic, hypothesis, cpmpy (constraint programming)
- anthropic, openai, tiktoken (LLM APIs + token counting)
- torch, transformers, sentence-transformers (local models for SetFit classification)
- numpy, pandas, polars, seaborn (data analysis)

**Safety considerations**:
- Use sandbox/isolated environment only
- No production credentials in test environment
- Start with `--dry-run` or read-only modes

### Phase 2: Baseline Establishment (Week 2)

**Goal**: Measure Claude Code's current performance on target tasks WITHOUT RLM

**Test cases for cybersecurity domain**:

| Test Case | Input Size | Task | Baseline Metric |
|-----------|------------|------|-----------------|
| OCSF log classification | 50K tokens | Classify 100 events to OCSF categories | Accuracy % |
| SIEM rule analysis | 100K tokens | Map 50 Sigma rules to ATT&CK TTPs | F1 score |
| Vulnerability triage | 150K tokens | Prioritize 200 CVEs by EPSS/context | Ranking correlation |
| Threat intel synthesis | 200K tokens | Synthesize report from 20 STIX bundles | Human eval (1-5) |

**Process**:
1. Run each test case with standard Claude Code (no RLM)
2. Record: accuracy, latency, token usage, cost
3. Note where context rot is observable (quality degradation patterns)

### Phase 3: RLM Integration Testing (Weeks 3-4)

**Goal**: Test RLM scaffolding with identical test cases

**Using rand/rlm-claude-code**:
```bash
# Example test command structure
python -m rlm_claude test \
  --input data/ocsf-logs-50k.jsonl \
  --task "Classify each event to OCSF category" \
  --output results/ocsf-rlm-baseline.json
```

**Metrics to capture**:

| Metric | Why It Matters |
|--------|----------------|
| Accuracy vs baseline | Primary quality signal |
| Latency | Production viability |
| Token usage | Cost scaling |
| Sub-call count | Decomposition behavior |
| Context peak | Memory/context utilization |

**Key questions to answer**:
1. Does RLM improve accuracy on cybersecurity tasks?
2. What's the crossover point (input size where RLM wins)?
3. Does Claude exhibit learned-like behaviors (peek, grep, partition) through prompting alone?

### Phase 4: Cybersecurity-Specific Validation (Weeks 5-6)

**Goal**: Test domain-specific scenarios that matter for production

**High-value test scenarios**:

| Scenario | Why It Matters | Expected RLM Benefit |
|----------|----------------|----------------------|
| Multi-day incident timeline | Temporal reasoning across large context | Maintains coherence |
| Cross-tenant correlation | Isolate relevant signals from noise | Efficient filtering |
| MITRE ATT&CK chain analysis | Multi-hop reasoning through techniques | Recursive decomposition |
| Compliance evidence mapping | Match controls to evidence across large doc set | Partition + search |

**Domain-specific success criteria**:
- Incident timeline: Correct temporal ordering of 95%+ events
- ATT&CK chains: Identify 80%+ of technique transitions
- Compliance: Map 90%+ of controls to evidence

### Phase 5: Production Readiness Assessment (Week 7+)

**Decision framework**:

| Outcome | Evidence Required | Action |
|---------|-------------------|--------|
| **Adopt** | >20% improvement on 3+ test cases, acceptable latency, cost < 2x | Document patterns, create skills |
| **Monitor** | Mixed results, some improvements | Continue testing, wait for Claude RLM training |
| **Defer** | No improvement or degradation | Archive learnings, revisit when Anthropic announces context-trained models |

**Production deployment considerations**:
- Start with non-critical workflows (research, analysis)
- Maintain fallback to standard Claude Code
- Monitor for edge cases and failures

---

## Monitoring Signals

### Near-term (weeks)

| Signal | Source | Implication |
|--------|--------|-------------|
| Anthropic "context-trained" announcement | Blog, changelog | Native RLM coming |
| rand/rlm-claude-code major release | GitHub | Community validation |
| Chroma context rot follow-up | Research blog | Updated Claude benchmarks |

### Medium-term (months)

| Signal | Source | Implication |
|--------|--------|-------------|
| Claude Agent SDK RLM patterns | Anthropic docs | Official support |
| RLM in Claude Code changelog | Release notes | Native integration |
| Production case studies | Community, vendors | Validation data |

### Domain-specific (cybersecurity)

| Signal | Source | Implication |
|--------|--------|-------------|
| SIEM vendor RLM integration | Splunk, Elastic blogs | Market validation |
| RLM + OCSF patterns | OCSF community | Schema-specific optimization |
| LogRESP-Agent RLM variant | MDPI, arXiv | Recursive log analysis advances |

---

## Hypothesis to Validate

**H-RLM-CYBER-01**: RLM scaffolding with Claude will improve cybersecurity log analysis accuracy by >30% compared to standard Claude Code on tasks exceeding 100K token contexts.

| Attribute | Value |
|-----------|-------|
| **Confidence** | 3/5 (Medium) |
| **Evidence needed** | Controlled comparison on OCSF classification task |
| **Validation timeline** | 6 weeks from test environment setup |
| **Falsification criteria** | <10% improvement OR >3x cost increase |

**Rationale**:
- LogRESP-Agent (similar recursive approach) achieved 99.97% accuracy
- CodeQA improvement (24%→62%) suggests large gains possible
- Cybersecurity has structured data ideal for RLM's partition+search

---

## Related Patterns

- [GSD Orchestration](./gsd-orchestration.md) - Manual implementation of fresh-context principles
- [Context Engineering](./context-engineering.md) - Broader context management strategies
- [Subagent Orchestration](./subagent-orchestration.md) - Current Claude Code parallel execution
- [Framework Selection Guide](./framework-selection-guide.md) - When to use which approach

---

## Sources

**Primary (Tier B)**:
- [alexzhang13/rlm](https://github.com/alexzhang13/rlm) - Official implementation
- [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) - Academic paper (Zhang, Kraska, Khattab)
- [Alex Zhang's Blog](https://alexzhang13.github.io/blog/2025/rlm/) - Original motivation and results

**Claude Code Integrations (Tier C - Community)**:
- [rand/rlm-claude-code](https://github.com/rand/rlm-claude-code) - Most mature integration (144 commits, Jan 2026)
- [brainqub3/claude_code_RLM](https://github.com/brainqub3/claude_code_RLM) - Minimal scaffold (experimental)
- [zircote/rlm-rs](https://github.com/zircote/rlm-rs) - Rust CLI with SQLite persistence
- [ysz/recursive-llm](https://github.com/ysz/recursive-llm) - Multi-model library (supports Claude Sonnet 4)

**Industry Analysis (Tier B)**:
- [Prime Intellect: RLM - The Paradigm of 2026](https://www.primeintellect.ai/blog/rlm) - Industry perspective and verifiers library
- [Chroma Context Rot Research](https://research.trychroma.com/context-rot) - Empirical study of context degradation

**Cybersecurity-Relevant Research (Tier B)**:
- [LogRESP-Agent](https://www.mdpi.com/2076-3417/15/13/7237) - Recursive log anomaly detection (99.97% accuracy)
- [Rule-ATT&CK Mapper (RAM)](https://arxiv.org/html/2502.02337v1) - LLM SIEM rule to ATT&CK mapping

**Related Patterns**:
- AgentFold (hierarchical action summaries)
- Scaling Long-Horizon (active branching with summaries)
- GSD (fresh context per subagent - manual RLM principles)

*Last updated: January 2026*
