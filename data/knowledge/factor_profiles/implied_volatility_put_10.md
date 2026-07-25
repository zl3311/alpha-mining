---
field: implied_volatility_put_10
dataset: option8
best_template: ts_mean
best_sharpe: 0.65
best_fitness: 1.3
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1626
ann_vol: 0.1113
hit_rate: 0.5263
rolling_sharpe_min: 0.375
rolling_sharpe_max: 2.698
top_merge_partner: fnd6_newqv1300_dpactq
redundancy_cluster: 15
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.65
---
# implied_volatility_put_10 (option8)

*At-the-money implied volatility of put options with 10 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_10)`: S=0.34, F=0.26, T=13.2%, INFERIOR (TOP200)
- `rank(implied_volatility_put_10 / close)`: S=0.11, F=0.04, T=5.9%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_10, 5))`: S=1.30, F=0.75, T=43.3%, INFERIOR (TOP200)
- `-rank(implied_volatility_put_10)`: S=-0.17, F=-0.09, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_10, 5))`: S=-1.16, F=-0.36, T=58.0%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_10, 22)`: S=0.78, F=0.31, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_10, 10)`: S=0.65, F=1.30, T=3.0%, AVERAGE (TOP3000)
- `rank(ts_rank(implied_volatility_put_10, 22))`: S=0.56, F=0.17, T=35.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_10)`: S=-0.04, F=-0.01, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_10 / close)`: S=0.00, F=0.00, T=8.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 20F/1P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.29, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.24 (moderate), ret=+7.4%
  - 2020: S=2.01 (strong), ret=+20.8%
  - 2021: S=0.53 (moderate), ret=+6.9%
  - 2022: S=1.80 (strong), ret=+25.1%
  - 2023: S=1.07 (moderate), ret=+10.1%

## Risk & Drawdown
- Max drawdown: 16.26% over 298 days (recovered)
- Annualized: return +14.4%, volatility 11.1% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.71, excess kurtosis +5.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.38, max 2.70, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.72%; worst month: -7.63%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.04
- Sideways: S=1.62
- Bear: S=1.37

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_10 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_10)`: S=-0.04, F=-0.01, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_10 / close)`: S=0.00, F=0.00, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_10, 5))`: S=-1.16, F=-0.36, T=58.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_10, 5))` | TOP200 | 1.29 | 0.75 | 16.3% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_10, 5))` | TOP1000 | 1.17 | 0.48 | 8.9% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_10, 5))` | TOP500 | 0.96 | 0.40 | 11.3% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_10, 5))` | TOP3000 | 1.17 | 0.36 | 5.0% | 100% | all-weather |
| `rank(implied_volatility_put_10)` | TOP200 | 0.34 | 0.26 | 73.2% | 60% | bear-only |
| `rank(implied_volatility_put_10)` | TOP500 | 0.23 | 0.14 | 72.5% | 60% | bear-only |
| `rank(implied_volatility_put_10)` | TOP1000 | 0.17 | 0.09 | 66.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_10: 0.989 (strongly positively correlated)
- implied_volatility_call_10: 0.954 (strongly positively correlated)
- implied_volatility_put_20: 0.784 (strongly positively correlated)
- implied_volatility_mean_20: 0.781 (strongly positively correlated)
- implied_volatility_call_20: 0.562 (moderately positively correlated)

Redundancy cluster #15: 5 similar fields, mean |rho| 0.853 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_dpactq | fundamental_depreciation | -0.12 | 1.94 | +0.64 | -0.55 | yes |
| fnd6_city | fundamental_rare_event | -0.15 | 2.19 | +0.63 | -0.47 | yes |
| anl4_bvps_flag | analyst_revision | -0.12 | 1.93 | +0.62 | -0.43 | yes |
| fnd6_newqv1300_ppegtq | fundamental6 | -0.08 | 1.87 | +0.58 | -0.63 | yes |
| fnd6_fate | fundamental_capital_intensity | -0.10 | 1.89 | +0.59 | -0.38 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
