---
field: fn_line_of_credit_facility_amount_out_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.29
best_fitness: 1.25
best_universe: TOP500
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.3309
ann_vol: 0.2081
hit_rate: 0.4964
rolling_sharpe_min: -0.724
rolling_sharpe_max: 3.275
top_merge_partner: implied_volatility_put_10
negated_best_sharpe: 0.59
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: -0.7
---
# fn_line_of_credit_facility_amount_out_a (fundamental2)

*Amount borrowed under the credit facility as of the balance sheet date.*

## Signal Profile
- `rank(fn_line_of_credit_facility_amount_out_a)`: S=0.77, F=0.28, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_line_of_credit_facility_amount_out_a / close)`: S=0.63, F=0.27, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_line_of_credit_facility_amount_out_a, 5))`: S=1.29, F=1.25, T=28.6%, AVERAGE (TOP500)
- `-rank(fn_line_of_credit_facility_amount_out_a)`: S=-0.45, F=-0.15, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_amount_out_a, 5))`: S=-0.26, F=-0.14, T=19.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_line_of_credit_facility_amount_out_a, 22)`: S=0.37, F=0.27, T=14.0%, INFERIOR (TOP3000)
- `ts_mean(fn_line_of_credit_facility_amount_out_a, 10)`: S=0.04, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_line_of_credit_facility_amount_out_a, 22))`: S=0.56, F=0.38, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_a)`: S=0.59, F=0.36, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_a / close)`: S=0.59, F=0.38, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.29, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+10.2%
  - 2020: S=-0.05 (negative), ret=-1.2%
  - 2021: S=2.45 (strong), ret=+52.0%
  - 2022: S=1.81 (strong), ret=+47.2%
  - 2023: S=1.64 (strong), ret=+23.2%

## Risk & Drawdown
- Max drawdown: 33.09% over 441 days (recovered)
- Annualized: return +26.8%, volatility 20.8% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.86, excess kurtosis +8.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 3.27, latest 1.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +29.18%; worst month: -24.11%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.90
- Sideways: S=1.02
- Bear: S=0.88

## Negated Direction
Best negated: `rank(-1 * fn_line_of_credit_facility_amount_out_a / close)` S=0.59, F=0.38, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_line_of_credit_facility_amount_out_a)`: S=0.59, F=0.36, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_amount_out_a / close)`: S=0.59, F=0.38, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_amount_out_a, 5))`: S=-0.26, F=-0.14, T=19.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_line_of_credit_facility_amount_out_a, 5))` | TOP500 | 1.29 | 1.25 | 33.1% | 80% | all-weather |
| `rank(ts_delta(fn_line_of_credit_facility_amount_out_a, 5))` | TOP1000 | 0.58 | 0.32 | 57.1% | 80% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_a)` | TOP3000 | 0.76 | 0.28 | 2.5% | 100% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_a / close)` | TOP3000 | 0.63 | 0.27 | 6.8% | 80% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_a / close)` | TOP1000 | 0.49 | 0.21 | 10.2% | 60% | mixed |
| `rank(ts_delta(fn_line_of_credit_facility_amount_out_a, 5))` | TOP200 | 0.31 | 0.18 | 41.8% | 40% | mixed |
| `rank(fn_line_of_credit_facility_amount_out_a)` | TOP1000 | 0.45 | 0.15 | 8.5% | 40% | mixed |
| `rank(ts_delta(fn_line_of_credit_facility_amount_out_a, 5))` | TOP3000 | 0.28 | 0.10 | 30.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_ltrmdmrepoplinnext12m: 0.225 (weakly positively correlated)
- actual_dividend_value_quarterly: 0.188 (weakly positively correlated)
- anl4_af_cfps_value: 0.175 (weakly positively correlated)
- fnd6_ibmii: 0.172 (weakly positively correlated)
- fnd2_propplteqmuflmeqmt: 0.172 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_put_10 | option8 | -0.07 | 1.80 | +0.51 | -0.70 | yes |
| news_mins_4_pct_dn | news12 | +0.07 | 1.77 | +0.47 | -0.96 | yes |
| implied_volatility_mean_10 | option8 | -0.06 | 1.77 | +0.48 | -0.77 | yes |
| fnd6_nopio | fundamental6 | -0.01 | 1.82 | +0.54 | -0.11 | yes |
| anl4_ptp_flag | analyst_revision | -0.00 | 1.93 | +0.50 | -0.44 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
