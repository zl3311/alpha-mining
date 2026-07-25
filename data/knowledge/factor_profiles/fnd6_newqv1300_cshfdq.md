---
field: fnd6_newqv1300_cshfdq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1363
ann_vol: 0.0649
hit_rate: 0.5004
rolling_sharpe_min: -0.845
rolling_sharpe_max: 2.029
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_newqv1300_cshfdq (fundamental6)

*Common Shares for Diluted EPS*

## Signal Profile
- `rank(fnd6_newqv1300_cshfdq)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_cshfdq / close)`: S=0.48, F=0.24, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_cshfdq, 5))`: S=-0.11, F=-0.02, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cshfdq)`: S=-0.24, F=-0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshfdq, 5))`: S=0.46, F=0.13, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cshfdq, 63)`: S=0.54, F=0.31, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cshfdq, 10)`: S=0.04, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cshfdq, 22))`: S=-0.37, F=-0.14, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshfdq)`: S=-0.12, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshfdq / close)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+2.6%
  - 2020: S=0.53 (moderate), ret=+4.1%
  - 2021: S=-0.51 (negative), ret=-4.1%
  - 2022: S=1.82 (strong), ret=+11.0%
  - 2023: S=0.34 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 13.63% over 512 days (recovered)
- Annualized: return +3.1%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.44, excess kurtosis +1.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.03, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +4.94%; worst month: -2.63%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.54
- Sideways: S=-0.52
- Bear: S=0.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cshfdq, 5))` S=0.46, F=0.13, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cshfdq)`: S=-0.12, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshfdq / close)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshfdq, 5))`: S=0.46, F=0.13, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cshfdq / close)` | TOP500 | 0.48 | 0.24 | 13.6% | 80% | mixed |
| `rank(fnd6_newqv1300_cshfdq / close)` | TOP200 | 0.35 | 0.16 | 20.9% | 80% | mixed |
| `rank(fnd6_newqv1300_cshfdq / close)` | TOP1000 | 0.33 | 0.14 | 14.8% | 80% | all-weather |
| `rank(fnd6_newqv1300_cshfdq)` | TOP1000 | 0.24 | 0.08 | 13.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshfdq)` | TOP500 | 0.20 | 0.07 | 23.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshfdq)` | TOP3000 | 0.13 | 0.03 | 8.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cshprq: 1.000 (strongly positively correlated)
- fnd6_mfmq_cshprq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.997 (strongly positively correlated)
- fnd6_mfma1_csho: 0.973 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
