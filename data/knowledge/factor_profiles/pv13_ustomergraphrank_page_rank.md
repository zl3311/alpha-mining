---
field: pv13_ustomergraphrank_page_rank
dataset: pv13
best_template: rank_ts_rank
best_sharpe: 0.91
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1585
ann_vol: 0.0717
hit_rate: 0.4907
rolling_sharpe_min: -1.681
rolling_sharpe_max: 2.322
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.59
---
# pv13_ustomergraphrank_page_rank (pv13)

*the PageRank of customers*

## Signal Profile
- `rank(pv13_ustomergraphrank_page_rank)`: S=0.41, F=0.20, T=1.0%, INFERIOR (TOP3000)
- `rank(pv13_ustomergraphrank_page_rank / close)`: S=0.33, F=0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_ustomergraphrank_page_rank, 5))`: S=0.41, F=0.20, T=15.6%, INFERIOR (TOP200)
- `-rank(pv13_ustomergraphrank_page_rank)`: S=-0.35, F=-0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_page_rank, 5))`: S=0.29, F=0.12, T=15.4%, INFERIOR (TOP3000)
- `ts_zscore(pv13_ustomergraphrank_page_rank, 22)`: S=0.43, F=0.14, T=21.3%, INFERIOR (TOP3000)
- `ts_mean(pv13_ustomergraphrank_page_rank, 10)`: S=0.01, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_ustomergraphrank_page_rank, 22))`: S=0.91, F=0.49, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_page_rank)`: S=0.32, F=0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_page_rank / close)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/17P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/9P
- LOW_TURNOVER: 1F/24P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.02 (strong), ret=+8.1%
  - 2020: S=-0.20 (negative), ret=-1.3%
  - 2021: S=0.74 (moderate), ret=+7.9%
  - 2022: S=-0.18 (negative), ret=-1.3%
  - 2023: S=0.43 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 15.85% over 517 days (recovered)
- Annualized: return +3.2%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew -0.21, excess kurtosis +4.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.32, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +6.69%; worst month: -6.25%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.35
- Sideways: S=1.43
- Bear: S=-1.57

## Negated Direction
Best negated: `rank(-1 * pv13_ustomergraphrank_page_rank)` S=0.32, F=0.19, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_ustomergraphrank_page_rank)`: S=0.32, F=0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ustomergraphrank_page_rank / close)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ustomergraphrank_page_rank, 5))`: S=0.29, F=0.12, T=15.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_ustomergraphrank_page_rank, 5))` | TOP200 | 0.40 | 0.20 | 11.8% | 60% | bull-only |
| `rank(pv13_ustomergraphrank_page_rank)` | TOP3000 | 0.41 | 0.20 | 21.0% | 80% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_page_rank, 5))` | TOP500 | 0.44 | 0.20 | 15.8% | 60% | bull-only |
| `rank(pv13_ustomergraphrank_page_rank)` | TOP1000 | 0.34 | 0.17 | 24.3% | 80% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_page_rank, 5))` | TOP1000 | 0.19 | 0.06 | 14.9% | 60% | bull-only |
| `rank(ts_delta(pv13_ustomergraphrank_page_rank, 5))` | TOP3000 | 0.17 | 0.05 | 20.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pv13_ustomergraphrank_auth_rank: 0.632 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.603 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.603 (moderately positively correlated)
- min_total_assets_guidance: 0.603 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.603 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
