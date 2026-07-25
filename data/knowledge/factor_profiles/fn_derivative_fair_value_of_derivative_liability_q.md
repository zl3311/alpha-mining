---
field: fn_derivative_fair_value_of_derivative_liability_q
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.44
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.1887
ann_vol: 0.1077
hit_rate: 0.5109
rolling_sharpe_min: -1.405
rolling_sharpe_max: 1.887
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.0
---
# fn_derivative_fair_value_of_derivative_liability_q (fundamental2)

*Fair value, before effects of master netting arrangements, of a financial liability or contract with one or more underlyings, notional amount or payment provision or both, and the contract can be net settled by means outside the contract or delivery of an asset. Includes liabilities elected not to be offset. Excludes liabilities not subject to a master netting arrangement.*

## Signal Profile
- `rank(fn_derivative_fair_value_of_derivative_liability_q)`: S=0.19, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_derivative_fair_value_of_derivative_liability_q / close)`: S=0.35, F=0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_q, 5))`: S=0.44, F=0.16, T=36.2%, INFERIOR (TOP1000)
- `-rank(fn_derivative_fair_value_of_derivative_liability_q)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_liability_q, 5))`: S=0.27, F=0.10, T=37.5%, INFERIOR (TOP3000)
- `ts_zscore(fn_derivative_fair_value_of_derivative_liability_q, 22)`: S=-0.08, F=-0.02, T=31.8%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_fair_value_of_derivative_liability_q, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_fair_value_of_derivative_liability_q, 22))`: S=-0.15, F=-0.04, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_q)`: S=0.44, F=0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_q / close)`: S=0.33, F=0.17, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-0.8%
  - 2020: S=2.03 (strong), ret=+24.9%
  - 2021: S=-1.28 (negative), ret=-14.1%
  - 2022: S=1.38 (moderate), ret=+15.4%
  - 2023: S=-0.24 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 18.87% over 644 days (recovered)
- Annualized: return +4.8%, volatility 10.8% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.32, excess kurtosis +5.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 1.89, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +10.94%; worst month: -7.26%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.50
- Sideways: S=1.09
- Bear: S=0.66

## Negated Direction
Best negated: `rank(-1 * fn_derivative_fair_value_of_derivative_liability_q)` S=0.44, F=0.25, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_q)`: S=0.44, F=0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_q / close)`: S=0.33, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_liability_q, 5))`: S=0.27, F=0.10, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_q, 5))` | TOP1000 | 0.44 | 0.16 | 18.9% | 40% | bear-only |
| `rank(fn_derivative_fair_value_of_derivative_liability_q / close)` | TOP3000 | 0.35 | 0.12 | 13.0% | 80% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_q, 5))` | TOP500 | 0.20 | 0.05 | 27.6% | 60% | weak |
| `rank(fn_derivative_fair_value_of_derivative_liability_q)` | TOP3000 | 0.18 | 0.05 | 10.9% | 80% | bull-only |
| `rank(fn_derivative_fair_value_of_derivative_liability_q / close)` | TOP1000 | 0.14 | 0.04 | 8.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q: -0.161 (weakly negatively correlated)
- fnd6_newqv1300_spiq: -0.132 (weakly negatively correlated)
- fnd6_prcc: -0.122 (weakly negatively correlated)
- fnd6_prcl: -0.112 (weakly negatively correlated)
- anl4_totassets_std: -0.109 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
