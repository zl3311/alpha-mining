---
field: rel_num_all
dataset: pv13
best_template: rank_level
best_sharpe: 1.24
best_fitness: 1.06
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 18
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1435
ann_vol: 0.0737
hit_rate: 0.5174
rolling_sharpe_min: -2.393
rolling_sharpe_max: 2.999
top_merge_partner: rank(fnd6_acdo) + rank(open/close - 1)
redundancy_cluster: 13
negated_best_sharpe: -0.35
negated_best_template: rank_neg_delta
negated_best_fitness: -0.07
n_negated_sims: 4
direction_gap: -1.59
---
# rel_num_all (pv13)

*number of the companies whose product overlapped with the instrument*

## Signal Profile
- `rank(rel_num_all)`: S=1.24, F=1.06, T=1.2%, AVERAGE (TOP3000)
- `rank(ts_delta(rel_num_all, 5))`: S=0.38, F=0.11, T=34.5%, INFERIOR (TOP200)
- `-rank(rel_num_all)`: S=-0.53, F=-0.35, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_all, 5))`: S=-0.35, F=-0.07, T=35.3%, INFERIOR (TOP3000)
- `-ts_zscore(rel_num_all, 63)`: S=0.72, F=0.31, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(rel_num_all, 10)`: S=0.30, F=0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_num_all, 22))`: S=-0.23, F=-0.05, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_all)`: S=-1.24, F=-1.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_all / close)`: S=-1.03, F=-0.84, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 17F/1P
- LOW_SHARPE: 18F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.22, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.78 (strong), ret=+5.8%
  - 2020: S=-1.01 (negative), ret=-4.2%
  - 2021: S=1.89 (strong), ret=+21.1%
  - 2022: S=2.06 (strong), ret=+19.7%
  - 2023: S=0.40 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 14.35% over 519 days (recovered)
- Annualized: return +9.0%, volatility 7.4% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.18, excess kurtosis +3.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.39, max 3.00, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.28%; worst month: -2.13%
Positive months: 68%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.09
- Sideways: S=1.32
- Bear: S=-1.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_num_all, 5))` S=-0.35, F=-0.07, INFERIOR
Direction gap: -1.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rel_num_all)`: S=-1.24, F=-1.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_all / close)`: S=-1.03, F=-0.84, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_all, 5))`: S=-0.35, F=-0.07, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_num_all)` | TOP3000 | 1.22 | 1.06 | 14.3% | 80% | bull-only |
| `rank(rel_num_all)` | TOP1000 | 0.52 | 0.35 | 26.6% | 80% | bull-only |
| `rank(rel_num_all)` | TOP500 | 0.38 | 0.24 | 41.6% | 80% | bull-only |
| `rank(ts_delta(rel_num_all, 5))` | TOP200 | 0.41 | 0.11 | 12.0% | 40% | mixed |
| `rank(ts_delta(rel_num_all, 5))` | TOP3000 | 0.37 | 0.07 | 15.1% | 60% | weak |
| `rank(ts_delta(rel_num_all, 5))` | TOP1000 | 0.21 | 0.03 | 9.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- rel_num_comp: 0.977 (strongly positively correlated)
- rel_num_part: 0.945 (strongly positively correlated)
- pv13_com_page_rank: 0.905 (strongly positively correlated)
- fnd6_mrc3: 0.896 (strongly positively correlated)
- fnd6_mrc4: 0.894 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.90 | +0.88 | -0.74 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.34 | 2.49 | +0.86 | -0.83 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.33 | 2.67 | +0.80 | -0.79 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.46 | 2.06 | +0.84 | -0.34 | yes |
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.95 | +0.73 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
