---
field: fnd6_newqv1300_epsfiq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.76
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3763
ann_vol: 0.1101
hit_rate: 0.498
rolling_sharpe_min: -4.541
rolling_sharpe_max: 2.839
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.29
---
# fnd6_newqv1300_epsfiq (fundamental6)

*Earnings Per Share (Diluted) - Including Extraordinary Items*

## Signal Profile
- `rank(fnd6_newqv1300_epsfiq)`: S=0.22, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_epsfiq / close)`: S=0.29, F=0.15, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_epsfiq, 5))`: S=0.12, F=0.03, T=36.7%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_epsfiq)`: S=-0.17, F=-0.07, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epsfiq, 5))`: S=0.76, F=0.25, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_epsfiq, 22)`: S=0.47, F=0.16, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_epsfiq, 10)`: S=0.10, F=0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_epsfiq, 22))`: S=0.34, F=0.10, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epsfiq)`: S=-0.22, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epsfiq / close)`: S=-0.29, F=-0.15, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-0.9%
  - 2020: S=-3.86 (negative), ret=-25.9%
  - 2021: S=1.63 (strong), ret=+18.7%
  - 2022: S=1.57 (strong), ret=+25.8%
  - 2023: S=-0.25 (negative), ret=-2.7%

## Risk & Drawdown
- Max drawdown: 37.63% over 801 days (recovered)
- Annualized: return +3.1%, volatility 11.0% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew -0.18, excess kurtosis +1.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.54, max 2.84, latest -0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.76%; worst month: -9.36%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.82
- Sideways: S=0.45
- Bear: S=-3.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_epsfiq, 5))` S=0.76, F=0.25, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_epsfiq)`: S=-0.22, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epsfiq / close)`: S=-0.29, F=-0.15, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epsfiq, 5))`: S=0.76, F=0.25, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_epsfiq / close)` | TOP3000 | 0.28 | 0.15 | 37.6% | 40% | bull-only |
| `rank(fnd6_newqv1300_epsfiq)` | TOP3000 | 0.22 | 0.10 | 41.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_epsfiq / close)` | TOP1000 | 0.16 | 0.07 | 33.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_epsfiq)` | TOP1000 | 0.16 | 0.07 | 39.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_epsfiq, 5))` | TOP200 | 0.11 | 0.03 | 31.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_epspiq: 1.000 (strongly positively correlated)
- eps: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.999 (strongly positively correlated)
- earnings_per_share_reported_value: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
