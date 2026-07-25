---
field: fnd2_a_bnsacqproformarvn
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.13
best_fitness: 0.89
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0717
ann_vol: 0.0691
hit_rate: 0.5012
rolling_sharpe_min: -0.838
rolling_sharpe_max: 2.568
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.44
---
# fnd2_a_bnsacqproformarvn (fundamental2)

*The pro forma revenue for a period as if the business combination or combinations had been completed at the beginning of the period.*

## Signal Profile
- `rank(fnd2_a_bnsacqproformarvn)`: S=0.66, F=0.44, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_bnsacqproformarvn / close)`: S=1.13, F=0.89, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_bnsacqproformarvn, 5))`: S=-0.33, F=-0.16, T=28.4%, INFERIOR (TOP3000)
- `-rank(fnd2_a_bnsacqproformarvn)`: S=-0.45, F=-0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_bnsacqproformarvn, 5))`: S=0.69, F=0.58, T=16.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_bnsacqproformarvn, 63)`: S=0.83, F=0.84, T=6.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_bnsacqproformarvn, 10)`: S=-0.10, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_bnsacqproformarvn, 22))`: S=-0.57, F=-0.52, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_bnsacqproformarvn)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_bnsacqproformarvn / close)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.7%
  - 2020: S=1.15 (moderate), ret=+10.7%
  - 2021: S=1.08 (moderate), ret=+8.0%
  - 2022: S=2.09 (strong), ret=+13.1%
  - 2023: S=1.00 (moderate), ret=+4.6%

## Risk & Drawdown
- Max drawdown: 7.17% over 233 days (recovered)
- Annualized: return +7.8%, volatility 6.9% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.60, excess kurtosis +3.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.57, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.03%; worst month: -3.38%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.53
- Sideways: S=0.64
- Bear: S=0.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_bnsacqproformarvn, 5))` S=0.69, F=0.58, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_bnsacqproformarvn)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_bnsacqproformarvn / close)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_bnsacqproformarvn, 5))`: S=0.69, F=0.58, T=16.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_bnsacqproformarvn / close)` | TOP3000 | 1.12 | 0.89 | 7.2% | 100% | mixed |
| `rank(fnd2_a_bnsacqproformarvn)` | TOP3000 | 0.65 | 0.44 | 21.1% | 80% | bull-only |
| `rank(fnd2_a_bnsacqproformarvn / close)` | TOP1000 | 0.60 | 0.40 | 13.8% | 80% | bull-only |
| `rank(fnd2_a_bnsacqproformarvn)` | TOP1000 | 0.44 | 0.27 | 30.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.903 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.897 (strongly positively correlated)
- fnd6_intpn: 0.884 (strongly positively correlated)
- fnd6_xopr: 0.882 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.878 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.97 | +0.80 | -0.01 | yes |
| est_rd_expense | analyst4 | -0.13 | 1.69 | +0.57 | -0.12 | yes |
| anl4_cfo_flag | analyst4 | -0.05 | 1.62 | +0.50 | -0.69 | yes |
| anl4_capex_high | analyst4 | -0.19 | 1.61 | +0.49 | -0.75 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.67 | +0.55 | -0.15 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
