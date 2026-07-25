---
field: fn_def_tax_liab_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.089
ann_vol: 0.0563
hit_rate: 0.5077
rolling_sharpe_min: -1.2
rolling_sharpe_max: 2.278
redundancy_cluster: 1
negated_best_sharpe: 0.39
negated_best_template: neg_rank_level
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.33
---
# fn_def_tax_liab_q (fundamental2)

*Amount, after deferred tax asset, of deferred tax liability attributable to taxable differences without jurisdictional netting.*

## Signal Profile
- `rank(fn_def_tax_liab_q)`: S=0.34, F=0.15, T=0.6%, INFERIOR (TOP3000)
- `rank(fn_def_tax_liab_q / close)`: S=0.67, F=0.37, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_tax_liab_q, 5))`: S=0.05, F=0.01, T=17.1%, INFERIOR (TOP200)
- `-rank(fn_def_tax_liab_q)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_liab_q, 5))`: S=-0.17, F=-0.07, T=16.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_def_tax_liab_q, 22)`: S=0.72, F=0.63, T=13.7%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_liab_q, 10)`: S=0.07, F=0.02, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_liab_q, 22))`: S=-0.61, F=-0.41, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_q)`: S=0.39, F=0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_q / close)`: S=0.39, F=0.22, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.34 (moderate), ret=+4.5%
  - 2020: S=1.46 (moderate), ret=+9.5%
  - 2021: S=-0.12 (negative), ret=-0.8%
  - 2022: S=1.13 (moderate), ret=+7.1%
  - 2023: S=-0.62 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 8.90% over 258 days (recovered)
- Annualized: return +3.7%, volatility 5.6% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.48, excess kurtosis +3.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.28, latest -0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.68%; worst month: -3.50%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.21
- Sideways: S=1.14
- Bear: S=-1.45

## Negated Direction
Best negated: `rank(-1 * fn_def_tax_liab_q)` S=0.39, F=0.22, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_def_tax_liab_q)`: S=0.39, F=0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_q / close)`: S=0.39, F=0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_liab_q, 5))`: S=-0.17, F=-0.07, T=16.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_liab_q / close)` | TOP3000 | 0.65 | 0.37 | 8.9% | 60% | bull-only |
| `rank(fn_def_tax_liab_q)` | TOP3000 | 0.33 | 0.15 | 17.4% | 40% | bull-only |
| `rank(fn_def_tax_liab_q / close)` | TOP1000 | 0.23 | 0.08 | 11.9% | 80% | bull-only |
| `rank(fn_def_tax_liab_q / close)` | TOP500 | 0.14 | 0.04 | 11.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_def_tax_liab_a: 0.879 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.868 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.861 (strongly positively correlated)
- fn_intangible_assets_accum_amort_q: 0.859 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.857 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
