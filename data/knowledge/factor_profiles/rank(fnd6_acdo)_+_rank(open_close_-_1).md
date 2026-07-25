---
field: rank(fnd6_acdo) + rank(open/close - 1)
dataset: unknown
best_template: unknown
best_sharpe: 2.02
best_fitness: 1.12
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 1
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0692
ann_vol: 0.1011
hit_rate: 0.5255
rolling_sharpe_min: -0.176
rolling_sharpe_max: 3.783
top_merge_partner: anl4_bvps_flag
redundancy_cluster: 2
---
# rank(fnd6_acdo) + rank(open/close - 1) (unknown)


## Signal Profile
- No simulation data available

## Check Summary
No check failures observed across simulations.

## Temporal Behavior
Headline (unknown): Overall Sharpe 2.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.7%
  - 2020: S=3.22 (strong), ret=+29.1%
  - 2021: S=1.68 (strong), ret=+20.0%
  - 2022: S=1.87 (strong), ret=+26.2%
  - 2023: S=3.48 (strong), ret=+24.2%

## Risk & Drawdown
- Max drawdown: 6.92% over 49 days (recovered)
- Annualized: return +20.4%, volatility 10.1% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +1.70, excess kurtosis +9.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.18, max 3.78, latest 3.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +12.22%; worst month: -3.87%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.95
- Sideways: S=2.32
- Bear: S=1.96

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_acdo) + rank(open/close - 1)` | TOP3000 | 2.02 | 1.12 | 6.9% | 100% | all-weather |

## Correlation Notes
Top correlates:
- rank(fnd6_acdo) * rank(-1 * returns): 0.959 (strongly positively correlated)
- rank(scl12_buzz * (-1 * returns)): 0.903 (strongly positively correlated)
- rank(scl12_sentiment * (-1 * returns)): 0.460 (moderately positively correlated)
- snt_social_value: -0.441 (moderately negatively correlated)
- fnd6_prccq: 0.415 (moderately positively correlated)

Redundancy cluster #2: 3 similar fields, mean |rho| 0.933 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_bvps_flag | analyst_revision | -0.35 | 2.96 | +0.93 | -0.68 | yes |
| rel_num_all | pv13 | -0.36 | 2.90 | +0.88 | -0.74 | yes |
| anl4_netdebt_flag | analyst_revision | -0.33 | 2.87 | +0.85 | -0.46 | yes |
| anl4_ptpr_flag | analyst_revision | -0.32 | 2.83 | +0.81 | -0.74 | yes |
| rel_num_comp | pv13 | -0.36 | 2.82 | +0.80 | -0.65 | yes |

## Actionability
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
