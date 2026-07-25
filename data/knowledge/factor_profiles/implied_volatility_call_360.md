---
field: implied_volatility_call_360
dataset: option8
best_template: rank_delta
best_sharpe: 1.55
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0396
ann_vol: 0.0455
hit_rate: 0.5336
rolling_sharpe_min: 0.209
rolling_sharpe_max: 2.762
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.56
---
# implied_volatility_call_360 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 360 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_360)`: S=0.28, F=0.20, T=6.6%, INFERIOR (TOP200)
- `rank(implied_volatility_call_360 / close)`: S=0.12, F=0.05, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_360, 5))`: S=1.55, F=0.53, T=60.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_360)`: S=-0.16, F=-0.08, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_360, 5))`: S=-1.55, F=-0.53, T=60.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_360, 22)`: S=0.92, F=0.38, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_360, 10)`: S=0.08, F=0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_360, 22))`: S=0.73, F=0.25, T=32.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_360)`: S=-0.09, F=-0.03, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_360 / close)`: S=-0.01, F=0.00, T=6.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.57, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+0.7%
  - 2020: S=2.28 (strong), ret=+9.5%
  - 2021: S=2.10 (strong), ret=+10.4%
  - 2022: S=1.83 (strong), ret=+11.3%
  - 2023: S=0.88 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 3.96% over 330 days (recovered)
- Annualized: return +7.1%, volatility 4.5% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +1.06, excess kurtosis +9.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.21, max 2.76, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +4.32%; worst month: -2.48%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.29
- Sideways: S=0.88
- Bear: S=1.36

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_360 / close)` S=-0.01, F=0.00, INFERIOR
Direction gap: -1.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_360)`: S=-0.09, F=-0.03, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_360 / close)`: S=-0.01, F=0.00, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_360, 5))`: S=-1.55, F=-0.53, T=60.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_360, 5))` | TOP3000 | 1.57 | 0.53 | 4.0% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_360, 5))` | TOP1000 | 0.98 | 0.35 | 4.8% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_360, 5))` | TOP500 | 0.70 | 0.24 | 7.7% | 80% | bull-only |
| `rank(implied_volatility_call_360)` | TOP200 | 0.29 | 0.20 | 72.3% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_360, 5))` | TOP200 | 0.54 | 0.19 | 20.8% | 80% | mixed |
| `rank(implied_volatility_call_360)` | TOP500 | 0.23 | 0.13 | 71.8% | 60% | bear-only |
| `rank(implied_volatility_call_360)` | TOP1000 | 0.16 | 0.08 | 66.8% | 40% | bear-only |
| `rank(implied_volatility_call_360)` | TOP3000 | 0.10 | 0.03 | 70.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_270: 0.986 (strongly positively correlated)
- implied_volatility_call_720: 0.953 (strongly positively correlated)
- implied_volatility_call_1080: 0.947 (strongly positively correlated)
- implied_volatility_call_180: 0.938 (strongly positively correlated)
- implied_volatility_mean_360: 0.925 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.14 | 2.20 | +0.64 | +0.88 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.04 | 2.20 | +0.63 | +0.87 | yes |
| current_ratio | fundamental6 | -0.06 | 2.20 | +0.54 | +0.34 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.07 | +0.50 | -0.13 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.07 | +0.50 | -0.13 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
