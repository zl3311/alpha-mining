---
field: fnd6_newqv1300_txwq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.58
best_fitness: 0.95
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2432
ann_vol: 0.1633
hit_rate: 0.4964
rolling_sharpe_min: -0.2
rolling_sharpe_max: 2.912
top_merge_partner: multi_factor_static_score_derivative
negated_best_sharpe: 0.58
negated_best_template: neg_rank_level
negated_best_fitness: 0.95
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newqv1300_txwq (fundamental6)

*Excise Taxes*

## Signal Profile
- `rank(fnd6_newqv1300_txwq)`: S=-0.21, F=-0.17, T=11.2%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_txwq / close)`: S=-0.19, F=-0.18, T=3.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_txwq, 5))`: S=0.81, F=0.78, T=14.2%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_txwq)`: S=0.20, F=0.20, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txwq, 5))`: S=0.54, F=0.47, T=18.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_txwq, 63)`: S=0.12, F=0.06, T=12.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txwq, 10)`: S=0.49, F=0.40, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txwq, 22))`: S=-0.11, F=-0.05, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txwq)`: S=0.58, F=0.95, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txwq / close)`: S=0.58, F=0.95, T=9.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+17.9%
  - 2020: S=0.28 (weak), ret=+3.4%
  - 2021: S=0.39 (weak), ret=+9.4%
  - 2022: S=2.46 (strong), ret=+31.3%
  - 2023: S=0.43 (weak), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 24.32% over 324 days (recovered)
- Annualized: return +13.3%, volatility 16.3% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.55, excess kurtosis +17.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.20, max 2.91, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +18.69%; worst month: -9.50%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.50
- Sideways: S=0.86
- Bear: S=-0.13

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_txwq)` S=0.58, F=0.95, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txwq)`: S=0.58, F=0.95, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txwq / close)`: S=0.58, F=0.95, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txwq, 5))`: S=0.54, F=0.47, T=18.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_txwq, 5))` | TOP200 | 0.81 | 0.78 | 24.3% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_txwq, 5))` | TOP3000 | 0.15 | 0.05 | 56.4% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.453 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.419 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.419 (moderately positively correlated)
- min_investing_cashflow_guidance_2: 0.411 (moderately positively correlated)
- max_investing_cashflow_guidance_2: 0.411 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.21 | 1.31 | +0.47 | -0.09 | yes |
| cashflow_efficiency_rank_derivative | model16 | -0.21 | 1.28 | +0.47 | -0.10 | yes |
| growth_potential_rank_derivative | model16 | -0.21 | 1.35 | +0.46 | -0.09 | yes |
| analyst_revision_rank_derivative | model16 | -0.21 | 1.39 | +0.46 | -0.08 | yes |
| relative_valuation_rank_derivative | model16 | -0.21 | 1.39 | +0.46 | -0.08 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
