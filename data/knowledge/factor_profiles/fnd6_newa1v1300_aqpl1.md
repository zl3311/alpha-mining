---
field: fnd6_newa1v1300_aqpl1
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.9
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1277
ann_vol: 0.0684
hit_rate: 0.5101
rolling_sharpe_min: -1.737
rolling_sharpe_max: 2.042
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.59
n_negated_sims: 10
direction_gap: 0.45
---
# fnd6_newa1v1300_aqpl1 (fundamental6)

*Assets Level 1 (Quoted Prices)*

## Signal Profile
- `rank(fnd6_newa1v1300_aqpl1)`: S=0.40, F=0.20, T=2.8%, INFERIOR (TOP500)
- `rank(fnd6_newa1v1300_aqpl1 / close)`: S=0.53, F=0.29, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_aqpl1, 5))`: S=-0.02, F=0.00, T=26.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_aqpl1)`: S=-0.24, F=-0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aqpl1, 5))`: S=0.90, F=0.59, T=36.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_aqpl1, 63)`: S=0.45, F=0.31, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aqpl1, 10)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aqpl1, 22))`: S=0.26, F=0.10, T=20.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aqpl1)`: S=-0.24, F=-0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aqpl1 / close)`: S=-0.14, F=-0.03, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+2.5%
  - 2020: S=-0.85 (negative), ret=-4.9%
  - 2021: S=0.75 (moderate), ret=+7.0%
  - 2022: S=0.49 (weak), ret=+3.7%
  - 2023: S=1.71 (strong), ret=+9.4%

## Risk & Drawdown
- Max drawdown: 12.77% over 644 days (recovered)
- Annualized: return +3.6%, volatility 6.8% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.17, excess kurtosis +2.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.74, max 2.04, latest 1.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +6.93%; worst month: -4.56%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.43
- Sideways: S=0.97
- Bear: S=-0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_aqpl1, 5))` S=0.90, F=0.59, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aqpl1)`: S=-0.24, F=-0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aqpl1 / close)`: S=-0.14, F=-0.03, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aqpl1, 5))`: S=0.90, F=0.59, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_aqpl1 / close)` | TOP500 | 0.53 | 0.29 | 12.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1)` | TOP500 | 0.40 | 0.20 | 20.6% | 60% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1)` | TOP3000 | 0.36 | 0.13 | 15.5% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1 / close)` | TOP200 | 0.26 | 0.11 | 23.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1 / close)` | TOP3000 | 0.34 | 0.11 | 7.5% | 40% | weak |
| `rank(fnd6_newa1v1300_aqpl1)` | TOP1000 | 0.24 | 0.08 | 21.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1)` | TOP200 | 0.16 | 0.05 | 32.3% | 60% | bull-only |
| `rank(fnd6_newa1v1300_aqpl1 / close)` | TOP1000 | 0.14 | 0.03 | 12.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_stkco: 0.639 (moderately positively correlated)
- fnd6_ch: 0.615 (moderately positively correlated)
- fnd6_newa1v1300_che: 0.597 (moderately positively correlated)
- fnd6_loxdr: 0.590 (moderately positively correlated)
- fnd6_itcb: 0.558 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
