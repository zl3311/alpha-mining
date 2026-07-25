---
id: "20260705-001-results"
session: "20260705-001"
total_expressions: 20
gate_passers: 16
best_sharpe: 2.82
best_fitness: 2.60
best_alpha_id: "GrLJLGN5"
---

# Results: Session 20260705-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 20 |
| Gate-passers (S>=1.25, F>=1.0) | 16 |
| EXCELLENT+ | 3 |
| Submittable (BRAIN self-corr PASS) | 2 |
| Recommended winner | GrLJLGN5 |

## Top Candidates

| Alpha | Grade | S | F | T | Self-Corr | Verdict |
|-------|-------|---|---|---|-----------|---------|
| **GrLJLGN5** | EXCELLENT | 2.77 | 2.40 | 20.7% | 0.780 PASS | **SUBMITTABLE (minimal)** |
| kq0lKW98 | EXCELLENT | 2.82 | 2.33 | 23.1% | 0.775 PASS | SUBMITTABLE |
| QPVXVWpK | SPECTACULAR | 2.70 | 2.60 | 16.6% | 0.775 FAIL | BLOCKED |
| Xgn6KdR8 | GOOD | 2.07 | 1.69 | 15.5% | 0.646 PASS | Below EXCELLENT |

## Winner Details: GrLJLGN5

**Expression:**
```
ts_decay_linear(rank(-1 * rel_ret_cust) + rank(anl4_ptpr_flag) + rank(open/close - 1), 5)
```

**BRAIN self-correlation (authoritative `/check`):**
- Result: PASS
- Value: 0.7795 (limit 0.7)
- Top peer: LLR0n261 (S=2.51, corr=0.7795)
- Premium: 2.77 >= 1.10 × 2.51 = 2.761 ✓

**Platform URL:** https://platform.worldquantbrain.com/alpha/GrLJLGN5

## Round 1 Batch (negation_blend_r1)

All 20 expressions used negated anchors from the negation sweep combined with
anl4_ptpr_flag and/or open/close-1. 16 gate-passers; best novel discovery is
the rel_ret_cust negated level signal (simpler than ts_delta variants).
