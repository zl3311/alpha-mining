---
field: fn_payments_to_acquire_businesses_net_of_cash_acquired_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.44
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2851
ann_vol: 0.161
hit_rate: 0.5093
rolling_sharpe_min: -1.41
rolling_sharpe_max: 2.081
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: 0.05
---
# fn_payments_to_acquire_businesses_net_of_cash_acquired_q (fundamental2)

*The cash outflow associated with the acquisition of a business, net of the cash acquired from the purchase.*

## Signal Profile
- `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_q)`: S=0.09, F=0.01, T=2.5%, INFERIOR (TOP1000)
- `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_q / close)`: S=0.17, F=0.04, T=2.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 5))`: S=0.40, F=0.17, T=34.2%, INFERIOR (TOP200)
- `-rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_q)`: S=-0.09, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 5))`: S=0.49, F=0.19, T=35.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 22)`: S=0.44, F=0.21, T=31.6%, INFERIOR (TOP3000)
- `ts_mean(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 10)`: S=-0.25, F=-0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 22))`: S=-0.61, F=-0.29, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_q)`: S=-0.09, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_q / close)`: S=-0.17, F=-0.04, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.69 (negative), ret=-7.1%
  - 2020: S=0.08 (weak), ret=+1.5%
  - 2021: S=0.82 (moderate), ret=+15.4%
  - 2022: S=0.43 (weak), ret=+7.1%
  - 2023: S=1.01 (moderate), ret=+14.5%

## Risk & Drawdown
- Max drawdown: 28.51% over 586 days (recovered)
- Annualized: return +6.4%, volatility 16.1% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.23, excess kurtosis +6.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 2.08, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +12.99%; worst month: -11.19%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.69
- Sideways: S=0.41
- Bear: S=0.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 5))` S=0.49, F=0.19, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_q)`: S=-0.09, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_q / close)`: S=-0.17, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 5))`: S=0.49, F=0.19, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_q, 5))` | TOP200 | 0.40 | 0.17 | 28.5% | 80% | mixed |
| `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_q / close)` | TOP1000 | 0.17 | 0.04 | 8.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prchq: -0.168 (weakly negatively correlated)
- fnd6_prch: -0.161 (weakly negatively correlated)
- fnd2_propplteqmuflmblgland: -0.151 (weakly negatively correlated)
- dividend_max_guidance_value: -0.149 (weakly negatively correlated)
- max_stock_option_expense_guidance: -0.148 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
