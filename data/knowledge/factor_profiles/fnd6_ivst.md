---
field: fnd6_ivst
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.87
best_fitness: 0.59
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1972
ann_vol: 0.184
hit_rate: 0.5239
rolling_sharpe_min: -0.6
rolling_sharpe_max: 2.729
top_merge_partner: fn_assets_fair_val_l3_a
negated_best_sharpe: 0.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.58
---
# fnd6_ivst (fundamental6)

*Short-Term Investments - Total*

## Signal Profile
- `rank(fnd6_ivst)`: S=0.50, F=0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_ivst / close)`: S=0.53, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ivst, 5))`: S=0.87, F=0.59, T=34.9%, INFERIOR (TOP500)
- `-rank(fnd6_ivst)`: S=-0.08, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivst, 5))`: S=0.29, F=0.09, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ivst, 63)`: S=0.22, F=0.11, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivst, 10)`: S=0.24, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivst, 22))`: S=0.34, F=0.15, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivst)`: S=-0.50, F=-0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivst / close)`: S=-0.53, F=-0.22, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.61 (strong), ret=+22.6%
  - 2020: S=1.17 (moderate), ret=+20.8%
  - 2021: S=1.08 (moderate), ret=+20.2%
  - 2022: S=1.35 (moderate), ret=+29.5%
  - 2023: S=-0.77 (negative), ret=-13.1%

## Risk & Drawdown
- Max drawdown: 19.72% over 183 days (recovered)
- Annualized: return +16.3%, volatility 18.4% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew -0.17, excess kurtosis +12.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.73, latest -0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +24.74%; worst month: -12.19%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.02
- Sideways: S=1.28
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ivst, 5))` S=0.29, F=0.09, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_ivst)`: S=-0.50, F=-0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivst / close)`: S=-0.53, F=-0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivst, 5))`: S=0.29, F=0.09, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ivst, 5))` | TOP500 | 0.89 | 0.59 | 19.7% | 80% | mixed |
| `rank(ts_delta(fnd6_ivst, 5))` | TOP200 | 0.44 | 0.23 | 46.8% | 60% | mixed |
| `rank(fnd6_ivst / close)` | TOP3000 | 0.54 | 0.22 | 4.2% | 80% | mixed |
| `rank(fnd6_ivst)` | TOP3000 | 0.51 | 0.21 | 11.4% | 60% | bull-only |
| `rank(fnd6_ivst / close)` | TOP500 | 0.43 | 0.19 | 11.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_ivst, 5))` | TOP1000 | 0.37 | 0.14 | 15.2% | 80% | weak |
| `rank(fnd6_ivst)` | TOP500 | 0.22 | 0.08 | 20.4% | 60% | bull-only |
| `rank(fnd6_ivst / close)` | TOP1000 | 0.24 | 0.07 | 8.3% | 80% | bull-only |
| `rank(fnd6_ivst / close)` | TOP200 | 0.12 | 0.03 | 18.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cisecgl: 0.176 (weakly positively correlated)
- fnd6_newqv1300_acomincq: -0.164 (weakly negatively correlated)
- cashflow_invst: -0.157 (weakly negatively correlated)
- fnd6_newa1v1300_ivncf: -0.156 (weakly negatively correlated)
- fnd6_mrc1: 0.149 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l3_a | fundamental2 | -0.07 | 1.41 | +0.38 | -0.90 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | +0.01 | 1.25 | +0.36 | -0.64 | yes |
| pv13_revere_company_total | pv13 | -0.04 | 1.40 | +0.35 | -0.68 | yes |
| fn_income_taxes_paid_q | fundamental2 | +0.01 | 1.25 | +0.33 | -0.81 | yes |
| fn_avg_diluted_sharesout_adj_a | fundamental2 | -0.02 | 1.26 | +0.38 | -0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
