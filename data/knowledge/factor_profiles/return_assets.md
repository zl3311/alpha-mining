---
field: return_assets
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.34
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3329
ann_vol: 0.0972
hit_rate: 0.4972
rolling_sharpe_min: -4.125
rolling_sharpe_max: 2.982
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.08
---
# return_assets (fundamental6)

*Return on Assets*

## Signal Profile
- `rank(return_assets)`: S=0.20, F=0.09, T=2.6%, INFERIOR (TOP3000)
- `rank(return_assets / close)`: S=0.22, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(return_assets, 5))`: S=0.01, F=0.00, T=37.2%, INFERIOR (TOP200)
- `-rank(return_assets)`: S=-0.03, F=0.00, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(return_assets, 5))`: S=0.51, F=0.19, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(return_assets, 22)`: S=0.42, F=0.14, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(return_assets, 10)`: S=-0.15, F=-0.07, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(return_assets, 22))`: S=0.14, F=0.03, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * return_assets)`: S=0.34, F=0.19, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * return_assets / close)`: S=0.34, F=0.18, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.80 (negative), ret=-3.1%
  - 2020: S=-3.39 (negative), ret=-21.9%
  - 2021: S=1.71 (strong), ret=+17.3%
  - 2022: S=1.53 (strong), ret=+21.5%
  - 2023: S=-0.38 (negative), ret=-3.7%

## Risk & Drawdown
- Max drawdown: 33.29% over 819 days (recovered)
- Annualized: return +2.1%, volatility 9.7% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew -0.22, excess kurtosis +1.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.12, max 2.98, latest -0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.20%; worst month: -8.42%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.78
- Sideways: S=0.27
- Bear: S=-3.19

## Negated Direction
Best negated: `rank(-1 * return_assets)` S=0.34, F=0.19, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * return_assets)`: S=0.34, F=0.19, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * return_assets / close)`: S=0.34, F=0.18, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(return_assets, 5))`: S=0.51, F=0.19, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(return_assets / close)` | TOP3000 | 0.21 | 0.09 | 33.3% | 40% | bull-only |
| `rank(return_assets)` | TOP3000 | 0.19 | 0.09 | 43.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- eps: 0.987 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.987 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.986 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.986 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.985 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
