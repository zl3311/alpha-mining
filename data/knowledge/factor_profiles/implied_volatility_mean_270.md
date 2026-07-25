---
field: implied_volatility_mean_270
dataset: option8
best_template: ts_zscore
best_sharpe: 0.99
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0529
ann_vol: 0.0528
hit_rate: 0.5271
rolling_sharpe_min: -0.309
rolling_sharpe_max: 2.923
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.01
---
# implied_volatility_mean_270 (option8)

*The average of IvCall270 and IvPut270*

## Signal Profile
- `rank(implied_volatility_mean_270)`: S=0.28, F=0.21, T=5.9%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_270 / close)`: S=0.11, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_270, 5))`: S=1.27, F=0.43, T=57.9%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_270)`: S=-0.13, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_270, 5))`: S=-1.27, F=-0.43, T=57.9%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_270, 22)`: S=0.99, F=0.46, T=30.5%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_270, 10)`: S=0.01, F=0.00, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_270, 22))`: S=0.96, F=0.39, T=32.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_270)`: S=-0.05, F=-0.01, T=9.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_270 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.2%
  - 2020: S=2.12 (strong), ret=+9.8%
  - 2021: S=1.71 (strong), ret=+9.8%
  - 2022: S=1.99 (strong), ret=+14.9%
  - 2023: S=-0.29 (negative), ret=-1.0%

## Risk & Drawdown
- Max drawdown: 5.29% over 330 days (recovered)
- Annualized: return +6.8%, volatility 5.3% (fraction of booksize)
- Hit rate: 52.7% positive days
- Tail shape: skew +1.41, excess kurtosis +10.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.31, max 2.92, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.43%; worst month: -2.48%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.10
- Sideways: S=0.29
- Bear: S=1.18

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_270 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.01 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_270)`: S=-0.05, F=-0.01, T=9.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_270 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_270, 5))`: S=-1.27, F=-0.43, T=57.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_270, 5))` | TOP3000 | 1.28 | 0.43 | 5.3% | 60% | all-weather |
| `rank(ts_delta(implied_volatility_mean_270, 5))` | TOP1000 | 0.84 | 0.30 | 7.1% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_270, 5))` | TOP500 | 0.66 | 0.23 | 7.8% | 80% | bull-only |
| `rank(implied_volatility_mean_270)` | TOP200 | 0.29 | 0.21 | 73.2% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_mean_270, 5))` | TOP200 | 0.46 | 0.16 | 20.3% | 80% | mixed |
| `rank(implied_volatility_mean_270)` | TOP500 | 0.21 | 0.12 | 73.6% | 40% | bear-only |
| `rank(implied_volatility_mean_270)` | TOP1000 | 0.14 | 0.06 | 68.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_360: 0.989 (strongly positively correlated)
- implied_volatility_mean_180: 0.966 (strongly positively correlated)
- implied_volatility_mean_720: 0.941 (strongly positively correlated)
- implied_volatility_mean_150: 0.940 (strongly positively correlated)
- implied_volatility_mean_1080: 0.935 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.12 | 1.90 | +0.54 | +0.80 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.08 | 1.94 | +0.54 | +0.57 | yes |
| fnd6_cld3 | fundamental6 | -0.01 | 1.81 | +0.53 | +0.75 | yes |
| anl4_tbve_ft | analyst_estimate | +0.02 | 1.75 | +0.47 | -0.45 | yes |
| rel_num_part | pv13 | +0.01 | 1.79 | +0.51 | +0.22 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
