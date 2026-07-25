---
field: pcr_oi_720
dataset: option9
best_template: rank_level
best_sharpe: 0.58
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1138
ann_vol: 0.0387
hit_rate: 0.5247
rolling_sharpe_min: -2.805
rolling_sharpe_max: 2.882
redundancy_cluster: 82
negated_best_sharpe: 0.06
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.52
---
# pcr_oi_720 (option9)

*Ratio of put open interest to call open interest for options expiring in 720 days, indicating very long-term option sentiment*

## Signal Profile
- `rank(pcr_oi_720)`: S=0.58, F=0.24, T=8.0%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_720, 5))`: S=-0.13, F=-0.01, T=33.5%, INFERIOR (TOP3000)
- `-rank(pcr_oi_720)`: S=0.06, F=0.01, T=7.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_720, 5))`: S=0.13, F=0.01, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_720, 63)`: S=0.34, F=0.09, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_720, 10)`: S=0.19, F=0.06, T=7.9%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_720, 22))`: S=-0.61, F=-0.18, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_720)`: S=-0.58, F=-0.24, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_720 / close)`: S=-0.13, F=-0.03, T=8.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.77 (strong), ret=+5.8%
  - 2020: S=-2.12 (negative), ret=-6.2%
  - 2021: S=0.68 (moderate), ret=+2.9%
  - 2022: S=1.52 (strong), ret=+8.0%
  - 2023: S=0.12 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 11.38% over 758 days (recovered)
- Annualized: return +2.2%, volatility 3.9% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.02, excess kurtosis +0.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.81, max 2.88, latest -0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.96%; worst month: -2.46%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.12
- Sideways: S=1.45
- Bear: S=-2.04

## Negated Direction
Best negated: `-rank(pcr_oi_720)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_720)`: S=-0.58, F=-0.24, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_720 / close)`: S=-0.13, F=-0.03, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_720, 5))`: S=0.13, F=0.01, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_720)` | TOP3000 | 0.57 | 0.24 | 11.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_1080: 0.995 (strongly positively correlated)
- pcr_oi_360: 0.959 (strongly positively correlated)
- pcr_oi_270: 0.918 (strongly positively correlated)
- pcr_oi_all: 0.869 (strongly positively correlated)
- anl4_qfv4_eps_high: 0.802 (strongly positively correlated)

Redundancy cluster #82: 3 similar fields, mean |rho| 0.844 (representative: pcr_oi_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
