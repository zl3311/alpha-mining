---
field: fnd6_cld3
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.27
best_fitness: 0.93
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0646
ann_vol: 0.0528
hit_rate: 0.5287
rolling_sharpe_min: -0.185
rolling_sharpe_max: 3.251
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 14
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_cld3 (fundamental6)

*Capitalized Leases - Due in 3rd Year*

## Signal Profile
- `rank(fnd6_cld3)`: S=0.93, F=0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_cld3 / close)`: S=1.27, F=0.93, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cld3, 5))`: S=-0.01, F=0.00, T=32.8%, INFERIOR (TOP1000)
- `-rank(fnd6_cld3)`: S=-0.56, F=-0.31, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld3, 5))`: S=0.59, F=0.34, T=41.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cld3, 63)`: S=0.64, F=0.69, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cld3, 10)`: S=0.64, F=0.52, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cld3, 22))`: S=0.06, F=0.01, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld3)`: S=-0.93, F=-0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld3 / close)`: S=-1.27, F=-0.93, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.27, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+2.9%
  - 2020: S=1.31 (moderate), ret=+7.8%
  - 2021: S=2.10 (strong), ret=+12.2%
  - 2022: S=1.50 (moderate), ret=+9.0%
  - 2023: S=0.22 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 6.46% over 252 days (recovered)
- Annualized: return +6.7%, volatility 5.3% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +0.36, excess kurtosis +1.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.18, max 3.25, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.20%; worst month: -2.22%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.43
- Sideways: S=1.36
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cld3, 5))` S=0.59, F=0.34, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cld3)`: S=-0.93, F=-0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld3 / close)`: S=-1.27, F=-0.93, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld3, 5))`: S=0.59, F=0.34, T=41.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cld3 / close)` | TOP3000 | 1.27 | 0.93 | 6.5% | 100% | mixed |
| `rank(fnd6_cld3)` | TOP3000 | 0.92 | 0.66 | 9.9% | 100% | bull-only |
| `rank(fnd6_cld3)` | TOP500 | 0.66 | 0.44 | 21.9% | 80% | bull-only |
| `rank(fnd6_cld3 / close)` | TOP500 | 0.55 | 0.32 | 12.3% | 60% | mixed |
| `rank(fnd6_cld3)` | TOP1000 | 0.56 | 0.31 | 18.3% | 80% | bull-only |
| `rank(fnd6_cld3 / close)` | TOP1000 | 0.52 | 0.27 | 10.3% | 80% | bull-only |
| `rank(fnd6_cld3)` | TOP200 | 0.40 | 0.27 | 40.5% | 80% | bull-only |
| `rank(fnd6_cld3 / close)` | TOP200 | 0.31 | 0.18 | 33.7% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cld2: 0.953 (strongly positively correlated)
- fnd6_dclo: 0.700 (moderately positively correlated)
- fnd6_newa1v1300_dltt: 0.682 (moderately positively correlated)
- debt_lt: 0.679 (moderately positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.679 (moderately positively correlated)

Redundancy cluster #14: 2 similar fields, mean |rho| 0.953 (representative: fnd6_cld2). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.20 | 1.79 | +0.52 | -0.81 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.08 | 2.12 | +0.50 | -0.67 | yes |
| implied_volatility_call_120 | option8 | -0.07 | 1.96 | +0.56 | +0.87 | yes |
| implied_volatility_call_20 | option8 | -0.06 | 1.83 | +0.55 | +0.50 | yes |
| implied_volatility_mean_60 | option8 | -0.05 | 1.88 | +0.55 | +0.91 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
