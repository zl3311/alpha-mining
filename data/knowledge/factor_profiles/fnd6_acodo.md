---
field: fnd6_acodo
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0546
ann_vol: 0.0612
hit_rate: 0.5036
rolling_sharpe_min: -0.779
rolling_sharpe_max: 2.856
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_acodo (fundamental6)

*Other Current Assets Excl Discontinued Operations*

## Signal Profile
- `rank(fnd6_acodo)`: S=0.67, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_acodo / close)`: S=0.99, F=0.69, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_acodo, 5))`: S=0.46, F=0.24, T=34.8%, INFERIOR (TOP200)
- `-rank(fnd6_acodo)`: S=-0.27, F=-0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acodo, 5))`: S=-0.40, F=-0.19, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_acodo, 63)`: S=0.79, F=0.54, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_acodo, 10)`: S=-0.35, F=-0.19, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_acodo, 22))`: S=0.62, F=0.33, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acodo)`: S=0.43, F=0.32, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acodo / close)`: S=0.31, F=0.17, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+1.8%
  - 2020: S=-0.17 (negative), ret=-1.1%
  - 2021: S=1.86 (strong), ret=+15.5%
  - 2022: S=1.93 (strong), ret=+11.6%
  - 2023: S=0.42 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 5.46% over 215 days (recovered)
- Annualized: return +6.0%, volatility 6.1% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.47, excess kurtosis +3.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.78, max 2.86, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.57%; worst month: -2.66%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=0.23
- Bear: S=-0.73

## Negated Direction
Best negated: `rank(-1 * fnd6_acodo)` S=0.43, F=0.32, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_acodo)`: S=0.43, F=0.32, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acodo / close)`: S=0.31, F=0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acodo, 5))`: S=-0.40, F=-0.19, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_acodo / close)` | TOP3000 | 0.99 | 0.69 | 5.5% | 80% | bull-only |
| `rank(fnd6_acodo)` | TOP3000 | 0.67 | 0.47 | 27.5% | 80% | bull-only |
| `rank(fnd6_acodo / close)` | TOP1000 | 0.46 | 0.26 | 13.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_acodo, 5))` | TOP200 | 0.46 | 0.24 | 54.7% | 80% | bear-only |
| `rank(fnd6_acodo / close)` | TOP500 | 0.38 | 0.21 | 25.3% | 40% | bull-only |
| `rank(ts_delta(fnd6_acodo, 5))` | TOP1000 | 0.52 | 0.20 | 17.0% | 60% | bear-only |
| `rank(fnd6_acodo)` | TOP1000 | 0.27 | 0.13 | 31.9% | 60% | bull-only |
| `rank(fnd6_acodo)` | TOP500 | 0.07 | 0.02 | 47.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_acox: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_aco: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.942 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.938 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.938 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 1.80 | +0.62 | -0.77 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.51 | +0.53 | -0.83 | yes |
| anl4_rd_exp_flag | analyst4 | -0.22 | 1.54 | +0.52 | -0.68 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.17 | 1.47 | +0.48 | -0.88 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.15 | 2.05 | +0.43 | -0.59 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
