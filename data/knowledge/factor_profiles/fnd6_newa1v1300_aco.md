---
field: fnd6_newa1v1300_aco
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.87
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0692
ann_vol: 0.0644
hit_rate: 0.498
rolling_sharpe_min: -1.123
rolling_sharpe_max: 2.741
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.45
---
# fnd6_newa1v1300_aco (fundamental6)

*Current Assets - Other - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_aco)`: S=0.69, F=0.49, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_aco / close)`: S=0.87, F=0.58, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_aco, 5))`: S=0.41, F=0.15, T=35.4%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_aco)`: S=-0.30, F=-0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aco, 5))`: S=-0.27, F=-0.11, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_aco, 63)`: S=0.28, F=0.12, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aco, 10)`: S=-0.32, F=-0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aco, 22))`: S=0.48, F=0.22, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aco)`: S=0.42, F=0.31, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aco / close)`: S=0.29, F=0.15, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.08 (weak), ret=+0.4%
  - 2020: S=0.46 (weak), ret=+3.1%
  - 2021: S=1.70 (strong), ret=+13.2%
  - 2022: S=1.11 (moderate), ret=+7.3%
  - 2023: S=0.63 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 6.92% over 420 days (recovered)
- Annualized: return +5.6%, volatility 6.4% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.48, excess kurtosis +2.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.74, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.01%; worst month: -3.30%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.51
- Sideways: S=0.16
- Bear: S=-0.46

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_aco)` S=0.42, F=0.31, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aco)`: S=0.42, F=0.31, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aco / close)`: S=0.29, F=0.15, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aco, 5))`: S=-0.27, F=-0.11, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_aco / close)` | TOP3000 | 0.87 | 0.58 | 6.9% | 100% | mixed |
| `rank(fnd6_newa1v1300_aco)` | TOP3000 | 0.69 | 0.49 | 26.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aco / close)` | TOP1000 | 0.50 | 0.28 | 10.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aco)` | TOP1000 | 0.29 | 0.15 | 30.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_aco, 5))` | TOP1000 | 0.42 | 0.15 | 19.0% | 80% | bear-only |
| `rank(fnd6_newa1v1300_aco / close)` | TOP500 | 0.28 | 0.13 | 23.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_aco, 5))` | TOP200 | 0.14 | 0.04 | 56.0% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lco: 0.960 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.957 (strongly positively correlated)
- fnd6_newa1v1300_lse: 0.957 (strongly positively correlated)
- fnd6_mfma1_at: 0.956 (strongly positively correlated)
- fnd6_xopr: 0.953 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.75 | +0.57 | -0.73 | yes |
| rp_ess_revenue | news18 | -0.30 | 1.43 | +0.54 | -0.77 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.24 | 1.30 | +0.43 | -0.94 | yes |
| min_gross_income_guidance | analyst4 | -0.18 | 1.30 | +0.43 | -0.56 | yes |
| max_gross_income_guidance | analyst4 | -0.18 | 1.32 | +0.43 | -0.56 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
