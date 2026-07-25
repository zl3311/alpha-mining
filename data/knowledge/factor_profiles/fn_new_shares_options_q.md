---
field: fn_new_shares_options_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.34
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.2446
ann_vol: 0.1278
hit_rate: 0.5069
rolling_sharpe_min: -1.319
rolling_sharpe_max: 2.297
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.05
---
# fn_new_shares_options_q (fundamental2)

*Number of share options (or share units) exercised during the current period.*

## Signal Profile
- `rank(fn_new_shares_options_q)`: S=-0.04, F=-0.01, T=2.8%, INFERIOR (TOP200)
- `rank(fn_new_shares_options_q / close)`: S=0.17, F=0.06, T=2.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_new_shares_options_q, 5))`: S=0.29, F=0.09, T=37.0%, INFERIOR (TOP3000)
- `-rank(fn_new_shares_options_q)`: S=0.08, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_options_q, 5))`: S=0.34, F=0.18, T=35.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_new_shares_options_q, 63)`: S=-0.06, F=-0.01, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fn_new_shares_options_q, 10)`: S=0.07, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_new_shares_options_q, 22))`: S=-0.43, F=-0.22, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_q)`: S=0.25, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_q / close)`: S=-0.03, F=-0.01, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+4.8%
  - 2020: S=1.35 (moderate), ret=+16.6%
  - 2021: S=-0.64 (negative), ret=-8.8%
  - 2022: S=-0.38 (negative), ret=-5.1%
  - 2023: S=0.79 (moderate), ret=+9.9%

## Risk & Drawdown
- Max drawdown: 24.46% over 1164 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 12.8% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.04, excess kurtosis +2.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.32, max 2.30, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +8.24%; worst month: -10.02%
Positive months: 51%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.16
- Sideways: S=0.57
- Bear: S=0.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_new_shares_options_q, 5))` S=0.34, F=0.18, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_new_shares_options_q)`: S=0.25, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_q / close)`: S=-0.03, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_options_q, 5))`: S=0.34, F=0.18, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_new_shares_options_q, 5))` | TOP3000 | 0.28 | 0.09 | 24.5% | 60% | weak |
| `rank(fn_new_shares_options_q / close)` | TOP1000 | 0.18 | 0.06 | 22.8% | 80% | bear-only |

## Correlation Notes
Top correlates:
- beta_last_360_days_spy: -0.124 (weakly negatively correlated)
- anl4_dts_ptp: 0.118 (weakly positively correlated)
- lowest_sales_estimate: 0.117 (weakly positively correlated)
- sales_estimate_average_annual: 0.115 (weakly positively correlated)
- fn_comp_options_out_weighted_avg_q: 0.115 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
