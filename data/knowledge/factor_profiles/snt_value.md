---
field: snt_value
dataset: socialmedia12
cluster: socialmedia12_analyst_rating
coverage: 1.0
community_alphas: 2526
best_template: ts_mean
best_sharpe: 0.46
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 29
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0678
ann_vol: 0.0327
hit_rate: 0.5093
rolling_sharpe_min: -1.615
rolling_sharpe_max: 2.168
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: 0.08
---
# snt_value (socialmedia12)

*Negative sentiment score/indicator for current day, with missing values filled as 0*

## Signal Profile
- `rank(snt_value)`: S=0.29, F=0.04, T=55.6%, INFERIOR (TOP1000)
- `rank(ts_delta(snt_value, 5))`: S=-0.04, F=0.00, T=68.9%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(snt_value), 5)`: S=0.31, F=0.06, T=29.9%, INFERIOR (TOP3000)
- `-rank(snt_value)`: S=-0.29, F=-0.04, T=55.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_value, 5))`: S=0.54, F=0.10, T=71.2%, INFERIOR (TOP3000)
- `ts_zscore(snt_value, 22)`: S=0.28, F=0.04, T=58.7%, INFERIOR (TOP3000)
- `ts_mean(snt_value, 10)`: S=0.46, F=0.24, T=19.1%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_value, 22))`: S=0.04, F=0.00, T=63.5%, INFERIOR (TOP3000)
- `rank(-1 * snt_value)`: S=0.17, F=0.02, T=56.4%, INFERIOR (TOP3000)
- `rank(-1 * snt_value / close)`: S=-0.05, F=0.00, T=55.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/28P
- HIGH_TURNOVER: 7F/22P
- LOW_FITNESS: 29F/0P
- LOW_SHARPE: 29F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/17P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 0.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.13 (moderate), ret=+2.5%
  - 2020: S=0.28 (weak), ret=+1.0%
  - 2021: S=-0.76 (negative), ret=-2.7%
  - 2022: S=1.03 (moderate), ret=+3.3%
  - 2023: S=0.29 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 6.78% over 1296 days (not yet recovered, ongoing at window end)
- Annualized: return +1.0%, volatility 3.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.14, excess kurtosis +2.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.17, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +2.72%; worst month: -2.98%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.02
- Sideways: S=-0.10
- Bear: S=0.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_value, 5))` S=0.54, F=0.10, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_value)`: S=0.17, F=0.02, T=56.4%, INFERIOR (TOP3000)
- `rank(-1 * snt_value / close)`: S=-0.05, F=0.00, T=55.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_value, 5))`: S=0.54, F=0.10, T=71.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(snt_value), 5)` | TOP3000 | 0.31 | 0.06 | 6.8% | 80% | mixed |
| `rank(snt_value)` | TOP1000 | 0.29 | 0.04 | 8.1% | 60% | mixed |
| `rank(snt_value)` | TOP3000 | 0.25 | 0.03 | 6.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_qf_az_div_number: 0.496 (moderately positively correlated)
- anl4_qfd1_az_div_number: 0.496 (moderately positively correlated)
- fn_oth_comp_fair_value_a: 0.489 (moderately positively correlated)
- fnd2_propplteqmuflmblgland: 0.480 (moderately positively correlated)
- cap: -0.479 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: rank_value_norm, trade_when
