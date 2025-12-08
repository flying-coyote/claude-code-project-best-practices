# MCP Failure Modes

**Source**: [Nate B. Jones - MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving)
**Evidence Tier**: B (Validated secondary - expert practitioner)

## The Core Problem

Teams are connecting MCP wrong. The Model Context Protocol is powerful, but its **300-800ms baseline latency** destroys user experience when placed in the wrong locations.

**MCP belongs in**: Decision support, development assistance, background analysis
**MCP does NOT belong in**: Checkout flows, real-time trading, transaction paths

---

## The 7 Failure Modes

### 1. Universal Router Trap

**Mistake**: Routing all requests through MCP
**Symptom**: Everything gets slower
**Impact**: 300-800ms added to every operation

**Reality Check**:
- Not every request needs AI analysis
- Simple operations should stay simple
- MCP is for intelligence, not routing

**Fix**: Route selectively. Only send requests that need AI analysis.

### 2. Kitchen Sink Server Pattern

**Mistake**: Creating overly permissive MCP servers with too many capabilities
**Symptom**: Security nightmares, confused AI behavior
**Impact**: Command injection vulnerabilities, data exposure

**Security Reality**: ~43% of MCP servers have command injection vulnerabilities. Only ~10 of 5,960+ available servers are genuinely trustworthy.

**Fix**:
- Minimal capabilities per server
- Explicit permission boundaries
- Security audit before deployment

### 3. Real-Time Context Delusion

**Mistake**: Using MCP in latency-sensitive paths
**Symptom**: Destroyed conversion rates, frustrated users
**Impact**: E-commerce abandonment, failed transactions

**Where It Kills**:
- Checkout flows
- Search results
- Form submissions
- Real-time pricing

**Fix**: Keep MCP out of user-facing transaction paths.

### 4. Permission Overexposure

**Mistake**: Granting broad permissions "to make it work"
**Symptom**: AI accessing data it shouldn't
**Impact**: Data leakage, compliance violations

**Fix**:
- Principle of least privilege
- Scoped tokens per context
- Regular permission audits

### 5. Transaction Path Integration

**Mistake**: Placing MCP in critical business workflows
**Symptom**: Transaction failures when MCP has issues
**Impact**: Revenue loss, customer trust erosion

**Fix**: MCP for analysis, not execution. Keep transactions on traditional rails.

### 6. Hot Path Placement

**Mistake**: MCP on frequently-accessed endpoints
**Symptom**: Scale issues, cascading failures
**Impact**: System-wide degradation under load

**Fix**: Background processing, caching, async patterns.

### 7. Deployment Timeline Mismatch

**Mistake**: Expecting MCP to be production-ready immediately
**Symptom**: Rushing immature integrations to production
**Impact**: Reliability issues, rollbacks, lost confidence

**Fix**: Staged deployment, shadow mode testing, gradual rollout.

---

## Production-Proven Patterns

### Intelligence Layer Pattern (Block)

**Approach**: Background analysis without touching production systems
**Example**: Block analyzes millions of transactions for fraud patterns—MCP runs analysis, not transactions

**Architecture**:
```
[Transactions] → [Traditional System] → [Database]
                         ↓
                  [Batch Export]
                         ↓
                   [MCP Analysis]
                         ↓
                [Intelligence Dashboard]
```

**Key**: MCP never touches the transaction path.

### Sidecar Pattern (Zapier)

**Approach**: Enhance workflows without blocking users
**Result**: 89% AI adoption through non-blocking integration

**How It Works**:
- User completes action normally
- Sidecar process triggers AI enhancement
- Results appear asynchronously
- No user-perceived latency

**Best For**: Workflow enhancement, content enrichment, smart suggestions

### Batch Pattern

**Approach**: Process overnight, consume in morning
**Example**: Analyze day's data → Generate morning report

**Benefits**:
- Zero real-time impact
- Full dataset analysis
- Cost-efficient (off-peak compute)
- Predictable delivery

**Architecture**:
```
[Day's Data] → [Overnight Batch] → [MCP Processing] → [Morning Report]
```

---

## Decision Framework

```
Is this request time-sensitive?
├── YES → Keep MCP out
│   └── Use traditional processing
└── NO → Consider MCP
    └── Is this analysis or execution?
        ├── Analysis → Good MCP fit
        └── Execution → Keep traditional
```

## Security Checklist

Before deploying any MCP server:

- [ ] Minimal capabilities (no kitchen sink)
- [ ] Scoped permissions per context
- [ ] Audit logging enabled
- [ ] Command injection review
- [ ] Data exposure assessment
- [ ] Rate limiting configured
- [ ] Graceful degradation path

---

## Application to Claude Code

Claude Code's MCP integration should follow these patterns:

| Pattern | Claude Code Application |
|---------|------------------------|
| Intelligence Layer | Code analysis tools (linting, security scan) |
| Sidecar | Background documentation updates |
| Batch | Repository analysis overnight |

**Never** put MCP servers in:
- File save operations (use native filesystem)
- Git commits (use native git)
- Interactive typing (latency kills UX)

---

## Related Patterns
- [Advanced Tool Use](./advanced-tool-use.md) - Tool Search for token efficiency
- [Context Engineering](./context-engineering.md) - Security in context design
