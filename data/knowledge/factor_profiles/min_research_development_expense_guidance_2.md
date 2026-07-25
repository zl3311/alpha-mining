---
field: min_research_development_expense_guidance_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.46
best_fitness: 0.31
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3311
ann_vol: 0.1259
hit_rate: 0.5263
rolling_sharpe_min: -1.609
rolling_sharpe_max: 2.378
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.16
---
# min_research_development_expense_guidance_2 (analyst4)

*Minimum guidance value for Research & Development Expense on an annual basis*

## Signal Profile
- `rank(min_research_development_expense_guidance_2)`: S=0.46, F=0.31, T=1.7%, INFERIOR (TOP500)
- `rank(min_research_development_expense_guidance_2 / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_research_development_expense_guidance_2, 5))`: S=0.53, F=0.20, T=33.8%, INFERIOR (TOP200)
- `-rank(min_research_development_expense_guidance_2)`: S=-0.16, F=-0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_research_development_expense_guidance_2, 5))`: S=0.30, F=0.07, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_research_development_expense_guidance_2, 63)`: S=0.36, F=0.12, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(min_research_development_expense_guidance_2, 10)`: S=0.13, F=0.04, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(min_research_development_expense_guidance_2, 22))`: S=-0.18, F=-0.05, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance_2)`: S=-0.46, F=-0.31, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance_2 / close)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.2%
  - 2020: S=-0.55 (negative), ret=-7.9%
  - 2021: S=0.75 (moderate), ret=+11.7%
  - 2022: S=1.11 (moderate), ret=+12.8%
  - 2023: S=1.09 (moderate), ret=+10.6%

## Risk & Drawdown
- Max drawdown: 33.11% over 721 days (recovered)
- Annualized: return +5.6%, volatility 12.6% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.07, excess kurtosis +1.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.38, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.27%; worst month: -11.68%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.01
- Sideways: S=1.48
- Bear: S=-0.85

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_research_development_expense_guidance_2, 5))` S=0.30, F=0.07, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_research_development_expense_guidance_2)`: S=-0.46, F=-0.31, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * min_research_development_expense_guidance_2 / close)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_research_development_expense_guidance_2, 5))`: S=0.30, F=0.07, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_research_development_expense_guidance_2)` | TOP500 | 0.44 | 0.31 | 33.1% | 80% | bull-only |
| `rank(ts_delta(min_research_development_expense_guidance_2, 5))` | TOP200 | 0.54 | 0.20 | 18.5% | 60% | bear-only |
| `rank(min_research_development_expense_guidance_2)` | TOP1000 | 0.15 | 0.06 | 32.9% | 60% | bull-only |
| `rank(min_research_development_expense_guidance_2)` | TOP3000 | 0.12 | 0.04 | 30.3% | 60% | bull-only |
| `rank(min_research_development_expense_guidance_2 / close)` | TOP3000 | 0.07 | 0.02 | 50.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- research_development_max_guidance: 1.000 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.384 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.384 (weakly positively correlated)
- min_total_assets_guidance: 0.384 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.384 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
