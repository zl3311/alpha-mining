---
field: fn_excess_tax_benefit_from_share_based_comp_fin_activities_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.39
best_fitness: 3.06
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1668
ann_vol: 0.1211
hit_rate: 0.4753
rolling_sharpe_min: -1.372
rolling_sharpe_max: 2.999
negated_best_sharpe: 0.53
negated_best_template: neg_rank
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.86
---
# fn_excess_tax_benefit_from_share_based_comp_fin_activities_q (fundamental2)

*Amount of cash inflow from realized tax benefit related to deductible compensation cost reported on the entity's tax return for equity instruments in excess of the compensation cost for those instruments recognized for financial reporting purposes.*

## Signal Profile
- `rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q)`: S=-0.22, F=-0.09, T=1.6%, INFERIOR (TOP200)
- `rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q / close)`: S=-0.27, F=-0.07, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 5))`: S=0.78, F=0.68, T=8.3%, INFERIOR (TOP500)
- `-rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q)`: S=0.53, F=0.20, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 5))`: S=-0.84, F=-0.73, T=9.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22)`: S=1.39, F=3.06, T=10.0%, SPECTACULAR (TOP3000)
- `ts_mean(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 10)`: S=-0.36, F=-0.17, T=0.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22))`: S=-0.24, F=-0.12, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_q)`: S=0.53, F=0.20, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_q / close)`: S=0.38, F=0.12, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 9F/18P
- LOW_TURNOVER: 16F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.84 (strong), ret=+26.7%
  - 2020: S=1.01 (moderate), ret=+14.5%
  - 2021: S=-0.92 (negative), ret=-10.5%
  - 2022: S=1.12 (moderate), ret=+11.8%
  - 2023: S=0.52 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 16.68% over 846 days (recovered)
- Annualized: return +9.3%, volatility 12.1% (fraction of booksize)
- Hit rate: 47.5% positive days
- Tail shape: skew +2.88, excess kurtosis +35.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 3.00, latest 0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +24.63%; worst month: -7.10%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.92
- Sideways: S=1.90
- Bear: S=-0.72

## Negated Direction
Best negated: `-rank(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q)` S=0.53, F=0.20, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_q)`: S=0.53, F=0.20, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_excess_tax_benefit_from_share_based_comp_fin_activities_q / close)`: S=0.38, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 5))`: S=-0.84, F=-0.73, T=9.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 5))` | TOP500 | 0.77 | 0.68 | 16.7% | 80% | bull-only |
| `rank(ts_delta(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 5))` | TOP1000 | 0.08 | 0.03 | 29.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txbcof: 0.307 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.303 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.303 (weakly positively correlated)
- min_total_assets_guidance: 0.303 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.303 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
