---
field: rel_num_cust
dataset: pv13
best_template: ts_zscore
best_sharpe: 0.89
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0944
ann_vol: 0.0389
hit_rate: 0.5166
rolling_sharpe_min: -2.033
rolling_sharpe_max: 2.708
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.33
---
# rel_num_cust (pv13)

*number of the instrument's customers*

## Signal Profile
- `rank(rel_num_cust)`: S=0.80, F=0.40, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_num_cust, 5))`: S=0.27, F=0.06, T=35.4%, INFERIOR (TOP500)
- `-rank(rel_num_cust)`: S=-0.10, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_cust, 5))`: S=0.56, F=0.17, T=35.9%, INFERIOR (TOP3000)
- `-ts_zscore(rel_num_cust, 63)`: S=0.89, F=0.50, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(rel_num_cust, 10)`: S=0.12, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_num_cust, 22))`: S=-0.81, F=-0.42, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_cust)`: S=-0.10, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_cust / close)`: S=-0.23, F=-0.07, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/22P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+1.5%
  - 2020: S=-0.78 (negative), ret=-2.1%
  - 2021: S=1.52 (strong), ret=+8.6%
  - 2022: S=1.20 (moderate), ret=+5.6%
  - 2023: S=0.51 (moderate), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 9.44% over 717 days (recovered)
- Annualized: return +3.0%, volatility 3.9% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.19, excess kurtosis +2.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.03, max 2.71, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.83%; worst month: -2.34%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.90
- Bear: S=-2.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_num_cust, 5))` S=0.56, F=0.17, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rel_num_cust)`: S=-0.10, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * rel_num_cust / close)`: S=-0.23, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_num_cust, 5))`: S=0.56, F=0.17, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_num_cust)` | TOP3000 | 0.78 | 0.40 | 9.4% | 80% | bull-only |
| `rank(rel_num_cust)` | TOP500 | 0.19 | 0.07 | 23.6% | 80% | bull-only |
| `rank(ts_delta(rel_num_cust, 5))` | TOP500 | 0.29 | 0.06 | 16.9% | 60% | bear-only |
| `rank(rel_num_cust)` | TOP200 | 0.07 | 0.02 | 30.8% | 80% | bull-only |
| `rank(ts_delta(rel_num_cust, 5))` | TOP200 | 0.15 | 0.02 | 15.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- rel_num_all: 0.851 (strongly positively correlated)
- rel_num_part: 0.836 (strongly positively correlated)
- rel_num_comp: 0.779 (strongly positively correlated)
- anl4_bvps_flag: 0.758 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.745 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
