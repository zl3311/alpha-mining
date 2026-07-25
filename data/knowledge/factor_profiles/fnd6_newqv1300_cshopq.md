---
field: fnd6_newqv1300_cshopq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.59
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0798
ann_vol: 0.0398
hit_rate: 0.5053
rolling_sharpe_min: -2.033
rolling_sharpe_max: 2.355
negated_best_sharpe: 0.59
negated_best_template: neg_rank_level
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.22
---
# fnd6_newqv1300_cshopq (fundamental6)

*Total Shares Repurchased - Quarter*

## Signal Profile
- `rank(fnd6_newqv1300_cshopq)`: S=0.28, F=0.09, T=6.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_cshopq / close)`: S=0.37, F=0.13, T=6.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_cshopq, 5))`: S=0.18, F=0.04, T=45.4%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cshopq)`: S=-0.11, F=-0.02, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshopq, 5))`: S=-0.22, F=-0.06, T=45.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_cshopq, 22)`: S=0.18, F=0.04, T=36.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cshopq, 10)`: S=-0.42, F=-0.19, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cshopq, 22))`: S=0.20, F=0.04, T=19.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshopq)`: S=0.59, F=0.34, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshopq / close)`: S=0.47, F=0.24, T=8.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.02 (negative), ret=-0.1%
  - 2020: S=-1.87 (negative), ret=-5.5%
  - 2021: S=1.25 (moderate), ret=+5.2%
  - 2022: S=1.68 (strong), ret=+8.8%
  - 2023: S=-0.40 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 7.98% over 996 days (recovered)
- Annualized: return +1.4%, volatility 4.0% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.10, excess kurtosis +1.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.03, max 2.35, latest -0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.93%; worst month: -2.59%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=-0.12
- Bear: S=-2.84

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_cshopq)` S=0.59, F=0.34, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cshopq)`: S=0.59, F=0.34, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshopq / close)`: S=0.47, F=0.24, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshopq, 5))`: S=-0.22, F=-0.06, T=45.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cshopq / close)` | TOP3000 | 0.35 | 0.13 | 8.0% | 40% | bull-only |
| `rank(fnd6_newqv1300_cshopq)` | TOP3000 | 0.26 | 0.09 | 12.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_cshopq, 5))` | TOP200 | 0.19 | 0.04 | 37.3% | 60% | bear-only |
| `rank(fnd6_newqv1300_cshopq / close)` | TOP1000 | 0.10 | 0.02 | 9.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshopq)` | TOP1000 | 0.10 | 0.02 | 13.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- net_income_adjusted: 0.748 (strongly positively correlated)
- fn_repurchased_shares_value_q: 0.743 (strongly positively correlated)
- anl4_netprofit_mean: 0.742 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.741 (strongly positively correlated)
- est_ptp: 0.741 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
