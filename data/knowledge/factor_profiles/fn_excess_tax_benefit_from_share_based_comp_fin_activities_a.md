---
field: fn_excess_tax_benefit_from_share_based_comp_fin_activities_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 4.1
best_fitness: 10.75
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1521
ann_vol: 0.0903
hit_rate: 0.4802
rolling_sharpe_min: -1.266
rolling_sharpe_max: 2.297
negated_best_sharpe: 0.81
negated_best_template: neg_rank_level
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -3.29
---
# fn_excess_tax_benefit_from_share_based_comp_fin_activities_a (fundamental2)

*Amount of cash inflow from realized tax benefit related to deductible compensation cost reported on the entity's tax return for equity instruments in excess of the compensation cost for those instruments recognized for financial reporting purposes.*

## Signal Profile
- `rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a)`: S=-0.34, F=-0.10, T=0.4%, INFERIOR (TOP3000)
- `rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a / close)`: S=-0.20, F=-0.04, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 5))`: S=0.50, F=0.30, T=7.1%, INFERIOR (TOP500)
- `-rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a)`: S=0.72, F=0.33, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 5))`: S=-0.18, F=-0.07, T=7.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)`: S=4.10, F=10.75, T=10.0%, SPECTACULAR (TOP3000)
- `ts_mean(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 10)`: S=-0.13, F=-0.04, T=0.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22))`: S=-0.53, F=-0.40, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_a)`: S=0.81, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_a / close)`: S=0.72, F=0.40, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 10F/22P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+9.2%
  - 2020: S=-0.16 (negative), ret=-1.2%
  - 2021: S=-0.20 (negative), ret=-2.2%
  - 2022: S=1.33 (moderate), ret=+13.6%
  - 2023: S=0.49 (weak), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 15.21% over 663 days (recovered)
- Annualized: return +4.5%, volatility 9.0% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.80, excess kurtosis +15.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.30, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +6.29%; worst month: -6.53%
Positive months: 55%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.29
- Sideways: S=1.30
- Bear: S=-0.85

## Negated Direction
Best negated: `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_a)` S=0.81, F=0.47, INFERIOR
Direction gap: -3.29 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_a)`: S=0.81, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_a / close)`: S=0.72, F=0.40, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 5))`: S=-0.18, F=-0.07, T=7.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 5))` | TOP500 | 0.50 | 0.30 | 15.2% | 60% | bull-only |
| `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 5))` | TOP200 | 0.13 | 0.03 | 19.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_esopnr: 0.463 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.461 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.461 (moderately positively correlated)
- min_total_assets_guidance: 0.461 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.461 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
