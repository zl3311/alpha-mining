---
field: max_total_assets_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.5
best_fitness: 0.33
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3235
ann_vol: 0.1061
hit_rate: 0.4583
rolling_sharpe_min: -3.231
rolling_sharpe_max: 2.273
negated_best_sharpe: 0.5
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.0
---
# max_total_assets_guidance (analyst4)

*The maximum guidance value for Total Assets.*

## Signal Profile
- `rank(max_total_assets_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP500)
- `rank(max_total_assets_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_total_assets_guidance, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(max_total_assets_guidance)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_total_assets_guidance, 5))`: S=0.24, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_total_assets_guidance, 63)`: S=0.14, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(max_total_assets_guidance, 10)`: S=-0.10, F=-0.02, T=26.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_total_assets_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_total_assets_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * max_total_assets_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.33 (moderate), ret=+6.9%
  - 2020: S=-1.80 (negative), ret=-14.3%
  - 2021: S=1.03 (moderate), ret=+18.2%
  - 2022: S=1.36 (moderate), ret=+13.9%
  - 2023: S=-0.06 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 32.35% over 770 days (recovered)
- Annualized: return +5.0%, volatility 10.6% (fraction of booksize)
- Hit rate: 45.8% positive days
- Tail shape: skew +0.01, excess kurtosis +3.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.23, max 2.27, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.00%; worst month: -10.38%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.19
- Sideways: S=1.17
- Bear: S=-2.45

## Negated Direction
Best negated: `rank(-1 * max_total_assets_guidance)` S=0.50, F=0.33, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_total_assets_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * max_total_assets_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_total_assets_guidance, 5))`: S=0.24, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_total_assets_guidance)` | TOP500 | 0.47 | 0.33 | 32.4% | 60% | bull-only |
| `rank(ts_delta(max_total_assets_guidance, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(max_total_assets_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(max_total_assets_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 1.000 (strongly positively correlated)
- shareholders_equity_min_guidance: 1.000 (strongly positively correlated)
- min_total_assets_guidance: 1.000 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 1.000 (strongly positively correlated)
- shareholders_equity_max_guidance: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
