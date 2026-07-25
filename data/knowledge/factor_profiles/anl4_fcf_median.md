---
field: anl4_fcf_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1404
ann_vol: 0.0827
hit_rate: 0.5215
rolling_sharpe_min: -2.019
rolling_sharpe_max: 2.937
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.37
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.56
---
# anl4_fcf_median (analyst4)

*Free cash flow - aggregation on estimations, 50th percentile*

## Signal Profile
- `rank(anl4_fcf_median)`: S=0.44, F=0.27, T=1.7%, INFERIOR (TOP3000)
- `rank(anl4_fcf_median / close)`: S=0.93, F=0.73, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcf_median, 5))`: S=0.12, F=0.02, T=36.9%, INFERIOR (TOP500)
- `-rank(anl4_fcf_median)`: S=-0.21, F=-0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_median, 5))`: S=0.17, F=0.04, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_fcf_median, 22)`: S=0.21, F=0.04, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_median, 10)`: S=-0.04, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_median, 22))`: S=-0.01, F=0.00, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_median)`: S=0.19, F=0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_median / close)`: S=0.37, F=0.22, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.75 (moderate), ret=+2.9%
  - 2020: S=-1.65 (negative), ret=-10.2%
  - 2021: S=1.90 (strong), ret=+19.7%
  - 2022: S=1.76 (strong), ret=+20.2%
  - 2023: S=0.72 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 14.04% over 539 days (recovered)
- Annualized: return +7.6%, volatility 8.3% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.14, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.02, max 2.94, latest 0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.76%; worst month: -3.06%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.40
- Sideways: S=0.60
- Bear: S=-2.16

## Negated Direction
Best negated: `rank(-1 * anl4_fcf_median / close)` S=0.37, F=0.22, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcf_median)`: S=0.19, F=0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_median / close)`: S=0.37, F=0.22, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_median, 5))`: S=0.17, F=0.04, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_median / close)` | TOP3000 | 0.91 | 0.73 | 14.0% | 80% | bull-only |
| `rank(anl4_fcf_median)` | TOP3000 | 0.43 | 0.27 | 33.0% | 80% | bull-only |
| `rank(anl4_fcf_median / close)` | TOP1000 | 0.29 | 0.15 | 21.7% | 40% | bull-only |
| `rank(anl4_fcf_median)` | TOP1000 | 0.20 | 0.09 | 33.5% | 60% | bull-only |
| `rank(ts_delta(anl4_fcf_median, 5))` | TOP500 | 0.13 | 0.02 | 19.6% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_fcf_mean: 0.999 (strongly positively correlated)
- anl4_fcf_high: 0.991 (strongly positively correlated)
- anl4_fcf_low: 0.991 (strongly positively correlated)
- est_fcf: 0.979 (strongly positively correlated)
- anl4_cfo_low: 0.948 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.47 | 1.87 | +0.84 | -0.88 | no |
| fnd6_txtubadjust | fundamental6 | -0.35 | 1.55 | +0.64 | -0.68 | yes |
| news_open_vol | news12 | -0.34 | 1.59 | +0.66 | -0.42 | yes |
| rp_ess_revenue | news18 | -0.31 | 1.52 | +0.61 | -0.89 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.33 | 2.48 | +0.61 | -0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
