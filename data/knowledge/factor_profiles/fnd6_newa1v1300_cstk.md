---
field: fnd6_newa1v1300_cstk
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.51
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1469
ann_vol: 0.0736
hit_rate: 0.4874
rolling_sharpe_min: -2.494
rolling_sharpe_max: 2.17
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.13
---
# fnd6_newa1v1300_cstk (fundamental6)

*Common/Ordinary Stock (Capital)*

## Signal Profile
- `rank(fnd6_newa1v1300_cstk)`: S=0.21, F=0.08, T=1.9%, INFERIOR (TOP500)
- `rank(fnd6_newa1v1300_cstk / close)`: S=0.32, F=0.14, T=2.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_cstk, 5))`: S=-0.19, F=-0.07, T=33.3%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_cstk)`: S=-0.11, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cstk, 5))`: S=0.64, F=0.32, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_cstk, 63)`: S=0.51, F=0.45, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_cstk, 10)`: S=0.05, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_cstk, 22))`: S=-1.14, F=-1.03, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cstk)`: S=-0.18, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cstk / close)`: S=-0.23, F=-0.07, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/24P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.1%
  - 2020: S=-0.73 (negative), ret=-4.8%
  - 2021: S=1.39 (moderate), ret=+12.7%
  - 2022: S=1.54 (strong), ret=+14.6%
  - 2023: S=-2.38 (negative), ret=-12.7%

## Risk & Drawdown
- Max drawdown: 14.69% over 415 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 7.4% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.12, excess kurtosis +1.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.49, max 2.17, latest -2.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.84%; worst month: -3.24%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.16
- Sideways: S=-0.21
- Bear: S=-1.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_cstk, 5))` S=0.64, F=0.32, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_cstk)`: S=-0.18, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cstk / close)`: S=-0.23, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cstk, 5))`: S=0.64, F=0.32, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_cstk / close)` | TOP500 | 0.30 | 0.14 | 14.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cstk / close)` | TOP1000 | 0.21 | 0.08 | 10.5% | 40% | bull-only |
| `rank(fnd6_newa1v1300_cstk)` | TOP500 | 0.20 | 0.08 | 18.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cstk / close)` | TOP3000 | 0.22 | 0.07 | 11.7% | 40% | bull-only |
| `rank(fnd6_newa1v1300_cstk)` | TOP3000 | 0.17 | 0.06 | 22.2% | 40% | bull-only |
| `rank(fnd6_newa1v1300_cstk / close)` | TOP200 | 0.13 | 0.05 | 25.6% | 40% | bull-only |
| `rank(fnd6_newa1v1300_cstk)` | TOP1000 | 0.10 | 0.03 | 18.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cstkq: 0.973 (strongly positively correlated)
- fnd6_cstkcvq: 0.828 (strongly positively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: 0.807 (strongly positively correlated)
- anl4_af_div_value: 0.806 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.792 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
