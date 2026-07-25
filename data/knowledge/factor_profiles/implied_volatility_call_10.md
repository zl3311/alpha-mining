---
field: implied_volatility_call_10
dataset: option8
best_template: rank_delta
best_sharpe: 1.04
best_fitness: 0.53
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1721
ann_vol: 0.1117
hit_rate: 0.5393
rolling_sharpe_min: 0.066
rolling_sharpe_max: 2.638
top_merge_partner: anl4_fcf_high
redundancy_cluster: 15
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.04
---
# implied_volatility_call_10 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 10 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_10)`: S=0.36, F=0.30, T=12.6%, INFERIOR (TOP200)
- `rank(implied_volatility_call_10 / close)`: S=0.12, F=0.04, T=5.9%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_10, 5))`: S=1.04, F=0.53, T=44.2%, INFERIOR (TOP200)
- `-rank(implied_volatility_call_10)`: S=-0.16, F=-0.08, T=12.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_10, 5))`: S=-1.31, F=-0.44, T=58.1%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_10, 22)`: S=0.74, F=0.29, T=34.1%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_10, 10)`: S=-0.03, F=-0.01, T=6.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_10, 22))`: S=0.53, F=0.16, T=35.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_10)`: S=-0.07, F=-0.02, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_10 / close)`: S=0.00, F=0.00, T=8.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.03, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.05 (moderate), ret=+6.5%
  - 2020: S=1.68 (strong), ret=+17.1%
  - 2021: S=0.53 (moderate), ret=+7.0%
  - 2022: S=1.18 (moderate), ret=+16.3%
  - 2023: S=1.02 (moderate), ret=+9.6%

## Risk & Drawdown
- Max drawdown: 17.21% over 298 days (recovered)
- Annualized: return +11.6%, volatility 11.2% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew +0.34, excess kurtosis +3.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.07, max 2.64, latest 1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.20%; worst month: -8.49%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.06
- Sideways: S=1.03
- Bear: S=1.03

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_10 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.04 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_10)`: S=-0.07, F=-0.02, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_10 / close)`: S=0.00, F=0.00, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_10, 5))`: S=-1.31, F=-0.44, T=58.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_10, 5))` | TOP200 | 1.03 | 0.53 | 17.2% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_10, 5))` | TOP3000 | 1.33 | 0.44 | 5.4% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_10, 5))` | TOP1000 | 1.06 | 0.42 | 9.8% | 100% | all-weather |
| `rank(implied_volatility_call_10)` | TOP200 | 0.37 | 0.30 | 74.8% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_10, 5))` | TOP500 | 0.73 | 0.27 | 13.0% | 80% | all-weather |
| `rank(implied_volatility_call_10)` | TOP500 | 0.23 | 0.13 | 74.2% | 40% | bear-only |
| `rank(implied_volatility_call_10)` | TOP1000 | 0.17 | 0.08 | 66.9% | 40% | bear-only |
| `rank(implied_volatility_call_10)` | TOP3000 | 0.08 | 0.02 | 69.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_10: 0.980 (strongly positively correlated)
- implied_volatility_put_10: 0.954 (strongly positively correlated)
- implied_volatility_mean_20: 0.767 (strongly positively correlated)
- implied_volatility_put_20: 0.743 (strongly positively correlated)
- implied_volatility_call_20: 0.554 (moderately positively correlated)

Redundancy cluster #15: 5 similar fields, mean |rho| 0.853 (representative: implied_volatility_put_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_fcf_high | analyst4 | -0.13 | 1.53 | +0.50 | -0.81 | yes |
| fnd6_dpvieb | fundamental6 | -0.12 | 1.55 | +0.52 | -0.62 | yes |
| fnd6_newa1v1300_dpact | fundamental6 | -0.12 | 1.55 | +0.51 | -0.63 | yes |
| anl4_tot_gw_ft | analyst4 | -0.10 | 1.52 | +0.48 | -0.61 | yes |
| fn_accum_depr_depletion_and_amortization_ppne_q | fundamental2 | -0.11 | 1.51 | +0.47 | -0.60 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
