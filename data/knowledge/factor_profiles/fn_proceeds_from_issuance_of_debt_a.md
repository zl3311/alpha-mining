---
field: fn_proceeds_from_issuance_of_debt_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.2
best_fitness: 0.9
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.0586
ann_vol: 0.0593
hit_rate: 0.502
rolling_sharpe_min: -0.659
rolling_sharpe_max: 2.827
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: -0.32
negated_best_template: rank_neg_delta
negated_best_fitness: -0.11
n_negated_sims: 4
direction_gap: -1.52
---
# fn_proceeds_from_issuance_of_debt_a (fundamental2)

*The cash inflow during the period from additional borrowings in aggregate debt. Includes proceeds from short-term and long-term debt.*

## Signal Profile
- `rank(fn_proceeds_from_issuance_of_debt_a)`: S=0.83, F=0.56, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_proceeds_from_issuance_of_debt_a / close)`: S=1.20, F=0.90, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))`: S=0.41, F=0.16, T=33.6%, INFERIOR (TOP3000)
- `-rank(fn_proceeds_from_issuance_of_debt_a)`: S=-0.38, F=-0.18, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))`: S=-0.32, F=-0.11, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_proceeds_from_issuance_of_debt_a, 63)`: S=-0.08, F=-0.02, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_issuance_of_debt_a, 10)`: S=0.01, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_issuance_of_debt_a, 22))`: S=0.05, F=0.01, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_a)`: S=-0.83, F=-0.56, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_a / close)`: S=-1.20, F=-0.90, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/15P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/16P
- LOW_TURNOVER: 2F/24P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.20, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+2.1%
  - 2020: S=1.02 (moderate), ret=+7.6%
  - 2021: S=1.91 (strong), ret=+12.5%
  - 2022: S=1.13 (moderate), ret=+6.1%
  - 2023: S=1.28 (moderate), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 5.86% over 159 days (recovered)
- Annualized: return +7.1%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.59, excess kurtosis +2.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 2.83, latest 1.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.21%; worst month: -3.01%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.40
- Sideways: S=0.54
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))` S=-0.32, F=-0.11, INFERIOR
Direction gap: -1.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_proceeds_from_issuance_of_debt_a)`: S=-0.83, F=-0.56, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_a / close)`: S=-1.20, F=-0.90, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))`: S=-0.32, F=-0.11, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_issuance_of_debt_a / close)` | TOP3000 | 1.20 | 0.90 | 5.9% | 100% | all-weather |
| `rank(fn_proceeds_from_issuance_of_debt_a)` | TOP3000 | 0.83 | 0.56 | 17.1% | 80% | bull-only |
| `rank(fn_proceeds_from_issuance_of_debt_a / close)` | TOP1000 | 0.70 | 0.44 | 8.4% | 80% | mixed |
| `rank(fn_proceeds_from_issuance_of_debt_a / close)` | TOP500 | 0.35 | 0.18 | 16.6% | 80% | bull-only |
| `rank(fn_proceeds_from_issuance_of_debt_a)` | TOP1000 | 0.37 | 0.18 | 18.7% | 80% | bull-only |
| `rank(ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))` | TOP3000 | 0.43 | 0.16 | 14.8% | 60% | mixed |
| `rank(ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))` | TOP500 | 0.23 | 0.09 | 47.5% | 80% | mixed |
| `rank(ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))` | TOP200 | 0.21 | 0.08 | 59.2% | 40% | mixed |
| `rank(fn_proceeds_from_issuance_of_debt_a / close)` | TOP200 | 0.18 | 0.07 | 30.1% | 80% | bull-only |
| `rank(ts_delta(fn_proceeds_from_issuance_of_debt_a, 5))` | TOP1000 | 0.19 | 0.06 | 31.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_a: 0.898 (strongly positively correlated)
- fnd6_xopr: 0.897 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.895 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.893 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.892 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.97 | +0.78 | -0.58 | yes |
| est_rd_expense | analyst4 | -0.15 | 1.76 | +0.56 | +0.18 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.12 | 1.72 | +0.52 | +0.72 | yes |
| anl4_capex_high | analyst4 | -0.19 | 1.68 | +0.48 | -0.22 | yes |
| implied_volatility_call_20 | option8 | +0.02 | 1.72 | +0.46 | -0.40 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
