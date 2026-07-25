---
field: anl4_cff_median
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.12
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 1
max_drawdown: 0.5143
ann_vol: 0.1521
hit_rate: 0.5093
rolling_sharpe_min: -1.769
rolling_sharpe_max: 2.935
negated_best_sharpe: 1.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: 0.72
---
# anl4_cff_median (analyst4)

*Cash Flow From Financing Activities - Median value among forecasts*

## Signal Profile
- `rank(anl4_cff_median)`: S=0.04, F=0.01, T=2.8%, INFERIOR (TOP200)
- `rank(anl4_cff_median / close)`: S=0.06, F=0.02, T=2.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_median, 5))`: S=-0.11, F=-0.02, T=34.3%, INFERIOR (TOP200)
- `-rank(anl4_cff_median)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_median, 5))`: S=1.12, F=0.50, T=37.3%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cff_median, 63)`: S=0.40, F=0.14, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_median, 10)`: S=-0.33, F=-0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_median, 22))`: S=-1.15, F=-0.71, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_median)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_median / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+5.1%
  - 2020: S=2.17 (strong), ret=+25.7%
  - 2021: S=-0.34 (negative), ret=-6.3%
  - 2022: S=-1.26 (negative), ret=-26.4%
  - 2023: S=0.74 (moderate), ret=+7.0%

## Risk & Drawdown
- Max drawdown: 51.43% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +1.0%, volatility 15.2% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.12, excess kurtosis +2.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.94, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.86%; worst month: -12.59%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.63
- Sideways: S=0.36
- Bear: S=2.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cff_median, 5))` S=1.12, F=0.50, INFERIOR
Direction gap: +0.72 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_cff_median)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_median / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_median, 5))`: S=1.12, F=0.50, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cff_median / close)` | TOP200 | 0.07 | 0.02 | 51.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_low: 0.992 (strongly positively correlated)
- est_cashflow_fin: 0.954 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.818 (strongly positively correlated)
- fnd6_newa1v1300_dv: -0.801 (strongly negatively correlated)
- cashflow_dividends: -0.801 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
