---
field: total_goodwill_reported_value
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.45
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1633
ann_vol: 0.0778
hit_rate: 0.4874
rolling_sharpe_min: -1.535
rolling_sharpe_max: 1.77
negated_best_sharpe: 0.45
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.23
---
# total_goodwill_reported_value (analyst4)

*Total Goodwill - Actual Value in Millions*

## Signal Profile
- `rank(total_goodwill_reported_value)`: S=0.06, F=0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(total_goodwill_reported_value / close)`: S=0.22, F=0.08, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(total_goodwill_reported_value, 5))`: S=0.14, F=0.02, T=38.5%, INFERIOR (TOP1000)
- `-rank(total_goodwill_reported_value)`: S=0.21, F=0.10, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_goodwill_reported_value, 5))`: S=0.60, F=0.25, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(total_goodwill_reported_value, 63)`: S=0.13, F=0.03, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(total_goodwill_reported_value, 10)`: S=-0.38, F=-0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(total_goodwill_reported_value, 22))`: S=-0.22, F=-0.06, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_reported_value)`: S=0.45, F=0.33, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_reported_value / close)`: S=0.36, F=0.22, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.11 (weak), ret=+0.6%
  - 2020: S=-1.20 (negative), ret=-10.4%
  - 2021: S=0.72 (moderate), ret=+6.9%
  - 2022: S=1.24 (moderate), ret=+9.9%
  - 2023: S=0.21 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 16.33% over 794 days (recovered)
- Annualized: return +1.6%, volatility 7.8% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.30, excess kurtosis +1.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 1.77, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.34%; worst month: -3.39%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.79
- Sideways: S=-0.11
- Bear: S=-2.47

## Negated Direction
Best negated: `rank(-1 * total_goodwill_reported_value)` S=0.45, F=0.33, INFERIOR
Direction gap: +0.23 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * total_goodwill_reported_value)`: S=0.45, F=0.33, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_reported_value / close)`: S=0.36, F=0.22, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_goodwill_reported_value, 5))`: S=0.60, F=0.25, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(total_goodwill_reported_value / close)` | TOP3000 | 0.21 | 0.08 | 16.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- total_goodwill_actual_value: 1.000 (strongly positively correlated)
- anl4_totgw_mean: 0.946 (strongly positively correlated)
- anl4_totgw_median: 0.946 (strongly positively correlated)
- anl4_totgw_high: 0.946 (strongly positively correlated)
- anl4_totgw_low: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
