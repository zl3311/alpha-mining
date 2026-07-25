---
field: anl4_totgw_mean
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.65
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1566
ann_vol: 0.0755
hit_rate: 0.5069
rolling_sharpe_min: -1.434
rolling_sharpe_max: 1.902
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.18
---
# anl4_totgw_mean (analyst4)

*Total Goodwill - mean of estimations*

## Signal Profile
- `rank(anl4_totgw_mean)`: S=0.23, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_totgw_mean / close)`: S=0.37, F=0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totgw_mean, 5))`: S=0.18, F=0.05, T=33.6%, INFERIOR (TOP200)
- `-rank(anl4_totgw_mean)`: S=0.04, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_mean, 5))`: S=0.47, F=0.14, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_totgw_mean, 63)`: S=0.65, F=0.34, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_totgw_mean, 10)`: S=-0.15, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totgw_mean, 22))`: S=0.35, F=0.12, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_mean)`: S=0.04, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_mean / close)`: S=-0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+1.8%
  - 2020: S=-1.03 (negative), ret=-8.6%
  - 2021: S=0.65 (moderate), ret=+6.0%
  - 2022: S=1.21 (moderate), ret=+10.1%
  - 2023: S=0.89 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 15.66% over 791 days (recovered)
- Annualized: return +2.7%, volatility 7.5% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.33, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.43, max 1.90, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.14%; worst month: -2.92%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.45
- Bear: S=-2.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totgw_mean, 5))` S=0.47, F=0.14, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_totgw_mean)`: S=0.04, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_mean / close)`: S=-0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_mean, 5))`: S=0.47, F=0.14, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totgw_mean / close)` | TOP3000 | 0.36 | 0.18 | 15.7% | 80% | bull-only |
| `rank(anl4_totgw_mean)` | TOP3000 | 0.22 | 0.10 | 35.2% | 80% | bull-only |
| `rank(ts_delta(anl4_totgw_mean, 5))` | TOP200 | 0.17 | 0.05 | 20.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_totgw_median: 1.000 (strongly positively correlated)
- anl4_totgw_high: 1.000 (strongly positively correlated)
- anl4_totgw_low: 0.999 (strongly positively correlated)
- total_goodwill_reported_value: 0.946 (strongly positively correlated)
- total_goodwill_actual_value: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
