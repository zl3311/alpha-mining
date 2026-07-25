---
field: cashflow_fin
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.06
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.2822
ann_vol: 0.0906
hit_rate: 0.5174
rolling_sharpe_min: -1.622
rolling_sharpe_max: 5.105
negated_best_sharpe: 1.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.8
n_negated_sims: 10
direction_gap: 0.3
---
# cashflow_fin (fundamental6)

*Financing Activities - Net Cash Flow*

## Signal Profile
- `rank(cashflow_fin)`: S=0.35, F=0.18, T=2.1%, INFERIOR (TOP500)
- `rank(cashflow_fin / close)`: S=0.32, F=0.16, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(cashflow_fin, 5))`: S=-0.67, F=-0.43, T=32.7%, INFERIOR (TOP200)
- `ts_decay_linear(rank(cashflow_fin), 5)`: S=-0.26, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `-rank(cashflow_fin)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_fin, 5))`: S=1.06, F=0.80, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_fin, 63)`: S=0.76, F=0.56, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(cashflow_fin, 10)`: S=-0.01, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_fin, 22))`: S=-0.45, F=-0.22, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_fin)`: S=-0.35, F=-0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_fin / close)`: S=-0.32, F=-0.16, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/22P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.13 (negative), ret=-0.6%
  - 2020: S=4.41 (strong), ret=+28.5%
  - 2021: S=-0.32 (negative), ret=-3.3%
  - 2022: S=-1.02 (negative), ret=-13.5%
  - 2023: S=0.76 (moderate), ret=+5.5%

## Risk & Drawdown
- Max drawdown: 28.22% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +3.4%, volatility 9.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.30, excess kurtosis +2.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.62, max 5.11, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.59%; worst month: -4.82%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.56
- Sideways: S=-0.36
- Bear: S=3.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(cashflow_fin, 5))` S=1.06, F=0.80, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * cashflow_fin)`: S=-0.35, F=-0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_fin / close)`: S=-0.32, F=-0.16, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_fin, 5))`: S=1.06, F=0.80, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow_fin)` | TOP500 | 0.37 | 0.18 | 28.2% | 40% | bear-only |
| `rank(cashflow_fin / close)` | TOP500 | 0.34 | 0.16 | 35.0% | 60% | bear-only |
| `rank(cashflow_fin / close)` | TOP200 | 0.25 | 0.11 | 40.0% | 40% | bear-only |
| `rank(cashflow_fin)` | TOP200 | 0.21 | 0.08 | 37.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_fincf: 1.000 (strongly positively correlated)
- cash_flow_from_financing: 0.966 (strongly positively correlated)
- cashflow_dividends: -0.851 (strongly negatively correlated)
- fnd6_newa1v1300_dv: -0.850 (strongly negatively correlated)
- parkinson_volatility_150: 0.835 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
