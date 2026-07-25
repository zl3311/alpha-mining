---
field: implied_volatility_call_1080
dataset: option8
best_template: rank_delta
best_sharpe: 1.6
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 23
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0384
ann_vol: 0.0424
hit_rate: 0.5409
rolling_sharpe_min: 0.392
rolling_sharpe_max: 2.789
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.61
---
# implied_volatility_call_1080 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 1080 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_1080)`: S=0.24, F=0.16, T=7.3%, INFERIOR (TOP200)
- `rank(implied_volatility_call_1080 / close)`: S=0.13, F=0.05, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_1080, 5))`: S=1.60, F=0.53, T=61.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_1080)`: S=-0.16, F=-0.08, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_1080, 5))`: S=-1.60, F=-0.53, T=61.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_1080, 22)`: S=0.96, F=0.38, T=31.4%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_1080, 10)`: S=0.07, F=0.03, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_1080, 22))`: S=0.90, F=0.33, T=33.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_1080)`: S=-0.10, F=-0.04, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_1080 / close)`: S=-0.01, F=0.00, T=6.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 21F/2P
- LOW_SUB_UNIVERSE_SHARPE: 9F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.61, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+1.5%
  - 2020: S=1.79 (strong), ret=+7.2%
  - 2021: S=2.43 (strong), ret=+10.9%
  - 2022: S=1.85 (strong), ret=+10.6%
  - 2023: S=1.06 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 3.84% over 331 days (recovered)
- Annualized: return +6.8%, volatility 4.2% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew +0.97, excess kurtosis +8.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.39, max 2.79, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.88%; worst month: -2.51%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.11
- Sideways: S=1.15
- Bear: S=1.49

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_1080 / close)` S=-0.01, F=0.00, INFERIOR
Direction gap: -1.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_1080)`: S=-0.10, F=-0.04, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_1080 / close)`: S=-0.01, F=0.00, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_1080, 5))`: S=-1.60, F=-0.53, T=61.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_1080, 5))` | TOP3000 | 1.61 | 0.53 | 3.8% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_1080, 5))` | TOP1000 | 1.14 | 0.41 | 4.5% | 100% | mixed |
| `rank(ts_delta(implied_volatility_call_1080, 5))` | TOP500 | 0.62 | 0.18 | 13.2% | 80% | bull-only |
| `rank(implied_volatility_call_1080)` | TOP200 | 0.25 | 0.16 | 71.7% | 60% | bear-only |
| `rank(implied_volatility_call_1080)` | TOP500 | 0.21 | 0.12 | 69.8% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_1080, 5))` | TOP200 | 0.33 | 0.09 | 29.3% | 60% | bull-only |
| `rank(implied_volatility_call_1080)` | TOP1000 | 0.17 | 0.08 | 64.9% | 40% | bear-only |
| `rank(implied_volatility_call_1080)` | TOP3000 | 0.10 | 0.04 | 68.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_720: 0.998 (strongly positively correlated)
- implied_volatility_call_360: 0.947 (strongly positively correlated)
- implied_volatility_call_270: 0.924 (strongly positively correlated)
- implied_volatility_mean_1080: 0.915 (strongly positively correlated)
- implied_volatility_mean_720: 0.913 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.16 | 2.28 | +0.67 | +0.99 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.04 | 2.24 | +0.62 | +0.97 | yes |
| current_ratio | fundamental6 | -0.07 | 2.19 | +0.53 | +0.46 | yes |
| sales_estimate_count_quarterly | analyst4 | +0.08 | 2.12 | +0.51 | +0.81 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.08 | +0.47 | -0.42 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
