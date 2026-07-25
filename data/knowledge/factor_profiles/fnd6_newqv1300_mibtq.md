---
field: fnd6_newqv1300_mibtq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.5
best_fitness: 0.24
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0914
ann_vol: 0.056
hit_rate: 0.502
rolling_sharpe_min: -0.899
rolling_sharpe_max: 2.429
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_newqv1300_mibtq (fundamental6)

*Noncontrolling Interests - Total - Balance Sheet - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_mibtq)`: S=0.40, F=0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_mibtq / close)`: S=0.50, F=0.24, T=2.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_mibtq, 5))`: S=-0.10, F=-0.02, T=38.5%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_mibtq)`: S=-0.38, F=-0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_mibtq, 5))`: S=0.42, F=0.12, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_mibtq, 63)`: S=0.04, F=0.00, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_mibtq, 10)`: S=-0.20, F=-0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_mibtq, 22))`: S=-0.05, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibtq)`: S=-0.40, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibtq / close)`: S=-0.49, F=-0.21, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.49, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=-0.04 (negative), ret=-0.2%
  - 2021: S=0.37 (weak), ret=+2.9%
  - 2022: S=2.14 (strong), ret=+13.2%
  - 2023: S=-0.61 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 9.14% over 250 days (recovered)
- Annualized: return +2.8%, volatility 5.6% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.12, excess kurtosis +1.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.43, latest -0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.92%; worst month: -4.90%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=0.22
- Bear: S=-1.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_mibtq, 5))` S=0.42, F=0.12, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_mibtq)`: S=-0.40, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibtq / close)`: S=-0.49, F=-0.21, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_mibtq, 5))`: S=0.42, F=0.12, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_mibtq / close)` | TOP1000 | 0.49 | 0.24 | 9.1% | 40% | bull-only |
| `rank(fnd6_newqv1300_mibtq / close)` | TOP3000 | 0.49 | 0.21 | 10.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibtq)` | TOP3000 | 0.40 | 0.16 | 13.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibtq)` | TOP1000 | 0.37 | 0.16 | 9.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibtq)` | TOP200 | 0.29 | 0.14 | 22.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibtq / close)` | TOP200 | 0.24 | 0.10 | 22.6% | 40% | bull-only |
| `rank(fnd6_newqv1300_mibtq / close)` | TOP500 | 0.21 | 0.07 | 11.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibtq)` | TOP500 | 0.16 | 0.05 | 12.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_mibtq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_mibnq: 0.986 (strongly positively correlated)
- fnd6_mibt: 0.963 (strongly positively correlated)
- fnd6_mibn: 0.945 (strongly positively correlated)
- est_ebitda: 0.763 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
