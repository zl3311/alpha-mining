---
field: fnd6_txdfed
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.34
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.383
ann_vol: 0.1756
hit_rate: 0.4729
rolling_sharpe_min: -1.85
rolling_sharpe_max: 1.754
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_txdfed (fundamental6)

*Deferred Taxes - Federal*

## Signal Profile
- `rank(fnd6_txdfed)`: S=0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_txdfed / close)`: S=0.08, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txdfed, 5))`: S=0.09, F=0.02, T=32.1%, INFERIOR (TOP500)
- `-rank(fnd6_txdfed)`: S=0.01, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdfed, 5))`: S=0.26, F=0.12, T=24.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txdfed, 63)`: S=0.00, F=0.00, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txdfed, 10)`: S=-0.22, F=-0.08, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdfed, 22))`: S=0.34, F=0.15, T=21.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfed)`: S=0.13, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfed / close)`: S=0.14, F=0.04, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.09, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+3.0%
  - 2020: S=-0.72 (negative), ret=-12.3%
  - 2021: S=-0.13 (negative), ret=-2.6%
  - 2022: S=-0.10 (negative), ret=-1.6%
  - 2023: S=1.29 (moderate), ret=+21.5%

## Risk & Drawdown
- Max drawdown: 38.30% over 1352 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 17.6% (fraction of booksize)
- Hit rate: 47.3% positive days
- Tail shape: skew -0.10, excess kurtosis +12.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.85, max 1.75, latest 1.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +11.01%; worst month: -10.44%
Positive months: 61%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.02
- Sideways: S=0.18
- Bear: S=0.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txdfed, 5))` S=0.26, F=0.12, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdfed)`: S=0.13, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdfed / close)`: S=0.14, F=0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdfed, 5))`: S=0.26, F=0.12, T=24.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdfed, 5))` | TOP500 | 0.09 | 0.02 | 38.3% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_txdi: 0.477 (moderately positively correlated)
- fnd6_txds: 0.393 (weakly positively correlated)
- fnd2_dfdfeditxexp: 0.219 (weakly positively correlated)
- fnd6_pidom: 0.212 (weakly positively correlated)
- fnd6_cidergl: 0.211 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
