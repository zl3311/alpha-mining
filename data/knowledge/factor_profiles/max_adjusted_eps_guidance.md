---
field: max_adjusted_eps_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.32
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2803
ann_vol: 0.0936
hit_rate: 0.4923
rolling_sharpe_min: -3.961
rolling_sharpe_max: 2.554
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: 0.04
---
# max_adjusted_eps_guidance (analyst4)

*The maximum guidance value for adjusted earnings per share.*

## Signal Profile
- `rank(max_adjusted_eps_guidance)`: S=0.28, F=0.13, T=0.7%, INFERIOR (TOP3000)
- `rank(max_adjusted_eps_guidance / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_adjusted_eps_guidance, 5))`: S=0.31, F=0.09, T=33.3%, INFERIOR (TOP200)
- `-rank(max_adjusted_eps_guidance)`: S=0.09, F=0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_eps_guidance, 5))`: S=-0.31, F=-0.09, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(max_adjusted_eps_guidance, 63)`: S=0.18, F=0.04, T=22.2%, INFERIOR (TOP3000)
- `ts_mean(max_adjusted_eps_guidance, 10)`: S=-0.08, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_adjusted_eps_guidance, 22))`: S=-0.12, F=-0.03, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance)`: S=0.32, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance / close)`: S=0.23, F=0.11, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.27, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.43 (negative), ret=-1.7%
  - 2020: S=-3.22 (negative), ret=-16.1%
  - 2021: S=1.42 (moderate), ret=+16.4%
  - 2022: S=1.15 (moderate), ret=+15.8%
  - 2023: S=-0.26 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 28.03% over 814 days (recovered)
- Annualized: return +2.5%, volatility 9.4% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew -0.04, excess kurtosis +2.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.96, max 2.55, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.82%; worst month: -3.94%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.39
- Sideways: S=0.43
- Bear: S=-2.95

## Negated Direction
Best negated: `rank(-1 * max_adjusted_eps_guidance)` S=0.32, F=0.19, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * max_adjusted_eps_guidance)`: S=0.32, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance / close)`: S=0.23, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_eps_guidance, 5))`: S=-0.31, F=-0.09, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_adjusted_eps_guidance)` | TOP3000 | 0.27 | 0.13 | 28.0% | 40% | bull-only |
| `rank(ts_delta(max_adjusted_eps_guidance, 5))` | TOP200 | 0.33 | 0.09 | 13.2% | 60% | bear-only |
| `rank(max_adjusted_eps_guidance / close)` | TOP3000 | 0.11 | 0.04 | 51.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- eps_adjusted_min_guidance_qtr: 1.000 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.880 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.879 (strongly positively correlated)
- fnd6_cptnewqv1300_oiadpq: 0.878 (strongly positively correlated)
- operating_income: 0.878 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
