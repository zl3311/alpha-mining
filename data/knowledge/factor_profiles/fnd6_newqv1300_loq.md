---
field: fnd6_newqv1300_loq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0938
ann_vol: 0.0688
hit_rate: 0.4883
rolling_sharpe_min: -1.026
rolling_sharpe_max: 2.807
redundancy_cluster: 1
negated_best_sharpe: 0.08
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.69
---
# fnd6_newqv1300_loq (fundamental6)

*Liabilities - Other*

## Signal Profile
- `rank(fnd6_newqv1300_loq)`: S=0.61, F=0.42, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_loq / close)`: S=0.77, F=0.50, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_loq, 5))`: S=0.51, F=0.15, T=38.8%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_loq)`: S=-0.33, F=-0.19, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_loq, 5))`: S=0.09, F=0.01, T=38.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_loq, 63)`: S=0.57, F=0.19, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_loq, 10)`: S=0.24, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_loq, 22))`: S=-0.21, F=-0.05, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loq)`: S=0.08, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loq / close)`: S=0.08, F=0.02, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.76, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-0.7%
  - 2020: S=0.07 (weak), ret=+0.6%
  - 2021: S=1.69 (strong), ret=+16.2%
  - 2022: S=1.03 (moderate), ret=+6.8%
  - 2023: S=0.73 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 9.38% over 91 days (recovered)
- Annualized: return +5.3%, volatility 6.9% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.51, excess kurtosis +3.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 2.81, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.53%; worst month: -3.81%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.08
- Sideways: S=0.36
- Bear: S=-1.80

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_loq)` S=0.08, F=0.03, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_loq)`: S=0.08, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_loq / close)`: S=0.08, F=0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_loq, 5))`: S=0.09, F=0.01, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_loq / close)` | TOP3000 | 0.76 | 0.50 | 9.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_loq)` | TOP3000 | 0.60 | 0.42 | 26.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_loq / close)` | TOP1000 | 0.53 | 0.35 | 14.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_loq)` | TOP1000 | 0.32 | 0.19 | 32.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_loq, 5))` | TOP1000 | 0.51 | 0.15 | 16.9% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_loq, 5))` | TOP3000 | 0.56 | 0.14 | 10.7% | 40% | all-weather |
| `rank(fnd6_newqv1300_loq / close)` | TOP500 | 0.23 | 0.11 | 27.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_loq, 5))` | TOP500 | 0.19 | 0.04 | 20.3% | 60% | mixed |
| `rank(fnd6_newqv1300_loq)` | TOP500 | 0.11 | 0.04 | 44.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lo: 0.987 (strongly positively correlated)
- fnd6_newqv1300_loxdrq: 0.976 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.948 (strongly positively correlated)
- fnd6_newqv1300_altoq: 0.945 (strongly positively correlated)
- fnd6_aodo: 0.945 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
