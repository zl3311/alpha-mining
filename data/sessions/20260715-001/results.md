---
id: "20260715-001-results"
session: "20260715-001"
total_expressions: 25
gate_passers: 8
best_sharpe: 2.62
best_fitness: 2.12
best_alpha_id: "lelNqEZl"
---

# Results: Session 20260715-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 25 (15 round 1 + 10 round 2) |
| Gate-passers (S>=1.25, F>=1.0) | 8 |
| Best Sharpe (any grade) | 2.62 (`VkPR1LYJ`, self-corr FAIL) |
| Best submittable Fitness | 2.01 (`lelNqEZl`, SAFE) |
| Budget used | 25 (unlimited cap, manual session) |

## Gate-Passers

| # | Alpha ID | Expression (truncated) | Sharpe | Fitness | Turnover | Family | Self-Corr | Verdict |
|---|----------|-----------|--------|---------|----------|--------|-----------|---------|
| 1 | `blqKkP2l` | `ts_arg_max` recency + leverage + ivaco + drlt + buzz on `fn_assets_fair_val_l2_q` | 2.55 | 2.03 | 20.9% | fair_val_assets_recency_arg_max | 0.701 FAIL | BLOCKED |
| 2 | `lelNqEZl` | event-magnitude + leverage + cff_flag + drlt + ivaco + buzz on `fn_assets_fair_val_l2_q` | 2.01 | 2.01 | 11.0% | fair_val_assets_event_magnitude_leverage_blend | 0.567 PASS | **SAFE (submittable)** |
| 3 | `GrL7P6p5` | event-magnitude + leverage + cfo_flag + ivaco + buzz on `fnd6_dpvieb` | 1.98 | 2.12 | 12.4% | dpvieb_event_magnitude (mega-cluster #1) | 0.820 FAIL | BLOCKED |
| 4 | `VkPR1LYJ` | multi-horizon spread + leverage + drlt + buzz on `fnd6_dcvsub` | 2.62 | 1.93 | 25.9% | dcvsub_multi_horizon_spread | 0.848 FAIL | BLOCKED |
| 5 | `N1r20nKL` | event-magnitude + leverage + cff_flag + drlt + buzz on `fn_assets_fair_val_l2_q` (5-factor) | 1.79 | 1.75 | 11.8% | fair_val_assets_event_magnitude_leverage_blend | 0.572 PASS | REDUNDANT (superseded by `lelNqEZl`) |
| 6 | `zqmLK581` | `ts_arg_max` recency + leverage + drlt (no buzz) on `fn_assets_fair_val_l2_q` | 1.84 | 1.58 | 12.3% | fair_val_assets_recency_arg_max | 0.588 PASS | REDUNDANT (superseded by `blqKkP2l`/`lelNqEZl`) |
| 7 | `58O2xl1k` | event-magnitude + leverage + cfo_flag + ivaco + buzz on `fnd6_mrct` | 1.66 | 1.58 | 12.9% | mrct_event_magnitude | PENDING | GOOD, not pursued (lower fitness than `fn_assets_fair_val_l2_q` variant) |
| 8 | `qMlwr1Vj` | event-magnitude (d=5) + leverage + cff_flag + drlt + buzz on `fn_assets_fair_val_l2_q` | 1.80 | 1.77 | 11.9% | fair_val_assets_event_magnitude_leverage_blend | PENDING | GOOD (d=5 window inferior to d=3; superseded) |

## All Expressions Tested

| # | Expression | Sharpe | Fitness | Turnover | Status |
|---|-----------|--------|---------|----------|--------|
| 1 | `rank(-1 * ts_arg_max(abs(ts_delta(fnd6_mrct/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close)` | 1.51 | 1.00 | 15.9% | INFERIOR (self-corr 0.739 FAIL) |
| 2 | `rank(-1 * ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_drlt/close)` | 1.84 | 1.58 | 12.3% | GOOD (self-corr 0.588 PASS) |
| 3 | `rank(-1 * ts_arg_max(abs(ts_delta(fnd6_dpvieb/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close)` | 1.89 | 1.47 | 15.2% | AVERAGE (self-corr 0.770 FAIL) |
| 4 | `rank(ts_delta(fnd6_dpvieb,5)/ts_std_dev(fnd6_dpvieb,20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close)` | -0.04 | -0.01 | 44.4% | DEAD (new dead zone) |
| 5 | `rank(ts_delta(fn_assets_fair_val_l2_q,5)/ts_std_dev(fn_assets_fair_val_l2_q,20)) + rank(-1*equity/assets) + rank(fnd6_drlt/close)` | -0.13 | -0.04 | 36.2% | DEAD (new dead zone) |
| 6 | `rank(zscore(fnd6_mrct/close,10) - zscore(fnd6_mrct/close,60)) + ...` | — | — | — | ERROR (zscore is 1-arg; fixed in round 2 with ts_zscore) |
| 7 | `rank(zscore(fnd6_dcvsub/close,10) - zscore(fnd6_dcvsub/close,60)) + ...` | — | — | — | ERROR (same operator-arity mistake) |
| 8 | `rank(ts_delta(fnd6_dcvsub,5) - ts_delta(fnd6_dcvsub,22)) + rank(-1*equity/assets) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 2.62 | 1.93 | 25.9% | GOOD (self-corr 0.848 FAIL) |
| 9 | `ts_decay_linear((rank(-1*returns)-0.5)*abs(rank(-1*returns)-0.5) + rank(anl4_cfo_flag) + rank(anl4_cff_flag) + rank(fnd6_ivaco/close), 5)` | 1.45 | 1.17 | 5.4% | AVERAGE (self-corr 0.760 FAIL) |
| 10 | `trade_when(ts_delta(fnd6_ivaco,20)>0, ts_decay_linear(rank(abs(ts_delta(fnd6_mrct/close,3)))+rank(-1*equity/assets)+rank(fnd6_drlt/close),5), ts_delta(fnd6_ivaco,20)<=0)` | 0.01 | 0.00 | 23.3% | DEAD (new dead zone) |
| 11 | `rank(ts_mean(scl12_buzz,10)) * rank(abs(ts_delta(fnd6_dpvieb/close,5)))` | 0.97 | 0.59 | 14.1% | DEAD (new dead zone) |
| 12 | `rank(ts_mean(scl12_buzz,10)) * rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,5)))` | 0.51 | 0.22 | 10.9% | DEAD (new dead zone) |
| 13 | `ts_decay_linear(rank(abs(ts_delta(fnd6_dpvieb/close,3)))+rank(-1*equity/assets)+rank(anl4_cfo_flag)+rank(fnd6_ivaco/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 1.98 | 2.12 | 12.4% | EXCELLENT (self-corr 0.820 FAIL — dpvieb is in mega-cluster #1) |
| 14 | `ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,3)))+rank(-1*equity/assets)+rank(anl4_cff_flag)+rank(fnd6_drlt/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 1.79 | 1.75 | 11.8% | GOOD (self-corr 0.572 PASS) |
| 15 | `ts_decay_linear(rank(abs(ts_delta(fnd6_mrct/close,3)))+rank(-1*equity/assets)+rank(anl4_cfo_flag)+rank(fnd6_ivaco/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 1.66 | 1.58 | 12.9% | GOOD |
| 16 | `rank(-1*ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 2.26 | 1.65 | 23.6% | GOOD |
| 17 | `rank(-1*ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 2.53 | 1.83 | 23.4% | GOOD |
| 18 | `rank(-1*ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q/close,1)),20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 2.55 | 2.03 | 20.9% | EXCELLENT (self-corr 0.701 FAIL — 0.001 over, Sharpe premium missed by 0.002) |
| 19 | `rank(-1*ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q/close,1)),40)) + rank(-1*equity/assets) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 2.01 | 1.44 | 21.8% | AVERAGE (window=40 worse than 20) |
| 20 | `ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,3)))+rank(-1*equity/assets)+rank(anl4_cff_flag)+rank(fnd6_drlt/close)+rank(fnd6_ivaco/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 2.01 | 2.01 | 11.0% | **EXCELLENT (self-corr 0.567 PASS — SAFE, submittable = `lelNqEZl`)** |
| 21 | `ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,5)))+rank(-1*equity/assets)+rank(anl4_cff_flag)+rank(fnd6_drlt/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 1.80 | 1.77 | 11.9% | GOOD (d=5 inferior to d=3) |
| 22 | `ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q/close,3)))+rank(-1*equity/assets)+rank(anl4_cfo_flag)+rank(fnd6_drlt/close)+rank(ts_mean(scl12_buzz,5)*(-1*returns)),5)` | 1.76 | 1.67 | 11.5% | GOOD (cfo_flag inferior to cff_flag) |
| 23 | `rank(ts_delta(fn_assets_fair_val_l2_q,5) - ts_delta(fn_assets_fair_val_l2_q,22)) + rank(-1*equity/assets) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 1.84 | 1.24 | 23.6% | AVERAGE (multi-horizon spread weaker than event-magnitude on this anchor) |
| 24 | `rank(ts_zscore(fn_assets_fair_val_l2_q/close,10) - ts_zscore(fn_assets_fair_val_l2_q/close,60)) + rank(-1*equity/assets) + rank(fnd6_drlt/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 1.95 | 1.38 | 25.9% | AVERAGE (regime-divergence weaker than event-magnitude) |
| 25 | `rank(ts_zscore(fnd6_mrct/close,10) - ts_zscore(fnd6_mrct/close,60)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close) + rank(ts_mean(scl12_buzz,5)*(-1*returns))` | 1.70 | 1.08 | 26.5% | AVERAGE |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| `lelNqEZl` | PASS (2.01) | PASS (2.01) | PASS | PASS (0.1104) | PASS | PASS (1.61 vs 0.87) | **PASS (AUTHORITATIVE, 0.5666 vs 0.70)** | PASS |
| `blqKkP2l` | PASS (2.55) | PASS (2.03) | PASS | PASS (0.2095) | PASS | PASS | ERROR (unresolved on BRAIN; local PnL est. 0.701 FAIL) | PASS |

Note: `lelNqEZl`'s SELF_CORRELATION check returned `PENDING` for the first
~9 minutes after simulation, then resolved to the authoritative value shown
above (confirmed stable across 3 independent polls ~3.5 min apart, per the
known async-computation lag documented in session 20260711-001).
`blqKkP2l`'s check returned a distinct `ERROR` state (not PENDING, not
PASS/FAIL) that had not resolved by the end of this session.
