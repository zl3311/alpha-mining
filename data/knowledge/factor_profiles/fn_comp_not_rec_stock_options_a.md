---
field: fn_comp_not_rec_stock_options_a
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.86
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0743
ann_vol: 0.0491
hit_rate: 0.5231
rolling_sharpe_min: -0.604
rolling_sharpe_max: 2.439
negated_best_sharpe: -0.02
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.88
---
# fn_comp_not_rec_stock_options_a (fundamental2)

*Unrecognized cost of unvested stock option awards.*

## Signal Profile
- `rank(fn_comp_not_rec_stock_options_a)`: S=0.41, F=0.17, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_comp_not_rec_stock_options_a / close)`: S=0.58, F=0.28, T=1.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_comp_not_rec_stock_options_a, 5))`: S=-0.10, F=-0.02, T=34.4%, INFERIOR (TOP3000)
- `-rank(fn_comp_not_rec_stock_options_a)`: S=-0.21, F=-0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_stock_options_a, 5))`: S=-0.02, F=0.00, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_not_rec_stock_options_a, 63)`: S=0.51, F=0.36, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_not_rec_stock_options_a, 10)`: S=0.86, F=0.76, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_not_rec_stock_options_a, 22))`: S=0.12, F=0.03, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_stock_options_a)`: S=-0.10, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_stock_options_a / close)`: S=-0.22, F=-0.07, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.42 (strong), ret=+6.2%
  - 2020: S=1.20 (moderate), ret=+7.5%
  - 2021: S=-0.35 (negative), ret=-2.0%
  - 2022: S=-0.16 (negative), ret=-0.7%
  - 2023: S=0.68 (moderate), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 7.43% over 378 days (recovered)
- Annualized: return +2.8%, volatility 4.9% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.12, excess kurtosis +5.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.44, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +3.31%; worst month: -5.29%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.70
- Sideways: S=1.39
- Bear: S=-0.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_not_rec_stock_options_a, 5))` S=-0.02, F=0.00, INFERIOR
Direction gap: -0.88 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_not_rec_stock_options_a)`: S=-0.10, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_stock_options_a / close)`: S=-0.22, F=-0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_stock_options_a, 5))`: S=-0.02, F=0.00, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_not_rec_stock_options_a / close)` | TOP1000 | 0.57 | 0.28 | 7.4% | 60% | mixed |
| `rank(fn_comp_not_rec_stock_options_a / close)` | TOP3000 | 0.50 | 0.24 | 13.9% | 60% | mixed |
| `rank(fn_comp_not_rec_stock_options_a)` | TOP3000 | 0.41 | 0.17 | 16.9% | 60% | bull-only |
| `rank(fn_comp_not_rec_stock_options_a)` | TOP200 | 0.22 | 0.09 | 12.6% | 80% | bull-only |
| `rank(fn_comp_not_rec_stock_options_a / close)` | TOP200 | 0.21 | 0.08 | 10.4% | 100% | mixed |
| `rank(fn_comp_not_rec_stock_options_a / close)` | TOP500 | 0.21 | 0.07 | 10.5% | 80% | bull-only |
| `rank(fn_comp_not_rec_stock_options_a)` | TOP1000 | 0.20 | 0.06 | 17.8% | 60% | bull-only |
| `rank(fn_comp_not_rec_stock_options_a)` | TOP500 | 0.09 | 0.02 | 18.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_comp_not_rec_a: 0.647 (moderately positively correlated)
- fnd2_a_seniornotes: 0.627 (moderately positively correlated)
- fnd2_q_seniornotes: 0.627 (moderately positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.611 (moderately positively correlated)
- fn_op_lease_min_pay_due_a: 0.609 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
