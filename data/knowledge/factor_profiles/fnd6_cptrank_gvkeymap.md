---
field: fnd6_cptrank_gvkeymap
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.7
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.1523
ann_vol: 0.0787
hit_rate: 0.498
rolling_sharpe_min: -1.537
rolling_sharpe_max: 3.299
negated_best_sharpe: 0.7
negated_best_template: neg_rank_level
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: 0.08
---
# fnd6_cptrank_gvkeymap (fundamental6)

*technical code for a company, no need to use it for research*

## Signal Profile
- `rank(fnd6_cptrank_gvkeymap)`: S=-0.17, F=-0.04, T=1.1%, INFERIOR (TOP1000)
- `rank(fnd6_cptrank_gvkeymap / close)`: S=0.62, F=0.39, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptrank_gvkeymap, 5))`: S=0.39, F=0.23, T=3.6%, INFERIOR (TOP500)
- `-rank(fnd6_cptrank_gvkeymap)`: S=0.17, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptrank_gvkeymap, 5))`: S=0.16, F=0.06, T=3.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptrank_gvkeymap, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_cptrank_gvkeymap, 10)`: S=-0.21, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptrank_gvkeymap, 22))`: S=-0.23, F=-0.10, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptrank_gvkeymap)`: S=0.70, F=0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptrank_gvkeymap / close)`: S=0.40, F=0.21, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-1.0%
  - 2020: S=2.14 (strong), ret=+21.2%
  - 2021: S=0.22 (weak), ret=+1.9%
  - 2022: S=0.24 (weak), ret=+1.5%
  - 2023: S=0.08 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 15.23% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +4.9%, volatility 7.9% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.52, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 3.30, latest 0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +8.57%; worst month: -5.52%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.65
- Sideways: S=-0.34
- Bear: S=2.70

## Negated Direction
Best negated: `rank(-1 * fnd6_cptrank_gvkeymap)` S=0.70, F=0.46, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptrank_gvkeymap)`: S=0.70, F=0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptrank_gvkeymap / close)`: S=0.40, F=0.21, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptrank_gvkeymap, 5))`: S=0.16, F=0.06, T=3.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptrank_gvkeymap / close)` | TOP3000 | 0.63 | 0.39 | 15.2% | 80% | bear-only |
| `rank(fnd6_cptrank_gvkeymap / close)` | TOP1000 | 0.64 | 0.35 | 9.0% | 60% | mixed |
| `rank(ts_delta(fnd6_cptrank_gvkeymap, 5))` | TOP500 | 0.38 | 0.23 | 26.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptrank_gvkeymap, 5))` | TOP200 | 0.17 | 0.06 | 18.7% | 60% | bull-only |
| `rank(fnd6_cptrank_gvkeymap / close)` | TOP500 | 0.14 | 0.04 | 19.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd2_propplteqmuflmblgland: 0.877 (strongly positively correlated)
- anl4_afv4_div_number: 0.874 (strongly positively correlated)
- anl4_qfd1_az_div_number: 0.873 (strongly positively correlated)
- anl4_qf_az_div_number: 0.873 (strongly positively correlated)
- call_breakeven_360: -0.850 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
