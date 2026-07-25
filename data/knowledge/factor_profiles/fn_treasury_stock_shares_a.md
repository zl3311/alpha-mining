---
field: fn_treasury_stock_shares_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.86
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0651
ann_vol: 0.0527
hit_rate: 0.5166
rolling_sharpe_min: -0.31
rolling_sharpe_max: 2.75
top_merge_partner: fnd6_txtubadjust
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.52
---
# fn_treasury_stock_shares_a (fundamental2)

*Number of common and preferred shares that were previously issued and that were repurchased by the issuing entity and held in treasury on the financial statement date. This stock has no voting rights and receives no dividends.*

## Signal Profile
- `rank(fn_treasury_stock_shares_a)`: S=0.49, F=0.22, T=1.3%, INFERIOR (TOP500)
- `rank(fn_treasury_stock_shares_a / close)`: S=0.88, F=0.53, T=1.5%, INFERIOR (TOP500)
- `rank(ts_delta(fn_treasury_stock_shares_a, 5))`: S=0.40, F=0.25, T=18.8%, INFERIOR (TOP200)
- `-rank(fn_treasury_stock_shares_a)`: S=-0.20, F=-0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_treasury_stock_shares_a, 5))`: S=-0.68, F=-0.54, T=18.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_treasury_stock_shares_a, 22)`: S=0.86, F=0.81, T=15.1%, INFERIOR (TOP3000)
- `ts_mean(fn_treasury_stock_shares_a, 10)`: S=0.34, F=0.51, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_treasury_stock_shares_a, 22))`: S=0.41, F=0.24, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_a)`: S=0.34, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_a / close)`: S=0.21, F=0.07, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+3.2%
  - 2020: S=0.58 (moderate), ret=+3.4%
  - 2021: S=0.25 (weak), ret=+1.4%
  - 2022: S=2.42 (strong), ret=+14.5%
  - 2023: S=0.01 (weak), ret=+0.0%

## Risk & Drawdown
- Max drawdown: 6.51% over 290 days (recovered)
- Annualized: return +4.6%, volatility 5.3% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.30, excess kurtosis +1.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.31, max 2.75, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.76%; worst month: -2.63%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.33
- Sideways: S=-0.05
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * fn_treasury_stock_shares_a)` S=0.34, F=0.15, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_treasury_stock_shares_a)`: S=0.34, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_a / close)`: S=0.21, F=0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_treasury_stock_shares_a, 5))`: S=-0.68, F=-0.54, T=18.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_treasury_stock_shares_a / close)` | TOP500 | 0.87 | 0.53 | 6.5% | 100% | mixed |
| `rank(fn_treasury_stock_shares_a / close)` | TOP3000 | 0.84 | 0.44 | 6.6% | 80% | bull-only |
| `rank(fn_treasury_stock_shares_a / close)` | TOP1000 | 0.54 | 0.26 | 7.6% | 80% | mixed |
| `rank(ts_delta(fn_treasury_stock_shares_a, 5))` | TOP200 | 0.40 | 0.25 | 39.4% | 60% | weak |
| `rank(fn_treasury_stock_shares_a)` | TOP500 | 0.48 | 0.22 | 11.7% | 80% | bull-only |
| `rank(ts_delta(fn_treasury_stock_shares_a, 5))` | TOP3000 | 0.40 | 0.18 | 22.6% | 60% | mixed |
| `rank(fn_treasury_stock_shares_a)` | TOP3000 | 0.41 | 0.17 | 12.2% | 60% | bull-only |
| `rank(fn_treasury_stock_shares_a)` | TOP1000 | 0.18 | 0.06 | 12.4% | 60% | bull-only |
| `rank(ts_delta(fn_treasury_stock_shares_a, 5))` | TOP500 | 0.09 | 0.02 | 36.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cstkq: 0.567 (moderately positively correlated)
- fnd6_newa1v1300_cstk: 0.564 (moderately positively correlated)
- anl4_af_div_value: 0.561 (moderately positively correlated)
- fnd6_loxdr: 0.560 (moderately positively correlated)
- fn_treasury_stock_shares_q: 0.559 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.31 | 1.41 | +0.54 | -0.55 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.52 | +0.49 | -0.49 | yes |
| sales_min_guidance_quarterly | analyst4 | -0.20 | 1.34 | +0.47 | -0.60 | yes |
| max_gross_income_guidance | analyst4 | -0.28 | 1.34 | +0.46 | -0.57 | yes |
| min_gross_income_guidance | analyst4 | -0.28 | 1.32 | +0.45 | -0.59 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
