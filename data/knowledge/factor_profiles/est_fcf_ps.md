---
field: est_fcf_ps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1174
ann_vol: 0.0803
hit_rate: 0.5069
rolling_sharpe_min: -1.607
rolling_sharpe_max: 2.797
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.38
---
# est_fcf_ps (analyst4)

*Free Cash Flow Per Share - Mean of Estimations*

## Signal Profile
- `rank(est_fcf_ps)`: S=0.41, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(est_fcf_ps / close)`: S=0.81, F=0.58, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(est_fcf_ps, 5))`: S=0.24, F=0.05, T=36.7%, INFERIOR (TOP1000)
- `-rank(est_fcf_ps)`: S=-0.37, F=-0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_fcf_ps, 5))`: S=0.43, F=0.10, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(est_fcf_ps, 63)`: S=0.21, F=0.05, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(est_fcf_ps, 10)`: S=0.19, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(est_fcf_ps, 22))`: S=-0.11, F=-0.02, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf_ps)`: S=-0.41, F=-0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf_ps / close)`: S=-0.81, F=-0.58, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.72 (negative), ret=-3.3%
  - 2020: S=-0.58 (negative), ret=-5.4%
  - 2021: S=2.05 (strong), ret=+18.3%
  - 2022: S=1.79 (strong), ret=+17.3%
  - 2023: S=0.93 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 11.74% over 784 days (recovered)
- Annualized: return +6.4%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.42, excess kurtosis +2.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.80, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.37%; worst month: -3.03%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.25
- Sideways: S=-0.59
- Bear: S=-0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_fcf_ps, 5))` S=0.43, F=0.10, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_fcf_ps)`: S=-0.41, F=-0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf_ps / close)`: S=-0.81, F=-0.58, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_fcf_ps, 5))`: S=0.43, F=0.10, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_fcf_ps / close)` | TOP3000 | 0.80 | 0.58 | 11.7% | 60% | bull-only |
| `rank(est_fcf_ps / close)` | TOP1000 | 0.52 | 0.33 | 13.6% | 40% | bull-only |
| `rank(est_fcf_ps)` | TOP3000 | 0.40 | 0.22 | 27.6% | 80% | bull-only |
| `rank(est_fcf_ps)` | TOP1000 | 0.36 | 0.19 | 26.9% | 80% | bull-only |
| `rank(ts_delta(est_fcf_ps, 5))` | TOP1000 | 0.23 | 0.05 | 18.4% | 60% | bear-only |
| `rank(est_fcf_ps)` | TOP200 | 0.12 | 0.05 | 25.4% | 60% | bull-only |
| `rank(ts_delta(est_fcf_ps, 5))` | TOP500 | 0.19 | 0.03 | 24.2% | 40% | mixed |
| `rank(est_fcf_ps)` | TOP500 | 0.10 | 0.03 | 33.3% | 60% | bull-only |
| `rank(est_fcf_ps / close)` | TOP200 | 0.07 | 0.02 | 26.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_fcfps_mean: 0.965 (strongly positively correlated)
- anl4_fcfps_median: 0.964 (strongly positively correlated)
- anl4_fcfps_low: 0.961 (strongly positively correlated)
- anl4_fcfps_high: 0.958 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.897 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.38 | 1.51 | +0.62 | -0.76 | yes |
| fnd6_txtubadjust | fundamental6 | -0.36 | 1.45 | +0.60 | -0.79 | yes |
| news_open_vol | news12 | -0.34 | 1.50 | +0.57 | -0.81 | yes |
| anl4_rd_exp_flag | analyst4 | -0.45 | 1.74 | +0.71 | -0.46 | no |
| max_gross_income_guidance_2 | analyst4 | -0.38 | 1.43 | +0.62 | -0.84 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
