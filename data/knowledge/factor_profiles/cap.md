---
field: cap
dataset: pv1
cluster: pv1_valuation
coverage: 1.0
community_alphas: 410049
best_template: rank_neg_delta
best_sharpe: 1.44
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4357
ann_vol: 0.1207
hit_rate: 0.515
rolling_sharpe_min: -2.964
rolling_sharpe_max: 2.193
negated_best_sharpe: 1.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.81
n_negated_sims: 4
direction_gap: 0.71
---
# cap (pv1)

*Daily market capitalization (in millions)*

## Signal Profile
- `rank(cap)`: S=0.14, F=0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cap, 5))`: S=-0.80, F=-0.38, T=36.3%, INFERIOR (TOP200)
- `-rank(cap)`: S=0.00, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cap, 5))`: S=1.44, F=0.81, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(cap, 63)`: S=0.73, F=0.58, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(cap, 10)`: S=0.16, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(cap, 22))`: S=-0.99, F=-0.63, T=24.4%, INFERIOR (TOP3000)
- `rank(-1 * cap)`: S=-0.14, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * cap / close)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 19F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P
- LOW_TURNOVER: 1F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+5.4%
  - 2020: S=-1.65 (negative), ret=-19.1%
  - 2021: S=0.23 (weak), ret=+3.3%
  - 2022: S=1.27 (moderate), ret=+17.2%
  - 2023: S=0.12 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 43.57% over 1265 days (recovered)
- Annualized: return +1.7%, volatility 12.1% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew -0.20, excess kurtosis +0.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.96, max 2.19, latest -0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.13%; worst month: -8.98%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.92
- Sideways: S=1.30
- Bear: S=-2.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(cap, 5))` S=1.44, F=0.81, INFERIOR
Direction gap: +0.71 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * cap)`: S=-0.14, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * cap / close)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cap, 5))`: S=1.44, F=0.81, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cap)` | TOP3000 | 0.14 | 0.05 | 43.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- low: 0.954 (strongly positively correlated)
- close: 0.954 (strongly positively correlated)
- open: 0.954 (strongly positively correlated)
- high: 0.953 (strongly positively correlated)
- vwap: 0.953 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
