---
field: fn_repayments_of_lt_debt_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.1
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0532
ann_vol: 0.0359
hit_rate: 0.5239
rolling_sharpe_min: -0.758
rolling_sharpe_max: 3.537
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
negated_best_sharpe: 0.65
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: -0.45
---
# fn_repayments_of_lt_debt_q (fundamental2)

*The cash outflow for debt initially having maturity due after 1 year or beyond the normal operating cycle, if longer.*

## Signal Profile
- `rank(fn_repayments_of_lt_debt_q)`: S=0.86, F=0.42, T=1.5%, INFERIOR (TOP3000)
- `rank(fn_repayments_of_lt_debt_q / close)`: S=1.10, F=0.62, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repayments_of_lt_debt_q, 5))`: S=0.32, F=0.11, T=35.8%, INFERIOR (TOP500)
- `-rank(fn_repayments_of_lt_debt_q)`: S=-0.62, F=-0.27, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lt_debt_q, 5))`: S=0.53, F=0.24, T=37.5%, INFERIOR (TOP3000)
- `ts_zscore(fn_repayments_of_lt_debt_q, 22)`: S=0.27, F=0.08, T=31.9%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_lt_debt_q, 10)`: S=-0.33, F=-0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_lt_debt_q, 22))`: S=-0.10, F=-0.02, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_q)`: S=0.65, F=0.38, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_q / close)`: S=0.61, F=0.36, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.08, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+3.4%
  - 2020: S=1.04 (moderate), ret=+5.0%
  - 2021: S=2.67 (strong), ret=+8.0%
  - 2022: S=0.36 (weak), ret=+1.3%
  - 2023: S=0.53 (moderate), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 5.32% over 541 days (recovered)
- Annualized: return +3.9%, volatility 3.6% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.43, excess kurtosis +2.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 3.54, latest 0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +2.76%; worst month: -2.62%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.18
- Sideways: S=1.13
- Bear: S=-0.00

## Negated Direction
Best negated: `rank(-1 * fn_repayments_of_lt_debt_q)` S=0.65, F=0.38, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repayments_of_lt_debt_q)`: S=0.65, F=0.38, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_q / close)`: S=0.61, F=0.36, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lt_debt_q, 5))`: S=0.53, F=0.24, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_lt_debt_q / close)` | TOP3000 | 1.08 | 0.62 | 5.3% | 100% | mixed |
| `rank(fn_repayments_of_lt_debt_q)` | TOP3000 | 0.84 | 0.42 | 5.3% | 80% | bull-only |
| `rank(fn_repayments_of_lt_debt_q)` | TOP1000 | 0.61 | 0.27 | 6.8% | 80% | bull-only |
| `rank(fn_repayments_of_lt_debt_q / close)` | TOP1000 | 0.56 | 0.25 | 5.0% | 100% | bull-only |
| `rank(ts_delta(fn_repayments_of_lt_debt_q, 5))` | TOP500 | 0.30 | 0.11 | 20.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_repayments_of_lt_debt_a: 0.735 (strongly positively correlated)
- fn_interest_paid_net_a: 0.714 (strongly positively correlated)
- fnd6_intpn: 0.699 (moderately positively correlated)
- fnd2_a_flintasgcsrld: 0.697 (moderately positively correlated)
- fn_interest_paid_net_q: 0.696 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.21 | 1.79 | +0.63 | +0.43 | yes |
| anl4_capex_flag | analyst4 | -0.13 | 1.62 | +0.53 | -0.28 | yes |
| anl4_cfo_flag | analyst4 | -0.13 | 1.59 | +0.47 | -0.32 | yes |
| pcr_vol_30 | option9 | -0.09 | 1.63 | +0.50 | +0.28 | yes |
| anl4_epsr_flag | analyst4 | -0.23 | 1.60 | +0.42 | -0.81 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
