---
field: fnd6_rank
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.15
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0445
ann_vol: 0.0336
hit_rate: 0.5158
rolling_sharpe_min: -0.54
rolling_sharpe_max: 3.524
top_merge_partner: anl4_epsr_number
negated_best_sharpe: -0.47
negated_best_template: neg_rank
negated_best_fitness: -0.19
n_negated_sims: 10
direction_gap: -1.62
---
# fnd6_rank (fundamental6)

*SP rank with the following meaning: // 0----invalid rank //1----A+//2----A//3----A-//4----B+//5----B//6----B-//7----C+//8----C//9----C-*

## Signal Profile
- `rank(fnd6_rank)`: S=1.15, F=0.64, T=0.6%, INFERIOR (TOP3000)
- `rank(fnd6_rank / close)`: S=0.85, F=0.51, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_rank, 5))`: S=0.24, F=0.11, T=3.8%, INFERIOR (TOP200)
- `-rank(fnd6_rank)`: S=-0.47, F=-0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_rank, 5))`: S=-0.71, F=-0.55, T=3.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_rank, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_rank, 10)`: S=0.51, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_rank, 22))`: S=-0.71, F=-0.55, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rank)`: S=-0.47, F=-0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rank / close)`: S=-0.53, F=-0.26, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/9P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.16, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.4%
  - 2020: S=0.38 (weak), ret=+1.4%
  - 2021: S=1.82 (strong), ret=+6.6%
  - 2022: S=0.47 (weak), ret=+1.6%
  - 2023: S=3.07 (strong), ret=+9.2%

## Risk & Drawdown
- Max drawdown: 4.45% over 244 days (recovered)
- Annualized: return +3.9%, volatility 3.4% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.23, excess kurtosis +2.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 3.52, latest 3.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +4.10%; worst month: -2.66%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.99
- Sideways: S=0.46
- Bear: S=1.92

## Negated Direction
Best negated: `-rank(fnd6_rank)` S=-0.47, F=-0.19, INFERIOR
Direction gap: -1.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_rank)`: S=-0.47, F=-0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rank / close)`: S=-0.53, F=-0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_rank, 5))`: S=-0.71, F=-0.55, T=3.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_rank)` | TOP3000 | 1.16 | 0.64 | 4.5% | 100% | all-weather |
| `rank(fnd6_rank / close)` | TOP3000 | 0.86 | 0.51 | 6.3% | 100% | all-weather |
| `rank(fnd6_rank / close)` | TOP1000 | 0.53 | 0.26 | 12.8% | 60% | mixed |
| `rank(fnd6_rank)` | TOP1000 | 0.48 | 0.19 | 9.2% | 60% | mixed |
| `rank(ts_delta(fnd6_rank, 5))` | TOP200 | 0.23 | 0.11 | 14.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_rank, 5))` | TOP500 | 0.19 | 0.08 | 20.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptrank_gvkeymap: 0.530 (moderately positively correlated)
- fnd2_propplteqmuflmblgland: 0.498 (moderately positively correlated)
- fnd6_beta: 0.482 (moderately positively correlated)
- anl4_qf_az_div_number: 0.463 (moderately positively correlated)
- anl4_qfd1_az_div_number: 0.463 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_number | analyst4 | -0.16 | 1.79 | +0.60 | -0.92 | yes |
| rel_num_part | pv13 | -0.28 | 1.91 | +0.64 | +0.10 | yes |
| anl4_netprofit_number | analyst4 | -0.19 | 1.82 | +0.63 | +0.08 | yes |
| anl4_qfd1_az_eps_number | analyst4 | -0.22 | 1.97 | +0.61 | -0.24 | yes |
| pcr_vol_30 | option9 | -0.21 | 1.79 | +0.63 | +0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
