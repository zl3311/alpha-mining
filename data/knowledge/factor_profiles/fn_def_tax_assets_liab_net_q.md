---
field: fn_def_tax_assets_liab_net_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.42
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.0608
ann_vol: 0.025
hit_rate: 0.4907
rolling_sharpe_min: -2.553
rolling_sharpe_max: 2.206
negated_best_sharpe: 0.03
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.39
---
# fn_def_tax_assets_liab_net_q (fundamental2)

*Amount, after allocation of valuation allowances and deferred tax liability, of deferred tax asset attributable to deductible differences and carryforwards, without jurisdictional netting.*

## Signal Profile
- `rank(fn_def_tax_assets_liab_net_q)`: S=0.53, F=0.18, T=0.9%, INFERIOR (TOP1000)
- `rank(fn_def_tax_assets_liab_net_q / close)`: S=0.58, F=0.20, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_tax_assets_liab_net_q, 5))`: S=0.19, F=0.07, T=23.5%, INFERIOR (TOP200)
- `-rank(fn_def_tax_assets_liab_net_q)`: S=-0.53, F=-0.18, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_q, 5))`: S=0.03, F=0.00, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_tax_assets_liab_net_q, 63)`: S=0.42, F=0.30, T=13.6%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_assets_liab_net_q, 10)`: S=0.09, F=0.02, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_assets_liab_net_q, 22))`: S=0.16, F=0.06, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_q)`: S=-0.53, F=-0.18, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_q / close)`: S=-0.53, F=-0.19, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 10F/22P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.44 (negative), ret=-1.0%
  - 2020: S=-0.11 (negative), ret=-0.3%
  - 2021: S=1.25 (moderate), ret=+2.7%
  - 2022: S=1.38 (moderate), ret=+3.5%
  - 2023: S=1.07 (moderate), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 6.08% over 1070 days (recovered)
- Annualized: return +1.5%, volatility 2.5% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.30, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.55, max 2.21, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +1.55%; worst month: -1.37%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.95
- Sideways: S=0.25
- Bear: S=0.61

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_q, 5))` S=0.03, F=0.00, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_def_tax_assets_liab_net_q)`: S=-0.53, F=-0.18, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_q / close)`: S=-0.53, F=-0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_q, 5))`: S=0.03, F=0.00, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_assets_liab_net_q / close)` | TOP3000 | 0.60 | 0.20 | 6.1% | 60% | all-weather |
| `rank(fn_def_tax_assets_liab_net_q / close)` | TOP1000 | 0.53 | 0.19 | 8.8% | 60% | mixed |
| `rank(fn_def_tax_assets_liab_net_q)` | TOP1000 | 0.53 | 0.18 | 8.6% | 60% | all-weather |
| `rank(fn_def_tax_assets_liab_net_q)` | TOP3000 | 0.47 | 0.12 | 5.9% | 60% | mixed |
| `rank(ts_delta(fn_def_tax_assets_liab_net_q, 5))` | TOP200 | 0.19 | 0.07 | 38.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_def_tax_assets_net_q: 0.515 (moderately positively correlated)
- anl4_qf_az_div_number: 0.481 (moderately positively correlated)
- anl4_qfd1_az_div_number: 0.481 (moderately positively correlated)
- fnd6_beta: 0.471 (moderately positively correlated)
- est_bookvalue_ps: 0.468 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
