---
field: min_investing_cashflow_guidance_2
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.52
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3944
ann_vol: 0.1244
hit_rate: 0.4591
rolling_sharpe_min: -2.634
rolling_sharpe_max: 2.305
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.14
---
# min_investing_cashflow_guidance_2 (analyst4)

*Cash Flow From Investing - Minimum guidance value for the annual period*

## Signal Profile
- `rank(min_investing_cashflow_guidance_2)`: S=0.38, F=0.24, T=3.5%, INFERIOR (TOP500)
- `rank(min_investing_cashflow_guidance_2 / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_investing_cashflow_guidance_2, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(min_investing_cashflow_guidance_2)`: S=0.03, F=0.01, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_investing_cashflow_guidance_2, 5))`: S=0.25, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(min_investing_cashflow_guidance_2, 63)`: S=0.15, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(min_investing_cashflow_guidance_2, 10)`: S=-0.02, F=0.00, T=22.9%, INFERIOR (TOP3000)
- `rank(ts_rank(min_investing_cashflow_guidance_2, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_investing_cashflow_guidance_2)`: S=0.52, F=0.38, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * min_investing_cashflow_guidance_2 / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.33 (moderate), ret=+6.9%
  - 2020: S=-1.80 (negative), ret=-14.3%
  - 2021: S=0.69 (moderate), ret=+15.6%
  - 2022: S=1.36 (moderate), ret=+14.0%
  - 2023: S=-0.07 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 39.44% over 789 days (recovered)
- Annualized: return +4.5%, volatility 12.4% (fraction of booksize)
- Hit rate: 45.9% positive days
- Tail shape: skew -0.61, excess kurtosis +11.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.63, max 2.31, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.02%; worst month: -12.98%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.17
- Sideways: S=1.27
- Bear: S=-1.76

## Negated Direction
Best negated: `rank(-1 * min_investing_cashflow_guidance_2)` S=0.52, F=0.38, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * min_investing_cashflow_guidance_2)`: S=0.52, F=0.38, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * min_investing_cashflow_guidance_2 / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_investing_cashflow_guidance_2, 5))`: S=0.25, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_investing_cashflow_guidance_2)` | TOP500 | 0.36 | 0.24 | 39.4% | 60% | bull-only |
| `rank(ts_delta(min_investing_cashflow_guidance_2, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(min_investing_cashflow_guidance_2)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(min_investing_cashflow_guidance_2 / close)` | TOP3000 | 0.07 | 0.02 | 53.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_investing_cashflow_guidance_2: 1.000 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.863 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.863 (strongly positively correlated)
- min_total_assets_guidance: 0.863 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.863 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
