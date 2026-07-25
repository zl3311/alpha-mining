---
field: fnd6_newqv1300_cshoq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.26
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1388
ann_vol: 0.0654
hit_rate: 0.5004
rolling_sharpe_min: -0.812
rolling_sharpe_max: 1.994
redundancy_cluster: 31
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.21
---
# fnd6_newqv1300_cshoq (fundamental6)

*Common Shares Outstanding*

## Signal Profile
- `rank(fnd6_newqv1300_cshoq)`: S=0.21, F=0.08, T=1.7%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_cshoq / close)`: S=0.51, F=0.26, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_cshoq, 5))`: S=0.06, F=0.01, T=36.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_cshoq)`: S=-0.22, F=-0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshoq, 5))`: S=0.72, F=0.24, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cshoq, 63)`: S=0.25, F=0.10, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cshoq, 10)`: S=0.01, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cshoq, 22))`: S=-0.28, F=-0.09, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshoq)`: S=-0.13, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshoq / close)`: S=0.03, F=0.00, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+3.3%
  - 2020: S=0.61 (moderate), ret=+4.7%
  - 2021: S=-0.53 (negative), ret=-4.3%
  - 2022: S=1.79 (strong), ret=+10.8%
  - 2023: S=0.37 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 13.88% over 517 days (recovered)
- Annualized: return +3.3%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.43, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 1.99, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.21%; worst month: -2.74%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.48
- Sideways: S=-0.41
- Bear: S=0.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cshoq, 5))` S=0.72, F=0.24, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cshoq)`: S=-0.13, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshoq / close)`: S=0.03, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshoq, 5))`: S=0.72, F=0.24, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cshoq / close)` | TOP500 | 0.51 | 0.26 | 13.9% | 80% | mixed |
| `rank(fnd6_newqv1300_cshoq / close)` | TOP200 | 0.37 | 0.18 | 20.9% | 80% | mixed |
| `rank(fnd6_newqv1300_cshoq / close)` | TOP1000 | 0.31 | 0.13 | 15.0% | 80% | mixed |
| `rank(fnd6_newqv1300_cshoq)` | TOP500 | 0.21 | 0.08 | 22.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshoq)` | TOP1000 | 0.23 | 0.07 | 13.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshoq)` | TOP3000 | 0.14 | 0.03 | 8.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cshprq: 0.997 (strongly positively correlated)
- fnd6_mfmq_cshprq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_cshfdq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.993 (strongly positively correlated)
- fnd6_mfma1_csho: 0.973 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
