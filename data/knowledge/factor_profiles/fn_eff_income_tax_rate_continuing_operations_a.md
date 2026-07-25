---
field: fn_eff_income_tax_rate_continuing_operations_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.88
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1841
ann_vol: 0.1311
hit_rate: 0.5271
rolling_sharpe_min: -1.326
rolling_sharpe_max: 2.353
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.54
n_negated_sims: 10
direction_gap: 0.42
---
# fn_eff_income_tax_rate_continuing_operations_a (fundamental2)

*Percentage of current income tax expense (benefit) and deferred income tax expense (benefit) pertaining to continuing operations.*

## Signal Profile
- `rank(fn_eff_income_tax_rate_continuing_operations_a)`: S=0.04, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(fn_eff_income_tax_rate_continuing_operations_a / close)`: S=0.38, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))`: S=0.40, F=0.16, T=34.5%, INFERIOR (TOP3000)
- `-rank(fn_eff_income_tax_rate_continuing_operations_a)`: S=0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))`: S=0.88, F=0.54, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_eff_income_tax_rate_continuing_operations_a, 22)`: S=0.46, F=0.38, T=21.5%, INFERIOR (TOP3000)
- `ts_mean(fn_eff_income_tax_rate_continuing_operations_a, 10)`: S=0.46, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_eff_income_tax_rate_continuing_operations_a, 22))`: S=-0.39, F=-0.19, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_a)`: S=0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_a / close)`: S=-0.19, F=-0.06, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.38, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.1%
  - 2020: S=1.56 (strong), ret=+23.5%
  - 2021: S=0.69 (moderate), ret=+7.6%
  - 2022: S=-0.44 (negative), ret=-5.5%
  - 2023: S=-0.09 (negative), ret=-1.0%

## Risk & Drawdown
- Max drawdown: 18.41% over 350 days (recovered)
- Annualized: return +5.0%, volatility 13.1% (fraction of booksize)
- Hit rate: 52.7% positive days
- Tail shape: skew +0.39, excess kurtosis +5.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 2.35, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.80%; worst month: -10.37%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.11
- Sideways: S=0.65
- Bear: S=0.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))` S=0.88, F=0.54, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_a)`: S=0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_a / close)`: S=-0.19, F=-0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))`: S=0.88, F=0.54, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))` | TOP3000 | 0.38 | 0.16 | 18.4% | 40% | mixed |
| `rank(fn_eff_income_tax_rate_continuing_operations_a / close)` | TOP3000 | 0.36 | 0.16 | 7.8% | 60% | bull-only |
| `rank(fn_eff_income_tax_rate_continuing_operations_a / close)` | TOP1000 | 0.17 | 0.06 | 10.8% | 60% | bull-only |
| `rank(ts_delta(fn_eff_income_tax_rate_continuing_operations_a, 5))` | TOP200 | 0.09 | 0.02 | 64.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_profit_loss_a: -0.112 (weakly negatively correlated)
- fnd6_newqv1300_rcpq: 0.103 (weakly positively correlated)
- fnd6_mfma2_recch: 0.094 (weakly positively correlated)
- rp_ess_business: -0.091 (weakly negatively correlated)
- fn_comp_non_opt_grants_q: -0.083 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
