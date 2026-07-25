---
field: fnd2_a_lhdiprtsg
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2235
ann_vol: 0.0946
hit_rate: 0.5279
rolling_sharpe_min: -2.568
rolling_sharpe_max: 2.66
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.22
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.65
---
# fnd2_a_lhdiprtsg (fundamental2)

*Amount before accumulated depreciation of additions or improvements to assets held under a lease arrangement.*

## Signal Profile
- `rank(fnd2_a_lhdiprtsg)`: S=0.87, F=0.71, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd2_a_lhdiprtsg / close)`: S=0.95, F=0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_lhdiprtsg, 5))`: S=0.33, F=0.18, T=22.8%, INFERIOR (TOP200)
- `-rank(fnd2_a_lhdiprtsg)`: S=-0.37, F=-0.24, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_lhdiprtsg, 5))`: S=-0.35, F=-0.20, T=22.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_lhdiprtsg, 22)`: S=0.60, F=0.55, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_lhdiprtsg, 10)`: S=0.26, F=0.12, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_lhdiprtsg, 22))`: S=-0.33, F=-0.19, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_lhdiprtsg)`: S=0.22, F=0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_lhdiprtsg / close)`: S=0.01, F=0.00, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+5.1%
  - 2020: S=-1.02 (negative), ret=-6.2%
  - 2021: S=1.09 (moderate), ret=+15.2%
  - 2022: S=1.71 (strong), ret=+19.6%
  - 2023: S=0.97 (moderate), ret=+6.7%

## Risk & Drawdown
- Max drawdown: 22.35% over 740 days (recovered)
- Annualized: return +8.2%, volatility 9.5% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.04, excess kurtosis +2.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.57, max 2.66, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.05%; worst month: -5.38%
Positive months: 68%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.94
- Sideways: S=1.39
- Bear: S=-2.24

## Negated Direction
Best negated: `rank(-1 * fnd2_a_lhdiprtsg)` S=0.22, F=0.13, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_lhdiprtsg)`: S=0.22, F=0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_lhdiprtsg / close)`: S=0.01, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_lhdiprtsg, 5))`: S=-0.35, F=-0.20, T=22.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_lhdiprtsg)` | TOP3000 | 0.87 | 0.71 | 22.4% | 80% | bull-only |
| `rank(fnd2_a_lhdiprtsg / close)` | TOP3000 | 0.94 | 0.70 | 8.3% | 100% | mixed |
| `rank(fnd2_a_lhdiprtsg / close)` | TOP1000 | 0.45 | 0.29 | 14.7% | 60% | bull-only |
| `rank(fnd2_a_lhdiprtsg)` | TOP1000 | 0.36 | 0.24 | 34.9% | 80% | bull-only |
| `rank(fnd2_a_lhdiprtsg / close)` | TOP500 | 0.37 | 0.23 | 22.7% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_lhdiprtsg, 5))` | TOP200 | 0.34 | 0.18 | 43.8% | 60% | bull-only |
| `rank(fnd2_a_lhdiprtsg)` | TOP500 | 0.21 | 0.12 | 46.8% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_lhdiprtsg, 5))` | TOP1000 | 0.21 | 0.08 | 37.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_2y_a: 0.943 (strongly positively correlated)
- fnd6_mrc2: 0.938 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_3y_a: 0.937 (strongly positively correlated)
- fnd6_xrent: 0.936 (strongly positively correlated)
- fnd6_mrc3: 0.934 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.37 | 1.69 | +0.67 | -0.98 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.43 | 1.75 | +0.75 | -0.10 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.35 | 1.47 | +0.60 | -0.95 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.30 | 1.53 | +0.58 | -0.86 | yes |
| fnd6_txtubadjust | fundamental6 | -0.23 | 1.38 | +0.51 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
