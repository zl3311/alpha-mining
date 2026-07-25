---
field: fn_derivative_fair_value_of_derivative_asset_a
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.89
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0325
ann_vol: 0.0345
hit_rate: 0.5223
rolling_sharpe_min: -0.616
rolling_sharpe_max: 2.409
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 34
negated_best_sharpe: 0.49
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.4
---
# fn_derivative_fair_value_of_derivative_asset_a (fundamental2)

*Fair value, before effects of master netting arrangements, of a financial asset or other contract with one or more underlyings, notional amount or payment provision or both, and the contract can be net settled by means outside the contract or delivery of an asset. Includes assets elected not to be offset. Excludes assets not subject to a master netting arrangement.*

## Signal Profile
- `rank(fn_derivative_fair_value_of_derivative_asset_a)`: S=0.44, F=0.16, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_derivative_fair_value_of_derivative_asset_a / close)`: S=1.01, F=0.53, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))`: S=0.80, F=0.48, T=32.1%, INFERIOR (TOP500)
- `-rank(fn_derivative_fair_value_of_derivative_asset_a)`: S=-0.12, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))`: S=-0.09, F=-0.02, T=26.7%, INFERIOR (TOP3000)
- `-ts_zscore(fn_derivative_fair_value_of_derivative_asset_a, 63)`: S=0.30, F=0.16, T=15.4%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_fair_value_of_derivative_asset_a, 10)`: S=0.89, F=0.78, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_fair_value_of_derivative_asset_a, 22))`: S=-0.06, F=-0.01, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_a)`: S=0.49, F=0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_a / close)`: S=0.46, F=0.27, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+1.9%
  - 2020: S=0.82 (moderate), ret=+3.5%
  - 2021: S=1.42 (moderate), ret=+4.8%
  - 2022: S=0.95 (moderate), ret=+3.3%
  - 2023: S=1.36 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 3.25% over 119 days (recovered)
- Annualized: return +3.5%, volatility 3.5% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.56, excess kurtosis +2.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.62, max 2.41, latest 1.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +2.90%; worst month: -1.72%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.40
- Sideways: S=0.96
- Bear: S=-0.40

## Negated Direction
Best negated: `rank(-1 * fn_derivative_fair_value_of_derivative_asset_a)` S=0.49, F=0.29, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_a)`: S=0.49, F=0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_a / close)`: S=0.46, F=0.27, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))`: S=-0.09, F=-0.02, T=26.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_derivative_fair_value_of_derivative_asset_a / close)` | TOP3000 | 1.01 | 0.53 | 3.2% | 100% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))` | TOP500 | 0.81 | 0.48 | 15.1% | 100% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_asset_a / close)` | TOP1000 | 0.45 | 0.19 | 6.2% | 40% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_asset_a)` | TOP3000 | 0.44 | 0.16 | 8.7% | 80% | bull-only |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))` | TOP1000 | 0.21 | 0.06 | 32.3% | 60% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_a, 5))` | TOP200 | 0.08 | 0.02 | 28.1% | 40% | all-weather |

## Correlation Notes
Top correlates:
- fn_derivative_fair_value_of_derivative_asset_q: 0.818 (strongly positively correlated)
- fn_derivative_notional_amount_a: 0.763 (strongly positively correlated)
- fn_derivative_notional_amount_q: 0.717 (strongly positively correlated)
- fnd2_a_blgandiprtsg: 0.711 (strongly positively correlated)
- fnd2_a_ltrmdmrepoplay5: 0.693 (moderately positively correlated)

Redundancy cluster #34: 4 similar fields, mean |rho| 0.713 (representative: fn_derivative_notional_amount_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.18 | 1.69 | +0.53 | +0.61 | yes |
| implied_volatility_call_270 - implied_volatility_put_270 | option8 | -0.21 | 2.29 | +0.48 | -0.08 | yes |
| sales_max_guidance_quarterly | analyst4 | -0.09 | 1.54 | +0.47 | +0.38 | yes |
| anl4_epsr_number | analyst4 | -0.07 | 1.57 | +0.38 | -0.79 | yes |
| anl4_cfo_flag | analyst4 | -0.07 | 1.50 | +0.39 | -0.64 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
