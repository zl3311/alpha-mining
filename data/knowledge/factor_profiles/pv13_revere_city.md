---
field: pv13_revere_city
dataset: pv13
best_template: rank_ts_rank
best_sharpe: 0.57
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1785
ann_vol: 0.179
hit_rate: 0.4656
rolling_sharpe_min: -0.557
rolling_sharpe_max: 1.55
negated_best_sharpe: 0.82
negated_best_template: neg_rank_level
negated_best_fitness: 0.39
n_negated_sims: 10
direction_gap: 0.25
---
# pv13_revere_city (pv13)

*City code*

## Signal Profile
- `rank(pv13_revere_city)`: S=-0.14, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(ts_delta(pv13_revere_city, 5))`: S=0.47, F=0.39, T=11.2%, INFERIOR (TOP200)
- `-rank(pv13_revere_city)`: S=0.14, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_city, 5))`: S=-0.07, F=-0.02, T=31.4%, INFERIOR (TOP3000)
- `ts_zscore(pv13_revere_city, 22)`: S=0.05, F=0.02, T=3.7%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_city, 10)`: S=-0.31, F=-0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_city, 22))`: S=0.57, F=0.59, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_city)`: S=0.82, F=0.39, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_city / close)`: S=0.33, F=0.16, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/13P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/10P
- LOW_TURNOVER: 4F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+4.9%
  - 2020: S=0.14 (weak), ret=+2.8%
  - 2021: S=0.78 (moderate), ret=+17.8%
  - 2022: S=0.11 (weak), ret=+2.2%
  - 2023: S=1.15 (moderate), ret=+13.4%

## Risk & Drawdown
- Max drawdown: 17.85% over 98 days (recovered)
- Annualized: return +8.4%, volatility 17.9% (fraction of booksize)
- Hit rate: 46.6% positive days
- Tail shape: skew +0.41, excess kurtosis +18.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.56, max 1.55, latest 1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +17.05%; worst month: -13.12%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.49
- Sideways: S=0.68
- Bear: S=-0.84

## Negated Direction
Best negated: `rank(-1 * pv13_revere_city)` S=0.82, F=0.39, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_city)`: S=0.82, F=0.39, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_city / close)`: S=0.33, F=0.16, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_city, 5))`: S=-0.07, F=-0.02, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_city, 5))` | TOP200 | 0.47 | 0.39 | 17.8% | 100% | bull-only |
| `rank(ts_delta(pv13_revere_city, 5))` | TOP3000 | 0.17 | 0.06 | 44.6% | 60% | mixed |
| `rank(ts_delta(pv13_revere_city, 5))` | TOP500 | 0.12 | 0.04 | 26.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.581 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.551 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.551 (moderately positively correlated)
- pv13_revere_country: 0.522 (moderately positively correlated)
- unsystematic_risk_last_30_days: -0.516 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
