---
field: fnd6_cptnewqv1300_epsx12
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.87
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1401
ann_vol: 0.13
hit_rate: 0.5239
rolling_sharpe_min: -1.053
rolling_sharpe_max: 2.988
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.31
---
# fnd6_cptnewqv1300_epsx12 (fundamental6)

*Earnings Per Share (Basic) - Excluding Extraordinary Items - 12 Months Moving*

## Signal Profile
- `rank(fnd6_cptnewqv1300_epsx12)`: S=0.12, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_epsx12 / close)`: S=0.17, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_epsx12, 5))`: S=0.56, F=0.25, T=36.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_epsx12)`: S=0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsx12, 5))`: S=0.87, F=0.32, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptnewqv1300_epsx12, 63)`: S=0.05, F=0.01, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_epsx12, 10)`: S=-0.11, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_epsx12, 22))`: S=-0.18, F=-0.04, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsx12)`: S=-0.12, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsx12 / close)`: S=-0.17, F=-0.07, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.84 (negative), ret=-7.6%
  - 2020: S=0.87 (moderate), ret=+11.5%
  - 2021: S=-0.22 (negative), ret=-3.2%
  - 2022: S=2.39 (strong), ret=+33.5%
  - 2023: S=0.16 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 14.01% over 458 days (not yet recovered, ongoing at window end)
- Annualized: return +7.4%, volatility 13.0% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.21, excess kurtosis +4.97

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 2.99, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.46%; worst month: -10.39%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.86
- Sideways: S=-0.04
- Bear: S=0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsx12, 5))` S=0.87, F=0.32, INFERIOR
Direction gap: +0.31 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_epsx12)`: S=-0.12, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsx12 / close)`: S=-0.17, F=-0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsx12, 5))`: S=0.87, F=0.32, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cptnewqv1300_epsx12, 5))` | TOP200 | 0.57 | 0.25 | 14.0% | 60% | all-weather |
| `rank(fnd6_cptnewqv1300_epsx12 / close)` | TOP3000 | 0.15 | 0.07 | 37.2% | 40% | bull-only |
| `rank(fnd6_cptnewqv1300_epsx12)` | TOP3000 | 0.11 | 0.04 | 43.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_epsf12: 0.948 (strongly positively correlated)
- fnd6_newqv1300_ibadj12: 0.490 (moderately positively correlated)
- fnd6_newqv1300_reunaq: 0.400 (weakly positively correlated)
- fnd6_newa2v1300_ni: 0.267 (weakly positively correlated)
- fnd6_newa1v1300_ib: 0.263 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
