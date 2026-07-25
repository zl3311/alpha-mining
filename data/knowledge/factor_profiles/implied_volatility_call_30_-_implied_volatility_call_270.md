---
field: implied_volatility_call_30 - implied_volatility_call_270
dataset: option8
best_template: rank_level
best_sharpe: 0.13
best_fitness: 0.02
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 3
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.2102
ann_vol: 0.0685
hit_rate: 0.4834
rolling_sharpe_min: -1.837
rolling_sharpe_max: 2.912
negated_best_sharpe: -0.07
negated_best_template: neg_rank_level
negated_best_fitness: -0.02
n_negated_sims: 2
direction_gap: -0.2
---
# implied_volatility_call_30 - implied_volatility_call_270 (option8)


## Signal Profile
- `rank(implied_volatility_call_30 - implied_volatility_call_270)`: S=0.13, F=0.02, T=28.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30 - implied_volatility_call_270, 5))`: S=-0.73, F=-0.16, T=59.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_30 - implied_volatility_call_270)`: S=-0.07, F=-0.02, T=10.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/0P
- LOW_FITNESS: 3F/0P
- LOW_SHARPE: 3F/0P
- LOW_SUB_UNIVERSE_SHARPE: 3F/0P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.13, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+1.9%
  - 2020: S=2.13 (strong), ret=+13.3%
  - 2021: S=-1.47 (negative), ret=-9.8%
  - 2022: S=0.10 (weak), ret=+1.0%
  - 2023: S=-0.36 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 21.02% over 1046 days (not yet recovered, ongoing at window end)
- Annualized: return +0.9%, volatility 6.9% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.60, excess kurtosis +5.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.84, max 2.91, latest -0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.96%; worst month: -4.96%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.33
- Sideways: S=-1.27
- Bear: S=1.75

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_30 - implied_volatility_call_270)` S=-0.07, F=-0.02, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_call_30 - implied_volatility_call_270)`: S=-0.07, F=-0.02, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_30 - implied_volatility_call_270, 5))`: S=-0.73, F=-0.16, T=59.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_call_30 - implied_volatility_call_270)` | TOP3000 | 0.13 | 0.02 | 21.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- systematic_risk_last_90_days: 0.722 (strongly positively correlated)
- fnd6_newqv1300_cibegniq: -0.716 (strongly negatively correlated)
- income: -0.711 (strongly negatively correlated)
- fnd6_mfmq_ibcomq: -0.709 (strongly negatively correlated)
- put_breakeven_720: -0.702 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_value_norm, trade_when
