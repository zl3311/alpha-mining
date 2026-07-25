---
field: min_adjusted_net_income_guidance
dataset: analyst4
best_template: decay_linear
best_sharpe: 2.23
best_fitness: 2.44
best_universe: TOP3000
grade: EXCELLENT
submittability: potentially_submittable
n_sims: 38
regime_profile: all-weather
n_variations_with_pnl: 12
max_drawdown: 0.0987
ann_vol: 0.0804
hit_rate: 0.5401
rolling_sharpe_min: -1.547
rolling_sharpe_max: 4.292
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -1.81
---
# min_adjusted_net_income_guidance (analyst4)

*Adjusted net income - minimum guidance value*

## Signal Profile
- `rank(min_adjusted_net_income_guidance)`: S=1.50, F=1.11, T=1.0%, AVERAGE (TOP3000)
- `rank(min_adjusted_net_income_guidance / close)`: S=0.21, F=0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_adjusted_net_income_guidance, 5))`: S=0.78, F=0.35, T=33.8%, INFERIOR (TOP200)
- `ts_decay_linear(rank(min_adjusted_net_income_guidance) * 2 + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 5)`: S=2.23, F=2.44, T=14.9%, EXCELLENT (TOP3000)
- `-rank(min_adjusted_net_income_guidance)`: S=-0.94, F=-0.63, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_adjusted_net_income_guidance, 5))`: S=-0.78, F=-0.35, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(min_adjusted_net_income_guidance, 22)`: S=0.27, F=0.06, T=42.4%, INFERIOR (TOP3000)
- `ts_mean(min_adjusted_net_income_guidance, 10)`: S=0.95, F=0.64, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(min_adjusted_net_income_guidance, 22))`: S=0.03, F=0.00, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_net_income_guidance)`: S=0.42, F=0.29, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_net_income_guidance / close)`: S=0.27, F=0.13, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/29P
- LOW_FITNESS: 31F/7P
- LOW_SHARPE: 31F/7P
- LOW_SUB_UNIVERSE_SHARPE: 14F/12P
- LOW_TURNOVER: 1F/37P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 2.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.21 (negative), ret=-1.2%
  - 2020: S=1.22 (moderate), ret=+10.4%
  - 2021: S=3.64 (strong), ret=+35.2%
  - 2022: S=3.81 (strong), ret=+32.1%
  - 2023: S=1.71 (strong), ret=+10.5%

## Risk & Drawdown
- Max drawdown: 9.87% over 469 days (recovered)
- Annualized: return +17.8%, volatility 8.0% (fraction of booksize)
- Hit rate: 54.0% positive days
- Tail shape: skew +0.42, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 4.29, latest 1.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.99%; worst month: -5.14%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=4.74
- Sideways: S=0.53
- Bear: S=1.24

## Negated Direction
Best negated: `rank(-1 * min_adjusted_net_income_guidance)` S=0.42, F=0.29, INFERIOR
Direction gap: -1.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_adjusted_net_income_guidance)`: S=0.42, F=0.29, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_net_income_guidance / close)`: S=0.27, F=0.13, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_adjusted_net_income_guidance, 5))`: S=-0.78, F=-0.35, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) * 2 + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 5)` | TOP3000 | 2.21 | 2.44 | 9.9% | 80% | all-weather |
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 7)` | TOP3000 | 2.09 | 2.40 | 10.5% | 100% | all-weather |
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(ts_delta(anl4_ffo_flag, 5)) * 2 + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 5)` | TOP3000 | 2.21 | 2.38 | 10.4% | 80% | all-weather |
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 10)` | TOP3000 | 1.96 | 2.34 | 10.5% | 100% | all-weather |
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 2)` | TOP3000 | 2.43 | 2.27 | 10.3% | 80% | all-weather |
| `ts_decay_linear(rank(min_adjusted_net_income_guidance) + rank(ts_delta(anl4_ffo_flag, 5)) + rank(fnd6_fate / close) * 2 + rank(ts_mean(anl4_netdebt_flag, 5) * (-1 * returns)), 5)` | TOP3000 | 1.86 | 2.24 | 11.0% | 100% | mixed |
| `rank(min_adjusted_net_income_guidance)` | TOP3000 | 1.50 | 1.11 | 3.9% | 100% | all-weather |
| `rank(min_adjusted_net_income_guidance)` | TOP1000 | 0.95 | 0.63 | 4.8% | 80% | mixed |
| `rank(ts_delta(min_adjusted_net_income_guidance, 5))` | TOP200 | 0.80 | 0.35 | 12.8% | 60% | mixed |
| `rank(min_adjusted_net_income_guidance)` | TOP500 | 0.30 | 0.13 | 16.9% | 60% | mixed |
| `rank(min_adjusted_net_income_guidance / close)` | TOP3000 | 0.21 | 0.09 | 44.6% | 60% | bull-only |
| `rank(min_adjusted_net_income_guidance / close)` | TOP1000 | 0.16 | 0.06 | 33.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_fate: 0.760 (strongly positively correlated)
- fnd6_ppeveb: 0.722 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.721 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.721 (strongly positively correlated)
- debt: 0.720 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.28 | 2.70 | +0.49 | -0.51 | yes |
| fnd6_itci | fundamental_tax_credit | +0.22 | 2.68 | +0.47 | -0.23 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | +0.23 | 2.68 | +0.47 | +0.21 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.03 | 2.59 | +0.38 | -0.74 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.03 | 2.59 | +0.38 | -0.74 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Passes all non-self-corr checks. Candidate for submission pending self-corr verification.
Untried templates: trade_when
