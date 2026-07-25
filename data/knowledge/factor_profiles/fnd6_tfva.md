---
field: fnd6_tfva
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2017
ann_vol: 0.0616
hit_rate: 0.5174
rolling_sharpe_min: -2.409
rolling_sharpe_max: 3.026
redundancy_cluster: 17
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: 0.07
---
# fnd6_tfva (fundamental6)

*Total Fair Value Assets*

## Signal Profile
- `rank(fnd6_tfva)`: S=0.52, F=0.26, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_tfva / close)`: S=0.52, F=0.25, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_tfva, 5))`: S=0.12, F=0.03, T=33.0%, INFERIOR (TOP500)
- `-rank(fnd6_tfva)`: S=-0.32, F=-0.14, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfva, 5))`: S=0.59, F=0.42, T=26.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_tfva, 63)`: S=0.37, F=0.22, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_tfva, 10)`: S=0.47, F=0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_tfva, 22))`: S=0.31, F=0.13, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfva)`: S=0.05, F=0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfva / close)`: S=-0.19, F=-0.08, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+1.9%
  - 2020: S=-1.16 (negative), ret=-7.1%
  - 2021: S=0.25 (weak), ret=+2.2%
  - 2022: S=1.98 (strong), ret=+10.4%
  - 2023: S=1.75 (strong), ret=+8.4%

## Risk & Drawdown
- Max drawdown: 20.17% over 945 days (recovered)
- Annualized: return +3.2%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.10, excess kurtosis +1.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.41, max 3.03, latest 1.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.29%; worst month: -4.36%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.17
- Sideways: S=1.70
- Bear: S=-2.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_tfva, 5))` S=0.59, F=0.42, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_tfva)`: S=0.05, F=0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfva / close)`: S=-0.19, F=-0.08, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfva, 5))`: S=0.59, F=0.42, T=26.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_tfva)` | TOP3000 | 0.53 | 0.26 | 20.2% | 80% | bull-only |
| `rank(fnd6_tfva / close)` | TOP3000 | 0.53 | 0.25 | 7.0% | 80% | mixed |
| `rank(fnd6_tfva)` | TOP1000 | 0.32 | 0.14 | 24.7% | 60% | bull-only |
| `rank(fnd6_tfva / close)` | TOP1000 | 0.34 | 0.14 | 11.7% | 80% | bull-only |
| `rank(fnd6_tfva / close)` | TOP500 | 0.29 | 0.12 | 19.2% | 60% | bull-only |
| `rank(fnd6_tfva / close)` | TOP200 | 0.19 | 0.08 | 26.8% | 80% | bull-only |
| `rank(fnd6_tfva)` | TOP500 | 0.13 | 0.04 | 36.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_tfva, 5))` | TOP500 | 0.12 | 0.03 | 46.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cash: 0.896 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.861 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.853 (strongly positively correlated)
- sga_expense: 0.840 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.840 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
