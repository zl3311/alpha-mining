---
field: est_fcf
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.82
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1653
ann_vol: 0.0793
hit_rate: 0.5045
rolling_sharpe_min: -2.401
rolling_sharpe_max: 2.731
top_merge_partner: fnd6_txtubadjust
redundancy_cluster: 13
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.56
---
# est_fcf (analyst4)

*Free Cash Flow - Mean of Estimations*

## Signal Profile
- `rank(est_fcf)`: S=0.45, F=0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(est_fcf / close)`: S=0.82, F=0.59, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(est_fcf, 5))`: S=0.25, F=0.05, T=36.7%, INFERIOR (TOP500)
- `-rank(est_fcf)`: S=-0.23, F=-0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_fcf, 5))`: S=0.26, F=0.04, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(est_fcf, 22)`: S=0.30, F=0.07, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(est_fcf, 10)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(est_fcf, 22))`: S=-0.08, F=-0.01, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf)`: S=-0.45, F=-0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf / close)`: S=-0.82, F=-0.59, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+2.9%
  - 2020: S=-1.89 (negative), ret=-11.2%
  - 2021: S=1.69 (strong), ret=+16.9%
  - 2022: S=1.58 (strong), ret=+17.2%
  - 2023: S=0.99 (moderate), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 16.53% over 738 days (recovered)
- Annualized: return +6.4%, volatility 7.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.03, excess kurtosis +1.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.40, max 2.73, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.93%; worst month: -3.24%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.32
- Sideways: S=0.62
- Bear: S=-2.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_fcf, 5))` S=0.26, F=0.04, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_fcf)`: S=-0.45, F=-0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * est_fcf / close)`: S=-0.82, F=-0.59, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_fcf, 5))`: S=0.26, F=0.04, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_fcf / close)` | TOP3000 | 0.81 | 0.59 | 16.5% | 80% | bull-only |
| `rank(est_fcf)` | TOP3000 | 0.44 | 0.27 | 32.2% | 80% | bull-only |
| `rank(est_fcf / close)` | TOP1000 | 0.32 | 0.16 | 22.7% | 60% | bull-only |
| `rank(est_fcf)` | TOP1000 | 0.23 | 0.11 | 34.8% | 60% | bull-only |
| `rank(ts_delta(est_fcf, 5))` | TOP500 | 0.26 | 0.05 | 10.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcf_mean: 0.979 (strongly positively correlated)
- anl4_fcf_median: 0.979 (strongly positively correlated)
- anl4_fcf_high: 0.972 (strongly positively correlated)
- anl4_fcf_low: 0.972 (strongly positively correlated)
- anl4_cfo_low: 0.952 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.35 | 1.46 | +0.61 | -0.69 | yes |
| anl4_rd_exp_flag | analyst4 | -0.46 | 1.75 | +0.73 | -0.89 | no |
| rp_ess_revenue | news18 | -0.30 | 1.43 | +0.54 | -0.86 | yes |
| news_open_vol | news12 | -0.33 | 1.49 | +0.56 | -0.36 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.32 | 2.39 | +0.52 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
