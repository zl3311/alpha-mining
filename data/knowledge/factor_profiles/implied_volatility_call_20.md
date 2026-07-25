---
field: implied_volatility_call_20
dataset: option8
best_template: rank_delta
best_sharpe: 1.26
best_fitness: 0.54
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0896
ann_vol: 0.0681
hit_rate: 0.5239
rolling_sharpe_min: 0.147
rolling_sharpe_max: 2.724
top_merge_partner: fnd6_newqv1300_dpactq
redundancy_cluster: 20
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.26
---
# implied_volatility_call_20 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 20 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_20)`: S=0.36, F=0.30, T=10.6%, INFERIOR (TOP200)
- `rank(implied_volatility_call_20 / close)`: S=0.12, F=0.05, T=5.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_20, 5))`: S=1.26, F=0.54, T=46.9%, INFERIOR (TOP1000)
- `-rank(implied_volatility_call_20)`: S=-0.16, F=-0.08, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_20, 5))`: S=-1.42, F=-0.49, T=57.8%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_20, 22)`: S=0.93, F=0.42, T=31.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_20, 10)`: S=0.02, F=0.00, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_20, 22))`: S=0.83, F=0.32, T=33.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_20)`: S=-0.07, F=-0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_20 / close)`: S=0.00, F=0.00, T=7.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 17F/4P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.26, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.40 (moderate), ret=+5.4%
  - 2020: S=1.94 (strong), ret=+10.2%
  - 2021: S=1.00 (moderate), ret=+8.4%
  - 2022: S=1.79 (strong), ret=+16.3%
  - 2023: S=0.31 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 8.96% over 206 days (recovered)
- Annualized: return +8.6%, volatility 6.8% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.95, excess kurtosis +5.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.15, max 2.72, latest 0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.69%; worst month: -6.20%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.58
- Sideways: S=1.02
- Bear: S=1.12

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_20 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.26 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_20)`: S=-0.07, F=-0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_20 / close)`: S=0.00, F=0.00, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_20, 5))`: S=-1.42, F=-0.49, T=57.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_20, 5))` | TOP1000 | 1.26 | 0.54 | 9.0% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_20, 5))` | TOP3000 | 1.44 | 0.49 | 4.6% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_20, 5))` | TOP200 | 0.94 | 0.46 | 14.1% | 100% | all-weather |
| `rank(implied_volatility_call_20)` | TOP200 | 0.37 | 0.30 | 73.9% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_20, 5))` | TOP500 | 0.72 | 0.26 | 11.0% | 80% | mixed |
| `rank(implied_volatility_call_20)` | TOP500 | 0.23 | 0.13 | 75.7% | 60% | bear-only |
| `rank(implied_volatility_call_20)` | TOP1000 | 0.17 | 0.08 | 68.8% | 40% | bear-only |
| `rank(implied_volatility_call_20)` | TOP3000 | 0.07 | 0.02 | 71.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_30: 0.927 (strongly positively correlated)
- implied_volatility_mean_30: 0.914 (strongly positively correlated)
- implied_volatility_put_30: 0.889 (strongly positively correlated)
- implied_volatility_call_60: 0.819 (strongly positively correlated)
- implied_volatility_mean_60: 0.667 (moderately positively correlated)

Redundancy cluster #20: 5 similar fields, mean |rho| 0.906 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.07 | 1.84 | +0.56 | -0.38 | yes |
| fnd6_newqv1300_aol2q | fundamental6 | -0.03 | 1.80 | +0.52 | -0.72 | yes |
| actuals_value_currency_code | data_artifact | -0.04 | 1.81 | +0.55 | -0.34 | yes |
| rel_num_part | pv13 | -0.06 | 1.84 | +0.57 | -0.09 | yes |
| fnd6_newqv1300_ppegtq | fundamental6 | -0.04 | 1.79 | +0.54 | -0.43 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
