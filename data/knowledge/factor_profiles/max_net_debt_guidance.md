---
field: max_net_debt_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 1.02
best_fitness: 1.18
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.2186
ann_vol: 0.1648
hit_rate: 0.5206
rolling_sharpe_min: -1.429
rolling_sharpe_max: 3.037
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 35
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.83
---
# max_net_debt_guidance (analyst4)

*The maximum guidance value for Net Debt on an annual basis.*

## Signal Profile
- `rank(max_net_debt_guidance)`: S=1.02, F=1.18, T=1.7%, AVERAGE (TOP3000)
- `rank(max_net_debt_guidance / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_net_debt_guidance, 5))`: S=0.63, F=0.26, T=33.7%, INFERIOR (TOP200)
- `-rank(max_net_debt_guidance)`: S=-0.02, F=-0.01, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_debt_guidance, 5))`: S=0.19, F=0.03, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_net_debt_guidance, 63)`: S=-0.01, F=0.00, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(max_net_debt_guidance, 10)`: S=0.26, F=0.19, T=10.4%, INFERIOR (TOP3000)
- `rank(ts_rank(max_net_debt_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_net_debt_guidance)`: S=-0.46, F=-0.49, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * max_net_debt_guidance / close)`: S=0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+2.5%
  - 2020: S=-0.12 (negative), ret=-2.0%
  - 2021: S=2.04 (strong), ret=+40.5%
  - 2022: S=2.21 (strong), ret=+35.6%
  - 2023: S=0.48 (weak), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 21.86% over 530 days (recovered)
- Annualized: return +16.9%, volatility 16.5% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +1.51, excess kurtosis +13.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.43, max 3.04, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +12.98%; worst month: -10.18%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.97
- Sideways: S=0.62
- Bear: S=0.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_net_debt_guidance, 5))` S=0.19, F=0.03, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_net_debt_guidance)`: S=-0.46, F=-0.49, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * max_net_debt_guidance / close)`: S=0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_debt_guidance, 5))`: S=0.19, F=0.03, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_net_debt_guidance)` | TOP3000 | 1.03 | 1.18 | 21.9% | 80% | all-weather |
| `rank(max_net_debt_guidance)` | TOP500 | 0.42 | 0.47 | 71.5% | 60% | mixed |
| `rank(max_net_debt_guidance)` | TOP200 | 0.38 | 0.42 | 69.6% | 60% | mixed |
| `rank(ts_delta(max_net_debt_guidance, 5))` | TOP200 | 0.65 | 0.26 | 11.9% | 80% | bear-only |
| `rank(max_net_debt_guidance / close)` | TOP3000 | 0.10 | 0.04 | 52.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_net_debt_guidance: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.263 (weakly positively correlated)
- fnd6_newqv1300_epsfiq: 0.263 (weakly positively correlated)
- inventory_turnover: 0.261 (weakly positively correlated)
- fnd6_newqv1300_epspxq: 0.261 (weakly positively correlated)

Redundancy cluster #35: 2 similar fields, mean |rho| 1.0 (representative: min_net_debt_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.17 | 1.54 | +0.51 | -0.60 | yes |
| implied_volatility_call_10 | option8 | -0.10 | 1.50 | +0.46 | -0.60 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.12 | 1.47 | +0.44 | -0.72 | yes |
| sharesout | pv1 | -0.05 | 1.46 | +0.43 | -0.81 | yes |
| fnd6_optex | fundamental6 | -0.17 | 1.46 | +0.43 | -0.67 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
