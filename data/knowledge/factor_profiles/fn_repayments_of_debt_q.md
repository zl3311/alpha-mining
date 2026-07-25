---
field: fn_repayments_of_debt_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.04
best_fitness: 0.59
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0531
ann_vol: 0.0396
hit_rate: 0.5215
rolling_sharpe_min: -1.524
rolling_sharpe_max: 2.339
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.3
---
# fn_repayments_of_debt_q (fundamental2)

*The cash outflow during the period from the repayment of aggregate short-term and long-term debt. Excludes payment of capital lease obligations.*

## Signal Profile
- `rank(fn_repayments_of_debt_q)`: S=0.90, F=0.47, T=2.8%, INFERIOR (TOP1000)
- `rank(fn_repayments_of_debt_q / close)`: S=1.04, F=0.59, T=2.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_repayments_of_debt_q, 5))`: S=0.12, F=0.02, T=34.9%, INFERIOR (TOP500)
- `-rank(fn_repayments_of_debt_q)`: S=-0.90, F=-0.47, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_debt_q, 5))`: S=0.74, F=0.28, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(fn_repayments_of_debt_q, 22)`: S=0.63, F=0.28, T=34.7%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_debt_q, 10)`: S=-0.06, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_debt_q, 22))`: S=0.11, F=0.02, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_q)`: S=-0.77, F=-0.36, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_q / close)`: S=-0.96, F=-0.49, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.91 (strong), ret=+5.4%
  - 2020: S=1.16 (moderate), ret=+6.3%
  - 2021: S=1.82 (strong), ret=+6.9%
  - 2022: S=0.57 (moderate), ret=+2.1%
  - 2023: S=-0.28 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 5.31% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +4.1%, volatility 4.0% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.79, excess kurtosis +5.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 2.34, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +3.27%; worst month: -2.03%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.52
- Sideways: S=0.47
- Bear: S=0.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_repayments_of_debt_q, 5))` S=0.74, F=0.28, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repayments_of_debt_q)`: S=-0.77, F=-0.36, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_q / close)`: S=-0.96, F=-0.49, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_debt_q, 5))`: S=0.74, F=0.28, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_debt_q / close)` | TOP1000 | 1.03 | 0.59 | 5.3% | 80% | mixed |
| `rank(fn_repayments_of_debt_q / close)` | TOP3000 | 0.94 | 0.49 | 4.5% | 80% | mixed |
| `rank(fn_repayments_of_debt_q)` | TOP1000 | 0.90 | 0.47 | 5.2% | 80% | bull-only |
| `rank(fn_repayments_of_debt_q)` | TOP3000 | 0.76 | 0.36 | 4.2% | 60% | bull-only |
| `rank(fn_repayments_of_debt_q / close)` | TOP500 | 0.54 | 0.25 | 7.2% | 80% | bull-only |
| `rank(fn_repayments_of_debt_q)` | TOP500 | 0.29 | 0.10 | 10.4% | 60% | bull-only |
| `rank(ts_delta(fn_repayments_of_debt_q, 5))` | TOP500 | 0.10 | 0.02 | 29.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.674 (moderately positively correlated)
- fn_debt_instrument_face_amount_q: 0.660 (moderately positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.657 (moderately positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.656 (moderately positively correlated)
- fnd6_intpn: 0.656 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.25 | 1.78 | +0.62 | -0.16 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.69 | +0.51 | -0.64 | yes |
| anl4_capex_flag | analyst4 | -0.08 | 1.56 | +0.47 | -0.72 | yes |
| anl4_ebitda_number | analyst4 | -0.15 | 1.54 | +0.50 | +0.45 | yes |
| anl4_totassets_number | analyst4 | -0.10 | 1.64 | +0.46 | -0.30 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
