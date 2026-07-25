---
field: pcr_oi_360
dataset: option9
best_template: rank_level
best_sharpe: 0.34
best_fitness: 0.11
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1371
ann_vol: 0.0402
hit_rate: 0.5109
rolling_sharpe_min: -3.123
rolling_sharpe_max: 2.365
negated_best_sharpe: 0.09
negated_best_template: neg_rank
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.25
---
# pcr_oi_360 (option9)

*Ratio of total put option open interest to call option open interest for options expiring in 360 days*

## Signal Profile
- `rank(pcr_oi_360)`: S=0.34, F=0.11, T=8.2%, INFERIOR (TOP3000)
- `rank(pcr_oi_360 / close)`: S=-0.06, F=-0.01, T=7.8%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_360, 5))`: S=0.39, F=0.07, T=32.8%, INFERIOR (TOP1000)
- `-rank(pcr_oi_360)`: S=0.09, F=0.02, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_360, 5))`: S=-0.06, F=0.00, T=32.7%, INFERIOR (TOP3000)
- `ts_zscore(pcr_oi_360, 22)`: S=0.23, F=0.04, T=21.2%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_360, 10)`: S=-0.41, F=-0.19, T=9.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_360, 22))`: S=0.04, F=0.00, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_360)`: S=-0.34, F=-0.11, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_360 / close)`: S=0.06, F=0.01, T=8.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.33, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.91 (strong), ret=+4.0%
  - 2020: S=-1.95 (negative), ret=-6.4%
  - 2021: S=0.19 (weak), ret=+0.9%
  - 2022: S=1.31 (moderate), ret=+6.6%
  - 2023: S=0.36 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 13.71% over 1116 days (recovered)
- Annualized: return +1.3%, volatility 4.0% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.03, excess kurtosis +0.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.12, max 2.37, latest 0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.97%; worst month: -2.37%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.17
- Sideways: S=1.16
- Bear: S=-2.44

## Negated Direction
Best negated: `-rank(pcr_oi_360)` S=0.09, F=0.02, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_360)`: S=-0.34, F=-0.11, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_360 / close)`: S=0.06, F=0.01, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_360, 5))`: S=-0.06, F=0.00, T=32.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_360)` | TOP3000 | 0.33 | 0.11 | 13.7% | 80% | bull-only |
| `rank(ts_delta(pcr_oi_360, 5))` | TOP1000 | 0.39 | 0.07 | 5.1% | 60% | weak |
| `rank(pcr_oi_360)` | TOP500 | 0.09 | 0.02 | 17.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_270: 0.974 (strongly positively correlated)
- pcr_oi_720: 0.959 (strongly positively correlated)
- pcr_oi_1080: 0.948 (strongly positively correlated)
- pcr_oi_all: 0.881 (strongly positively correlated)
- cap: 0.819 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
