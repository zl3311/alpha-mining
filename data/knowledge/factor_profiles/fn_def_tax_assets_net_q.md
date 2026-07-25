---
field: fn_def_tax_assets_net_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.71
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0681
ann_vol: 0.052
hit_rate: 0.4947
rolling_sharpe_min: -1.592
rolling_sharpe_max: 2.733
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.5
---
# fn_def_tax_assets_net_q (fundamental2)

*Deferred Tax Assets Net Of Valuation Allowance*

## Signal Profile
- `rank(fn_def_tax_assets_net_q)`: S=0.32, F=0.15, T=1.3%, INFERIOR (TOP500)
- `rank(fn_def_tax_assets_net_q / close)`: S=0.71, F=0.38, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_tax_assets_net_q, 5))`: S=0.18, F=0.08, T=15.2%, INFERIOR (TOP200)
- `-rank(fn_def_tax_assets_net_q)`: S=-0.24, F=-0.08, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_net_q, 5))`: S=-0.21, F=-0.11, T=15.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_tax_assets_net_q, 63)`: S=0.39, F=0.33, T=8.8%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_assets_net_q, 10)`: S=0.54, F=0.37, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_assets_net_q, 22))`: S=0.35, F=0.20, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_q)`: S=0.21, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_q / close)`: S=0.12, F=0.04, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.6%
  - 2020: S=0.48 (weak), ret=+3.5%
  - 2021: S=1.75 (strong), ret=+8.4%
  - 2022: S=1.68 (strong), ret=+8.3%
  - 2023: S=-0.49 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 6.81% over 462 days (recovered)
- Annualized: return +3.6%, volatility 5.2% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.74, excess kurtosis +4.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.73, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.53%; worst month: -2.79%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.45
- Sideways: S=-0.09
- Bear: S=-0.45

## Negated Direction
Best negated: `rank(-1 * fn_def_tax_assets_net_q)` S=0.21, F=0.09, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_def_tax_assets_net_q)`: S=0.21, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_q / close)`: S=0.12, F=0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_net_q, 5))`: S=-0.21, F=-0.11, T=15.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_assets_net_q / close)` | TOP3000 | 0.70 | 0.38 | 6.8% | 60% | mixed |
| `rank(fn_def_tax_assets_net_q / close)` | TOP500 | 0.53 | 0.32 | 16.8% | 60% | bull-only |
| `rank(fn_def_tax_assets_net_q / close)` | TOP1000 | 0.51 | 0.27 | 11.8% | 60% | bull-only |
| `rank(fn_def_tax_assets_net_q)` | TOP500 | 0.32 | 0.15 | 21.6% | 60% | bull-only |
| `rank(fn_def_tax_assets_net_q)` | TOP3000 | 0.36 | 0.14 | 13.0% | 80% | bull-only |
| `rank(fn_def_tax_assets_net_q)` | TOP1000 | 0.23 | 0.08 | 18.1% | 40% | bull-only |
| `rank(ts_delta(fn_def_tax_assets_net_q, 5))` | TOP200 | 0.18 | 0.08 | 47.9% | 40% | mixed |
| `rank(ts_delta(fn_def_tax_assets_net_q, 5))` | TOP500 | 0.13 | 0.04 | 31.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.845 (strongly positively correlated)
- fnd6_intpn: 0.834 (strongly positively correlated)
- fnd2_a_bnsacqproformarvn: 0.828 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.815 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.812 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
