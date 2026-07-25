---
field: implied_volatility_mean_30
dataset: option8
best_template: ts_zscore
best_sharpe: 1.05
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0733
ann_vol: 0.0729
hit_rate: 0.5198
rolling_sharpe_min: 0.178
rolling_sharpe_max: 2.432
top_merge_partner: rp_css_mna
redundancy_cluster: 20
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.07
---
# implied_volatility_mean_30 (option8)

*The average of IvCall30 and IvPut30*

## Signal Profile
- `rank(implied_volatility_mean_30)`: S=0.34, F=0.27, T=9.0%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_30 / close)`: S=0.11, F=0.04, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_30, 5))`: S=1.19, F=0.52, T=44.9%, INFERIOR (TOP1000)
- `-rank(implied_volatility_mean_30)`: S=-0.15, F=-0.08, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_30, 5))`: S=-1.28, F=-0.44, T=55.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_30, 22)`: S=1.05, F=0.53, T=29.9%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_30, 10)`: S=-0.06, F=-0.02, T=4.8%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_30, 22))`: S=0.95, F=0.41, T=32.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_30)`: S=-0.06, F=-0.02, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_30 / close)`: S=-0.02, F=0.00, T=8.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.18, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.13 (moderate), ret=+4.3%
  - 2020: S=1.53 (strong), ret=+8.3%
  - 2021: S=1.55 (strong), ret=+13.7%
  - 2022: S=1.26 (moderate), ret=+13.1%
  - 2023: S=0.54 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 7.33% over 105 days (recovered)
- Annualized: return +8.6%, volatility 7.3% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.91, excess kurtosis +6.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.18, max 2.43, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.61%; worst month: -3.87%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.75
- Sideways: S=1.39
- Bear: S=0.30

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_30 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.07 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_30)`: S=-0.06, F=-0.02, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_30 / close)`: S=-0.02, F=0.00, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_30, 5))`: S=-1.28, F=-0.44, T=55.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_30, 5))` | TOP1000 | 1.18 | 0.52 | 7.3% | 100% | mixed |
| `rank(ts_delta(implied_volatility_mean_30, 5))` | TOP3000 | 1.30 | 0.44 | 5.0% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_30, 5))` | TOP200 | 0.75 | 0.34 | 14.6% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_30, 5))` | TOP500 | 0.78 | 0.30 | 8.4% | 80% | mixed |
| `rank(implied_volatility_mean_30)` | TOP200 | 0.35 | 0.27 | 73.1% | 60% | bear-only |
| `rank(implied_volatility_mean_30)` | TOP500 | 0.22 | 0.13 | 74.9% | 40% | bear-only |
| `rank(implied_volatility_mean_30)` | TOP1000 | 0.16 | 0.08 | 68.5% | 40% | bear-only |
| `rank(implied_volatility_mean_30)` | TOP3000 | 0.06 | 0.02 | 72.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_30: 0.983 (strongly positively correlated)
- implied_volatility_call_30: 0.979 (strongly positively correlated)
- implied_volatility_call_20: 0.914 (strongly positively correlated)
- implied_volatility_call_60: 0.874 (strongly positively correlated)
- implied_volatility_mean_60: 0.724 (strongly positively correlated)

Redundancy cluster #20: 5 similar fields, mean |rho| 0.906 (representative: implied_volatility_call_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_css_mna | news18 | -0.00 | 1.63 | +0.44 | -0.73 | yes |
| fnd6_dxd5 | fundamental6 | -0.05 | 1.70 | +0.51 | +0.04 | yes |
| fnd6_dd5 | fundamental6 | -0.06 | 1.69 | +0.50 | +0.01 | yes |
| actuals_value_currency_code | data_artifact | -0.00 | 1.72 | +0.47 | -0.32 | yes |
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.04 | 1.78 | +0.49 | -0.12 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
