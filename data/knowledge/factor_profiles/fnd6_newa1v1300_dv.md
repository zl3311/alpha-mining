---
field: fnd6_newa1v1300_dv
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.98
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.236
ann_vol: 0.1195
hit_rate: 0.4988
rolling_sharpe_min: -2.103
rolling_sharpe_max: 1.865
negated_best_sharpe: 0.37
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.61
---
# fnd6_newa1v1300_dv (fundamental6)

*Cash Dividends (Cash Flow)*

## Signal Profile
- `rank(fnd6_newa1v1300_dv)`: S=0.12, F=0.04, T=1.5%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_dv / close)`: S=0.26, F=0.13, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_dv, 5))`: S=0.23, F=0.06, T=34.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_dv)`: S=-0.12, F=-0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dv, 5))`: S=-0.11, F=-0.03, T=29.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dv, 63)`: S=0.98, F=0.81, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dv, 10)`: S=0.15, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dv, 22))`: S=0.14, F=0.04, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dv)`: S=0.37, F=0.25, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dv / close)`: S=0.31, F=0.19, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+2.0%
  - 2020: S=-1.47 (negative), ret=-11.9%
  - 2021: S=0.94 (moderate), ret=+14.3%
  - 2022: S=1.15 (moderate), ret=+19.9%
  - 2023: S=-1.13 (negative), ret=-9.5%

## Risk & Drawdown
- Max drawdown: 23.60% over 785 days (recovered)
- Annualized: return +3.0%, volatility 11.9% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.07, excess kurtosis +2.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.10, max 1.86, latest -1.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.56%; worst month: -5.68%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.49
- Sideways: S=-0.04
- Bear: S=-2.76

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_dv)` S=0.37, F=0.25, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dv)`: S=0.37, F=0.25, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dv / close)`: S=0.31, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dv, 5))`: S=-0.11, F=-0.03, T=29.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dv / close)` | TOP1000 | 0.25 | 0.13 | 23.6% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dv / close)` | TOP3000 | 0.21 | 0.09 | 28.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dv, 5))` | TOP3000 | 0.21 | 0.06 | 33.9% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_dv, 5))` | TOP500 | 0.17 | 0.05 | 32.8% | 80% | mixed |
| `rank(fnd6_newa1v1300_dv)` | TOP1000 | 0.11 | 0.04 | 33.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dv, 5))` | TOP200 | 0.11 | 0.03 | 33.0% | 60% | mixed |
| `rank(fnd6_newa1v1300_dv)` | TOP3000 | 0.08 | 0.03 | 36.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_dividends: 1.000 (strongly positively correlated)
- anl4_af_div_value: 0.965 (strongly positively correlated)
- anl4_afv4_div_mean: 0.942 (strongly positively correlated)
- anl4_afv4_div_median: 0.939 (strongly positively correlated)
- anl4_afv4_div_high: 0.932 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
