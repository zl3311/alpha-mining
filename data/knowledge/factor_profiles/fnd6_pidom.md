---
field: fnd6_pidom
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.68
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.6239
ann_vol: 0.2079
hit_rate: 0.4672
rolling_sharpe_min: -2.077
rolling_sharpe_max: 2.34
negated_best_sharpe: 0.68
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: 0.26
---
# fnd6_pidom (fundamental6)

*Pretax Income - Domestic*

## Signal Profile
- `rank(fnd6_pidom)`: S=-0.09, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_pidom / close)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_pidom, 5))`: S=0.42, F=0.25, T=24.8%, INFERIOR (TOP200)
- `-rank(fnd6_pidom)`: S=0.23, F=0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pidom, 5))`: S=-0.28, F=-0.14, T=24.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_pidom, 22)`: S=-0.37, F=-0.26, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pidom, 10)`: S=0.00, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pidom, 22))`: S=-0.54, F=-0.32, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pidom)`: S=0.68, F=0.58, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pidom / close)`: S=0.68, F=0.58, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+14.1%
  - 2020: S=-0.40 (negative), ret=-7.4%
  - 2021: S=-0.04 (negative), ret=-1.2%
  - 2022: S=1.47 (moderate), ret=+36.1%
  - 2023: S=0.10 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 62.39% over 912 days (recovered)
- Annualized: return +8.8%, volatility 20.8% (fraction of booksize)
- Hit rate: 46.7% positive days
- Tail shape: skew -0.73, excess kurtosis +24.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.08, max 2.34, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +21.53%; worst month: -20.53%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.04
- Sideways: S=0.84
- Bear: S=0.61

## Negated Direction
Best negated: `rank(-1 * fnd6_pidom / close)` S=0.68, F=0.58, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_pidom)`: S=0.68, F=0.58, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pidom / close)`: S=0.68, F=0.58, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pidom, 5))`: S=-0.28, F=-0.14, T=24.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_pidom, 5))` | TOP200 | 0.42 | 0.25 | 62.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cibegni: 0.557 (moderately positively correlated)
- fnd6_citotal: 0.539 (moderately positively correlated)
- fnd6_newa1v1300_ibc: 0.337 (weakly positively correlated)
- fnd6_newa2v1300_ni: 0.300 (weakly positively correlated)
- fnd6_newa1v1300_ib: 0.300 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
