---
field: fn_assets_fair_val_q
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.53
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1589
ann_vol: 0.0496
hit_rate: 0.5174
rolling_sharpe_min: -2.014
rolling_sharpe_max: 2.662
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.05
---
# fn_assets_fair_val_q (fundamental2)

*Asset Fair Value, Recurring, Total*

## Signal Profile
- `rank(fn_assets_fair_val_q)`: S=0.53, F=0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_q / close)`: S=0.24, F=0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_q, 5))`: S=0.33, F=0.14, T=37.5%, INFERIOR (TOP500)
- `-rank(fn_assets_fair_val_q)`: S=-0.14, F=-0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_q, 5))`: S=0.48, F=0.20, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_assets_fair_val_q, 63)`: S=0.10, F=0.02, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_q, 10)`: S=0.08, F=0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_q, 22))`: S=-0.34, F=-0.16, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_q)`: S=-0.53, F=-0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_q / close)`: S=-0.24, F=-0.08, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/22P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+0.9%
  - 2020: S=-0.89 (negative), ret=-4.6%
  - 2021: S=0.70 (moderate), ret=+4.3%
  - 2022: S=1.08 (moderate), ret=+4.8%
  - 2023: S=1.66 (strong), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 15.89% over 930 days (recovered)
- Annualized: return +2.7%, volatility 5.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.13, excess kurtosis +0.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.01, max 2.66, latest 1.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +2.21%; worst month: -3.51%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.11
- Sideways: S=1.71
- Bear: S=-1.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_assets_fair_val_q, 5))` S=0.48, F=0.20, INFERIOR
Direction gap: -0.05 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_q)`: S=-0.53, F=-0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_q / close)`: S=-0.24, F=-0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_q, 5))`: S=0.48, F=0.20, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_assets_fair_val_q)` | TOP3000 | 0.54 | 0.24 | 15.9% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_q, 5))` | TOP500 | 0.32 | 0.14 | 31.2% | 60% | weak |
| `rank(ts_delta(fn_assets_fair_val_q, 5))` | TOP200 | 0.30 | 0.12 | 43.8% | 40% | mixed |
| `rank(fn_assets_fair_val_q / close)` | TOP3000 | 0.24 | 0.08 | 14.2% | 60% | bear-only |
| `rank(fn_assets_fair_val_q / close)` | TOP500 | 0.13 | 0.03 | 13.1% | 80% | mixed |
| `rank(fn_assets_fair_val_q)` | TOP1000 | 0.14 | 0.03 | 15.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_tfva: 0.776 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.756 (strongly positively correlated)
- cash: 0.721 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.692 (moderately positively correlated)
- working_capital: 0.692 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
