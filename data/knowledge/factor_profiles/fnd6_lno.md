---
field: fnd6_lno
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.74
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1857
ann_vol: 0.0758
hit_rate: 0.481
rolling_sharpe_min: -1.862
rolling_sharpe_max: 2.287
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.55
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_lno (fundamental6)

*Liabilities Netting & Other Adjustments*

## Signal Profile
- `rank(fnd6_lno)`: S=-0.33, F=-0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_lno / close)`: S=-0.33, F=-0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_lno, 5))`: S=0.59, F=0.36, T=8.8%, INFERIOR (TOP500)
- `-rank(fnd6_lno)`: S=0.46, F=0.21, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lno, 5))`: S=0.74, F=0.55, T=7.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_lno, 22)`: S=0.58, F=0.32, T=5.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lno, 10)`: S=-0.30, F=-0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lno, 22))`: S=-0.05, F=-0.01, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lno)`: S=0.49, F=0.36, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lno / close)`: S=0.47, F=0.33, T=4.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+5.1%
  - 2020: S=0.38 (weak), ret=+2.5%
  - 2021: S=0.56 (moderate), ret=+5.7%
  - 2022: S=1.06 (moderate), ret=+7.7%
  - 2023: S=0.12 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 18.57% over 443 days (recovered)
- Annualized: return +4.4%, volatility 7.6% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.63, excess kurtosis +6.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.86, max 2.29, latest 0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +9.56%; worst month: -8.08%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.96
- Sideways: S=0.72
- Bear: S=-1.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_lno, 5))` S=0.74, F=0.55, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_lno)`: S=0.49, F=0.36, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lno / close)`: S=0.47, F=0.33, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lno, 5))`: S=0.74, F=0.55, T=7.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_lno, 5))` | TOP500 | 0.58 | 0.36 | 18.6% | 100% | bull-only |
| `rank(ts_delta(fnd6_lno, 5))` | TOP3000 | 0.15 | 0.08 | 39.3% | 80% | mixed |
| `rank(ts_delta(fnd6_lno, 5))` | TOP1000 | 0.17 | 0.07 | 15.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_lno, 5))` | TOP200 | 0.11 | 0.04 | 22.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dvpa: 0.526 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.458 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.458 (moderately positively correlated)
- min_total_assets_guidance: 0.458 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.458 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
