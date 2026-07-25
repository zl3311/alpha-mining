---
field: anl4_totgw_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.37
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1554
ann_vol: 0.0751
hit_rate: 0.5045
rolling_sharpe_min: -1.424
rolling_sharpe_max: 1.891
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: 0.11
---
# anl4_totgw_high (analyst4)

*Total Goodwill - The highest estimation*

## Signal Profile
- `rank(anl4_totgw_high)`: S=0.23, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_totgw_high / close)`: S=0.37, F=0.17, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totgw_high, 5))`: S=0.24, F=0.07, T=35.1%, INFERIOR (TOP200)
- `-rank(anl4_totgw_high)`: S=0.04, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_high, 5))`: S=0.48, F=0.14, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_totgw_high, 63)`: S=0.20, F=0.06, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_totgw_high, 10)`: S=-0.14, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totgw_high, 22))`: S=-0.11, F=-0.02, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_high)`: S=-0.23, F=-0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_high / close)`: S=-0.37, F=-0.17, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.8%
  - 2020: S=-1.02 (negative), ret=-8.5%
  - 2021: S=0.64 (moderate), ret=+5.9%
  - 2022: S=1.19 (moderate), ret=+9.8%
  - 2023: S=0.89 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 15.54% over 791 days (recovered)
- Annualized: return +2.7%, volatility 7.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.34, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 1.89, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.09%; worst month: -2.90%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.43
- Bear: S=-2.74

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totgw_high, 5))` S=0.48, F=0.14, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_totgw_high)`: S=-0.23, F=-0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_high / close)`: S=-0.37, F=-0.17, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_high, 5))`: S=0.48, F=0.14, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totgw_high / close)` | TOP3000 | 0.35 | 0.17 | 15.5% | 80% | bull-only |
| `rank(anl4_totgw_high)` | TOP3000 | 0.22 | 0.10 | 35.0% | 80% | bull-only |
| `rank(ts_delta(anl4_totgw_high, 5))` | TOP200 | 0.24 | 0.07 | 28.6% | 80% | weak |
| `rank(ts_delta(anl4_totgw_high, 5))` | TOP500 | 0.14 | 0.02 | 16.1% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_totgw_mean: 1.000 (strongly positively correlated)
- anl4_totgw_median: 1.000 (strongly positively correlated)
- anl4_totgw_low: 0.999 (strongly positively correlated)
- total_goodwill_reported_value: 0.946 (strongly positively correlated)
- total_goodwill_actual_value: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
