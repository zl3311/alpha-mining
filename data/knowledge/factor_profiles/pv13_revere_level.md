---
field: pv13_revere_level
dataset: pv13
best_template: rank_delta
best_sharpe: 0.63
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2721
ann_vol: 0.1013
hit_rate: 0.4607
rolling_sharpe_min: -2.313
rolling_sharpe_max: 3.129
redundancy_cluster: 13
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.14
---
# pv13_revere_level (pv13)

*Level of the sector within the hierarchy*

## Signal Profile
- `rank(pv13_revere_level)`: S=0.22, F=0.11, T=2.8%, INFERIOR (TOP200)
- `rank(pv13_revere_level / close)`: S=-0.35, F=-0.22, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_level, 5))`: S=0.63, F=0.46, T=2.4%, INFERIOR (TOP3000)
- `-rank(pv13_revere_level)`: S=0.46, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_level, 5))`: S=0.49, F=0.36, T=3.3%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_level, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(pv13_revere_level, 10)`: S=-0.32, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_level, 22))`: S=0.49, F=0.37, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_level)`: S=0.46, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_level / close)`: S=0.35, F=0.22, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/13P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/11P
- LOW_TURNOVER: 2F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.42 (negative), ret=-8.8%
  - 2020: S=-1.02 (negative), ret=-8.3%
  - 2021: S=1.43 (moderate), ret=+22.1%
  - 2022: S=2.44 (strong), ret=+25.5%
  - 2023: S=-0.23 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 27.21% over 1055 days (recovered)
- Annualized: return +5.9%, volatility 10.1% (fraction of booksize)
- Hit rate: 46.1% positive days
- Tail shape: skew +0.06, excess kurtosis +3.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.31, max 3.13, latest -0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.79%; worst month: -5.19%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.51
- Sideways: S=-0.10
- Bear: S=-1.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_level, 5))` S=0.49, F=0.36, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_level)`: S=0.46, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_level / close)`: S=0.35, F=0.22, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_level, 5))`: S=0.49, F=0.36, T=3.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_level, 5))` | TOP500 | 0.52 | 0.46 | 27.5% | 60% | bull-only |
| `rank(ts_delta(pv13_revere_level, 5))` | TOP3000 | 0.58 | 0.46 | 27.2% | 40% | bull-only |
| `rank(ts_delta(pv13_revere_level, 5))` | TOP1000 | 0.46 | 0.36 | 33.2% | 40% | bull-only |
| `rank(pv13_revere_level)` | TOP200 | 0.22 | 0.11 | 21.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- pv13_revere_parent: 1.000 (strongly positively correlated)
- max_share_buyback_guidance: 0.859 (strongly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.859 (strongly positively correlated)
- max_total_goodwill_guidance_2: 0.859 (strongly positively correlated)
- min_custom_eps_guidance: 0.859 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
