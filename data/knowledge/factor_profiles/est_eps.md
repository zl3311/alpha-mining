---
field: est_eps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.376
ann_vol: 0.1197
hit_rate: 0.5117
rolling_sharpe_min: -3.979
rolling_sharpe_max: 2.641
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.65
---
# est_eps (analyst4)

*Earnings per share - mean of estimations*

## Signal Profile
- `rank(est_eps)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(est_eps / close)`: S=0.90, F=0.74, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(est_eps, 5))`: S=0.36, F=0.08, T=36.0%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(est_eps), 5)`: S=0.39, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `-rank(est_eps)`: S=-0.14, F=-0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_eps, 5))`: S=0.25, F=0.06, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(est_eps, 22)`: S=0.05, F=0.00, T=32.7%, INFERIOR (TOP3000)
- `ts_mean(est_eps, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(est_eps, 22))`: S=0.07, F=0.01, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * est_eps)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_eps / close)`: S=0.04, F=0.01, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/34P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+2.7%
  - 2020: S=-3.23 (negative), ret=-24.1%
  - 2021: S=1.60 (strong), ret=+21.9%
  - 2022: S=1.60 (strong), ret=+27.5%
  - 2023: S=-0.45 (negative), ret=-5.1%

## Risk & Drawdown
- Max drawdown: 37.60% over 831 days (recovered)
- Annualized: return +4.7%, volatility 12.0% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew -0.05, excess kurtosis +1.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.98, max 2.64, latest -0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.69%; worst month: -8.10%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.71
- Sideways: S=0.77
- Bear: S=-3.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_eps, 5))` S=0.25, F=0.06, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_eps)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_eps / close)`: S=0.04, F=0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_eps, 5))`: S=0.25, F=0.06, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_eps)` | TOP3000 | 0.39 | 0.25 | 37.6% | 60% | bull-only |
| `ts_decay_linear(rank(est_eps), 5)` | TOP3000 | 0.38 | 0.24 | 37.7% | 60% | bull-only |
| `rank(ts_delta(est_eps, 5))` | TOP1000 | 0.37 | 0.08 | 8.9% | 60% | mixed |
| `rank(ts_delta(est_eps, 5))` | TOP3000 | 0.17 | 0.02 | 9.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfv4_eps_high: 0.999 (strongly positively correlated)
- anl4_netprofit_value: 0.968 (strongly positively correlated)
- net_profit_reported_value: 0.968 (strongly positively correlated)
- anl4_ptp_value: 0.966 (strongly positively correlated)
- pretax_income_standalone_value: 0.966 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
