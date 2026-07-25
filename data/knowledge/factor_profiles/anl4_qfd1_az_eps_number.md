---
field: anl4_qfd1_az_eps_number
dataset: analyst4
best_template: rank_level
best_sharpe: 1.36
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.0387
ann_vol: 0.0254
hit_rate: 0.5247
rolling_sharpe_min: -0.214
rolling_sharpe_max: 3.518
top_merge_partner: fnd6_rank
redundancy_cluster: 5
negated_best_sharpe: 0.83
negated_best_template: neg_rank_level
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.53
---
# anl4_qfd1_az_eps_number (analyst4)

*Earnings per share - number of estimations*

## Signal Profile
- `rank(anl4_qfd1_az_eps_number)`: S=1.36, F=0.71, T=2.9%, INFERIOR (TOP3000)
- `rank(anl4_qfd1_az_eps_number / close)`: S=0.25, F=0.11, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfd1_az_eps_number, 5))`: S=0.00, F=0.00, T=34.7%, INFERIOR (TOP3000)
- `-rank(anl4_qfd1_az_eps_number)`: S=-0.68, F=-0.30, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_eps_number, 5))`: S=0.62, F=0.28, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfd1_az_eps_number, 22)`: S=0.31, F=0.08, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_eps_number, 10)`: S=0.75, F=0.38, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_eps_number, 22))`: S=-0.18, F=-0.04, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_eps_number)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_eps_number / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.36, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.79 (strong), ret=+3.8%
  - 2020: S=0.69 (moderate), ret=+1.7%
  - 2021: S=2.24 (strong), ret=+6.4%
  - 2022: S=1.39 (moderate), ret=+3.8%
  - 2023: S=0.56 (moderate), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 3.87% over 263 days (recovered)
- Annualized: return +3.4%, volatility 2.5% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.01, excess kurtosis +1.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.21, max 3.52, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +2.35%; worst month: -1.25%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.02
- Sideways: S=1.16
- Bear: S=0.82

## Negated Direction
Best negated: `rank(-1 * anl4_qfd1_az_eps_number)` S=0.83, F=0.58, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_eps_number)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_eps_number / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_eps_number, 5))`: S=0.62, F=0.28, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qfd1_az_eps_number)` | TOP3000 | 1.36 | 0.71 | 3.9% | 100% | all-weather |
| `rank(anl4_qfd1_az_eps_number)` | TOP1000 | 0.68 | 0.30 | 6.3% | 80% | mixed |
| `rank(anl4_qfd1_az_eps_number / close)` | TOP1000 | 0.25 | 0.11 | 25.4% | 40% | bear-only |
| `rank(anl4_qfd1_az_eps_number / close)` | TOP3000 | 0.16 | 0.06 | 40.5% | 40% | bear-only |
| `rank(anl4_qfd1_az_eps_number / close)` | TOP500 | 0.14 | 0.04 | 23.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_eps_number: 0.998 (strongly positively correlated)
- sales_estimate_count_quarterly: 0.801 (strongly positively correlated)
- anl4_netprofit_number: 0.684 (moderately positively correlated)
- anl4_ebit_number: 0.663 (moderately positively correlated)
- anl4_epsr_number: 0.640 (moderately positively correlated)

Redundancy cluster #5: 5 similar fields, mean |rho| 0.774 (representative: sales_estimate_count_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.22 | 1.97 | +0.61 | -0.24 | yes |
| fn_liab_fair_val_l2_q | fundamental2 | +0.06 | 1.89 | +0.48 | -0.26 | yes |
| implied_volatility_put_1080 | option8 | +0.02 | 1.87 | +0.48 | +0.32 | yes |
| implied_volatility_put_720 | option8 | +0.02 | 1.89 | +0.48 | +0.31 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.02 | 1.73 | +0.37 | -0.96 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
