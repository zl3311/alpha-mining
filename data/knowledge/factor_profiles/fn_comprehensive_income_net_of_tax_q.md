---
field: fn_comprehensive_income_net_of_tax_q
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.64
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3378
ann_vol: 0.1026
hit_rate: 0.5053
rolling_sharpe_min: -4.392
rolling_sharpe_max: 2.62
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.01
---
# fn_comprehensive_income_net_of_tax_q (fundamental2)

*Amount after tax of increase (decrease) in equity from transactions and other events and circumstances from net income and other comprehensive income, attributable to parent entity. Excludes changes in equity resulting from investments by owners and distributions to owners.*

## Signal Profile
- `rank(fn_comprehensive_income_net_of_tax_q)`: S=0.12, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(fn_comprehensive_income_net_of_tax_q / close)`: S=0.16, F=0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comprehensive_income_net_of_tax_q, 5))`: S=-0.19, F=-0.04, T=36.1%, INFERIOR (TOP1000)
- `-rank(fn_comprehensive_income_net_of_tax_q)`: S=-0.12, F=-0.04, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_q, 5))`: S=0.63, F=0.21, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comprehensive_income_net_of_tax_q, 63)`: S=0.16, F=0.03, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fn_comprehensive_income_net_of_tax_q, 10)`: S=-0.07, F=-0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comprehensive_income_net_of_tax_q, 22))`: S=0.64, F=0.27, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_q)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_q / close)`: S=-0.16, F=-0.06, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.15, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.2%
  - 2020: S=-3.60 (negative), ret=-23.1%
  - 2021: S=1.26 (moderate), ret=+13.0%
  - 2022: S=1.59 (strong), ret=+24.3%
  - 2023: S=-0.63 (negative), ret=-6.4%

## Risk & Drawdown
- Max drawdown: 33.78% over 1003 days (recovered)
- Annualized: return +1.6%, volatility 10.3% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew -0.18, excess kurtosis +1.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.39, max 2.62, latest -0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.83%; worst month: -7.53%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.62
- Sideways: S=0.58
- Bear: S=-3.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_q, 5))` S=0.63, F=0.21, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comprehensive_income_net_of_tax_q)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comprehensive_income_net_of_tax_q / close)`: S=-0.16, F=-0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comprehensive_income_net_of_tax_q, 5))`: S=0.63, F=0.21, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comprehensive_income_net_of_tax_q / close)` | TOP3000 | 0.15 | 0.06 | 33.8% | 40% | bull-only |
| `rank(fn_comprehensive_income_net_of_tax_q)` | TOP3000 | 0.12 | 0.04 | 37.6% | 60% | bull-only |
| `rank(fn_comprehensive_income_net_of_tax_q)` | TOP1000 | 0.11 | 0.04 | 36.8% | 60% | bull-only |
| `rank(fn_comprehensive_income_net_of_tax_q / close)` | TOP1000 | 0.10 | 0.03 | 27.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_dilavq: 0.978 (strongly positively correlated)
- fnd6_newqv1300_ibq: 0.978 (strongly positively correlated)
- income_beforeextra: 0.978 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.978 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.978 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
