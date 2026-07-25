---
field: fnd6_mfmq_piq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.39
best_fitness: 0.12
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3935
ann_vol: 0.1135
hit_rate: 0.5085
rolling_sharpe_min: -4.417
rolling_sharpe_max: 2.56
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: 0.08
---
# fnd6_mfmq_piq (fundamental6)

*Pretax Income*

## Signal Profile
- `rank(fnd6_mfmq_piq)`: S=0.22, F=0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_mfmq_piq / close)`: S=0.23, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfmq_piq, 5))`: S=-0.02, F=0.00, T=36.9%, INFERIOR (TOP500)
- `-rank(fnd6_mfmq_piq)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_piq, 5))`: S=0.47, F=0.12, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfmq_piq, 22)`: S=0.39, F=0.12, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfmq_piq, 10)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfmq_piq, 22))`: S=0.05, F=0.01, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_piq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_piq / close)`: S=-0.23, F=-0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.3%
  - 2020: S=-3.48 (negative), ret=-25.9%
  - 2021: S=1.16 (moderate), ret=+14.3%
  - 2022: S=1.56 (strong), ret=+25.2%
  - 2023: S=-0.21 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 39.35% over 891 days (recovered)
- Annualized: return +2.6%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.17, excess kurtosis +1.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.42, max 2.56, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.50%; worst month: -9.47%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=0.80
- Bear: S=-3.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfmq_piq, 5))` S=0.47, F=0.12, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfmq_piq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_piq / close)`: S=-0.23, F=-0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_piq, 5))`: S=0.47, F=0.12, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfmq_piq / close)` | TOP3000 | 0.23 | 0.11 | 39.4% | 60% | bull-only |
| `rank(fnd6_mfmq_piq)` | TOP3000 | 0.21 | 0.10 | 42.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income: 1.000 (strongly positively correlated)
- fnd6_newqv1300_piq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibq: 0.999 (strongly positively correlated)
- income_beforeextra: 0.999 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
