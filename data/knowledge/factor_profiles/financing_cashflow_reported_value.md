---
field: financing_cashflow_reported_value
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.52
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 1
max_drawdown: 0.3197
ann_vol: 0.1192
hit_rate: 0.5028
rolling_sharpe_min: -1.497
rolling_sharpe_max: 2.663
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.06
---
# financing_cashflow_reported_value (analyst4)

*Cash Flow From Financing - Value*

## Signal Profile
- `rank(financing_cashflow_reported_value)`: S=0.04, F=0.01, T=5.0%, INFERIOR (TOP200)
- `rank(financing_cashflow_reported_value / close)`: S=0.15, F=0.06, T=5.1%, INFERIOR (TOP200)
- `rank(ts_delta(financing_cashflow_reported_value, 5))`: S=-0.08, F=-0.01, T=35.7%, INFERIOR (TOP200)
- `-rank(financing_cashflow_reported_value)`: S=0.26, F=0.12, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(financing_cashflow_reported_value, 5))`: S=0.58, F=0.17, T=38.5%, INFERIOR (TOP3000)
- `ts_zscore(financing_cashflow_reported_value, 22)`: S=0.52, F=0.19, T=38.2%, INFERIOR (TOP3000)
- `ts_mean(financing_cashflow_reported_value, 10)`: S=-0.56, F=-0.35, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(financing_cashflow_reported_value, 22))`: S=-0.13, F=-0.02, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * financing_cashflow_reported_value)`: S=0.26, F=0.12, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * financing_cashflow_reported_value / close)`: S=0.26, F=0.11, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.70 (negative), ret=-5.3%
  - 2020: S=1.69 (strong), ret=+16.3%
  - 2021: S=0.06 (weak), ret=+0.9%
  - 2022: S=-1.23 (negative), ret=-18.2%
  - 2023: S=1.87 (strong), ret=+15.4%

## Risk & Drawdown
- Max drawdown: 31.97% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +1.8%, volatility 11.9% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew -0.08, excess kurtosis +2.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 2.66, latest 1.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +8.36%; worst month: -9.20%
Positive months: 49%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.55
- Sideways: S=0.92
- Bear: S=1.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(financing_cashflow_reported_value, 5))` S=0.58, F=0.17, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * financing_cashflow_reported_value)`: S=0.26, F=0.12, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * financing_cashflow_reported_value / close)`: S=0.26, F=0.11, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(financing_cashflow_reported_value, 5))`: S=0.58, F=0.17, T=38.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(financing_cashflow_reported_value / close)` | TOP200 | 0.15 | 0.06 | 32.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_value: 1.000 (strongly positively correlated)
- anl4_cff_median: 0.797 (strongly positively correlated)
- anl4_cff_low: 0.795 (strongly positively correlated)
- est_cashflow_fin: 0.779 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.729 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
