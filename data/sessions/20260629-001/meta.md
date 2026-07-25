---
id: "20260629-001"
date: "2026-06-29"
strategy: "EXPLORE"
research_question: "Can structurally novel operator trees (product interactions, MA crossovers, signal-to-noise ratios, convex weighting) produce EXCELLENT+ submittable alphas distinct from the additive-blend-dominated book?"
budget_used: 25
budget_cap: null
trigger: "local_manual"
gate_passers: 17
submissions: 1
submitted: ["JjpzQAze"]
submittable_candidates: 1
status: "productive"
branch: "session/20260629-001-explore-novel-structures"
tags:
  - "20260629-001"
  - "explore_novel"
  - "product_interaction"
  - "ma_crossover"
  - "signal_to_noise"
  - "convex_value"
  - "regime_gate"
candidates:
  - id: "JjpzQAze"
    grade: "EXCELLENT"
    sharpe: 2.30
    fitness: 2.05
    turnover: 0.117
    self_corr_value: 0.6813
    self_corr_result: "PASS"
    self_corr_peer: "LLR0n261"
    verdict: "SUBMITTED"
  - id: "9qwMj8kd"
    grade: "SPECTACULAR"
    sharpe: 2.49
    fitness: 2.63
    turnover: 0.137
    self_corr_value: 0.7592
    self_corr_result: "FAIL"
    self_corr_peer: "LLR0n261"
    verdict: "BLOCKED — self-corr 0.76, need Sharpe >= 2.76 for premium escape"
  - id: "npgqPYKq"
    grade: "EXCELLENT"
    sharpe: 2.14
    fitness: 2.41
    turnover: 0.127
    self_corr_value: 0.7979
    self_corr_result: "FAIL"
    self_corr_peer: "6Xzm6PQP"
    verdict: "BLOCKED — self-corr 0.80"
  - id: "rKoGeARo"
    grade: "EXCELLENT"
    sharpe: 2.47
    fitness: 2.04
    turnover: 0.285
    self_corr_value: 0.7816
    self_corr_result: "FAIL"
    self_corr_peer: "LLR0n261"
    verdict: "BLOCKED — self-corr 0.78"
  - id: "zq9G81pG"
    grade: "EXCELLENT"
    sharpe: 2.28
    fitness: 2.10
    turnover: 0.180
    self_corr_value: 0.8220
    self_corr_result: "FAIL"
    self_corr_peer: "LLR0n261"
    verdict: "BLOCKED — self-corr 0.82"
best_alpha: "JjpzQAze"
best_sharpe: 2.30
best_fitness: 2.05
best_self_corr: 0.6813
---

# Session 20260629-001: EXPLORE — Novel Operator Tree Structures

## Research Question

Can structurally novel operator trees — 3-way product interactions, MA crossovers
on fundamentals, signal-to-noise ratios, rank-squared convex weighting, and
volatility-adjusted value — produce EXCELLENT+ submittable alphas distinct from
the additive-blend-dominated book?

## Strategy Rationale

The book has 47 entries (31 ACTIVE) spanning 39+ mechanism families. Nearly all
use additive `rank(A) + rank(B) + rank(C)` blend structures wrapped in
`ts_decay_linear`. Multiplicative (product) interactions represent a genuinely
novel operator tree shape that requires all factors to agree simultaneously,
creating a different position profile from additive blends.

## Key Findings

- **Product interactions are viable**: 3-way `rank(A) * rank(B) * rank(C)` produces
  EXCELLENT grade with lower self-corr than additive blends using the same fields.
- **fnd6_ivaco is the decorrelation key**: Among all fundamental6 fields tested in
  product interactions, ivaco (investment in associated companies) produced the
  lowest self-corr (0.68) vs the existing book. Fields like acdo, dlto, drlt
  correlate at 0.76-0.82 with LLR0n261.
- **Volatility-adjusted value is SPECTACULAR but blocked**: `rank(F / close /
  ts_std_dev(returns, 20))` with fnd6_drlt reached SPECTACULAR S=2.49 F=2.63
  but fails self-corr at 0.76 vs LLR0n261. Could be unlocked with MARKET neut.
- **LLR0n261 is the primary correlation blocker**: 4 of 5 top candidates have
  LLR0n261 (accrual_intraday_analyst_revision) as their highest-corr peer.
  Shared `open/close - 1` and `anl4_bvps_flag` components drive this.
- **MA crossover and signal-to-noise templates underperformed**: These reached
  GOOD grade at best, not EXCELLENT. The momentum acceleration concept
  (`ts_mean(F,5) - ts_mean(F,22)`) needs further refinement.
- **Rank-squared convex value works**: `rank(F) * rank(F)` with fnd6_dlto reached
  EXCELLENT S=2.14 F=2.41 but failed self-corr at 0.80 vs 6Xzm6PQP.

## Next Steps

- Submit JjpzQAze if confirmed acceptable by the user
- Retry the SPECTACULAR 9qwMj8kd with MARKET neutralization to reduce self-corr
- Explore product interactions with fields NOT shared by LLR0n261 (guidance,
  sentiment, non-ivaco fundamental fields)
- Test volatility-adjusted template with MARKET neut for decorrelation
