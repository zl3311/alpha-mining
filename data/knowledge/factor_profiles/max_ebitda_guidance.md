---
field: max_ebitda_guidance
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.68
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.2634
ann_vol: 0.0998
hit_rate: 0.5061
rolling_sharpe_min: -1.863
rolling_sharpe_max: 3.661
negated_best_sharpe: 0.22
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.46
---
# max_ebitda_guidance (analyst4)

*The maximum guidance value for Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) on an annual basis.*

## Signal Profile
- `rank(max_ebitda_guidance)`: S=0.34, F=0.18, T=2.2%, INFERIOR (TOP500)
- `rank(max_ebitda_guidance / close)`: S=0.10, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_ebitda_guidance, 5))`: S=0.27, F=0.07, T=33.6%, INFERIOR (TOP200)
- `-rank(max_ebitda_guidance)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_ebitda_guidance, 5))`: S=0.22, F=0.04, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(max_ebitda_guidance, 22)`: S=0.68, F=0.27, T=43.1%, INFERIOR (TOP3000)
- `ts_mean(max_ebitda_guidance, 10)`: S=0.02, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_ebitda_guidance, 22))`: S=-0.27, F=-0.09, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * max_ebitda_guidance)`: S=-0.20, F=-0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * max_ebitda_guidance / close)`: S=-0.10, F=-0.03, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.69 (negative), ret=-5.0%
  - 2020: S=3.29 (strong), ret=+28.4%
  - 2021: S=0.33 (weak), ret=+3.4%
  - 2022: S=-1.09 (negative), ret=-12.1%
  - 2023: S=0.26 (weak), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 26.34% over 886 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.50, excess kurtosis +1.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.86, max 3.66, latest 0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.29%; worst month: -6.01%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.20
- Sideways: S=-0.49
- Bear: S=2.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_ebitda_guidance, 5))` S=0.22, F=0.04, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_ebitda_guidance)`: S=-0.20, F=-0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * max_ebitda_guidance / close)`: S=-0.10, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_ebitda_guidance, 5))`: S=0.22, F=0.04, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_ebitda_guidance)` | TOP500 | 0.36 | 0.18 | 26.3% | 60% | bear-only |
| `rank(max_ebitda_guidance)` | TOP200 | 0.21 | 0.10 | 70.6% | 60% | bear-only |
| `rank(ts_delta(max_ebitda_guidance, 5))` | TOP200 | 0.28 | 0.07 | 22.1% | 40% | bear-only |
| `rank(max_ebitda_guidance)` | TOP3000 | 0.19 | 0.05 | 13.9% | 60% | mixed |
| `rank(max_ebitda_guidance / close)` | TOP3000 | 0.10 | 0.03 | 30.5% | 60% | bull-only |
| `rank(max_ebitda_guidance / close)` | TOP500 | 0.09 | 0.02 | 17.0% | 40% | mixed |

## Correlation Notes
Top correlates:
- min_ebitda_guidance: 0.998 (strongly positively correlated)
- operating_profit_before_depr_amort_max_guidance_qtr: 0.533 (moderately positively correlated)
- operating_profit_before_depr_amort_min_guidance_qtr: 0.526 (moderately positively correlated)
- pretax_income_reported: -0.514 (moderately negatively correlated)
- pretax_income_actual_reported_value: -0.514 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
