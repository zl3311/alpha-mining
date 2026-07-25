---
field: fn_business_combination_assets_aquired_goodwill_q
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.7
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3755
ann_vol: 0.1575
hit_rate: 0.4858
rolling_sharpe_min: -1.865
rolling_sharpe_max: 2.143
negated_best_sharpe: 0.7
negated_best_template: neg_rank_level
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: 0.2
---
# fn_business_combination_assets_aquired_goodwill_q (fundamental2)

*Business Combination, Portion of Purchase Price Allocated to Goodwill*

## Signal Profile
- `rank(fn_business_combination_assets_aquired_goodwill_q)`: S=0.08, F=0.01, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_business_combination_assets_aquired_goodwill_q / close)`: S=0.08, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))`: S=0.14, F=0.05, T=22.4%, INFERIOR (TOP200)
- `-rank(fn_business_combination_assets_aquired_goodwill_q)`: S=0.25, F=0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))`: S=-0.22, F=-0.09, T=22.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_business_combination_assets_aquired_goodwill_q, 22)`: S=-0.47, F=-0.34, T=15.1%, INFERIOR (TOP3000)
- `ts_mean(fn_business_combination_assets_aquired_goodwill_q, 10)`: S=-0.53, F=-0.29, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_business_combination_assets_aquired_goodwill_q, 22))`: S=0.50, F=0.31, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_q)`: S=0.70, F=0.56, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_q / close)`: S=0.64, F=0.47, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+4.8%
  - 2020: S=-0.05 (negative), ret=-1.1%
  - 2021: S=-1.20 (negative), ret=-16.6%
  - 2022: S=1.18 (moderate), ret=+18.2%
  - 2023: S=0.57 (moderate), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 37.55% over 1261 days (recovered)
- Annualized: return +2.7%, volatility 15.8% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew -0.70, excess kurtosis +11.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.86, max 2.14, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +9.63%; worst month: -13.25%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.12
- Sideways: S=0.41
- Bear: S=-0.89

## Negated Direction
Best negated: `rank(-1 * fn_business_combination_assets_aquired_goodwill_q)` S=0.70, F=0.56, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_q)`: S=0.70, F=0.56, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_q / close)`: S=0.64, F=0.47, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))`: S=-0.22, F=-0.09, T=22.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))` | TOP200 | 0.14 | 0.05 | 25.1% | 60% | bull-only |
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))` | TOP1000 | 0.17 | 0.05 | 37.5% | 60% | bull-only |
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_q, 5))` | TOP3000 | 0.08 | 0.02 | 36.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- news_mins_20_pct_up: -0.206 (weakly negatively correlated)
- news_mins_20_chg: -0.206 (weakly negatively correlated)
- split: 0.157 (weakly positively correlated)
- min_free_cash_flow_per_share_guidance: 0.157 (weakly positively correlated)
- free_cash_flow_per_share_max_guidance: 0.157 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
