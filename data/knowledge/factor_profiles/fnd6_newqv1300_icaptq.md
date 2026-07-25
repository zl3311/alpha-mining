---
field: fnd6_newqv1300_icaptq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3038
ann_vol: 0.1085
hit_rate: 0.519
rolling_sharpe_min: -3.183
rolling_sharpe_max: 2.531
redundancy_cluster: 13
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_newqv1300_icaptq (fundamental6)

*Invested Capital - Total - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_icaptq)`: S=0.63, F=0.47, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_icaptq / close)`: S=0.67, F=0.44, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_icaptq, 5))`: S=0.16, F=0.04, T=37.1%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_icaptq)`: S=-0.21, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_icaptq, 5))`: S=0.65, F=0.22, T=37.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_icaptq, 63)`: S=0.39, F=0.12, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_icaptq, 10)`: S=0.05, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_icaptq, 22))`: S=-0.08, F=-0.01, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_icaptq)`: S=-0.21, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_icaptq / close)`: S=-0.47, F=-0.28, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.71 (moderate), ret=+3.7%
  - 2020: S=-1.75 (negative), ret=-13.2%
  - 2021: S=1.02 (moderate), ret=+16.2%
  - 2022: S=1.66 (strong), ret=+21.4%
  - 2023: S=0.60 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 30.38% over 617 days (recovered)
- Annualized: return +6.8%, volatility 10.8% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.06, excess kurtosis +2.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.18, max 2.53, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.57%; worst month: -6.56%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.01
- Sideways: S=1.33
- Bear: S=-3.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_icaptq, 5))` S=0.65, F=0.22, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_icaptq)`: S=-0.21, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_icaptq / close)`: S=-0.47, F=-0.28, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_icaptq, 5))`: S=0.65, F=0.22, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_icaptq)` | TOP3000 | 0.62 | 0.47 | 30.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_icaptq / close)` | TOP3000 | 0.67 | 0.44 | 8.6% | 100% | bull-only |
| `rank(fnd6_newqv1300_icaptq / close)` | TOP1000 | 0.47 | 0.28 | 13.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_icaptq / close)` | TOP500 | 0.33 | 0.18 | 25.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_icaptq)` | TOP1000 | 0.21 | 0.10 | 35.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_icaptq, 5))` | TOP200 | 0.17 | 0.04 | 17.9% | 60% | weak |
| `rank(fnd6_newqv1300_icaptq)` | TOP500 | 0.07 | 0.02 | 48.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_icaptq / close)` | TOP200 | 0.06 | 0.02 | 32.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- invested_capital: 1.000 (strongly positively correlated)
- operating_expense: 0.987 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.987 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.982 (strongly positively correlated)
- fnd6_newqv1300_seqq: 0.981 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
