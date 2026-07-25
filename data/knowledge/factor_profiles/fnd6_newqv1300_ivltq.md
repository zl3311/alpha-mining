---
field: fnd6_newqv1300_ivltq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.52
best_fitness: 0.22
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.3017
ann_vol: 0.1418
hit_rate: 0.5069
rolling_sharpe_min: -2.45
rolling_sharpe_max: 2.556
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.43
---
# fnd6_newqv1300_ivltq (fundamental6)

*Total Long-term Investments*

## Signal Profile
- `rank(fnd6_newqv1300_ivltq)`: S=0.27, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ivltq / close)`: S=0.34, F=0.17, T=3.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_ivltq, 5))`: S=0.52, F=0.22, T=40.5%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_ivltq)`: S=-0.23, F=-0.10, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ivltq, 5))`: S=0.09, F=0.01, T=39.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_ivltq, 63)`: S=0.53, F=0.20, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ivltq, 10)`: S=-0.21, F=-0.07, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ivltq, 22))`: S=0.16, F=0.04, T=18.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivltq)`: S=-0.27, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivltq / close)`: S=-0.33, F=-0.13, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.12 (negative), ret=-11.1%
  - 2020: S=0.68 (moderate), ret=+10.2%
  - 2021: S=1.00 (moderate), ret=+12.2%
  - 2022: S=0.23 (weak), ret=+3.8%
  - 2023: S=1.28 (moderate), ret=+19.4%

## Risk & Drawdown
- Max drawdown: 30.17% over 711 days (recovered)
- Annualized: return +7.0%, volatility 14.2% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.17, excess kurtosis +5.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.45, max 2.56, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +13.26%; worst month: -5.83%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.22
- Sideways: S=0.72
- Bear: S=0.61

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ivltq, 5))` S=0.09, F=0.01, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ivltq)`: S=-0.27, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivltq / close)`: S=-0.33, F=-0.13, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ivltq, 5))`: S=0.09, F=0.01, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_ivltq, 5))` | TOP500 | 0.50 | 0.22 | 30.2% | 80% | mixed |
| `rank(fnd6_newqv1300_ivltq / close)` | TOP1000 | 0.33 | 0.17 | 13.5% | 40% | bull-only |
| `rank(fnd6_newqv1300_ivltq / close)` | TOP3000 | 0.33 | 0.13 | 13.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_ivltq)` | TOP3000 | 0.27 | 0.11 | 22.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_ivltq)` | TOP1000 | 0.22 | 0.10 | 23.1% | 40% | bull-only |
| `rank(fnd6_newqv1300_ivltq / close)` | TOP500 | 0.20 | 0.09 | 21.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_ivltq, 5))` | TOP200 | 0.22 | 0.07 | 45.3% | 60% | weak |
| `rank(ts_delta(fnd6_newqv1300_ivltq, 5))` | TOP1000 | 0.19 | 0.04 | 22.5% | 80% | mixed |
| `rank(fnd6_newqv1300_ivltq)` | TOP500 | 0.08 | 0.03 | 30.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- retained_earnings: 0.154 (weakly positively correlated)
- fnd6_cptnewqv1300_req: 0.154 (weakly positively correlated)
- fnd6_newqv1300_rectaq: 0.125 (weakly positively correlated)
- pv13_ustomergraphrank_page_rank: 0.119 (weakly positively correlated)
- fnd6_txr: 0.115 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
