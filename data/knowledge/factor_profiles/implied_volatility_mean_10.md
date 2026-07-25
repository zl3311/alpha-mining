---
field: implied_volatility_mean_10
dataset: option8
cluster: option8_other
coverage: 0.9688
community_alphas: 7077
best_template: ts_mean
best_sharpe: 0.66
best_fitness: 1.33
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1792
ann_vol: 0.1153
hit_rate: 0.5336
rolling_sharpe_min: 0.209
rolling_sharpe_max: 2.628
top_merge_partner: fnd6_newqv1300_dpactq
redundancy_cluster: 15
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.68
---
# implied_volatility_mean_10 (option8)

*The average of IvCall10 and IvPut10*

## Signal Profile
- `rank(implied_volatility_mean_10)`: S=0.36, F=0.29, T=12.2%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_10 / close)`: S=0.11, F=0.04, T=5.7%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_10, 5))`: S=1.23, F=0.70, T=43.3%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_10)`: S=-0.16, F=-0.08, T=11.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_10, 5))`: S=-1.20, F=-0.40, T=56.4%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_10, 22)`: S=0.82, F=0.35, T=33.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_10, 10)`: S=0.66, F=1.33, T=2.9%, AVERAGE (TOP3000)
- `rank(ts_rank(implied_volatility_mean_10, 22))`: S=0.66, F=0.22, T=35.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_10)`: S=-0.07, F=-0.02, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_10 / close)`: S=-0.02, F=0.00, T=8.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 20F/1P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.22, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.27 (moderate), ret=+8.0%
  - 2020: S=1.86 (strong), ret=+19.8%
  - 2021: S=0.49 (weak), ret=+6.7%
  - 2022: S=1.57 (strong), ret=+22.7%
  - 2023: S=1.22 (moderate), ret=+11.8%

## Risk & Drawdown
- Max drawdown: 17.92% over 298 days (recovered)
- Annualized: return +14.1%, volatility 11.5% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +0.48, excess kurtosis +4.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.21, max 2.63, latest 1.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.67%; worst month: -8.42%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.04
- Sideways: S=1.44
- Bear: S=1.29

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_10 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_10)`: S=-0.07, F=-0.02, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_10 / close)`: S=-0.02, F=0.00, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_10, 5))`: S=-1.20, F=-0.40, T=56.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_10, 5))` | TOP200 | 1.22 | 0.70 | 17.9% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_mean_10, 5))` | TOP1000 | 1.17 | 0.50 | 9.8% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_mean_10, 5))` | TOP3000 | 1.21 | 0.40 | 5.3% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_mean_10, 5))` | TOP500 | 0.91 | 0.38 | 12.9% | 100% | all-weather |
| `rank(implied_volatility_mean_10)` | TOP200 | 0.36 | 0.29 | 73.6% | 60% | bear-only |
| `rank(implied_volatility_mean_10)` | TOP500 | 0.23 | 0.14 | 73.4% | 40% | bear-only |
| `rank(implied_volatility_mean_10)` | TOP1000 | 0.17 | 0.08 | 66.5% | 40% | bear-only |
| `rank(implied_volatility_mean_10)` | TOP3000 | 0.07 | 0.02 | 69.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_10: 0.989 (strongly positively correlated)
- implied_volatility_call_10: 0.980 (strongly positively correlated)
- implied_volatility_mean_20: 0.782 (strongly positively correlated)
- implied_volatility_put_20: 0.771 (strongly positively correlated)
- implied_volatility_call_20: 0.560 (moderately positively correlated)

Redundancy cluster #15: 5 similar fields, mean |rho| 0.853 (representative: implied_volatility_put_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.12 | 1.88 | +0.59 | -0.64 | yes |
| fnd6_city | fundamental_rare_event | -0.15 | 2.14 | +0.59 | -0.55 | yes |
| fnd6_fate | fundamental_capital_intensity | -0.10 | 1.83 | +0.58 | -0.49 | yes |
| fnd6_newqv1300_ppegtq | fundamental6 | -0.08 | 1.81 | +0.56 | -0.73 | yes |
| rel_num_all | pv13 | -0.12 | 1.79 | +0.57 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
