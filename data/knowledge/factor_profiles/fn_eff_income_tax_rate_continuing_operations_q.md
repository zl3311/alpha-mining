---
field: fn_eff_income_tax_rate_continuing_operations_q
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.78
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1006
ann_vol: 0.0726
hit_rate: 0.4923
rolling_sharpe_min: -1.532
rolling_sharpe_max: 2.115
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.25
---
# fn_eff_income_tax_rate_continuing_operations_q (fundamental2)

*Percentage of current income tax expense (benefit) and deferred income tax expense (benefit) pertaining to continuing operations.*

## Signal Profile
- `rank(fn_eff_income_tax_rate_continuing_operations_q)`: S=0.50, F=0.25, T=2.4%, INFERIOR (TOP1000)
- `rank(fn_eff_income_tax_rate_continuing_operations_q / close)`: S=0.55, F=0.31, T=2.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_eff_income_tax_rate_continuing_operations_q, 5))`: S=-0.01, F=0.00, T=37.2%, INFERIOR (TOP1000)
- `-rank(fn_eff_income_tax_rate_continuing_operations_q)`: S=-0.50, F=-0.25, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_q, 5))`: S=0.53, F=0.22, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_eff_income_tax_rate_continuing_operations_q, 22)`: S=0.12, F=0.03, T=30.5%, INFERIOR (TOP3000)
- `ts_mean(fn_eff_income_tax_rate_continuing_operations_q, 10)`: S=0.78, F=0.74, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_eff_income_tax_rate_continuing_operations_q, 22))`: S=0.42, F=0.17, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_q)`: S=-0.37, F=-0.16, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_q / close)`: S=-0.40, F=-0.19, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.43 (negative), ret=-2.3%
  - 2020: S=0.91 (moderate), ret=+8.4%
  - 2021: S=0.99 (moderate), ret=+7.2%
  - 2022: S=1.64 (strong), ret=+12.9%
  - 2023: S=-1.50 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 10.06% over 455 days (recovered)
- Annualized: return +3.9%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.56, excess kurtosis +3.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 2.12, latest -1.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.30%; worst month: -3.28%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.01
- Sideways: S=-0.76
- Bear: S=0.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_q, 5))` S=0.53, F=0.22, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_q)`: S=-0.37, F=-0.16, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_eff_income_tax_rate_continuing_operations_q / close)`: S=-0.40, F=-0.19, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_eff_income_tax_rate_continuing_operations_q, 5))`: S=0.53, F=0.22, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_eff_income_tax_rate_continuing_operations_q / close)` | TOP1000 | 0.54 | 0.31 | 10.1% | 60% | mixed |
| `rank(fn_eff_income_tax_rate_continuing_operations_q)` | TOP1000 | 0.49 | 0.25 | 7.0% | 60% | bull-only |
| `rank(fn_eff_income_tax_rate_continuing_operations_q / close)` | TOP3000 | 0.50 | 0.25 | 10.2% | 60% | mixed |
| `rank(fn_eff_income_tax_rate_continuing_operations_q / close)` | TOP500 | 0.38 | 0.19 | 9.7% | 60% | mixed |
| `rank(fn_eff_income_tax_rate_continuing_operations_q)` | TOP500 | 0.36 | 0.16 | 14.1% | 60% | mixed |
| `rank(fn_eff_income_tax_rate_continuing_operations_q)` | TOP3000 | 0.26 | 0.10 | 13.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fscore_bfl_value: 0.746 (strongly positively correlated)
- sales_ps: 0.728 (strongly positively correlated)
- anl4_afv4_cfps_low: 0.716 (strongly positively correlated)
- est_fcf_ps: 0.715 (strongly positively correlated)
- anl4_fcfps_high: 0.711 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
