# Agentic Retrieval vs Traditional RAG

**Source**: [LlamaIndex - RAG is Dead, Long Live Agentic Retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
**Evidence Tier**: B (Validated secondary - major framework vendor)
**Related Implementation**: [PromtEngineer/agentic-file-search](https://github.com/PromtEngineer/agentic-file-search)

## Overview

Agentic retrieval uses an AI agent with tools to dynamically navigate documents, reasoning about what to explore next. This contrasts with traditional RAG which relies on pre-computed embeddings and vector similarity search.

**SDD Phase**: Tasks + Implement (execution layer for information retrieval)

---

## The Problem with Traditional RAG

Traditional Retrieval-Augmented Generation has three fundamental limitations:

### 1. Context Fragmentation

Breaking documents into chunks severs relationships between ideas. A chunk about "authentication" may lose connection to the "authorization" chunk that follows.

### 2. Hidden Cross-References

References like "See Exhibit B" or "as described in Section 3.2" remain opaque to vector-based matching. The embedding captures the text but not the logical dependency.

### 3. Relevance Mismatch

Semantic similarity doesn't capture logical dependencies. Two paragraphs might be semantically similar but serve completely different purposes in context.

---

## Agentic Retrieval Architecture

Instead of pre-computing embeddings, an agent dynamically explores documents using tools:

```
Traditional RAG:
Document → Chunk → Embed → Vector DB → Query → Top-K → LLM

Agentic Retrieval:
Query → Agent → [Tool: scan] → [Tool: preview] → [Tool: read] → LLM
                     ↑                                    │
                     └────── reasoning loop ──────────────┘
```

### Core Tools

| Tool | Purpose | Claude Code Equivalent |
|------|---------|----------------------|
| `scan_folder` | List directory contents | Glob, Bash ls |
| `preview_file` | Quick look at file start | Read (with limit) |
| `parse_file` | Full document extraction | Read |
| `read` | Read specific sections | Read (with offset) |
| `grep` | Pattern search in content | Grep |
| `glob` | Find files by pattern | Glob |

---

## Three-Phase Exploration Strategy

The most effective agentic retrieval follows three phases:

### Phase 1: Parallel Scan

Quick overview of all available documents simultaneously.

```
Agent receives query
    │
    ├── [scan_folder] List all documents
    │
    └── [preview_file × N] Preview each document (~1500 chars)
            │
            └── Categorize: RELEVANT / MAYBE / SKIP
```

**Output**: Triage list with relevance assessments

### Phase 2: Deep Dive

Full extraction on relevant documents only.

```
For each RELEVANT document:
    │
    ├── [parse_file] Full content extraction
    │
    ├── Extract key information
    │
    └── Identify cross-references
```

**Output**: Detailed information + reference list

### Phase 3: Backtrack

Follow cross-references to previously skipped documents.

```
For each cross-reference found:
    │
    ├── Check if target was SKIP or MAYBE
    │
    └── If referenced: [parse_file] Extract from skipped doc
```

**Output**: Complete information with all dependencies resolved

---

## Claude Code Implementation

Claude Code's Explore subagent type implements agentic retrieval natively:

```markdown
## Example: Three-Phase Document Exploration

Task tool with:
- subagent_type: "Explore"
- prompt: |
    Research how authentication works in this codebase.

    Phase 1: Scan the codebase structure, identify all auth-related files
    Phase 2: Deep dive into the most relevant files
    Phase 3: Follow any imports or references to complete the picture

    Return: Summary of auth flow with key file locations
```

### Parallel Exploration

For large codebases, spawn multiple Explore agents:

```markdown
## Parallel Agentic Retrieval

Launch IN PARALLEL (single message, multiple Task calls):

[Task 1: Explore]
- prompt: "Phase 1-3 exploration of authentication system"

[Task 2: Explore]
- prompt: "Phase 1-3 exploration of authorization/permissions"

[Task 3: Explore]
- prompt: "Phase 1-3 exploration of session management"

Synthesize results to understand complete security architecture.
```

---

## When to Use Each Approach

| Scenario | Traditional RAG | Agentic Retrieval |
|----------|-----------------|-------------------|
| **Known, stable corpus** | Good | Overkill |
| **High-volume queries** | Better (cached) | Expensive |
| **Cross-referenced docs** | Poor | Excellent |
| **Dynamic content** | Needs re-indexing | Works naturally |
| **Complex relationships** | Poor | Excellent |
| **Exploratory research** | Limited | Ideal |

### Decision Framework

```
Is the corpus stable and queries predictable?
    YES → Traditional RAG (cached embeddings)
    NO  → Agentic Retrieval

Are document cross-references important?
    YES → Agentic Retrieval
    NO  → Either approach works

Is query volume very high (1000s/hour)?
    YES → Traditional RAG (cost efficiency)
    NO  → Agentic Retrieval (quality)
```

---

## Cost Comparison

| Approach | Setup Cost | Per-Query Cost | Quality |
|----------|------------|----------------|---------|
| **Traditional RAG** | High (embed all docs) | Low (~$0.0001) | Medium |
| **Agentic Retrieval** | None | Medium (~$0.001-0.01) | High |
| **Hybrid** | Medium | Low-Medium | High |

The agentic-file-search project reports ~$0.001/query with Gemini Flash, including multi-step reasoning.

---

## Hybrid Approach

Combine both for optimal results:

```
Query → Quick RAG search → Top candidates
                               │
                               ▼
                    Agent explores candidates
                               │
                               ▼
                    Follow cross-references
                               │
                               ▼
                    Synthesize answer
```

**Implementation**: Use RAG to narrow the search space, then agentic retrieval for deep exploration.

---

## Anti-Patterns

### Pre-Indexing Everything

**Problem**: Spending time embedding documents that may never be queried
**Symptom**: Long setup time, stale embeddings, maintenance burden
**Solution**: Use agentic retrieval for exploratory/infrequent queries

### Ignoring Cross-References

**Problem**: Treating documents as isolated chunks
**Symptom**: Incomplete answers, missed context, broken logic chains
**Solution**: Phase 3 backtracking to follow references

### Single-Pass Exploration

**Problem**: Reading documents once without revisiting based on findings
**Symptom**: Missing connections discovered later in exploration
**Solution**: Three-phase strategy with backtracking

### Over-Reading

**Problem**: Full-parsing every document regardless of relevance
**Symptom**: High token costs, slow responses, context pollution
**Solution**: Phase 1 triage with preview before deep dive

---

## Integration with SDD Phases

| SDD Phase | Agentic Retrieval Application |
|-----------|------------------------------|
| **Specify** | Explore existing requirements, find related specs |
| **Plan** | Research architecture patterns, find similar implementations |
| **Tasks** | Identify dependencies, estimate complexity from codebase |
| **Implement** | Find code patterns, understand existing implementations |

---

## Related Patterns

- [Subagent Orchestration](./subagent-orchestration.md) - Parallel exploration with Explore subagents
- [Advanced Tool Use](./advanced-tool-use.md) - Tool search and programmatic calling
- [Context Engineering](./context-engineering.md) - Managing retrieved context effectively

---

## Sources

**Primary (Tier B)**:
- [LlamaIndex - Introducing Agentic Document Workflows](https://www.llamaindex.ai/blog/introducing-agentic-document-workflows)
- [LlamaIndex - RAG is Dead, Long Live Agentic Retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)

**Implementation Reference (Tier C)**:
- [PromtEngineer/agentic-file-search](https://github.com/PromtEngineer/agentic-file-search) - Open-source implementation with Gemini + LlamaIndex Workflows

*Last updated: January 2026*
