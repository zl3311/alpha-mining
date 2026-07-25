---
field: fn_business_combination_purchase_price_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.49
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.3038
ann_vol: 0.1534
hit_rate: 0.5134
rolling_sharpe_min: -1.527
rolling_sharpe_max: 1.718
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.12
---
# fn_business_combination_purchase_price_q (fundamental2)

*Business Combination, Purchase Price*

## Signal Profile
- `rank(fn_business_combination_purchase_price_q)`: S=0.20, F=0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_business_combination_purchase_price_q / close)`: S=0.23, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_business_combination_purchase_price_q, 5))`: S=0.37, F=0.15, T=35.7%, INFERIOR (TOP3000)
- `-rank(fn_business_combination_purchase_price_q)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_purchase_price_q, 5))`: S=0.49, F=0.24, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_business_combination_purchase_price_q, 63)`: S=0.02, F=0.00, T=15.4%, INFERIOR (TOP3000)
- `ts_mean(fn_business_combination_purchase_price_q, 10)`: S=0.05, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_business_combination_purchase_price_q, 22))`: S=-0.31, F=-0.13, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_q)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_q / close)`: S=0.04, F=0.00, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.34, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.54 (negative), ret=-7.5%
  - 2020: S=0.82 (moderate), ret=+15.3%
  - 2021: S=-0.30 (negative), ret=-4.7%
  - 2022: S=0.41 (weak), ret=+5.7%
  - 2023: S=1.43 (moderate), ret=+16.8%

## Risk & Drawdown
- Max drawdown: 30.38% over 713 days (recovered)
- Annualized: return +5.2%, volatility 15.3% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.74, excess kurtosis +7.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 1.72, latest 1.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +21.86%; worst month: -8.13%
Positive months: 51%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.39
- Sideways: S=0.55
- Bear: S=0.14

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_business_combination_purchase_price_q, 5))` S=0.49, F=0.24, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_business_combination_purchase_price_q)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_q / close)`: S=0.04, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_purchase_price_q, 5))`: S=0.49, F=0.24, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_business_combination_purchase_price_q, 5))` | TOP3000 | 0.34 | 0.15 | 30.4% | 60% | weak |
| `rank(fn_business_combination_purchase_price_q / close)` | TOP3000 | 0.21 | 0.06 | 11.1% | 60% | mixed |
| `rank(fn_business_combination_purchase_price_q)` | TOP3000 | 0.18 | 0.05 | 12.2% | 80% | bull-only |
| `rank(ts_delta(fn_business_combination_purchase_price_q, 5))` | TOP200 | 0.12 | 0.03 | 67.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xpp: 0.142 (weakly positively correlated)
- fn_payments_to_acquire_businesses_net_of_cash_acquired_q: 0.119 (weakly positively correlated)
- fnd6_ivaco: 0.104 (weakly positively correlated)
- fnd6_newqv1300_acomincq: 0.104 (weakly positively correlated)
- adv20: -0.094 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
