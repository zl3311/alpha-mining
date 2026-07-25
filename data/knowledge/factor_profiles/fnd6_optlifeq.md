---
field: fnd6_optlifeq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.52
best_fitness: 0.54
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.3659
ann_vol: 0.3018
hit_rate: 0.5231
rolling_sharpe_min: -0.809
rolling_sharpe_max: 2.427
redundancy_cluster: 80
negated_best_sharpe: 0.49
negated_best_template: neg_rank
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.03
---
# fnd6_optlifeq (fundamental6)

*Life of Options - Assumption (# yrs)*

## Signal Profile
- `rank(fnd6_optlifeq)`: S=0.07, F=0.02, T=12.0%, INFERIOR (TOP500)
- `rank(fnd6_optlifeq / close)`: S=0.52, F=0.54, T=14.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optlifeq, 5))`: S=0.53, F=0.45, T=16.5%, INFERIOR (TOP200)
- `-rank(fnd6_optlifeq)`: S=0.49, F=0.33, T=10.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optlifeq, 5))`: S=0.42, F=0.24, T=44.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optlifeq, 22)`: S=0.25, F=0.17, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optlifeq, 10)`: S=-0.04, F=-0.01, T=6.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optlifeq, 22))`: S=-0.51, F=-0.33, T=27.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlifeq)`: S=0.48, F=0.25, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlifeq / close)`: S=0.27, F=0.16, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+11.7%
  - 2020: S=0.51 (moderate), ret=+21.2%
  - 2021: S=1.09 (moderate), ret=+31.3%
  - 2022: S=0.37 (weak), ret=+11.2%
  - 2023: S=0.01 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 36.59% over 196 days (recovered)
- Annualized: return +15.5%, volatility 30.2% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.30, excess kurtosis +19.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.43, latest 0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +25.99%; worst month: -16.46%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.20
- Sideways: S=0.32
- Bear: S=1.35

## Negated Direction
Best negated: `-rank(fnd6_optlifeq)` S=0.49, F=0.33, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optlifeq)`: S=0.48, F=0.25, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlifeq / close)`: S=0.27, F=0.16, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optlifeq, 5))`: S=0.42, F=0.24, T=44.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optlifeq / close)` | TOP200 | 0.51 | 0.54 | 36.6% | 100% | mixed |
| `rank(ts_delta(fnd6_optlifeq, 5))` | TOP200 | 0.52 | 0.45 | 38.0% | 60% | mixed |
| `rank(ts_delta(fnd6_optlifeq, 5))` | TOP1000 | 0.23 | 0.09 | 101.2% | 40% | mixed |
| `rank(ts_delta(fnd6_optlifeq, 5))` | TOP500 | 0.13 | 0.04 | 63.3% | 40% | bull-only |
| `rank(fnd6_optlifeq)` | TOP500 | 0.07 | 0.02 | 19.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_optrfrq: 0.825 (strongly positively correlated)
- fnd6_optvolq: 0.681 (moderately positively correlated)
- historical_volatility_180: 0.223 (weakly positively correlated)
- historical_volatility_150: 0.222 (weakly positively correlated)
- parkinson_volatility_180: 0.213 (weakly positively correlated)

Redundancy cluster #80: 3 similar fields, mean |rho| 0.756 (representative: fnd6_newqv1300_optrfrq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
