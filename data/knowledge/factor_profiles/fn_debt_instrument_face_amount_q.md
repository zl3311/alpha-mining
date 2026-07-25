---
field: fn_debt_instrument_face_amount_q
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.54
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0817
ann_vol: 0.0617
hit_rate: 0.4923
rolling_sharpe_min: -1.564
rolling_sharpe_max: 2.131
negated_best_sharpe: 0.49
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.05
---
# fn_debt_instrument_face_amount_q (fundamental2)

*Debt face amount*

## Signal Profile
- `rank(fn_debt_instrument_face_amount_q)`: S=0.13, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_face_amount_q / close)`: S=0.50, F=0.25, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_debt_instrument_face_amount_q, 5))`: S=0.10, F=0.03, T=24.4%, INFERIOR (TOP3000)
- `-rank(fn_debt_instrument_face_amount_q)`: S=0.03, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_face_amount_q, 5))`: S=0.16, F=0.05, T=20.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_instrument_face_amount_q, 63)`: S=0.22, F=0.10, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_instrument_face_amount_q, 10)`: S=0.54, F=0.30, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_face_amount_q, 22))`: S=-0.21, F=-0.09, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_q)`: S=0.49, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_q / close)`: S=0.26, F=0.11, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.49, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.7%
  - 2020: S=0.91 (moderate), ret=+8.0%
  - 2021: S=0.69 (moderate), ret=+4.3%
  - 2022: S=1.39 (moderate), ret=+6.7%
  - 2023: S=-0.76 (negative), ret=-3.5%

## Risk & Drawdown
- Max drawdown: 8.17% over 491 days (recovered)
- Annualized: return +3.0%, volatility 6.2% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.66, excess kurtosis +3.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 2.13, latest -0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.30%; worst month: -3.99%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.08
- Sideways: S=-0.07
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * fn_debt_instrument_face_amount_q)` S=0.49, F=0.29, INFERIOR
Direction gap: -0.05 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_face_amount_q)`: S=0.49, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_q / close)`: S=0.26, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_face_amount_q, 5))`: S=0.16, F=0.05, T=20.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_face_amount_q / close)` | TOP1000 | 0.49 | 0.25 | 8.2% | 60% | mixed |
| `rank(fn_debt_instrument_face_amount_q / close)` | TOP3000 | 0.44 | 0.21 | 10.7% | 60% | mixed |
| `rank(fn_debt_instrument_face_amount_q / close)` | TOP500 | 0.18 | 0.05 | 10.4% | 80% | mixed |
| `rank(ts_delta(fn_debt_instrument_face_amount_q, 5))` | TOP3000 | 0.09 | 0.03 | 57.7% | 40% | bull-only |
| `rank(fn_debt_instrument_face_amount_q)` | TOP3000 | 0.12 | 0.03 | 21.2% | 60% | bull-only |
| `rank(ts_delta(fn_debt_instrument_face_amount_q, 5))` | TOP200 | 0.08 | 0.02 | 35.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_debt_instrument_face_amount_a: 0.805 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.791 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.780 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.771 (strongly positively correlated)
- fn_interest_paid_net_a: 0.769 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
