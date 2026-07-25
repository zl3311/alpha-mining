---
id: "20260705-001"
date: "2026-07-05"
strategy: "EXPLORE"
research_question: "Can negation-dominant building blocks from the negation sweep produce a minimal EXCELLENT+ submittable alpha when blended with proven catalyst legs?"
budget_used: 20
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal EXCELLENT+ submittable)"
gate_passers: 16
submissions: 1
submitted: ["GrLJLGN5"]
submitted_date: "2026-07-11"
submittable_candidates: 1
status: "productive"
best_alpha: "GrLJLGN5"
best_grade: "EXCELLENT"
best_sharpe: 2.77
best_fitness: 2.40
best_self_corr: 0.7795
best_self_corr_peer: "LLR0n261"
best_self_corr_verdict: "PASS via Sharpe premium (2.77 >= 1.10 * 2.51 = 2.761)"
tags:
  - "20260705-001"
  - "negation_blend"
  - "cross_direction"
candidates:
  - id: "GrLJLGN5"
    grade: "EXCELLENT"
    sharpe: 2.77
    fitness: 2.40
    self_corr_value: 0.7795
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "kq0lKW98"
    grade: "EXCELLENT"
    sharpe: 2.82
    fitness: 2.33
    self_corr_value: 0.7746
    self_corr_result: "PASS"
    verdict: "BLOCKED"
  - id: "QPVXVWpK"
    grade: "SPECTACULAR"
    sharpe: 2.70
    fitness: 2.60
    self_corr_value: 0.7745
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
---

# Session 20260705-001: Negation Building Block Blends

## Research Question

Can negation-dominant fields from the completed negation sweep (20260705-negation-analysis)
produce a minimal EXCELLENT+ submittable alpha when combined with proven catalyst legs
(anl4_ptpr_flag, open/close-1)?

## Strategy Rationale

EXPLORE mode targeting structurally novel cross-direction additive blends. The negation
sweep identified 34 negation-dominant building blocks; round 1 tested 20 expressions
combining top negated anchors with the standard 3-leg decay template.

## Key Findings

1. **Negation blends work**: 16/20 gate-passers (S>=1.25, F>=1.0) from a single round.
2. **Winner: GrLJLGN5** — minimal 3-factor EXCELLENT with BRAIN self-corr PASS.
3. **rel_ret_cust** (negated level) outperforms **rel_ret_all** (negated delta) on fitness
   while staying simpler (no ts_delta wrapper).
4. **QPVXVWpK** (dividend_min_guidance_value) reached SPECTACULAR but FAIL self-corr.
5. **fnd6_intc** negated reaches GOOD only (S=2.07, F=1.69) — insufficient fitness boost.

## Winner Expression

```
ts_decay_linear(rank(-1 * rel_ret_cust) + rank(anl4_ptpr_flag) + rank(open/close - 1), 5)
```

Config: SUBINDUSTRY, decay 6, TOP3000, USA

## Post-Review Update

- The user submitted GrLJLGN5 on 2026-07-11; BRAIN reports `ACTIVE` with all
  submission checks passing.
- kq0lKW98 is blocked as a sibling companion now that the primary variant is active.
- Avoid dividend_min_guidance_value despite SPECTACULAR metrics (self-corr blocked).
