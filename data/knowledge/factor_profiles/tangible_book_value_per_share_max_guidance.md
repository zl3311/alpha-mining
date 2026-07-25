---
field: tangible_book_value_per_share_max_guidance
dataset: analyst4
best_template: neg_rank
best_sharpe: 1.13
best_fitness: 1.5
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1543
ann_vol: 0.0901
hit_rate: 0.5109
rolling_sharpe_min: -1.052
rolling_sharpe_max: 3.189
redundancy_cluster: 40
negated_best_sharpe: 1.13
negated_best_template: neg_rank
negated_best_fitness: 1.5
n_negated_sims: 10
direction_gap: 0.59
---
# tangible_book_value_per_share_max_guidance (analyst4)

*Tangible Book Value per Share - Maximum guidance value*

## Signal Profile
- `rank(tangible_book_value_per_share_max_guidance)`: S=0.28, F=0.14, T=3.6%, INFERIOR (TOP500)
- `rank(tangible_book_value_per_share_max_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(tangible_book_value_per_share_max_guidance, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(tangible_book_value_per_share_max_guidance)`: S=1.13, F=1.50, T=3.1%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(tangible_book_value_per_share_max_guidance, 5))`: S=0.09, F=0.01, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(tangible_book_value_per_share_max_guidance, 63)`: S=0.16, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(tangible_book_value_per_share_max_guidance, 10)`: S=-0.84, F=-0.59, T=17.8%, INFERIOR (TOP3000)
- `rank(ts_rank(tangible_book_value_per_share_max_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * tangible_book_value_per_share_max_guidance)`: S=0.62, F=0.60, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * tangible_book_value_per_share_max_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+4.2%
  - 2020: S=2.93 (strong), ret=+23.0%
  - 2021: S=-0.23 (negative), ret=-2.4%
  - 2022: S=0.01 (weak), ret=+0.1%
  - 2023: S=-0.03 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 15.43% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.0%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.62, excess kurtosis +5.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 3.19, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.05%; worst month: -5.00%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.95
- Sideways: S=0.69
- Bear: S=2.35

## Negated Direction
Best negated: `-rank(tangible_book_value_per_share_max_guidance)` S=1.13, F=1.50, AVERAGE
Direction gap: +0.59 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * tangible_book_value_per_share_max_guidance)`: S=0.62, F=0.60, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * tangible_book_value_per_share_max_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(tangible_book_value_per_share_max_guidance, 5))`: S=0.09, F=0.01, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(tangible_book_value_per_share_max_guidance, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(tangible_book_value_per_share_max_guidance)` | TOP500 | 0.26 | 0.14 | 32.4% | 60% | bull-only |
| `rank(tangible_book_value_per_share_max_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(tangible_book_value_per_share_max_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_tangible_book_value_per_share_guidance_2: 1.000 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.999 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.998 (strongly positively correlated)
- max_operating_cashflow_guidance: 0.996 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.995 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
