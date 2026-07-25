---
field: fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.5
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.5068
ann_vol: 0.1636
hit_rate: 0.5158
rolling_sharpe_min: -2.362
rolling_sharpe_max: 3.01
negated_best_sharpe: 0.16
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.34
---
# fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a (fundamental2)

*Amount after tax and reclassification adjustments, of appreciation (loss) in value of unsold available-for-sale securities. Excludes amounts related to other than temporary impairment (OTTI) loss.*

## Signal Profile
- `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)`: S=0.15, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a / close)`: S=0.54, F=0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))`: S=0.50, F=0.25, T=32.4%, INFERIOR (TOP3000)
- `-rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))`: S=-0.05, F=-0.01, T=26.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 22)`: S=0.24, F=0.13, T=12.5%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 22))`: S=0.40, F=0.25, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)`: S=0.16, F=0.05, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.26 (negative), ret=-16.5%
  - 2020: S=0.25 (weak), ret=+4.5%
  - 2021: S=-1.11 (negative), ret=-18.2%
  - 2022: S=1.87 (strong), ret=+31.7%
  - 2023: S=2.53 (strong), ret=+37.1%

## Risk & Drawdown
- Max drawdown: 50.68% over 1400 days (recovered)
- Annualized: return +7.9%, volatility 16.4% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.04, excess kurtosis +2.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.36, max 3.01, latest 2.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +16.79%; worst month: -13.29%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.61
- Sideways: S=-0.04
- Bear: S=-0.15

## Negated Direction
Best negated: `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)` S=0.16, F=0.05, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)`: S=0.16, F=0.05, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))`: S=-0.05, F=-0.01, T=26.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))` | TOP3000 | 0.48 | 0.25 | 50.7% | 60% | mixed |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a / close)` | TOP3000 | 0.54 | 0.22 | 5.1% | 60% | bull-only |
| `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))` | TOP500 | 0.17 | 0.06 | 52.3% | 80% | bull-only |
| `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a, 5))` | TOP1000 | 0.15 | 0.05 | 77.1% | 40% | bull-only |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a / close)` | TOP1000 | 0.15 | 0.04 | 6.0% | 60% | bull-only |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a)` | TOP3000 | 0.15 | 0.03 | 4.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_comprehensive_income_net_of_tax_a: 0.138 (weakly positively correlated)
- fnd6_cisecgl: 0.129 (weakly positively correlated)
- fnd6_msa: 0.128 (weakly positively correlated)
- fnd6_newqv1300_aocipenq: -0.120 (weakly negatively correlated)
- fnd6_esopct: -0.116 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
