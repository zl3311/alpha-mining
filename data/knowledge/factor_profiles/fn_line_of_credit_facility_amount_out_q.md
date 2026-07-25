---
field: fn_line_of_credit_facility_amount_out_q
dataset: fundamental2
best_template: rank_level
best_sharpe: 1.15
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0242
ann_vol: 0.027
hit_rate: 0.5126
rolling_sharpe_min: -0.435
rolling_sharpe_max: 3.645
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.65
---
# fn_line_of_credit_facility_amount_out_q (fundamental2)

*Amount borrowed under the credit facility as of the balance sheet date.*

## Signal Profile
- `rank(fn_line_of_credit_facility_amount_out_q)`: S=1.15, F=0.57, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_line_of_credit_facility_amount_out_q / close)`: S=0.89, F=0.50, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_line_of_credit_facility_amount_out_q, 5))`: S=0.15, F=0.03, T=37.0%, INFERIOR (TOP3000)
- `-rank(fn_line_of_credit_facility_amount_out_q)`: S=-0.37, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_amount_out_q, 5))`: S=0.50, F=0.21, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_line_of_credit_facility_amount_out_q, 63)`: S=-0.31, F=-0.14, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fn_line_of_credit_facility_amount_out_q, 10)`: S=0.34, F=0.42, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_line_of_credit_facility_amount_out_q, 22))`: S=0.45, F=0.22, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_q)`: S=-0.37, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_q / close)`: S=-0.41, F=-0.16, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.13, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+1.1%
  - 2020: S=0.58 (moderate), ret=+2.2%
  - 2021: S=3.20 (strong), ret=+7.5%
  - 2022: S=1.10 (moderate), ret=+2.7%
  - 2023: S=0.69 (moderate), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 2.42% over 212 days (recovered)
- Annualized: return +3.0%, volatility 2.7% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.62, excess kurtosis +3.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.43, max 3.65, latest 0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +1.73%; worst month: -0.93%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.97
- Sideways: S=1.29
- Bear: S=0.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_line_of_credit_facility_amount_out_q, 5))` S=0.50, F=0.21, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_line_of_credit_facility_amount_out_q)`: S=-0.37, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_q / close)`: S=-0.41, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_amount_out_q, 5))`: S=0.50, F=0.21, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_line_of_credit_facility_amount_out_q)` | TOP3000 | 1.13 | 0.57 | 2.4% | 100% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_q / close)` | TOP3000 | 0.88 | 0.50 | 4.8% | 80% | all-weather |
| `rank(fn_line_of_credit_facility_amount_out_q / close)` | TOP1000 | 0.41 | 0.16 | 13.9% | 60% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_q)` | TOP1000 | 0.37 | 0.12 | 12.0% | 40% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_q / close)` | TOP500 | 0.15 | 0.03 | 13.8% | 40% | bear-only |
| `rank(ts_delta(fn_line_of_credit_facility_amount_out_q, 5))` | TOP3000 | 0.16 | 0.03 | 23.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.652 (moderately positively correlated)
- fn_interest_paid_net_q: 0.645 (moderately positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.642 (moderately positively correlated)
- fnd6_intpn: 0.639 (moderately positively correlated)
- fnd6_dlto: 0.632 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.12 | 1.71 | +0.55 | +0.43 | yes |
| anl4_netprofit_number | analyst4 | -0.06 | 1.69 | +0.50 | +0.39 | yes |
| anl4_totassets_number | analyst4 | -0.04 | 1.64 | +0.47 | -0.30 | yes |
| rp_nip_credit_ratings | news18 | -0.05 | 1.52 | +0.39 | -0.84 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | +0.04 | 1.57 | +0.42 | -0.49 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
