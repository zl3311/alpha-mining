---
field: fnd2_a_consinprogressg
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.96
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.084
ann_vol: 0.0653
hit_rate: 0.4874
rolling_sharpe_min: -0.847
rolling_sharpe_max: 2.058
redundancy_cluster: 1
negated_best_sharpe: 0.96
negated_best_template: rank_neg_delta
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: 0.28
---
# fnd2_a_consinprogressg (fundamental2)

*Amount of structure or a modification to a structure under construction. Includes recently completed structures or modifications to structures that have not been placed into service.*

## Signal Profile
- `rank(fnd2_a_consinprogressg)`: S=0.33, F=0.16, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_consinprogressg / close)`: S=0.56, F=0.30, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_consinprogressg, 5))`: S=-0.78, F=-0.60, T=26.4%, INFERIOR (TOP200)
- `-rank(fnd2_a_consinprogressg)`: S=-0.18, F=-0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_consinprogressg, 5))`: S=0.96, F=0.71, T=32.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_consinprogressg, 63)`: S=0.68, F=0.64, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_consinprogressg, 10)`: S=0.16, F=0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_consinprogressg, 22))`: S=-0.39, F=-0.22, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_consinprogressg)`: S=0.07, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_consinprogressg / close)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.58 (negative), ret=-2.7%
  - 2020: S=0.75 (moderate), ret=+5.6%
  - 2021: S=1.12 (moderate), ret=+8.8%
  - 2022: S=0.13 (weak), ret=+0.8%
  - 2023: S=1.01 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 8.40% over 451 days (recovered)
- Annualized: return +3.6%, volatility 6.5% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.24, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 2.06, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.73%; worst month: -3.44%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.01
- Sideways: S=0.42
- Bear: S=-0.87

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_consinprogressg, 5))` S=0.96, F=0.71, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_consinprogressg)`: S=0.07, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_consinprogressg / close)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_consinprogressg, 5))`: S=0.96, F=0.71, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_consinprogressg / close)` | TOP3000 | 0.56 | 0.30 | 8.4% | 80% | bull-only |
| `rank(fnd2_a_consinprogressg)` | TOP3000 | 0.33 | 0.16 | 26.3% | 80% | bull-only |
| `rank(fnd2_a_consinprogressg / close)` | TOP1000 | 0.24 | 0.10 | 19.9% | 60% | bull-only |
| `rank(fnd2_a_consinprogressg)` | TOP1000 | 0.18 | 0.07 | 39.7% | 60% | bull-only |
| `rank(fnd2_a_consinprogressg)` | TOP200 | 0.07 | 0.03 | 56.8% | 60% | bull-only |
| `rank(fnd2_a_consinprogressg / close)` | TOP500 | 0.07 | 0.02 | 32.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- est_capex: 0.864 (strongly positively correlated)
- fnd6_mfma1_capx: 0.860 (strongly positively correlated)
- capex: 0.859 (strongly positively correlated)
- est_tot_assets: 0.859 (strongly positively correlated)
- fnd6_newa1v1300_capx: 0.859 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
