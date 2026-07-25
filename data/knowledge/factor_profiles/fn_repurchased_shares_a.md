---
field: fn_repurchased_shares_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.45
best_fitness: 0.19
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2834
ann_vol: 0.1294
hit_rate: 0.4931
rolling_sharpe_min: -1.59
rolling_sharpe_max: 2.313
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.25
---
# fn_repurchased_shares_a (fundamental2)

*Number of shares that have been repurchased during the period.*

## Signal Profile
- `rank(fn_repurchased_shares_a)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(fn_repurchased_shares_a / close)`: S=0.32, F=0.12, T=1.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_repurchased_shares_a, 5))`: S=0.45, F=0.19, T=33.8%, INFERIOR (TOP1000)
- `-rank(fn_repurchased_shares_a)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_a, 5))`: S=-0.43, F=-0.19, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_repurchased_shares_a, 22)`: S=-0.14, F=-0.05, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(fn_repurchased_shares_a, 10)`: S=-0.45, F=-0.38, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repurchased_shares_a, 22))`: S=0.34, F=0.15, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_a)`: S=0.20, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_a / close)`: S=0.06, F=0.01, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.05 (strong), ret=+24.9%
  - 2020: S=-0.89 (negative), ret=-12.0%
  - 2021: S=-0.48 (negative), ret=-5.9%
  - 2022: S=0.25 (weak), ret=+3.4%
  - 2023: S=1.57 (strong), ret=+18.6%

## Risk & Drawdown
- Max drawdown: 28.34% over 1359 days (not yet recovered, ongoing at window end)
- Annualized: return +5.9%, volatility 12.9% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.47, excess kurtosis +4.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.31, latest 1.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +12.01%; worst month: -9.03%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.90
- Sideways: S=1.43
- Bear: S=-1.11

## Negated Direction
Best negated: `rank(-1 * fn_repurchased_shares_a)` S=0.20, F=0.07, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repurchased_shares_a)`: S=0.20, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_a / close)`: S=0.06, F=0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_a, 5))`: S=-0.43, F=-0.19, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_repurchased_shares_a, 5))` | TOP1000 | 0.46 | 0.19 | 28.3% | 60% | bull-only |
| `rank(ts_delta(fn_repurchased_shares_a, 5))` | TOP500 | 0.42 | 0.18 | 31.6% | 60% | bull-only |
| `rank(fn_repurchased_shares_a / close)` | TOP1000 | 0.30 | 0.12 | 9.6% | 60% | bull-only |
| `rank(fn_repurchased_shares_a / close)` | TOP3000 | 0.19 | 0.05 | 7.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_payments_for_repurchase_of_common_stock_a: 0.307 (weakly positively correlated)
- fn_repurchased_shares_value_a: 0.272 (weakly positively correlated)
- fnd2_dfdfeditxexp: 0.134 (weakly positively correlated)
- fn_comp_options_exercisable_number_a: 0.134 (weakly positively correlated)
- fn_assets_fair_val_l3_a: 0.126 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
