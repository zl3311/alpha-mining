---
field: pv13_ustomergraphrank_auth_rank
dataset: pv13
best_template: rank_delta
best_sharpe: 0.73
best_fitness: 0.48
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1062
ann_vol: 0.0927
hit_rate: 0.4834
rolling_sharpe_min: -1.187
rolling_sharpe_max: 2.351
redundancy_cluster: 69
negated_best_sharpe: 0.14
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.59
---
# pv13_ustomergraphrank_auth_rank (pv13)

*the HITS authority score of customers*

## Signal Profile
- `rank(pv13_ustomergraphrank_auth_rank)`: S=0.44, F=0.24, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_ustomergraphrank_auth_rank, 5))`: S=0.73, F=0.48, T=15.5%, INFERIOR (TOP200)
- `-rank(pv13_ustomergraphrank_auth_rank)`: S=-0.25, F=-0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_auth_rank, 5))`: S=0.05, F=0.01, T=15.9%, INFERIOR (TOP3000)
- `ts_zscore(pv13_ustomergraphrank_auth_rank, 22)`: S=0.50, F=0.17, T=20.0%, INFERIOR (TOP3000)
- `ts_mean(pv13_ustomergraphrank_auth_rank, 10)`: S=0.08, F=0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_ustomergraphrank_auth_rank, 22))`: S=0.06, F=0.01, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_auth_rank)`: S=0.14, F=0.06, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_auth_rank / close)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/16P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.72, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+1.7%
  - 2020: S=0.43 (weak), ret=+4.0%
  - 2021: S=1.29 (moderate), ret=+15.8%
  - 2022: S=0.43 (weak), ret=+4.4%
  - 2023: S=1.02 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 10.62% over 527 days (recovered)
- Annualized: return +6.7%, volatility 9.3% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew -0.03, excess kurtosis +3.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.35, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.94%; worst month: -5.27%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.24
- Sideways: S=0.00
- Bear: S=-0.67

## Negated Direction
Best negated: `rank(-1 * pv13_ustomergraphrank_auth_rank)` S=0.14, F=0.06, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_ustomergraphrank_auth_rank)`: S=0.14, F=0.06, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_auth_rank / close)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_auth_rank, 5))`: S=0.05, F=0.01, T=15.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_ustomergraphrank_auth_rank, 5))` | TOP200 | 0.72 | 0.48 | 10.6% | 100% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_auth_rank, 5))` | TOP500 | 0.57 | 0.30 | 19.6% | 80% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_auth_rank, 5))` | TOP3000 | 0.55 | 0.29 | 20.2% | 80% | bull-only |
| `rank(pv13_ustomergraphrank_auth_rank)` | TOP3000 | 0.43 | 0.24 | 25.4% | 80% | bull-only |
| `rank(pv13_ustomergraphrank_auth_rank)` | TOP1000 | 0.24 | 0.11 | 26.6% | 60% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_auth_rank, 5))` | TOP1000 | 0.17 | 0.06 | 23.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pv13_ustomergraphrank_hub_rank: 0.777 (strongly positively correlated)
- pv13_ustomergraphrank_page_rank: 0.632 (moderately positively correlated)
- fnd6_itcb: 0.630 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.586 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.586 (moderately positively correlated)

Redundancy cluster #69: 2 similar fields, mean |rho| 0.777 (representative: pv13_ustomergraphrank_hub_rank). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
