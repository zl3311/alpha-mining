---
field: fnd6_fate
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.26
best_fitness: 1.24
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SUB_UNIVERSE_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1032
ann_vol: 0.0969
hit_rate: 0.5045
rolling_sharpe_min: -1.028
rolling_sharpe_max: 2.931
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.71
---
# fnd6_fate (fundamental6)

*Plant, Property and Equipment at Cost - Machinery & Equipment*

## Signal Profile
- `rank(fnd6_fate)`: S=0.87, F=0.85, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_fate / close)`: S=1.26, F=1.24, T=2.3%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_fate, 5))`: S=-0.10, F=-0.02, T=35.5%, INFERIOR (TOP1000)
- `-rank(fnd6_fate)`: S=-0.50, F=-0.40, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fate, 5))`: S=0.55, F=0.29, T=39.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fate, 63)`: S=0.15, F=0.07, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fate, 10)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fate, 22))`: S=0.31, F=0.16, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fate)`: S=-0.87, F=-0.85, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fate / close)`: S=-1.26, F=-1.24, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.25, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.5%
  - 2020: S=0.17 (weak), ret=+1.7%
  - 2021: S=2.04 (strong), ret=+27.0%
  - 2022: S=2.12 (strong), ret=+22.5%
  - 2023: S=1.43 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 10.32% over 194 days (recovered)
- Annualized: return +12.1%, volatility 9.7% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.43, excess kurtosis +2.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 2.93, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +11.17%; worst month: -3.98%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.40
- Sideways: S=0.70
- Bear: S=-1.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fate, 5))` S=0.55, F=0.29, INFERIOR
Direction gap: -0.71 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fate)`: S=-0.87, F=-0.85, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fate / close)`: S=-1.26, F=-1.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fate, 5))`: S=0.55, F=0.29, T=39.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fate / close)` | TOP3000 | 1.25 | 1.24 | 10.3% | 100% | bull-only |
| `rank(fnd6_fate)` | TOP3000 | 0.86 | 0.85 | 28.9% | 80% | bull-only |
| `rank(fnd6_fate / close)` | TOP1000 | 0.67 | 0.56 | 16.9% | 60% | bull-only |
| `rank(fnd6_fate)` | TOP1000 | 0.50 | 0.40 | 38.9% | 60% | bull-only |
| `rank(fnd6_fate / close)` | TOP500 | 0.42 | 0.29 | 36.3% | 60% | bull-only |
| `rank(fnd6_fate / close)` | TOP200 | 0.22 | 0.13 | 45.8% | 60% | bull-only |
| `rank(fnd6_fate)` | TOP500 | 0.21 | 0.12 | 59.3% | 60% | bull-only |
| `rank(fnd6_fate)` | TOP200 | 0.06 | 0.02 | 63.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ppeveb: 0.963 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.962 (strongly positively correlated)
- fnd6_dpvieb: 0.957 (strongly positively correlated)
- fnd6_newa1v1300_dpact: 0.955 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.944 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 2.08 | +0.84 | -0.50 | yes |
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.98 | +0.74 | -0.49 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.90 | +0.66 | -0.71 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.20 | 2.26 | +0.64 | -0.13 | yes |
| implied_volatility_put_10 | option8 | -0.10 | 1.89 | +0.59 | -0.38 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SUB_UNIVERSE_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
