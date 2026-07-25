---
field: fnd6_newa1v1300_bkvlps
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.48
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1394
ann_vol: 0.0897
hit_rate: 0.4704
rolling_sharpe_min: -1.909
rolling_sharpe_max: 1.972
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_newa1v1300_bkvlps (fundamental6)

*Book Value Per Share*

## Signal Profile
- `rank(fnd6_newa1v1300_bkvlps)`: S=0.30, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_bkvlps / close)`: S=0.48, F=0.28, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_bkvlps, 5))`: S=0.34, F=0.13, T=39.5%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_bkvlps)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_bkvlps, 5))`: S=0.33, F=0.11, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_bkvlps, 63)`: S=0.47, F=0.28, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_bkvlps, 10)`: S=-0.33, F=-0.15, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_bkvlps, 22))`: S=-0.30, F=-0.12, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_bkvlps)`: S=-0.30, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_bkvlps / close)`: S=-0.48, F=-0.28, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.78 (negative), ret=-4.7%
  - 2020: S=0.30 (weak), ret=+3.9%
  - 2021: S=1.42 (moderate), ret=+11.3%
  - 2022: S=0.93 (moderate), ret=+6.4%
  - 2023: S=0.48 (weak), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 13.94% over 474 days (recovered)
- Annualized: return +4.2%, volatility 9.0% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +1.01, excess kurtosis +5.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 1.97, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.32%; worst month: -4.34%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.59
- Sideways: S=-0.91
- Bear: S=0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_bkvlps, 5))` S=0.33, F=0.11, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_bkvlps)`: S=-0.30, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_bkvlps / close)`: S=-0.48, F=-0.28, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_bkvlps, 5))`: S=0.33, F=0.11, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_bkvlps / close)` | TOP3000 | 0.47 | 0.28 | 13.9% | 80% | all-weather |
| `rank(fnd6_newa1v1300_bkvlps)` | TOP3000 | 0.28 | 0.14 | 35.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_bkvlps, 5))` | TOP1000 | 0.35 | 0.13 | 28.0% | 60% | weak |
| `rank(fnd6_newa1v1300_bkvlps / close)` | TOP1000 | 0.23 | 0.10 | 13.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- book_value_per_share_2: 0.910 (strongly positively correlated)
- est_bookvalue_ps: 0.908 (strongly positively correlated)
- fnd6_optprcey: 0.888 (strongly positively correlated)
- book_value_per_share_reported_value: 0.887 (strongly positively correlated)
- anl4_bvps_high: 0.872 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
