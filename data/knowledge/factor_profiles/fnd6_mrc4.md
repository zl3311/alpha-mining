---
field: fnd6_mrc4
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.88
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1667
ann_vol: 0.081
hit_rate: 0.5182
rolling_sharpe_min: -1.832
rolling_sharpe_max: 2.475
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 13
negated_best_sharpe: 0.07
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.81
---
# fnd6_mrc4 (fundamental6)

*Rental Commitments - Minimum - 4th Year*

## Signal Profile
- `rank(fnd6_mrc4)`: S=0.88, F=0.66, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrc4 / close)`: S=0.79, F=0.54, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrc4, 5))`: S=0.74, F=0.56, T=34.6%, INFERIOR (TOP500)
- `-rank(fnd6_mrc4)`: S=-0.37, F=-0.20, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc4, 5))`: S=-0.20, F=-0.08, T=27.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mrc4, 22)`: S=-0.03, F=0.00, T=23.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrc4, 10)`: S=0.29, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrc4, 22))`: S=0.89, F=0.65, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc4)`: S=0.07, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc4 / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+3.4%
  - 2020: S=0.01 (weak), ret=+0.1%
  - 2021: S=1.20 (moderate), ret=+15.0%
  - 2022: S=1.33 (moderate), ret=+12.0%
  - 2023: S=0.75 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 16.67% over 185 days (recovered)
- Annualized: return +7.1%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.05, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 2.48, latest 0.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.33%; worst month: -4.60%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.75
- Sideways: S=1.34
- Bear: S=-1.98

## Negated Direction
Best negated: `rank(-1 * fnd6_mrc4)` S=0.07, F=0.02, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrc4)`: S=0.07, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc4 / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc4, 5))`: S=-0.20, F=-0.08, T=27.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mrc4)` | TOP3000 | 0.87 | 0.66 | 16.7% | 100% | bull-only |
| `rank(ts_delta(fnd6_mrc4, 5))` | TOP500 | 0.75 | 0.56 | 34.8% | 80% | mixed |
| `rank(fnd6_mrc4 / close)` | TOP3000 | 0.79 | 0.54 | 9.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_mrc4, 5))` | TOP1000 | 0.58 | 0.34 | 40.8% | 60% | weak |
| `rank(fnd6_mrc4 / close)` | TOP1000 | 0.43 | 0.23 | 8.6% | 80% | bull-only |
| `rank(fnd6_mrc4)` | TOP1000 | 0.37 | 0.20 | 22.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_mrc4, 5))` | TOP200 | 0.17 | 0.07 | 50.3% | 60% | weak |
| `rank(fnd6_mrc4 / close)` | TOP500 | 0.14 | 0.05 | 13.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_mrc4, 5))` | TOP3000 | 0.16 | 0.04 | 38.6% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_mrc3: 0.997 (strongly positively correlated)
- fnd6_mrc5: 0.995 (strongly positively correlated)
- fnd6_mrc2: 0.991 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_3y_a: 0.976 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.974 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.42 | 1.73 | +0.73 | -0.43 | yes |
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.67 | +0.65 | -0.88 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.54 | +0.60 | -0.94 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.35 | 1.46 | +0.59 | -0.95 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.33 | 2.58 | +0.56 | -0.42 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
