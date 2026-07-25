---
field: pv13_revere_index_cap
dataset: pv13
cluster: pv13_valuation
coverage: 0.8495
community_alphas: 1783
best_template: rank_delta
best_sharpe: 0.36
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.4044
ann_vol: 0.11
hit_rate: 0.4502
rolling_sharpe_min: -3.214
rolling_sharpe_max: 2.951
negated_best_sharpe: 0.01
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.35
---
# pv13_revere_index_cap (pv13)

*Company market capitalization*

## Signal Profile
- `rank(pv13_revere_index_cap)`: S=0.11, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_index_cap, 5))`: S=0.36, F=0.20, T=6.1%, INFERIOR (TOP3000)
- `-rank(pv13_revere_index_cap)`: S=0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_index_cap, 5))`: S=-0.16, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `ts_zscore(pv13_revere_index_cap, 22)`: S=0.19, F=0.03, T=32.9%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_index_cap, 10)`: S=-0.08, F=-0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_index_cap, 22))`: S=-0.27, F=-0.12, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_cap)`: S=0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_cap / close)`: S=-0.44, F=-0.25, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/11P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/10P
- LOW_TURNOVER: 1F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.35, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.77 (strong), ret=+30.0%
  - 2020: S=-1.24 (negative), ret=-12.1%
  - 2021: S=-0.15 (negative), ret=-2.6%
  - 2022: S=0.98 (moderate), ret=+6.4%
  - 2023: S=-0.55 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 40.44% over 1498 days (not yet recovered, ongoing at window end)
- Annualized: return +3.9%, volatility 11.0% (fraction of booksize)
- Hit rate: 45.0% positive days
- Tail shape: skew +0.77, excess kurtosis +8.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.21, max 2.95, latest -0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +31.07%; worst month: -11.31%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.43
- Sideways: S=0.12
- Bear: S=-2.27

## Negated Direction
Best negated: `-rank(pv13_revere_index_cap)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_index_cap)`: S=0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_index_cap / close)`: S=-0.44, F=-0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_index_cap, 5))`: S=-0.16, F=-0.06, T=6.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_index_cap, 5))` | TOP3000 | 0.35 | 0.20 | 40.4% | 40% | bull-only |
| `rank(pv13_revere_index_cap)` | TOP3000 | 0.11 | 0.03 | 34.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pv13_revere_index_value: 0.993 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.756 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.740 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.736 (strongly positively correlated)
- working_capital: 0.736 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
