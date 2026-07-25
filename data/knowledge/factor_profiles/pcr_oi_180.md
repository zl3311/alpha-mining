---
field: pcr_oi_180
dataset: option9
best_template: rank_level
best_sharpe: 0.66
best_fitness: 0.41
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.236
ann_vol: 0.0738
hit_rate: 0.5085
rolling_sharpe_min: -2.194
rolling_sharpe_max: 3.883
redundancy_cluster: 77
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 4
direction_gap: -0.02
---
# pcr_oi_180 (option9)

*Ratio of total put option open interest to call option open interest for options expiring in 180 days, representing longer-term positioning*

## Signal Profile
- `rank(pcr_oi_180)`: S=0.66, F=0.41, T=10.8%, INFERIOR (TOP200)
- `rank(pcr_oi_180 / close)`: S=0.13, F=0.04, T=7.9%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_180, 5))`: S=-0.53, F=-0.12, T=30.3%, INFERIOR (TOP1000)
- `-rank(pcr_oi_180)`: S=-0.55, F=-0.23, T=9.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_180, 5))`: S=0.64, F=0.14, T=29.1%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_180, 63)`: S=0.49, F=0.16, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_180, 10)`: S=0.53, F=0.28, T=9.3%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_180, 22))`: S=-0.65, F=-0.21, T=19.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_180)`: S=-0.52, F=-0.21, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_180 / close)`: S=-0.04, F=-0.01, T=7.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.68, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+3.8%
  - 2020: S=3.43 (strong), ret=+22.4%
  - 2021: S=-1.19 (negative), ret=-12.0%
  - 2022: S=-0.33 (negative), ret=-2.3%
  - 2023: S=2.15 (strong), ret=+12.4%

## Risk & Drawdown
- Max drawdown: 23.60% over 1079 days (not yet recovered, ongoing at window end)
- Annualized: return +5.0%, volatility 7.4% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.05, excess kurtosis +2.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.19, max 3.88, latest 2.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.56%; worst month: -6.32%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.89
- Sideways: S=1.09
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(pcr_oi_180, 5))` S=0.64, F=0.14, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_180)`: S=-0.52, F=-0.21, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_180 / close)`: S=-0.04, F=-0.01, T=7.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_180, 5))`: S=0.64, F=0.14, T=29.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_180)` | TOP200 | 0.68 | 0.41 | 23.6% | 60% | mixed |
| `rank(pcr_oi_180)` | TOP1000 | 0.54 | 0.23 | 7.1% | 80% | bull-only |
| `rank(pcr_oi_180)` | TOP500 | 0.50 | 0.22 | 9.5% | 80% | bull-only |
| `rank(pcr_oi_180)` | TOP3000 | 0.51 | 0.21 | 12.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_150: 0.856 (strongly positively correlated)
- pcr_oi_90: 0.459 (moderately positively correlated)
- pcr_oi_120: 0.413 (moderately positively correlated)
- anl4_epsa_flag: -0.319 (weakly negatively correlated)
- fnd6_cshtrq: -0.304 (weakly negatively correlated)

Redundancy cluster #77: 2 similar fields, mean |rho| 0.856 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
