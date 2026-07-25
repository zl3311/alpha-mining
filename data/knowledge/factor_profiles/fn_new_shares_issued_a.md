---
field: fn_new_shares_issued_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.52
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.7426
ann_vol: 0.21
hit_rate: 0.4874
rolling_sharpe_min: -1.889
rolling_sharpe_max: 3.081
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.05
---
# fn_new_shares_issued_a (fundamental2)

*Number of new stock issued during the period.*

## Signal Profile
- `rank(fn_new_shares_issued_a)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP1000)
- `rank(fn_new_shares_issued_a / close)`: S=0.14, F=0.04, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_new_shares_issued_a, 5))`: S=0.33, F=0.21, T=17.4%, INFERIOR (TOP200)
- `-rank(fn_new_shares_issued_a)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_issued_a, 5))`: S=0.57, F=0.41, T=25.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_new_shares_issued_a, 63)`: S=0.52, F=0.62, T=9.0%, INFERIOR (TOP3000)
- `ts_mean(fn_new_shares_issued_a, 10)`: S=-0.35, F=-0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_new_shares_issued_a, 22))`: S=-0.67, F=-0.75, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_issued_a)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_issued_a / close)`: S=-0.14, F=-0.04, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.32, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.47 (moderate), ret=+19.1%
  - 2020: S=-0.58 (negative), ret=-10.2%
  - 2021: S=-0.08 (negative), ret=-2.8%
  - 2022: S=1.40 (moderate), ret=+26.6%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 74.26% over 696 days (recovered)
- Annualized: return +6.7%, volatility 21.0% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew -2.69, excess kurtosis +42.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.08, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +13.78%; worst month: -27.69%
Positive months: 55%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.14
- Sideways: S=0.05
- Bear: S=-0.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_new_shares_issued_a, 5))` S=0.57, F=0.41, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_new_shares_issued_a)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_issued_a / close)`: S=-0.14, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_issued_a, 5))`: S=0.57, F=0.41, T=25.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_new_shares_issued_a, 5))` | TOP200 | 0.32 | 0.21 | 74.3% | 40% | mixed |
| `rank(ts_delta(fn_new_shares_issued_a, 5))` | TOP3000 | 0.24 | 0.10 | 76.2% | 80% | mixed |
| `rank(fn_new_shares_issued_a / close)` | TOP1000 | 0.14 | 0.04 | 20.0% | 60% | bear-only |
| `rank(ts_delta(fn_new_shares_issued_a, 5))` | TOP500 | 0.10 | 0.03 | 56.4% | 40% | mixed |
| `rank(fn_new_shares_issued_a / close)` | TOP500 | 0.11 | 0.03 | 20.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.262 (weakly positively correlated)
- min_stock_option_expense_guidance: 0.239 (weakly positively correlated)
- stock_option_expense_max_guidance_qtr: 0.239 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.237 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.237 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
