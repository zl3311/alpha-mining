---
field: fnd6_xad
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.64
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1478
ann_vol: 0.073
hit_rate: 0.5279
rolling_sharpe_min: -1.664
rolling_sharpe_max: 2.96
redundancy_cluster: 32
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.07
---
# fnd6_xad (fundamental6)

*Advertising Expense*

## Signal Profile
- `rank(fnd6_xad)`: S=0.64, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_xad / close)`: S=0.36, F=0.16, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xad, 5))`: S=-0.04, F=-0.01, T=20.3%, INFERIOR (TOP200)
- `-rank(fnd6_xad)`: S=-0.03, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xad, 5))`: S=0.57, F=0.33, T=38.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_xad, 63)`: S=-0.03, F=-0.01, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xad, 10)`: S=-0.01, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xad, 22))`: S=0.44, F=0.26, T=19.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xad)`: S=-0.03, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xad / close)`: S=-0.26, F=-0.12, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.42 (weak), ret=+1.9%
  - 2020: S=-0.85 (negative), ret=-5.2%
  - 2021: S=1.03 (moderate), ret=+10.8%
  - 2022: S=1.08 (moderate), ret=+8.1%
  - 2023: S=1.24 (moderate), ret=+7.3%

## Risk & Drawdown
- Max drawdown: 14.78% over 597 days (recovered)
- Annualized: return +4.7%, volatility 7.3% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.16, excess kurtosis +1.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.96, latest 1.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +6.40%; worst month: -3.73%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.65
- Sideways: S=0.79
- Bear: S=-1.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_xad, 5))` S=0.57, F=0.33, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_xad)`: S=-0.03, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xad / close)`: S=-0.26, F=-0.12, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xad, 5))`: S=0.57, F=0.33, T=38.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xad)` | TOP3000 | 0.64 | 0.39 | 14.8% | 80% | bull-only |
| `rank(fnd6_xad / close)` | TOP3000 | 0.36 | 0.16 | 13.4% | 80% | mixed |
| `rank(fnd6_xad / close)` | TOP500 | 0.27 | 0.13 | 34.4% | 60% | bull-only |
| `rank(fnd6_xad / close)` | TOP1000 | 0.26 | 0.12 | 18.2% | 60% | bull-only |
| `rank(fnd6_xad / close)` | TOP200 | 0.16 | 0.06 | 48.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sga_expense: 0.865 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.865 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.861 (strongly positively correlated)
- highest_sales_estimate: 0.836 (strongly positively correlated)
- median_sales_estimate: 0.834 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
