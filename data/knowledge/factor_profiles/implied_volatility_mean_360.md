---
field: implied_volatility_mean_360
dataset: option8
best_template: ts_zscore
best_sharpe: 1.08
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0526
ann_vol: 0.0521
hit_rate: 0.5223
rolling_sharpe_min: -0.221
rolling_sharpe_max: 2.837
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.05
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -1.13
---
# implied_volatility_mean_360 (option8)

*The average of IvCall360 and IvPut360*

## Signal Profile
- `rank(implied_volatility_mean_360)`: S=0.27, F=0.19, T=5.8%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_360 / close)`: S=0.11, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_360, 5))`: S=1.34, F=0.46, T=58.5%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_360)`: S=-0.13, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_360, 5))`: S=-1.34, F=-0.46, T=58.5%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_360, 22)`: S=1.08, F=0.52, T=30.7%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_360, 10)`: S=0.00, F=0.00, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_360, 22))`: S=1.01, F=0.42, T=32.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_360)`: S=-0.05, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_360 / close)`: S=-0.03, F=-0.01, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.35, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.10 (negative), ret=-0.3%
  - 2020: S=2.24 (strong), ret=+10.3%
  - 2021: S=1.85 (strong), ret=+10.4%
  - 2022: S=2.03 (strong), ret=+15.0%
  - 2023: S=-0.23 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 5.26% over 334 days (recovered)
- Annualized: return +7.0%, volatility 5.2% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +1.44, excess kurtosis +11.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.22, max 2.84, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.53%; worst month: -2.63%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.12
- Sideways: S=0.36
- Bear: S=1.30

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_360)` S=-0.05, F=-0.01, INFERIOR
Direction gap: -1.13 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_360)`: S=-0.05, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_360 / close)`: S=-0.03, F=-0.01, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_360, 5))`: S=-1.34, F=-0.46, T=58.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_360, 5))` | TOP3000 | 1.35 | 0.46 | 5.3% | 60% | all-weather |
| `rank(ts_delta(implied_volatility_mean_360, 5))` | TOP1000 | 0.89 | 0.32 | 6.6% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_360, 5))` | TOP500 | 0.63 | 0.22 | 8.5% | 80% | bull-only |
| `rank(implied_volatility_mean_360)` | TOP200 | 0.28 | 0.19 | 73.3% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_mean_360, 5))` | TOP200 | 0.49 | 0.18 | 19.2% | 80% | mixed |
| `rank(implied_volatility_mean_360)` | TOP500 | 0.21 | 0.12 | 73.3% | 40% | bear-only |
| `rank(implied_volatility_mean_360)` | TOP1000 | 0.14 | 0.06 | 68.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_270: 0.989 (strongly positively correlated)
- implied_volatility_mean_720: 0.960 (strongly positively correlated)
- implied_volatility_mean_1080: 0.954 (strongly positively correlated)
- implied_volatility_mean_180: 0.949 (strongly positively correlated)
- implied_volatility_call_360: 0.925 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.13 | 1.97 | +0.61 | +0.81 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.07 | 1.97 | +0.57 | +0.60 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 1.96 | +0.51 | -0.23 | yes |
| rp_ess_dividends | news18 | +0.01 | 1.90 | +0.50 | -0.36 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 1.96 | +0.51 | -0.23 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
