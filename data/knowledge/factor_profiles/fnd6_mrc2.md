---
field: fnd6_mrc2
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.91
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1774
ann_vol: 0.0879
hit_rate: 0.5263
rolling_sharpe_min: -2.021
rolling_sharpe_max: 2.466
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.85
---
# fnd6_mrc2 (fundamental6)

*Rental Commitments - Minimum - 2nd Year*

## Signal Profile
- `rank(fnd6_mrc2)`: S=0.91, F=0.73, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrc2 / close)`: S=0.91, F=0.68, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrc2, 5))`: S=0.92, F=0.70, T=41.1%, INFERIOR (TOP1000)
- `-rank(fnd6_mrc2)`: S=-0.43, F=-0.26, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc2, 5))`: S=-0.55, F=-0.38, T=27.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrc2, 63)`: S=0.00, F=0.00, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrc2, 10)`: S=0.31, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrc2, 22))`: S=0.78, F=0.53, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc2)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc2 / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+4.1%
  - 2020: S=-0.32 (negative), ret=-1.9%
  - 2021: S=1.19 (moderate), ret=+15.7%
  - 2022: S=1.59 (strong), ret=+16.2%
  - 2023: S=0.79 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 17.74% over 397 days (recovered)
- Annualized: return +8.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.06, excess kurtosis +2.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.02, max 2.47, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.20%; worst month: -4.66%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=1.54
- Bear: S=-2.17

## Negated Direction
Best negated: `rank(-1 * fnd6_mrc2)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrc2)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc2 / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc2, 5))`: S=-0.55, F=-0.38, T=27.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mrc2)` | TOP3000 | 0.91 | 0.73 | 17.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_mrc2, 5))` | TOP1000 | 0.92 | 0.70 | 25.9% | 100% | mixed |
| `rank(fnd6_mrc2 / close)` | TOP3000 | 0.91 | 0.68 | 7.8% | 100% | all-weather |
| `rank(ts_delta(fnd6_mrc2, 5))` | TOP500 | 0.66 | 0.47 | 28.5% | 40% | weak |
| `rank(ts_delta(fnd6_mrc2, 5))` | TOP200 | 0.60 | 0.44 | 33.9% | 80% | mixed |
| `rank(fnd6_mrc2 / close)` | TOP1000 | 0.51 | 0.31 | 9.1% | 80% | bull-only |
| `rank(fnd6_mrc2)` | TOP1000 | 0.42 | 0.26 | 26.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_mrc2, 5))` | TOP3000 | 0.49 | 0.21 | 34.0% | 60% | mixed |
| `rank(fnd6_mrc2 / close)` | TOP500 | 0.18 | 0.07 | 17.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrc3: 0.997 (strongly positively correlated)
- fnd6_mrc4: 0.991 (strongly positively correlated)
- fnd6_mrc5: 0.984 (strongly positively correlated)
- fnd6_xrent: 0.984 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.982 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.38 | 1.73 | +0.70 | -0.94 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.41 | 1.76 | +0.76 | -0.29 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.57 | +0.63 | -0.90 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.35 | 1.50 | +0.60 | -0.95 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.34 | 2.60 | +0.58 | -0.46 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
