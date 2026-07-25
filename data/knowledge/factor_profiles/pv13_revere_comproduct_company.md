---
field: pv13_revere_comproduct_company
dataset: pv13
best_template: rank_delta
best_sharpe: 0.82
best_fitness: 1.29
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.4424
ann_vol: 0.3553
hit_rate: 0.4486
rolling_sharpe_min: -2.283
rolling_sharpe_max: 3.259
negated_best_sharpe: 0.76
negated_best_template: neg_rank
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -0.06
---
# pv13_revere_comproduct_company (pv13)

*Company product*

## Signal Profile
- `rank(pv13_revere_comproduct_company)`: S=0.39, F=0.19, T=1.3%, INFERIOR (TOP3000)
- `rank(pv13_revere_comproduct_company / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_comproduct_company, 5))`: S=0.82, F=1.29, T=2.1%, AVERAGE (TOP3000)
- `-rank(pv13_revere_comproduct_company)`: S=0.76, F=0.47, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_comproduct_company, 5))`: S=-0.10, F=-0.03, T=2.3%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_comproduct_company, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(pv13_revere_comproduct_company, 10)`: S=-0.50, F=-0.26, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_comproduct_company, 22))`: S=-0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_comproduct_company)`: S=0.76, F=0.47, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_comproduct_company / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/8P
- LOW_FITNESS: 22F/1P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/16P
- LOW_TURNOVER: 2F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+75.9%
  - 2020: S=0.63 (moderate), ret=+17.1%
  - 2021: S=1.03 (moderate), ret=+14.6%
  - 2022: S=2.29 (strong), ret=+23.6%
  - 2023: S=0.61 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 44.24% over 783 days (recovered)
- Annualized: return +27.4%, volatility 35.5% (fraction of booksize)
- Hit rate: 44.9% positive days
- Tail shape: skew -1.34, excess kurtosis +35.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.28, max 3.26, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +41.10%; worst month: -12.32%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.15
- Sideways: S=0.78
- Bear: S=0.34

## Negated Direction
Best negated: `-rank(pv13_revere_comproduct_company)` S=0.76, F=0.47, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_comproduct_company)`: S=0.76, F=0.47, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_comproduct_company / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_comproduct_company, 5))`: S=-0.10, F=-0.03, T=2.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_comproduct_company, 5))` | TOP3000 | 0.77 | 1.29 | 44.2% | 100% | mixed |
| `rank(ts_delta(pv13_revere_comproduct_company, 5))` | TOP500 | 0.43 | 0.39 | 47.0% | 80% | bull-only |
| `rank(pv13_revere_comproduct_company)` | TOP3000 | 0.40 | 0.19 | 17.0% | 40% | weak |
| `rank(ts_delta(pv13_revere_comproduct_company, 5))` | TOP200 | 0.14 | 0.10 | 69.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pv13_revere_index_value: 0.254 (weakly positively correlated)
- pv13_revere_index_cap: 0.250 (weakly positively correlated)
- implied_volatility_mean_skew_150: 0.218 (weakly positively correlated)
- implied_volatility_mean_skew_270: 0.216 (weakly positively correlated)
- implied_volatility_mean_skew_360: 0.216 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
