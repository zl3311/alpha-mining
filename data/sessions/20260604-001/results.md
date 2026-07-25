---
id: "20260604-001-results"
session: "20260604-001"
total_expressions: 68
gate_passers: 8
best_sharpe: 2.22
best_fitness: 2.47
best_alpha_id: "vRm07LP3"
---

# Results: Session 20260604-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | ~68 |
| Gate-passers (S>=1.25, F>=1.0) | 8+ |
| Best Sharpe (gate-pass, not submittable) | 2.22 (Wjgk0wMG) |
| Best Fitness (submittable) | 2.35 (vRm07LP3) |
| Submittable EXCELLENT | 1 (vRm07LP3) |

## Submittable Candidate

| Alpha ID | Expression | S | F | T | Grade | BRAIN | Self-corr | Verdict |
|----------|-----------|---|---|---|-------|-------|-----------|---------|
| vRm07LP3 | `ts_decay_linear(zscore(ts_mean(IV_call_270 - IV_put_270, 22)), 10)` MARKET d=10 | 1.82 | 2.35 | 4.6% | EXCELLENT | ALL PASS | 0.309 | **SUBMIT** |

## Near-Miss EXCELLENT (blocked on BRAIN checks)

| Alpha ID | S | F | Fails |
|----------|---|---|-------|
| Wjgk0wMG | 2.22 | 2.47 | CONCENTRATED_WEIGHT, SUB_UNIVERSE |
| 6XEx0mjY | 2.06 | 2.08 | CONCENTRATED_WEIGHT, SUB_UNIVERSE |
| N1OM2kxE | 2.03 | 2.15 | CONCENTRATED_WEIGHT, SUB_UNIVERSE |
| ZYoZgoV3 | 2.09 | 1.85 | CONCENTRATED_WEIGHT, SUB_UNIVERSE |

## Backup Submittable (GOOD grade)

| Alpha ID | S | F | Grade | Self-corr |
|----------|---|---|-------|-----------|
| 9qRoMPAo | 1.45 | 1.65 | GOOD | 0.296 |
| wpe6d15d | 1.58 | 1.98 | GOOD | 0.328 |

## Dead Ends

| Approach | Result |
|----------|--------|
| pcr_oi_270 standalone | S=0.38 DEAD |
| group_neutralize + buzz addition | Unit error on BRAIN |
| TOP1000 zscore variants | S<1.0 INFERIOR |
| rel_num MARKET blends | ALL PASS but self-corr 0.818 vs xAR9Ybjp |
