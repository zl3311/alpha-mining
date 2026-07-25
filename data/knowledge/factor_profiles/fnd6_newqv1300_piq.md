---
field: fnd6_newqv1300_piq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.44
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3949
ann_vol: 0.1135
hit_rate: 0.5109
rolling_sharpe_min: -4.426
rolling_sharpe_max: 2.561
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: 0.04
---
# fnd6_newqv1300_piq (fundamental6)

*Pretax Income*

## Signal Profile
- `rank(fnd6_newqv1300_piq)`: S=0.22, F=0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_piq / close)`: S=0.24, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_piq, 5))`: S=-0.03, F=0.00, T=36.8%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_piq)`: S=-0.06, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_piq, 5))`: S=0.48, F=0.12, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_piq, 22)`: S=0.44, F=0.15, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_piq, 10)`: S=0.11, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_piq, 22))`: S=0.09, F=0.01, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_piq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_piq / close)`: S=-0.24, F=-0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.24, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.2%
  - 2020: S=-3.50 (negative), ret=-25.9%
  - 2021: S=1.16 (moderate), ret=+14.3%
  - 2022: S=1.58 (strong), ret=+25.6%
  - 2023: S=-0.18 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 39.49% over 891 days (recovered)
- Annualized: return +2.7%, volatility 11.3% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew -0.17, excess kurtosis +1.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.43, max 2.56, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.54%; worst month: -9.53%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.75
- Sideways: S=0.81
- Bear: S=-3.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_piq, 5))` S=0.48, F=0.12, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_piq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_piq / close)`: S=-0.24, F=-0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_piq, 5))`: S=0.48, F=0.12, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_piq / close)` | TOP3000 | 0.24 | 0.11 | 39.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_piq)` | TOP3000 | 0.21 | 0.10 | 42.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_piq)` | TOP1000 | 0.06 | 0.02 | 44.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income: 1.000 (strongly positively correlated)
- fnd6_mfmq_piq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibq: 0.999 (strongly positively correlated)
- income_beforeextra: 0.999 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
