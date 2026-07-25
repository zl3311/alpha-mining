---
field: correlation_last_360_days_spy
dataset: model51
best_template: ts_zscore
best_sharpe: 0.7
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.402
ann_vol: 0.0904
hit_rate: 0.498
rolling_sharpe_min: -4.015
rolling_sharpe_max: 2.525
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.49
---
# correlation_last_360_days_spy (model51)

*The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recent 360 calendar days*

## Signal Profile
- `rank(correlation_last_360_days_spy)`: S=0.35, F=0.18, T=10.4%, INFERIOR (TOP3000)
- `rank(ts_delta(correlation_last_360_days_spy, 5))`: S=0.25, F=0.06, T=50.7%, INFERIOR (TOP200)
- `-rank(correlation_last_360_days_spy)`: S=-0.05, F=-0.01, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_360_days_spy, 5))`: S=0.21, F=0.03, T=47.3%, INFERIOR (TOP3000)
- `-ts_zscore(correlation_last_360_days_spy, 63)`: S=0.70, F=0.35, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(correlation_last_360_days_spy, 10)`: S=0.09, F=0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(correlation_last_360_days_spy, 22))`: S=-0.90, F=-0.39, T=30.9%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_360_days_spy)`: S=-0.35, F=-0.18, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_360_days_spy / close)`: S=-0.10, F=-0.03, T=9.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.62 (strong), ret=+7.6%
  - 2020: S=-2.29 (negative), ret=-17.3%
  - 2021: S=0.81 (moderate), ret=+11.8%
  - 2022: S=0.91 (moderate), ret=+8.0%
  - 2023: S=1.14 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 40.20% over 1087 days (recovered)
- Annualized: return +3.2%, volatility 9.0% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew -0.04, excess kurtosis +3.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.01, max 2.52, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.08%; worst month: -11.39%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.95
- Sideways: S=0.76
- Bear: S=-1.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(correlation_last_360_days_spy, 5))` S=0.21, F=0.03, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * correlation_last_360_days_spy)`: S=-0.35, F=-0.18, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_360_days_spy / close)`: S=-0.10, F=-0.03, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_360_days_spy, 5))`: S=0.21, F=0.03, T=47.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(correlation_last_360_days_spy)` | TOP3000 | 0.36 | 0.18 | 40.2% | 80% | bull-only |
| `rank(ts_delta(correlation_last_360_days_spy, 5))` | TOP200 | 0.25 | 0.06 | 19.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- correlation_last_90_days_spy: 0.786 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.739 (strongly positively correlated)
- sga_expense: 0.739 (strongly positively correlated)
- fnd6_mrc5: 0.731 (strongly positively correlated)
- fnd6_mrc4: 0.730 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
