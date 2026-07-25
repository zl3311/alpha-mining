---
field: anl4_qfv4_eps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.363
ann_vol: 0.1156
hit_rate: 0.5101
rolling_sharpe_min: -4.042
rolling_sharpe_max: 2.693
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.43
---
# anl4_qfv4_eps_high (analyst4)

*Earnings per share - The highest estimation*

## Signal Profile
- `rank(anl4_qfv4_eps_high)`: S=0.44, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_eps_high / close)`: S=1.01, F=0.85, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_eps_high, 5))`: S=0.39, F=0.09, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_qfv4_eps_high)`: S=-0.18, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_eps_high, 5))`: S=0.58, F=0.18, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_eps_high, 22)`: S=0.43, F=0.12, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_eps_high, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_eps_high, 22))`: S=0.55, F=0.21, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_high)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_high / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+3.3%
  - 2020: S=-3.28 (negative), ret=-23.6%
  - 2021: S=1.62 (strong), ret=+21.7%
  - 2022: S=1.70 (strong), ret=+27.9%
  - 2023: S=-0.45 (negative), ret=-4.9%

## Risk & Drawdown
- Max drawdown: 36.30% over 827 days (recovered)
- Annualized: return +5.0%, volatility 11.6% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew -0.04, excess kurtosis +1.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.04, max 2.69, latest -0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.41%; worst month: -7.54%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.79
- Sideways: S=0.79
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qfv4_eps_high, 5))` S=0.58, F=0.18, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_eps_high)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_high / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_eps_high, 5))`: S=0.58, F=0.18, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qfv4_eps_high)` | TOP3000 | 0.43 | 0.28 | 36.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- est_eps: 0.999 (strongly positively correlated)
- anl4_netprofit_value: 0.966 (strongly positively correlated)
- net_profit_reported_value: 0.965 (strongly positively correlated)
- anl4_ptp_value: 0.963 (strongly positively correlated)
- pretax_income_standalone_value: 0.963 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
