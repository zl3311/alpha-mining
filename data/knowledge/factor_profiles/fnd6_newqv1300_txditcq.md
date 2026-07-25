---
field: fnd6_newqv1300_txditcq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.46
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.3542
ann_vol: 0.1718
hit_rate: 0.4923
rolling_sharpe_min: -1.61
rolling_sharpe_max: 3.506
redundancy_cluster: 53
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newqv1300_txditcq (fundamental6)

*Deferred Taxes and Investment Tax Credit*

## Signal Profile
- `rank(fnd6_newqv1300_txditcq)`: S=0.48, F=0.30, T=2.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_txditcq / close)`: S=0.63, F=0.42, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_txditcq, 5))`: S=0.78, F=0.46, T=39.2%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_txditcq)`: S=-0.06, F=-0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txditcq, 5))`: S=0.55, F=0.17, T=38.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_txditcq, 63)`: S=0.13, F=0.02, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txditcq, 10)`: S=-0.06, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txditcq, 22))`: S=0.16, F=0.03, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txditcq)`: S=-0.48, F=-0.30, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txditcq / close)`: S=-0.63, F=-0.42, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.96 (negative), ret=-10.8%
  - 2020: S=-0.97 (negative), ret=-18.8%
  - 2021: S=1.61 (strong), ret=+29.1%
  - 2022: S=2.51 (strong), ret=+45.7%
  - 2023: S=1.24 (moderate), ret=+19.2%

## Risk & Drawdown
- Max drawdown: 35.42% over 951 days (recovered)
- Annualized: return +13.2%, volatility 17.2% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew -0.18, excess kurtosis +3.97

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 3.51, latest 1.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +13.43%; worst month: -15.66%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.43
- Sideways: S=-0.10
- Bear: S=1.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_txditcq, 5))` S=0.55, F=0.17, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txditcq)`: S=-0.48, F=-0.30, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txditcq / close)`: S=-0.63, F=-0.42, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txditcq, 5))`: S=0.55, F=0.17, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_txditcq, 5))` | TOP200 | 0.77 | 0.46 | 35.4% | 60% | all-weather |
| `rank(fnd6_newqv1300_txditcq / close)` | TOP3000 | 0.62 | 0.42 | 16.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_txditcq)` | TOP3000 | 0.47 | 0.30 | 26.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_txditcq / close)` | TOP500 | 0.21 | 0.10 | 32.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_txditcq / close)` | TOP1000 | 0.18 | 0.08 | 22.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_txditcq)` | TOP500 | 0.07 | 0.02 | 41.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_txdbq: 0.973 (strongly positively correlated)
- implied_volatility_mean_20: 0.118 (weakly positively correlated)
- implied_volatility_put_90: 0.118 (weakly positively correlated)
- implied_volatility_put_150: 0.114 (weakly positively correlated)
- implied_volatility_put_20: 0.114 (weakly positively correlated)

Redundancy cluster #53: 2 similar fields, mean |rho| 0.973 (representative: fnd6_newqv1300_txdbq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
