---
field: pcr_oi_60
dataset: option9
best_template: rank_level
best_sharpe: 0.62
best_fitness: 0.25
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0558
ann_vol: 0.0496
hit_rate: 0.5166
rolling_sharpe_min: -1.106
rolling_sharpe_max: 1.944
negated_best_sharpe: 0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.6
---
# pcr_oi_60 (option9)

*Ratio of put open interest to call open interest for options expiring in 60 days, reflecting medium-to-long term option positioning*

## Signal Profile
- `rank(pcr_oi_60)`: S=0.62, F=0.25, T=18.7%, INFERIOR (TOP500)
- `rank(pcr_oi_60 / close)`: S=0.08, F=0.02, T=13.0%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_60, 5))`: S=0.69, F=0.14, T=34.4%, INFERIOR (TOP3000)
- `-rank(pcr_oi_60)`: S=-0.30, F=-0.08, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_60, 5))`: S=-0.69, F=-0.14, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(pcr_oi_60, 22)`: S=0.17, F=0.02, T=27.6%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_60, 10)`: S=0.30, F=0.12, T=14.7%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_60, 22))`: S=-0.07, F=-0.01, T=25.5%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_60)`: S=-0.30, F=-0.09, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_60 / close)`: S=0.02, F=0.00, T=11.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.30 (weak), ret=+0.9%
  - 2020: S=0.70 (moderate), ret=+3.0%
  - 2021: S=1.50 (strong), ret=+11.1%
  - 2022: S=-0.31 (negative), ret=-1.5%
  - 2023: S=0.39 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 5.58% over 204 days (recovered)
- Annualized: return +3.1%, volatility 5.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.01, excess kurtosis +2.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 1.94, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.73%; worst month: -3.32%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.50
- Sideways: S=0.73
- Bear: S=0.67

## Negated Direction
Best negated: `rank(-1 * pcr_oi_60 / close)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_60)`: S=-0.30, F=-0.09, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_60 / close)`: S=0.02, F=0.00, T=11.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_60, 5))`: S=-0.69, F=-0.14, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_60)` | TOP500 | 0.62 | 0.25 | 5.6% | 80% | mixed |
| `rank(pcr_oi_60)` | TOP200 | 0.52 | 0.22 | 12.2% | 80% | bear-only |
| `rank(ts_delta(pcr_oi_60, 5))` | TOP3000 | 0.69 | 0.14 | 5.7% | 80% | mixed |
| `rank(pcr_oi_60)` | TOP3000 | 0.30 | 0.09 | 12.7% | 80% | bull-only |
| `rank(pcr_oi_60)` | TOP1000 | 0.29 | 0.08 | 6.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_120: 0.613 (moderately positively correlated)
- pcr_vol_10: 0.515 (moderately positively correlated)
- pcr_vol_30: 0.471 (moderately positively correlated)
- pcr_vol_360: 0.449 (moderately positively correlated)
- pcr_vol_all: 0.435 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
