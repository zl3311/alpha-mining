---
field: fn_business_combination_assets_aquired_goodwill_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.53
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.377
ann_vol: 0.1779
hit_rate: 0.4729
rolling_sharpe_min: -1.585
rolling_sharpe_max: 2.491
negated_best_sharpe: 0.59
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: 0.06
---
# fn_business_combination_assets_aquired_goodwill_a (fundamental2)

*Business Combination, Portion of Purchase Price Allocated to Goodwill*

## Signal Profile
- `rank(fn_business_combination_assets_aquired_goodwill_a)`: S=-0.21, F=-0.06, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_business_combination_assets_aquired_goodwill_a / close)`: S=0.08, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))`: S=0.35, F=0.21, T=16.4%, INFERIOR (TOP200)
- `-rank(fn_business_combination_assets_aquired_goodwill_a)`: S=0.33, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))`: S=-0.05, F=-0.01, T=16.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_business_combination_assets_aquired_goodwill_a, 63)`: S=0.53, F=0.56, T=9.1%, INFERIOR (TOP3000)
- `ts_mean(fn_business_combination_assets_aquired_goodwill_a, 10)`: S=-0.38, F=-0.15, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_business_combination_assets_aquired_goodwill_a, 22))`: S=0.02, F=0.00, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_a)`: S=0.50, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_a / close)`: S=0.59, F=0.36, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.34, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.60 (strong), ret=+17.6%
  - 2020: S=-0.09 (negative), ret=-1.3%
  - 2021: S=2.00 (strong), ret=+37.0%
  - 2022: S=-0.85 (negative), ret=-17.1%
  - 2023: S=-0.29 (negative), ret=-6.3%

## Risk & Drawdown
- Max drawdown: 37.70% over 701 days (not yet recovered, ongoing at window end)
- Annualized: return +6.1%, volatility 17.8% (fraction of booksize)
- Hit rate: 47.3% positive days
- Tail shape: skew -1.11, excess kurtosis +26.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 2.49, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +13.14%; worst month: -12.07%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.90
- Sideways: S=0.28
- Bear: S=-0.31

## Negated Direction
Best negated: `rank(-1 * fn_business_combination_assets_aquired_goodwill_a / close)` S=0.59, F=0.36, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_a)`: S=0.50, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_assets_aquired_goodwill_a / close)`: S=0.59, F=0.36, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))`: S=-0.05, F=-0.01, T=16.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))` | TOP200 | 0.34 | 0.21 | 37.7% | 40% | mixed |
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))` | TOP1000 | 0.26 | 0.11 | 20.6% | 80% | weak |
| `rank(ts_delta(fn_business_combination_assets_aquired_goodwill_a, 5))` | TOP500 | 0.19 | 0.08 | 26.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.224 (weakly positively correlated)
- historical_volatility_180: -0.222 (weakly negatively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: -0.221 (weakly negatively correlated)
- historical_volatility_150: -0.220 (weakly negatively correlated)
- parkinson_volatility_180: -0.220 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
