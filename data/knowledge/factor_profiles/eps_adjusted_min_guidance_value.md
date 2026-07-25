---
field: eps_adjusted_min_guidance_value
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.58
best_fitness: 0.22
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1068
ann_vol: 0.0822
hit_rate: 0.5093
rolling_sharpe_min: -0.771
rolling_sharpe_max: 2.07
negated_best_sharpe: 0.15
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.43
---
# eps_adjusted_min_guidance_value (analyst4)

*The minimum guidance value for adjusted earnings per share excluding extraordinary items and stock option expenses on an annual basis.*

## Signal Profile
- `rank(eps_adjusted_min_guidance_value)`: S=0.30, F=0.15, T=0.7%, INFERIOR (TOP3000)
- `rank(eps_adjusted_min_guidance_value / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_adjusted_min_guidance_value, 5))`: S=0.58, F=0.22, T=33.5%, INFERIOR (TOP200)
- `-rank(eps_adjusted_min_guidance_value)`: S=-0.10, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_adjusted_min_guidance_value, 5))`: S=0.15, F=0.02, T=36.0%, INFERIOR (TOP3000)
- `ts_zscore(eps_adjusted_min_guidance_value, 22)`: S=0.17, F=0.03, T=43.4%, INFERIOR (TOP3000)
- `ts_mean(eps_adjusted_min_guidance_value, 10)`: S=0.12, F=0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_adjusted_min_guidance_value, 22))`: S=-0.04, F=0.00, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_value)`: S=-0.10, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_value / close)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.74 (moderate), ret=+4.6%
  - 2020: S=1.63 (strong), ret=+12.8%
  - 2021: S=-0.10 (negative), ret=-0.9%
  - 2022: S=0.35 (weak), ret=+3.2%
  - 2023: S=0.53 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 10.68% over 503 days (recovered)
- Annualized: return +4.9%, volatility 8.2% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.55, excess kurtosis +4.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.07, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +4.29%; worst month: -4.25%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.50
- Sideways: S=0.27
- Bear: S=2.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(eps_adjusted_min_guidance_value, 5))` S=0.15, F=0.02, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * eps_adjusted_min_guidance_value)`: S=-0.10, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_value / close)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_adjusted_min_guidance_value, 5))`: S=0.15, F=0.02, T=36.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(eps_adjusted_min_guidance_value, 5))` | TOP200 | 0.60 | 0.22 | 10.7% | 80% | bear-only |
| `rank(eps_adjusted_min_guidance_value)` | TOP3000 | 0.29 | 0.15 | 32.1% | 60% | bull-only |
| `rank(eps_adjusted_min_guidance_value / close)` | TOP3000 | 0.09 | 0.03 | 52.7% | 60% | bull-only |
| `rank(eps_adjusted_min_guidance_value)` | TOP1000 | 0.10 | 0.03 | 31.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_adjusted_eps_guidance_2: 0.780 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.644 (moderately positively correlated)
- pretax_income_reported_min_guidance: 0.643 (moderately positively correlated)
- max_operating_cashflow_guidance: 0.639 (moderately positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.638 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
