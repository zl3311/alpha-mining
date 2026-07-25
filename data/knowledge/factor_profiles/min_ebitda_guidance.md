---
field: min_ebitda_guidance
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.67
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.2917
ann_vol: 0.1005
hit_rate: 0.5061
rolling_sharpe_min: -1.981
rolling_sharpe_max: 3.693
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.34
---
# min_ebitda_guidance (analyst4)

*Minimum guidance value for Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) - Annual*

## Signal Profile
- `rank(min_ebitda_guidance)`: S=0.29, F=0.14, T=2.1%, INFERIOR (TOP500)
- `rank(min_ebitda_guidance / close)`: S=0.10, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_ebitda_guidance, 5))`: S=0.33, F=0.10, T=33.7%, INFERIOR (TOP200)
- `-rank(min_ebitda_guidance)`: S=0.00, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebitda_guidance, 5))`: S=0.33, F=0.06, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(min_ebitda_guidance, 22)`: S=0.67, F=0.28, T=41.9%, INFERIOR (TOP3000)
- `ts_mean(min_ebitda_guidance, 10)`: S=-0.03, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(min_ebitda_guidance, 22))`: S=-0.20, F=-0.06, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * min_ebitda_guidance)`: S=-0.19, F=-0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * min_ebitda_guidance / close)`: S=-0.10, F=-0.03, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.31, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.70 (negative), ret=-5.0%
  - 2020: S=3.32 (strong), ret=+29.1%
  - 2021: S=0.33 (weak), ret=+3.6%
  - 2022: S=-1.23 (negative), ret=-13.9%
  - 2023: S=0.14 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 29.17% over 886 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 10.1% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.49, excess kurtosis +1.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.98, max 3.69, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.24%; worst month: -6.15%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.29
- Sideways: S=-0.53
- Bear: S=2.54

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_ebitda_guidance, 5))` S=0.33, F=0.06, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_ebitda_guidance)`: S=-0.19, F=-0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * min_ebitda_guidance / close)`: S=-0.10, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebitda_guidance, 5))`: S=0.33, F=0.06, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_ebitda_guidance)` | TOP500 | 0.31 | 0.14 | 29.2% | 60% | bear-only |
| `rank(ts_delta(min_ebitda_guidance, 5))` | TOP200 | 0.33 | 0.10 | 15.3% | 40% | bear-only |
| `rank(min_ebitda_guidance)` | TOP200 | 0.19 | 0.09 | 71.7% | 60% | bear-only |
| `rank(min_ebitda_guidance)` | TOP3000 | 0.18 | 0.05 | 14.5% | 60% | mixed |
| `rank(min_ebitda_guidance / close)` | TOP3000 | 0.10 | 0.03 | 28.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_ebitda_guidance: 0.998 (strongly positively correlated)
- operating_profit_before_depr_amort_max_guidance_qtr: 0.536 (moderately positively correlated)
- operating_profit_before_depr_amort_min_guidance_qtr: 0.528 (moderately positively correlated)
- pretax_income_reported: -0.527 (moderately negatively correlated)
- pretax_income_actual_reported_value: -0.526 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
