---
field: fnd2_propplteqmuflmeqmt
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.65
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.222
ann_vol: 0.1616
hit_rate: 0.4785
rolling_sharpe_min: -1.178
rolling_sharpe_max: 2.037
negated_best_sharpe: 0.65
negated_best_template: neg_rank_level
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.0
---
# fnd2_propplteqmuflmeqmt (fundamental2)

*PPE, Equipment, Useful Life, Minimum*

## Signal Profile
- `rank(fnd2_propplteqmuflmeqmt)`: S=0.33, F=0.10, T=1.1%, INFERIOR (TOP1000)
- `rank(fnd2_propplteqmuflmeqmt / close)`: S=0.18, F=0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_propplteqmuflmeqmt, 5))`: S=0.30, F=0.19, T=10.2%, INFERIOR (TOP1000)
- `-rank(fnd2_propplteqmuflmeqmt)`: S=-0.33, F=-0.10, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmeqmt, 5))`: S=0.35, F=0.20, T=5.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_propplteqmuflmeqmt, 63)`: S=-0.40, F=-0.39, T=0.9%, INFERIOR (TOP3000)
- `ts_mean(fnd2_propplteqmuflmeqmt, 10)`: S=0.65, F=0.32, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_propplteqmuflmeqmt, 22))`: S=-0.11, F=-0.05, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmeqmt)`: S=0.65, F=0.37, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmeqmt / close)`: S=0.28, F=0.13, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.29, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.02 (negative), ret=-0.2%
  - 2020: S=0.05 (weak), ret=+0.7%
  - 2021: S=-0.15 (negative), ret=-2.2%
  - 2022: S=1.30 (moderate), ret=+32.2%
  - 2023: S=-0.68 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 22.20% over 657 days (recovered)
- Annualized: return +4.7%, volatility 16.2% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +1.72, excess kurtosis +44.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.18, max 2.04, latest -0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +28.33%; worst month: -10.74%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.40
- Sideways: S=-0.29
- Bear: S=-0.35

## Negated Direction
Best negated: `rank(-1 * fnd2_propplteqmuflmeqmt)` S=0.65, F=0.37, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_propplteqmuflmeqmt)`: S=0.65, F=0.37, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmeqmt / close)`: S=0.28, F=0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmeqmt, 5))`: S=0.35, F=0.20, T=5.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_propplteqmuflmeqmt, 5))` | TOP1000 | 0.29 | 0.19 | 22.2% | 40% | mixed |
| `rank(fnd2_propplteqmuflmeqmt)` | TOP1000 | 0.33 | 0.10 | 8.6% | 80% | bull-only |
| `rank(fnd2_propplteqmuflmeqmt / close)` | TOP3000 | 0.19 | 0.07 | 35.1% | 40% | bear-only |
| `rank(fnd2_propplteqmuflmeqmt / close)` | TOP1000 | 0.15 | 0.05 | 29.6% | 60% | bear-only |
| `rank(fnd2_propplteqmuflmeqmt / close)` | TOP500 | 0.10 | 0.02 | 19.2% | 60% | mixed |
| `rank(fnd2_propplteqmuflmeqmt)` | TOP3000 | 0.13 | 0.02 | 8.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptpr_low: 0.342 (weakly positively correlated)
- anl4_ptpr_median: 0.341 (weakly positively correlated)
- anl4_ptpr_mean: 0.341 (weakly positively correlated)
- pretax_income_total: 0.340 (weakly positively correlated)
- fnd6_pifo: 0.340 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
