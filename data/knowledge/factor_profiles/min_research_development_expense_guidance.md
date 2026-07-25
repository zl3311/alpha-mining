---
field: min_research_development_expense_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.69
best_fitness: 0.87
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 7
max_drawdown: 0.4106
ann_vol: 0.2876
hit_rate: 0.5126
rolling_sharpe_min: -0.754
rolling_sharpe_max: 2.822
redundancy_cluster: 74
negated_best_sharpe: 0.17
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.52
---
# min_research_development_expense_guidance (analyst4)

*Minimum guidance value for Research & Development Expense*

## Signal Profile
- `rank(min_research_development_expense_guidance)`: S=0.69, F=0.87, T=2.4%, INFERIOR (TOP500)
- `rank(min_research_development_expense_guidance / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_research_development_expense_guidance, 5))`: S=0.59, F=0.50, T=12.3%, INFERIOR (TOP3000)
- `-rank(min_research_development_expense_guidance)`: S=-0.28, F=-0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_research_development_expense_guidance, 5))`: S=-0.07, F=-0.02, T=3.9%, INFERIOR (TOP3000)
- `ts_zscore(min_research_development_expense_guidance, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(min_research_development_expense_guidance, 10)`: S=0.23, F=0.15, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(min_research_development_expense_guidance, 22))`: S=0.37, F=0.26, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance)`: S=-0.60, F=-0.73, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 31F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.72, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+13.3%
  - 2020: S=1.43 (moderate), ret=+39.7%
  - 2021: S=-0.53 (negative), ret=-14.6%
  - 2022: S=0.41 (weak), ret=+12.5%
  - 2023: S=1.70 (strong), ret=+50.6%

## Risk & Drawdown
- Max drawdown: 41.06% over 968 days (recovered)
- Annualized: return +20.7%, volatility 28.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.80, excess kurtosis +5.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 2.82, latest 1.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +20.90%; worst month: -19.09%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.52
- Sideways: S=1.26
- Bear: S=1.53

## Negated Direction
Best negated: `rank(-1 * min_research_development_expense_guidance / close)` S=0.17, F=0.07, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_research_development_expense_guidance)`: S=-0.60, F=-0.73, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_research_development_expense_guidance, 5))`: S=-0.07, F=-0.02, T=3.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_research_development_expense_guidance)` | TOP500 | 0.72 | 0.87 | 41.1% | 80% | bear-only |
| `rank(min_research_development_expense_guidance)` | TOP200 | 0.64 | 0.74 | 56.8% | 60% | mixed |
| `rank(ts_delta(min_research_development_expense_guidance, 5))` | TOP3000 | 0.58 | 0.50 | 32.4% | 100% | mixed |
| `rank(min_research_development_expense_guidance)` | TOP1000 | 0.30 | 0.21 | 52.1% | 60% | mixed |
| `rank(ts_delta(min_research_development_expense_guidance, 5))` | TOP200 | 0.18 | 0.09 | 30.7% | 60% | bull-only |
| `rank(ts_delta(min_research_development_expense_guidance, 5))` | TOP500 | 0.07 | 0.02 | 34.5% | 80% | bull-only |
| `rank(min_research_development_expense_guidance / close)` | TOP3000 | 0.07 | 0.02 | 52.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_research_development_expense_guidance: 1.000 (strongly positively correlated)
- min_sg_and_a_expense_guidance: 0.297 (weakly positively correlated)
- selling_general_admin_expense_max_guidance_qtr: 0.297 (weakly positively correlated)
- min_research_development_expense_guidance_2: 0.283 (weakly positively correlated)
- research_development_max_guidance: 0.283 (weakly positively correlated)

Redundancy cluster #74: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
