---
field: anl4_cff_value
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.91
best_fitness: 0.46
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
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.33
---
# anl4_cff_value (analyst4)

*Cash Flow From Financing - announced financial value*

## Signal Profile
- `rank(anl4_cff_value)`: S=0.04, F=0.01, T=5.0%, INFERIOR (TOP200)
- `rank(anl4_cff_value / close)`: S=0.15, F=0.06, T=5.1%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_value, 5))`: S=-0.02, F=0.00, T=37.5%, INFERIOR (TOP500)
- `-rank(anl4_cff_value)`: S=0.26, F=0.12, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_value, 5))`: S=0.18, F=0.03, T=40.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cff_value, 22)`: S=0.91, F=0.46, T=38.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_value, 10)`: S=-0.56, F=-0.35, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_value, 22))`: S=0.14, F=0.03, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_value)`: S=0.47, F=0.27, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_value / close)`: S=0.58, F=0.35, T=4.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

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
Best negated: `rank(-1 * anl4_cff_value / close)` S=0.58, F=0.35, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cff_value)`: S=0.47, F=0.27, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_value / close)`: S=0.58, F=0.35, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_value, 5))`: S=0.18, F=0.03, T=40.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cff_value / close)` | TOP200 | 0.15 | 0.06 | 32.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- financing_cashflow_reported_value: 1.000 (strongly positively correlated)
- anl4_cff_median: 0.797 (strongly positively correlated)
- anl4_cff_low: 0.795 (strongly positively correlated)
- est_cashflow_fin: 0.779 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.729 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
