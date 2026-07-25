---
field: fn_derivative_notional_amount_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.04
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0593
ann_vol: 0.0451
hit_rate: 0.519
rolling_sharpe_min: -1.4
rolling_sharpe_max: 2.872
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 34
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.52
---
# fn_derivative_notional_amount_q (fundamental2)

*Nominal or face amount used to calculate payments on the derivative liability.*

## Signal Profile
- `rank(fn_derivative_notional_amount_q)`: S=0.27, F=0.08, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_derivative_notional_amount_q / close)`: S=1.04, F=0.64, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_notional_amount_q, 5))`: S=0.09, F=0.02, T=37.1%, INFERIOR (TOP500)
- `-rank(fn_derivative_notional_amount_q)`: S=-0.18, F=-0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_notional_amount_q, 5))`: S=0.64, F=0.33, T=38.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_derivative_notional_amount_q, 22)`: S=0.42, F=0.18, T=31.3%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_notional_amount_q, 10)`: S=-0.50, F=-0.32, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_notional_amount_q, 22))`: S=-0.49, F=-0.21, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_q)`: S=0.52, F=0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_q / close)`: S=0.34, F=0.18, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.03, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.98 (moderate), ret=+3.2%
  - 2020: S=1.74 (strong), ret=+11.2%
  - 2021: S=1.04 (moderate), ret=+3.6%
  - 2022: S=0.64 (moderate), ret=+2.5%
  - 2023: S=0.57 (moderate), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 5.93% over 583 days (not yet recovered, ongoing at window end)
- Annualized: return +4.7%, volatility 4.5% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.65, excess kurtosis +3.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 2.87, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +3.27%; worst month: -2.43%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.07
- Sideways: S=0.90
- Bear: S=0.22

## Negated Direction
Best negated: `rank(-1 * fn_derivative_notional_amount_q)` S=0.52, F=0.33, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_derivative_notional_amount_q)`: S=0.52, F=0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_q / close)`: S=0.34, F=0.18, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_notional_amount_q, 5))`: S=0.64, F=0.33, T=38.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_derivative_notional_amount_q / close)` | TOP3000 | 1.03 | 0.64 | 5.9% | 100% | mixed |
| `rank(fn_derivative_notional_amount_q / close)` | TOP1000 | 0.27 | 0.10 | 8.5% | 60% | bull-only |
| `rank(fn_derivative_notional_amount_q)` | TOP3000 | 0.26 | 0.08 | 10.1% | 80% | bull-only |
| `rank(fn_derivative_notional_amount_q)` | TOP1000 | 0.17 | 0.05 | 11.2% | 60% | bull-only |
| `rank(ts_delta(fn_derivative_notional_amount_q, 5))` | TOP500 | 0.09 | 0.02 | 26.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_derivative_notional_amount_a: 0.926 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.812 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.809 (strongly positively correlated)
- fn_interest_paid_net_a: 0.800 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.794 (strongly positively correlated)

Redundancy cluster #34: 4 similar fields, mean |rho| 0.713 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.75 | +0.58 | +0.11 | yes |
| anl4_capex_high | analyst4 | -0.20 | 1.53 | +0.50 | +0.09 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.15 | 1.66 | +0.50 | +0.45 | yes |
| est_rd_expense | analyst4 | -0.14 | 1.60 | +0.49 | +0.54 | yes |
| anl4_capex_flag | analyst4 | -0.03 | 1.52 | +0.43 | -0.55 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
