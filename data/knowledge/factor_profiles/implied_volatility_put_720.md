---
field: implied_volatility_put_720
dataset: option8
best_template: rank_delta
best_sharpe: 1.41
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0522
ann_vol: 0.043
hit_rate: 0.5231
rolling_sharpe_min: -0.874
rolling_sharpe_max: 3.192
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.41
---
# implied_volatility_put_720 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 720 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_720)`: S=0.22, F=0.14, T=7.7%, INFERIOR (TOP200)
- `rank(implied_volatility_put_720 / close)`: S=0.11, F=0.04, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_720, 5))`: S=1.41, F=0.45, T=60.1%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_720)`: S=-0.12, F=-0.05, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_720, 5))`: S=-1.41, F=-0.45, T=60.1%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_720, 22)`: S=0.96, F=0.39, T=30.5%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_720, 10)`: S=-0.07, F=-0.03, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_720, 22))`: S=0.85, F=0.30, T=32.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_720)`: S=-0.03, F=-0.01, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_720 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.41, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+0.6%
  - 2020: S=1.70 (strong), ret=+6.4%
  - 2021: S=1.75 (strong), ret=+8.6%
  - 2022: S=2.88 (strong), ret=+16.2%
  - 2023: S=-0.64 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 5.22% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +6.0%, volatility 4.3% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +1.01, excess kurtosis +7.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 3.19, latest -0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.77%; worst month: -1.92%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.34
- Sideways: S=-0.14
- Bear: S=1.74

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_720 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.41 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_720)`: S=-0.03, F=-0.01, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_720 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_720, 5))`: S=-1.41, F=-0.45, T=60.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_720, 5))` | TOP3000 | 1.41 | 0.45 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_720, 5))` | TOP500 | 0.77 | 0.26 | 6.2% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_720, 5))` | TOP200 | 0.58 | 0.21 | 14.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_720, 5))` | TOP1000 | 0.66 | 0.18 | 5.8% | 80% | mixed |
| `rank(implied_volatility_put_720)` | TOP200 | 0.23 | 0.14 | 73.8% | 60% | bear-only |
| `rank(implied_volatility_put_720)` | TOP500 | 0.14 | 0.06 | 73.2% | 40% | bear-only |
| `rank(implied_volatility_put_720)` | TOP1000 | 0.12 | 0.05 | 67.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_1080: 0.997 (strongly positively correlated)
- implied_volatility_put_360: 0.955 (strongly positively correlated)
- implied_volatility_put_270: 0.934 (strongly positively correlated)
- implied_volatility_put_180: 0.890 (strongly positively correlated)
- implied_volatility_mean_720: 0.882 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.13 | 2.07 | +0.66 | +0.74 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.00 | 1.98 | +0.53 | -0.51 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.00 | 1.98 | +0.53 | -0.51 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.00 | 2.05 | +0.56 | +0.80 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.07 | 1.94 | +0.54 | +0.39 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
