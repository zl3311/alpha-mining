---
field: rp_nip_price
dataset: news18
best_template: rank_neg_delta
best_sharpe: 0.53
best_fitness: 0.07
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1896
ann_vol: 0.0804
hit_rate: 0.4972
rolling_sharpe_min: -1.554
rolling_sharpe_max: 2.294
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: 0.21
---
# rp_nip_price (news18)

*News impact projection of stock price news*

## Signal Profile
- `rank(rp_nip_price)`: S=0.32, F=0.05, T=91.1%, INFERIOR (TOP200)
- `rank(rp_nip_price / close)`: S=-0.22, F=-0.03, T=98.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_price, 5))`: S=-0.13, F=-0.01, T=125.4%, INFERIOR (TOP500)
- `-rank(rp_nip_price)`: S=0.17, F=0.01, T=114.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_price, 5))`: S=0.53, F=0.07, T=153.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_price, 63)`: S=-0.03, F=0.00, T=120.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_price, 10)`: S=-0.05, F=-0.01, T=19.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_price, 22))`: S=0.32, F=0.03, T=123.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_price)`: S=0.11, F=0.01, T=138.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_price / close)`: S=-0.09, F=-0.01, T=125.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.32, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+6.9%
  - 2020: S=1.48 (moderate), ret=+11.7%
  - 2021: S=-0.50 (negative), ret=-4.8%
  - 2022: S=-0.00 (negative), ret=-0.0%
  - 2023: S=-0.23 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 18.96% over 1106 days (not yet recovered, ongoing at window end)
- Annualized: return +2.5%, volatility 8.0% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew -0.05, excess kurtosis +1.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 2.29, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.29%; worst month: -6.40%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.32
- Sideways: S=0.47
- Bear: S=0.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_price, 5))` S=0.53, F=0.07, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_price)`: S=0.11, F=0.01, T=138.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_price / close)`: S=-0.09, F=-0.01, T=125.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_price, 5))`: S=0.53, F=0.07, T=153.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_price)` | TOP200 | 0.32 | 0.05 | 19.0% | 40% | mixed |

## Correlation Notes
Top correlates:
- rp_nip_equity: 0.350 (weakly positively correlated)
- rp_nip_ptg: 0.320 (weakly positively correlated)
- anl4_cff_value: 0.258 (weakly positively correlated)
- financing_cashflow_reported_value: 0.258 (weakly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.256 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
