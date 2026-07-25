---
field: fnd6_txds
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.6
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.2676
ann_vol: 0.1635
hit_rate: 0.4664
rolling_sharpe_min: -1.083
rolling_sharpe_max: 1.607
negated_best_sharpe: 0.6
negated_best_template: neg_rank_level
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.26
---
# fnd6_txds (fundamental6)

*Deferred Taxes - State*

## Signal Profile
- `rank(fnd6_txds)`: S=0.00, F=0.00, T=2.9%, INFERIOR (TOP500)
- `rank(fnd6_txds / close)`: S=0.05, F=0.01, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_txds, 5))`: S=0.35, F=0.15, T=30.0%, INFERIOR (TOP500)
- `-rank(fnd6_txds)`: S=0.23, F=0.07, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txds, 5))`: S=0.30, F=0.10, T=43.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txds, 63)`: S=0.34, F=0.20, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txds, 10)`: S=-0.27, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txds, 22))`: S=-0.53, F=-0.29, T=21.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txds)`: S=0.60, F=0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txds / close)`: S=0.58, F=0.22, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.35, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.15 (moderate), ret=+15.0%
  - 2020: S=-0.23 (negative), ret=-4.1%
  - 2021: S=0.50 (moderate), ret=+7.9%
  - 2022: S=0.92 (moderate), ret=+16.3%
  - 2023: S=-0.45 (negative), ret=-7.0%

## Risk & Drawdown
- Max drawdown: 26.76% over 659 days (recovered)
- Annualized: return +5.7%, volatility 16.4% (fraction of booksize)
- Hit rate: 46.6% positive days
- Tail shape: skew +1.30, excess kurtosis +21.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 1.61, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +9.05%; worst month: -12.76%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.64
- Sideways: S=0.66
- Bear: S=-0.26

## Negated Direction
Best negated: `rank(-1 * fnd6_txds)` S=0.60, F=0.22, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txds)`: S=0.60, F=0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txds / close)`: S=0.58, F=0.22, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txds, 5))`: S=0.30, F=0.10, T=43.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txds, 5))` | TOP500 | 0.35 | 0.15 | 26.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdfed: 0.393 (weakly positively correlated)
- fnd6_lno: 0.255 (weakly positively correlated)
- fnd6_dvpa: 0.185 (weakly positively correlated)
- fnd2_dfdlocalitxexp: 0.184 (weakly positively correlated)
- min_free_cash_flow_per_share_guidance: 0.177 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
