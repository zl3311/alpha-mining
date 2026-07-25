---
field: fnd6_mrc3
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.04
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.1691
ann_vol: 0.0846
hit_rate: 0.5231
rolling_sharpe_min: -1.809
rolling_sharpe_max: 2.487
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 13
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.98
---
# fnd6_mrc3 (fundamental6)

*Rental Commitments - Minimum - 3rd Year*

## Signal Profile
- `rank(fnd6_mrc3)`: S=0.90, F=0.70, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrc3 / close)`: S=0.87, F=0.63, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrc3, 5))`: S=0.80, F=0.64, T=34.4%, INFERIOR (TOP500)
- `-rank(fnd6_mrc3)`: S=-0.41, F=-0.24, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc3, 5))`: S=-0.68, F=-0.52, T=27.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrc3, 63)`: S=0.32, F=0.17, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrc3, 10)`: S=0.32, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrc3, 22))`: S=1.04, F=0.80, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc3)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc3 / close)`: S=-0.07, F=-0.02, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.90, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+3.3%
  - 2020: S=0.00 (weak), ret=+0.0%
  - 2021: S=1.22 (moderate), ret=+15.7%
  - 2022: S=1.36 (moderate), ret=+13.1%
  - 2023: S=0.86 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 16.91% over 185 days (recovered)
- Annualized: return +7.6%, volatility 8.5% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.06, excess kurtosis +3.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 2.49, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.74%; worst month: -4.62%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.77
- Sideways: S=1.43
- Bear: S=-2.00

## Negated Direction
Best negated: `rank(-1 * fnd6_mrc3)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrc3)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc3 / close)`: S=-0.07, F=-0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc3, 5))`: S=-0.68, F=-0.52, T=27.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mrc3)` | TOP3000 | 0.90 | 0.70 | 16.9% | 100% | bull-only |
| `rank(ts_delta(fnd6_mrc3, 5))` | TOP500 | 0.81 | 0.64 | 27.9% | 80% | mixed |
| `rank(ts_delta(fnd6_mrc3, 5))` | TOP1000 | 0.88 | 0.63 | 26.5% | 60% | mixed |
| `rank(fnd6_mrc3 / close)` | TOP3000 | 0.86 | 0.63 | 9.2% | 80% | all-weather |
| `rank(ts_delta(fnd6_mrc3, 5))` | TOP200 | 0.70 | 0.55 | 39.3% | 80% | mixed |
| `rank(fnd6_mrc3 / close)` | TOP1000 | 0.52 | 0.31 | 8.7% | 100% | bull-only |
| `rank(ts_delta(fnd6_mrc3, 5))` | TOP3000 | 0.58 | 0.28 | 42.0% | 80% | mixed |
| `rank(fnd6_mrc3)` | TOP1000 | 0.41 | 0.24 | 24.3% | 60% | bull-only |
| `rank(fnd6_mrc3 / close)` | TOP500 | 0.18 | 0.07 | 14.7% | 60% | bull-only |
| `rank(fnd6_mrc3 / close)` | TOP200 | 0.07 | 0.02 | 19.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrc4: 0.997 (strongly positively correlated)
- fnd6_mrc2: 0.997 (strongly positively correlated)
- fnd6_mrc5: 0.991 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_3y_a: 0.980 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.979 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.42 | 1.75 | +0.75 | -0.40 | yes |
| anl4_rd_exp_flag | analyst4 | -0.37 | 1.71 | +0.68 | -0.87 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.57 | +0.62 | -0.92 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.35 | 1.49 | +0.60 | -0.95 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.34 | 2.60 | +0.58 | -0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
