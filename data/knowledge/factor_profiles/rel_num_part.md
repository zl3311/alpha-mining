---
field: rel_num_part
dataset: pv13
cluster: pv13_other
coverage: 0.7837
community_alphas: 6898
best_template: rank_level
best_sharpe: 1.28
best_fitness: 1.01
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SUB_UNIVERSE_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0988
ann_vol: 0.0616
hit_rate: 0.5231
rolling_sharpe_min: -1.563
rolling_sharpe_max: 2.983
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -1.26
---
# rel_num_part (pv13)

*number of the instrument's partners*

## Signal Profile
- `rank(rel_num_part)`: S=1.28, F=1.01, T=1.1%, AVERAGE (TOP3000)
- `rank(ts_delta(rel_num_part, 5))`: S=0.93, F=0.34, T=35.7%, INFERIOR (TOP1000)
- `-rank(rel_num_part)`: S=-0.46, F=-0.26, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_part, 5))`: S=-0.22, F=-0.05, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(rel_num_part, 22)`: S=0.33, F=0.09, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(rel_num_part, 10)`: S=0.32, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_num_part, 22))`: S=0.90, F=0.45, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_part)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_part / close)`: S=-0.44, F=-0.27, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/23P
- LOW_FITNESS: 23F/1P
- LOW_SHARPE: 23F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.27, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+2.1%
  - 2020: S=-0.29 (negative), ret=-1.2%
  - 2021: S=1.83 (strong), ret=+16.5%
  - 2022: S=2.32 (strong), ret=+17.6%
  - 2023: S=0.78 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 9.88% over 511 days (recovered)
- Annualized: return +7.8%, volatility 6.2% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.28, excess kurtosis +2.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 2.98, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.40%; worst month: -2.56%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.43
- Sideways: S=1.38
- Bear: S=-1.78

## Negated Direction
Best negated: `rank(-1 * rel_num_part)` S=0.02, F=0.00, INFERIOR
Direction gap: -1.26 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rel_num_part)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_part / close)`: S=-0.44, F=-0.27, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_part, 5))`: S=-0.22, F=-0.05, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_num_part)` | TOP3000 | 1.27 | 1.01 | 9.9% | 80% | bull-only |
| `rank(ts_delta(rel_num_part, 5))` | TOP1000 | 0.95 | 0.34 | 4.8% | 100% | all-weather |
| `rank(rel_num_part)` | TOP1000 | 0.44 | 0.26 | 23.4% | 60% | bull-only |
| `rank(rel_num_part)` | TOP500 | 0.41 | 0.24 | 36.0% | 60% | bull-only |
| `rank(ts_delta(rel_num_part, 5))` | TOP500 | 0.34 | 0.07 | 7.8% | 80% | all-weather |
| `rank(ts_delta(rel_num_part, 5))` | TOP3000 | 0.37 | 0.07 | 16.0% | 60% | mixed |
| `rank(ts_delta(rel_num_part, 5))` | TOP200 | 0.24 | 0.05 | 12.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- rel_num_all: 0.945 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.909 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.905 (strongly positively correlated)
- sga_expense: 0.905 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.901 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.31 | 2.44 | +0.82 | -0.54 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.33 | 2.84 | +0.82 | -0.32 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.47 | 2.02 | +0.74 | -0.53 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.30 | 2.61 | +0.74 | -0.38 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.20 | 1.93 | +0.66 | -0.59 | yes |

## Actionability
Blocked by LOW_SUB_UNIVERSE_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
