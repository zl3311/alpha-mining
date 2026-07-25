---
field: pcr_oi_30
dataset: option9
best_template: ts_mean
best_sharpe: 0.56
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.127
ann_vol: 0.0377
hit_rate: 0.5004
rolling_sharpe_min: -2.585
rolling_sharpe_max: 2.251
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.58
---
# pcr_oi_30 (option9)

*Ratio of put open interest to call open interest for options expiring in 30 days, reflecting medium-term option positioning*

## Signal Profile
- `rank(pcr_oi_30)`: S=0.28, F=0.08, T=13.4%, INFERIOR (TOP3000)
- `rank(pcr_oi_30 / close)`: S=0.09, F=0.02, T=13.7%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_30, 5))`: S=0.28, F=0.04, T=32.2%, INFERIOR (TOP3000)
- `-rank(pcr_oi_30)`: S=-0.13, F=-0.02, T=17.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_30, 5))`: S=-0.28, F=-0.04, T=32.2%, INFERIOR (TOP3000)
- `ts_zscore(pcr_oi_30, 22)`: S=0.15, F=0.02, T=26.1%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_30, 10)`: S=0.56, F=0.29, T=13.9%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_30, 22))`: S=0.02, F=0.00, T=25.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_30)`: S=-0.28, F=-0.08, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_30 / close)`: S=-0.02, F=0.00, T=11.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+0.5%
  - 2020: S=-2.37 (negative), ret=-8.4%
  - 2021: S=1.48 (moderate), ret=+7.1%
  - 2022: S=1.13 (moderate), ret=+5.1%
  - 2023: S=0.23 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 12.70% over 1074 days (recovered)
- Annualized: return +1.0%, volatility 3.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.21, excess kurtosis +1.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.58, max 2.25, latest -0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +2.67%; worst month: -2.67%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.78
- Sideways: S=0.64
- Bear: S=-1.70

## Negated Direction
Best negated: `rank(-1 * pcr_oi_30 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_30)`: S=-0.28, F=-0.08, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_30 / close)`: S=-0.02, F=0.00, T=11.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_30, 5))`: S=-0.28, F=-0.04, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_30)` | TOP3000 | 0.28 | 0.08 | 12.7% | 80% | bull-only |
| `rank(pcr_oi_30)` | TOP500 | 0.29 | 0.07 | 9.1% | 80% | weak |
| `rank(ts_delta(pcr_oi_30, 5))` | TOP3000 | 0.27 | 0.04 | 3.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- pcr_oi_20: 0.962 (strongly positively correlated)
- pcr_oi_10: 0.925 (strongly positively correlated)
- pcr_oi_all: 0.891 (strongly positively correlated)
- pcr_oi_360: 0.773 (strongly positively correlated)
- pcr_oi_720: 0.756 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
