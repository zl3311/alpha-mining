---
field: fnd6_donr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.7495
ann_vol: 0.2517
hit_rate: 0.5142
rolling_sharpe_min: -1.154
rolling_sharpe_max: 3.041
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: 0.42
---
# fnd6_donr (fundamental6)

*Nonrecurring Disc Operations*

## Signal Profile
- `rank(fnd6_donr)`: S=0.14, F=0.07, T=3.5%, INFERIOR (TOP200)
- `rank(fnd6_donr / close)`: S=0.14, F=0.07, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_donr, 5))`: S=0.12, F=0.04, T=10.4%, INFERIOR (TOP500)
- `-rank(fnd6_donr)`: S=0.35, F=0.18, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_donr, 5))`: S=0.56, F=0.42, T=13.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_donr, 22)`: S=0.14, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_donr, 10)`: S=-0.01, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_donr, 22))`: S=-0.73, F=-0.77, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_donr)`: S=0.35, F=0.18, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_donr / close)`: S=0.35, F=0.18, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.32 (moderate), ret=+21.8%
  - 2020: S=1.16 (moderate), ret=+22.4%
  - 2021: S=-0.72 (negative), ret=-33.5%
  - 2022: S=0.97 (moderate), ret=+11.2%
  - 2023: S=-0.41 (negative), ret=-4.5%

## Risk & Drawdown
- Max drawdown: 74.95% over 1281 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 25.2% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew -1.03, excess kurtosis +53.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 3.04, latest -0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +17.41%; worst month: -26.86%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.29
- Sideways: S=0.95
- Bear: S=-0.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_donr, 5))` S=0.56, F=0.42, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_donr)`: S=0.35, F=0.18, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_donr / close)`: S=0.35, F=0.18, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_donr, 5))`: S=0.56, F=0.42, T=13.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_donr)` | TOP200 | 0.14 | 0.07 | 75.0% | 60% | weak |
| `rank(fnd6_donr / close)` | TOP200 | 0.14 | 0.07 | 75.1% | 60% | weak |
| `rank(ts_delta(fnd6_donr, 5))` | TOP500 | 0.11 | 0.04 | 18.9% | 60% | weak |

## Correlation Notes
Top correlates:
- news_short_interest: -0.471 (moderately negatively correlated)
- fnd6_newqv1300_cimiiq: 0.258 (weakly positively correlated)
- fnd6_newa2v1300_rdipd: -0.243 (weakly negatively correlated)
- fnd6_newqv1300_miiq: 0.240 (weakly positively correlated)
- fnd6_newa2v1300_rdipeps: -0.234 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
