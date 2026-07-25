---
field: fnd2_propplteqmuflmameqmt
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.47
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.3062
ann_vol: 0.1758
hit_rate: 0.4826
rolling_sharpe_min: -1.404
rolling_sharpe_max: 2.243
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.1
---
# fnd2_propplteqmuflmameqmt (fundamental2)

*PPE, Equipment, Useful Life, Maximum*

## Signal Profile
- `rank(fnd2_propplteqmuflmameqmt)`: S=-0.04, F=-0.01, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_propplteqmuflmameqmt / close)`: S=0.15, F=0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_propplteqmuflmameqmt, 5))`: S=0.47, F=0.34, T=15.6%, INFERIOR (TOP3000)
- `-rank(fnd2_propplteqmuflmameqmt)`: S=0.13, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmameqmt, 5))`: S=0.28, F=0.17, T=10.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_propplteqmuflmameqmt, 22)`: S=0.20, F=0.08, T=1.6%, INFERIOR (TOP3000)
- `ts_mean(fnd2_propplteqmuflmameqmt, 10)`: S=0.19, F=0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_propplteqmuflmameqmt, 22))`: S=0.01, F=0.00, T=9.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmameqmt)`: S=0.57, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmameqmt / close)`: S=-0.10, F=-0.03, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.14 (moderate), ret=+19.9%
  - 2020: S=0.28 (weak), ret=+6.7%
  - 2021: S=0.58 (moderate), ret=+9.7%
  - 2022: S=0.41 (weak), ret=+6.2%
  - 2023: S=-0.34 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 30.62% over 602 days (recovered)
- Annualized: return +8.0%, volatility 17.6% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew -0.20, excess kurtosis +20.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 2.24, latest -0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +12.73%; worst month: -8.46%
Positive months: 57%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.27
- Sideways: S=0.30
- Bear: S=-0.46

## Negated Direction
Best negated: `rank(-1 * fnd2_propplteqmuflmameqmt)` S=0.57, F=0.31, INFERIOR
Direction gap: +0.10 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_propplteqmuflmameqmt)`: S=0.57, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmameqmt / close)`: S=-0.10, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmameqmt, 5))`: S=0.28, F=0.17, T=10.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_propplteqmuflmameqmt, 5))` | TOP3000 | 0.46 | 0.34 | 30.6% | 80% | mixed |
| `rank(fnd2_propplteqmuflmameqmt / close)` | TOP3000 | 0.15 | 0.05 | 32.9% | 40% | bear-only |
| `rank(fnd2_propplteqmuflmameqmt / close)` | TOP500 | 0.10 | 0.03 | 18.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_netprofit_value: 0.290 (weakly positively correlated)
- net_profit_reported_value: 0.290 (weakly positively correlated)
- anl4_netprofita_value: 0.286 (weakly positively correlated)
- net_profit_adjusted_value: 0.286 (weakly positively correlated)
- fn_income_tax_expense_q: 0.285 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
