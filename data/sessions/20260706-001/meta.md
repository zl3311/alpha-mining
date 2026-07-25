---
id: "20260706-001"
date: "2026-07-06"
strategy: "HYPOTHESIS"
trigger: "manual (user-initiated, no budget constraint, find EXCELLENT+ submittable)"
status: "complete"
budget: "unlimited"
budget_used: 40
rounds: 2
simulations: 40
gate_passers: 20
submissions: 1
target: "EXCELLENT+ submittable (not submitted by agent, present to user + draft PR)"
research_question: "Can negated tax/fundamental fields blended with orthogonal analyst flags yield decorrelated EXCELLENT+ alphas?"
opportunity: "negation-blend-candidates.md"
best_alpha: "ZYpjKeKx"
best_grade: "EXCELLENT"
best_sharpe: 2.49
best_fitness: 2.25
best_self_corr: 0.75
best_self_corr_result: "PASS"
submitted: ["ZYpjKeKx"]
outcome: "Re-verified ZYpjKeKx (20260622 discovery); user submitted manually 2026-07-06"
candidates:
  - id: "ZYpjKeKx"
    grade: "EXCELLENT"
    sharpe: 2.49
    fitness: 2.25
    self_corr_value: 0.75
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
---

# Session 20260706-001: HYPOTHESIS — Negation-Enriched Cross-Family Blends

## Outcome

**Submitted:** [ZYpjKeKx](https://platform.worldquantbrain.com/alpha/ZYpjKeKx) — EXCELLENT, BRAIN self-corr **PASS** (0.75, Sharpe premium vs `zqOrkbbG`).

Originally discovered in session 20260622-001; re-verified this session via authoritative BRAIN `/check` poll.

## Context Assessment

- Book: 39 ACTIVE + 11 PENDING across 47 mechanism families
- Strategy: HYPOTHESIS on negation-blend-candidates.md
- 40 sims across 2 rounds (negated tax blends + txbcof CONCENTRATED_WEIGHT fixes)

## Key Findings

1. **`fnd6_txbcof` + analyst flags**: SPECTACULAR IS metrics but **structural CONCENTRATED_WEIGHT block** (13+ variants, val=0.5). Do not mutate further.
2. **Accrued-liability without buzz** (`lerlAg5l`, `blvvlQAR`): SPECTACULAR, 7/7 IS checks pass, but self-corr **FAIL** (0.82–0.83 vs `zqOrkbbG`).
3. **`trade_when` + itci event-leverage** (`j2gPZJwO`, `bl9rLraM`): self-corr **FAIL** (0.96–0.98 vs book event-leverage alphas).
4. **Event-magnitude + buzz** (`ZYpjKeKx`): `abs(ts_delta(fn_accrued_liab_q/close, 3))` decorrelates vs raw accrued-liab template; buzz component enables Sharpe premium escape.

## Dead Zones Confirmed

- `fnd6_txbcof` blends: CONCENTRATED_WEIGHT structural block (same family as standalone `-ts_zscore`)
- Accrued-liab + cfi + bvps without buzz: self-corr wall at 0.83
