---
field: fscore_bfl_value
dataset: model16
best_template: rank_level
best_sharpe: 0.44
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1558
ann_vol: 0.0926
hit_rate: 0.4858
rolling_sharpe_min: -1.346
rolling_sharpe_max: 2.131
negated_best_sharpe: -0.4
negated_best_template: rank_neg_delta
negated_best_fitness: -0.17
n_negated_sims: 4
direction_gap: -0.84
---
# fscore_bfl_value (model16)

*Valuation composite indicating how under- or overpriced a stock is versus common valuation measures; higher is better (cheaper) (0–100)*

## Signal Profile
- `rank(fscore_bfl_value)`: S=0.44, F=0.25, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fscore_bfl_value, 5))`: S=0.08, F=0.01, T=15.6%, INFERIOR (TOP500)
- `-rank(fscore_bfl_value)`: S=-0.36, F=-0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_value, 5))`: S=-0.40, F=-0.17, T=15.2%, INFERIOR (TOP3000)
- `ts_zscore(fscore_bfl_value, 22)`: S=0.47, F=0.21, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_value, 10)`: S=0.34, F=0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_value, 22))`: S=0.46, F=0.20, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_value)`: S=-0.44, F=-0.25, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_value / close)`: S=-0.47, F=-0.31, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.43, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.36 (negative), ret=-2.9%
  - 2020: S=0.19 (weak), ret=+2.5%
  - 2021: S=1.19 (moderate), ret=+10.0%
  - 2022: S=1.31 (moderate), ret=+9.7%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 15.58% over 474 days (recovered)
- Annualized: return +3.9%, volatility 9.3% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.60, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.35, max 2.13, latest 0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +5.14%; worst month: -6.01%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.96
- Sideways: S=-1.00
- Bear: S=0.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(fscore_bfl_value, 5))` S=-0.40, F=-0.17, INFERIOR
Direction gap: -0.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fscore_bfl_value)`: S=-0.44, F=-0.25, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_value / close)`: S=-0.47, F=-0.31, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_value, 5))`: S=-0.40, F=-0.17, T=15.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fscore_bfl_value)` | TOP3000 | 0.43 | 0.25 | 15.6% | 80% | mixed |
| `rank(fscore_bfl_value)` | TOP1000 | 0.34 | 0.19 | 13.4% | 40% | mixed |
| `rank(fscore_bfl_value)` | TOP500 | 0.12 | 0.05 | 16.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sales_ps: 0.845 (strongly positively correlated)
- anl4_bvps_median: 0.843 (strongly positively correlated)
- anl4_bvps_mean: 0.842 (strongly positively correlated)
- anl4_bvps_high: 0.842 (strongly positively correlated)
- anl4_bvps_low: 0.842 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
