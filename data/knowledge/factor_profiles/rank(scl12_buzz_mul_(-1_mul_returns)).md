---
field: rank(scl12_buzz * (-1 * returns))
dataset: socialmedia12
best_template: unknown
best_sharpe: 1.63
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 1
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0841
ann_vol: 0.0902
hit_rate: 0.5304
rolling_sharpe_min: 0.129
rolling_sharpe_max: 4.001
top_merge_partner: anl4_bvps_flag
redundancy_cluster: 2
---
# rank(scl12_buzz * (-1 * returns)) (socialmedia12)


## Signal Profile
- No simulation data available

## Check Summary
- HIGH_TURNOVER: 1F/0P
- LOW_FITNESS: 1F/0P

## Temporal Behavior
Headline (unknown): Overall Sharpe 1.63, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.32 (weak), ret=+1.5%
  - 2020: S=3.20 (strong), ret=+24.8%
  - 2021: S=0.62 (moderate), ret=+7.2%
  - 2022: S=1.32 (moderate), ret=+15.4%
  - 2023: S=3.70 (strong), ret=+23.0%

## Risk & Drawdown
- Max drawdown: 8.41% over 349 days (recovered)
- Annualized: return +14.7%, volatility 9.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +1.56, excess kurtosis +9.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.13, max 4.00, latest 3.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +8.75%; worst month: -3.46%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.66
- Sideways: S=2.01
- Bear: S=1.39

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(scl12_buzz * (-1 * returns))` | TOP3000 | 1.63 | 0.65 | 8.4% | 100% | all-weather |

## Correlation Notes
Top correlates:
- rank(fnd6_acdo) * rank(-1 * returns): 0.938 (strongly positively correlated)
- rank(fnd6_acdo) + rank(open/close - 1): 0.903 (strongly positively correlated)
- rank(scl12_sentiment * (-1 * returns)): 0.577 (moderately positively correlated)
- snt_social_value: -0.459 (moderately negatively correlated)
- fnd6_prccq: 0.442 (moderately positively correlated)

Redundancy cluster #2: 3 similar fields, mean |rho| 0.933 (representative: rank(fnd6_acdo) + rank(open/close - 1)). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_bvps_flag | analyst_revision | -0.34 | 2.55 | +0.93 | -0.76 | yes |
| rel_num_all | pv13 | -0.34 | 2.49 | +0.86 | -0.83 | yes |
| anl4_netdebt_flag | analyst_revision | -0.31 | 2.48 | +0.85 | -0.60 | yes |
| anl4_ptpr_flag | analyst_revision | -0.31 | 2.45 | +0.82 | -0.79 | yes |
| rel_num_part | pv13 | -0.31 | 2.44 | +0.82 | -0.54 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
