---
field: rp_nip_product
dataset: news18
best_template: ts_zscore
best_sharpe: 0.57
best_fitness: 0.1
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.2879
ann_vol: 0.0957
hit_rate: 0.5109
rolling_sharpe_min: -1.973
rolling_sharpe_max: 2.075
negated_best_sharpe: 0.46
negated_best_template: neg_rank
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.11
---
# rp_nip_product (news18)

*News impact projection of product and service-related news*

## Signal Profile
- `rank(rp_nip_product)`: S=0.15, F=0.02, T=112.7%, INFERIOR (TOP200)
- `rank(rp_nip_product / close)`: S=-0.20, F=-0.03, T=113.4%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_product, 5))`: S=-0.29, F=-0.04, T=144.8%, INFERIOR (TOP3000)
- `-rank(rp_nip_product)`: S=0.46, F=0.07, T=136.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_product, 5))`: S=0.29, F=0.04, T=144.8%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_product, 63)`: S=0.57, F=0.10, T=134.7%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_product, 10)`: S=-0.60, F=-0.18, T=28.6%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_product, 22))`: S=-0.66, F=-0.12, T=139.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_product)`: S=-0.13, F=-0.01, T=146.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_product / close)`: S=-0.31, F=-0.05, T=128.4%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.85 (strong), ret=+13.9%
  - 2020: S=0.26 (weak), ret=+2.6%
  - 2021: S=-0.24 (negative), ret=-2.7%
  - 2022: S=-1.22 (negative), ret=-11.8%
  - 2023: S=0.76 (moderate), ret=+6.2%

## Risk & Drawdown
- Max drawdown: 28.79% over 1186 days (not yet recovered, ongoing at window end)
- Annualized: return +1.7%, volatility 9.6% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew -0.03, excess kurtosis +1.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 2.08, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +5.45%; worst month: -6.41%
Positive months: 61%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.38
- Sideways: S=0.66
- Bear: S=0.35

## Negated Direction
Best negated: `-rank(rp_nip_product)` S=0.46, F=0.07, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_product)`: S=-0.13, F=-0.01, T=146.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_product / close)`: S=-0.31, F=-0.05, T=128.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_product, 5))`: S=0.29, F=0.04, T=144.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_product)` | TOP200 | 0.18 | 0.02 | 28.8% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_cff_median: 0.270 (weakly positively correlated)
- est_cashflow_fin: 0.269 (weakly positively correlated)
- anl4_cff_low: 0.267 (weakly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.242 (weakly positively correlated)
- fnd6_mibn: -0.240 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
