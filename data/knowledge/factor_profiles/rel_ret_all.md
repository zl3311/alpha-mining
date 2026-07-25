---
field: rel_ret_all
dataset: pv13
best_template: rank_neg_delta
best_sharpe: 1.35
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 25
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.1441
ann_vol: 0.0842
hit_rate: 0.5085
rolling_sharpe_min: -1.548
rolling_sharpe_max: 0.88
negated_best_sharpe: 1.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.91
---
# rel_ret_all (pv13)

*Averaged one-day return of the companies whose product overlapped with the instrument*

## Signal Profile
- `rank(rel_ret_all)`: S=-0.03, F=0.00, T=70.6%, INFERIOR (TOP200)
- `rank(rel_ret_all / close)`: S=-0.47, F=-0.09, T=71.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_ret_all, 5))`: S=0.16, F=0.02, T=75.5%, INFERIOR (TOP200)
- `-rank(rel_ret_all)`: S=0.79, F=0.17, T=71.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_all, 5))`: S=1.35, F=0.33, T=77.7%, INFERIOR (TOP3000)
- `-ts_zscore(rel_ret_all, 63)`: S=0.32, F=0.05, T=69.9%, INFERIOR (TOP3000)
- `ts_mean(rel_ret_all, 10)`: S=0.44, F=0.14, T=23.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_ret_all, 22))`: S=-0.67, F=-0.14, T=71.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_all)`: S=0.89, F=0.18, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_all / close)`: S=0.11, F=0.01, T=72.8%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 23F/2P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 22F/3P
- LOW_SUB_UNIVERSE_SHARPE: 10F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+3.6%
  - 2020: S=-0.37 (negative), ret=-3.0%
  - 2021: S=0.26 (weak), ret=+2.8%
  - 2022: S=-0.19 (negative), ret=-1.7%
  - 2023: S=0.79 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 14.41% over 1004 days (not yet recovered, ongoing at window end)
- Annualized: return +1.5%, volatility 8.4% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.23, excess kurtosis +2.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 0.88, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +6.13%; worst month: -6.32%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.28
- Sideways: S=-0.17
- Bear: S=0.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_ret_all, 5))` S=1.35, F=0.33, INFERIOR
Direction gap: +0.91 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rel_ret_all)`: S=0.89, F=0.18, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_all / close)`: S=0.11, F=0.01, T=72.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_all, 5))`: S=1.35, F=0.33, T=77.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rel_ret_all, 5))` | TOP200 | 0.18 | 0.02 | 14.4% | 60% | weak |

## Correlation Notes
Top correlates:
- rel_ret_comp: 0.351 (weakly positively correlated)
- rel_ret_part: 0.319 (weakly positively correlated)
- unsystematic_risk_last_60_days: 0.104 (weakly positively correlated)
- fnd6_newqv1300_cicurrq: 0.101 (weakly positively correlated)
- correlation_last_60_days_spy: -0.098 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
