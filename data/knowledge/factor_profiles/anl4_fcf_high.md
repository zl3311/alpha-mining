---
field: anl4_fcf_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.83
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1258
ann_vol: 0.0799
hit_rate: 0.5223
rolling_sharpe_min: -1.803
rolling_sharpe_max: 2.811
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 36
negated_best_sharpe: 0.32
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.71
---
# anl4_fcf_high (analyst4)

*Free cash flow - aggregation on estimations, max*

## Signal Profile
- `rank(anl4_fcf_high)`: S=0.51, F=0.34, T=1.7%, INFERIOR (TOP3000)
- `rank(anl4_fcf_high / close)`: S=1.03, F=0.83, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcf_high, 5))`: S=0.10, F=0.02, T=34.6%, INFERIOR (TOP200)
- `-rank(anl4_fcf_high)`: S=-0.26, F=-0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_high, 5))`: S=-0.10, F=-0.02, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_fcf_high, 22)`: S=0.31, F=0.08, T=34.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_high, 10)`: S=-0.03, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_high, 22))`: S=0.11, F=0.02, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_high)`: S=0.15, F=0.06, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_high / close)`: S=0.32, F=0.18, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.00 (moderate), ret=+4.1%
  - 2020: S=-1.38 (negative), ret=-8.6%
  - 2021: S=1.75 (strong), ret=+18.0%
  - 2022: S=1.89 (strong), ret=+20.1%
  - 2023: S=1.09 (moderate), ret=+6.2%

## Risk & Drawdown
- Max drawdown: 12.58% over 495 days (recovered)
- Annualized: return +8.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.18, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.81, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.67%; worst month: -3.13%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.51
- Sideways: S=0.78
- Bear: S=-2.07

## Negated Direction
Best negated: `rank(-1 * anl4_fcf_high / close)` S=0.32, F=0.18, INFERIOR
Direction gap: -0.71 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcf_high)`: S=0.15, F=0.06, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_high / close)`: S=0.32, F=0.18, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_high, 5))`: S=-0.10, F=-0.02, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_high / close)` | TOP3000 | 1.02 | 0.83 | 12.6% | 80% | bull-only |
| `rank(anl4_fcf_high)` | TOP3000 | 0.50 | 0.34 | 33.1% | 80% | bull-only |
| `rank(anl4_fcf_high / close)` | TOP1000 | 0.39 | 0.21 | 20.1% | 60% | bull-only |
| `rank(anl4_fcf_high)` | TOP1000 | 0.25 | 0.13 | 32.7% | 60% | bull-only |
| `rank(ts_delta(anl4_fcf_high, 5))` | TOP200 | 0.10 | 0.02 | 33.6% | 60% | weak |
| `rank(anl4_fcf_high / close)` | TOP500 | 0.07 | 0.02 | 32.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_fcf_mean: 0.992 (strongly positively correlated)
- anl4_fcf_median: 0.991 (strongly positively correlated)
- anl4_fcf_low: 0.972 (strongly positively correlated)
- est_fcf: 0.972 (strongly positively correlated)
- anl4_cfo_mean: 0.949 (strongly positively correlated)

Redundancy cluster #36: 4 similar fields, mean |rho| 0.734 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.45 | 1.92 | +0.89 | -0.92 | no |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.31 | 2.28 | +0.66 | -0.55 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.31 | 2.52 | +0.65 | -0.52 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.32 | 2.67 | +0.65 | -0.43 | yes |
| fnd6_txtubadjust | fundamental6 | -0.34 | 1.62 | +0.61 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
