---
field: anl4_fcf_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1422
ann_vol: 0.0831
hit_rate: 0.5166
rolling_sharpe_min: -2.052
rolling_sharpe_max: 2.928
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.54
---
# anl4_fcf_mean (analyst4)

*Free Cash Flow - mean of estimations*

## Signal Profile
- `rank(anl4_fcf_mean)`: S=0.44, F=0.27, T=1.7%, INFERIOR (TOP3000)
- `rank(anl4_fcf_mean / close)`: S=0.92, F=0.72, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcf_mean, 5))`: S=0.10, F=0.01, T=36.7%, INFERIOR (TOP500)
- `-rank(anl4_fcf_mean)`: S=-0.22, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_mean, 5))`: S=0.38, F=0.08, T=36.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_fcf_mean, 22)`: S=0.22, F=0.04, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_mean, 10)`: S=-0.02, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_mean, 22))`: S=-0.16, F=-0.03, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_mean)`: S=-0.44, F=-0.27, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_mean / close)`: S=-0.92, F=-0.72, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+3.2%
  - 2020: S=-1.68 (negative), ret=-10.3%
  - 2021: S=1.88 (strong), ret=+19.6%
  - 2022: S=1.76 (strong), ret=+20.3%
  - 2023: S=0.69 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 14.22% over 539 days (recovered)
- Annualized: return +7.6%, volatility 8.3% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.14, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.05, max 2.93, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.78%; worst month: -3.06%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.40
- Sideways: S=0.60
- Bear: S=-2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcf_mean, 5))` S=0.38, F=0.08, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcf_mean)`: S=-0.44, F=-0.27, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_mean / close)`: S=-0.92, F=-0.72, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_mean, 5))`: S=0.38, F=0.08, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_mean / close)` | TOP3000 | 0.91 | 0.72 | 14.2% | 80% | bull-only |
| `rank(anl4_fcf_mean)` | TOP3000 | 0.43 | 0.27 | 33.5% | 80% | bull-only |
| `rank(anl4_fcf_mean / close)` | TOP1000 | 0.29 | 0.15 | 21.3% | 40% | bull-only |
| `rank(anl4_fcf_mean)` | TOP1000 | 0.21 | 0.10 | 33.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_fcf_median: 0.999 (strongly positively correlated)
- anl4_fcf_high: 0.992 (strongly positively correlated)
- anl4_fcf_low: 0.991 (strongly positively correlated)
- est_fcf: 0.979 (strongly positively correlated)
- anl4_cfo_low: 0.948 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.47 | 1.86 | +0.84 | -0.89 | no |
| fnd6_txtubadjust | fundamental6 | -0.35 | 1.55 | +0.64 | -0.67 | yes |
| news_open_vol | news12 | -0.34 | 1.58 | +0.66 | -0.40 | yes |
| rp_ess_revenue | news18 | -0.31 | 1.52 | +0.61 | -0.89 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.33 | 2.47 | +0.60 | -0.56 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
