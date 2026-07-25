---
field: fnd6_newqv1300_optrfrq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.65
best_fitness: 0.73
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.3548
ann_vol: 0.2871
hit_rate: 0.5142
rolling_sharpe_min: -1.204
rolling_sharpe_max: 2.085
redundancy_cluster: 80
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.31
---
# fnd6_newqv1300_optrfrq (fundamental6)

*Risk-Free Rate - Assumption (%)*

## Signal Profile
- `rank(fnd6_newqv1300_optrfrq)`: S=0.01, F=0.00, T=14.8%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_optrfrq / close)`: S=0.65, F=0.73, T=14.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_optrfrq, 5))`: S=-0.09, F=-0.03, T=25.1%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_optrfrq)`: S=0.12, F=0.04, T=11.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_optrfrq, 5))`: S=0.34, F=0.15, T=55.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_optrfrq, 22)`: S=0.09, F=0.03, T=24.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_optrfrq, 10)`: S=-0.32, F=-0.17, T=7.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_optrfrq, 22))`: S=-0.04, F=-0.01, T=25.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optrfrq)`: S=0.06, F=0.02, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optrfrq / close)`: S=-0.07, F=-0.02, T=12.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.06 (moderate), ret=+21.4%
  - 2020: S=1.17 (moderate), ret=+39.8%
  - 2021: S=0.66 (moderate), ret=+19.6%
  - 2022: S=0.29 (weak), ret=+9.2%
  - 2023: S=0.04 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 35.48% over 427 days (recovered)
- Annualized: return +18.6%, volatility 28.7% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.16, excess kurtosis +7.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.08, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +22.13%; worst month: -18.76%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.36
- Sideways: S=1.31
- Bear: S=1.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_optrfrq, 5))` S=0.34, F=0.15, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_optrfrq)`: S=0.06, F=0.02, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optrfrq / close)`: S=-0.07, F=-0.02, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_optrfrq, 5))`: S=0.34, F=0.15, T=55.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_optrfrq / close)` | TOP200 | 0.65 | 0.73 | 35.5% | 100% | mixed |
| `rank(fnd6_newqv1300_optrfrq / close)` | TOP500 | 0.05 | 0.02 | 38.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_optlifeq: 0.825 (strongly positively correlated)
- fnd6_optvolq: 0.761 (strongly positively correlated)
- fnd6_optex: 0.228 (weakly positively correlated)
- fn_antidilutive_securities_excl_from_eps_q: 0.218 (weakly positively correlated)
- historical_volatility_180: 0.210 (weakly positively correlated)

Redundancy cluster #80: 3 similar fields, mean |rho| 0.756 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
