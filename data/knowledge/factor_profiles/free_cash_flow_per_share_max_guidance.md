---
field: free_cash_flow_per_share_max_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.48
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.494
ann_vol: 0.1626
hit_rate: 0.4632
rolling_sharpe_min: -1.161
rolling_sharpe_max: 3.136
negated_best_sharpe: 0.48
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.08
---
# free_cash_flow_per_share_max_guidance (analyst4)

*The maximum guidance value for Free Cash Flow Per Share on an annual basis.*

## Signal Profile
- `rank(free_cash_flow_per_share_max_guidance)`: S=0.40, F=0.29, T=3.2%, INFERIOR (TOP500)
- `rank(free_cash_flow_per_share_max_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(free_cash_flow_per_share_max_guidance, 5))`: S=0.54, F=0.21, T=33.7%, INFERIOR (TOP200)
- `-rank(free_cash_flow_per_share_max_guidance)`: S=0.18, F=0.11, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share_max_guidance, 5))`: S=0.27, F=0.06, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(free_cash_flow_per_share_max_guidance, 63)`: S=0.22, F=0.05, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(free_cash_flow_per_share_max_guidance, 10)`: S=-0.53, F=-0.33, T=19.4%, INFERIOR (TOP3000)
- `rank(ts_rank(free_cash_flow_per_share_max_guidance, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_max_guidance)`: S=0.48, F=0.38, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_max_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.47 (moderate), ret=+15.8%
  - 2020: S=-0.43 (negative), ret=-11.0%
  - 2021: S=0.89 (moderate), ret=+15.5%
  - 2022: S=1.37 (moderate), ret=+14.1%
  - 2023: S=-0.48 (negative), ret=-3.3%

## Risk & Drawdown
- Max drawdown: 49.40% over 1103 days (recovered)
- Annualized: return +6.3%, volatility 16.3% (fraction of booksize)
- Hit rate: 46.3% positive days
- Tail shape: skew -1.81, excess kurtosis +49.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 3.14, latest -0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +8.00%; worst month: -10.29%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.00
- Sideways: S=1.22
- Bear: S=-1.23

## Negated Direction
Best negated: `rank(-1 * free_cash_flow_per_share_max_guidance)` S=0.48, F=0.38, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * free_cash_flow_per_share_max_guidance)`: S=0.48, F=0.38, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_max_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share_max_guidance, 5))`: S=0.27, F=0.06, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(free_cash_flow_per_share_max_guidance)` | TOP500 | 0.39 | 0.29 | 49.4% | 60% | bull-only |
| `rank(ts_delta(free_cash_flow_per_share_max_guidance, 5))` | TOP200 | 0.56 | 0.21 | 15.4% | 60% | bear-only |
| `rank(free_cash_flow_per_share_max_guidance)` | TOP200 | 0.09 | 0.04 | 37.9% | 60% | bull-only |
| `rank(free_cash_flow_per_share_max_guidance)` | TOP3000 | 0.04 | 0.02 | 82.0% | 60% | bull-only |
| `rank(free_cash_flow_per_share_max_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cash_flow_per_share_guidance: 1.000 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.637 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.637 (moderately positively correlated)
- min_total_assets_guidance: 0.637 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.637 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
