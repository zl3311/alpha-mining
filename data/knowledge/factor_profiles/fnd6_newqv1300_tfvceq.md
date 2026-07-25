---
field: fnd6_newqv1300_tfvceq
dataset: fundamental6
best_template: neg_rank
best_sharpe: 0.67
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.4254
ann_vol: 0.1897
hit_rate: 0.4632
rolling_sharpe_min: -1.106
rolling_sharpe_max: 1.889
negated_best_sharpe: 0.67
negated_best_template: neg_rank
negated_best_fitness: 0.53
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_newqv1300_tfvceq (fundamental6)

*Total Fair Value Changes including Earnings*

## Signal Profile
- `rank(fnd6_newqv1300_tfvceq)`: S=0.18, F=0.07, T=19.1%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_tfvceq / close)`: S=0.11, F=0.03, T=19.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_tfvceq, 5))`: S=0.23, F=0.09, T=27.8%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_tfvceq)`: S=0.67, F=0.53, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvceq, 5))`: S=0.54, F=0.29, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_tfvceq, 22)`: S=0.49, F=0.33, T=12.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_tfvceq, 10)`: S=0.61, F=0.44, T=8.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_tfvceq, 22))`: S=0.67, F=0.47, T=29.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvceq)`: S=0.68, F=0.44, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvceq / close)`: S=0.68, F=0.44, T=9.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 24F/8P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+4.8%
  - 2020: S=1.58 (strong), ret=+35.9%
  - 2021: S=-0.94 (negative), ret=-23.1%
  - 2022: S=-0.17 (negative), ret=-2.5%
  - 2023: S=0.39 (weak), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 42.54% over 1145 days (not yet recovered, ongoing at window end)
- Annualized: return +4.3%, volatility 19.0% (fraction of booksize)
- Hit rate: 46.3% positive days
- Tail shape: skew -0.40, excess kurtosis +36.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 1.89, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +15.05%; worst month: -15.49%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.11
- Sideways: S=1.96
- Bear: S=-0.69

## Negated Direction
Best negated: `-rank(fnd6_newqv1300_tfvceq)` S=0.67, F=0.53, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_tfvceq)`: S=0.68, F=0.44, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvceq / close)`: S=0.68, F=0.44, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvceq, 5))`: S=0.54, F=0.29, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_tfvceq, 5))` | TOP1000 | 0.23 | 0.09 | 42.5% | 60% | mixed |
| `rank(fnd6_newqv1300_tfvceq)` | TOP200 | 0.18 | 0.07 | 25.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_tfvceq / close)` | TOP200 | 0.10 | 0.03 | 24.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ivstq: 0.151 (weakly positively correlated)
- fnd6_incorp: -0.149 (weakly negatively correlated)
- fnd6_newa1v1300_ceqt: 0.140 (weakly positively correlated)
- reporting_currency_code_9: -0.137 (weakly negatively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.134 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
