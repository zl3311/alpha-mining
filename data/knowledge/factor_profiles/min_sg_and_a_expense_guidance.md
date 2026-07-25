---
field: min_sg_and_a_expense_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.61
best_fitness: 0.71
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.5483
ann_vol: 0.2753
hit_rate: 0.5077
rolling_sharpe_min: -1.19
rolling_sharpe_max: 2.773
redundancy_cluster: 87
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: 0.04
---
# min_sg_and_a_expense_guidance (analyst4)

*Selling, General & Administrative Expense - Minimum guidance value*

## Signal Profile
- `rank(min_sg_and_a_expense_guidance)`: S=0.61, F=0.71, T=3.6%, INFERIOR (TOP500)
- `rank(min_sg_and_a_expense_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_sg_and_a_expense_guidance, 5))`: S=0.30, F=0.17, T=5.1%, INFERIOR (TOP200)
- `-rank(min_sg_and_a_expense_guidance)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_sg_and_a_expense_guidance, 5))`: S=0.65, F=0.57, T=10.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_sg_and_a_expense_guidance, 63)`: S=0.23, F=0.08, T=0.7%, INFERIOR (TOP3000)
- `ts_mean(min_sg_and_a_expense_guidance, 10)`: S=0.06, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(min_sg_and_a_expense_guidance, 22))`: S=-0.47, F=-0.41, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * min_sg_and_a_expense_guidance)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * min_sg_and_a_expense_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 31F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/16P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.34 (strong), ret=+59.4%
  - 2020: S=0.26 (weak), ret=+9.8%
  - 2021: S=0.04 (weak), ret=+1.2%
  - 2022: S=0.43 (weak), ret=+9.2%
  - 2023: S=0.26 (weak), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 54.83% over 1185 days (not yet recovered, ongoing at window end)
- Annualized: return +17.0%, volatility 27.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.06, excess kurtosis +7.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.77, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +27.51%; worst month: -20.85%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.56
- Sideways: S=0.99
- Bear: S=0.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_sg_and_a_expense_guidance, 5))` S=0.65, F=0.57, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * min_sg_and_a_expense_guidance)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * min_sg_and_a_expense_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_sg_and_a_expense_guidance, 5))`: S=0.65, F=0.57, T=10.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_sg_and_a_expense_guidance)` | TOP500 | 0.62 | 0.71 | 54.8% | 100% | mixed |
| `rank(ts_delta(min_sg_and_a_expense_guidance, 5))` | TOP200 | 0.30 | 0.17 | 26.1% | 80% | bull-only |
| `rank(min_sg_and_a_expense_guidance)` | TOP200 | 0.13 | 0.07 | 37.6% | 60% | bull-only |
| `rank(min_sg_and_a_expense_guidance / close)` | TOP3000 | 0.06 | 0.02 | 53.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- selling_general_admin_expense_max_guidance_qtr: 1.000 (strongly positively correlated)
- fnd6_dlto: -0.303 (weakly negatively correlated)
- fnd2_a_ltrmdmrepoplinyfour: -0.299 (weakly negatively correlated)
- min_research_development_expense_guidance: 0.297 (weakly positively correlated)
- max_research_development_expense_guidance: 0.297 (weakly positively correlated)

Redundancy cluster #87: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
