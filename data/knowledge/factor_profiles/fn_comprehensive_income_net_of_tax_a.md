---
field: fn_comprehensive_income_net_of_tax_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.55
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2892
ann_vol: 0.1189
hit_rate: 0.5158
rolling_sharpe_min: -2.047
rolling_sharpe_max: 2.955
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: -0.02
---
# fn_comprehensive_income_net_of_tax_a (fundamental2)

*Amount after tax of increase (decrease) in equity from transactions and other events and circumstances from net income and other comprehensive income, attributable to parent entity. Excludes changes in equity resulting from investments by owners and distributions to owners.*

## Signal Profile
- `rank(fn_comprehensive_income_net_of_tax_a)`: S=0.05, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_comprehensive_income_net_of_tax_a / close)`: S=0.21, F=0.09, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_comprehensive_income_net_of_tax_a, 5))`: S=0.57, F=0.25, T=34.6%, INFERIOR (TOP3000)
- `-rank(fn_comprehensive_income_net_of_tax_a)`: S=-0.05, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_a, 5))`: S=0.55, F=0.27, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comprehensive_income_net_of_tax_a, 63)`: S=0.32, F=0.17, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fn_comprehensive_income_net_of_tax_a, 10)`: S=0.08, F=0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comprehensive_income_net_of_tax_a, 22))`: S=0.06, F=0.01, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_a)`: S=0.26, F=0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_a / close)`: S=0.17, F=0.07, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.10 (strong), ret=+22.1%
  - 2020: S=0.65 (moderate), ret=+8.2%
  - 2021: S=-0.55 (negative), ret=-6.8%
  - 2022: S=0.64 (moderate), ret=+7.8%
  - 2023: S=0.28 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 28.92% over 886 days (recovered)
- Annualized: return +7.0%, volatility 11.9% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.25, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.05, max 2.96, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +9.51%; worst month: -11.81%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.49
- Sideways: S=1.69
- Bear: S=0.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_a, 5))` S=0.55, F=0.27, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comprehensive_income_net_of_tax_a)`: S=0.26, F=0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_a / close)`: S=0.17, F=0.07, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_a, 5))`: S=0.55, F=0.27, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_comprehensive_income_net_of_tax_a, 5))` | TOP3000 | 0.58 | 0.25 | 28.9% | 80% | mixed |
| `rank(ts_delta(fn_comprehensive_income_net_of_tax_a, 5))` | TOP200 | 0.32 | 0.14 | 54.2% | 40% | bull-only |
| `rank(fn_comprehensive_income_net_of_tax_a / close)` | TOP1000 | 0.20 | 0.09 | 28.6% | 60% | bull-only |
| `rank(fn_comprehensive_income_net_of_tax_a / close)` | TOP3000 | 0.17 | 0.07 | 29.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_profit_loss_a: 0.411 (moderately positively correlated)
- fnd6_prch: -0.167 (weakly negatively correlated)
- forward_price_180: 0.159 (weakly positively correlated)
- forward_price_270: 0.159 (weakly positively correlated)
- forward_price_150: 0.159 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
