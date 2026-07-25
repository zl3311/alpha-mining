---
field: fn_debt_instrument_carrying_amount_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.26
best_fitness: 1.44
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0726
ann_vol: 0.0537
hit_rate: 0.5036
rolling_sharpe_min: -1.568
rolling_sharpe_max: 2.55
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 1.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.92
n_negated_sims: 10
direction_gap: -0.07
---
# fn_debt_instrument_carrying_amount_a (fundamental2)

*Debt carrying amount*

## Signal Profile
- `rank(fn_debt_instrument_carrying_amount_a)`: S=0.41, F=0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_carrying_amount_a / close)`: S=0.82, F=0.49, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_debt_instrument_carrying_amount_a, 5))`: S=-0.21, F=-0.08, T=22.0%, INFERIOR (TOP500)
- `-rank(fn_debt_instrument_carrying_amount_a)`: S=-0.31, F=-0.13, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_a, 5))`: S=1.19, F=0.92, T=23.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_instrument_carrying_amount_a, 63)`: S=1.26, F=1.44, T=15.6%, AVERAGE (TOP3000)
- `ts_mean(fn_debt_instrument_carrying_amount_a, 10)`: S=0.52, F=0.26, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_carrying_amount_a, 22))`: S=0.04, F=0.01, T=10.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_a)`: S=-0.41, F=-0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_a / close)`: S=-0.82, F=-0.49, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 23F/6P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.49 (weak), ret=+1.7%
  - 2020: S=0.97 (moderate), ret=+6.7%
  - 2021: S=1.37 (moderate), ret=+8.5%
  - 2022: S=1.01 (moderate), ret=+4.9%
  - 2023: S=-0.09 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 7.26% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +4.4%, volatility 5.4% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.55, excess kurtosis +2.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.55, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.23%; worst month: -2.64%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.35
- Sideways: S=0.62
- Bear: S=-0.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_a, 5))` S=1.19, F=0.92, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_carrying_amount_a)`: S=-0.41, F=-0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_a / close)`: S=-0.82, F=-0.49, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_a, 5))`: S=1.19, F=0.92, T=23.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_carrying_amount_a / close)` | TOP3000 | 0.81 | 0.49 | 7.3% | 80% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_a / close)` | TOP1000 | 0.75 | 0.47 | 7.7% | 60% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_a / close)` | TOP500 | 0.41 | 0.21 | 14.6% | 60% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_a)` | TOP3000 | 0.40 | 0.19 | 17.9% | 80% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_a)` | TOP1000 | 0.30 | 0.13 | 19.5% | 60% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_a)` | TOP500 | 0.14 | 0.05 | 27.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.927 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_q: 0.926 (strongly positively correlated)
- fnd6_intpn: 0.920 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.916 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.913 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.72 | +0.54 | -0.69 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.37 | +0.48 | -0.36 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.25 | +0.44 | -0.57 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.36 | +0.41 | -0.31 | yes |
| anl4_rd_exp_flag | analyst4 | -0.28 | 1.46 | +0.43 | +0.09 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
