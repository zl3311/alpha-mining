---
field: fnd6_newa1v1300_act
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.62
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3577
ann_vol: 0.1113
hit_rate: 0.5223
rolling_sharpe_min: -3.355
rolling_sharpe_max: 2.647
redundancy_cluster: 13
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.12
---
# fnd6_newa1v1300_act (fundamental6)

*Current Assets - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_act)`: S=0.62, F=0.46, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_act / close)`: S=0.66, F=0.44, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_act, 5))`: S=-0.17, F=-0.05, T=33.8%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_act)`: S=-0.32, F=-0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_act, 5))`: S=0.50, F=0.25, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_act, 63)`: S=0.52, F=0.32, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_act, 10)`: S=0.13, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_act, 22))`: S=0.07, F=0.01, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_act)`: S=-0.13, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_act / close)`: S=-0.36, F=-0.19, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+4.7%
  - 2020: S=-2.01 (negative), ret=-16.8%
  - 2021: S=1.01 (moderate), ret=+16.6%
  - 2022: S=1.79 (strong), ret=+22.1%
  - 2023: S=0.84 (moderate), ret=+7.3%

## Risk & Drawdown
- Max drawdown: 35.77% over 819 days (recovered)
- Annualized: return +6.9%, volatility 11.1% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.05, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.35, max 2.65, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.37%; worst month: -6.80%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.13
- Sideways: S=1.26
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_act, 5))` S=0.50, F=0.25, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_act)`: S=-0.13, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_act / close)`: S=-0.36, F=-0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_act, 5))`: S=0.50, F=0.25, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_act)` | TOP3000 | 0.62 | 0.46 | 35.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_act / close)` | TOP3000 | 0.66 | 0.44 | 9.0% | 100% | mixed |
| `rank(fnd6_newa1v1300_act / close)` | TOP1000 | 0.43 | 0.25 | 12.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_act / close)` | TOP500 | 0.36 | 0.19 | 20.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_act)` | TOP1000 | 0.31 | 0.18 | 34.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_act)` | TOP500 | 0.13 | 0.05 | 49.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptmfmq_actq: 0.993 (strongly positively correlated)
- assets_curr: 0.993 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.993 (strongly positively correlated)
- fnd6_newqv1300_acoq: 0.978 (strongly positively correlated)
- invested_capital: 0.977 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
