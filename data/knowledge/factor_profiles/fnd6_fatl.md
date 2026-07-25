---
field: fnd6_fatl
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.24
best_fitness: 1.09
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.0869
ann_vol: 0.0783
hit_rate: 0.5012
rolling_sharpe_min: -0.561
rolling_sharpe_max: 2.975
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.74
---
# fnd6_fatl (fundamental6)

*Property, Plant, and Equipment - Leases at Cost*

## Signal Profile
- `rank(fnd6_fatl)`: S=1.12, F=1.05, T=2.0%, AVERAGE (TOP3000)
- `rank(fnd6_fatl / close)`: S=1.24, F=1.09, T=2.3%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_fatl, 5))`: S=0.51, F=0.33, T=26.6%, INFERIOR (TOP200)
- `-rank(fnd6_fatl)`: S=-0.58, F=-0.44, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatl, 5))`: S=0.50, F=0.28, T=42.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fatl, 63)`: S=0.47, F=0.38, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fatl, 10)`: S=0.15, F=0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fatl, 22))`: S=0.19, F=0.07, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatl)`: S=-1.12, F=-1.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatl / close)`: S=-1.24, F=-1.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.24, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.53 (strong), ret=+5.7%
  - 2020: S=1.63 (strong), ret=+14.0%
  - 2021: S=1.90 (strong), ret=+18.0%
  - 2022: S=0.85 (moderate), ret=+6.4%
  - 2023: S=0.45 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 8.69% over 151 days (not yet recovered, ongoing at window end)
- Annualized: return +9.7%, volatility 7.8% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.68, excess kurtosis +2.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.56, max 2.98, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +7.95%; worst month: -4.51%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.34
- Sideways: S=0.44
- Bear: S=0.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fatl, 5))` S=0.50, F=0.28, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fatl)`: S=-1.12, F=-1.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatl / close)`: S=-1.24, F=-1.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatl, 5))`: S=0.50, F=0.28, T=42.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fatl / close)` | TOP3000 | 1.24 | 1.09 | 8.7% | 100% | all-weather |
| `rank(fnd6_fatl)` | TOP3000 | 1.11 | 1.05 | 17.1% | 80% | bull-only |
| `rank(fnd6_fatl / close)` | TOP1000 | 0.70 | 0.53 | 10.6% | 80% | bull-only |
| `rank(fnd6_fatl)` | TOP1000 | 0.57 | 0.44 | 25.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_fatl, 5))` | TOP200 | 0.51 | 0.33 | 37.6% | 80% | mixed |
| `rank(fnd6_fatl / close)` | TOP500 | 0.37 | 0.22 | 15.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_fatl, 5))` | TOP500 | 0.24 | 0.09 | 53.3% | 40% | weak |
| `rank(fnd6_fatl / close)` | TOP200 | 0.17 | 0.08 | 26.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_fatl, 5))` | TOP1000 | 0.20 | 0.07 | 55.0% | 80% | mixed |
| `rank(fnd6_fatl)` | TOP500 | 0.07 | 0.02 | 40.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_a: 0.897 (strongly positively correlated)
- fnd6_xopr: 0.884 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.883 (strongly positively correlated)
- fnd6_xacc: 0.871 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.867 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 2.07 | +0.83 | -0.59 | yes |
| anl4_netprofit_flag | analyst4 | -0.05 | 1.78 | +0.50 | -0.69 | yes |
| est_rd_expense | analyst4 | -0.15 | 1.81 | +0.57 | +0.94 | yes |
| implied_volatility_mean_10 | option8 | -0.03 | 1.73 | +0.49 | -0.29 | yes |
| fn_comp_options_out_weighted_avg_q | fundamental2 | -0.12 | 1.74 | +0.50 | -0.20 | yes |

## Actionability
Already in submitted book (alpha: ['np30Odjd']).
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
