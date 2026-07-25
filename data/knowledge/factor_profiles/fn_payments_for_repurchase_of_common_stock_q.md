---
field: fn_payments_for_repurchase_of_common_stock_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.56
best_fitness: 0.29
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1791
ann_vol: 0.1728
hit_rate: 0.5117
rolling_sharpe_min: -1.35
rolling_sharpe_max: 2.499
negated_best_sharpe: 0.33
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.23
---
# fn_payments_for_repurchase_of_common_stock_q (fundamental2)

*Value reported on Cash Flow Statement. May include shares repurchased as part of a buyback plan, as well as shares purchased for employee compensation, etc.*

## Signal Profile
- `rank(fn_payments_for_repurchase_of_common_stock_q)`: S=0.10, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(fn_payments_for_repurchase_of_common_stock_q / close)`: S=0.11, F=0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))`: S=0.56, F=0.29, T=36.6%, INFERIOR (TOP200)
- `-rank(fn_payments_for_repurchase_of_common_stock_q)`: S=0.08, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))`: S=-0.36, F=-0.12, T=35.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_payments_for_repurchase_of_common_stock_q, 22)`: S=-0.30, F=-0.09, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(fn_payments_for_repurchase_of_common_stock_q, 10)`: S=-0.15, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_payments_for_repurchase_of_common_stock_q, 22))`: S=0.33, F=0.10, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_q)`: S=0.26, F=0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_q / close)`: S=0.33, F=0.13, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+1.8%
  - 2020: S=0.01 (weak), ret=+0.2%
  - 2021: S=1.10 (moderate), ret=+30.3%
  - 2022: S=1.03 (moderate), ret=+15.2%
  - 2023: S=0.07 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 17.91% over 659 days (recovered)
- Annualized: return +9.8%, volatility 17.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.34, excess kurtosis +41.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.35, max 2.50, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +15.27%; worst month: -8.27%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.63
- Sideways: S=0.13
- Bear: S=0.96

## Negated Direction
Best negated: `rank(-1 * fn_payments_for_repurchase_of_common_stock_q / close)` S=0.33, F=0.13, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_q)`: S=0.26, F=0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_q / close)`: S=0.33, F=0.13, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))`: S=-0.36, F=-0.12, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))` | TOP200 | 0.57 | 0.29 | 17.9% | 100% | all-weather |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))` | TOP1000 | 0.51 | 0.15 | 12.5% | 60% | all-weather |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))` | TOP500 | 0.38 | 0.12 | 12.6% | 60% | weak |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_q, 5))` | TOP3000 | 0.27 | 0.04 | 12.4% | 40% | all-weather |
| `rank(fn_payments_for_repurchase_of_common_stock_q / close)` | TOP3000 | 0.10 | 0.02 | 12.4% | 60% | bull-only |
| `rank(fn_payments_for_repurchase_of_common_stock_q)` | TOP3000 | 0.10 | 0.02 | 16.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_unrgtxbnfinregfprtxps: -0.118 (weakly negatively correlated)
- fnd6_newqv1300_txwq: -0.114 (weakly negatively correlated)
- fn_avg_diluted_sharesout_adj_a: -0.106 (weakly negatively correlated)
- earnings_per_share_median_value: -0.103 (weakly negatively correlated)
- fn_accum_oth_income_loss_fx_adj_net_of_tax_a: 0.103 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
