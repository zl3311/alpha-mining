---
field: implied_volatility_put_30
dataset: option8
best_template: rank_delta
best_sharpe: 1.22
best_fitness: 0.53
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0634
ann_vol: 0.0709
hit_rate: 0.5223
rolling_sharpe_min: 0.024
rolling_sharpe_max: 2.603
top_merge_partner: actuals_value_currency_code
redundancy_cluster: 20
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.22
---
# implied_volatility_put_30 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 30 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_30)`: S=0.32, F=0.25, T=9.9%, INFERIOR (TOP200)
- `rank(implied_volatility_put_30 / close)`: S=0.11, F=0.04, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_30, 5))`: S=1.22, F=0.53, T=46.3%, INFERIOR (TOP1000)
- `-rank(implied_volatility_put_30)`: S=-0.16, F=-0.08, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_30, 5))`: S=-1.35, F=-0.47, T=57.5%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_30, 22)`: S=1.00, F=0.48, T=30.3%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_30, 10)`: S=-0.14, F=-0.08, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_30, 22))`: S=0.90, F=0.36, T=32.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_30)`: S=-0.04, F=-0.01, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_30 / close)`: S=0.00, F=0.00, T=7.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 21F/2P
- LOW_SUB_UNIVERSE_SHARPE: 5F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.22, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+3.5%
  - 2020: S=1.81 (strong), ret=+9.6%
  - 2021: S=1.62 (strong), ret=+14.0%
  - 2022: S=1.31 (moderate), ret=+13.2%
  - 2023: S=0.42 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 6.34% over 103 days (recovered)
- Annualized: return +8.6%, volatility 7.1% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.93, excess kurtosis +6.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.02, max 2.60, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.98%; worst month: -3.78%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.72
- Sideways: S=1.46
- Bear: S=0.41

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_30 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.22 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_30)`: S=-0.04, F=-0.01, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_30 / close)`: S=0.00, F=0.00, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_30, 5))`: S=-1.35, F=-0.47, T=57.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_30, 5))` | TOP1000 | 1.22 | 0.53 | 6.3% | 100% | mixed |
| `rank(ts_delta(implied_volatility_put_30, 5))` | TOP3000 | 1.36 | 0.47 | 4.6% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_30, 5))` | TOP200 | 0.89 | 0.43 | 11.1% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_30, 5))` | TOP500 | 0.94 | 0.39 | 7.3% | 100% | mixed |
| `rank(implied_volatility_put_30)` | TOP200 | 0.33 | 0.25 | 73.1% | 60% | bear-only |
| `rank(implied_volatility_put_30)` | TOP500 | 0.22 | 0.13 | 74.1% | 40% | bear-only |
| `rank(implied_volatility_put_30)` | TOP1000 | 0.17 | 0.08 | 68.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_30: 0.983 (strongly positively correlated)
- implied_volatility_call_30: 0.943 (strongly positively correlated)
- implied_volatility_call_20: 0.889 (strongly positively correlated)
- implied_volatility_call_60: 0.851 (strongly positively correlated)
- implied_volatility_mean_60: 0.711 (strongly positively correlated)

Redundancy cluster #20: 5 similar fields, mean |rho| 0.906 (representative: implied_volatility_call_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| actuals_value_currency_code | data_artifact | -0.01 | 1.75 | +0.50 | -0.48 | yes |
| rel_num_all | pv13 | -0.02 | 1.75 | +0.53 | -0.15 | yes |
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.04 | 1.79 | +0.51 | -0.20 | yes |
| fnd6_dxd5 | fundamental6 | -0.06 | 1.73 | +0.51 | -0.08 | yes |
| anl4_tbve_ft | analyst_estimate | -0.02 | 1.76 | +0.51 | -0.07 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
