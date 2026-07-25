---
field: fnd6_newqv1300_esopnrq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.38
best_fitness: 0.28
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2933
ann_vol: 0.1819
hit_rate: 0.5061
rolling_sharpe_min: -1.414
rolling_sharpe_max: 2.184
negated_best_sharpe: 0.29
negated_best_template: neg_rank_level
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.09
---
# fnd6_newqv1300_esopnrq (fundamental6)

*Preferred ESOP Obligation - Non-Redeemable*

## Signal Profile
- `rank(fnd6_newqv1300_esopnrq)`: S=0.38, F=0.28, T=6.9%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_esopnrq / close)`: S=0.38, F=0.28, T=6.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_esopnrq, 5))`: S=0.40, F=0.20, T=5.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_esopnrq)`: S=0.27, F=0.19, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_esopnrq, 5))`: S=0.36, F=0.17, T=5.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_esopnrq, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_newqv1300_esopnrq, 10)`: S=-0.25, F=-0.17, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_esopnrq, 22))`: S=0.36, F=0.22, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esopnrq)`: S=0.29, F=0.22, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esopnrq / close)`: S=0.29, F=0.22, T=6.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/21P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.95 (moderate), ret=+16.1%
  - 2020: S=-1.07 (negative), ret=-17.3%
  - 2021: S=0.55 (moderate), ret=+9.3%
  - 2022: S=0.36 (weak), ret=+7.1%
  - 2023: S=0.85 (moderate), ret=+16.6%

## Risk & Drawdown
- Max drawdown: 29.33% over 854 days (recovered)
- Annualized: return +6.5%, volatility 18.2% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.38, excess kurtosis +5.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 2.18, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +14.30%; worst month: -14.32%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=0.19
- Bear: S=-0.79

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_esopnrq)` S=0.29, F=0.22, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_esopnrq)`: S=0.29, F=0.22, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esopnrq / close)`: S=0.29, F=0.22, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_esopnrq, 5))`: S=0.36, F=0.17, T=5.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_esopnrq / close)` | TOP500 | 0.36 | 0.28 | 29.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_esopnrq)` | TOP500 | 0.35 | 0.28 | 29.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_esopnrq, 5))` | TOP3000 | 0.39 | 0.20 | 30.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_esopnrq, 5))` | TOP1000 | 0.20 | 0.08 | 27.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_esopnrq, 5))` | TOP500 | 0.21 | 0.08 | 26.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- beta_last_90_days_spy: -0.324 (weakly negatively correlated)
- systematic_risk_last_90_days: -0.320 (weakly negatively correlated)
- fnd6_newa1v1300_fincf: -0.297 (weakly negatively correlated)
- cashflow_fin: -0.296 (weakly negatively correlated)
- fnd6_prch: -0.279 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
