---
field: fnd6_optvol
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.39
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 7
max_drawdown: 0.6892
ann_vol: 0.1871
hit_rate: 0.5182
rolling_sharpe_min: -1.962
rolling_sharpe_max: 3.879
negated_best_sharpe: 0.17
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.22
---
# fnd6_optvol (fundamental6)

*Volatility - Assumption (%)*

## Signal Profile
- `rank(fnd6_optvol)`: S=0.36, F=0.26, T=3.2%, INFERIOR (TOP200)
- `rank(fnd6_optvol / close)`: S=0.31, F=0.18, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optvol, 5))`: S=0.40, F=0.23, T=27.4%, INFERIOR (TOP500)
- `-rank(fnd6_optvol)`: S=0.08, F=0.03, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optvol, 5))`: S=-0.22, F=-0.08, T=39.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optvol, 63)`: S=0.39, F=0.35, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optvol, 10)`: S=0.06, F=0.02, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optvol, 22))`: S=-0.86, F=-0.77, T=20.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvol)`: S=0.10, F=0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvol / close)`: S=0.17, F=0.08, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.37 (moderate), ret=+12.4%
  - 2020: S=2.90 (strong), ret=+44.5%
  - 2021: S=0.02 (weak), ret=+0.6%
  - 2022: S=-1.45 (negative), ret=-36.2%
  - 2023: S=1.14 (moderate), ret=+11.1%

## Risk & Drawdown
- Max drawdown: 68.92% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +6.6%, volatility 18.7% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.19, excess kurtosis +2.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.96, max 3.88, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +19.71%; worst month: -13.40%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.54
- Sideways: S=0.44
- Bear: S=2.63

## Negated Direction
Best negated: `rank(-1 * fnd6_optvol / close)` S=0.17, F=0.08, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optvol)`: S=0.10, F=0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvol / close)`: S=0.17, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optvol, 5))`: S=-0.22, F=-0.08, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optvol)` | TOP200 | 0.35 | 0.26 | 68.9% | 80% | bear-only |
| `rank(ts_delta(fnd6_optvol, 5))` | TOP500 | 0.40 | 0.23 | 66.1% | 60% | mixed |
| `rank(fnd6_optvol / close)` | TOP200 | 0.30 | 0.18 | 47.8% | 60% | bear-only |
| `rank(ts_delta(fnd6_optvol, 5))` | TOP3000 | 0.32 | 0.16 | 63.1% | 80% | weak |
| `rank(ts_delta(fnd6_optvol, 5))` | TOP200 | 0.25 | 0.15 | 77.5% | 60% | mixed |
| `rank(fnd6_optvol / close)` | TOP500 | 0.19 | 0.08 | 43.8% | 60% | bear-only |
| `rank(fnd6_optvol / close)` | TOP1000 | 0.07 | 0.02 | 40.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.849 (strongly positively correlated)
- parkinson_volatility_150: 0.801 (strongly positively correlated)
- parkinson_volatility_180: 0.800 (strongly positively correlated)
- historical_volatility_150: 0.797 (strongly positively correlated)
- historical_volatility_180: 0.796 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
