---
field: est_capex
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.67
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1043
ann_vol: 0.067
hit_rate: 0.4802
rolling_sharpe_min: -1.58
rolling_sharpe_max: 2.219
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.28
---
# est_capex (analyst4)

*Capital Expenditures - mean of estimations*

## Signal Profile
- `rank(est_capex)`: S=0.32, F=0.16, T=1.0%, INFERIOR (TOP3000)
- `rank(est_capex / close)`: S=0.39, F=0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(est_capex, 5))`: S=0.20, F=0.03, T=36.5%, INFERIOR (TOP3000)
- `-rank(est_capex)`: S=-0.15, F=-0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_capex, 5))`: S=0.67, F=0.24, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(est_capex, 63)`: S=-0.35, F=-0.11, T=17.3%, INFERIOR (TOP3000)
- `ts_mean(est_capex, 10)`: S=0.10, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_capex, 22))`: S=-0.15, F=-0.03, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * est_capex)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * est_capex / close)`: S=-0.09, F=-0.02, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.34 (negative), ret=-1.6%
  - 2020: S=0.27 (weak), ret=+2.1%
  - 2021: S=0.92 (moderate), ret=+7.5%
  - 2022: S=0.34 (weak), ret=+2.1%
  - 2023: S=0.49 (weak), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 10.43% over 577 days (not yet recovered, ongoing at window end)
- Annualized: return +2.6%, volatility 6.7% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.56, excess kurtosis +2.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 2.22, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.89%; worst month: -4.26%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.11
- Sideways: S=-0.11
- Bear: S=-1.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_capex, 5))` S=0.67, F=0.24, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_capex)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * est_capex / close)`: S=-0.09, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_capex, 5))`: S=0.67, F=0.24, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_capex / close)` | TOP3000 | 0.39 | 0.18 | 10.4% | 80% | bull-only |
| `rank(est_capex)` | TOP3000 | 0.32 | 0.16 | 30.8% | 80% | bull-only |
| `rank(est_capex / close)` | TOP1000 | 0.17 | 0.06 | 13.3% | 40% | bull-only |
| `rank(est_capex)` | TOP1000 | 0.14 | 0.05 | 34.5% | 60% | bull-only |
| `rank(ts_delta(est_capex, 5))` | TOP3000 | 0.22 | 0.03 | 10.0% | 80% | weak |
| `rank(est_capex / close)` | TOP500 | 0.08 | 0.02 | 27.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_capex_mean: 0.974 (strongly positively correlated)
- anl4_capex_low: 0.968 (strongly positively correlated)
- est_tot_assets: 0.959 (strongly positively correlated)
- assets: 0.953 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 0.953 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
