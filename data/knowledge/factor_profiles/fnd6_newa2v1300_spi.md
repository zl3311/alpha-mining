---
field: fnd6_newa2v1300_spi
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.81
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1491
ann_vol: 0.0784
hit_rate: 0.5174
rolling_sharpe_min: -1.553
rolling_sharpe_max: 2.458
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: 0.43
---
# fnd6_newa2v1300_spi (fundamental6)

*Special Items*

## Signal Profile
- `rank(fnd6_newa2v1300_spi)`: S=0.28, F=0.12, T=2.5%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_spi / close)`: S=0.38, F=0.19, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_spi, 5))`: S=-0.28, F=-0.09, T=34.4%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_spi)`: S=0.35, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_spi, 5))`: S=0.81, F=0.50, T=33.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_spi, 63)`: S=0.22, F=0.08, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_spi, 10)`: S=-0.10, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_spi, 22))`: S=-0.45, F=-0.22, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_spi)`: S=0.26, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_spi / close)`: S=0.37, F=0.15, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.05 (negative), ret=-5.0%
  - 2020: S=2.13 (strong), ret=+17.8%
  - 2021: S=0.23 (weak), ret=+2.3%
  - 2022: S=-1.01 (negative), ret=-7.8%
  - 2023: S=1.23 (moderate), ret=+8.0%

## Risk & Drawdown
- Max drawdown: 14.91% over 760 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 7.8% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.10, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 2.46, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.17%; worst month: -6.35%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.10
- Sideways: S=0.23
- Bear: S=2.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_spi, 5))` S=0.81, F=0.50, INFERIOR
Direction gap: +0.43 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_spi)`: S=0.26, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_spi / close)`: S=0.37, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_spi, 5))`: S=0.81, F=0.50, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_spi / close)` | TOP200 | 0.40 | 0.19 | 14.9% | 60% | bear-only |
| `rank(fnd6_newa2v1300_spi)` | TOP200 | 0.29 | 0.12 | 21.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_loxdr: -0.561 (moderately negatively correlated)
- est_cashflow_fin: 0.534 (moderately positively correlated)
- fnd6_ch: -0.525 (moderately negatively correlated)
- fn_proceeds_from_stock_options_exercised_a: -0.522 (moderately negatively correlated)
- fnd6_newa2v1300_stkco: -0.521 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
