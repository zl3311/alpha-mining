---
field: implied_volatility_call_30 - implied_volatility_put_30
dataset: option8
best_template: rank_level
best_sharpe: 1.75
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 3
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0421
ann_vol: 0.0392
hit_rate: 0.5676
rolling_sharpe_min: 0.369
rolling_sharpe_max: 3.873
top_merge_partner: fnd6_itci
redundancy_cluster: 3
negated_best_sharpe: -0.06
negated_best_template: neg_rank_level
negated_best_fitness: -0.02
n_negated_sims: 2
direction_gap: -1.81
---
# implied_volatility_call_30 - implied_volatility_put_30 (option8)


## Signal Profile
- `rank(implied_volatility_call_30 - implied_volatility_put_30)`: S=1.75, F=0.65, T=49.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30 - implied_volatility_put_30, 5))`: S=-0.34, F=-0.04, T=75.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_30 - implied_volatility_put_30)`: S=-0.06, F=-0.02, T=12.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/0P
- HIGH_TURNOVER: 1F/2P
- LOW_FITNESS: 3F/0P
- LOW_SHARPE: 2F/1P
- LOW_SUB_UNIVERSE_SHARPE: 2F/1P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.22 (moderate), ret=+3.3%
  - 2020: S=1.45 (moderate), ret=+5.2%
  - 2021: S=2.00 (strong), ret=+9.0%
  - 2022: S=2.84 (strong), ret=+13.7%
  - 2023: S=0.85 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 4.21% over 144 days (recovered)
- Annualized: return +6.9%, volatility 3.9% (fraction of booksize)
- Hit rate: 56.8% positive days
- Tail shape: skew -0.52, excess kurtosis +5.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.37, max 3.87, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.39%; worst month: -2.51%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.84
- Sideways: S=1.09
- Bear: S=1.26

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_30 - implied_volatility_put_30)` S=-0.06, F=-0.02, INFERIOR
Direction gap: -1.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_30 - implied_volatility_put_30)`: S=-0.06, F=-0.02, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30 - implied_volatility_put_30, 5))`: S=-0.34, F=-0.04, T=75.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_call_30 - implied_volatility_put_30)` | TOP3000 | 1.76 | 0.65 | 4.2% | 100% | all-weather |

## Correlation Notes
Top correlates:
- implied_volatility_call_270 - implied_volatility_put_270: 0.739 (strongly positively correlated)
- implied_volatility_mean_skew_10: 0.490 (moderately positively correlated)
- implied_volatility_mean_skew_720: 0.483 (moderately positively correlated)
- implied_volatility_mean_skew_1080: 0.480 (moderately positively correlated)
- implied_volatility_mean_skew_30: 0.476 (moderately positively correlated)

Redundancy cluster #3: 2 similar fields, mean |rho| 0.739 (representative: implied_volatility_call_270 - implied_volatility_put_270). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_itci | fundamental_tax_credit | +0.12 | 2.52 | +0.51 | -0.52 | yes |
| implied_volatility_put_90 | option8 | -0.01 | 2.46 | +0.69 | +0.86 | no |
| sales_estimate_count_quarterly | analyst4 | +0.10 | 2.24 | +0.48 | +0.79 | yes |
| implied_volatility_put_120 | option8 | -0.00 | 2.39 | +0.63 | +0.84 | no |
| anl4_qf_az_wol_spfc | analyst4 | -0.02 | 2.16 | +0.40 | -0.77 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_value_norm, trade_when
