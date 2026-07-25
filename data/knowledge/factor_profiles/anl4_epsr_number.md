---
field: anl4_epsr_number
dataset: analyst4
best_template: rank_level
best_sharpe: 1.19
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0338
ann_vol: 0.0254
hit_rate: 0.5352
rolling_sharpe_min: -0.569
rolling_sharpe_max: 2.804
top_merge_partner: fnd6_rank
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.81
---
# anl4_epsr_number (analyst4)

*GAAP Earnings per share - number of estimations*

## Signal Profile
- `rank(anl4_epsr_number)`: S=1.19, F=0.58, T=2.8%, INFERIOR (TOP3000)
- `rank(anl4_epsr_number / close)`: S=0.16, F=0.06, T=2.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_epsr_number, 5))`: S=-0.02, F=0.00, T=33.7%, INFERIOR (TOP200)
- `-rank(anl4_epsr_number)`: S=-0.49, F=-0.18, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_number, 5))`: S=0.02, F=0.00, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_epsr_number, 63)`: S=0.13, F=0.02, T=19.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsr_number, 10)`: S=0.34, F=0.11, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_epsr_number, 22))`: S=0.06, F=0.01, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_number)`: S=0.38, F=0.17, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_number / close)`: S=-0.06, F=-0.01, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.19, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.86 (strong), ret=+3.7%
  - 2020: S=1.20 (moderate), ret=+3.1%
  - 2021: S=0.90 (moderate), ret=+2.4%
  - 2022: S=1.95 (strong), ret=+5.1%
  - 2023: S=0.20 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 3.38% over 336 days (recovered)
- Annualized: return +3.0%, volatility 2.5% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew +0.05, excess kurtosis +0.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.80, latest 0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +2.20%; worst month: -1.52%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.38
- Sideways: S=0.93
- Bear: S=1.24

## Negated Direction
Best negated: `rank(-1 * anl4_epsr_number)` S=0.38, F=0.17, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_epsr_number)`: S=0.38, F=0.17, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_number / close)`: S=-0.06, F=-0.01, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_number, 5))`: S=0.02, F=0.00, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsr_number)` | TOP3000 | 1.19 | 0.58 | 3.4% | 100% | all-weather |
| `rank(anl4_epsr_number)` | TOP500 | 0.65 | 0.31 | 6.6% | 100% | all-weather |
| `rank(anl4_epsr_number)` | TOP1000 | 0.50 | 0.18 | 4.8% | 80% | mixed |
| `rank(anl4_epsr_number / close)` | TOP1000 | 0.16 | 0.06 | 27.5% | 40% | bear-only |
| `rank(anl4_epsr_number / close)` | TOP500 | 0.17 | 0.05 | 24.8% | 60% | bear-only |
| `rank(anl4_epsr_number / close)` | TOP3000 | 0.10 | 0.03 | 43.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_eps_number: 0.643 (moderately positively correlated)
- anl4_qfd1_az_eps_number: 0.640 (moderately positively correlated)
- anl4_netprofit_number: 0.621 (moderately positively correlated)
- sales_estimate_count_quarterly: 0.603 (moderately positively correlated)
- anl4_ebit_number: 0.597 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.16 | 1.79 | +0.60 | -0.92 | yes |
| fn_repayments_of_lt_debt_a | fundamental2 | -0.13 | 1.69 | +0.50 | -0.76 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.03 | 1.64 | +0.45 | -0.65 | yes |
| fn_repayments_of_debt_a | fundamental2 | -0.11 | 1.70 | +0.51 | -0.08 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.10 | 1.66 | +0.47 | -0.18 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
