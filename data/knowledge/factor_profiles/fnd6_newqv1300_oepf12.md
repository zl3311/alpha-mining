---
field: fnd6_newqv1300_oepf12
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.31
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3623
ann_vol: 0.122
hit_rate: 0.4996
rolling_sharpe_min: -4.009
rolling_sharpe_max: 2.613
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: 0.16
---
# fnd6_newqv1300_oepf12 (fundamental6)

*Earnings Per Share - Diluted - from Operations - 12MM*

## Signal Profile
- `rank(fnd6_newqv1300_oepf12)`: S=0.16, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_oepf12 / close)`: S=0.31, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_oepf12, 5))`: S=0.22, F=0.06, T=36.4%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_oepf12)`: S=-0.07, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_oepf12, 5))`: S=0.47, F=0.12, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_oepf12, 22)`: S=0.45, F=0.15, T=37.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_oepf12, 10)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_oepf12, 22))`: S=0.36, F=0.11, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepf12)`: S=-0.16, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepf12 / close)`: S=-0.31, F=-0.17, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-0.4%
  - 2020: S=-3.08 (negative), ret=-22.6%
  - 2021: S=1.31 (moderate), ret=+18.4%
  - 2022: S=1.38 (moderate), ret=+24.7%
  - 2023: S=-0.21 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 36.23% over 792 days (recovered)
- Annualized: return +3.6%, volatility 12.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.01, excess kurtosis +1.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.01, max 2.61, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.54%; worst month: -7.99%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.91
- Sideways: S=0.33
- Bear: S=-3.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_oepf12, 5))` S=0.47, F=0.12, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_oepf12)`: S=-0.16, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepf12 / close)`: S=-0.31, F=-0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_oepf12, 5))`: S=0.47, F=0.12, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_oepf12 / close)` | TOP3000 | 0.29 | 0.17 | 36.2% | 40% | bull-only |
| `rank(fnd6_newqv1300_oepf12 / close)` | TOP1000 | 0.15 | 0.07 | 32.1% | 40% | bull-only |
| `rank(fnd6_newqv1300_oepf12)` | TOP3000 | 0.15 | 0.07 | 46.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_oepf12, 5))` | TOP200 | 0.23 | 0.06 | 26.3% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_oepf12, 5))` | TOP500 | 0.17 | 0.04 | 14.3% | 60% | mixed |
| `rank(fnd6_newqv1300_oepf12)` | TOP1000 | 0.06 | 0.02 | 41.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_oeps12: 1.000 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 0.968 (strongly positively correlated)
- fnd6_cptnewqv1300_opepsq: 0.968 (strongly positively correlated)
- fnd6_cptmfmq_opepsq: 0.967 (strongly positively correlated)
- earnings_per_share_reported: 0.965 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
