---
alpha_id: "xAxVAYwn"
status: "ACTIVE"
grade: "SPECTACULAR"
sharpe: 1.54
fitness: 2.62
turnover: 0.079
family: "buzz_reversal_accumulated"
dataset: "socialmedia12 + analyst4"
fields:
  - "scl12_buzz"
  - "returns"
  - "anl4_bvps_flag"
  - "anl4_netdebt_flag"
expression: "ts_decay_linear(zscore(ts_sum(scl12_buzz * (-1 * returns), 22)) + rank(anl4_bvps_flag) + rank(anl4_netdebt_flag), 5)"
neutralization: "SUBINDUSTRY"
decay: 12
universe: "TOP3000"
region: "USA"
self_corr_value: 0.419
self_corr_result: "PASS"
self_corr_peer: "XgpJGaL0"
brain_checks: "ALL PASS"
session: "20260628-001"
submitted_date: "2026-06-28"
platform_url: "https://platform.worldquantbrain.com/alpha/xAxVAYwn"
---

# xAxVAYwn — Accumulated Buzz Reversal + BVPS + NetDebt (22d)

## Expression

```
ts_decay_linear(zscore(ts_sum(scl12_buzz * (-1 * returns), 22)) + rank(anl4_bvps_flag) + rank(anl4_netdebt_flag), 5)
```

Settings: SUBINDUSTRY neutralization, decay=12, USA TOP3000

## Mechanism

Three-factor blend capturing attention-driven overselling reversion with dual
analyst revision confirmation:

1. **Accumulated buzz reversal** (`zscore(ts_sum(scl12_buzz * (-1 * returns), 22))`):
   Stocks consistently discussed on social media AND experiencing negative returns
   over 22 days are deeply oversold. The longer 22-day window captures extended
   panic cycles with very low turnover (7.9%).

2. **BVPS revision** (`rank(anl4_bvps_flag)`): Book value per share analyst revision
   adds contrarian quality — positive fundamental revisions during social media panic.

3. **Net debt revision** (`rank(anl4_netdebt_flag)`): Net debt revision provides a
   second orthogonal confirmation signal — improving balance sheet health during
   market panic indicates structural undervaluation.

## Self-Correlation Profile

Self-corr 0.419 vs XgpJGaL0 (top peer). Well below 0.7 threshold — auto PASS.
The buzz reversal mechanism creates genuinely different position rankings from
the fundamental/analyst/options families that dominate the existing book.
