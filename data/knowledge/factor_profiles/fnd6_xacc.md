---
field: fnd6_xacc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.91
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.079
ann_vol: 0.0754
hit_rate: 0.4883
rolling_sharpe_min: -0.899
rolling_sharpe_max: 2.514
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.53
---
# fnd6_xacc (fundamental6)

*Accrued Expenses*

## Signal Profile
- `rank(fnd6_xacc)`: S=0.63, F=0.47, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_xacc / close)`: S=0.86, F=0.62, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xacc, 5))`: S=0.31, F=0.14, T=33.2%, INFERIOR (TOP200)
- `-rank(fnd6_xacc)`: S=-0.30, F=-0.17, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xacc, 5))`: S=0.38, F=0.16, T=37.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_xacc, 63)`: S=0.91, F=0.77, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xacc, 10)`: S=0.10, F=0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xacc, 22))`: S=0.15, F=0.04, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xacc)`: S=-0.05, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xacc / close)`: S=-0.13, F=-0.04, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.4%
  - 2020: S=0.70 (moderate), ret=+5.8%
  - 2021: S=1.54 (strong), ret=+14.3%
  - 2022: S=1.05 (moderate), ret=+7.7%
  - 2023: S=0.53 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 7.90% over 236 days (recovered)
- Annualized: return +6.4%, volatility 7.5% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.48, excess kurtosis +2.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.51, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.94%; worst month: -3.55%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.64
- Sideways: S=-0.09
- Bear: S=-0.51

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_xacc, 5))` S=0.38, F=0.16, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_xacc)`: S=-0.05, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xacc / close)`: S=-0.13, F=-0.04, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xacc, 5))`: S=0.38, F=0.16, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xacc / close)` | TOP3000 | 0.85 | 0.62 | 7.9% | 100% | bull-only |
| `rank(fnd6_xacc)` | TOP3000 | 0.63 | 0.47 | 28.8% | 80% | bull-only |
| `rank(fnd6_xacc / close)` | TOP1000 | 0.49 | 0.31 | 11.8% | 60% | bull-only |
| `rank(fnd6_xacc)` | TOP1000 | 0.29 | 0.17 | 34.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_xacc, 5))` | TOP200 | 0.31 | 0.14 | 62.8% | 80% | mixed |
| `rank(fnd6_xacc / close)` | TOP500 | 0.13 | 0.04 | 27.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lco: 0.964 (strongly positively correlated)
- fnd6_xopr: 0.962 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.961 (strongly positively correlated)
- fnd6_xaccq: 0.958 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.957 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.78 | +0.61 | -0.66 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.49 | +0.60 | -0.61 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.34 | +0.49 | -0.97 | yes |
| min_gross_income_guidance | analyst4 | -0.21 | 1.34 | +0.47 | -0.57 | yes |
| max_gross_income_guidance | analyst4 | -0.21 | 1.35 | +0.47 | -0.56 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
