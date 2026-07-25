---
field: fnd6_optvolq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.53
best_fitness: 0.53
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.4952
ann_vol: 0.2737
hit_rate: 0.5166
rolling_sharpe_min: -1.766
rolling_sharpe_max: 2.131
redundancy_cluster: 80
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_optvolq (fundamental6)

*Volatility - Assumption (%)*

## Signal Profile
- `rank(fnd6_optvolq)`: S=0.30, F=0.23, T=15.0%, INFERIOR (TOP200)
- `rank(fnd6_optvolq / close)`: S=0.53, F=0.53, T=14.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optvolq, 5))`: S=0.25, F=0.10, T=47.8%, INFERIOR (TOP3000)
- `-rank(fnd6_optvolq)`: S=0.24, F=0.15, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optvolq, 5))`: S=-0.28, F=-0.12, T=47.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optvolq, 22)`: S=0.51, F=0.41, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optvolq, 10)`: S=-0.19, F=-0.12, T=6.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optvolq, 22))`: S=-0.34, F=-0.18, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvolq)`: S=0.38, F=0.28, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvolq / close)`: S=0.34, F=0.23, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.89 (moderate), ret=+19.9%
  - 2020: S=0.70 (moderate), ret=+20.9%
  - 2021: S=0.68 (moderate), ret=+17.4%
  - 2022: S=0.33 (weak), ret=+10.7%
  - 2023: S=0.10 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 49.52% over 625 days (recovered)
- Annualized: return +14.5%, volatility 27.4% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.46, excess kurtosis +5.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.13, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +21.98%; worst month: -17.16%
Positive months: 49%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.08
- Sideways: S=0.91
- Bear: S=1.75

## Negated Direction
Best negated: `rank(-1 * fnd6_optvolq)` S=0.38, F=0.28, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optvolq)`: S=0.38, F=0.28, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optvolq / close)`: S=0.34, F=0.23, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optvolq, 5))`: S=-0.28, F=-0.12, T=47.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optvolq / close)` | TOP200 | 0.53 | 0.53 | 49.5% | 100% | bear-only |
| `rank(fnd6_optvolq)` | TOP200 | 0.30 | 0.23 | 68.3% | 60% | bear-only |
| `rank(ts_delta(fnd6_optvolq, 5))` | TOP3000 | 0.29 | 0.10 | 56.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_optrfrq: 0.761 (strongly positively correlated)
- fnd6_optlifeq: 0.681 (moderately positively correlated)
- historical_volatility_150: 0.355 (weakly positively correlated)
- historical_volatility_180: 0.354 (weakly positively correlated)
- parkinson_volatility_180: 0.350 (weakly positively correlated)

Redundancy cluster #80: 3 similar fields, mean |rho| 0.756 (representative: fnd6_newqv1300_optrfrq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
