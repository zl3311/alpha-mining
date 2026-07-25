---
field: fn_derivative_notional_amount_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0535
ann_vol: 0.0449
hit_rate: 0.5101
rolling_sharpe_min: -0.801
rolling_sharpe_max: 2.11
top_merge_partner: anl4_capex_high
redundancy_cluster: 1
negated_best_sharpe: 0.53
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.39
---
# fn_derivative_notional_amount_a (fundamental2)

*Nominal or face amount used to calculate payments on the derivative liability.*

## Signal Profile
- `rank(fn_derivative_notional_amount_a)`: S=0.10, F=0.02, T=0.6%, INFERIOR (TOP3000)
- `rank(fn_derivative_notional_amount_a / close)`: S=0.92, F=0.53, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_notional_amount_a, 5))`: S=0.33, F=0.12, T=33.5%, INFERIOR (TOP3000)
- `-rank(fn_derivative_notional_amount_a)`: S=0.06, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_notional_amount_a, 5))`: S=0.10, F=0.02, T=28.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_derivative_notional_amount_a, 63)`: S=0.18, F=0.09, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_notional_amount_a, 10)`: S=0.19, F=0.08, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_notional_amount_a, 22))`: S=0.42, F=0.20, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_a)`: S=0.53, F=0.33, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_a / close)`: S=0.39, F=0.21, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.25 (moderate), ret=+3.9%
  - 2020: S=1.07 (moderate), ret=+6.7%
  - 2021: S=0.58 (moderate), ret=+2.4%
  - 2022: S=1.34 (moderate), ret=+5.4%
  - 2023: S=0.48 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 5.35% over 568 days (recovered)
- Annualized: return +4.1%, volatility 4.5% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.62, excess kurtosis +3.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.11, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +3.35%; worst month: -2.37%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.53
- Sideways: S=1.10
- Bear: S=-0.82

## Negated Direction
Best negated: `rank(-1 * fn_derivative_notional_amount_a)` S=0.53, F=0.33, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_derivative_notional_amount_a)`: S=0.53, F=0.33, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_notional_amount_a / close)`: S=0.39, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_notional_amount_a, 5))`: S=0.10, F=0.02, T=28.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_derivative_notional_amount_a / close)` | TOP3000 | 0.92 | 0.53 | 5.3% | 100% | bull-only |
| `rank(ts_delta(fn_derivative_notional_amount_a, 5))` | TOP1000 | 0.33 | 0.12 | 18.8% | 80% | weak |
| `rank(ts_delta(fn_derivative_notional_amount_a, 5))` | TOP3000 | 0.35 | 0.12 | 20.0% | 60% | bull-only |
| `rank(fn_derivative_notional_amount_a / close)` | TOP1000 | 0.15 | 0.04 | 10.8% | 60% | bull-only |
| `rank(fn_derivative_notional_amount_a)` | TOP3000 | 0.08 | 0.02 | 14.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_derivative_notional_amount_q: 0.926 (strongly positively correlated)
- fn_interest_paid_net_a: 0.827 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.826 (strongly positively correlated)
- fnd6_intpn: 0.825 (strongly positively correlated)
- fnd2_a_blgandiprtsg: 0.809 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_capex_high | analyst4 | -0.19 | 1.45 | +0.52 | +0.11 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.19 | 1.59 | +0.43 | -0.65 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.68 | +0.50 | +0.13 | yes |
| anl4_netprofita_std | analyst4 | -0.01 | 1.28 | +0.37 | -0.79 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.36 | +0.45 | +0.37 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
