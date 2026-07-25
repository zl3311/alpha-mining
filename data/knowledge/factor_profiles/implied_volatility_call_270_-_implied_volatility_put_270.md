---
field: implied_volatility_call_270 - implied_volatility_put_270
dataset: option8
best_template: rank_level
best_sharpe: 1.79
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 3
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0367
ann_vol: 0.0425
hit_rate: 0.5684
rolling_sharpe_min: 0.434
rolling_sharpe_max: 3.182
top_merge_partner: fn_liab_fair_val_l2_q
redundancy_cluster: 3
negated_best_sharpe: -0.05
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 2
direction_gap: -1.84
---
# implied_volatility_call_270 - implied_volatility_put_270 (option8)


## Signal Profile
- `rank(implied_volatility_call_270 - implied_volatility_put_270)`: S=1.79, F=0.87, T=32.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_270 - implied_volatility_put_270, 5))`: S=-0.56, F=-0.08, T=72.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_270 - implied_volatility_put_270)`: S=-0.05, F=-0.01, T=9.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/0P
- HIGH_TURNOVER: 1F/2P
- LOW_FITNESS: 3F/0P
- LOW_SHARPE: 2F/1P
- LOW_SUB_UNIVERSE_SHARPE: 2F/1P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.81, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.15 (moderate), ret=+4.0%
  - 2020: S=2.52 (strong), ret=+9.2%
  - 2021: S=2.17 (strong), ret=+11.0%
  - 2022: S=2.08 (strong), ret=+10.1%
  - 2023: S=0.94 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 3.67% over 88 days (recovered)
- Annualized: return +7.7%, volatility 4.2% (fraction of booksize)
- Hit rate: 56.8% positive days
- Tail shape: skew -0.16, excess kurtosis +2.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.43, max 3.18, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.11%; worst month: -2.47%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.87
- Sideways: S=1.80
- Bear: S=1.79

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_270 - implied_volatility_put_270)` S=-0.05, F=-0.01, INFERIOR
Direction gap: -1.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_270 - implied_volatility_put_270)`: S=-0.05, F=-0.01, T=9.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_270 - implied_volatility_put_270, 5))`: S=-0.56, F=-0.08, T=72.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_call_270 - implied_volatility_put_270)` | TOP3000 | 1.81 | 0.87 | 3.7% | 100% | all-weather |

## Correlation Notes
Top correlates:
- implied_volatility_call_30 - implied_volatility_put_30: 0.739 (strongly positively correlated)
- implied_volatility_mean_skew_1080: 0.506 (moderately positively correlated)
- implied_volatility_mean_skew_720: 0.506 (moderately positively correlated)
- implied_volatility_mean_skew_360: 0.465 (moderately positively correlated)
- implied_volatility_mean_skew_10: 0.441 (moderately positively correlated)

Redundancy cluster #3: 2 similar fields, mean |rho| 0.739 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_liab_fair_val_l2_q | fundamental2 | +0.02 | 2.26 | +0.46 | -0.86 | yes |
| implied_volatility_put_90 | option8 | +0.01 | 2.48 | +0.67 | +0.88 | no |
| fn_derivative_fair_value_of_derivative_asset_a | fundamental2 | -0.21 | 2.29 | +0.48 | -0.08 | yes |
| fn_assets_fair_val_l2_q | fundamental2 | -0.05 | 2.21 | +0.41 | -0.78 | yes |
| implied_volatility_put_120 | option8 | -0.00 | 2.44 | +0.63 | +0.86 | no |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_value_norm, trade_when
