---
field: anl4_capex_value
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.75
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1077
ann_vol: 0.0686
hit_rate: 0.4842
rolling_sharpe_min: -1.544
rolling_sharpe_max: 2.454
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.32
---
# anl4_capex_value (analyst4)

*Capital Expenditures - announced financial value*

## Signal Profile
- `rank(anl4_capex_value)`: S=0.31, F=0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(anl4_capex_value / close)`: S=0.43, F=0.21, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_capex_value, 5))`: S=-0.58, F=-0.21, T=37.4%, INFERIOR (TOP500)
- `-rank(anl4_capex_value)`: S=-0.16, F=-0.06, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_value, 5))`: S=0.75, F=0.24, T=39.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_capex_value, 22)`: S=0.46, F=0.16, T=38.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_value, 10)`: S=-0.15, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_value, 22))`: S=-0.40, F=-0.13, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_value)`: S=-0.31, F=-0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_value / close)`: S=-0.43, F=-0.21, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.42, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.94 (negative), ret=-4.8%
  - 2020: S=0.07 (weak), ret=+0.6%
  - 2021: S=1.32 (moderate), ret=+10.8%
  - 2022: S=0.45 (weak), ret=+2.8%
  - 2023: S=0.92 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 10.77% over 765 days (recovered)
- Annualized: return +2.9%, volatility 6.9% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.52, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 2.45, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.94%; worst month: -3.81%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.14
- Sideways: S=-0.33
- Bear: S=-0.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_capex_value, 5))` S=0.75, F=0.24, INFERIOR
Direction gap: +0.32 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_capex_value)`: S=-0.31, F=-0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_value / close)`: S=-0.43, F=-0.21, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_value, 5))`: S=0.75, F=0.24, T=39.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_capex_value / close)` | TOP3000 | 0.42 | 0.21 | 10.8% | 80% | bull-only |
| `rank(anl4_capex_value)` | TOP3000 | 0.30 | 0.15 | 28.9% | 60% | bull-only |
| `rank(anl4_capex_value)` | TOP1000 | 0.15 | 0.06 | 27.4% | 60% | bull-only |
| `rank(anl4_capex_value / close)` | TOP500 | 0.14 | 0.05 | 23.6% | 80% | bull-only |
| `rank(anl4_capex_value / close)` | TOP1000 | 0.13 | 0.04 | 14.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- capital_expenditure_reported_value: 1.000 (strongly positively correlated)
- anl4_capex_mean: 0.952 (strongly positively correlated)
- anl4_capex_low: 0.948 (strongly positively correlated)
- est_capex: 0.943 (strongly positively correlated)
- est_tot_assets: 0.929 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
