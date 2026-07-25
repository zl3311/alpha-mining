---
field: implied_volatility_call_30
dataset: option8
best_template: rank_delta
best_sharpe: 1.23
best_fitness: 0.53
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0703
ann_vol: 0.0702
hit_rate: 0.5166
rolling_sharpe_min: 0.508
rolling_sharpe_max: 2.255
top_merge_partner: actuals_value_currency_code
redundancy_cluster: 20
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.23
---
# implied_volatility_call_30 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 30 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_30)`: S=0.34, F=0.27, T=9.6%, INFERIOR (TOP200)
- `rank(implied_volatility_call_30 / close)`: S=0.12, F=0.04, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_30, 5))`: S=1.23, F=0.53, T=46.6%, INFERIOR (TOP1000)
- `-rank(implied_volatility_call_30)`: S=-0.16, F=-0.08, T=9.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30, 5))`: S=-1.29, F=-0.43, T=57.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_30, 22)`: S=0.95, F=0.44, T=30.5%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_30, 10)`: S=0.04, F=0.01, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_30, 22))`: S=0.88, F=0.35, T=32.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_30)`: S=-0.07, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_30 / close)`: S=0.00, F=0.00, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 21F/2P
- LOW_SUB_UNIVERSE_SHARPE: 5F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.23, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+4.0%
  - 2020: S=1.45 (moderate), ret=+7.6%
  - 2021: S=1.46 (moderate), ret=+12.7%
  - 2022: S=1.40 (moderate), ret=+13.8%
  - 2023: S=0.81 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 7.03% over 189 days (recovered)
- Annualized: return +8.6%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.98, excess kurtosis +6.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.51, max 2.25, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.95%; worst month: -4.03%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.79
- Sideways: S=1.21
- Bear: S=0.55

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_30 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.23 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_30)`: S=-0.07, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_30 / close)`: S=0.00, F=0.00, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30, 5))`: S=-1.29, F=-0.43, T=57.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_30, 5))` | TOP1000 | 1.23 | 0.53 | 7.0% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_30, 5))` | TOP3000 | 1.31 | 0.43 | 4.7% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_30, 5))` | TOP500 | 0.74 | 0.27 | 8.3% | 80% | mixed |
| `rank(implied_volatility_call_30)` | TOP200 | 0.35 | 0.27 | 74.0% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_30, 5))` | TOP200 | 0.54 | 0.20 | 16.7% | 80% | mixed |
| `rank(implied_volatility_call_30)` | TOP500 | 0.22 | 0.13 | 75.9% | 60% | bear-only |
| `rank(implied_volatility_call_30)` | TOP1000 | 0.17 | 0.08 | 68.9% | 40% | bear-only |
| `rank(implied_volatility_call_30)` | TOP3000 | 0.08 | 0.02 | 72.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_30: 0.979 (strongly positively correlated)
- implied_volatility_put_30: 0.943 (strongly positively correlated)
- implied_volatility_call_20: 0.927 (strongly positively correlated)
- implied_volatility_call_60: 0.882 (strongly positively correlated)
- implied_volatility_mean_60: 0.720 (strongly positively correlated)

Redundancy cluster #20: 5 similar fields, mean |rho| 0.906 (representative: implied_volatility_call_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| actuals_value_currency_code | data_artifact | -0.02 | 1.77 | +0.52 | -0.26 | yes |
| rel_num_all | pv13 | -0.05 | 1.77 | +0.54 | +0.08 | yes |
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.07 | 1.82 | +0.53 | +0.02 | yes |
| rel_num_part | pv13 | -0.05 | 1.80 | +0.53 | +0.23 | yes |
| anl4_tbve_ft | analyst_estimate | -0.02 | 1.77 | +0.52 | -0.11 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
