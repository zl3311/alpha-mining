---
field: fnd6_cptnewqv1300_oeps12
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.31
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3572
ann_vol: 0.1204
hit_rate: 0.4955
rolling_sharpe_min: -3.958
rolling_sharpe_max: 2.64
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: 0.22
---
# fnd6_cptnewqv1300_oeps12 (fundamental6)

*Earnings Per Share from Operations - 12 Months Moving*

## Signal Profile
- `rank(fnd6_cptnewqv1300_oeps12)`: S=0.16, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_oeps12 / close)`: S=0.31, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_oeps12, 5))`: S=0.21, F=0.06, T=36.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_oeps12)`: S=-0.06, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_oeps12, 5))`: S=0.53, F=0.15, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_oeps12, 22)`: S=0.49, F=0.17, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_oeps12, 10)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_oeps12, 22))`: S=0.40, F=0.14, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oeps12)`: S=-0.16, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oeps12 / close)`: S=-0.31, F=-0.17, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.13 (negative), ret=-0.6%
  - 2020: S=-3.03 (negative), ret=-22.2%
  - 2021: S=1.32 (moderate), ret=+18.3%
  - 2022: S=1.38 (moderate), ret=+24.2%
  - 2023: S=-0.19 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 35.72% over 792 days (recovered)
- Annualized: return +3.6%, volatility 12.0% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.01, excess kurtosis +1.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.96, max 2.64, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.42%; worst month: -7.88%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=0.34
- Bear: S=-3.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_oeps12, 5))` S=0.53, F=0.15, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_oeps12)`: S=-0.16, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oeps12 / close)`: S=-0.31, F=-0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_oeps12, 5))`: S=0.53, F=0.15, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_oeps12 / close)` | TOP3000 | 0.30 | 0.17 | 35.7% | 40% | bull-only |
| `rank(fnd6_cptnewqv1300_oeps12)` | TOP3000 | 0.15 | 0.07 | 45.9% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_oeps12 / close)` | TOP1000 | 0.14 | 0.06 | 32.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_oeps12, 5))` | TOP200 | 0.22 | 0.06 | 28.7% | 40% | all-weather |
| `rank(ts_delta(fnd6_cptnewqv1300_oeps12, 5))` | TOP500 | 0.14 | 0.03 | 11.6% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_oepf12: 1.000 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 0.967 (strongly positively correlated)
- fnd6_cptnewqv1300_opepsq: 0.966 (strongly positively correlated)
- fnd6_cptmfmq_opepsq: 0.966 (strongly positively correlated)
- fnd6_oprepsx: 0.965 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
