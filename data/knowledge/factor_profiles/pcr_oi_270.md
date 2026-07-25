---
field: pcr_oi_270
dataset: option9
cluster: option9_ratio
coverage: 0.9838
community_alphas: 12721
best_template: ts_zscore
best_sharpe: 0.49
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1286
ann_vol: 0.0384
hit_rate: 0.5198
rolling_sharpe_min: -2.878
rolling_sharpe_max: 2.529
negated_best_sharpe: 0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.43
---
# pcr_oi_270 (option9)

*Ratio of put open interest to call open interest for options expiring in 270 days, indicating longer-term position skew*

## Signal Profile
- `rank(pcr_oi_270)`: S=0.38, F=0.13, T=8.7%, INFERIOR (TOP3000)
- `rank(pcr_oi_270 / close)`: S=0.00, F=0.00, T=8.9%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_270, 5))`: S=-0.08, F=-0.01, T=32.9%, INFERIOR (TOP3000)
- `-rank(pcr_oi_270)`: S=-0.06, F=-0.01, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_270, 5))`: S=0.08, F=0.01, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_270, 63)`: S=0.49, F=0.15, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_270, 10)`: S=-0.13, F=-0.03, T=10.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_270, 22))`: S=-0.40, F=-0.10, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_270)`: S=-0.38, F=-0.13, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_270 / close)`: S=0.06, F=0.01, T=8.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.42 (strong), ret=+5.1%
  - 2020: S=-1.97 (negative), ret=-6.5%
  - 2021: S=0.45 (weak), ret=+2.2%
  - 2022: S=1.07 (moderate), ret=+4.8%
  - 2023: S=0.43 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 12.86% over 1249 days (recovered)
- Annualized: return +1.4%, volatility 3.8% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.01, excess kurtosis +0.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.88, max 2.53, latest 0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.85%; worst month: -2.25%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.26
- Sideways: S=1.29
- Bear: S=-2.45

## Negated Direction
Best negated: `rank(-1 * pcr_oi_270 / close)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_270)`: S=-0.38, F=-0.13, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_270 / close)`: S=0.06, F=0.01, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_270, 5))`: S=0.08, F=0.01, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_270)` | TOP3000 | 0.37 | 0.13 | 12.9% | 80% | bull-only |
| `rank(pcr_oi_270)` | TOP500 | 0.21 | 0.06 | 9.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_360: 0.974 (strongly positively correlated)
- pcr_oi_720: 0.918 (strongly positively correlated)
- pcr_oi_1080: 0.906 (strongly positively correlated)
- pcr_oi_all: 0.848 (strongly positively correlated)
- cap: 0.782 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
