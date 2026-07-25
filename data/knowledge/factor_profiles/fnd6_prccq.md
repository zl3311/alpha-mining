---
field: fnd6_prccq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.41
best_fitness: 0.26
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1801
ann_vol: 0.1278
hit_rate: 0.4947
rolling_sharpe_min: -0.702
rolling_sharpe_max: 2.08
negated_best_sharpe: 0.15
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_prccq (fundamental6)

*Price Close - Quarter*

## Signal Profile
- `rank(fnd6_prccq)`: S=0.18, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_prccq / close)`: S=0.41, F=0.26, T=11.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_prccq, 5))`: S=0.40, F=0.11, T=36.2%, INFERIOR (TOP500)
- `-rank(fnd6_prccq)`: S=-0.04, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prccq, 5))`: S=0.08, F=0.01, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_prccq, 63)`: S=0.15, F=0.05, T=9.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prccq, 10)`: S=0.26, F=0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prccq, 22))`: S=-0.15, F=-0.04, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prccq)`: S=0.15, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prccq / close)`: S=-0.04, F=-0.01, T=12.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+6.1%
  - 2020: S=1.05 (moderate), ret=+11.1%
  - 2021: S=0.44 (weak), ret=+6.5%
  - 2022: S=-0.21 (negative), ret=-4.0%
  - 2023: S=0.65 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 18.01% over 911 days (not yet recovered, ongoing at window end)
- Annualized: return +5.0%, volatility 12.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.65, excess kurtosis +4.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.08, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.65%; worst month: -5.54%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.32
- Sideways: S=0.35
- Bear: S=0.56

## Negated Direction
Best negated: `rank(-1 * fnd6_prccq)` S=0.15, F=0.05, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_prccq)`: S=0.15, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prccq / close)`: S=-0.04, F=-0.01, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prccq, 5))`: S=0.08, F=0.01, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prccq / close)` | TOP1000 | 0.39 | 0.26 | 18.0% | 80% | mixed |
| `rank(fnd6_prccq / close)` | TOP3000 | 0.30 | 0.18 | 17.4% | 80% | mixed |
| `rank(fnd6_prccq / close)` | TOP500 | 0.24 | 0.14 | 20.4% | 80% | mixed |
| `rank(ts_delta(fnd6_prccq, 5))` | TOP500 | 0.40 | 0.11 | 13.7% | 80% | bull-only |
| `rank(fnd6_prccq)` | TOP3000 | 0.18 | 0.08 | 50.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_prccq, 5))` | TOP1000 | 0.20 | 0.04 | 12.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_prchq: 0.776 (strongly positively correlated)
- fnd6_prclq: 0.682 (moderately positively correlated)
- fnd6_prcc: 0.652 (moderately positively correlated)
- fnd6_prch: 0.637 (moderately positively correlated)
- rp_ess_price: -0.513 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
