---
field: implied_volatility_put_1080
dataset: option8
best_template: rank_delta
best_sharpe: 1.39
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.052
ann_vol: 0.0428
hit_rate: 0.5239
rolling_sharpe_min: -0.798
rolling_sharpe_max: 3.15
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.39
---
# implied_volatility_put_1080 (option8)

*At-the-money implied volatility of put options with 1080 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_1080)`: S=0.22, F=0.14, T=7.8%, INFERIOR (TOP200)
- `rank(implied_volatility_put_1080 / close)`: S=0.11, F=0.04, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_1080, 5))`: S=1.39, F=0.44, T=60.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_1080)`: S=-0.11, F=-0.05, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_1080, 5))`: S=-1.39, F=-0.44, T=60.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_1080, 22)`: S=1.05, F=0.44, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_1080, 10)`: S=-0.07, F=-0.03, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_1080, 22))`: S=0.96, F=0.37, T=32.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_1080)`: S=-0.03, F=-0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_1080 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+0.6%
  - 2020: S=1.65 (strong), ret=+6.2%
  - 2021: S=1.73 (strong), ret=+8.4%
  - 2022: S=2.87 (strong), ret=+16.1%
  - 2023: S=-0.69 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 5.20% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +5.9%, volatility 4.3% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +1.02, excess kurtosis +7.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 3.15, latest -0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.75%; worst month: -1.92%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.34
- Sideways: S=-0.17
- Bear: S=1.71

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_1080 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.39 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_1080)`: S=-0.03, F=-0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_1080 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_1080, 5))`: S=-1.39, F=-0.44, T=60.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_1080, 5))` | TOP3000 | 1.39 | 0.44 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_1080, 5))` | TOP500 | 0.83 | 0.29 | 6.3% | 100% | mixed |
| `rank(ts_delta(implied_volatility_put_1080, 5))` | TOP200 | 0.58 | 0.21 | 14.3% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_1080, 5))` | TOP1000 | 0.70 | 0.20 | 5.9% | 80% | mixed |
| `rank(implied_volatility_put_1080)` | TOP200 | 0.23 | 0.14 | 73.9% | 60% | bear-only |
| `rank(implied_volatility_put_1080)` | TOP500 | 0.14 | 0.06 | 73.2% | 40% | bear-only |
| `rank(implied_volatility_put_1080)` | TOP1000 | 0.12 | 0.05 | 67.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_720: 0.997 (strongly positively correlated)
- implied_volatility_put_360: 0.947 (strongly positively correlated)
- implied_volatility_put_270: 0.926 (strongly positively correlated)
- implied_volatility_put_180: 0.883 (strongly positively correlated)
- implied_volatility_mean_720: 0.880 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.13 | 2.05 | +0.66 | +0.73 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.00 | 1.97 | +0.52 | -0.52 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.00 | 1.97 | +0.52 | -0.52 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.00 | 2.04 | +0.55 | +0.79 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.07 | 1.94 | +0.53 | +0.38 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
