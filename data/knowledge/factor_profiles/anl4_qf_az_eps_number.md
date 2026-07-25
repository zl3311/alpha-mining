---
field: anl4_qf_az_eps_number
dataset: analyst4
best_template: decay_linear
best_sharpe: 1.37
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 35
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0379
ann_vol: 0.0254
hit_rate: 0.5263
rolling_sharpe_min: -0.18
rolling_sharpe_max: 3.521
top_merge_partner: fnd6_rank
redundancy_cluster: 5
negated_best_sharpe: 0.83
negated_best_template: neg_rank_level
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.54
---
# anl4_qf_az_eps_number (analyst4)

*Earnings per share - number of estimations*

## Signal Profile
- `rank(anl4_qf_az_eps_number)`: S=1.36, F=0.71, T=2.9%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_eps_number / close)`: S=0.25, F=0.11, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qf_az_eps_number, 5))`: S=0.00, F=0.00, T=34.7%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(anl4_qf_az_eps_number), 5)`: S=1.37, F=0.72, T=2.8%, INFERIOR (TOP3000)
- `-rank(anl4_qf_az_eps_number)`: S=-0.68, F=-0.30, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_eps_number, 5))`: S=0.62, F=0.28, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_eps_number, 22)`: S=0.31, F=0.08, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_eps_number, 10)`: S=0.75, F=0.38, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_eps_number, 22))`: S=-0.18, F=-0.04, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps_number)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps_number / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/31P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 32F/3P
- LOW_SUB_UNIVERSE_SHARPE: 17F/6P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 1.37, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.89 (strong), ret=+4.0%
  - 2020: S=0.73 (moderate), ret=+1.8%
  - 2021: S=2.26 (strong), ret=+6.5%
  - 2022: S=1.31 (moderate), ret=+3.6%
  - 2023: S=0.56 (moderate), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 3.79% over 263 days (recovered)
- Annualized: return +3.5%, volatility 2.5% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.01, excess kurtosis +1.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.18, max 3.52, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +2.31%; worst month: -1.19%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.99
- Sideways: S=1.27
- Bear: S=0.79

## Negated Direction
Best negated: `rank(-1 * anl4_qf_az_eps_number)` S=0.83, F=0.58, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qf_az_eps_number)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps_number / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_eps_number, 5))`: S=0.62, F=0.28, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(anl4_qf_az_eps_number), 5)` | TOP3000 | 1.37 | 0.72 | 3.8% | 100% | all-weather |
| `rank(anl4_qf_az_eps_number)` | TOP3000 | 1.36 | 0.71 | 3.9% | 100% | all-weather |
| `rank(anl4_qf_az_eps_number)` | TOP1000 | 0.68 | 0.30 | 6.3% | 80% | mixed |
| `rank(anl4_qf_az_eps_number / close)` | TOP1000 | 0.25 | 0.11 | 25.4% | 40% | bear-only |
| `rank(anl4_qf_az_eps_number / close)` | TOP3000 | 0.16 | 0.06 | 40.5% | 40% | bear-only |
| `rank(anl4_qf_az_eps_number / close)` | TOP500 | 0.14 | 0.04 | 23.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_eps_number: 0.998 (strongly positively correlated)
- sales_estimate_count_quarterly: 0.800 (strongly positively correlated)
- anl4_netprofit_number: 0.683 (moderately positively correlated)
- anl4_ebit_number: 0.663 (moderately positively correlated)
- anl4_epsr_number: 0.643 (moderately positively correlated)

Redundancy cluster #5: 5 similar fields, mean |rho| 0.774 (representative: sales_estimate_count_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.21 | 1.97 | +0.60 | -0.26 | yes |
| fn_liab_fair_val_l2_q | fundamental2 | +0.06 | 1.89 | +0.49 | -0.27 | yes |
| implied_volatility_put_1080 | option8 | +0.02 | 1.88 | +0.49 | +0.26 | yes |
| implied_volatility_put_720 | option8 | +0.02 | 1.89 | +0.48 | +0.25 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.13 | 2.01 | +0.38 | -0.94 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: trade_when
