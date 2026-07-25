---
id: "20260711-001-results"
session: "20260711-001"
total_expressions: 84
gate_passers: 57
best_sharpe: 2.54
best_fitness: 2.76
best_alpha_id: "YP0bLdzA"
---

# Results: Session 20260711-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 84 |
| Gate-passers (S>=1.25, F>=1.0) | 57 |
| Grade breakdown | 7 SPECTACULAR, 17 EXCELLENT, 18 GOOD, 17 AVERAGE, 20 INFERIOR |
| Best Sharpe (any grade) | 2.54 (WjGPr2xd) |
| Best Fitness (any grade) | 2.76 (3qR9JvXX) |
| Winning submittable candidate | YP0bLdzA — EXCELLENT, S=2.32, F=2.22 |
| Budget used | 84 / unlimited |

## Gate-Passers (Key Candidates by Round)

| # | Round | Alpha ID | Expression (abbreviated) | Sharpe | Fitness | Turnover | Self-Corr (local) | Verdict |
|---|-------|----------|---------------------------|--------|---------|----------|--------------------|---------|
| 1 | 1 | RR8Vz96o | `dltis + open/close-1 + ptpr_flag` | 2.37 | 2.54 | 11.9% | 0.801 | BLOCKED (skeleton) |
| 2 | 1 | d50OzQNg | `gric_flag spread + open/close-1 + ptpr_flag` | 2.53 | 2.34 | 17.5% | 0.770 | BLOCKED (skeleton) |
| 3 | 1 | lel8GE72 | `fn_liab + open/close-1 + ptpr_flag + dltis` | 2.16 | 2.16 | 9.4% | 0.800 | BLOCKED + FAIL SUB_UNIVERSE |
| 4 | 2 | 3qR9JvXX | `dltis + open/close-1 + netdebt_flag` | 2.50 | 2.76 | 12.3% | 0.797 | BLOCKED (near-exact match to LLR0n261) |
| 5 | 2 | xAkYEmlN | `abs(delta(dltis)) + ptpr_flag + open/close-1` | 2.47 | 2.65 | 12.5% | 0.766 | BLOCKED (skeleton) |
| 6 | 2 | ZYn09ke1 | `gric_flag spread + open/close-1 + ptpr_flag` (MARKET) | 2.15 | 2.37 | 14.7% | 0.744 | BLOCKED (marginal MARKET improvement insufficient) |
| 7 | 3 | e709MonM | `abs(delta(fn_liab)) + gric_flag + dltis` (pure fresh, no skeleton) | 1.47 | 1.14 | 4.1% | (decorrelated by construction) | Below grade bar (AVERAGE) |
| 8 | 4 | gJMQN0dQ | event-magnitude(dltis) + leverage + ivaco + drlt + buzz | 2.49 | 2.63 | 9.7% | 0.937 (vs WjGVJ7bN) | BLOCKED (dltis~txw economic overlap) |
| 9 | 4 | WjGPr2xd | event-magnitude(fn_liab) + leverage + ivaco + drlt + buzz | 2.54 | 2.59 | 9.8% | 0.709 (vs WjGVJ7bN) | RISKY (borderline, Sharpe premium not cleared) |
| 10 | 4 | E5Evj7wK | event-magnitude(fn_liab) + leverage + ivaco + drlt (no buzz) | 2.30 | 2.13 | 3.5% | 0.662 (vs WjGVJ7bN) | FAIL LOW_SUB_UNIVERSE_SHARPE |
| 11 | 6 | P03ZkrkW | event-magnitude(fn_liab) + leverage + fatl + ivaco + buzz | 2.16 | 2.33 | 10.0% | 0.696 (vs rKlo39p1) | RISKY (margin too thin) |
| 12 | 6 | VkP6WQqV | event-magnitude(fn_liab) + leverage + fatl + drlt + buzz | 1.95 | 2.08 | 9.7% | 0.691 (vs rKlo39p1) | RISKY (margin too thin) |
| 13 | 7 | VkPavmgJ | event-magnitude(fn_liab, d=5) + leverage + fatl + ivaco + buzz | 2.16 | 2.33 | 10.0% | 0.694 (vs rKlo39p1) | RISKY (margin too thin) |
| 14 | 8 | QPVbPqaM | event-magnitude(fn_liab) + leverage + fatl + ivaco + buzz(w=20) | 2.15 | 2.31 | 8.6% | 0.703 (vs rKlo39p1) | BLOCKED (just over threshold) |
| 15 | **9** | **YP0bLdzA** | **event-magnitude(fn_liab) + leverage + gric_flag + ivaco + buzz** | **2.32** | **2.22** | **10.7%** | **0.673 (vs WjGVJ7bN)** | **SAFE — WINNER** |

Full set of 57 gate-passers is queryable via:
```bash
uv run python3 scripts/hf_query.py --sql "SELECT r.alpha_id, r.sharpe, r.fitness, r.turnover, r.grade, j.expression FROM results r JOIN jobs j ON r.job_id=j.id WHERE j.tags_json LIKE '%20260711-001%' AND r.sharpe>=1.25 AND r.fitness>=1.0 ORDER BY r.fitness DESC"
```

## BRAIN Check Results (candidates that reached full 7-check verification)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|-------------------|----------------------|
| **YP0bLdzA** | PASS | PASS | PASS | PASS | PASS | PASS | PENDING (local est. 0.673, PASS) | PASS |
| P03ZkrkW | PASS | PASS | PASS | PASS | PASS | PASS | PENDING | PASS |
| VkPavmgJ | PASS | PASS | PASS | PASS | PASS | PASS | PENDING | PASS |
| WjGPr2xd | PASS | PASS | PASS | PASS | PASS | PASS | PENDING | PASS |
| E5Evj7wK | PASS | PASS | PASS | PASS | PASS | **FAIL (0.90 vs 0.91)** | PENDING | PASS |
| QPVbPqaM | PASS | PASS | PASS | PASS | PASS | PASS | PENDING | PASS |
| 6X9jXdRG | PASS | PASS | PASS | PASS | PASS | **FAIL (0.90 vs 0.91)** | PENDING | PASS |

BRAIN's `SELF_CORRELATION` sub-check never resolved to PASS/FAIL during this
session (10-retry polling on `/alphas/{id}/check` and `/alphas/{id}/correlations/self`
timed out repeatedly, including for control queries against already-ACTIVE
alphas) — all verdicts above rely on local PnL correlation vs the 44-alpha
ACTIVE universe as the fallback method.
