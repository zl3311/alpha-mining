---
field: rp_css_credit
dataset: news18
best_template: ts_zscore
best_sharpe: 0.87
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.3292
ann_vol: 0.2038
hit_rate: 0.3142
rolling_sharpe_min: -0.874
rolling_sharpe_max: 1.879
negated_best_sharpe: 0.14
negated_best_template: neg_rank
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.73
---
# rp_css_credit (news18)

*Composite sentiment score of credit news*

## Signal Profile
- `rank(rp_css_credit)`: S=0.57, F=0.22, T=75.0%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_credit, 5))`: S=0.34, F=0.18, T=13.7%, INFERIOR (TOP1000)
- `-rank(rp_css_credit)`: S=0.14, F=0.02, T=150.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_credit, 5))`: S=-0.01, F=0.00, T=19.4%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_credit, 63)`: S=0.87, F=0.44, T=140.1%, INFERIOR (TOP3000)
- `ts_mean(rp_css_credit, 10)`: S=-0.33, F=-0.10, T=38.3%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_credit, 22))`: S=-0.28, F=-0.07, T=147.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit)`: S=-0.34, F=-0.08, T=177.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit / close)`: S=-0.18, F=-0.03, T=177.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 12F/8P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+13.9%
  - 2020: S=0.42 (weak), ret=+8.9%
  - 2021: S=0.24 (weak), ret=+5.5%
  - 2022: S=0.37 (weak), ret=+7.0%
  - 2023: S=0.99 (moderate), ret=+21.6%

## Risk & Drawdown
- Max drawdown: 32.92% over 1078 days (recovered)
- Annualized: return +11.6%, volatility 20.4% (fraction of booksize)
- Hit rate: 31.4% positive days
- Tail shape: skew +0.40, excess kurtosis +16.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 1.88, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +20.57%; worst month: -17.53%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.10
- Sideways: S=0.90
- Bear: S=0.88

## Negated Direction
Best negated: `-rank(rp_css_credit)` S=0.14, F=0.02, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_css_credit)`: S=-0.34, F=-0.08, T=177.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit / close)`: S=-0.18, F=-0.03, T=177.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_credit, 5))`: S=-0.01, F=0.00, T=19.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_credit)` | TOP200 | 0.57 | 0.22 | 32.9% | 100% | mixed |
| `rank(ts_delta(rp_css_credit, 5))` | TOP1000 | 0.34 | 0.18 | 10.7% | 80% | mixed |
| `rank(rp_css_credit)` | TOP3000 | 0.34 | 0.08 | 63.8% | 60% | all-weather |
| `rank(ts_delta(rp_css_credit, 5))` | TOP500 | 0.15 | 0.05 | 15.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- implied_volatility_call_30: -0.108 (weakly negatively correlated)
- fnd6_newqv1300_miiq: -0.105 (weakly negatively correlated)
- min_free_cash_flow_per_share_guidance: -0.105 (weakly negatively correlated)
- free_cash_flow_per_share_max_guidance: -0.105 (weakly negatively correlated)
- fnd6_newa2v1300_mii: -0.104 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
