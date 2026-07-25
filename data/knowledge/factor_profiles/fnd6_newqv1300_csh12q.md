---
field: fnd6_newqv1300_csh12q
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.22
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1361
ann_vol: 0.0652
hit_rate: 0.4939
rolling_sharpe_min: -0.844
rolling_sharpe_max: 2.165
negated_best_sharpe: 0.07
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.38
---
# fnd6_newqv1300_csh12q (fundamental6)

*Common Shares Used to Calculate Earnings Per Share - 12 Months Moving*

## Signal Profile
- `rank(fnd6_newqv1300_csh12q)`: S=0.24, F=0.09, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_csh12q / close)`: S=0.45, F=0.22, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_csh12q, 5))`: S=0.15, F=0.04, T=37.1%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_csh12q)`: S=-0.24, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_csh12q, 5))`: S=0.07, F=0.01, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_csh12q, 63)`: S=0.31, F=0.14, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_csh12q, 10)`: S=0.06, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_csh12q, 22))`: S=-0.64, F=-0.32, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_csh12q)`: S=-0.16, F=-0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_csh12q / close)`: S=0.00, F=0.00, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+2.7%
  - 2020: S=0.48 (weak), ret=+3.8%
  - 2021: S=-0.60 (negative), ret=-4.8%
  - 2022: S=1.90 (strong), ret=+11.5%
  - 2023: S=0.28 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 13.61% over 499 days (recovered)
- Annualized: return +2.9%, volatility 6.5% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.46, excess kurtosis +1.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.17, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +4.85%; worst month: -2.85%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.61
- Sideways: S=-0.52
- Bear: S=0.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_csh12q, 5))` S=0.07, F=0.01, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_csh12q)`: S=-0.16, F=-0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_csh12q / close)`: S=0.00, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_csh12q, 5))`: S=0.07, F=0.01, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_csh12q / close)` | TOP500 | 0.45 | 0.22 | 13.6% | 80% | mixed |
| `rank(fnd6_newqv1300_csh12q / close)` | TOP1000 | 0.34 | 0.14 | 13.7% | 80% | all-weather |
| `rank(fnd6_newqv1300_csh12q / close)` | TOP200 | 0.30 | 0.13 | 21.0% | 80% | mixed |
| `rank(fnd6_newqv1300_csh12q)` | TOP1000 | 0.24 | 0.09 | 14.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_csh12q)` | TOP500 | 0.15 | 0.05 | 25.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_csh12q)` | TOP3000 | 0.17 | 0.04 | 9.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_csh12q, 5))` | TOP200 | 0.14 | 0.04 | 30.3% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_csh12q, 5))` | TOP500 | 0.12 | 0.03 | 16.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_cshprq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_cshprq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_cshfdq: 0.997 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.993 (strongly positively correlated)
- fnd6_cshpri: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
