---
field: fnd6_cptnewqv1300_req
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.48
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1738
ann_vol: 0.1195
hit_rate: 0.5126
rolling_sharpe_min: -1.182
rolling_sharpe_max: 2.824
negated_best_sharpe: 0.48
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.18
---
# fnd6_cptnewqv1300_req (fundamental6)

*Retained Earnings*

## Signal Profile
- `rank(fnd6_cptnewqv1300_req)`: S=0.04, F=0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_req / close)`: S=0.18, F=0.07, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_req, 5))`: S=0.38, F=0.14, T=41.9%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_req)`: S=0.07, F=0.02, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_req, 5))`: S=-0.30, F=-0.10, T=41.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_req, 22)`: S=0.66, F=0.30, T=41.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_req, 10)`: S=-0.08, F=-0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_req, 22))`: S=0.44, F=0.18, T=18.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_req)`: S=0.42, F=0.27, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_req / close)`: S=0.48, F=0.34, T=5.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.06 (negative), ret=-9.3%
  - 2020: S=-0.02 (negative), ret=-0.2%
  - 2021: S=1.37 (moderate), ret=+17.8%
  - 2022: S=1.64 (strong), ret=+21.6%
  - 2023: S=-0.58 (negative), ret=-6.0%

## Risk & Drawdown
- Max drawdown: 17.38% over 817 days (recovered)
- Annualized: return +4.9%, volatility 11.9% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.59, excess kurtosis +6.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.18, max 2.82, latest -0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.13%; worst month: -9.18%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.11
- Sideways: S=-0.59
- Bear: S=-0.40

## Negated Direction
Best negated: `rank(-1 * fnd6_cptnewqv1300_req / close)` S=0.48, F=0.34, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_req)`: S=0.42, F=0.27, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_req / close)`: S=0.48, F=0.34, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_req, 5))`: S=-0.30, F=-0.10, T=41.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cptnewqv1300_req, 5))` | TOP200 | 0.39 | 0.14 | 27.4% | 40% | mixed |
| `rank(ts_delta(fnd6_cptnewqv1300_req, 5))` | TOP500 | 0.41 | 0.14 | 17.4% | 40% | mixed |
| `rank(fnd6_cptnewqv1300_req / close)` | TOP3000 | 0.17 | 0.07 | 37.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_req, 5))` | TOP3000 | 0.28 | 0.06 | 24.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- retained_earnings: 1.000 (strongly positively correlated)
- fnd6_newqv1300_reunaq: 0.451 (moderately positively correlated)
- fnd6_cptnewqv1300_oiadpq: 0.411 (moderately positively correlated)
- operating_income: 0.411 (moderately positively correlated)
- est_eps: 0.407 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
