---
field: fnd6_newqv1300_intanq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.69
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1241
ann_vol: 0.073
hit_rate: 0.4899
rolling_sharpe_min: -1.237
rolling_sharpe_max: 2.224
redundancy_cluster: 1
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.17
---
# fnd6_newqv1300_intanq (fundamental6)

*Intangible Assets - Total*

## Signal Profile
- `rank(fnd6_newqv1300_intanq)`: S=0.41, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_intanq / close)`: S=0.52, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_intanq, 5))`: S=0.46, F=0.12, T=37.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_intanq)`: S=-0.08, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_intanq, 5))`: S=0.69, F=0.34, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_intanq, 63)`: S=0.31, F=0.09, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_intanq, 10)`: S=-0.06, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_intanq, 22))`: S=0.50, F=0.18, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanq)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanq / close)`: S=0.11, F=0.04, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.52, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+1.8%
  - 2020: S=-0.42 (negative), ret=-3.0%
  - 2021: S=1.09 (moderate), ret=+11.5%
  - 2022: S=1.13 (moderate), ret=+9.2%
  - 2023: S=-0.27 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 12.41% over 316 days (recovered)
- Annualized: return +3.8%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.20, excess kurtosis +2.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 2.22, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.97%; worst month: -3.23%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.42
- Bear: S=-2.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_intanq, 5))` S=0.69, F=0.34, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_intanq)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanq / close)`: S=0.11, F=0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_intanq, 5))`: S=0.69, F=0.34, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_intanq / close)` | TOP3000 | 0.52 | 0.29 | 12.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_intanq)` | TOP3000 | 0.41 | 0.23 | 25.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_intanq, 5))` | TOP3000 | 0.47 | 0.12 | 10.9% | 60% | bear-only |
| `rank(fnd6_newqv1300_intanq / close)` | TOP1000 | 0.22 | 0.10 | 17.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_intanq, 5))` | TOP500 | 0.15 | 0.03 | 21.6% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_intanq, 5))` | TOP1000 | 0.16 | 0.03 | 15.9% | 80% | weak |
| `rank(fnd6_newqv1300_intanq)` | TOP1000 | 0.08 | 0.02 | 31.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_intan: 0.988 (strongly positively correlated)
- fnd6_newa1v1300_intano: 0.976 (strongly positively correlated)
- goodwill: 0.975 (strongly positively correlated)
- fnd6_newqv1300_gdwlq: 0.975 (strongly positively correlated)
- fnd6_am: 0.964 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
