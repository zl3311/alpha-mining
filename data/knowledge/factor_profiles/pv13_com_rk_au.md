---
field: pv13_com_rk_au
dataset: pv13
cluster: pv13_analyst_rating
coverage: 0.9051
community_alphas: 2280
best_template: rank_level
best_sharpe: 0.81
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1629
ann_vol: 0.0641
hit_rate: 0.5231
rolling_sharpe_min: -2.404
rolling_sharpe_max: 2.641
redundancy_cluster: 13
negated_best_sharpe: 0.05
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.76
---
# pv13_com_rk_au (pv13)

*the HITS authority score of competitors*

## Signal Profile
- `rank(pv13_com_rk_au)`: S=0.81, F=0.52, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_com_rk_au, 5))`: S=0.55, F=0.34, T=15.9%, INFERIOR (TOP200)
- `-rank(pv13_com_rk_au)`: S=-0.38, F=-0.21, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_com_rk_au, 5))`: S=0.01, F=0.00, T=15.1%, INFERIOR (TOP3000)
- `ts_zscore(pv13_com_rk_au, 22)`: S=0.71, F=0.35, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(pv13_com_rk_au, 10)`: S=0.10, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_com_rk_au, 22))`: S=-0.14, F=-0.04, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_rk_au)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_rk_au / close)`: S=-0.20, F=-0.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/16P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+3.8%
  - 2020: S=-0.54 (negative), ret=-2.3%
  - 2021: S=1.21 (moderate), ret=+11.9%
  - 2022: S=1.37 (moderate), ret=+9.9%
  - 2023: S=0.38 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 16.29% over 766 days (recovered)
- Annualized: return +5.1%, volatility 6.4% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.15, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.40, max 2.64, latest 0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.39%; worst month: -3.50%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.36
- Sideways: S=0.97
- Bear: S=-1.43

## Negated Direction
Best negated: `rank(-1 * pv13_com_rk_au)` S=0.05, F=0.01, INFERIOR
Direction gap: -0.76 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_com_rk_au)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * pv13_com_rk_au / close)`: S=-0.20, F=-0.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_com_rk_au, 5))`: S=0.01, F=0.00, T=15.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_com_rk_au)` | TOP3000 | 0.79 | 0.52 | 16.3% | 80% | bull-only |
| `rank(ts_delta(pv13_com_rk_au, 5))` | TOP200 | 0.55 | 0.34 | 16.3% | 100% | mixed |
| `rank(pv13_com_rk_au)` | TOP1000 | 0.38 | 0.21 | 28.8% | 80% | bull-only |
| `rank(ts_delta(pv13_com_rk_au, 5))` | TOP1000 | 0.19 | 0.07 | 23.7% | 60% | bull-only |
| `rank(pv13_com_rk_au)` | TOP500 | 0.13 | 0.05 | 41.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pv13_com_page_rank: 0.910 (strongly positively correlated)
- rel_num_all: 0.876 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.869 (strongly positively correlated)
- sga_expense: 0.865 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.865 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
