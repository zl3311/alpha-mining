---
field: rp_ess_society
dataset: news18
best_template: rank_level
best_sharpe: 0.32
best_fitness: 0.05
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.2251
ann_vol: 0.1304
hit_rate: 0.515
rolling_sharpe_min: -1.264
rolling_sharpe_max: 1.645
negated_best_sharpe: 0.25
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.07
---
# rp_ess_society (news18)

*Event sentiment score of society-related news*

## Signal Profile
- `rank(rp_ess_society)`: S=0.32, F=0.05, T=146.4%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_society, 5))`: S=0.08, F=0.01, T=144.7%, INFERIOR (TOP200)
- `-rank(rp_ess_society)`: S=0.25, F=0.04, T=143.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_society, 5))`: S=0.01, F=0.00, T=150.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_society, 63)`: S=-0.07, F=-0.01, T=142.9%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_society, 10)`: S=-0.04, F=0.00, T=28.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_society, 22))`: S=-0.49, F=-0.09, T=146.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_society)`: S=-0.32, F=-0.05, T=146.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_society / close)`: S=-0.73, F=-0.23, T=137.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+8.6%
  - 2020: S=-0.69 (negative), ret=-8.5%
  - 2021: S=0.21 (weak), ret=+2.6%
  - 2022: S=0.46 (weak), ret=+5.7%
  - 2023: S=0.83 (moderate), ret=+11.6%

## Risk & Drawdown
- Max drawdown: 22.51% over 1082 days (recovered)
- Annualized: return +4.1%, volatility 13.0% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.15, excess kurtosis +3.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 1.65, latest 0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +10.34%; worst month: -6.05%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.83
- Sideways: S=0.14
- Bear: S=-0.10

## Negated Direction
Best negated: `-rank(rp_ess_society)` S=0.25, F=0.04, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_society)`: S=-0.32, F=-0.05, T=146.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_society / close)`: S=-0.73, F=-0.23, T=137.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_society, 5))`: S=0.01, F=0.00, T=150.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_society)` | TOP3000 | 0.31 | 0.05 | 22.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_afv4_dts_spe: -0.195 (weakly negatively correlated)
- anl4_epsa_flag: -0.191 (weakly negatively correlated)
- news_pre_vwap: 0.188 (weakly positively correlated)
- fnd2_dfdtxasoprlcarryfwd: -0.188 (weakly negatively correlated)
- news_main_vwap: 0.184 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
