---
field: unsystematic_risk_last_30_days
dataset: model51
best_template: rank_level
best_sharpe: 0.43
best_fitness: 0.27
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.4395
ann_vol: 0.178
hit_rate: 0.5206
rolling_sharpe_min: -1.522
rolling_sharpe_max: 3.421
negated_best_sharpe: 0.07
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.36
---
# unsystematic_risk_last_30_days (model51)

*The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 30 calendar days*

## Signal Profile
- `rank(unsystematic_risk_last_30_days)`: S=0.43, F=0.27, T=19.7%, INFERIOR (TOP200)
- `rank(unsystematic_risk_last_30_days / close)`: S=0.08, F=0.02, T=13.4%, INFERIOR (TOP3000)
- `rank(ts_delta(unsystematic_risk_last_30_days, 5))`: S=0.50, F=0.14, T=47.4%, INFERIOR (TOP500)
- `-rank(unsystematic_risk_last_30_days)`: S=-0.09, F=-0.03, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_30_days, 5))`: S=-0.36, F=-0.07, T=52.4%, INFERIOR (TOP3000)
- `ts_zscore(unsystematic_risk_last_30_days, 22)`: S=0.50, F=0.16, T=31.1%, INFERIOR (TOP3000)
- `ts_mean(unsystematic_risk_last_30_days, 10)`: S=0.03, F=0.01, T=7.1%, INFERIOR (TOP3000)
- `rank(ts_rank(unsystematic_risk_last_30_days, 22))`: S=0.52, F=0.16, T=32.9%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_30_days)`: S=0.07, F=0.02, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_30_days / close)`: S=0.05, F=0.01, T=15.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.67 (moderate), ret=+5.2%
  - 2020: S=2.47 (strong), ret=+33.3%
  - 2021: S=-0.39 (negative), ret=-10.2%
  - 2022: S=0.05 (weak), ret=+1.2%
  - 2023: S=0.76 (moderate), ret=+8.5%

## Risk & Drawdown
- Max drawdown: 43.95% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +7.8%, volatility 17.8% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.32, excess kurtosis +3.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 3.42, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +14.66%; worst month: -15.12%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.31
- Sideways: S=0.69
- Bear: S=2.87

## Negated Direction
Best negated: `rank(-1 * unsystematic_risk_last_30_days)` S=0.07, F=0.02, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * unsystematic_risk_last_30_days)`: S=0.07, F=0.02, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_30_days / close)`: S=0.05, F=0.01, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_30_days, 5))`: S=-0.36, F=-0.07, T=52.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(unsystematic_risk_last_30_days)` | TOP200 | 0.44 | 0.27 | 44.0% | 80% | bear-only |
| `rank(ts_delta(unsystematic_risk_last_30_days, 5))` | TOP500 | 0.49 | 0.14 | 18.5% | 80% | bull-only |
| `rank(ts_delta(unsystematic_risk_last_30_days, 5))` | TOP1000 | 0.43 | 0.11 | 13.6% | 60% | mixed |
| `rank(ts_delta(unsystematic_risk_last_30_days, 5))` | TOP3000 | 0.36 | 0.07 | 7.7% | 60% | mixed |
| `rank(unsystematic_risk_last_30_days)` | TOP500 | 0.17 | 0.06 | 53.1% | 40% | bear-only |
| `rank(unsystematic_risk_last_30_days)` | TOP1000 | 0.10 | 0.03 | 50.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_150: 0.860 (strongly positively correlated)
- historical_volatility_150: 0.852 (strongly positively correlated)
- parkinson_volatility_180: 0.851 (strongly positively correlated)
- historical_volatility_180: 0.842 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.838 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
