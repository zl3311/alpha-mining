---
field: fnd6_newa1v1300_ibc
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.51
best_fitness: 0.3
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.4397
ann_vol: 0.2173
hit_rate: 0.4964
rolling_sharpe_min: -1.731
rolling_sharpe_max: 2.397
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.09
---
# fnd6_newa1v1300_ibc (fundamental6)

*Income Before Extraordinary Items (Cash Flow)*

## Signal Profile
- `rank(fnd6_newa1v1300_ibc)`: S=0.01, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ibc / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ibc, 5))`: S=0.51, F=0.30, T=32.5%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ibc)`: S=0.02, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibc, 5))`: S=-0.38, F=-0.19, T=32.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_ibc, 63)`: S=-0.35, F=-0.17, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ibc, 10)`: S=0.10, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ibc, 22))`: S=-0.53, F=-0.29, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibc)`: S=0.42, F=0.29, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibc / close)`: S=0.40, F=0.27, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+11.1%
  - 2020: S=-0.47 (negative), ret=-7.9%
  - 2021: S=0.29 (weak), ret=+7.3%
  - 2022: S=1.69 (strong), ret=+52.0%
  - 2023: S=-0.66 (negative), ret=-9.4%

## Risk & Drawdown
- Max drawdown: 43.97% over 713 days (recovered)
- Annualized: return +10.8%, volatility 21.7% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew -0.92, excess kurtosis +18.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.73, max 2.40, latest -0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +35.57%; worst month: -13.34%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.25
- Sideways: S=0.92
- Bear: S=0.49

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ibc)` S=0.42, F=0.29, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ibc)`: S=0.42, F=0.29, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibc / close)`: S=0.40, F=0.27, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibc, 5))`: S=-0.38, F=-0.19, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ibc, 5))` | TOP200 | 0.50 | 0.30 | 44.0% | 60% | weak |
| `rank(fnd6_newa1v1300_ibc / close)` | TOP3000 | 0.10 | 0.04 | 34.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ibmii: 0.883 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.820 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.818 (strongly positively correlated)
- fnd6_newa2v1300_pi: 0.804 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.803 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
