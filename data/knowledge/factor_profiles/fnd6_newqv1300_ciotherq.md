---
field: fnd6_newqv1300_ciotherq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.46
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.254
ann_vol: 0.1433
hit_rate: 0.5093
rolling_sharpe_min: -1.674
rolling_sharpe_max: 3.382
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.01
---
# fnd6_newqv1300_ciotherq (fundamental6)

*Comp Inc - Other Adj*

## Signal Profile
- `rank(fnd6_newqv1300_ciotherq)`: S=0.29, F=0.08, T=6.5%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ciotherq / close)`: S=0.29, F=0.08, T=6.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ciotherq, 5))`: S=0.46, F=0.18, T=45.4%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_ciotherq)`: S=-0.12, F=-0.02, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciotherq, 5))`: S=0.45, F=0.17, T=52.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_ciotherq, 63)`: S=0.06, F=0.01, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ciotherq, 10)`: S=0.01, F=0.00, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ciotherq, 22))`: S=-0.32, F=-0.13, T=21.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciotherq)`: S=-0.02, F=0.00, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciotherq / close)`: S=-0.04, F=-0.01, T=8.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.76 (strong), ret=+31.1%
  - 2020: S=0.79 (moderate), ret=+14.3%
  - 2021: S=0.32 (weak), ret=+4.5%
  - 2022: S=-0.04 (negative), ret=-0.5%
  - 2023: S=-1.39 (negative), ret=-16.6%

## Risk & Drawdown
- Max drawdown: 25.40% over 1037 days (not yet recovered, ongoing at window end)
- Annualized: return +6.7%, volatility 14.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.91, excess kurtosis +13.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.67, max 3.38, latest -1.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +19.09%; worst month: -7.22%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.95
- Sideways: S=0.98
- Bear: S=-0.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ciotherq, 5))` S=0.45, F=0.17, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ciotherq)`: S=-0.02, F=0.00, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciotherq / close)`: S=-0.04, F=-0.01, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciotherq, 5))`: S=0.45, F=0.17, T=52.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_ciotherq, 5))` | TOP3000 | 0.47 | 0.18 | 25.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_ciotherq, 5))` | TOP200 | 0.40 | 0.14 | 27.9% | 60% | mixed |
| `rank(fnd6_newqv1300_ciotherq / close)` | TOP3000 | 0.27 | 0.08 | 6.0% | 60% | all-weather |
| `rank(fnd6_newqv1300_ciotherq)` | TOP3000 | 0.27 | 0.08 | 5.9% | 60% | all-weather |
| `rank(fnd6_newqv1300_ciotherq / close)` | TOP200 | 0.14 | 0.04 | 19.6% | 40% | bear-only |
| `rank(fnd6_newqv1300_ciotherq)` | TOP200 | 0.10 | 0.02 | 20.0% | 40% | bear-only |
| `rank(fnd6_newqv1300_ciotherq)` | TOP1000 | 0.11 | 0.02 | 8.6% | 60% | weak |
| `rank(fnd6_newqv1300_ciotherq / close)` | TOP1000 | 0.11 | 0.02 | 8.8% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rcpq: 0.166 (weakly positively correlated)
- fnd6_cipen: -0.112 (weakly negatively correlated)
- fn_business_combination_assets_aquired_goodwill_q: -0.108 (weakly negatively correlated)
- news_mins_20_pct_up: 0.105 (weakly positively correlated)
- news_mins_20_chg: 0.105 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
