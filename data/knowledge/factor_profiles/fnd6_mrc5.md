---
field: fnd6_mrc5
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.86
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.1624
ann_vol: 0.0784
hit_rate: 0.5134
rolling_sharpe_min: -2.078
rolling_sharpe_max: 2.434
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 13
negated_best_sharpe: -0.41
negated_best_template: neg_rank
negated_best_fitness: -0.22
n_negated_sims: 4
direction_gap: -1.27
---
# fnd6_mrc5 (fundamental6)

*Rental Commitments - Minimum - 5th Year*

## Signal Profile
- `rank(fnd6_mrc5)`: S=0.86, F=0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrc5 / close)`: S=0.80, F=0.54, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrc5, 5))`: S=0.84, F=0.59, T=39.4%, INFERIOR (TOP1000)
- `-rank(fnd6_mrc5)`: S=-0.41, F=-0.22, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc5, 5))`: S=-0.73, F=-0.39, T=43.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrc5, 63)`: S=-0.04, F=-0.01, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrc5, 10)`: S=0.37, F=0.19, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrc5, 22))`: S=0.66, F=0.40, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc5)`: S=-0.86, F=-0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc5 / close)`: S=-0.80, F=-0.54, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+3.5%
  - 2020: S=-0.23 (negative), ret=-1.2%
  - 2021: S=1.15 (moderate), ret=+13.9%
  - 2022: S=1.22 (moderate), ret=+10.6%
  - 2023: S=1.09 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 16.24% over 492 days (recovered)
- Annualized: return +6.7%, volatility 7.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.04, excess kurtosis +3.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.08, max 2.43, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.30%; worst month: -4.50%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.81
- Sideways: S=1.37
- Bear: S=-2.17

## Negated Direction
Best negated: `-rank(fnd6_mrc5)` S=-0.41, F=-0.22, INFERIOR
Direction gap: -1.27 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrc5)`: S=-0.86, F=-0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc5 / close)`: S=-0.80, F=-0.54, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc5, 5))`: S=-0.73, F=-0.39, T=43.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mrc5)` | TOP3000 | 0.85 | 0.63 | 16.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_mrc5, 5))` | TOP1000 | 0.84 | 0.59 | 23.8% | 80% | all-weather |
| `rank(fnd6_mrc5 / close)` | TOP3000 | 0.80 | 0.54 | 8.8% | 60% | mixed |
| `rank(ts_delta(fnd6_mrc5, 5))` | TOP3000 | 0.78 | 0.44 | 16.3% | 100% | all-weather |
| `rank(fnd6_mrc5)` | TOP1000 | 0.40 | 0.22 | 21.8% | 60% | bull-only |
| `rank(fnd6_mrc5 / close)` | TOP1000 | 0.38 | 0.19 | 9.0% | 100% | bull-only |
| `rank(ts_delta(fnd6_mrc5, 5))` | TOP500 | 0.35 | 0.18 | 48.5% | 60% | weak |
| `rank(ts_delta(fnd6_mrc5, 5))` | TOP200 | 0.20 | 0.08 | 42.6% | 80% | mixed |
| `rank(fnd6_mrc5 / close)` | TOP500 | 0.15 | 0.05 | 14.8% | 60% | bull-only |
| `rank(fnd6_mrc5)` | TOP200 | 0.10 | 0.04 | 40.3% | 60% | bull-only |
| `rank(fnd6_mrc5 / close)` | TOP200 | 0.10 | 0.03 | 20.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrc4: 0.995 (strongly positively correlated)
- fnd6_mrc3: 0.991 (strongly positively correlated)
- fnd6_mrc2: 0.984 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_3y_a: 0.969 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.966 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.41 | 1.70 | +0.70 | -0.19 | yes |
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.65 | +0.62 | -0.88 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.34 | 1.43 | +0.58 | -0.96 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.30 | 1.52 | +0.58 | -0.87 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.33 | 2.57 | +0.55 | -0.31 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
