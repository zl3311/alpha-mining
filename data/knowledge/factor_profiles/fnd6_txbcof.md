---
field: fnd6_txbcof
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 4.18
best_fitness: 9.05
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2816
ann_vol: 0.0954
hit_rate: 0.4559
rolling_sharpe_min: -3.635
rolling_sharpe_max: 2.107
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -3.97
---
# fnd6_txbcof (fundamental6)

*Excess Tax Benefit of Stock Options - Cash Flow Financing*

## Signal Profile
- `rank(fnd6_txbcof)`: S=0.21, F=0.08, T=3.1%, INFERIOR (TOP500)
- `rank(fnd6_txbcof / close)`: S=0.20, F=0.08, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_txbcof, 5))`: S=0.29, F=0.14, T=3.1%, INFERIOR (TOP500)
- `-rank(fnd6_txbcof)`: S=-0.07, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txbcof, 5))`: S=0.06, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txbcof, 63)`: S=4.18, F=9.05, T=10.2%, SPECTACULAR (TOP3000)
- `ts_mean(fnd6_txbcof, 10)`: S=-0.60, F=-0.55, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txbcof, 22))`: S=-0.19, F=-0.07, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbcof)`: S=0.21, F=0.09, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbcof / close)`: S=0.21, F=0.09, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 30F/2P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+6.8%
  - 2020: S=-2.15 (negative), ret=-12.8%
  - 2021: S=0.89 (moderate), ret=+12.5%
  - 2022: S=0.93 (moderate), ret=+8.8%
  - 2023: S=-0.43 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 28.16% over 706 days (recovered)
- Annualized: return +2.7%, volatility 9.5% (fraction of booksize)
- Hit rate: 45.6% positive days
- Tail shape: skew +0.25, excess kurtosis +7.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.63, max 2.11, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.36%; worst month: -7.37%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.07
- Sideways: S=0.47
- Bear: S=-2.35

## Negated Direction
Best negated: `rank(-1 * fnd6_txbcof)` S=0.21, F=0.09, INFERIOR
Direction gap: -3.97 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txbcof)`: S=0.21, F=0.09, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbcof / close)`: S=0.21, F=0.09, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txbcof, 5))`: S=0.06, F=0.01, T=3.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txbcof, 5))` | TOP500 | 0.28 | 0.14 | 28.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_txbcof, 5))` | TOP3000 | 0.23 | 0.10 | 34.9% | 40% | bull-only |
| `rank(fnd6_txbcof)` | TOP500 | 0.20 | 0.08 | 30.0% | 60% | bull-only |
| `rank(fnd6_txbcof / close)` | TOP500 | 0.19 | 0.08 | 31.0% | 60% | bull-only |
| `rank(fnd6_txbcof / close)` | TOP200 | 0.12 | 0.05 | 33.1% | 40% | bull-only |
| `rank(fnd6_txbcof)` | TOP200 | 0.12 | 0.05 | 33.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_txbcof, 5))` | TOP200 | 0.12 | 0.04 | 25.9% | 40% | bull-only |
| `rank(fnd6_txbcof)` | TOP1000 | 0.06 | 0.02 | 27.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_esopnr: 0.859 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.847 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.847 (strongly positively correlated)
- min_total_assets_guidance: 0.847 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.847 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
