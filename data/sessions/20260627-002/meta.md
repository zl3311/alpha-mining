---
id: "20260627-002"
date: "2026-06-27"
strategy: "EXPLORE"
trigger: "local_manual"
budget: "unlimited"
budget_used: 27
target_grade: "EXCELLENT+"
status: "productive"
branch: "session/20260627-002-explore-novel-cross-family"
tags:
  - "20260627-002"
  - "explore_novel"
  - "iv_skew"
  - "guidance"
  - "coverage_breadth"
gate_passers: 8
submissions: 1
submitted: ["e7O5EQbJ"]
best_alpha: "e7O5EQbJ"
best_sharpe: 2.50
best_fitness: 2.31
best_self_corr: 0.577
candidates:
  - id: "e7O5EQbJ"
    grade: "EXCELLENT"
    sharpe: 2.50
    fitness: 2.31
    self_corr_value: 0.577
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "GrwWx6AQ"
    grade: "EXCELLENT"
    sharpe: 2.35
    fitness: 2.12
    self_corr_value: 0.590
    self_corr_result: "PASS"
    verdict: "BLOCKED — sibling of e7O5EQbJ (mutual corr ~0.90)"
  - id: "npgvr2Ql"
    grade: "EXCELLENT"
    sharpe: 2.47
    fitness: 2.17
    self_corr_value: 0.634
    self_corr_result: "PASS"
    verdict: "BLOCKED — sibling of e7O5EQbJ (mutual corr ~0.90)"
  - id: "LLpM3ALL"
    grade: "EXCELLENT"
    sharpe: 2.48
    fitness: 2.46
    self_corr_value: 0.685
    self_corr_result: "PASS"
    verdict: "BLOCKED — sibling of e7O5EQbJ (mutual corr ~0.90, self-corr near limit)"
---

# Session 20260627-002: EXPLORE — Novel Cross-Family Interactions

## Research Question

Can novel cross-family interactions using underexplored datasets (option8 IV skew,
company guidance, analyst coverage breadth) combined with novel fundamental6
anchors (drc, mrct, cld2, nopio) produce EXCELLENT+ submittable alphas?

## Strategy Rationale

EXPLORE mode (default). Book is saturated with 45 entries across 39+ families.
Focus on cross-family interactions from underrepresented datasets: option8 IV
skew, company guidance, coverage breadth, and novel fnd6 fields.

## Key Discovery: Coverage Breadth × Deferred Revenue Template

The template `ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(fnd6_drc / close) + rank(open/close - 1) [+ 4th factor], D)` produces a family of EXCELLENT-grade alphas that pass all 8 BRAIN checks AND self-correlation.

### Novel elements
- `sales_estimate_count_quarterly` (analyst coverage breadth) — not in the book
  as a primary anchor. Captures institutional attention and information quality.
- `fnd6_drc` (deferred revenue) — not in the book. Captures business model
  quality (subscription/SaaS characteristics).
- The combination of coverage breadth + deferred revenue is genuinely novel —
  no existing book entry uses either as primary signal.

### Results Summary

| Batch | Size | Strategy | Gate-Passers | Best |
|-------|------|----------|-------------|------|
| batch_r1 | 15 | Novel cross-family (4 families) | 6 | GrwWx6AQ EXCELLENT S=2.35 |
| batch_r2_exploit | 12 | Winner mutations (4th factor, decay, normalization) | 5 | e7O5EQbJ EXCELLENT S=2.50 |

### Submittable Candidates

| Alpha | Expression | S | F | T | Self-Corr | Top Peer | Verdict |
|-------|-----------|---|---|---|-----------|----------|---------|
| e7O5EQbJ | + rank(fnd6_acdo/close) [4-factor] | 2.50 | 2.31 | 11.2% | 0.577 PASS | zq5RLWO8 | SAFE |
| GrwWx6AQ | base 3-factor (decay=5) | 2.35 | 2.12 | 11.3% | 0.590 PASS | zq5RLWO8 | SAFE |
| npgvr2Ql | base 3-factor (decay=3) | 2.47 | 2.17 | 14.5% | 0.634 PASS | RRN1EM51 | SAFE |
| LLpM3ALL | + rank(fnd6_itci/close) [4-factor] | 2.48 | 2.46 | 10.5% | 0.685 PASS | omnopQ9k | SAFE |

### Submission Recommendation

Per long-term point maximization strategy: submit **e7O5EQbJ** first (lowest
self-corr 0.577, highest Sharpe 2.50). All 4 candidates are from the same
template family, so only 1 is submittable at a time (siblings will be blocked
by mutual self-correlation after first submission).

## What Worked

1. **`sales_estimate_count_quarterly` is a strong novel anchor** — analyst
   coverage breadth has standalone Sharpe ~1.36, and in combination with
   deferred revenue + overnight gap produces EXCELLENT (S=2.35+).
2. **`fnd6_drc` (deferred revenue) is a productive value signal** — normalizing
   by close gives a business-model quality factor that decorrelates well from
   the existing IV-heavy and analyst-revision-heavy book.
3. **Adding `fnd6_acdo` as 4th factor improves both Sharpe and self-corr** —
   Sharpe lifted from 2.35 to 2.50, self-corr dropped from 0.590 to 0.577.
4. **Decay=3 improves Sharpe** — decay=3 variant (npgvr2Ql) has S=2.47 vs
   decay=5 at S=2.35, but slightly higher turnover (14.5% vs 11.3%).

## What Didn't Work

1. **IV skew (implied_volatility_mean_skew_360)**: All blends were GOOD at best
   (S=2.23, F=1.59). The field produces high turnover (27%) that kills fitness.
   One variant (omKEr1Nn) also failed CONCENTRATED_WEIGHT.
2. **Company guidance (max_adjusted_net_income_guidance)**: All variants were
   below gate-passer thresholds. The field has low coverage in TOP3000.
3. **Net debt guidance (min_net_debt_guidance)**: Same coverage issue as guidance.
4. **Product template (rank(F1) * rank(F2))**: AVERAGE grade (S=1.69, F=1.48).
   Non-linear combination doesn't improve over additive.
5. **Multi-horizon MA crossover**: Below gate-passer threshold. Fundamental
   fields are too slow-moving for short-term MA crossover signals.
6. **trade_when (volatility gate)**: Failed — likely an expression error.

## Lessons Learned

1. **Coverage breadth + deferred revenue is a new submittable family** — novel
   combination of analyst4 and fundamental6 that decorrelates from existing book.
2. **IV skew from option8 is a dead end** — high turnover kills fitness.
   Consider adding to dead zones.
3. **Company guidance fields have low coverage** — single-field guidance
   doesn't produce signal in TOP3000. May work in TOP1000 with higher coverage.
4. **4th factor (acdo) improves AND decorrelates** — adding fnd6_acdo/close as
   a 4th factor improved Sharpe while reducing self-corr (rare beneficial
   combination). This is because acdo contributes orthogonal PnL that dilutes
   correlation with existing book entries.
