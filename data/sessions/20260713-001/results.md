---
id: "20260713-001-results"
session: "20260713-001"
total_expressions: 67
gate_passers: 35
best_sharpe: 2.83
best_fitness: 2.51
best_alpha_id: "O0Z6NE0b"
---

# Results: Session 20260713-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 67 |
| Gate-passers (S>=1.25, F>=1.0) | 35 |
| Best Sharpe (any grade) | 2.83 (`KP9V7YLz`) |
| Best Fitness (any grade) | 2.51 (`A1PLkE6W`, BLOCKED self-corr) |
| Winning submittable candidate | `O0Z6NE0b` — EXCELLENT, S=2.10, F=2.02, self-corr 0.528 SAFE |
| Budget used | 67 / unlimited, across 8 rounds |

## Gate-Passers (Key Candidates by Round)

| # | Round | Alpha ID | Expression (abbreviated) | Sharpe | Fitness | Turnover | Self-Corr (local unless noted) | Verdict |
|---|-------|----------|---------------------------|--------|---------|----------|--------------------|---------|
| 1 | 1 | `vRlY5MPd` | event-mag(msaq)+leverage+ivaco+ffo+buzz | 2.59 | 2.43 | 15.6% | 0.8827 (BRAIN authoritative) | BLOCKED |
| 2 | 1 | `A1PLkE6W`(rd6) | event-mag(msaq)+leverage+drlt+ffo+buzz | 2.62 | 2.51 | 15.4% | 0.789 (local) | BLOCKED |
| 3 | 1-2 | `O0Z6bkKv` | `leverage*sign(delta(msaq,20)) + ivaco` (novel gating) | 1.83 | 1.32 | 11.3% | 0.520 (local) | SAFE (AVERAGE grade, below target) |
| 4 | 3 | `QPVWnxKK` | gating + ivaco + buzz | 2.53 | 1.71 | 22.7% | **0.5667 (BRAIN authoritative PASS)** | SAFE (GOOD grade, below EXCELLENT target) |
| 5 | 4 | `gJMr9zAK` | event-mag(current_ratio)+leverage+ivaco+ffo+buzz | 2.20 | 2.06 | 13.4% | 0.922 (local) | BLOCKED |
| 6 | 5 | `P03PGeex` | event-mag(msaq)+ivaco+drlt+ffo (no leverage, no buzz) | 2.03 | 1.70 | 6.5% | 0.590 (local) | RISKY (GOOD grade) |
| 7 | 6 | `KP9V7YLz` | event-mag(msaq)+ivaco+drlt+ffo+buzz (no leverage) | 2.83 | 2.49 | 15.6% | 0.646 (local) | RISKY (EXCELLENT grade, superseded below) |
| 8 | 7-8 | **`O0Z6NE0b`** | same as #7, **MARKET neut**, buzz window=10 | **2.10** | **2.02** | **12.7%** | **0.528 (local, SAFE)** | **SAFE — WINNER** |

Full set of 35 gate-passers is queryable via:
```bash
uv run python3 scripts/hf_query.py --gate-passers --tag session_20260713-001 --min-fitness 0 --min-sharpe 0
```

## BRAIN Check Results (candidates that reached full verification)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER/HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------------|-------------------------|-------------------|----------------------|
| **O0Z6NE0b** | PASS | PASS | PASS | PASS | PASS | PENDING (local est. 0.528, SAFE) | PASS |
| `vRlY5MPd` | PASS | PASS | PASS | PASS | PASS | **FAIL (0.8827 vs 0.70, authoritative)** | PASS |
| `QPVWnxKK` | PASS | PASS | PASS | PASS | PASS | **PASS (0.5667, authoritative via /correlations/self)** | PASS |

BRAIN's `/alphas/{id}/check` endpoint returned `SELF_CORRELATION: PENDING` for
every OTHER freshly-simulated candidate this session despite repeated 10-retry
polling — consistent with the platform-latency pattern documented in session
20260711-001.

## Round-by-Round Summary

1. **Round 1 (21 sims)**: novel structures (directional gating by fundamental
   trend, `ts_arg_max` recency, multi-horizon spread, non-return `ts_corr`,
   `quantile()`, cross-dataset ratio) on `fnd6_newqv1300_msaq` + proven
   event-magnitude/product-blend backstops. Best novel structure: AVERAGE
   (S=1.83). Event-magnitude backstop reached EXCELLENT but authoritative
   BRAIN check confirmed FAIL (0.8827).
2. **Rounds 2-3 (21 sims)**: amplified the directional-gating structure with
   window/decay/leg sweeps. `QPVWnxKK` confirmed self-corr PASS at 0.5667
   (BRAIN authoritative) but capped at GOOD (F<=1.88).
3. **Round 4 (8 sims)**: tested `current_ratio` (liquidity, economically
   distinct anchor) on the event-magnitude template — worse correlation
   (0.922) than `msaq`, proving the shared stabilizer skeleton (not anchor
   novelty) drives correlation.
4. **Round 5 (6 sims)**: removed `leverage` from the blend to escape the
   skeleton; removing `leverage`+`ivaco` together collapsed fitness
   (F<=0.67), removing only `leverage` (keep `ivaco+drlt`) preserved GOOD
   fitness (F=1.70) at improved but still-thin correlation (0.590).
5. **Round 6 (4 sims)**: added buzz back to the leverage-free
   `ivaco+drlt+ffo_flag` combo -> `KP9V7YLz`, EXCELLENT S=2.83 F=2.49, but
   RISKY correlation (0.646).
6. **Rounds 7-8 (12 sims)**: applied MARKET neutralization to `KP9V7YLz`'s
   expression (safe now that `leverage` is absent) and tuned the buzz window
   -> **`O0Z6NE0b`**, EXCELLENT S=2.10 F=2.02, SAFE correlation (0.528).
