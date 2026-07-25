---
field: fn_def_tax_liab_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.77
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0921
ann_vol: 0.07
hit_rate: 0.4964
rolling_sharpe_min: -1.367
rolling_sharpe_max: 2.412
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.52
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.25
---
# fn_def_tax_liab_a (fundamental2)

*Amount, after deferred tax asset, of deferred tax liability attributable to taxable differences without jurisdictional netting.*

## Signal Profile
- `rank(fn_def_tax_liab_a)`: S=0.54, F=0.35, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_def_tax_liab_a / close)`: S=0.83, F=0.57, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_tax_liab_a, 5))`: S=-0.18, F=-0.04, T=35.1%, INFERIOR (TOP3000)
- `-rank(fn_def_tax_liab_a)`: S=-0.23, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_liab_a, 5))`: S=0.52, F=0.23, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_tax_liab_a, 63)`: S=0.77, F=0.60, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_liab_a, 10)`: S=0.19, F=0.06, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_liab_a, 22))`: S=-0.54, F=-0.29, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_a)`: S=-0.23, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_a / close)`: S=-0.38, F=-0.20, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+1.6%
  - 2020: S=0.66 (moderate), ret=+5.3%
  - 2021: S=1.21 (moderate), ret=+11.2%
  - 2022: S=1.38 (moderate), ret=+9.8%
  - 2023: S=0.10 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 9.21% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +5.8%, volatility 7.0% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.42, excess kurtosis +2.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 2.41, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +7.38%; worst month: -3.15%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.88
- Sideways: S=0.45
- Bear: S=-1.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_def_tax_liab_a, 5))` S=0.52, F=0.23, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_def_tax_liab_a)`: S=-0.23, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_liab_a / close)`: S=-0.38, F=-0.20, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_liab_a, 5))`: S=0.52, F=0.23, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_liab_a / close)` | TOP3000 | 0.83 | 0.57 | 9.2% | 100% | bull-only |
| `rank(fn_def_tax_liab_a)` | TOP3000 | 0.53 | 0.35 | 22.9% | 80% | bull-only |
| `rank(fn_def_tax_liab_a / close)` | TOP1000 | 0.37 | 0.20 | 12.6% | 60% | bull-only |
| `rank(fn_def_tax_liab_a)` | TOP1000 | 0.23 | 0.11 | 28.2% | 60% | bull-only |
| `rank(fn_def_tax_liab_a / close)` | TOP500 | 0.22 | 0.10 | 25.2% | 60% | bull-only |
| `rank(fn_def_tax_liab_a)` | TOP500 | 0.07 | 0.02 | 38.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txndbl: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.950 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.947 (strongly positively correlated)
- fnd6_mfma1_dp: 0.947 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.947 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.76 | +0.58 | -0.65 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.49 | +0.60 | -0.48 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.34 | 1.37 | +0.54 | -0.66 | yes |
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.60 | +0.57 | -0.26 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.44 | +0.49 | -0.51 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
