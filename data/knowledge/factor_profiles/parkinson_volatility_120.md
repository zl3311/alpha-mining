---
field: parkinson_volatility_120
dataset: option8
best_template: rank_delta
best_sharpe: 0.89
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 29
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1141
ann_vol: 0.0815
hit_rate: 0.5158
rolling_sharpe_min: -0.356
rolling_sharpe_max: 2.351
top_merge_partner: fnd6_xrent
redundancy_cluster: 48
negated_best_sharpe: 0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.86
---
# parkinson_volatility_120 (option8)

*Historical Parkinson volatility for approximately 120 calendar days*

## Signal Profile
- `rank(parkinson_volatility_120)`: S=0.25, F=0.16, T=4.8%, INFERIOR (TOP200)
- `rank(parkinson_volatility_120 / close)`: S=0.02, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_120, 5))`: S=0.89, F=0.45, T=28.7%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_120)`: S=-0.03, F=-0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_120, 5))`: S=-0.89, F=-0.45, T=28.7%, INFERIOR (TOP3000)
- `-ts_zscore(parkinson_volatility_120, 63)`: S=0.04, F=0.01, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_120, 10)`: S=-0.21, F=-0.14, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_120, 22))`: S=0.10, F=0.02, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_120)`: S=0.02, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_120 / close)`: S=0.03, F=0.01, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 28F/1P
- LOW_FITNESS: 29F/0P
- LOW_SHARPE: 29F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.20 (strong), ret=+8.0%
  - 2020: S=0.53 (moderate), ret=+5.4%
  - 2021: S=1.25 (moderate), ret=+10.6%
  - 2022: S=0.80 (moderate), ret=+8.2%
  - 2023: S=0.71 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 11.41% over 401 days (recovered)
- Annualized: return +7.2%, volatility 8.2% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.89, excess kurtosis +8.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.36, max 2.35, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.82%; worst month: -3.19%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.31
- Sideways: S=0.16
- Bear: S=1.02

## Negated Direction
Best negated: `rank(-1 * parkinson_volatility_120 / close)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * parkinson_volatility_120)`: S=0.02, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_120 / close)`: S=0.03, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_120, 5))`: S=-0.89, F=-0.45, T=28.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_120, 5))` | TOP3000 | 0.89 | 0.45 | 11.4% | 100% | all-weather |
| `rank(ts_delta(parkinson_volatility_120, 5))` | TOP1000 | 0.47 | 0.18 | 13.8% | 100% | all-weather |
| `rank(parkinson_volatility_120)` | TOP200 | 0.25 | 0.16 | 62.4% | 60% | bear-only |
| `rank(parkinson_volatility_120)` | TOP500 | 0.17 | 0.08 | 65.5% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_120, 5))` | TOP500 | 0.26 | 0.08 | 24.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- historical_volatility_120: 0.819 (strongly positively correlated)
- parkinson_volatility_90: 0.764 (strongly positively correlated)
- historical_volatility_90: 0.684 (moderately positively correlated)
- parkinson_volatility_60: 0.580 (moderately positively correlated)
- implied_volatility_call_30 - implied_volatility_call_270: 0.576 (moderately positively correlated)

Redundancy cluster #48: 4 similar fields, mean |rho| 0.738 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_xrent | fundamental6 | -0.32 | 1.56 | +0.63 | +0.26 | yes |
| fnd6_mrc2 | fundamental6 | -0.30 | 1.51 | +0.61 | +0.29 | yes |
| fnd6_mrc3 | fundamental6 | -0.29 | 1.50 | +0.60 | +0.18 | yes |
| anl4_bvps_flag | analyst_revision | -0.33 | 1.89 | +0.59 | +0.53 | yes |
| anl4_fcf_mean | analyst4 | -0.28 | 1.50 | +0.59 | +0.35 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
