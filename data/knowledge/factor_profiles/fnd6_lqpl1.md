---
field: fnd6_lqpl1
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.69
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 8
max_drawdown: 0.2713
ann_vol: 0.1558
hit_rate: 0.4769
rolling_sharpe_min: -0.588
rolling_sharpe_max: 2.084
negated_best_sharpe: 0.69
negated_best_template: neg_rank_level
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: 0.17
---
# fnd6_lqpl1 (fundamental6)

*Liabilities Level 1 (Quoted Prices)*

## Signal Profile
- `rank(fnd6_lqpl1)`: S=0.22, F=0.07, T=2.8%, INFERIOR (TOP500)
- `rank(fnd6_lqpl1 / close)`: S=0.24, F=0.08, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_lqpl1, 5))`: S=0.52, F=0.30, T=23.7%, INFERIOR (TOP1000)
- `-rank(fnd6_lqpl1)`: S=-0.14, F=-0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lqpl1, 5))`: S=0.44, F=0.30, T=13.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_lqpl1, 63)`: S=0.34, F=0.27, T=11.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lqpl1, 10)`: S=0.07, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lqpl1, 22))`: S=0.14, F=0.05, T=18.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lqpl1)`: S=0.69, F=0.48, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lqpl1 / close)`: S=0.68, F=0.46, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.51, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+3.7%
  - 2020: S=0.83 (moderate), ret=+10.8%
  - 2021: S=0.36 (weak), ret=+7.5%
  - 2022: S=0.07 (weak), ret=+1.3%
  - 2023: S=1.78 (strong), ret=+15.7%

## Risk & Drawdown
- Max drawdown: 27.13% over 358 days (recovered)
- Annualized: return +8.0%, volatility 15.6% (fraction of booksize)
- Hit rate: 47.7% positive days
- Tail shape: skew +1.09, excess kurtosis +25.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.59, max 2.08, latest 1.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +7.90%; worst month: -11.31%
Positive months: 56%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.36
- Sideways: S=1.39
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * fnd6_lqpl1)` S=0.69, F=0.48, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_lqpl1)`: S=0.69, F=0.48, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lqpl1 / close)`: S=0.68, F=0.46, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lqpl1, 5))`: S=0.44, F=0.30, T=13.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_lqpl1, 5))` | TOP1000 | 0.51 | 0.30 | 27.1% | 100% | weak |
| `rank(ts_delta(fnd6_lqpl1, 5))` | TOP3000 | 0.31 | 0.12 | 39.8% | 40% | mixed |
| `rank(fnd6_lqpl1 / close)` | TOP500 | 0.22 | 0.08 | 10.0% | 60% | bull-only |
| `rank(fnd6_lqpl1)` | TOP500 | 0.20 | 0.07 | 9.9% | 60% | bull-only |
| `rank(fnd6_lqpl1)` | TOP1000 | 0.12 | 0.03 | 10.1% | 40% | bull-only |
| `rank(fnd6_lqpl1 / close)` | TOP1000 | 0.11 | 0.03 | 9.7% | 40% | bull-only |
| `rank(ts_delta(fnd6_lqpl1, 5))` | TOP200 | 0.06 | 0.02 | 24.1% | 40% | mixed |
| `rank(ts_delta(fnd6_lqpl1, 5))` | TOP500 | 0.09 | 0.02 | 28.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.284 (weakly positively correlated)
- fnd6_txpd: 0.280 (weakly positively correlated)
- historical_volatility_20: 0.229 (weakly positively correlated)
- fnd6_newa1v1300_fca: 0.217 (weakly positively correlated)
- fnd6_fiao: 0.207 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
