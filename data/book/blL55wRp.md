---
alpha_id: "blL55wRp"
name: "vol_gated_capintensity_totassets_buzz"
tags:
  - "capital_intensity"
  - "analyst4"
  - "totassets_flag"
  - "volatility_gate"
  - "buzz_stabilizer"
  - "session_20260618-001"
  - "excellent"
expression: "trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(fnd6_fate / close) + rank(anl4_totassets_flag) + rank(open / close - 1) + rank(ts_mean(scl12_buzz, 5)), 5), ts_std_dev(returns, 20) < 0.01)"
sharpe: 2.10
fitness: 2.03
turnover: 0.167
grade: "EXCELLENT"
family: "capital_intensity_totassets_volregime"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.6941
self_corr_peer: "6Xzm6PQP"
self_corr_method: "brain_self_correlation_check"
self_corr_result: "PASS"
status: "ACTIVE"
session: "20260618-001"
brain_url: "https://platform.worldquantbrain.com/alpha/blL55wRp"
---

# Alpha: blL55wRp

## Expression

```
trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(fnd6_fate / close) + rank(anl4_totassets_flag) + rank(open / close - 1) + rank(ts_mean(scl12_buzz, 5)), 5), ts_std_dev(returns, 20) < 0.01)
```

## Simulation Settings

| Setting | Value |
|---------|-------|
| Region | USA |
| Universe | TOP3000 |
| Delay | 1 |
| Decay | 6 |
| Neutralization | SUBINDUSTRY |
| Truncation | 0.08 |

## Mechanism

Capital intensity (fixed asset turnover efficiency, `fnd6_fate/close`) combined
with analyst total-assets revision (`anl4_totassets_flag`), intraday dislocation
(`open/close - 1`), and social attention breadth (`ts_mean(scl12_buzz, 5)`).
The volatility-regime gate concentrates exposure into elevated-volatility periods,
which lifts liquid sub-universe Sharpe and reduces self-correlation vs the
guidance/fundamental book cluster.

The ungated 3-leg base (`KPbjjWPx`, S=2.07 F=2.30) passes all computable BRAIN
checks but FAILS self-corr at 0.84 vs `6Xzm6PQP`. The volatility gate drops
self-corr from 0.84 to 0.69, confirming the pattern from `0m7lnAEr`.

## Self-Correlation Profile

BRAIN authoritative check PASS at 0.6941, with top correlated peer `6Xzm6PQP`
(guidance_fundamental, S=2.31) at 0.694. Below the 0.70 threshold; no Sharpe
premium escape needed. Margin is thin (0.006 below limit).

Other correlated book entries:
- 0mzQQvX8: 0.6425
- pw8wNe76: 0.5973
- np30Odjd: 0.5946
- xARzmVEW: 0.5910
