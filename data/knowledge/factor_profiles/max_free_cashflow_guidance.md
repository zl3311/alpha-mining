---
field: max_free_cashflow_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.75
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1895
ann_vol: 0.0921
hit_rate: 0.5223
rolling_sharpe_min: -1.579
rolling_sharpe_max: 3.024
redundancy_cluster: 68
negated_best_sharpe: 0.18
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.57
---
# max_free_cashflow_guidance (analyst4)

*The maximum guidance value for Free Cash Flow.*

## Signal Profile
- `rank(max_free_cashflow_guidance)`: S=0.75, F=0.56, T=1.5%, INFERIOR (TOP3000)
- `rank(max_free_cashflow_guidance / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_free_cashflow_guidance, 5))`: S=0.54, F=0.21, T=33.7%, INFERIOR (TOP200)
- `-rank(max_free_cashflow_guidance)`: S=-0.41, F=-0.25, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_free_cashflow_guidance, 5))`: S=-0.54, F=-0.21, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(max_free_cashflow_guidance, 63)`: S=0.49, F=0.18, T=22.2%, INFERIOR (TOP3000)
- `ts_mean(max_free_cashflow_guidance, 10)`: S=0.52, F=0.36, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(max_free_cashflow_guidance, 22))`: S=-0.22, F=-0.07, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cashflow_guidance)`: S=0.18, F=0.12, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cashflow_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+4.5%
  - 2020: S=-0.92 (negative), ret=-8.8%
  - 2021: S=1.55 (strong), ret=+16.1%
  - 2022: S=1.97 (strong), ret=+18.9%
  - 2023: S=0.45 (weak), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 18.95% over 748 days (recovered)
- Annualized: return +6.9%, volatility 9.2% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.01, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 3.02, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.66%; worst month: -8.40%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.12
- Sideways: S=0.08
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * max_free_cashflow_guidance)` S=0.18, F=0.12, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_free_cashflow_guidance)`: S=0.18, F=0.12, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cashflow_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_free_cashflow_guidance, 5))`: S=-0.54, F=-0.21, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_free_cashflow_guidance)` | TOP3000 | 0.75 | 0.56 | 18.9% | 80% | mixed |
| `rank(max_free_cashflow_guidance)` | TOP1000 | 0.41 | 0.25 | 22.0% | 80% | mixed |
| `rank(ts_delta(max_free_cashflow_guidance, 5))` | TOP200 | 0.56 | 0.21 | 14.9% | 80% | bear-only |
| `rank(max_free_cashflow_guidance / close)` | TOP3000 | 0.11 | 0.04 | 52.3% | 60% | bull-only |
| `rank(max_free_cashflow_guidance)` | TOP200 | 0.04 | 0.04 | 43.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- min_free_cashflow_guidance: 1.000 (strongly positively correlated)
- max_free_cash_flow_guidance: 0.524 (moderately positively correlated)
- min_free_cash_flow_guidance: 0.522 (moderately positively correlated)
- earnings_per_share_min_guidance: 0.478 (moderately positively correlated)
- eps_max_guidance_quarterly: 0.478 (moderately positively correlated)

Redundancy cluster #68: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
