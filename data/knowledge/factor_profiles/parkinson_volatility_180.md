---
field: parkinson_volatility_180
dataset: option8
best_template: rank_level
best_sharpe: 0.34
best_fitness: 0.26
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.5984
ann_vol: 0.2094
hit_rate: 0.5109
rolling_sharpe_min: -1.798
rolling_sharpe_max: 3.503
negated_best_sharpe: 0.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.22
---
# parkinson_volatility_180 (option8)

*Historical Parkinson volatility for approximately 180 calendar days*

## Signal Profile
- `rank(parkinson_volatility_180)`: S=0.34, F=0.26, T=4.5%, INFERIOR (TOP200)
- `rank(parkinson_volatility_180 / close)`: S=0.07, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_180, 5))`: S=0.47, F=0.17, T=28.0%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_180)`: S=-0.08, F=-0.03, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_180, 5))`: S=0.12, F=0.03, T=29.9%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_180, 22)`: S=0.54, F=0.23, T=23.2%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_180, 10)`: S=-0.14, F=-0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_180, 22))`: S=0.23, F=0.06, T=25.5%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_180)`: S=-0.34, F=-0.26, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_180 / close)`: S=-0.27, F=-0.14, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.35, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.47 (moderate), ret=+16.3%
  - 2020: S=2.97 (strong), ret=+44.8%
  - 2021: S=-0.49 (negative), ret=-12.3%
  - 2022: S=-0.93 (negative), ret=-28.0%
  - 2023: S=0.98 (moderate), ret=+15.0%

## Risk & Drawdown
- Max drawdown: 59.84% over 1043 days (not yet recovered, ongoing at window end)
- Annualized: return +7.3%, volatility 20.9% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.36, excess kurtosis +2.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 3.50, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +13.06%; worst month: -12.81%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.59
- Sideways: S=0.50
- Bear: S=3.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(parkinson_volatility_180, 5))` S=0.12, F=0.03, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_180)`: S=-0.34, F=-0.26, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_180 / close)`: S=-0.27, F=-0.14, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_180, 5))`: S=0.12, F=0.03, T=29.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(parkinson_volatility_180)` | TOP200 | 0.35 | 0.26 | 59.8% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_180, 5))` | TOP3000 | 0.46 | 0.17 | 10.8% | 100% | mixed |
| `rank(parkinson_volatility_180)` | TOP500 | 0.27 | 0.16 | 59.4% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_180, 5))` | TOP1000 | 0.31 | 0.10 | 16.8% | 80% | mixed |
| `rank(parkinson_volatility_180)` | TOP1000 | 0.09 | 0.03 | 60.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_150: 0.995 (strongly positively correlated)
- historical_volatility_180: 0.992 (strongly positively correlated)
- historical_volatility_150: 0.988 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.867 (strongly positively correlated)
- unsystematic_risk_last_30_days: 0.851 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
