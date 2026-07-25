---
field: pv13_com_page_rank
dataset: pv13
best_template: rank_level
best_sharpe: 0.68
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2064
ann_vol: 0.0736
hit_rate: 0.5134
rolling_sharpe_min: -2.944
rolling_sharpe_max: 2.701
redundancy_cluster: 13
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.48
---
# pv13_com_page_rank (pv13)

*the PageRank of competitors*

## Signal Profile
- `rank(pv13_com_page_rank)`: S=0.68, F=0.43, T=1.0%, INFERIOR (TOP3000)
- `rank(pv13_com_page_rank / close)`: S=0.52, F=0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_com_page_rank, 5))`: S=0.45, F=0.24, T=16.0%, INFERIOR (TOP200)
- `-rank(pv13_com_page_rank)`: S=-0.32, F=-0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_com_page_rank, 5))`: S=0.20, F=0.07, T=15.2%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_com_page_rank, 63)`: S=0.15, F=0.04, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(pv13_com_page_rank, 10)`: S=0.19, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_com_page_rank, 22))`: S=0.23, F=0.07, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_page_rank)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_page_rank / close)`: S=-0.41, F=-0.24, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/17P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/5P
- LOW_TURNOVER: 1F/24P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+3.1%
  - 2020: S=-1.69 (negative), ret=-8.7%
  - 2021: S=1.36 (moderate), ret=+14.1%
  - 2022: S=1.55 (strong), ret=+14.4%
  - 2023: S=0.26 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 20.64% over 781 days (recovered)
- Annualized: return +4.9%, volatility 7.4% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.02, excess kurtosis +1.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.94, max 2.70, latest 0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.18%; worst month: -3.14%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.66
- Sideways: S=1.22
- Bear: S=-2.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_com_page_rank, 5))` S=0.20, F=0.07, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_com_page_rank)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_page_rank / close)`: S=-0.41, F=-0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_com_page_rank, 5))`: S=0.20, F=0.07, T=15.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_com_page_rank)` | TOP3000 | 0.67 | 0.43 | 20.6% | 80% | bull-only |
| `rank(ts_delta(pv13_com_page_rank, 5))` | TOP200 | 0.44 | 0.24 | 15.4% | 80% | mixed |
| `rank(pv13_com_page_rank)` | TOP1000 | 0.31 | 0.17 | 31.2% | 60% | bull-only |
| `rank(pv13_com_page_rank)` | TOP500 | 0.12 | 0.05 | 47.9% | 60% | bull-only |
| `rank(ts_delta(pv13_com_page_rank, 5))` | TOP1000 | 0.15 | 0.05 | 19.6% | 60% | bull-only |
| `rank(ts_delta(pv13_com_page_rank, 5))` | TOP500 | 0.08 | 0.02 | 25.1% | 80% | bull-only |
| `rank(ts_delta(pv13_com_page_rank, 5))` | TOP3000 | 0.09 | 0.02 | 20.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- invested_capital: 0.950 (strongly positively correlated)
- fnd6_newqv1300_icaptq: 0.950 (strongly positively correlated)
- operating_expense: 0.947 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.947 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.944 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
