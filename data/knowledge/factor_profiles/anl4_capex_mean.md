---
field: anl4_capex_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.37
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.098
ann_vol: 0.0703
hit_rate: 0.4704
rolling_sharpe_min: -1.588
rolling_sharpe_max: 2.227
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: 0.0
---
# anl4_capex_mean (analyst4)

*Capital Expenditures - mean of estimations*

## Signal Profile
- `rank(anl4_capex_mean)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_capex_mean / close)`: S=0.37, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_capex_mean, 5))`: S=0.46, F=0.11, T=36.6%, INFERIOR (TOP3000)
- `-rank(anl4_capex_mean)`: S=-0.11, F=-0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_mean, 5))`: S=0.37, F=0.10, T=36.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_capex_mean, 63)`: S=-0.28, F=-0.08, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_mean, 10)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_mean, 22))`: S=0.02, F=0.00, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_mean)`: S=0.00, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_mean / close)`: S=-0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.25 (negative), ret=-1.3%
  - 2020: S=0.01 (weak), ret=+0.1%
  - 2021: S=1.03 (moderate), ret=+8.7%
  - 2022: S=0.27 (weak), ret=+1.7%
  - 2023: S=0.58 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 9.80% over 591 days (not yet recovered, ongoing at window end)
- Annualized: return +2.5%, volatility 7.0% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +0.66, excess kurtosis +2.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.23, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.46%; worst month: -4.46%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.03
- Sideways: S=-0.09
- Bear: S=-1.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_capex_mean, 5))` S=0.37, F=0.10, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_capex_mean)`: S=0.00, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_mean / close)`: S=-0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_mean, 5))`: S=0.37, F=0.10, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_capex_mean / close)` | TOP3000 | 0.36 | 0.17 | 9.8% | 80% | bull-only |
| `rank(anl4_capex_mean)` | TOP3000 | 0.28 | 0.14 | 32.1% | 80% | bull-only |
| `rank(ts_delta(anl4_capex_mean, 5))` | TOP3000 | 0.48 | 0.11 | 7.7% | 80% | weak |
| `rank(anl4_capex_mean / close)` | TOP1000 | 0.10 | 0.03 | 12.9% | 40% | bull-only |
| `rank(anl4_capex_mean)` | TOP1000 | 0.10 | 0.03 | 33.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_capex_low: 0.994 (strongly positively correlated)
- est_capex: 0.974 (strongly positively correlated)
- capital_expenditure_reported_value: 0.952 (strongly positively correlated)
- anl4_capex_value: 0.952 (strongly positively correlated)
- anl4_totassets_high: 0.945 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
