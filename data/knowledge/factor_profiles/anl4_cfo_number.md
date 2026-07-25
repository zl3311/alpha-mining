---
field: anl4_cfo_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.76
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 10
max_drawdown: 0.0327
ann_vol: 0.0318
hit_rate: 0.5336
rolling_sharpe_min: -0.716
rolling_sharpe_max: 1.72
negated_best_sharpe: 0.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.71
---
# anl4_cfo_number (analyst4)

*Cash Flow From Operations - number of estimations*

## Signal Profile
- `rank(anl4_cfo_number)`: S=0.76, F=0.33, T=2.5%, INFERIOR (TOP3000)
- `rank(anl4_cfo_number / close)`: S=0.52, F=0.33, T=3.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfo_number, 5))`: S=0.59, F=0.20, T=36.7%, INFERIOR (TOP3000)
- `-rank(anl4_cfo_number)`: S=-0.34, F=-0.11, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_number, 5))`: S=0.05, F=0.01, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfo_number, 63)`: S=-0.04, F=0.00, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfo_number, 10)`: S=0.50, F=0.23, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfo_number, 22))`: S=-0.13, F=-0.03, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_number)`: S=-0.18, F=-0.05, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_number / close)`: S=-0.21, F=-0.08, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.08 (moderate), ret=+3.0%
  - 2020: S=0.70 (moderate), ret=+2.3%
  - 2021: S=0.50 (weak), ret=+1.6%
  - 2022: S=0.58 (moderate), ret=+2.0%
  - 2023: S=1.15 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 3.27% over 242 days (recovered)
- Annualized: return +2.5%, volatility 3.2% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +0.04, excess kurtosis +0.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 1.72, latest 1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +1.58%; worst month: -1.27%
Positive months: 61%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.49
- Sideways: S=1.47
- Bear: S=0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfo_number, 5))` S=0.05, F=0.01, INFERIOR
Direction gap: -0.71 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cfo_number)`: S=-0.18, F=-0.05, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_number / close)`: S=-0.21, F=-0.08, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_number, 5))`: S=0.05, F=0.01, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfo_number / close)` | TOP200 | 0.53 | 0.33 | 16.9% | 100% | mixed |
| `rank(anl4_cfo_number)` | TOP3000 | 0.78 | 0.33 | 3.3% | 100% | weak |
| `rank(ts_delta(anl4_cfo_number, 5))` | TOP1000 | 0.58 | 0.20 | 8.1% | 100% | bear-only |
| `rank(ts_delta(anl4_cfo_number, 5))` | TOP3000 | 0.60 | 0.20 | 15.3% | 80% | mixed |
| `rank(anl4_cfo_number)` | TOP1000 | 0.36 | 0.11 | 7.2% | 80% | mixed |
| `rank(anl4_cfo_number / close)` | TOP500 | 0.22 | 0.08 | 24.8% | 60% | bear-only |
| `rank(anl4_cfo_number / close)` | TOP1000 | 0.17 | 0.07 | 30.2% | 40% | bear-only |
| `rank(ts_delta(anl4_cfo_number, 5))` | TOP200 | 0.19 | 0.05 | 30.1% | 60% | weak |
| `rank(anl4_cfo_number)` | TOP500 | 0.20 | 0.05 | 10.5% | 80% | weak |
| `rank(anl4_cfo_number / close)` | TOP3000 | 0.07 | 0.02 | 48.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_number: 0.630 (moderately positively correlated)
- anl4_ebit_number: 0.416 (moderately positively correlated)
- anl4_cfi_number: 0.411 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.404 (moderately positively correlated)
- anl4_netprofit_number: 0.386 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
