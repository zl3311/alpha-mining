---
field: fn_oth_income_loss_net_of_tax_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.47
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0467
ann_vol: 0.0317
hit_rate: 0.5287
rolling_sharpe_min: -0.568
rolling_sharpe_max: 3.008
top_merge_partner: fnd6_rank
negated_best_sharpe: 0.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.77
---
# fn_oth_income_loss_net_of_tax_a (fundamental2)

*Amount after tax and reclassification adjustments of other comprehensive income (loss).*

## Signal Profile
- `rank(fn_oth_income_loss_net_of_tax_a)`: S=0.66, F=0.27, T=1.8%, INFERIOR (TOP1000)
- `rank(fn_oth_income_loss_net_of_tax_a / close)`: S=0.95, F=0.47, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_oth_income_loss_net_of_tax_a, 5))`: S=0.19, F=0.06, T=33.7%, INFERIOR (TOP500)
- `-rank(fn_oth_income_loss_net_of_tax_a)`: S=-0.66, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_net_of_tax_a, 5))`: S=0.18, F=0.06, T=30.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_oth_income_loss_net_of_tax_a, 22)`: S=0.59, F=0.44, T=23.3%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_net_of_tax_a, 10)`: S=0.38, F=0.14, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_net_of_tax_a, 22))`: S=-0.14, F=-0.04, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_a)`: S=-0.10, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_a / close)`: S=-0.25, F=-0.08, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.98, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.59 (negative), ret=-1.4%
  - 2020: S=2.67 (strong), ret=+6.8%
  - 2021: S=0.74 (moderate), ret=+2.9%
  - 2022: S=1.34 (moderate), ret=+4.4%
  - 2023: S=0.80 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 4.67% over 421 days (recovered)
- Annualized: return +3.1%, volatility 3.2% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew -0.17, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 3.01, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +2.34%; worst month: -3.13%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.44
- Sideways: S=2.01
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_oth_income_loss_net_of_tax_a, 5))` S=0.18, F=0.06, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_net_of_tax_a)`: S=-0.10, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_a / close)`: S=-0.25, F=-0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_net_of_tax_a, 5))`: S=0.18, F=0.06, T=30.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_income_loss_net_of_tax_a / close)` | TOP1000 | 0.98 | 0.47 | 4.7% | 80% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_a)` | TOP1000 | 0.69 | 0.27 | 6.1% | 80% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_a / close)` | TOP500 | 0.58 | 0.21 | 6.9% | 80% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_a)` | TOP500 | 0.48 | 0.16 | 7.9% | 80% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_a / close)` | TOP3000 | 0.45 | 0.13 | 6.0% | 80% | bull-only |
| `rank(fn_oth_income_loss_net_of_tax_a)` | TOP3000 | 0.35 | 0.08 | 5.9% | 80% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_a / close)` | TOP200 | 0.29 | 0.08 | 11.6% | 60% | mixed |
| `rank(ts_delta(fn_oth_income_loss_net_of_tax_a, 5))` | TOP500 | 0.17 | 0.06 | 39.6% | 40% | bull-only |
| `rank(fn_oth_income_loss_net_of_tax_a)` | TOP200 | 0.13 | 0.02 | 14.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cicurr: 0.432 (moderately positively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a: 0.314 (weakly positively correlated)
- anl4_afv4_cfps_number: -0.261 (weakly negatively correlated)
- fnd6_prchq: -0.259 (weakly negatively correlated)
- anl4_afv4_dts_spe: -0.252 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.12 | 1.62 | +0.46 | -0.09 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.17 | 1.42 | +0.44 | +1.00 | yes |
| sales_max_guidance_quarterly | analyst4 | -0.05 | 1.49 | +0.42 | +0.47 | yes |
| fnd6_cshtr | fundamental6 | -0.11 | 1.43 | +0.42 | +0.23 | yes |
| rp_ess_ratings | news18 | -0.02 | 1.32 | +0.34 | -0.72 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
