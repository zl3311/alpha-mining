---
field: rp_ess_credit
dataset: news18
best_template: rank_delta
best_sharpe: 0.55
best_fitness: 0.26
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.0449
ann_vol: 0.0464
hit_rate: 0.0211
rolling_sharpe_min: -1.983
rolling_sharpe_max: 2.014
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 4
direction_gap: -0.3
---
# rp_ess_credit (news18)

*Event sentiment score of credit news*

## Signal Profile
- `rank(rp_ess_credit)`: S=0.06, F=0.01, T=174.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_credit, 5))`: S=0.55, F=0.26, T=5.7%, INFERIOR (TOP200)
- `-rank(rp_ess_credit)`: S=0.12, F=0.02, T=146.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_credit, 5))`: S=0.25, F=0.10, T=17.4%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_credit, 22)`: S=-0.06, F=-0.01, T=97.0%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_credit, 10)`: S=-0.23, F=-0.06, T=37.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_credit, 22))`: S=0.04, F=0.00, T=145.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit)`: S=-0.06, F=-0.01, T=174.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit / close)`: S=0.14, F=0.02, T=176.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 12F/8P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.06 (negative), ret=-1.2%
  - 2020: S=1.03 (moderate), ret=+9.6%
  - 2021: S=1.47 (moderate), ret=+2.0%
  - 2022: S=-1.85 (negative), ret=-2.1%
  - 2023: S=1.08 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 4.49% over 351 days (recovered)
- Annualized: return +2.3%, volatility 4.6% (fraction of booksize)
- Hit rate: 2.1% positive days
- Tail shape: skew +18.00, excess kurtosis +483.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.98, max 2.01, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +11.72%; worst month: -3.85%
Positive months: 47%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.48
- Sideways: S=0.94
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_ess_credit, 5))` S=0.25, F=0.10, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_credit)`: S=-0.06, F=-0.01, T=174.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit / close)`: S=0.14, F=0.02, T=176.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_credit, 5))`: S=0.25, F=0.10, T=17.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_credit, 5))` | TOP200 | 0.49 | 0.26 | 4.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- min_free_cash_flow_per_share_guidance: -0.379 (weakly negatively correlated)
- free_cash_flow_per_share_max_guidance: -0.379 (weakly negatively correlated)
- parkinson_volatility_10: -0.193 (weakly negatively correlated)
- fnd2_a_eplsbvdcpcstnrgprg: -0.163 (weakly negatively correlated)
- cashflow_per_share_minimum: 0.158 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
