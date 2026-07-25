---
field: fnd6_newqv1300_cstkq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.83
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1563
ann_vol: 0.0746
hit_rate: 0.4955
rolling_sharpe_min: -2.49
rolling_sharpe_max: 2.166
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.4
---
# fnd6_newqv1300_cstkq (fundamental6)

*Common/Ordinary Stock (Capital)*

## Signal Profile
- `rank(fnd6_newqv1300_cstkq)`: S=0.24, F=0.10, T=4.4%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_cstkq / close)`: S=0.33, F=0.15, T=4.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_cstkq, 5))`: S=0.01, F=0.00, T=37.7%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cstkq)`: S=-0.12, F=-0.03, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cstkq, 5))`: S=0.83, F=0.43, T=39.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cstkq, 63)`: S=0.43, F=0.23, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cstkq, 10)`: S=0.17, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cstkq, 22))`: S=-0.61, F=-0.30, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cstkq)`: S=-0.12, F=-0.03, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cstkq / close)`: S=-0.25, F=-0.09, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.31, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+2.5%
  - 2020: S=-0.58 (negative), ret=-4.3%
  - 2021: S=1.36 (moderate), ret=+11.8%
  - 2022: S=1.52 (strong), ret=+14.6%
  - 2023: S=-2.40 (negative), ret=-13.1%

## Risk & Drawdown
- Max drawdown: 15.63% over 415 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 7.5% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.10, excess kurtosis +1.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.49, max 2.17, latest -2.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.37%; worst month: -3.29%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.03
- Sideways: S=-0.06
- Bear: S=-1.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cstkq, 5))` S=0.83, F=0.43, INFERIOR
Direction gap: +0.40 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cstkq)`: S=-0.12, F=-0.03, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cstkq / close)`: S=-0.25, F=-0.09, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cstkq, 5))`: S=0.83, F=0.43, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cstkq / close)` | TOP500 | 0.31 | 0.15 | 15.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_cstkq)` | TOP500 | 0.23 | 0.10 | 17.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_cstkq / close)` | TOP1000 | 0.23 | 0.09 | 11.2% | 40% | bull-only |
| `rank(fnd6_newqv1300_cstkq / close)` | TOP3000 | 0.25 | 0.09 | 11.0% | 40% | bull-only |
| `rank(fnd6_newqv1300_cstkq)` | TOP3000 | 0.21 | 0.08 | 21.2% | 40% | bull-only |
| `rank(fnd6_newqv1300_cstkq / close)` | TOP200 | 0.15 | 0.05 | 23.7% | 40% | bull-only |
| `rank(fnd6_newqv1300_cstkq)` | TOP1000 | 0.11 | 0.03 | 18.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_cstk: 0.973 (strongly positively correlated)
- fnd6_cstkcvq: 0.835 (strongly positively correlated)
- anl4_af_div_value: 0.803 (strongly positively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: 0.800 (strongly positively correlated)
- cashflow_dividends: 0.775 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
