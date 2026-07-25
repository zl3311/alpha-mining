---
field: implied_volatility_mean_skew_120
dataset: option8
best_template: ts_mean
best_sharpe: 0.85
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.217
ann_vol: 0.082
hit_rate: 0.5247
rolling_sharpe_min: -2.944
rolling_sharpe_max: 2.346
redundancy_cluster: 13
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.1
---
# implied_volatility_mean_skew_120 (option8)

*Skew steepness for the implied volatility duration of 120 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_120)`: S=0.70, F=0.27, T=39.5%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_120 / close)`: S=0.63, F=0.36, T=17.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_120, 5))`: S=-0.09, F=-0.01, T=54.8%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_skew_120)`: S=-0.33, F=-0.13, T=23.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_120, 5))`: S=0.75, F=0.19, T=58.9%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_120, 63)`: S=0.44, F=0.11, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_120, 10)`: S=0.85, F=0.79, T=9.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_120, 22))`: S=-0.65, F=-0.16, T=42.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_120)`: S=-0.29, F=-0.12, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_120 / close)`: S=-0.84, F=-0.62, T=14.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.15 (moderate), ret=+3.3%
  - 2020: S=-1.57 (negative), ret=-8.2%
  - 2021: S=1.06 (moderate), ret=+13.4%
  - 2022: S=1.48 (moderate), ret=+15.0%
  - 2023: S=0.83 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 21.70% over 738 days (recovered)
- Annualized: return +5.7%, volatility 8.2% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.13, excess kurtosis +2.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.94, max 2.35, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.39%; worst month: -7.97%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.50
- Sideways: S=0.95
- Bear: S=-1.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_120, 5))` S=0.75, F=0.19, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_120)`: S=-0.29, F=-0.12, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_120 / close)`: S=-0.84, F=-0.62, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_120, 5))`: S=0.75, F=0.19, T=58.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_120)` | TOP3000 | 0.70 | 0.27 | 21.7% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_120)` | TOP1000 | 0.34 | 0.13 | 28.9% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_120)` | TOP500 | 0.30 | 0.12 | 22.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_90: 0.994 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.993 (strongly positively correlated)
- implied_volatility_mean_skew_60: 0.980 (strongly positively correlated)
- implied_volatility_mean_skew_270: 0.955 (strongly positively correlated)
- implied_volatility_mean_skew_30: 0.952 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
