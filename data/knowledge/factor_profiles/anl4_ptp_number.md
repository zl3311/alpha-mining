---
field: anl4_ptp_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.94
best_fitness: 0.47
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0717
ann_vol: 0.0334
hit_rate: 0.5279
rolling_sharpe_min: -1.791
rolling_sharpe_max: 3.344
top_merge_partner: fn_repayments_of_debt_q
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.5
---
# anl4_ptp_number (analyst4)

*Pretax Income - number of estimations*

## Signal Profile
- `rank(anl4_ptp_number)`: S=0.94, F=0.47, T=4.0%, INFERIOR (TOP1000)
- `rank(anl4_ptp_number / close)`: S=0.34, F=0.16, T=3.5%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_ptp_number, 5))`: S=0.23, F=0.06, T=34.5%, INFERIOR (TOP200)
- `-rank(anl4_ptp_number)`: S=-0.94, F=-0.47, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_number, 5))`: S=0.44, F=0.12, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ptp_number, 63)`: S=0.18, F=0.04, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_number, 10)`: S=0.83, F=0.44, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptp_number, 22))`: S=-0.29, F=-0.09, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_number)`: S=-0.94, F=-0.47, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_number / close)`: S=-0.28, F=-0.13, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.4%
  - 2020: S=0.53 (moderate), ret=+1.6%
  - 2021: S=0.93 (moderate), ret=+3.6%
  - 2022: S=1.94 (strong), ret=+7.2%
  - 2023: S=1.23 (moderate), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 7.17% over 486 days (recovered)
- Annualized: return +3.2%, volatility 3.3% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.01, excess kurtosis +0.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.79, max 3.34, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +2.66%; worst month: -2.52%
Positive months: 70%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.31
- Sideways: S=0.72
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_number, 5))` S=0.44, F=0.12, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ptp_number)`: S=-0.94, F=-0.47, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_number / close)`: S=-0.28, F=-0.13, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_number, 5))`: S=0.44, F=0.12, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_number)` | TOP1000 | 0.96 | 0.47 | 7.2% | 80% | all-weather |
| `rank(anl4_ptp_number)` | TOP3000 | 0.88 | 0.38 | 5.1% | 80% | all-weather |
| `rank(anl4_ptp_number)` | TOP500 | 0.69 | 0.33 | 6.8% | 80% | all-weather |
| `rank(anl4_ptp_number / close)` | TOP500 | 0.35 | 0.16 | 22.5% | 80% | bear-only |
| `rank(anl4_ptp_number / close)` | TOP1000 | 0.28 | 0.13 | 24.2% | 40% | bear-only |
| `rank(anl4_ptp_number / close)` | TOP200 | 0.25 | 0.09 | 19.1% | 80% | mixed |
| `rank(ts_delta(anl4_ptp_number, 5))` | TOP200 | 0.24 | 0.06 | 24.7% | 60% | weak |
| `rank(anl4_ptp_number / close)` | TOP3000 | 0.10 | 0.03 | 41.9% | 40% | bear-only |
| `rank(ts_delta(anl4_ptp_number, 5))` | TOP3000 | 0.19 | 0.02 | 15.4% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_netprofit_number: 0.491 (moderately positively correlated)
- anl4_ebit_number: 0.477 (moderately positively correlated)
- sales_estimate_count_quarterly: 0.386 (weakly positively correlated)
- anl4_gric_number: 0.359 (weakly positively correlated)
- anl4_netprofita_number: 0.355 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_repayments_of_debt_q | fundamental2 | -0.04 | 1.44 | +0.41 | -0.65 | yes |
| rp_nip_credit_ratings | news18 | -0.04 | 1.37 | +0.41 | -0.17 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.13 | 1.39 | +0.42 | +0.33 | yes |
| fnd6_fopo | fundamental6 | -0.04 | 1.45 | +0.37 | -0.48 | yes |
| fn_derivative_notional_amount_q | fundamental2 | +0.02 | 1.39 | +0.36 | -0.53 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
