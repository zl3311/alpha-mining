---
field: anl4_totgw_low
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.92
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1585
ann_vol: 0.0759
hit_rate: 0.5036
rolling_sharpe_min: -1.463
rolling_sharpe_max: 1.898
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.49
---
# anl4_totgw_low (analyst4)

*Total Goodwill - The lowest estimation*

## Signal Profile
- `rank(anl4_totgw_low)`: S=0.23, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_totgw_low / close)`: S=0.38, F=0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totgw_low, 5))`: S=0.24, F=0.08, T=34.4%, INFERIOR (TOP200)
- `-rank(anl4_totgw_low)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_low, 5))`: S=0.43, F=0.12, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_totgw_low, 63)`: S=0.92, F=0.56, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_totgw_low, 10)`: S=-0.15, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totgw_low, 22))`: S=0.29, F=0.09, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_low)`: S=-0.23, F=-0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_low / close)`: S=-0.38, F=-0.18, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+2.2%
  - 2020: S=-1.07 (negative), ret=-8.9%
  - 2021: S=0.64 (moderate), ret=+6.0%
  - 2022: S=1.24 (moderate), ret=+10.4%
  - 2023: S=0.87 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 15.85% over 791 days (recovered)
- Annualized: return +2.8%, volatility 7.6% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.32, excess kurtosis +1.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 1.90, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.21%; worst month: -2.97%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=0.49
- Bear: S=-2.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totgw_low, 5))` S=0.43, F=0.12, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_totgw_low)`: S=-0.23, F=-0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_low / close)`: S=-0.38, F=-0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_low, 5))`: S=0.43, F=0.12, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totgw_low / close)` | TOP3000 | 0.37 | 0.18 | 15.8% | 80% | bull-only |
| `rank(anl4_totgw_low)` | TOP3000 | 0.23 | 0.10 | 35.5% | 80% | bull-only |
| `rank(ts_delta(anl4_totgw_low, 5))` | TOP200 | 0.22 | 0.08 | 27.4% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_totgw_median: 0.999 (strongly positively correlated)
- anl4_totgw_mean: 0.999 (strongly positively correlated)
- anl4_totgw_high: 0.999 (strongly positively correlated)
- total_goodwill_reported_value: 0.946 (strongly positively correlated)
- total_goodwill_actual_value: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
