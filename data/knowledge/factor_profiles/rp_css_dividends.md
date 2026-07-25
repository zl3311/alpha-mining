---
field: rp_css_dividends
dataset: news18
best_template: rank_delta
best_sharpe: 0.42
best_fitness: 0.06
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.068
ann_vol: 0.0648
hit_rate: 0.5134
rolling_sharpe_min: -0.658
rolling_sharpe_max: 1.91
negated_best_sharpe: 0.11
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.31
---
# rp_css_dividends (news18)

*Composite sentiment score of dividends news*

## Signal Profile
- `rank(rp_css_dividends)`: S=0.43, F=0.06, T=140.3%, INFERIOR (TOP500)
- `rank(ts_delta(rp_css_dividends, 5))`: S=0.42, F=0.06, T=173.3%, INFERIOR (TOP3000)
- `-rank(rp_css_dividends)`: S=-0.20, F=-0.02, T=145.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_dividends, 5))`: S=-0.42, F=-0.06, T=173.3%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_dividends, 22)`: S=0.20, F=0.02, T=151.7%, INFERIOR (TOP3000)
- `ts_mean(rp_css_dividends, 10)`: S=0.27, F=0.06, T=23.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_dividends, 22))`: S=0.41, F=0.05, T=153.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_dividends)`: S=0.11, F=0.01, T=155.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_dividends / close)`: S=-0.06, F=0.00, T=155.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/3P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+1.2%
  - 2020: S=0.53 (moderate), ret=+3.6%
  - 2021: S=1.41 (moderate), ret=+9.1%
  - 2022: S=0.02 (weak), ret=+0.1%
  - 2023: S=-0.03 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 6.80% over 319 days (recovered)
- Annualized: return +2.9%, volatility 6.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.07, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 1.91, latest -0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.75%; worst month: -4.85%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.29
- Sideways: S=0.03
- Bear: S=1.60

## Negated Direction
Best negated: `rank(-1 * rp_css_dividends)` S=0.11, F=0.01, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_dividends)`: S=0.11, F=0.01, T=155.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_dividends / close)`: S=-0.06, F=0.00, T=155.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_dividends, 5))`: S=-0.42, F=-0.06, T=173.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_dividends)` | TOP500 | 0.44 | 0.06 | 6.8% | 80% | mixed |
| `rank(ts_delta(rp_css_dividends, 5))` | TOP3000 | 0.43 | 0.06 | 15.8% | 60% | weak |
| `rank(ts_delta(rp_css_dividends, 5))` | TOP1000 | 0.41 | 0.06 | 8.9% | 100% | weak |
| `rank(rp_css_dividends)` | TOP200 | 0.33 | 0.05 | 26.4% | 60% | mixed |
| `rank(ts_delta(rp_css_dividends, 5))` | TOP200 | 0.17 | 0.02 | 22.3% | 60% | weak |

## Correlation Notes
Top correlates:
- capital_expenditure_guidance_value: -0.104 (weakly negatively correlated)
- rp_css_earnings: 0.104 (weakly positively correlated)
- fn_proceeds_from_issuance_of_debt_q: -0.100 (weakly negatively correlated)
- fnd2_q_seniornotes: -0.100 (weakly negatively correlated)
- fn_repayments_of_lt_debt_a: -0.098 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
