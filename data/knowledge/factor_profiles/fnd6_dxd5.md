---
field: fnd6_dxd5
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.19
best_fitness: 0.84
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0639
ann_vol: 0.0526
hit_rate: 0.5174
rolling_sharpe_min: -0.329
rolling_sharpe_max: 2.761
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: -0.23
negated_best_template: neg_rank
negated_best_fitness: -0.08
n_negated_sims: 4
direction_gap: -1.42
---
# fnd6_dxd5 (fundamental6)

*Debt (excl Capitalized Leases) - Due in 5th Year*

## Signal Profile
- `rank(fnd6_dxd5)`: S=0.91, F=0.59, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_dxd5 / close)`: S=1.19, F=0.84, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dxd5, 5))`: S=0.92, F=0.56, T=41.7%, INFERIOR (TOP3000)
- `-rank(fnd6_dxd5)`: S=-0.23, F=-0.08, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd5, 5))`: S=-0.85, F=-0.50, T=41.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dxd5, 63)`: S=0.35, F=0.21, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dxd5, 10)`: S=0.19, F=0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dxd5, 22))`: S=-0.18, F=-0.06, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd5)`: S=-0.91, F=-0.59, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd5 / close)`: S=-1.19, F=-0.84, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.19, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.26 (moderate), ret=+3.6%
  - 2020: S=0.57 (moderate), ret=+3.0%
  - 2021: S=1.38 (moderate), ret=+9.7%
  - 2022: S=1.81 (strong), ret=+10.8%
  - 2023: S=0.98 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 6.39% over 118 days (recovered)
- Annualized: return +6.2%, volatility 5.3% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.15, excess kurtosis +2.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.33, max 2.76, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.72%; worst month: -2.88%
Positive months: 73%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.31
- Sideways: S=1.39
- Bear: S=-1.50

## Negated Direction
Best negated: `-rank(fnd6_dxd5)` S=-0.23, F=-0.08, INFERIOR
Direction gap: -1.42 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dxd5)`: S=-0.91, F=-0.59, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd5 / close)`: S=-1.19, F=-0.84, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd5, 5))`: S=-0.85, F=-0.50, T=41.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dxd5 / close)` | TOP3000 | 1.19 | 0.84 | 6.4% | 100% | bull-only |
| `rank(fnd6_dxd5)` | TOP3000 | 0.90 | 0.59 | 9.8% | 80% | bull-only |
| `rank(ts_delta(fnd6_dxd5, 5))` | TOP3000 | 0.92 | 0.56 | 21.5% | 60% | all-weather |
| `rank(ts_delta(fnd6_dxd5, 5))` | TOP500 | 0.62 | 0.41 | 21.1% | 80% | mixed |
| `rank(ts_delta(fnd6_dxd5, 5))` | TOP1000 | 0.67 | 0.38 | 31.5% | 80% | all-weather |
| `rank(fnd6_dxd5 / close)` | TOP500 | 0.41 | 0.22 | 14.4% | 60% | bull-only |
| `rank(fnd6_dxd5 / close)` | TOP1000 | 0.35 | 0.16 | 9.6% | 40% | bull-only |
| `rank(fnd6_dxd5)` | TOP500 | 0.32 | 0.16 | 18.5% | 40% | bull-only |
| `rank(fnd6_dxd5)` | TOP1000 | 0.21 | 0.08 | 15.9% | 40% | bull-only |
| `rank(fnd6_dxd5)` | TOP200 | 0.12 | 0.05 | 29.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd5: 0.981 (strongly positively correlated)
- fnd6_dd4: 0.888 (strongly positively correlated)
- fnd6_dd3: 0.888 (strongly positively correlated)
- fnd6_dxd4: 0.883 (strongly positively correlated)
- fnd6_dxd3: 0.878 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.78 | +0.59 | -0.91 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.35 | 1.81 | +0.62 | -0.54 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.14 | 1.79 | +0.60 | -0.72 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.21 | 2.22 | +0.59 | -0.67 | yes |
| anl4_epsr_flag | analyst4 | -0.24 | 1.78 | +0.60 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
