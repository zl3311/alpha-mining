---
alpha_id: "XgpJGaL0"
name: "cumrev_epsr_depreciation_intraday"
status: "ACTIVE"
grade: "EXCELLENT"
family: "cumrev_depreciation_reversal"
tags:
  - "analyst4"
  - "fundamental6"
  - "intraday"
  - "anl4_epsr_flag"
  - "fnd6_newqv1300_dpactq"
  - "overnight_gap"
  - "session_20260626-001"
  - "excellent"
sharpe: 2.08
fitness: 2.36
turnover: 0.16
self_corr: 0.604
self_corr_verdict: "PASS"
top_corr_peer: "6Xzm6PQP"
top_corr_value: 0.604
brain_checks: "ALL PASS"
expression: "ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(open / close - 1), 5)"
settings:
  region: "USA"
  universe: "TOP3000"
  decay: 6
  neutralization: "SUBINDUSTRY"
  truncation: 0.08
session: "20260626-001"
discovered: "20260626-001"
brain_url: "https://platform.worldquantbrain.com/alpha/XgpJGaL0"
---

# XgpJGaL0 — Cumulative EPS Revision + Depreciation + Intraday Reversal

## Mechanism

Three-factor blend combining:

1. **Cumulative analyst EPS revision** (`zscore(ts_sum(anl4_epsr_flag, 22))`):
   Accumulated analyst conviction over 22 days. Uses `zscore` normalization
   (critical for sparse flag fields) and `ts_sum` (captures revision persistence).

2. **Depreciation-to-price** (`rank(fnd6_newqv1300_dpactq / close)`):
   Capital depreciation intensity relative to market price. High depreciation
   signals capital-heavy operations where replacement value diverges from market
   cap — a value signal from a novel fundamental6 field not yet in the book.

3. **Intraday reversal** (`rank(open / close - 1)`): Short-term mean-reversion
   from overnight gap corrections. Provides dense daily signal that stabilizes
   the sparse analyst and quarterly fundamental legs.

## Self-Correlation Notes

BRAIN self-corr = 0.604, below 0.70 threshold → auto PASS. The `zscore(ts_sum())`
wrapper avoids the `flag*(-ret)` driver that is the #1 correlation driver for
existing analyst revision entries. The combination of `anl4_epsr_flag` accumulation
with depreciation intensity produces a structurally distinct signal.

Top peer: 6Xzm6PQP (guidance_fundamental, S=2.31) at 0.604.

## Companion Candidates

- MPp3WAd9: S=1.95, F=2.42, self-corr=0.662 PASS (leverage variant)
- E5wR7wN0: S=1.95, F=2.36, self-corr=0.632 PASS (event magnitude variant)
