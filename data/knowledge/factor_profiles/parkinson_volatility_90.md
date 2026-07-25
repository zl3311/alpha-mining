---
field: parkinson_volatility_90
dataset: option8
cluster: option8_analyst_forecast
coverage: 0.9803
community_alphas: 1841
best_template: rank_delta
best_sharpe: 0.89
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0859
ann_vol: 0.0724
hit_rate: 0.5077
rolling_sharpe_min: -1.28
rolling_sharpe_max: 2.19
top_merge_partner: fn_op_lease_min_pay_due_in_4y_a
redundancy_cluster: 48
negated_best_sharpe: 0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.83
---
# parkinson_volatility_90 (option8)

*Historical volatility using the Parkinson high–low estimator over approximately the past 90 calendar days*

## Signal Profile
- `rank(parkinson_volatility_90)`: S=0.18, F=0.10, T=5.2%, INFERIOR (TOP200)
- `rank(parkinson_volatility_90 / close)`: S=0.01, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_90, 5))`: S=0.89, F=0.41, T=29.5%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_90)`: S=-0.02, F=0.00, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_90, 5))`: S=-0.89, F=-0.41, T=29.5%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_90, 22)`: S=0.51, F=0.21, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_90, 10)`: S=-0.25, F=-0.19, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_90, 22))`: S=0.48, F=0.17, T=25.6%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_90)`: S=0.04, F=0.01, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_90 / close)`: S=0.06, F=0.02, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+0.9%
  - 2020: S=1.14 (moderate), ret=+10.7%
  - 2021: S=1.14 (moderate), ret=+8.0%
  - 2022: S=0.99 (moderate), ret=+8.6%
  - 2023: S=0.73 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 8.59% over 156 days (recovered)
- Annualized: return +6.4%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.82, excess kurtosis +7.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.19, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.92%; worst month: -2.90%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.26
- Sideways: S=-0.41
- Bear: S=1.43

## Negated Direction
Best negated: `rank(-1 * parkinson_volatility_90 / close)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * parkinson_volatility_90)`: S=0.04, F=0.01, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_90 / close)`: S=0.06, F=0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_90, 5))`: S=-0.89, F=-0.41, T=29.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_90, 5))` | TOP3000 | 0.89 | 0.41 | 8.6% | 100% | all-weather |
| `rank(ts_delta(parkinson_volatility_90, 5))` | TOP1000 | 0.65 | 0.28 | 12.7% | 80% | all-weather |
| `rank(ts_delta(parkinson_volatility_90, 5))` | TOP200 | 0.35 | 0.14 | 19.5% | 40% | mixed |
| `rank(ts_delta(parkinson_volatility_90, 5))` | TOP500 | 0.37 | 0.13 | 19.3% | 40% | mixed |
| `rank(parkinson_volatility_90)` | TOP200 | 0.18 | 0.10 | 67.9% | 60% | bear-only |
| `rank(parkinson_volatility_90)` | TOP500 | 0.15 | 0.07 | 67.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_90: 0.870 (strongly positively correlated)
- parkinson_volatility_120: 0.764 (strongly positively correlated)
- historical_volatility_120: 0.640 (moderately positively correlated)
- parkinson_volatility_60: 0.624 (moderately positively correlated)
- historical_volatility_60: 0.551 (moderately positively correlated)

Redundancy cluster #48: 4 similar fields, mean |rho| 0.738 (representative: parkinson_volatility_120). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_op_lease_min_pay_due_in_4y_a | fundamental2 | -0.18 | 1.37 | +0.48 | -0.53 | yes |
| cashflow_per_share_minimum | analyst4 | -0.20 | 1.33 | +0.44 | -0.86 | yes |
| fnd6_xrent | fundamental6 | -0.22 | 1.45 | +0.52 | -0.12 | yes |
| rel_num_all | pv13 | -0.24 | 1.72 | +0.50 | -0.29 | yes |
| rel_num_comp | pv13 | -0.25 | 1.62 | +0.51 | -0.12 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
