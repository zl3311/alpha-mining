---
field: pcr_oi_90
dataset: option9
best_template: rank_level
best_sharpe: 0.68
best_fitness: 0.42
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1225
ann_vol: 0.0731
hit_rate: 0.5304
rolling_sharpe_min: -1.245
rolling_sharpe_max: 3.339
negated_best_sharpe: 0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.62
---
# pcr_oi_90 (option9)

*Ratio of put open interest to call open interest for options expiring in 90 days, reflecting longer-term positioning*

## Signal Profile
- `rank(pcr_oi_90)`: S=0.68, F=0.42, T=12.7%, INFERIOR (TOP200)
- `rank(pcr_oi_90 / close)`: S=0.11, F=0.03, T=7.7%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_90, 5))`: S=0.08, F=0.01, T=28.2%, INFERIOR (TOP3000)
- `-rank(pcr_oi_90)`: S=-0.22, F=-0.06, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_90, 5))`: S=-0.08, F=-0.01, T=28.2%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_90, 63)`: S=0.38, F=0.10, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_90, 10)`: S=0.14, F=0.04, T=9.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_90, 22))`: S=-0.59, F=-0.18, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_90)`: S=-0.19, F=-0.05, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_90 / close)`: S=0.06, F=0.01, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.69, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+2.9%
  - 2020: S=2.86 (strong), ret=+20.0%
  - 2021: S=0.77 (moderate), ret=+7.1%
  - 2022: S=-0.63 (negative), ret=-4.7%
  - 2023: S=-0.11 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 12.25% over 793 days (not yet recovered, ongoing at window end)
- Annualized: return +5.0%, volatility 7.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.01, excess kurtosis +2.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 3.34, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.58%; worst month: -4.58%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.00
- Sideways: S=1.51
- Bear: S=0.72

## Negated Direction
Best negated: `rank(-1 * pcr_oi_90 / close)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_90)`: S=-0.19, F=-0.05, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_90 / close)`: S=0.06, F=0.01, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_90, 5))`: S=-0.08, F=-0.01, T=28.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_90)` | TOP200 | 0.69 | 0.42 | 12.2% | 60% | mixed |
| `rank(pcr_oi_90)` | TOP500 | 0.66 | 0.33 | 6.1% | 80% | mixed |
| `rank(pcr_oi_90)` | TOP1000 | 0.22 | 0.06 | 6.8% | 80% | bull-only |
| `rank(pcr_oi_90)` | TOP3000 | 0.19 | 0.05 | 15.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_150: 0.564 (moderately positively correlated)
- pcr_oi_180: 0.459 (moderately positively correlated)
- pcr_oi_120: 0.435 (moderately positively correlated)
- pcr_oi_60: 0.426 (moderately positively correlated)
- fn_entity_common_stock_shares_out_a: -0.284 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
