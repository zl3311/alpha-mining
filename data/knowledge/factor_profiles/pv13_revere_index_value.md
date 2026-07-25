---
field: pv13_revere_index_value
dataset: pv13
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.4144
ann_vol: 0.11
hit_rate: 0.4453
rolling_sharpe_min: -3.199
rolling_sharpe_max: 2.762
negated_best_sharpe: 0.01
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.6
---
# pv13_revere_index_value (pv13)

*Value of specified index for the date*

## Signal Profile
- `rank(pv13_revere_index_value)`: S=0.22, F=0.10, T=2.0%, INFERIOR (TOP200)
- `rank(pv13_revere_index_value / close)`: S=0.61, F=0.46, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_index_value, 5))`: S=0.30, F=0.15, T=6.1%, INFERIOR (TOP3000)
- `-rank(pv13_revere_index_value)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_index_value, 5))`: S=-0.32, F=-0.16, T=6.1%, INFERIOR (TOP3000)
- `ts_zscore(pv13_revere_index_value, 22)`: S=0.40, F=0.09, T=33.2%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_index_value, 10)`: S=0.21, F=0.08, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_index_value, 22))`: S=-0.24, F=-0.10, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_value)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_value / close)`: S=-0.61, F=-0.46, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/12P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/9P
- LOW_TURNOVER: 1F/24P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.29, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.51 (strong), ret=+27.0%
  - 2020: S=-1.20 (negative), ret=-11.8%
  - 2021: S=-0.16 (negative), ret=-2.8%
  - 2022: S=0.97 (moderate), ret=+6.4%
  - 2023: S=-0.56 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 41.44% over 1506 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 11.0% (fraction of booksize)
- Hit rate: 44.5% positive days
- Tail shape: skew +0.77, excess kurtosis +8.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.20, max 2.76, latest -0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +31.07%; worst month: -11.49%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.31
- Sideways: S=0.11
- Bear: S=-2.27

## Negated Direction
Best negated: `-rank(pv13_revere_index_value)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_revere_index_value)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_value / close)`: S=-0.61, F=-0.46, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_index_value, 5))`: S=-0.32, F=-0.16, T=6.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_index_value, 5))` | TOP3000 | 0.29 | 0.15 | 41.4% | 40% | bull-only |
| `rank(pv13_revere_index_value)` | TOP200 | 0.22 | 0.10 | 37.7% | 60% | bull-only |
| `rank(pv13_revere_index_value)` | TOP500 | 0.11 | 0.03 | 29.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pv13_revere_index_cap: 0.993 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.755 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.740 (strongly positively correlated)
- cash: 0.736 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.735 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
