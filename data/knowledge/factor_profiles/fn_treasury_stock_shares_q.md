---
field: fn_treasury_stock_shares_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.88
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0514
ann_vol: 0.0444
hit_rate: 0.5215
rolling_sharpe_min: -0.689
rolling_sharpe_max: 3.013
top_merge_partner: fnd6_txtubadjust
negated_best_sharpe: 0.52
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.36
---
# fn_treasury_stock_shares_q (fundamental2)

*Number of common and preferred shares that were previously issued and that were repurchased by the issuing entity and held in treasury on the financial statement date. This stock has no voting rights and receives no dividends.*

## Signal Profile
- `rank(fn_treasury_stock_shares_q)`: S=0.41, F=0.18, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_treasury_stock_shares_q / close)`: S=0.88, F=0.49, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_treasury_stock_shares_q, 5))`: S=-0.40, F=-0.20, T=34.1%, INFERIOR (TOP500)
- `-rank(fn_treasury_stock_shares_q)`: S=-0.25, F=-0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_treasury_stock_shares_q, 5))`: S=0.52, F=0.29, T=28.1%, INFERIOR (TOP3000)
- `-ts_zscore(fn_treasury_stock_shares_q, 63)`: S=0.28, F=0.12, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fn_treasury_stock_shares_q, 10)`: S=0.13, F=0.05, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_treasury_stock_shares_q, 22))`: S=-0.34, F=-0.15, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_q)`: S=0.38, F=0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_q / close)`: S=0.24, F=0.10, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+3.2%
  - 2020: S=0.23 (weak), ret=+1.1%
  - 2021: S=0.76 (moderate), ret=+3.6%
  - 2022: S=2.51 (strong), ret=+12.7%
  - 2023: S=-0.53 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 5.14% over 218 days (recovered)
- Annualized: return +3.9%, volatility 4.4% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.16, excess kurtosis +1.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 3.01, latest -0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.46%; worst month: -1.63%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.44
- Sideways: S=0.60
- Bear: S=-0.61

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_treasury_stock_shares_q, 5))` S=0.52, F=0.29, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_treasury_stock_shares_q)`: S=0.38, F=0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_treasury_stock_shares_q / close)`: S=0.24, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_treasury_stock_shares_q, 5))`: S=0.52, F=0.29, T=28.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_treasury_stock_shares_q / close)` | TOP3000 | 0.87 | 0.49 | 5.1% | 80% | bull-only |
| `rank(fn_treasury_stock_shares_q / close)` | TOP1000 | 0.59 | 0.31 | 7.0% | 60% | mixed |
| `rank(fn_treasury_stock_shares_q / close)` | TOP500 | 0.54 | 0.29 | 8.4% | 80% | mixed |
| `rank(fn_treasury_stock_shares_q)` | TOP3000 | 0.41 | 0.18 | 12.3% | 60% | bull-only |
| `rank(fn_treasury_stock_shares_q)` | TOP500 | 0.29 | 0.12 | 14.2% | 60% | bull-only |
| `rank(fn_treasury_stock_shares_q)` | TOP1000 | 0.24 | 0.08 | 14.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.739 (strongly positively correlated)
- fn_ppne_gross_a: 0.735 (strongly positively correlated)
- fn_mne_a: 0.731 (strongly positively correlated)
- fnd2_a_rvndm: 0.729 (strongly positively correlated)
- fnd6_xpr: 0.728 (strongly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.25 | 1.31 | +0.44 | -0.47 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.45 | +0.42 | -0.60 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.21 | 1.58 | +0.42 | -0.51 | yes |
| anl4_epsr_flag | analyst4 | -0.27 | 1.60 | +0.42 | -0.39 | yes |
| rp_ess_revenue | news18 | -0.30 | 1.32 | +0.43 | -0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
