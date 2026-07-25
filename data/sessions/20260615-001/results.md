---
id: "20260615-001-results"
session: "20260615-001"
total_expressions: 168
gate_passers: 20
best_sharpe: 2.73
best_fitness: 4.38
best_alpha_id: "1YgMZ6OW"
---

# Results: Session 20260615-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 168 (12 rounds) |
| Gate-passers (S>=1.25, F>=1.0) | ~20 |
| Best Sharpe | 2.73 (1YgMZ6OW) |
| Best Fitness | 4.38 (1YgMZ6OW) |
| Submittable (all 8 checks + self-corr) | 1 (LLR0Xjz2, AVERAGE) |
| Budget used | 168 (unlimited cap) |

## Submittable Candidate

| Alpha ID | Expression | Grade | Sharpe | Fitness | Self-Corr | Verdict |
|----------|-----------|-------|--------|---------|-----------|---------|
| LLR0Xjz2 | `ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count), 10)` | AVERAGE | 1.75 | 1.48 | 0.675 (PASS, BRAIN gate 0.70) | SUBMITTABLE (borderline) |

## High-Grade Near-Misses (each blocked by exactly one gate)

| Alpha ID | Expression (short) | Grade | S / F | Blocker |
|----------|-------------------|-------|-------|---------|
| 1YgMZ6OW | IV90 spread + guidance + itci (MARKET) | SPECTACULAR | 2.73 / 4.38 | self-corr 0.966 vs Gro21wWG (IV saturated) |
| pw72Yqeq | IV90 call-put spread (MARKET) | SPECTACULAR | 2.57 / 4.14 | CONCENTRATED_WEIGHT + self-corr |
| 9qRnjZMq | vol-gated IV120 spread (MARKET) | SPECTACULAR | 2.52 / 4.11 | self-corr 0.991 vs Gro21wWG |
| mLXGw2R2 | IV180 spread (MARKET) | SPECTACULAR | 2.10 / 2.96 | self-corr 0.982 vs vRm07LP3 |
| kqKAKLgl | guidance + itci (SUBINDUSTRY) | EXCELLENT | 2.19 / 2.02 | LOW_SUB_UNIVERSE_SHARPE (itci); self-corr PASS 0.608 |

## Round Log

| Round | Tag | Focus | Best result |
|-------|-----|-------|-------------|
| 1-2 | sub6 / mkt6 | equal-weight core+orthogonal blends (SUB + MKT) | INFERIOR (dilution) |
| 3 | nl-sub | nonlinear transforms of orthogonal legs | itci^2 GOOD F1.81 |
| 4 | r2-sub/mkt-d10 | smoothed-options + convex core | itci+pcr GOOD F1.55; itci dies at MARKET |
| 5 | r3-guidance | guidance + value + decorrelator | kqKAKLgl EXCELLENT F2.02 |
| 6 | r4-subuniv-fix | stabilizer broadeners | degraded grade |
| 7 | r5-clean-excellent | clean SUB_UNIV-passing legs (no itci) | AVERAGE only |
| 8 | r6-excellent-decorr | proven recipe minus flag*(-ret) | GOOD (flag-ret carried EXCELLENT) |
| 9 | r7-iv-maturity | IV call-put spread maturities | SPECTACULAR F4.14 (self-corr blocked) |
| 10 | r8-subuniv-excellent | guidance-dominant weighting | GOOD; SUB_UNIV scales with fitness |
| 11 | r9-iv-novel | IV term-structure / skew / vol-gated | vol-gated SPECTACULAR F4.11 |
| 12 | r10-iv-dilute | IV diluted with decorrelating mass | SPECTACULAR F4.38 (still self-corr blocked) |
| 13 | r11-clean-decorr | clean fundamental/analyst blends | LLR0Xjz2 SUBMITTABLE (AVERAGE) |
| 14 | r12-decorr-tilt | clean base + orthogonal smoothed tilt | GOOD F1.76 but SUB_UNIV fail |

(Round numbers in log are batch tags; 12 generation rounds total.)
