---
field: actuals_value_currency_code
dataset: analyst4
cluster: analyst4_other
coverage: 1.0
community_alphas: 2108
best_template: rank_level
best_sharpe: 1.26
best_fitness: 1.04
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SUB_UNIVERSE_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1586
ann_vol: 0.0675
hit_rate: 0.5441
rolling_sharpe_min: -2.356
rolling_sharpe_max: 2.885
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.67
n_negated_sims: 10
direction_gap: -0.52
---
# actuals_value_currency_code (analyst4)

*Pricing Currency where the security trades*

## Signal Profile
- `rank(actuals_value_currency_code)`: S=1.26, F=1.04, T=1.5%, AVERAGE (TOP3000)
- `rank(actuals_value_currency_code / close)`: S=0.78, F=0.56, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(actuals_value_currency_code, 5))`: S=-0.05, F=-0.01, T=15.7%, INFERIOR (TOP500)
- `-rank(actuals_value_currency_code)`: S=-0.48, F=-0.31, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actuals_value_currency_code, 5))`: S=0.74, F=0.67, T=29.9%, INFERIOR (TOP3000)
- `ts_zscore(actuals_value_currency_code, 22)`: S=0.29, F=0.25, T=7.0%, INFERIOR (TOP3000)
- `ts_mean(actuals_value_currency_code, 10)`: S=0.47, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(actuals_value_currency_code, 22))`: S=0.45, F=0.46, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * actuals_value_currency_code)`: S=-1.26, F=-1.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * actuals_value_currency_code / close)`: S=-0.78, F=-0.56, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.25, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.27 (strong), ret=+7.8%
  - 2020: S=-1.92 (negative), ret=-9.2%
  - 2021: S=1.70 (strong), ret=+17.0%
  - 2022: S=2.48 (strong), ret=+20.2%
  - 2023: S=1.36 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 15.86% over 720 days (recovered)
- Annualized: return +8.5%, volatility 6.8% (fraction of booksize)
- Hit rate: 54.4% positive days
- Tail shape: skew +0.04, excess kurtosis +4.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.36, max 2.88, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.79%; worst month: -4.72%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.60
- Sideways: S=1.51
- Bear: S=-0.77

## Negated Direction
Best negated: `rank(-1 * ts_delta(actuals_value_currency_code, 5))` S=0.74, F=0.67, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * actuals_value_currency_code)`: S=-1.26, F=-1.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * actuals_value_currency_code / close)`: S=-0.78, F=-0.56, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actuals_value_currency_code, 5))`: S=0.74, F=0.67, T=29.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actuals_value_currency_code)` | TOP3000 | 1.25 | 1.04 | 15.9% | 80% | bull-only |
| `rank(actuals_value_currency_code / close)` | TOP3000 | 0.78 | 0.56 | 9.7% | 100% | mixed |
| `rank(actuals_value_currency_code / close)` | TOP1000 | 0.62 | 0.39 | 12.7% | 80% | mixed |
| `rank(actuals_value_currency_code / close)` | TOP500 | 0.53 | 0.31 | 15.0% | 60% | all-weather |
| `rank(actuals_value_currency_code)` | TOP1000 | 0.48 | 0.31 | 16.1% | 80% | bull-only |
| `rank(actuals_value_currency_code / close)` | TOP200 | 0.31 | 0.15 | 19.7% | 80% | mixed |
| `rank(actuals_value_currency_code)` | TOP500 | 0.21 | 0.10 | 23.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- rel_num_comp: 0.823 (strongly positively correlated)
- rel_num_all: 0.822 (strongly positively correlated)
- anl4_bvps_flag: 0.776 (strongly positively correlated)
- rel_num_part: 0.757 (strongly positively correlated)
- anl4_netdebt_flag: 0.752 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.27 | 2.38 | +0.75 | -0.63 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.28 | 2.77 | +0.75 | -0.61 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.26 | 2.56 | +0.69 | -0.68 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.20 | 1.92 | +0.66 | -0.79 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.86 | +0.61 | -0.99 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SUB_UNIVERSE_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
