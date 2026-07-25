---
field: rp_css_inverstor
dataset: news18
best_template: rank_neg_delta
best_sharpe: 0.82
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.4602
ann_vol: 0.2036
hit_rate: 0.5385
rolling_sharpe_min: -1.78
rolling_sharpe_max: 2.677
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 4
direction_gap: 0.13
---
# rp_css_inverstor (news18)

*Composite sentiment score of investor relations news*

## Signal Profile
- `rank(rp_css_inverstor)`: S=0.69, F=0.20, T=163.9%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_css_inverstor, 5))`: S=-0.24, F=-0.06, T=123.0%, INFERIOR (TOP1000)
- `-rank(rp_css_inverstor)`: S=-0.69, F=-0.20, T=163.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_inverstor, 5))`: S=0.82, F=0.41, T=141.7%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_inverstor, 22)`: S=0.31, F=0.07, T=161.5%, INFERIOR (TOP3000)
- `ts_mean(rp_css_inverstor, 10)`: S=0.21, F=0.04, T=34.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_inverstor, 22))`: S=-0.24, F=-0.04, T=165.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_inverstor)`: S=0.32, F=0.06, T=164.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_inverstor / close)`: S=0.23, F=0.04, T=159.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.68, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.45 (negative), ret=-9.1%
  - 2020: S=-0.75 (negative), ret=-12.8%
  - 2021: S=0.51 (moderate), ret=+10.5%
  - 2022: S=1.91 (strong), ret=+41.1%
  - 2023: S=1.86 (strong), ret=+38.0%

## Risk & Drawdown
- Max drawdown: 46.02% over 1051 days (recovered)
- Annualized: return +13.8%, volatility 20.4% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew +0.34, excess kurtosis +16.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.78, max 2.68, latest 1.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +18.79%; worst month: -12.03%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.61
- Sideways: S=0.14
- Bear: S=1.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_inverstor, 5))` S=0.82, F=0.41, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_css_inverstor)`: S=0.32, F=0.06, T=164.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_inverstor / close)`: S=0.23, F=0.04, T=159.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_inverstor, 5))`: S=0.82, F=0.41, T=141.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_inverstor)` | TOP1000 | 0.68 | 0.20 | 46.0% | 60% | all-weather |
| `rank(rp_css_inverstor)` | TOP200 | 0.51 | 0.15 | 32.9% | 100% | all-weather |
| `rank(rp_css_inverstor)` | TOP500 | 0.50 | 0.13 | 42.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_incorp: -0.140 (weakly negatively correlated)
- reporting_currency_code_9: -0.118 (weakly negatively correlated)
- fn_derivative_fair_value_of_derivative_liability_a: -0.110 (weakly negatively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: -0.101 (weakly negatively correlated)
- fnd6_optvolq: -0.101 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
