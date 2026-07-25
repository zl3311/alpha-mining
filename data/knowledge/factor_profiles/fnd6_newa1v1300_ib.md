---
field: fnd6_newa1v1300_ib
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.42
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.3804
ann_vol: 0.1937
hit_rate: 0.4988
rolling_sharpe_min: -1.573
rolling_sharpe_max: 2.201
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_newa1v1300_ib (fundamental6)

*Income Before Extraordinary Items*

## Signal Profile
- `rank(fnd6_newa1v1300_ib)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ib / close)`: S=0.12, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ib, 5))`: S=0.40, F=0.19, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ib)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ib, 5))`: S=-0.31, F=-0.13, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ib, 22)`: S=-0.26, F=-0.12, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ib, 10)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ib, 22))`: S=-0.36, F=-0.16, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ib)`: S=0.42, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ib / close)`: S=0.37, F=0.24, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.40, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+9.0%
  - 2020: S=-0.13 (negative), ret=-2.2%
  - 2021: S=-0.12 (negative), ret=-2.8%
  - 2022: S=1.54 (strong), ret=+35.6%
  - 2023: S=-0.15 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 38.04% over 758 days (recovered)
- Annualized: return +7.7%, volatility 19.4% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -0.56, excess kurtosis +8.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.20, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +22.81%; worst month: -10.39%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.13
- Sideways: S=0.87
- Bear: S=0.26

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ib)` S=0.42, F=0.30, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ib)`: S=0.42, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ib / close)`: S=0.37, F=0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ib, 5))`: S=-0.31, F=-0.13, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ib, 5))` | TOP200 | 0.40 | 0.19 | 38.0% | 40% | weak |
| `rank(fnd6_newa1v1300_ib / close)` | TOP3000 | 0.11 | 0.04 | 34.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_ni: 0.996 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.979 (strongly positively correlated)
- fnd6_newa1v1300_ibadj: 0.921 (strongly positively correlated)
- fnd6_ibmii: 0.918 (strongly positively correlated)
- fnd6_niadj: 0.918 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
