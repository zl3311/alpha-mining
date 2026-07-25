---
field: rank(fnd6_acdo) * rank(-1 * returns)
dataset: unknown
best_template: unknown
best_sharpe: 1.87
best_fitness: 1.04
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 1
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0773
ann_vol: 0.1122
hit_rate: 0.5166
rolling_sharpe_min: -0.584
rolling_sharpe_max: 3.839
top_merge_partner: anl4_bvps_flag
redundancy_cluster: 2
---
# rank(fnd6_acdo) * rank(-1 * returns) (unknown)


## Signal Profile
- No simulation data available

## Check Summary
No check failures observed across simulations.

## Temporal Behavior
Headline (unknown): Overall Sharpe 1.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.28 (negative), ret=-1.5%
  - 2020: S=3.46 (strong), ret=+37.0%
  - 2021: S=1.21 (moderate), ret=+16.0%
  - 2022: S=1.74 (strong), ret=+26.3%
  - 2023: S=3.33 (strong), ret=+25.1%

## Risk & Drawdown
- Max drawdown: 7.73% over 334 days (recovered)
- Annualized: return +21.0%, volatility 11.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +1.55, excess kurtosis +8.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.58, max 3.84, latest 3.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +14.65%; worst month: -3.22%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.78
- Sideways: S=2.02
- Bear: S=1.96

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_acdo) * rank(-1 * returns)` | TOP3000 | 1.87 | 1.04 | 7.7% | 80% | all-weather |

## Correlation Notes
Top correlates:
- rank(fnd6_acdo) + rank(open/close - 1): 0.959 (strongly positively correlated)
- rank(scl12_buzz * (-1 * returns)): 0.938 (strongly positively correlated)
- rank(scl12_sentiment * (-1 * returns)): 0.491 (moderately positively correlated)
- snt_social_value: -0.455 (moderately negatively correlated)
- fnd6_prccq: 0.428 (moderately positively correlated)

Redundancy cluster #2: 3 similar fields, mean |rho| 0.933 (representative: rank(fnd6_acdo) + rank(open/close - 1)). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_bvps_flag | analyst_revision | -0.33 | 2.74 | +0.87 | -0.73 | yes |
| rel_num_all | pv13 | -0.33 | 2.67 | +0.80 | -0.79 | yes |
| anl4_netdebt_flag | analyst_revision | -0.30 | 2.66 | +0.79 | -0.52 | yes |
| anl4_ptpr_flag | analyst_revision | -0.29 | 2.60 | +0.73 | -0.79 | yes |
| rel_num_comp | pv13 | -0.34 | 2.59 | +0.72 | -0.71 | yes |

## Actionability
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
