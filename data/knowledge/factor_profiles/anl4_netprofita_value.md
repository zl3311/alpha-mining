---
field: anl4_netprofita_value
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.77
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3387
ann_vol: 0.1084
hit_rate: 0.5101
rolling_sharpe_min: -4.404
rolling_sharpe_max: 2.726
negated_best_sharpe: 0.77
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.39
---
# anl4_netprofita_value (analyst4)

*Adjusted net income- announced financial value*

## Signal Profile
- `rank(anl4_netprofita_value)`: S=0.21, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_value / close)`: S=0.38, F=0.22, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofita_value, 5))`: S=-0.64, F=-0.23, T=38.2%, INFERIOR (TOP1000)
- `-rank(anl4_netprofita_value)`: S=-0.07, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_value, 5))`: S=0.77, F=0.25, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netprofita_value, 63)`: S=-0.30, F=-0.08, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_value, 10)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_value, 22))`: S=0.05, F=0.01, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_value)`: S=-0.21, F=-0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_value / close)`: S=-0.38, F=-0.22, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+2.1%
  - 2020: S=-3.46 (negative), ret=-21.7%
  - 2021: S=1.31 (moderate), ret=+16.5%
  - 2022: S=1.73 (strong), ret=+27.4%
  - 2023: S=-0.42 (negative), ret=-4.1%

## Risk & Drawdown
- Max drawdown: 33.87% over 792 days (recovered)
- Annualized: return +4.1%, volatility 10.8% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew -0.10, excess kurtosis +1.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.40, max 2.73, latest -0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.15%; worst month: -7.72%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.87
- Bear: S=-3.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofita_value, 5))` S=0.77, F=0.25, INFERIOR
Direction gap: +0.39 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofita_value)`: S=-0.21, F=-0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_value / close)`: S=-0.38, F=-0.22, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_value, 5))`: S=0.77, F=0.25, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofita_value / close)` | TOP3000 | 0.38 | 0.22 | 33.9% | 60% | bull-only |
| `rank(anl4_netprofita_value)` | TOP3000 | 0.20 | 0.10 | 44.4% | 60% | bull-only |
| `rank(anl4_netprofita_value / close)` | TOP1000 | 0.22 | 0.10 | 35.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- net_profit_adjusted_value: 1.000 (strongly positively correlated)
- pretax_income_standalone_value: 0.987 (strongly positively correlated)
- anl4_ptp_value: 0.987 (strongly positively correlated)
- net_profit_reported_value: 0.987 (strongly positively correlated)
- anl4_netprofit_value: 0.987 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
