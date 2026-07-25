---
field: anl4_ebitda_number
dataset: analyst4
best_template: rank_level
best_sharpe: 1.02
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0318
ann_vol: 0.0256
hit_rate: 0.5296
rolling_sharpe_min: -0.363
rolling_sharpe_max: 2.154
top_merge_partner: rank(scl12_sentiment * (-1 * returns))
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.64
---
# anl4_ebitda_number (analyst4)

*Earnings before interest, taxes, depreciation and amortization - number of estimations*

## Signal Profile
- `rank(anl4_ebitda_number)`: S=1.02, F=0.47, T=2.9%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_number / close)`: S=0.07, F=0.02, T=3.4%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_ebitda_number, 5))`: S=0.32, F=0.08, T=36.7%, INFERIOR (TOP1000)
- `-rank(anl4_ebitda_number)`: S=-0.41, F=-0.14, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_number, 5))`: S=0.06, F=0.01, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebitda_number, 22)`: S=-0.03, F=0.00, T=36.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_number, 10)`: S=0.53, F=0.23, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_number, 22))`: S=0.42, F=0.16, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_number)`: S=0.38, F=0.19, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_number / close)`: S=0.07, F=0.02, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.04, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+3.0%
  - 2020: S=0.63 (moderate), ret=+1.6%
  - 2021: S=1.99 (strong), ret=+5.7%
  - 2022: S=0.08 (weak), ret=+0.2%
  - 2023: S=1.25 (moderate), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 3.18% over 301 days (recovered)
- Annualized: return +2.7%, volatility 2.6% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.15, excess kurtosis +0.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.36, max 2.15, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +2.57%; worst month: -1.97%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.96
- Sideways: S=1.04
- Bear: S=1.14

## Negated Direction
Best negated: `rank(-1 * anl4_ebitda_number)` S=0.38, F=0.19, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ebitda_number)`: S=0.38, F=0.19, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_number / close)`: S=0.07, F=0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_number, 5))`: S=0.06, F=0.01, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_number)` | TOP3000 | 1.04 | 0.47 | 3.2% | 100% | all-weather |
| `rank(anl4_ebitda_number)` | TOP1000 | 0.42 | 0.14 | 6.9% | 60% | mixed |
| `rank(ts_delta(anl4_ebitda_number, 5))` | TOP1000 | 0.33 | 0.08 | 12.5% | 40% | mixed |
| `rank(ts_delta(anl4_ebitda_number, 5))` | TOP3000 | 0.33 | 0.07 | 6.8% | 80% | all-weather |
| `rank(ts_delta(anl4_ebitda_number, 5))` | TOP500 | 0.17 | 0.04 | 20.0% | 60% | all-weather |
| `rank(anl4_ebitda_number / close)` | TOP500 | 0.07 | 0.02 | 24.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- sales_estimate_count_quarterly: 0.566 (moderately positively correlated)
- anl4_ebit_number: 0.511 (moderately positively correlated)
- anl4_netprofit_number: 0.510 (moderately positively correlated)
- anl4_qfd1_az_eps_number: 0.508 (moderately positively correlated)
- anl4_qf_az_eps_number: 0.508 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.10 | 1.61 | +0.47 | -0.32 | yes |
| fn_repayments_of_debt_q | fundamental2 | -0.15 | 1.54 | +0.50 | +0.45 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.10 | 1.56 | +0.47 | +0.78 | yes |
| fnd6_rank | fundamental6 | -0.07 | 1.61 | +0.45 | +0.44 | yes |
| fnd6_ivaco | fundamental_investment | -0.10 | 1.80 | +0.45 | -0.05 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
