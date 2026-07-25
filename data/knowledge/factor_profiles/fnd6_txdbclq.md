---
field: fnd6_txdbclq
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.68
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.244
ann_vol: 0.1326
hit_rate: 0.4283
rolling_sharpe_min: -2.474
rolling_sharpe_max: 2.421
negated_best_sharpe: 0.68
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.76
n_negated_sims: 10
direction_gap: 0.28
---
# fnd6_txdbclq (fundamental6)

*Current Deferred Tax Liability*

## Signal Profile
- `rank(fnd6_txdbclq)`: S=-0.10, F=-0.03, T=7.4%, INFERIOR (TOP200)
- `rank(fnd6_txdbclq / close)`: S=-0.10, F=-0.03, T=7.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txdbclq, 5))`: S=0.40, F=0.26, T=12.9%, INFERIOR (TOP3000)
- `-rank(fnd6_txdbclq)`: S=0.41, F=0.36, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbclq, 5))`: S=0.30, F=0.15, T=10.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txdbclq, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_txdbclq, 10)`: S=-0.71, F=-1.03, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdbclq, 22))`: S=-0.20, F=-0.10, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbclq)`: S=0.68, F=0.76, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbclq / close)`: S=0.68, F=0.76, T=8.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.81 (negative), ret=-8.3%
  - 2020: S=-0.81 (negative), ret=-9.3%
  - 2021: S=0.72 (moderate), ret=+13.6%
  - 2022: S=1.37 (moderate), ret=+21.4%
  - 2023: S=0.82 (moderate), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 24.40% over 1163 days (recovered)
- Annualized: return +5.1%, volatility 13.3% (fraction of booksize)
- Hit rate: 42.8% positive days
- Tail shape: skew +1.33, excess kurtosis +25.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.47, max 2.42, latest 0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +17.64%; worst month: -6.44%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.68
- Sideways: S=-1.20
- Bear: S=-0.12

## Negated Direction
Best negated: `rank(-1 * fnd6_txdbclq / close)` S=0.68, F=0.76, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdbclq)`: S=0.68, F=0.76, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbclq / close)`: S=0.68, F=0.76, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbclq, 5))`: S=0.30, F=0.15, T=10.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdbclq, 5))` | TOP3000 | 0.39 | 0.26 | 24.4% | 60% | mixed |
| `rank(ts_delta(fnd6_txdbclq, 5))` | TOP500 | 0.35 | 0.18 | 19.0% | 60% | mixed |
| `rank(ts_delta(fnd6_txdbclq, 5))` | TOP200 | 0.07 | 0.02 | 35.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdbcl: 0.516 (moderately positively correlated)
- earnings_per_share_reported: 0.188 (weakly positively correlated)
- anl4_af_eps_value: 0.176 (weakly positively correlated)
- fnd6_newqv1300_oepf12: 0.176 (weakly positively correlated)
- fnd6_cptnewqv1300_oeps12: 0.176 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
