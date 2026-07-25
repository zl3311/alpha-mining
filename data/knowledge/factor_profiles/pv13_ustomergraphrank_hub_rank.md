---
field: pv13_ustomergraphrank_hub_rank
dataset: pv13
best_template: rank_ts_rank
best_sharpe: 1.09
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1188
ann_vol: 0.0947
hit_rate: 0.4721
rolling_sharpe_min: -0.889
rolling_sharpe_max: 2.318
redundancy_cluster: 69
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.52
---
# pv13_ustomergraphrank_hub_rank (pv13)

*the HITS hub score of customers*

## Signal Profile
- `rank(pv13_ustomergraphrank_hub_rank)`: S=0.36, F=0.16, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(pv13_ustomergraphrank_hub_rank, 5))`: S=0.75, F=0.51, T=15.5%, INFERIOR (TOP200)
- `-rank(pv13_ustomergraphrank_hub_rank)`: S=0.36, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_hub_rank, 5))`: S=0.25, F=0.08, T=14.7%, INFERIOR (TOP3000)
- `ts_zscore(pv13_ustomergraphrank_hub_rank, 22)`: S=0.13, F=0.03, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(pv13_ustomergraphrank_hub_rank, 10)`: S=-0.11, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_ustomergraphrank_hub_rank, 22))`: S=1.09, F=0.59, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_hub_rank)`: S=0.57, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_hub_rank / close)`: S=0.25, F=0.08, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/16P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/18P
- LOW_TURNOVER: 4F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.42 (negative), ret=-2.2%
  - 2020: S=0.91 (moderate), ret=+9.1%
  - 2021: S=0.72 (moderate), ret=+8.9%
  - 2022: S=1.29 (moderate), ret=+13.3%
  - 2023: S=0.82 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 11.88% over 178 days (recovered)
- Annualized: return +7.0%, volatility 9.5% (fraction of booksize)
- Hit rate: 47.2% positive days
- Tail shape: skew +0.11, excess kurtosis +2.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 2.32, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.37%; worst month: -7.91%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.42
- Sideways: S=-0.22
- Bear: S=-0.54

## Negated Direction
Best negated: `rank(-1 * pv13_ustomergraphrank_hub_rank)` S=0.57, F=0.19, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_ustomergraphrank_hub_rank)`: S=0.57, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_hub_rank / close)`: S=0.25, F=0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_hub_rank, 5))`: S=0.25, F=0.08, T=14.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_ustomergraphrank_hub_rank, 5))` | TOP200 | 0.74 | 0.51 | 11.9% | 80% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_hub_rank, 5))` | TOP3000 | 0.60 | 0.33 | 14.3% | 60% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_hub_rank, 5))` | TOP500 | 0.47 | 0.23 | 21.9% | 80% | bull-only |
| `rank(pv13_ustomergraphrank_hub_rank)` | TOP200 | 0.37 | 0.16 | 11.5% | 60% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_hub_rank, 5))` | TOP1000 | 0.19 | 0.07 | 21.2% | 60% | bull-only |
| `rank(pv13_ustomergraphrank_hub_rank)` | TOP500 | 0.17 | 0.05 | 11.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- pv13_ustomergraphrank_auth_rank: 0.777 (strongly positively correlated)
- fnd6_itcb: 0.646 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.609 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.609 (moderately positively correlated)
- pv13_ustomergraphrank_page_rank: 0.595 (moderately positively correlated)

Redundancy cluster #69: 2 similar fields, mean |rho| 0.777 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
