---
field: fnd2_dfctrbplancstrg
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1029
ann_vol: 0.0673
hit_rate: 0.4834
rolling_sharpe_min: -1.064
rolling_sharpe_max: 2.006
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: neg_rank_level
negated_best_fitness: 0.39
n_negated_sims: 10
direction_gap: -0.15
---
# fnd2_dfctrbplancstrg (fundamental2)

*The amount of the cost recognized during the period for defined contribution plans.*

## Signal Profile
- `rank(fnd2_dfctrbplancstrg)`: S=0.29, F=0.14, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_dfctrbplancstrg / close)`: S=0.66, F=0.39, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfctrbplancstrg, 5))`: S=-0.11, F=-0.02, T=34.7%, INFERIOR (TOP1000)
- `-rank(fnd2_dfctrbplancstrg)`: S=-0.04, F=-0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfctrbplancstrg, 5))`: S=0.26, F=0.11, T=27.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfctrbplancstrg, 22)`: S=0.41, F=0.25, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfctrbplancstrg, 10)`: S=-0.19, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfctrbplancstrg, 22))`: S=0.14, F=0.04, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfctrbplancstrg)`: S=0.51, F=0.39, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfctrbplancstrg / close)`: S=0.45, F=0.29, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.4%
  - 2020: S=0.44 (weak), ret=+3.5%
  - 2021: S=0.76 (moderate), ret=+6.0%
  - 2022: S=1.48 (moderate), ret=+10.1%
  - 2023: S=0.13 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 10.29% over 244 days (recovered)
- Annualized: return +4.4%, volatility 6.7% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.51, excess kurtosis +2.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.01, latest 0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +7.83%; worst month: -3.84%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.13
- Bear: S=-1.60

## Negated Direction
Best negated: `rank(-1 * fnd2_dfctrbplancstrg)` S=0.51, F=0.39, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfctrbplancstrg)`: S=0.51, F=0.39, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfctrbplancstrg / close)`: S=0.45, F=0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfctrbplancstrg, 5))`: S=0.26, F=0.11, T=27.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfctrbplancstrg / close)` | TOP3000 | 0.66 | 0.39 | 10.3% | 100% | bull-only |
| `rank(fnd2_dfctrbplancstrg)` | TOP3000 | 0.29 | 0.14 | 27.9% | 80% | bull-only |
| `rank(fnd2_dfctrbplancstrg / close)` | TOP1000 | 0.28 | 0.13 | 11.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xpr: 0.934 (strongly positively correlated)
- actual_sales_value_annual: 0.922 (strongly positively correlated)
- fn_employee_related_liab_a: 0.922 (strongly positively correlated)
- fnd6_newa1v1300_ap: 0.919 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.918 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
