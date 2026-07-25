---
field: total_goodwill_amount
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.84
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1491
ann_vol: 0.0742
hit_rate: 0.4955
rolling_sharpe_min: -1.606
rolling_sharpe_max: 1.868
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.45
---
# total_goodwill_amount (analyst4)

*Total Goodwill - Value*

## Signal Profile
- `rank(total_goodwill_amount)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(total_goodwill_amount / close)`: S=0.24, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(total_goodwill_amount, 5))`: S=0.04, F=0.00, T=36.9%, INFERIOR (TOP1000)
- `-rank(total_goodwill_amount)`: S=0.22, F=0.09, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_goodwill_amount, 5))`: S=0.84, F=0.30, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(total_goodwill_amount, 63)`: S=0.39, F=0.15, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(total_goodwill_amount, 10)`: S=-0.37, F=-0.20, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(total_goodwill_amount, 22))`: S=0.25, F=0.07, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_amount)`: S=-0.11, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_amount / close)`: S=-0.24, F=-0.09, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+1.9%
  - 2020: S=-1.18 (negative), ret=-8.9%
  - 2021: S=0.76 (moderate), ret=+7.3%
  - 2022: S=0.97 (moderate), ret=+8.4%
  - 2023: S=-0.09 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 14.91% over 789 days (recovered)
- Annualized: return +1.7%, volatility 7.4% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.16, excess kurtosis +2.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 1.87, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.27%; worst month: -3.53%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.64
- Sideways: S=0.40
- Bear: S=-3.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(total_goodwill_amount, 5))` S=0.84, F=0.30, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * total_goodwill_amount)`: S=-0.11, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * total_goodwill_amount / close)`: S=-0.24, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_goodwill_amount, 5))`: S=0.84, F=0.30, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(total_goodwill_amount / close)` | TOP3000 | 0.23 | 0.09 | 14.9% | 60% | bull-only |
| `rank(total_goodwill_amount)` | TOP3000 | 0.10 | 0.03 | 34.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_totgw_low: 0.942 (strongly positively correlated)
- anl4_totgw_mean: 0.941 (strongly positively correlated)
- anl4_totgw_median: 0.941 (strongly positively correlated)
- anl4_totgw_high: 0.940 (strongly positively correlated)
- fnd6_intan: 0.916 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
