---
field: correlation_last_90_days_spy
dataset: model51
best_template: ts_zscore
best_sharpe: 0.8
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.2949
ann_vol: 0.0714
hit_rate: 0.4923
rolling_sharpe_min: -3.37
rolling_sharpe_max: 2.724
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.57
---
# correlation_last_90_days_spy (model51)

*The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recent 90 calendar days*

## Signal Profile
- `rank(correlation_last_90_days_spy)`: S=0.19, F=0.06, T=13.0%, INFERIOR (TOP3000)
- `rank(ts_delta(correlation_last_90_days_spy, 5))`: S=-0.23, F=-0.04, T=42.9%, INFERIOR (TOP3000)
- `-rank(correlation_last_90_days_spy)`: S=0.08, F=0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_90_days_spy, 5))`: S=0.23, F=0.04, T=42.9%, INFERIOR (TOP3000)
- `-ts_zscore(correlation_last_90_days_spy, 63)`: S=0.80, F=0.42, T=20.3%, INFERIOR (TOP3000)
- `ts_mean(correlation_last_90_days_spy, 10)`: S=0.00, F=0.00, T=4.8%, INFERIOR (TOP3000)
- `rank(ts_rank(correlation_last_90_days_spy, 22))`: S=-0.63, F=-0.23, T=30.4%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_90_days_spy)`: S=-0.19, F=-0.06, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_90_days_spy / close)`: S=-0.05, F=-0.01, T=10.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.20, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.35 (moderate), ret=+5.2%
  - 2020: S=-2.23 (negative), ret=-15.9%
  - 2021: S=1.17 (moderate), ret=+11.5%
  - 2022: S=0.57 (moderate), ret=+4.6%
  - 2023: S=0.40 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 29.49% over 1079 days (recovered)
- Annualized: return +1.4%, volatility 7.1% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.10, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.37, max 2.72, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +7.77%; worst month: -8.09%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.41
- Sideways: S=0.47
- Bear: S=-1.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(correlation_last_90_days_spy, 5))` S=0.23, F=0.04, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * correlation_last_90_days_spy)`: S=-0.19, F=-0.06, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_90_days_spy / close)`: S=-0.05, F=-0.01, T=10.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_90_days_spy, 5))`: S=0.23, F=0.04, T=42.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(correlation_last_90_days_spy)` | TOP3000 | 0.20 | 0.06 | 29.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- correlation_last_360_days_spy: 0.786 (strongly positively correlated)
- implied_volatility_mean_skew_10: 0.520 (moderately positively correlated)
- fnd6_newa2v1300_wcap: 0.502 (moderately positively correlated)
- working_capital: 0.499 (moderately positively correlated)
- fnd6_newqv1300_wcapq: 0.499 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
