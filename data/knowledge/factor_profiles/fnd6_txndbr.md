---
field: fnd6_txndbr
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.67
best_fitness: 0.74
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.3862
ann_vol: 0.23
hit_rate: 0.4648
rolling_sharpe_min: -2.746
rolling_sharpe_max: 2.475
negated_best_sharpe: 0.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_txndbr (fundamental6)

*Deferred Tax Residual*

## Signal Profile
- `rank(fnd6_txndbr)`: S=0.67, F=0.74, T=3.1%, INFERIOR (TOP500)
- `rank(fnd6_txndbr / close)`: S=0.67, F=0.74, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_txndbr, 5))`: S=0.66, F=0.41, T=3.8%, INFERIOR (TOP500)
- `-rank(fnd6_txndbr)`: S=-0.39, F=-0.36, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndbr, 5))`: S=0.18, F=0.06, T=3.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txndbr, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_txndbr, 10)`: S=0.43, F=0.43, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txndbr, 22))`: S=0.33, F=0.20, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbr)`: S=-0.31, F=-0.25, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbr / close)`: S=-0.31, F=-0.25, T=4.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/18P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.67, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.58 (strong), ret=+45.7%
  - 2020: S=-1.18 (negative), ret=-6.6%
  - 2021: S=-0.34 (negative), ret=-11.6%
  - 2022: S=2.33 (strong), ret=+50.9%
  - 2023: S=-0.33 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 38.62% over 1089 days (recovered)
- Annualized: return +15.5%, volatility 23.0% (fraction of booksize)
- Hit rate: 46.5% positive days
- Tail shape: skew +1.73, excess kurtosis +21.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.75, max 2.48, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +18.33%; worst month: -8.26%
Positive months: 57%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.56
- Sideways: S=1.45
- Bear: S=-0.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txndbr, 5))` S=0.18, F=0.06, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txndbr)`: S=-0.31, F=-0.25, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbr / close)`: S=-0.31, F=-0.25, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndbr, 5))`: S=0.18, F=0.06, T=3.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txndbr)` | TOP500 | 0.67 | 0.74 | 38.6% | 40% | mixed |
| `rank(fnd6_txndbr / close)` | TOP500 | 0.67 | 0.74 | 38.6% | 40% | mixed |
| `rank(ts_delta(fnd6_txndbr, 5))` | TOP500 | 0.62 | 0.41 | 21.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_txndbr, 5))` | TOP3000 | 0.62 | 0.38 | 7.3% | 60% | mixed |
| `rank(fnd6_txndbr / close)` | TOP1000 | 0.39 | 0.36 | 35.8% | 80% | bull-only |
| `rank(fnd6_txndbr)` | TOP1000 | 0.39 | 0.36 | 35.8% | 80% | bull-only |
| `rank(fnd6_txndbr / close)` | TOP200 | 0.49 | 0.36 | 19.8% | 60% | bull-only |
| `rank(fnd6_txndbr)` | TOP200 | 0.49 | 0.36 | 19.8% | 60% | bull-only |
| `rank(fnd6_txndbr / close)` | TOP3000 | 0.30 | 0.17 | 45.3% | 60% | mixed |
| `rank(fnd6_txndbr)` | TOP3000 | 0.30 | 0.17 | 45.3% | 60% | mixed |
| `rank(ts_delta(fnd6_txndbr, 5))` | TOP200 | 0.21 | 0.09 | 21.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.353 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.353 (weakly positively correlated)
- min_total_assets_guidance: 0.353 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.353 (weakly positively correlated)
- shareholders_equity_max_guidance: 0.353 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
