---
field: pcr_oi_120
dataset: option9
best_template: rank_level
best_sharpe: 0.5
best_fitness: 0.22
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0756
ann_vol: 0.0475
hit_rate: 0.5279
rolling_sharpe_min: -1.162
rolling_sharpe_max: 3.121
negated_best_sharpe: 0.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.44
---
# pcr_oi_120 (option9)

*Ratio of total put option open interest to total call option open interest for options expiring in 120 days, indicating longer-term put-call positioning*

## Signal Profile
- `rank(pcr_oi_120)`: S=0.50, F=0.22, T=8.3%, INFERIOR (TOP500)
- `rank(pcr_oi_120 / close)`: S=0.11, F=0.03, T=6.1%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_120, 5))`: S=-0.06, F=0.00, T=24.8%, INFERIOR (TOP3000)
- `-rank(pcr_oi_120)`: S=-0.36, F=-0.12, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_120, 5))`: S=0.06, F=0.00, T=24.8%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_120, 63)`: S=0.57, F=0.21, T=12.7%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_120, 10)`: S=0.33, F=0.13, T=6.8%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_120, 22))`: S=-0.68, F=-0.23, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_120)`: S=-0.33, F=-0.11, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_120 / close)`: S=0.03, F=0.00, T=5.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.1%
  - 2020: S=2.20 (strong), ret=+8.9%
  - 2021: S=0.49 (weak), ret=+3.6%
  - 2022: S=-0.83 (negative), ret=-3.6%
  - 2023: S=0.87 (moderate), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 7.56% over 855 days (not yet recovered, ongoing at window end)
- Annualized: return +2.4%, volatility 4.8% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.11, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 3.12, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.96%; worst month: -3.18%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.22
- Sideways: S=0.92
- Bear: S=-0.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(pcr_oi_120, 5))` S=0.06, F=0.00, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_120)`: S=-0.33, F=-0.11, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_120 / close)`: S=0.03, F=0.00, T=5.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_120, 5))`: S=0.06, F=0.00, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_120)` | TOP500 | 0.51 | 0.22 | 7.6% | 80% | bull-only |
| `rank(pcr_oi_120)` | TOP200 | 0.43 | 0.19 | 15.1% | 60% | mixed |
| `rank(pcr_oi_120)` | TOP1000 | 0.36 | 0.12 | 7.3% | 60% | bull-only |
| `rank(pcr_oi_120)` | TOP3000 | 0.33 | 0.11 | 14.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_60: 0.613 (moderately positively correlated)
- pcr_oi_150: 0.495 (moderately positively correlated)
- pcr_vol_360: 0.475 (moderately positively correlated)
- pcr_vol_all: 0.456 (moderately positively correlated)
- pcr_vol_10: 0.453 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
