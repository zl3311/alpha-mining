---
field: fnd6_txdfo
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1752
ann_vol: 0.1638
hit_rate: 0.4972
rolling_sharpe_min: -0.991
rolling_sharpe_max: 1.613
negated_best_sharpe: 0.57
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: 0.03
---
# fnd6_txdfo (fundamental6)

*Deferred Taxes - Foreign*

## Signal Profile
- `rank(fnd6_txdfo)`: S=0.08, F=0.01, T=2.7%, INFERIOR (TOP500)
- `rank(fnd6_txdfo / close)`: S=-0.02, F=0.00, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_txdfo, 5))`: S=0.46, F=0.22, T=31.9%, INFERIOR (TOP500)
- `-rank(fnd6_txdfo)`: S=0.34, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdfo, 5))`: S=-0.03, F=0.00, T=42.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txdfo, 22)`: S=0.54, F=0.38, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txdfo, 10)`: S=0.05, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdfo, 22))`: S=-0.02, F=0.00, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfo)`: S=0.53, F=0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfo / close)`: S=0.57, F=0.21, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.53 (strong), ret=+23.1%
  - 2020: S=0.44 (weak), ret=+8.2%
  - 2021: S=0.67 (moderate), ret=+9.9%
  - 2022: S=-0.15 (negative), ret=-2.5%
  - 2023: S=-0.15 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 17.52% over 701 days (not yet recovered, ongoing at window end)
- Annualized: return +7.5%, volatility 16.4% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew -0.80, excess kurtosis +14.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.61, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +13.12%; worst month: -8.53%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.44
- Sideways: S=1.49
- Bear: S=-0.54

## Negated Direction
Best negated: `rank(-1 * fnd6_txdfo / close)` S=0.57, F=0.21, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdfo)`: S=0.53, F=0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfo / close)`: S=0.57, F=0.21, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdfo, 5))`: S=-0.03, F=0.00, T=42.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdfo, 5))` | TOP500 | 0.46 | 0.22 | 17.5% | 60% | mixed |
| `rank(ts_delta(fnd6_txdfo, 5))` | TOP200 | 0.22 | 0.09 | 31.9% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd2_dfdfritxexp: 0.385 (weakly positively correlated)
- fnd6_optca: 0.236 (weakly positively correlated)
- fnd6_txdi: 0.222 (weakly positively correlated)
- fnd6_esopnr: 0.190 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.189 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
