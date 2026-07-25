---
field: research_development_max_guidance
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.43
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3336
ann_vol: 0.1259
hit_rate: 0.5239
rolling_sharpe_min: -1.634
rolling_sharpe_max: 2.369
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.03
---
# research_development_max_guidance (analyst4)

*The maximum guidance value for Research and Development Expense on an annual basis.*

## Signal Profile
- `rank(research_development_max_guidance)`: S=0.46, F=0.31, T=1.7%, INFERIOR (TOP500)
- `rank(research_development_max_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(research_development_max_guidance, 5))`: S=0.33, F=0.18, T=21.0%, INFERIOR (TOP3000)
- `-rank(research_development_max_guidance)`: S=-0.17, F=-0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_max_guidance, 5))`: S=0.43, F=0.34, T=11.5%, INFERIOR (TOP3000)
- `-ts_zscore(research_development_max_guidance, 63)`: S=0.25, F=0.22, T=7.4%, INFERIOR (TOP3000)
- `ts_mean(research_development_max_guidance, 10)`: S=0.28, F=0.14, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(research_development_max_guidance, 22))`: S=-0.26, F=-0.18, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * research_development_max_guidance)`: S=-0.02, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * research_development_max_guidance / close)`: S=0.28, F=0.14, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.2%
  - 2020: S=-0.57 (negative), ret=-8.1%
  - 2021: S=0.73 (moderate), ret=+11.4%
  - 2022: S=1.13 (moderate), ret=+13.1%
  - 2023: S=1.14 (moderate), ret=+11.0%

## Risk & Drawdown
- Max drawdown: 33.36% over 722 days (recovered)
- Annualized: return +5.6%, volatility 12.6% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew -0.06, excess kurtosis +1.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.63, max 2.37, latest 1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +8.27%; worst month: -11.68%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.01
- Sideways: S=1.51
- Bear: S=-0.87

## Negated Direction
Best negated: `rank(-1 * ts_delta(research_development_max_guidance, 5))` S=0.43, F=0.34, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * research_development_max_guidance)`: S=-0.02, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * research_development_max_guidance / close)`: S=0.28, F=0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_max_guidance, 5))`: S=0.43, F=0.34, T=11.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(research_development_max_guidance)` | TOP500 | 0.45 | 0.31 | 33.4% | 80% | bull-only |
| `rank(ts_delta(research_development_max_guidance, 5))` | TOP3000 | 0.33 | 0.18 | 26.3% | 60% | mixed |
| `rank(research_development_max_guidance)` | TOP1000 | 0.16 | 0.06 | 33.0% | 60% | bull-only |
| `rank(research_development_max_guidance)` | TOP3000 | 0.12 | 0.04 | 30.4% | 60% | bull-only |
| `rank(research_development_max_guidance / close)` | TOP3000 | 0.07 | 0.02 | 50.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_research_development_expense_guidance_2: 1.000 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.385 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.385 (weakly positively correlated)
- min_total_assets_guidance: 0.385 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.385 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
