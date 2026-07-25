---
field: anl4_capex_low
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.38
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.0942
ann_vol: 0.0698
hit_rate: 0.4656
rolling_sharpe_min: -1.715
rolling_sharpe_max: 2.187
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.02
---
# anl4_capex_low (analyst4)

*Capital Expenditures - The lowest estimation*

## Signal Profile
- `rank(anl4_capex_low)`: S=0.28, F=0.13, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_capex_low / close)`: S=0.36, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_capex_low, 5))`: S=-0.08, F=-0.01, T=34.0%, INFERIOR (TOP200)
- `-rank(anl4_capex_low)`: S=-0.07, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_low, 5))`: S=0.08, F=0.01, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_capex_low, 63)`: S=0.27, F=0.07, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_low, 10)`: S=-0.10, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_low, 22))`: S=-0.19, F=-0.05, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_low)`: S=0.38, F=0.25, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_low / close)`: S=0.30, F=0.16, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.34, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.27 (negative), ret=-1.4%
  - 2020: S=-0.04 (negative), ret=-0.3%
  - 2021: S=0.98 (moderate), ret=+8.5%
  - 2022: S=0.54 (moderate), ret=+3.3%
  - 2023: S=0.34 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 9.42% over 591 days (not yet recovered, ongoing at window end)
- Annualized: return +2.4%, volatility 7.0% (fraction of booksize)
- Hit rate: 46.6% positive days
- Tail shape: skew +0.66, excess kurtosis +2.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.72, max 2.19, latest 0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.67%; worst month: -3.79%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.07
- Sideways: S=-0.06
- Bear: S=-1.28

## Negated Direction
Best negated: `rank(-1 * anl4_capex_low)` S=0.38, F=0.25, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_capex_low)`: S=0.38, F=0.25, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_low / close)`: S=0.30, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_low, 5))`: S=0.08, F=0.01, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_capex_low / close)` | TOP3000 | 0.34 | 0.16 | 9.4% | 60% | bull-only |
| `rank(anl4_capex_low)` | TOP3000 | 0.27 | 0.13 | 31.8% | 80% | bull-only |
| `rank(anl4_capex_low / close)` | TOP1000 | 0.10 | 0.03 | 13.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_capex_mean: 0.994 (strongly positively correlated)
- est_capex: 0.968 (strongly positively correlated)
- capital_expenditure_reported_value: 0.948 (strongly positively correlated)
- anl4_capex_value: 0.948 (strongly positively correlated)
- anl4_totassets_low: 0.943 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
