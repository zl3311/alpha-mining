---
field: rp_ess_price
dataset: news18
best_template: rank_neg_delta
best_sharpe: 1.1
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1672
ann_vol: 0.1174
hit_rate: 0.5126
rolling_sharpe_min: -1.492
rolling_sharpe_max: 1.233
negated_best_sharpe: 1.1
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 4
direction_gap: 0.68
---
# rp_ess_price (news18)

*Event sentiment score of stock price news*

## Signal Profile
- `rank(rp_ess_price)`: S=0.13, F=0.02, T=88.9%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_price, 5))`: S=-0.35, F=-0.05, T=122.0%, INFERIOR (TOP500)
- `-rank(rp_ess_price)`: S=0.25, F=0.03, T=113.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_price, 5))`: S=1.10, F=0.24, T=149.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_price, 63)`: S=0.42, F=0.06, T=117.2%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_price, 10)`: S=-0.21, F=-0.06, T=20.8%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_price, 22))`: S=-0.32, F=-0.04, T=120.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_price)`: S=0.61, F=0.11, T=134.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_price / close)`: S=0.49, F=0.08, T=136.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/19P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+3.5%
  - 2020: S=0.68 (moderate), ret=+8.2%
  - 2021: S=-0.26 (negative), ret=-3.7%
  - 2022: S=0.61 (moderate), ret=+8.4%
  - 2023: S=-1.01 (negative), ret=-7.9%

## Risk & Drawdown
- Max drawdown: 16.72% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +1.7%, volatility 11.7% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -1.06, excess kurtosis +9.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 1.23, latest -1.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +6.93%; worst month: -5.57%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.12
- Sideways: S=-0.11
- Bear: S=0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_ess_price, 5))` S=1.10, F=0.24, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rp_ess_price)`: S=0.61, F=0.11, T=134.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_price / close)`: S=0.49, F=0.08, T=136.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_price, 5))`: S=1.10, F=0.24, T=149.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_price)` | TOP200 | 0.15 | 0.02 | 16.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prchq: -0.534 (moderately negatively correlated)
- fnd6_prch: -0.523 (moderately negatively correlated)
- fnd6_prccq: -0.513 (moderately negatively correlated)
- fnd6_prcc: -0.509 (moderately negatively correlated)
- fnd6_prcl: -0.409 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
