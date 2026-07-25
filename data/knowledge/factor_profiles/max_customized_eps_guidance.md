---
field: max_customized_eps_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.51
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3762
ann_vol: 0.1082
hit_rate: 0.4591
rolling_sharpe_min: -3.179
rolling_sharpe_max: 3.039
negated_best_sharpe: 0.5
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.01
---
# max_customized_eps_guidance (analyst4)

*The maximum guidance value for custom earnings per share on an annual basis.*

## Signal Profile
- `rank(max_customized_eps_guidance)`: S=0.51, F=0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(max_customized_eps_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_customized_eps_guidance, 5))`: S=0.56, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(max_customized_eps_guidance)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_customized_eps_guidance, 5))`: S=0.22, F=0.04, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_customized_eps_guidance, 63)`: S=0.62, F=0.24, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(max_customized_eps_guidance, 10)`: S=0.47, F=0.22, T=26.1%, INFERIOR (TOP3000)
- `rank(ts_rank(max_customized_eps_guidance, 22))`: S=-0.21, F=-0.06, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_customized_eps_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * max_customized_eps_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.48, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-4.1%
  - 2020: S=-1.78 (negative), ret=-14.4%
  - 2021: S=1.05 (moderate), ret=+16.8%
  - 2022: S=2.40 (strong), ret=+27.9%
  - 2023: S=-0.15 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 37.62% over 930 days (recovered)
- Annualized: return +5.2%, volatility 10.8% (fraction of booksize)
- Hit rate: 45.9% positive days
- Tail shape: skew +0.01, excess kurtosis +6.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.18, max 3.04, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.56%; worst month: -9.47%
Positive months: 50%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=-0.46
- Bear: S=-1.97

## Negated Direction
Best negated: `rank(-1 * max_customized_eps_guidance)` S=0.50, F=0.33, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_customized_eps_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * max_customized_eps_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_customized_eps_guidance, 5))`: S=0.22, F=0.04, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_customized_eps_guidance)` | TOP3000 | 0.48 | 0.35 | 37.6% | 40% | bull-only |
| `rank(max_customized_eps_guidance)` | TOP500 | 0.47 | 0.33 | 32.4% | 60% | bull-only |
| `rank(ts_delta(max_customized_eps_guidance, 5))` | TOP200 | 0.57 | 0.22 | 15.4% | 40% | bear-only |
| `rank(max_customized_eps_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(max_customized_eps_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_share_buyback_guidance: 1.000 (strongly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 1.000 (strongly positively correlated)
- max_total_goodwill_guidance_2: 1.000 (strongly positively correlated)
- min_custom_eps_guidance: 1.000 (strongly positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
