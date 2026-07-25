---
field: pcr_oi_150
dataset: option9
best_template: rank_level
best_sharpe: 0.62
best_fitness: 0.37
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1676
ann_vol: 0.0708
hit_rate: 0.5263
rolling_sharpe_min: -1.074
rolling_sharpe_max: 3.919
redundancy_cluster: 77
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.43
---
# pcr_oi_150 (option9)

*Ratio of total put option open interest to total call option open interest for options expiring in 150 days, indicating longer-term put-call positioning*

## Signal Profile
- `rank(pcr_oi_150)`: S=0.62, F=0.37, T=9.4%, INFERIOR (TOP200)
- `rank(pcr_oi_150 / close)`: S=0.09, F=0.02, T=6.7%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_150, 5))`: S=-0.07, F=-0.01, T=27.9%, INFERIOR (TOP1000)
- `-rank(pcr_oi_150)`: S=-0.50, F=-0.20, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_150, 5))`: S=0.19, F=0.02, T=26.6%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_150, 63)`: S=0.55, F=0.20, T=13.4%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_150, 10)`: S=0.42, F=0.19, T=7.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_150, 22))`: S=-0.51, F=-0.15, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_150)`: S=-0.44, F=-0.17, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_150 / close)`: S=0.01, F=0.00, T=6.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.8%
  - 2020: S=3.47 (strong), ret=+21.8%
  - 2021: S=-0.83 (negative), ret=-8.2%
  - 2022: S=0.32 (weak), ret=+2.0%
  - 2023: S=1.10 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 16.76% over 1080 days (not yet recovered, ongoing at window end)
- Annualized: return +4.5%, volatility 7.1% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.23, excess kurtosis +2.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 3.92, latest 1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +4.62%; worst month: -4.95%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.54
- Sideways: S=0.67
- Bear: S=0.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(pcr_oi_150, 5))` S=0.19, F=0.02, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_150)`: S=-0.44, F=-0.17, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_150 / close)`: S=0.01, F=0.00, T=6.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_150, 5))`: S=0.19, F=0.02, T=26.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_150)` | TOP200 | 0.64 | 0.37 | 16.8% | 80% | all-weather |
| `rank(pcr_oi_150)` | TOP1000 | 0.49 | 0.20 | 8.0% | 80% | bull-only |
| `rank(pcr_oi_150)` | TOP500 | 0.46 | 0.19 | 8.8% | 60% | bull-only |
| `rank(pcr_oi_150)` | TOP3000 | 0.43 | 0.17 | 13.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_180: 0.856 (strongly positively correlated)
- pcr_oi_90: 0.564 (moderately positively correlated)
- pcr_oi_120: 0.495 (moderately positively correlated)
- anl4_epsa_flag: -0.309 (weakly negatively correlated)
- fnd6_cshtrq: -0.305 (weakly negatively correlated)

Redundancy cluster #77: 2 similar fields, mean |rho| 0.856 (representative: pcr_oi_180). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
