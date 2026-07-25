---
id: "20260626-001-results"
session: "20260626-001"
total_expressions: 41
gate_passers: 12
best_sharpe: 2.08
best_fitness: 2.42
best_alpha_id: "XgpJGaL0"
---

# Results: Session 20260626-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 41 |
| Gate-passers (S>=1.25, F>=1.0) | 12 |
| Best Sharpe | 2.08 (XgpJGaL0) |
| Best Fitness | 2.42 (MPp3WAd9) |
| Budget used | 41 / no cap |

## Gate-Passers

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Family | Verdict |
|---|----------|-----------|--------|---------|----------|--------|---------|
| 1 | XgpJGaL0 | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(open / close - 1), 5) | 2.08 | 2.36 | 16.0% | eps_revision_depreciation_intraday | SAFE |
| 2 | MPp3WAd9 | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(-1 * equity / assets), 5) | 1.95 | 2.42 | 9.7% | eps_revision_depreciation_leverage | SAFE |
| 3 | E5wR7wN0 | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(abs(ts_delta(fnd6_newqv1300_dpactq / close, 3))), 5) | 1.95 | 2.36 | 13.3% | eps_revision_depreciation_event | unchecked |
| 4 | akdxY6Kw | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + zscore(fnd6_newqv1300_dpactq / close), 5) | 1.84 | 2.23 | 9.8% | eps_revision_depreciation | unchecked |
| 5 | d5x1XWlj | rank(abs(ts_delta(fnd6_newqv1300_dpactq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close) | 1.80 | 1.87 | 11.6% | depreciation_event_leverage | unchecked |
| 6 | QPaKJOew | ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_dpactq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 3) | 1.78 | 1.84 | 9.8% | depreciation_event_leverage | unchecked |
| 7 | pw65mA2x | ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_dpactq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5) | 1.77 | 1.83 | 9.0% | depreciation_event_leverage | unchecked |
| 8 | RRp63q9j | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(fnd6_fatl / close), 5) | 1.77 | 2.36 | 9.7% | eps_revision_depreciation_capint | unchecked |
| 9 | LLpZWgG9 | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close), 3) | 1.76 | 2.15 | 10.8% | eps_revision_depreciation | SAFE |
| 10 | O0p80V3R | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close), 5) | 1.74 | 2.11 | 10.7% | eps_revision_depreciation | SAFE |
| 11 | 3q7VwVw0 | ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close), 10) | 1.72 | 2.07 | 10.4% | eps_revision_depreciation | unchecked |
| 12 | vRL2qN0w | ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_dpactq / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5) | 1.71 | 1.75 | 9.6% | depreciation_event_leverage | unchecked |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| XgpJGaL0 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.604) | PASS |
| MPp3WAd9 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.662) | PASS |
| E5wR7wN0 | PASS | PASS | PASS | PASS | PASS | PASS | unchecked | PASS |
| LLpZWgG9 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.591) | PASS |
| O0p80V3R | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.590) | PASS |

## Non-Gate-Passers Summary

| Template | Count | Best Result | Issue |
|----------|-------|-------------|-------|
| Dynamic correlation (ts_corr) | 4 | S=1.00 | No signal in ts_corr(fundamental, returns) |
| Inter-field ratios (F1/F2) | 4 | S=0.26 | Fundamental ratios produce no signal |
| Novel field blends (txs, dn, nopio, etc.) | 5 | S=1.22 | Below EXCELLENT threshold |
| Multiplicative epsr * deprec | 1 | S=0.70 | Product kills the signal |
| MARKET neut of winner | 1 | S=1.34 | MARKET kills sparse flag signals |
