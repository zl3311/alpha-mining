---
field: implied_volatility_mean_skew_90
dataset: option8
best_template: ts_mean
best_sharpe: 0.86
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.245
ann_vol: 0.0825
hit_rate: 0.5126
rolling_sharpe_min: -3.316
rolling_sharpe_max: 2.28
redundancy_cluster: 13
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.23
---
# implied_volatility_mean_skew_90 (option8)

*Skew steepness for the implied volatility duration of 90 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_90)`: S=0.58, F=0.20, T=41.0%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_90 / close)`: S=0.67, F=0.38, T=18.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_90, 5))`: S=-0.12, F=-0.02, T=54.9%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_skew_90)`: S=-0.28, F=-0.09, T=25.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_90, 5))`: S=0.63, F=0.10, T=79.5%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_90, 63)`: S=0.37, F=0.08, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_90, 10)`: S=0.86, F=0.81, T=9.7%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_90, 22))`: S=-0.68, F=-0.18, T=43.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_90)`: S=-0.58, F=-0.20, T=41.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_90 / close)`: S=-0.86, F=-0.39, T=35.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 4F/23P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+3.2%
  - 2020: S=-2.00 (negative), ret=-10.7%
  - 2021: S=0.91 (moderate), ret=+11.5%
  - 2022: S=1.44 (moderate), ret=+14.6%
  - 2023: S=0.88 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 24.50% over 764 days (recovered)
- Annualized: return +4.8%, volatility 8.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.11, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.32, max 2.28, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.46%; worst month: -8.41%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.43
- Sideways: S=0.84
- Bear: S=-1.97

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_90, 5))` S=0.63, F=0.10, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_90)`: S=-0.58, F=-0.20, T=41.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_90 / close)`: S=-0.86, F=-0.39, T=35.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_90, 5))`: S=0.63, F=0.10, T=79.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_90)` | TOP3000 | 0.58 | 0.20 | 24.5% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_90)` | TOP1000 | 0.28 | 0.09 | 30.3% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_90)` | TOP500 | 0.24 | 0.09 | 24.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_120: 0.994 (strongly positively correlated)
- implied_volatility_mean_skew_60: 0.991 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.983 (strongly positively correlated)
- implied_volatility_mean_skew_30: 0.963 (strongly positively correlated)
- implied_volatility_mean_skew_270: 0.945 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
