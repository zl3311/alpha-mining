---
field: pretax_income_reported_min_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.71
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1349
ann_vol: 0.0902
hit_rate: 0.5134
rolling_sharpe_min: -1.053
rolling_sharpe_max: 3.158
redundancy_cluster: 40
negated_best_sharpe: 0.71
negated_best_template: neg_rank_level
negated_best_fitness: 0.82
n_negated_sims: 10
direction_gap: 0.1
---
# pretax_income_reported_min_guidance (analyst4)

*Reported Pretax income - minimum guidance value*

## Signal Profile
- `rank(pretax_income_reported_min_guidance)`: S=-0.13, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(pretax_income_reported_min_guidance / close)`: S=0.06, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_reported_min_guidance, 5))`: S=0.61, F=0.25, T=33.7%, INFERIOR (TOP200)
- `-rank(pretax_income_reported_min_guidance)`: S=0.24, F=0.15, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported_min_guidance, 5))`: S=-0.61, F=-0.25, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(pretax_income_reported_min_guidance, 63)`: S=0.14, F=0.03, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_reported_min_guidance, 10)`: S=-0.23, F=-0.14, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_reported_min_guidance, 22))`: S=-0.10, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_min_guidance)`: S=0.71, F=0.82, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_min_guidance / close)`: S=0.24, F=0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+5.6%
  - 2020: S=2.89 (strong), ret=+22.7%
  - 2021: S=-0.02 (negative), ret=-0.2%
  - 2022: S=0.01 (weak), ret=+0.1%
  - 2023: S=-0.03 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 13.49% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.58, excess kurtosis +5.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 3.16, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +6.05%; worst month: -4.29%
Positive months: 61%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.83
- Sideways: S=0.65
- Bear: S=2.43

## Negated Direction
Best negated: `rank(-1 * pretax_income_reported_min_guidance)` S=0.71, F=0.82, INFERIOR
Direction gap: +0.10 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pretax_income_reported_min_guidance)`: S=0.71, F=0.82, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_min_guidance / close)`: S=0.24, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported_min_guidance, 5))`: S=-0.61, F=-0.25, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pretax_income_reported_min_guidance, 5))` | TOP200 | 0.63 | 0.25 | 13.5% | 60% | bear-only |
| `rank(pretax_income_reported_min_guidance / close)` | TOP3000 | 0.06 | 0.02 | 53.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_reported_pretax_income_guidance_2: 0.996 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.985 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.985 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.984 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.983 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
