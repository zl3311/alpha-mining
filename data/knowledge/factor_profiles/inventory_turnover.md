---
field: inventory_turnover
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.87
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1777
ann_vol: 0.0565
hit_rate: 0.5352
rolling_sharpe_min: -3.089
rolling_sharpe_max: 2.828
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.51
n_negated_sims: 10
direction_gap: 0.34
---
# inventory_turnover (fundamental6)

*Inventory Turnover*

## Signal Profile
- `rank(inventory_turnover)`: S=0.53, F=0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(inventory_turnover / close)`: S=0.42, F=0.21, T=4.0%, INFERIOR (TOP500)
- `rank(ts_delta(inventory_turnover, 5))`: S=-0.49, F=-0.16, T=37.8%, INFERIOR (TOP1000)
- `-rank(inventory_turnover)`: S=-0.15, F=-0.04, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(inventory_turnover, 5))`: S=0.87, F=0.51, T=38.5%, INFERIOR (TOP3000)
- `-ts_zscore(inventory_turnover, 63)`: S=0.14, F=0.03, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(inventory_turnover, 10)`: S=0.04, F=0.01, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(inventory_turnover, 22))`: S=0.18, F=0.04, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * inventory_turnover)`: S=-0.02, F=0.00, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * inventory_turnover / close)`: S=0.45, F=0.27, T=5.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.1%
  - 2020: S=-1.87 (negative), ret=-8.8%
  - 2021: S=0.46 (weak), ret=+2.5%
  - 2022: S=2.04 (strong), ret=+14.8%
  - 2023: S=0.97 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 17.77% over 728 days (recovered)
- Annualized: return +3.0%, volatility 5.7% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew -0.43, excess kurtosis +1.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.09, max 2.83, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.72%; worst month: -6.09%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.03
- Sideways: S=1.23
- Bear: S=-1.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(inventory_turnover, 5))` S=0.87, F=0.51, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * inventory_turnover)`: S=-0.02, F=0.00, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * inventory_turnover / close)`: S=0.45, F=0.27, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(inventory_turnover, 5))`: S=0.87, F=0.51, T=38.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(inventory_turnover)` | TOP3000 | 0.53 | 0.26 | 17.8% | 80% | bull-only |
| `rank(inventory_turnover / close)` | TOP500 | 0.41 | 0.21 | 12.6% | 40% | mixed |
| `rank(inventory_turnover / close)` | TOP1000 | 0.26 | 0.10 | 17.0% | 60% | bear-only |
| `rank(inventory_turnover / close)` | TOP3000 | 0.15 | 0.05 | 27.5% | 40% | bear-only |
| `rank(inventory_turnover)` | TOP1000 | 0.14 | 0.04 | 20.5% | 40% | bull-only |
| `rank(inventory_turnover)` | TOP500 | 0.08 | 0.02 | 24.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_dilavq: 0.741 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.740 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.740 (strongly positively correlated)
- income_beforeextra: 0.739 (strongly positively correlated)
- fnd6_newqv1300_ibq: 0.739 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
