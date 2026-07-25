---
field: parkinson_volatility_150
dataset: option8
best_template: rank_level
best_sharpe: 0.26
best_fitness: 0.17
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.6308
ann_vol: 0.2137
hit_rate: 0.5101
rolling_sharpe_min: -1.736
rolling_sharpe_max: 3.278
negated_best_sharpe: -0.02
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.28
---
# parkinson_volatility_150 (option8)

*Historical Parkinson volatility for approximately 150 calendar days*

## Signal Profile
- `rank(parkinson_volatility_150)`: S=0.26, F=0.17, T=4.6%, INFERIOR (TOP200)
- `rank(parkinson_volatility_150 / close)`: S=0.02, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_150, 5))`: S=0.31, F=0.09, T=28.4%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_150)`: S=-0.02, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_150, 5))`: S=-0.31, F=-0.09, T=28.4%, INFERIOR (TOP3000)
- `-ts_zscore(parkinson_volatility_150, 63)`: S=0.26, F=0.10, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_150, 10)`: S=-0.17, F=-0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_150, 22))`: S=-0.54, F=-0.20, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_150)`: S=0.01, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_150 / close)`: S=0.02, F=0.00, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.27, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.16 (moderate), ret=+13.2%
  - 2020: S=2.79 (strong), ret=+42.6%
  - 2021: S=-0.50 (negative), ret=-12.8%
  - 2022: S=-1.02 (negative), ret=-31.4%
  - 2023: S=1.10 (moderate), ret=+16.7%

## Risk & Drawdown
- Max drawdown: 63.08% over 1046 days (not yet recovered, ongoing at window end)
- Annualized: return +5.8%, volatility 21.4% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.34, excess kurtosis +2.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.74, max 3.28, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +12.77%; worst month: -12.67%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.66
- Sideways: S=0.45
- Bear: S=3.02

## Negated Direction
Best negated: `-rank(parkinson_volatility_150)` S=-0.02, F=0.00, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_150)`: S=0.01, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_150 / close)`: S=0.02, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_150, 5))`: S=-0.31, F=-0.09, T=28.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(parkinson_volatility_150)` | TOP200 | 0.27 | 0.17 | 63.1% | 60% | bear-only |
| `rank(parkinson_volatility_150)` | TOP500 | 0.20 | 0.10 | 64.5% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_150, 5))` | TOP3000 | 0.30 | 0.09 | 18.3% | 100% | mixed |

## Correlation Notes
Top correlates:
- parkinson_volatility_180: 0.995 (strongly positively correlated)
- historical_volatility_150: 0.992 (strongly positively correlated)
- historical_volatility_180: 0.986 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.872 (strongly positively correlated)
- unsystematic_risk_last_30_days: 0.860 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
