---
field: fnd6_newqv1300_aqpl1q
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.42
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.1551
ann_vol: 0.0545
hit_rate: 0.5215
rolling_sharpe_min: -1.911
rolling_sharpe_max: 2.049
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.12
---
# fnd6_newqv1300_aqpl1q (fundamental6)

*Assets Level 1 (Quoted Prices)*

## Signal Profile
- `rank(fnd6_newqv1300_aqpl1q)`: S=0.45, F=0.20, T=8.3%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_aqpl1q / close)`: S=0.41, F=0.17, T=8.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_aqpl1q, 5))`: S=0.32, F=0.10, T=60.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_aqpl1q)`: S=-0.45, F=-0.20, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aqpl1q, 5))`: S=0.30, F=0.08, T=49.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_aqpl1q, 22)`: S=0.19, F=0.05, T=40.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aqpl1q, 10)`: S=0.42, F=0.22, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aqpl1q, 22))`: S=-0.25, F=-0.07, T=23.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aqpl1q)`: S=-0.26, F=-0.08, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aqpl1q / close)`: S=-0.19, F=-0.05, T=6.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+1.6%
  - 2020: S=-0.74 (negative), ret=-3.9%
  - 2021: S=0.67 (moderate), ret=+5.1%
  - 2022: S=1.18 (moderate), ret=+5.9%
  - 2023: S=0.80 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 15.51% over 656 days (recovered)
- Annualized: return +2.5%, volatility 5.5% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.26, excess kurtosis +2.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 2.05, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.13%; worst month: -4.86%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.95
- Sideways: S=1.25
- Bear: S=-1.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_aqpl1q, 5))` S=0.30, F=0.08, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aqpl1q)`: S=-0.26, F=-0.08, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aqpl1q / close)`: S=-0.19, F=-0.05, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aqpl1q, 5))`: S=0.30, F=0.08, T=49.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_aqpl1q)` | TOP1000 | 0.46 | 0.20 | 15.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_aqpl1q / close)` | TOP1000 | 0.41 | 0.17 | 5.9% | 100% | weak |
| `rank(fnd6_newqv1300_aqpl1q / close)` | TOP500 | 0.35 | 0.14 | 11.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_aqpl1q / close)` | TOP200 | 0.27 | 0.12 | 17.6% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aqpl1q, 5))` | TOP500 | 0.31 | 0.10 | 37.1% | 60% | mixed |
| `rank(fnd6_newqv1300_aqpl1q)` | TOP500 | 0.26 | 0.09 | 15.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_aqpl1q)` | TOP3000 | 0.27 | 0.08 | 14.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_aqpl1q)` | TOP200 | 0.17 | 0.06 | 24.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aqpl1q, 5))` | TOP200 | 0.21 | 0.06 | 64.0% | 80% | bear-only |
| `rank(fnd6_newqv1300_aqpl1q / close)` | TOP3000 | 0.20 | 0.05 | 11.2% | 60% | bear-only |
| `rank(ts_delta(fnd6_newqv1300_aqpl1q, 5))` | TOP1000 | 0.13 | 0.03 | 45.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tfva: 0.615 (moderately positively correlated)
- news_cap: 0.553 (moderately positively correlated)
- cash: 0.536 (moderately positively correlated)
- fnd6_newqv1300_xrdq: 0.523 (moderately positively correlated)
- fnd6_newqv1300_xsgaq: 0.518 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
