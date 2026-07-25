---
field: fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a
dataset: fundamental2
cluster: fundamental2_income_earnings
coverage: 0.426
community_alphas: 14452
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.43
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0813
ann_vol: 0.0483
hit_rate: 0.5134
rolling_sharpe_min: -1.146
rolling_sharpe_max: 2.944
top_merge_partner: cashflow_per_share_minimum
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.03
---
# fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a (fundamental2)

*Amount after tax and reclassification adjustments of gain (loss) on foreign currency translation adjustments, foreign currency transactions designated and effective as economic hedges of a net investment in a foreign entity, and intra-entity foreign currency transactions that are of a long-term-investment nature.*

## Signal Profile
- `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)`: S=0.55, F=0.26, T=2.0%, INFERIOR (TOP500)
- `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)`: S=0.79, F=0.43, T=2.2%, INFERIOR (TOP500)
- `rank(ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 5))`: S=-0.02, F=0.00, T=29.4%, INFERIOR (TOP200)
- `-rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)`: S=-0.47, F=-0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 5))`: S=0.76, F=0.41, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 63)`: S=0.05, F=0.01, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 10)`: S=0.14, F=0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 22))`: S=0.06, F=0.01, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)`: S=-0.48, F=-0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)`: S=-0.79, F=-0.38, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.20 (negative), ret=-4.2%
  - 2020: S=0.19 (weak), ret=+0.7%
  - 2021: S=2.23 (strong), ret=+10.2%
  - 2022: S=0.43 (weak), ret=+2.5%
  - 2023: S=1.78 (strong), ret=+9.8%

## Risk & Drawdown
- Max drawdown: 8.13% over 224 days (recovered)
- Annualized: return +3.9%, volatility 4.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.23, excess kurtosis +0.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.94, latest 1.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.22%; worst month: -2.71%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.40
- Sideways: S=1.30
- Bear: S=1.70

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 5))` S=0.76, F=0.41, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)`: S=-0.48, F=-0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)`: S=-0.79, F=-0.38, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a, 5))`: S=0.76, F=0.41, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)` | TOP500 | 0.81 | 0.43 | 8.1% | 80% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)` | TOP1000 | 0.83 | 0.42 | 6.9% | 80% | bear-only |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)` | TOP3000 | 0.81 | 0.38 | 6.0% | 80% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)` | TOP500 | 0.58 | 0.26 | 10.1% | 80% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)` | TOP1000 | 0.49 | 0.20 | 9.0% | 80% | bear-only |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)` | TOP3000 | 0.50 | 0.20 | 8.0% | 80% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a)` | TOP200 | 0.20 | 0.06 | 10.8% | 60% | weak |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a / close)` | TOP200 | 0.18 | 0.05 | 12.8% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_cicurr: 0.614 (moderately positively correlated)
- fnd6_exre: 0.393 (weakly positively correlated)
- fn_oth_income_loss_net_of_tax_a: 0.314 (weakly positively correlated)
- fnd6_optprcgr: 0.312 (weakly positively correlated)
- fn_oth_comp_fair_value_a: 0.308 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| cashflow_per_share_minimum | analyst4 | -0.12 | 1.25 | +0.40 | -0.91 | yes |
| eps_guidance_value_quarterly | analyst4 | -0.11 | 1.24 | +0.39 | -0.29 | yes |
| max_reported_eps_guidance | analyst4 | -0.12 | 1.22 | +0.41 | +0.12 | yes |
| fnd6_newqv1300_miiq | fundamental6 | -0.02 | 1.19 | +0.32 | -0.86 | yes |
| anl4_ptpr_number | analyst4 | -0.05 | 1.16 | +0.33 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
