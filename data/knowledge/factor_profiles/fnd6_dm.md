---
field: fnd6_dm
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.0
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1113
ann_vol: 0.0567
hit_rate: 0.5093
rolling_sharpe_min: -2.225
rolling_sharpe_max: 2.902
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 12
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.75
---
# fnd6_dm (fundamental6)

*Debt - Mortgages & Other Secured*

## Signal Profile
- `rank(fnd6_dm)`: S=1.02, F=0.65, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_dm / close)`: S=1.00, F=0.67, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dm, 5))`: S=0.19, F=0.06, T=37.7%, INFERIOR (TOP1000)
- `-rank(fnd6_dm)`: S=-0.19, F=-0.05, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dm, 5))`: S=0.25, F=0.12, T=22.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dm, 63)`: S=0.31, F=0.19, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dm, 10)`: S=0.19, F=0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dm, 22))`: S=0.06, F=0.01, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dm)`: S=-0.27, F=-0.12, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dm / close)`: S=-0.28, F=-0.13, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.1%
  - 2020: S=0.97 (moderate), ret=+8.4%
  - 2021: S=2.10 (strong), ret=+10.9%
  - 2022: S=1.45 (moderate), ret=+6.1%
  - 2023: S=0.60 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 11.13% over 470 days (recovered)
- Annualized: return +5.6%, volatility 5.7% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.65, excess kurtosis +4.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.23, max 2.90, latest 0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.34%; worst month: -2.92%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.02
- Sideways: S=0.05
- Bear: S=0.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dm, 5))` S=0.25, F=0.12, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dm)`: S=-0.27, F=-0.12, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dm / close)`: S=-0.28, F=-0.13, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dm, 5))`: S=0.25, F=0.12, T=22.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dm / close)` | TOP3000 | 0.99 | 0.67 | 11.1% | 80% | all-weather |
| `rank(fnd6_dm)` | TOP3000 | 1.01 | 0.65 | 8.0% | 100% | mixed |
| `rank(fnd6_dm / close)` | TOP200 | 0.28 | 0.13 | 15.0% | 60% | weak |
| `rank(fnd6_dm)` | TOP200 | 0.25 | 0.12 | 14.1% | 60% | weak |
| `rank(fnd6_dm / close)` | TOP1000 | 0.24 | 0.08 | 9.8% | 80% | mixed |
| `rank(ts_delta(fnd6_dm, 5))` | TOP1000 | 0.18 | 0.06 | 30.0% | 60% | mixed |
| `rank(fnd6_dm)` | TOP1000 | 0.17 | 0.05 | 12.4% | 60% | bull-only |
| `rank(fnd6_dm / close)` | TOP500 | 0.11 | 0.03 | 11.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_dlto: 0.862 (strongly positively correlated)
- fnd6_dltp: 0.849 (strongly positively correlated)
- fn_interest_paid_net_q: 0.808 (strongly positively correlated)
- sales_ps: 0.807 (strongly positively correlated)
- fn_interest_paid_net_a: 0.797 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 1.81 | +0.63 | -0.64 | yes |
| anl4_capex_high | analyst4 | -0.17 | 1.49 | +0.50 | -0.28 | yes |
| cashflow_per_share_minimum | analyst4 | -0.15 | 1.42 | +0.42 | -0.89 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.54 | +0.51 | +0.02 | yes |
| est_rd_expense | analyst4 | -0.14 | 1.61 | +0.50 | +0.42 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
