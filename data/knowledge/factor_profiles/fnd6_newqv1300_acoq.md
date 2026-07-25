---
field: fnd6_newqv1300_acoq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.71
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2443
ann_vol: 0.0949
hit_rate: 0.5174
rolling_sharpe_min: -2.918
rolling_sharpe_max: 2.538
redundancy_cluster: 13
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.22
---
# fnd6_newqv1300_acoq (fundamental6)

*Current Assets - Other - Total*

## Signal Profile
- `rank(fnd6_newqv1300_acoq)`: S=0.71, F=0.52, T=2.3%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_acoq / close)`: S=0.79, F=0.51, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_acoq, 5))`: S=0.50, F=0.13, T=38.9%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_acoq)`: S=-0.36, F=-0.20, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_acoq, 5))`: S=0.49, F=0.17, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_acoq, 63)`: S=0.49, F=0.16, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_acoq, 10)`: S=-0.06, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_acoq, 22))`: S=-0.15, F=-0.03, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acoq)`: S=-0.14, F=-0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acoq / close)`: S=-0.41, F=-0.23, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+3.5%
  - 2020: S=-1.77 (negative), ret=-11.5%
  - 2021: S=1.14 (moderate), ret=+15.6%
  - 2022: S=1.73 (strong), ret=+19.8%
  - 2023: S=0.76 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 24.43% over 792 days (recovered)
- Annualized: return +6.7%, volatility 9.5% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.03, excess kurtosis +2.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.92, max 2.54, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.73%; worst month: -4.91%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=1.21
- Bear: S=-2.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_acoq, 5))` S=0.49, F=0.17, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_acoq)`: S=-0.14, F=-0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acoq / close)`: S=-0.41, F=-0.23, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_acoq, 5))`: S=0.49, F=0.17, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_acoq)` | TOP3000 | 0.71 | 0.52 | 24.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_acoq / close)` | TOP3000 | 0.78 | 0.51 | 8.0% | 100% | mixed |
| `rank(fnd6_newqv1300_acoq / close)` | TOP1000 | 0.56 | 0.34 | 10.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_acoq / close)` | TOP500 | 0.40 | 0.23 | 19.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_acoq)` | TOP1000 | 0.35 | 0.20 | 29.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_acoq, 5))` | TOP3000 | 0.52 | 0.13 | 10.2% | 80% | mixed |
| `rank(fnd6_newqv1300_acoq)` | TOP500 | 0.13 | 0.05 | 43.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_actq: 0.978 (strongly positively correlated)
- assets_curr: 0.978 (strongly positively correlated)
- fnd6_cptmfmq_actq: 0.978 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.978 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.975 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
