---
field: rp_css_labor
dataset: news18
best_template: rank_level
best_sharpe: 0.73
best_fitness: 0.2
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.3085
ann_vol: 0.1409
hit_rate: 0.5134
rolling_sharpe_min: -1.284
rolling_sharpe_max: 2.723
negated_best_sharpe: 0.2
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.53
---
# rp_css_labor (news18)

*Composite sentiment score of labor issues news*

## Signal Profile
- `rank(rp_css_labor)`: S=0.73, F=0.20, T=139.1%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_labor, 5))`: S=0.47, F=0.11, T=157.1%, INFERIOR (TOP3000)
- `-rank(rp_css_labor)`: S=-0.29, F=-0.04, T=154.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_labor, 5))`: S=-0.47, F=-0.11, T=157.1%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_labor, 22)`: S=0.14, F=0.01, T=150.8%, INFERIOR (TOP3000)
- `ts_mean(rp_css_labor, 10)`: S=0.06, F=0.01, T=31.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_labor, 22))`: S=-0.06, F=0.00, T=157.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_labor)`: S=-0.02, F=0.00, T=160.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_labor / close)`: S=0.20, F=0.02, T=160.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+6.1%
  - 2020: S=-0.98 (negative), ret=-13.6%
  - 2021: S=2.17 (strong), ret=+24.6%
  - 2022: S=1.36 (moderate), ret=+20.8%
  - 2023: S=0.91 (moderate), ret=+12.7%

## Risk & Drawdown
- Max drawdown: 30.85% over 891 days (recovered)
- Annualized: return +10.3%, volatility 14.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.43, excess kurtosis +3.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.72, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +12.02%; worst month: -9.23%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.40
- Sideways: S=0.56
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * rp_css_labor / close)` S=0.20, F=0.02, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_css_labor)`: S=-0.02, F=0.00, T=160.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_labor / close)`: S=0.20, F=0.02, T=160.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_labor, 5))`: S=-0.47, F=-0.11, T=157.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_labor)` | TOP200 | 0.73 | 0.20 | 30.9% | 80% | mixed |
| `rank(ts_delta(rp_css_labor, 5))` | TOP3000 | 0.46 | 0.11 | 26.5% | 80% | mixed |
| `rank(rp_css_labor)` | TOP500 | 0.46 | 0.09 | 21.6% | 60% | mixed |
| `rank(ts_delta(rp_css_labor, 5))` | TOP200 | 0.30 | 0.07 | 65.3% | 60% | bull-only |
| `rank(rp_css_labor)` | TOP1000 | 0.29 | 0.04 | 28.2% | 60% | weak |
| `rank(ts_delta(rp_css_labor, 5))` | TOP1000 | 0.21 | 0.04 | 29.0% | 40% | weak |
| `rank(ts_delta(rp_css_labor, 5))` | TOP500 | 0.10 | 0.02 | 46.5% | 60% | weak |

## Correlation Notes
Top correlates:
- rp_ess_price: 0.119 (weakly positively correlated)
- rp_ess_revenue: 0.106 (weakly positively correlated)
- est_cashflow_invst: -0.092 (weakly negatively correlated)
- fn_new_shares_options_a: 0.091 (weakly positively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.091 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
