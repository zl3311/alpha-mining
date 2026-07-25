---
field: rel_num_comp
dataset: pv13
best_template: rank_level
best_sharpe: 1.13
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 18
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1216
ann_vol: 0.0668
hit_rate: 0.5109
rolling_sharpe_min: -2.416
rolling_sharpe_max: 3.078
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: -0.24
negated_best_template: rank_neg_delta
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -1.37
---
# rel_num_comp (pv13)

*number of the instrument's competitors*

## Signal Profile
- `rank(rel_num_comp)`: S=1.13, F=0.88, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_num_comp, 5))`: S=0.54, F=0.22, T=34.5%, INFERIOR (TOP200)
- `-rank(rel_num_comp)`: S=-0.60, F=-0.41, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_comp, 5))`: S=-0.24, F=-0.05, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(rel_num_comp, 63)`: S=0.44, F=0.17, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(rel_num_comp, 10)`: S=0.34, F=0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_num_comp, 22))`: S=-0.33, F=-0.11, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_comp)`: S=-1.13, F=-0.88, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_comp / close)`: S=-1.23, F=-1.03, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/16P
- LOW_FITNESS: 18F/0P
- LOW_SHARPE: 18F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.11, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+3.5%
  - 2020: S=-1.32 (negative), ret=-5.0%
  - 2021: S=2.09 (strong), ret=+21.0%
  - 2022: S=1.88 (strong), ret=+16.4%
  - 2023: S=0.10 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 12.16% over 549 days (recovered)
- Annualized: return +7.4%, volatility 6.7% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.13, excess kurtosis +3.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.42, max 3.08, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.39%; worst month: -2.33%
Positive months: 70%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.80
- Sideways: S=1.15
- Bear: S=-1.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_num_comp, 5))` S=-0.24, F=-0.05, INFERIOR
Direction gap: -1.37 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rel_num_comp)`: S=-1.13, F=-0.88, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_comp / close)`: S=-1.23, F=-1.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_comp, 5))`: S=-0.24, F=-0.05, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_num_comp)` | TOP3000 | 1.11 | 0.88 | 12.2% | 80% | bull-only |
| `rank(rel_num_comp)` | TOP1000 | 0.59 | 0.41 | 23.8% | 80% | bull-only |
| `rank(ts_delta(rel_num_comp, 5))` | TOP200 | 0.56 | 0.22 | 15.2% | 80% | mixed |
| `rank(rel_num_comp)` | TOP500 | 0.34 | 0.21 | 40.8% | 40% | bull-only |
| `rank(ts_delta(rel_num_comp, 5))` | TOP3000 | 0.24 | 0.05 | 9.0% | 60% | mixed |
| `rank(ts_delta(rel_num_comp, 5))` | TOP500 | 0.12 | 0.02 | 17.9% | 80% | weak |

## Correlation Notes
Top correlates:
- rel_num_all: 0.977 (strongly positively correlated)
- rel_num_part: 0.896 (strongly positively correlated)
- pv13_com_page_rank: 0.881 (strongly positively correlated)
- pv13_com_rk_au: 0.864 (strongly positively correlated)
- anl4_bvps_flag: 0.858 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.35 | 2.42 | +0.79 | -0.80 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.46 | 1.93 | +0.82 | -0.50 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.82 | +0.80 | -0.65 | yes |
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.83 | +0.71 | -0.87 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.59 | +0.72 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
