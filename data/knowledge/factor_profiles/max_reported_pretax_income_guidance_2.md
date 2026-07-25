---
field: max_reported_pretax_income_guidance_2
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.71
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1452
ann_vol: 0.0906
hit_rate: 0.5126
rolling_sharpe_min: -1.054
rolling_sharpe_max: 3.197
redundancy_cluster: 40
negated_best_sharpe: 0.71
negated_best_template: neg_rank_level
negated_best_fitness: 0.82
n_negated_sims: 10
direction_gap: 0.15
---
# max_reported_pretax_income_guidance_2 (analyst4)

*Reported Pretax income- maximum guidance value*

## Signal Profile
- `rank(max_reported_pretax_income_guidance_2)`: S=-0.13, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(max_reported_pretax_income_guidance_2 / close)`: S=0.06, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_reported_pretax_income_guidance_2, 5))`: S=0.56, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(max_reported_pretax_income_guidance_2)`: S=0.24, F=0.15, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_pretax_income_guidance_2, 5))`: S=-0.56, F=-0.22, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(max_reported_pretax_income_guidance_2, 63)`: S=0.17, F=0.03, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(max_reported_pretax_income_guidance_2, 10)`: S=-0.20, F=-0.11, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_rank(max_reported_pretax_income_guidance_2, 22))`: S=-0.11, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance_2)`: S=0.71, F=0.82, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance_2 / close)`: S=0.24, F=0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+3.9%
  - 2020: S=2.94 (strong), ret=+23.2%
  - 2021: S=-0.13 (negative), ret=-1.3%
  - 2022: S=0.01 (weak), ret=+0.1%
  - 2023: S=-0.03 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 14.52% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 9.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.58, excess kurtosis +5.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 3.20, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.05%; worst month: -4.29%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.89
- Sideways: S=0.58
- Bear: S=2.43

## Negated Direction
Best negated: `rank(-1 * max_reported_pretax_income_guidance_2)` S=0.71, F=0.82, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * max_reported_pretax_income_guidance_2)`: S=0.71, F=0.82, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance_2 / close)`: S=0.24, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_pretax_income_guidance_2, 5))`: S=-0.56, F=-0.22, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_reported_pretax_income_guidance_2, 5))` | TOP200 | 0.58 | 0.22 | 14.5% | 60% | bear-only |
| `rank(max_reported_pretax_income_guidance_2 / close)` | TOP3000 | 0.06 | 0.02 | 53.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_reported_min_guidance: 0.996 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.995 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.995 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.995 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.993 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
