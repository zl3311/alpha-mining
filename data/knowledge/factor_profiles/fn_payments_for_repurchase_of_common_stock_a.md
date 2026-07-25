---
field: fn_payments_for_repurchase_of_common_stock_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.4
best_fitness: 0.16
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 7
max_drawdown: 0.303
ann_vol: 0.1427
hit_rate: 0.4931
rolling_sharpe_min: -1.803
rolling_sharpe_max: 2.528
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.06
---
# fn_payments_for_repurchase_of_common_stock_a (fundamental2)

*Value reported on Cash Flow Statement. May include shares repurchased as part of a buyback plan, as well as shares purchased for employee compensation, etc.*

## Signal Profile
- `rank(fn_payments_for_repurchase_of_common_stock_a)`: S=0.09, F=0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_payments_for_repurchase_of_common_stock_a / close)`: S=0.32, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))`: S=0.40, F=0.16, T=33.6%, INFERIOR (TOP500)
- `-rank(fn_payments_for_repurchase_of_common_stock_a)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))`: S=-0.50, F=-0.23, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(fn_payments_for_repurchase_of_common_stock_a, 63)`: S=-0.29, F=-0.15, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(fn_payments_for_repurchase_of_common_stock_a, 10)`: S=-0.11, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_payments_for_repurchase_of_common_stock_a, 22))`: S=-0.01, F=0.00, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_a)`: S=0.34, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_a / close)`: S=0.21, F=0.07, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.79 (strong), ret=+19.8%
  - 2020: S=0.64 (moderate), ret=+7.4%
  - 2021: S=-0.28 (negative), ret=-4.5%
  - 2022: S=-1.07 (negative), ret=-17.4%
  - 2023: S=1.59 (strong), ret=+23.1%

## Risk & Drawdown
- Max drawdown: 30.30% over 1080 days (recovered)
- Annualized: return +5.8%, volatility 14.3% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.05, excess kurtosis +4.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.53, latest 1.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +11.27%; worst month: -7.25%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.19
- Sideways: S=0.84
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * fn_payments_for_repurchase_of_common_stock_a)` S=0.34, F=0.15, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_a)`: S=0.34, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_for_repurchase_of_common_stock_a / close)`: S=0.21, F=0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))`: S=-0.50, F=-0.23, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))` | TOP500 | 0.41 | 0.16 | 30.3% | 60% | weak |
| `rank(fn_payments_for_repurchase_of_common_stock_a / close)` | TOP3000 | 0.30 | 0.12 | 10.2% | 60% | bull-only |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))` | TOP1000 | 0.27 | 0.08 | 39.3% | 40% | mixed |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))` | TOP200 | 0.22 | 0.08 | 29.6% | 60% | mixed |
| `rank(fn_payments_for_repurchase_of_common_stock_a / close)` | TOP1000 | 0.18 | 0.06 | 17.6% | 60% | bull-only |
| `rank(ts_delta(fn_payments_for_repurchase_of_common_stock_a, 5))` | TOP3000 | 0.26 | 0.06 | 21.6% | 60% | weak |
| `rank(fn_payments_for_repurchase_of_common_stock_a)` | TOP3000 | 0.08 | 0.02 | 20.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_repurchased_shares_value_a: 0.706 (strongly positively correlated)
- fn_repurchased_shares_a: 0.307 (weakly positively correlated)
- fnd2_ebitdm: 0.177 (weakly positively correlated)
- fnd6_cidergl: 0.148 (weakly positively correlated)
- fnd2_a_flintasamt1expyfour: 0.137 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
