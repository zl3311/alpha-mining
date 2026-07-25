---
field: fnd6_newqv1300_loxdrq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1326
ann_vol: 0.0767
hit_rate: 0.485
rolling_sharpe_min: -1.45
rolling_sharpe_max: 2.665
redundancy_cluster: 1
negated_best_sharpe: 0.11
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.4
---
# fnd6_newqv1300_loxdrq (fundamental6)

*Liabilities - Other - Excluding Deferred Revenue*

## Signal Profile
- `rank(fnd6_newqv1300_loxdrq)`: S=0.45, F=0.28, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_loxdrq / close)`: S=0.51, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_loxdrq, 5))`: S=0.54, F=0.16, T=39.0%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_loxdrq)`: S=-0.28, F=-0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_loxdrq, 5))`: S=0.18, F=0.04, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_loxdrq, 63)`: S=0.57, F=0.20, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_loxdrq, 10)`: S=0.17, F=0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_loxdrq, 22))`: S=-0.46, F=-0.15, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loxdrq)`: S=0.10, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loxdrq / close)`: S=0.11, F=0.04, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.63 (negative), ret=-2.8%
  - 2020: S=-0.50 (negative), ret=-4.0%
  - 2021: S=1.61 (strong), ret=+17.3%
  - 2022: S=0.83 (moderate), ret=+6.6%
  - 2023: S=0.43 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 13.26% over 789 days (recovered)
- Annualized: return +3.9%, volatility 7.7% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.34, excess kurtosis +3.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 2.67, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.72%; worst month: -4.59%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=0.06
- Bear: S=-2.31

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_loxdrq / close)` S=0.11, F=0.04, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_loxdrq)`: S=0.10, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loxdrq / close)`: S=0.11, F=0.04, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_loxdrq, 5))`: S=0.18, F=0.04, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_loxdrq / close)` | TOP3000 | 0.50 | 0.29 | 13.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_loxdrq)` | TOP3000 | 0.44 | 0.28 | 31.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_loxdrq / close)` | TOP1000 | 0.40 | 0.24 | 18.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_loxdrq, 5))` | TOP1000 | 0.54 | 0.16 | 15.0% | 60% | mixed |
| `rank(fnd6_newqv1300_loxdrq)` | TOP1000 | 0.27 | 0.15 | 34.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_loxdrq, 5))` | TOP3000 | 0.47 | 0.11 | 8.1% | 60% | all-weather |
| `rank(fnd6_newqv1300_loxdrq / close)` | TOP500 | 0.13 | 0.05 | 33.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_loxdrq)` | TOP500 | 0.06 | 0.02 | 48.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_loxdrq, 5))` | TOP500 | 0.11 | 0.02 | 20.0% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_loq: 0.976 (strongly positively correlated)
- fnd6_newa1v1300_lo: 0.964 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.946 (strongly positively correlated)
- fnd6_aodo: 0.944 (strongly positively correlated)
- fnd6_aox: 0.943 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
