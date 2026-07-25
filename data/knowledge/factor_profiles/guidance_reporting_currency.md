---
field: guidance_reporting_currency
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.83
best_fitness: 0.85
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.2695
ann_vol: 0.241
hit_rate: 0.5061
rolling_sharpe_min: -1.581
rolling_sharpe_max: 2.517
top_merge_partner: multi_factor_static_score_derivative
negated_best_sharpe: 0.8
negated_best_template: rank_neg_delta
negated_best_fitness: 0.84
n_negated_sims: 10
direction_gap: -0.03
---
# guidance_reporting_currency (analyst4)

*Pricing Currency where the security trades - Annual*

## Signal Profile
- `rank(guidance_reporting_currency)`: S=0.96, F=0.72, T=1.1%, INFERIOR (TOP3000)
- `rank(guidance_reporting_currency / close)`: S=0.81, F=0.61, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(guidance_reporting_currency, 5))`: S=0.83, F=0.85, T=19.3%, INFERIOR (TOP500)
- `-rank(guidance_reporting_currency)`: S=-0.69, F=-0.51, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(guidance_reporting_currency, 5))`: S=0.80, F=0.84, T=14.7%, INFERIOR (TOP3000)
- `ts_zscore(guidance_reporting_currency, 22)`: S=-0.16, F=-0.08, T=3.3%, INFERIOR (TOP3000)
- `ts_mean(guidance_reporting_currency, 10)`: S=0.24, F=0.10, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(guidance_reporting_currency, 22))`: S=-0.12, F=-0.05, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * guidance_reporting_currency)`: S=-0.07, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * guidance_reporting_currency / close)`: S=-0.11, F=-0.04, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+18.6%
  - 2020: S=0.21 (weak), ret=+5.2%
  - 2021: S=1.90 (strong), ret=+68.2%
  - 2022: S=0.21 (weak), ret=+3.2%
  - 2023: S=0.27 (weak), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 26.95% over 493 days (recovered)
- Annualized: return +20.0%, volatility 24.1% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +1.66, excess kurtosis +13.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 2.52, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +48.52%; worst month: -9.61%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.51
- Sideways: S=0.55
- Bear: S=0.37

## Negated Direction
Best negated: `rank(-1 * ts_delta(guidance_reporting_currency, 5))` S=0.80, F=0.84, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * guidance_reporting_currency)`: S=-0.07, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * guidance_reporting_currency / close)`: S=-0.11, F=-0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(guidance_reporting_currency, 5))`: S=0.80, F=0.84, T=14.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(guidance_reporting_currency, 5))` | TOP500 | 0.83 | 0.85 | 27.0% | 100% | mixed |
| `rank(guidance_reporting_currency)` | TOP3000 | 0.95 | 0.72 | 13.5% | 80% | bull-only |
| `rank(guidance_reporting_currency / close)` | TOP3000 | 0.80 | 0.61 | 21.4% | 80% | bull-only |
| `rank(ts_delta(guidance_reporting_currency, 5))` | TOP1000 | 0.68 | 0.56 | 26.5% | 80% | all-weather |
| `rank(guidance_reporting_currency / close)` | TOP1000 | 0.67 | 0.51 | 20.0% | 80% | bull-only |
| `rank(guidance_reporting_currency)` | TOP1000 | 0.69 | 0.51 | 17.4% | 80% | bull-only |
| `rank(guidance_reporting_currency / close)` | TOP500 | 0.42 | 0.27 | 32.2% | 80% | bull-only |
| `rank(guidance_reporting_currency)` | TOP500 | 0.42 | 0.26 | 30.6% | 80% | bull-only |
| `rank(guidance_reporting_currency / close)` | TOP200 | 0.11 | 0.04 | 50.4% | 80% | bull-only |
| `rank(ts_delta(guidance_reporting_currency, 5))` | TOP3000 | 0.07 | 0.02 | 45.8% | 60% | bull-only |
| `rank(guidance_reporting_currency)` | TOP200 | 0.07 | 0.02 | 48.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_q: -0.135 (weakly negatively correlated)
- min_investing_cashflow_guidance_2: 0.128 (weakly positively correlated)
- max_investing_cashflow_guidance_2: 0.128 (weakly positively correlated)
- pv13_revere_term_sector_total: 0.127 (weakly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_a: -0.125 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.08 | 1.22 | +0.38 | -0.62 | yes |
| cashflow_efficiency_rank_derivative | model16 | -0.08 | 1.20 | +0.37 | -0.63 | yes |
| growth_potential_rank_derivative | model16 | -0.08 | 1.25 | +0.37 | -0.60 | yes |
| fnd2_propplteqflublgland | fundamental2 | -0.04 | 1.17 | +0.34 | -0.79 | yes |
| earnings_certainty_rank_derivative | model16 | -0.09 | 1.29 | +0.35 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
