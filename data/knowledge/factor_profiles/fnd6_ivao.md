---
field: fnd6_ivao
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.65
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.165
ann_vol: 0.1716
hit_rate: 0.4923
rolling_sharpe_min: -0.441
rolling_sharpe_max: 1.436
negated_best_sharpe: 0.31
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_ivao (fundamental6)

*Investment and Advances - Other*

## Signal Profile
- `rank(fnd6_ivao)`: S=0.14, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_ivao / close)`: S=0.20, F=0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ivao, 5))`: S=0.37, F=0.16, T=35.4%, INFERIOR (TOP500)
- `-rank(fnd6_ivao)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivao, 5))`: S=-0.02, F=0.00, T=30.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ivao, 63)`: S=0.65, F=0.51, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivao, 10)`: S=0.33, F=0.15, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivao, 22))`: S=0.14, F=0.04, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivao)`: S=0.31, F=0.17, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivao / close)`: S=0.24, F=0.11, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+4.8%
  - 2020: S=-0.12 (negative), ret=-1.7%
  - 2021: S=1.13 (moderate), ret=+21.6%
  - 2022: S=-0.08 (negative), ret=-1.6%
  - 2023: S=0.47 (weak), ret=+7.5%

## Risk & Drawdown
- Max drawdown: 16.50% over 197 days (not yet recovered, ongoing at window end)
- Annualized: return +6.2%, volatility 17.2% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew -0.28, excess kurtosis +6.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.44, max 1.44, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +9.83%; worst month: -9.53%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.55
- Sideways: S=0.56
- Bear: S=-0.01

## Negated Direction
Best negated: `rank(-1 * fnd6_ivao)` S=0.31, F=0.17, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ivao)`: S=0.31, F=0.17, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivao / close)`: S=0.24, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivao, 5))`: S=-0.02, F=0.00, T=30.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ivao, 5))` | TOP500 | 0.36 | 0.16 | 16.5% | 60% | mixed |
| `rank(ts_delta(fnd6_ivao, 5))` | TOP1000 | 0.32 | 0.12 | 15.3% | 60% | mixed |
| `rank(ts_delta(fnd6_ivao, 5))` | TOP3000 | 0.27 | 0.09 | 29.5% | 60% | mixed |
| `rank(fnd6_ivao / close)` | TOP3000 | 0.20 | 0.06 | 11.4% | 40% | bull-only |
| `rank(fnd6_ivao)` | TOP3000 | 0.13 | 0.04 | 19.2% | 40% | bull-only |
| `rank(fnd6_ivao / close)` | TOP1000 | 0.10 | 0.03 | 13.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrcta: 0.162 (weakly positively correlated)
- fnd6_newa2v1300_nopi: 0.153 (weakly positively correlated)
- fnd6_lcoxdr: 0.135 (weakly positively correlated)
- fnd6_txpd: 0.126 (weakly positively correlated)
- fnd6_lqpl1: 0.122 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
