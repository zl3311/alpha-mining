---
field: historical_volatility_150
dataset: option8
best_template: rank_level
best_sharpe: 0.22
best_fitness: 0.13
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.6071
ann_vol: 0.2101
hit_rate: 0.5004
rolling_sharpe_min: -1.748
rolling_sharpe_max: 3.121
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: 0.02
---
# historical_volatility_150 (option8)

*Historical close-to-close volatility for approximately 150 calendar days*

## Signal Profile
- `rank(historical_volatility_150)`: S=0.22, F=0.13, T=5.3%, INFERIOR (TOP200)
- `rank(historical_volatility_150 / close)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_150, 5))`: S=0.05, F=0.01, T=32.5%, INFERIOR (TOP3000)
- `-rank(historical_volatility_150)`: S=-0.06, F=-0.02, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_150, 5))`: S=0.24, F=0.06, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(historical_volatility_150, 63)`: S=0.31, F=0.12, T=13.9%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_150, 10)`: S=-0.05, F=-0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_150, 22))`: S=-0.58, F=-0.21, T=25.9%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_150)`: S=-0.06, F=-0.02, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_150 / close)`: S=-0.03, F=-0.01, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+12.0%
  - 2020: S=2.54 (strong), ret=+40.2%
  - 2021: S=-0.57 (negative), ret=-14.5%
  - 2022: S=-0.94 (negative), ret=-27.9%
  - 2023: S=0.92 (moderate), ret=+13.7%

## Risk & Drawdown
- Max drawdown: 60.71% over 1046 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 21.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.37, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.75, max 3.12, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +11.12%; worst month: -12.63%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.59
- Sideways: S=0.21
- Bear: S=2.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(historical_volatility_150, 5))` S=0.24, F=0.06, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * historical_volatility_150)`: S=-0.06, F=-0.02, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_150 / close)`: S=-0.03, F=-0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_150, 5))`: S=0.24, F=0.06, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(historical_volatility_150)` | TOP200 | 0.23 | 0.13 | 60.7% | 60% | bear-only |
| `rank(historical_volatility_150)` | TOP500 | 0.22 | 0.12 | 64.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_180: 0.994 (strongly positively correlated)
- parkinson_volatility_150: 0.992 (strongly positively correlated)
- parkinson_volatility_180: 0.988 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.861 (strongly positively correlated)
- unsystematic_risk_last_30_days: 0.852 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
