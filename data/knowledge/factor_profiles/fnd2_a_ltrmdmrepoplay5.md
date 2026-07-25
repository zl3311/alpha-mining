---
field: fnd2_a_ltrmdmrepoplay5
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.94
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0658
ann_vol: 0.0481
hit_rate: 0.5077
rolling_sharpe_min: -1.084
rolling_sharpe_max: 2.777
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 34
negated_best_sharpe: 0.67
negated_best_template: neg_rank_level
negated_best_fitness: 0.49
n_negated_sims: 10
direction_gap: -0.27
---
# fnd2_a_ltrmdmrepoplay5 (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing after the 5th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepoplay5)`: S=0.07, F=0.01, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepoplay5 / close)`: S=0.94, F=0.56, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepoplay5, 5))`: S=0.16, F=0.04, T=33.7%, INFERIOR (TOP3000)
- `-rank(fnd2_a_ltrmdmrepoplay5)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplay5, 5))`: S=-0.05, F=-0.01, T=24.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_ltrmdmrepoplay5, 63)`: S=0.18, F=0.09, T=12.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepoplay5, 10)`: S=0.28, F=0.11, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepoplay5, 22))`: S=-0.15, F=-0.05, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplay5)`: S=0.67, F=0.49, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplay5 / close)`: S=0.54, F=0.35, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.93, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.00 (moderate), ret=+3.8%
  - 2020: S=1.36 (moderate), ret=+7.9%
  - 2021: S=1.52 (strong), ret=+7.4%
  - 2022: S=0.26 (weak), ret=+1.2%
  - 2023: S=0.37 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 6.58% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +4.5%, volatility 4.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.40, excess kurtosis +2.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.78, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.84%; worst month: -3.08%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=0.75
- Bear: S=-0.87

## Negated Direction
Best negated: `rank(-1 * fnd2_a_ltrmdmrepoplay5)` S=0.67, F=0.49, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepoplay5)`: S=0.67, F=0.49, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplay5 / close)`: S=0.54, F=0.35, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplay5, 5))`: S=-0.05, F=-0.01, T=24.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_ltrmdmrepoplay5 / close)` | TOP3000 | 0.93 | 0.56 | 6.6% | 100% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplay5 / close)` | TOP1000 | 0.58 | 0.31 | 7.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplay5, 5))` | TOP3000 | 0.17 | 0.04 | 47.4% | 60% | mixed |
| `rank(fnd2_a_ltrmdmrepoplay5 / close)` | TOP500 | 0.10 | 0.03 | 10.1% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplay5, 5))` | TOP500 | 0.12 | 0.02 | 39.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_debt_instrument_carrying_amount_a: 0.786 (strongly positively correlated)
- fnd6_intpn: 0.764 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.759 (strongly positively correlated)
- fn_def_tax_liab_a: 0.757 (strongly positively correlated)
- fn_interest_paid_net_a: 0.756 (strongly positively correlated)

Redundancy cluster #34: 4 similar fields, mean |rho| 0.713 (representative: fn_derivative_notional_amount_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.28 | 1.65 | +0.48 | -0.45 | yes |
| pcr_vol_60 | option9 | -0.06 | 1.30 | +0.38 | -0.91 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.23 | 1.63 | +0.47 | +0.46 | yes |
| rp_ess_revenue | news18 | -0.28 | 1.36 | +0.43 | -0.11 | yes |
| anl4_capex_high | analyst4 | -0.09 | 1.37 | +0.44 | +0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
