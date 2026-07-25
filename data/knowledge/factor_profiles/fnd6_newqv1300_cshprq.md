---
field: fnd6_newqv1300_cshprq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1365
ann_vol: 0.0651
hit_rate: 0.4996
rolling_sharpe_min: -0.851
rolling_sharpe_max: 2.033
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.1
---
# fnd6_newqv1300_cshprq (fundamental6)

*Common Shares Used to Calculate Earnings Per Share - Basic*

## Signal Profile
- `rank(fnd6_newqv1300_cshprq)`: S=0.25, F=0.09, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_cshprq / close)`: S=0.47, F=0.23, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_cshprq, 5))`: S=0.08, F=0.01, T=37.5%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cshprq)`: S=-0.25, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshprq, 5))`: S=0.76, F=0.31, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cshprq, 63)`: S=0.66, F=0.44, T=20.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cshprq, 10)`: S=0.04, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cshprq, 22))`: S=-0.65, F=-0.32, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshprq)`: S=-0.25, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshprq / close)`: S=-0.33, F=-0.14, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+2.6%
  - 2020: S=0.53 (moderate), ret=+4.1%
  - 2021: S=-0.52 (negative), ret=-4.2%
  - 2022: S=1.82 (strong), ret=+11.1%
  - 2023: S=0.32 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 13.65% over 512 days (recovered)
- Annualized: return +3.1%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.44, excess kurtosis +1.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 2.03, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +4.95%; worst month: -2.69%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.53
- Sideways: S=-0.51
- Bear: S=0.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cshprq, 5))` S=0.76, F=0.31, INFERIOR
Direction gap: +0.10 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cshprq)`: S=-0.25, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshprq / close)`: S=-0.33, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshprq, 5))`: S=0.76, F=0.31, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cshprq / close)` | TOP500 | 0.47 | 0.23 | 13.7% | 80% | mixed |
| `rank(fnd6_newqv1300_cshprq / close)` | TOP200 | 0.33 | 0.15 | 20.9% | 80% | mixed |
| `rank(fnd6_newqv1300_cshprq / close)` | TOP1000 | 0.33 | 0.14 | 14.7% | 80% | all-weather |
| `rank(fnd6_newqv1300_cshprq)` | TOP1000 | 0.26 | 0.09 | 13.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshprq)` | TOP500 | 0.20 | 0.07 | 23.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshprq)` | TOP3000 | 0.12 | 0.03 | 8.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cshfdq: 1.000 (strongly positively correlated)
- fnd6_mfmq_cshprq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.997 (strongly positively correlated)
- fnd6_mfma1_csho: 0.973 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
