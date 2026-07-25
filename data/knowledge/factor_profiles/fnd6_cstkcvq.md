---
field: fnd6_cstkcvq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.93
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1012
ann_vol: 0.0701
hit_rate: 0.4874
rolling_sharpe_min: -1.993
rolling_sharpe_max: 2.015
negated_best_sharpe: 0.93
negated_best_template: rank_neg_delta
negated_best_fitness: 0.61
n_negated_sims: 10
direction_gap: 0.46
---
# fnd6_cstkcvq (fundamental6)

*Common Stock-Carrying Value*

## Signal Profile
- `rank(fnd6_cstkcvq)`: S=0.35, F=0.17, T=3.7%, INFERIOR (TOP3000)
- `rank(fnd6_cstkcvq / close)`: S=0.47, F=0.24, T=5.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_cstkcvq, 5))`: S=-0.38, F=-0.18, T=28.7%, INFERIOR (TOP200)
- `-rank(fnd6_cstkcvq)`: S=-0.33, F=-0.16, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cstkcvq, 5))`: S=0.93, F=0.61, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cstkcvq, 22)`: S=0.18, F=0.12, T=14.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cstkcvq, 10)`: S=-0.14, F=-0.04, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cstkcvq, 22))`: S=-0.39, F=-0.19, T=20.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcvq)`: S=-0.33, F=-0.16, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcvq / close)`: S=-0.47, F=-0.24, T=5.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.49 (negative), ret=-1.8%
  - 2020: S=-0.45 (negative), ret=-3.4%
  - 2021: S=1.69 (strong), ret=+13.6%
  - 2022: S=1.20 (moderate), ret=+10.9%
  - 2023: S=-0.89 (negative), ret=-3.8%

## Risk & Drawdown
- Max drawdown: 10.12% over 726 days (recovered)
- Annualized: return +3.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.34, excess kurtosis +3.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.99, max 2.02, latest -0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.04%; worst month: -3.17%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.19
- Sideways: S=-0.41
- Bear: S=-0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cstkcvq, 5))` S=0.93, F=0.61, INFERIOR
Direction gap: +0.46 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cstkcvq)`: S=-0.33, F=-0.16, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcvq / close)`: S=-0.47, F=-0.24, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cstkcvq, 5))`: S=0.93, F=0.61, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cstkcvq / close)` | TOP1000 | 0.45 | 0.24 | 10.1% | 40% | bull-only |
| `rank(fnd6_cstkcvq / close)` | TOP3000 | 0.46 | 0.22 | 10.1% | 40% | bull-only |
| `rank(fnd6_cstkcvq / close)` | TOP500 | 0.38 | 0.20 | 12.4% | 60% | bull-only |
| `rank(fnd6_cstkcvq)` | TOP3000 | 0.34 | 0.17 | 21.3% | 40% | bull-only |
| `rank(fnd6_cstkcvq)` | TOP1000 | 0.32 | 0.16 | 17.5% | 40% | bull-only |
| `rank(fnd6_cstkcvq)` | TOP500 | 0.29 | 0.14 | 16.3% | 60% | bull-only |
| `rank(fnd6_cstkcvq / close)` | TOP200 | 0.15 | 0.06 | 22.7% | 40% | bull-only |
| `rank(fnd6_cstkcvq)` | TOP200 | 0.06 | 0.02 | 23.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cstkcv: 0.849 (strongly positively correlated)
- fnd6_newqv1300_cstkq: 0.835 (strongly positively correlated)
- fnd6_newa1v1300_cstk: 0.828 (strongly positively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: 0.798 (strongly positively correlated)
- fnd6_loxdr: 0.791 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
