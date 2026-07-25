---
field: fn_finite_lived_intangible_assets_gross_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.65
best_fitness: 0.37
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2658
ann_vol: 0.1958
hit_rate: 0.5117
rolling_sharpe_min: -1.131
rolling_sharpe_max: 2.552
negated_best_sharpe: 0.47
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.18
---
# fn_finite_lived_intangible_assets_gross_q (fundamental2)

*Amount before amortization of assets, excluding financial assets and goodwill, lacking physical substance with a finite life.*

## Signal Profile
- `rank(fn_finite_lived_intangible_assets_gross_q)`: S=0.38, F=0.20, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_finite_lived_intangible_assets_gross_q / close)`: S=0.46, F=0.23, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))`: S=0.65, F=0.37, T=38.5%, INFERIOR (TOP200)
- `-rank(fn_finite_lived_intangible_assets_gross_q)`: S=-0.03, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))`: S=-0.57, F=-0.27, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_finite_lived_intangible_assets_gross_q, 63)`: S=0.02, F=0.00, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fn_finite_lived_intangible_assets_gross_q, 10)`: S=0.14, F=0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_finite_lived_intangible_assets_gross_q, 22))`: S=-0.24, F=-0.08, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_q)`: S=0.43, F=0.31, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_q / close)`: S=0.47, F=0.32, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.65, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.11 (negative), ret=-20.0%
  - 2020: S=1.62 (strong), ret=+29.5%
  - 2021: S=0.22 (weak), ret=+4.2%
  - 2022: S=0.74 (moderate), ret=+17.8%
  - 2023: S=1.94 (strong), ret=+30.8%

## Risk & Drawdown
- Max drawdown: 26.58% over 575 days (recovered)
- Annualized: return +12.7%, volatility 19.6% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew -0.05, excess kurtosis +9.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.55, latest 1.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +15.07%; worst month: -8.48%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.71
- Sideways: S=-0.56
- Bear: S=0.73

## Negated Direction
Best negated: `rank(-1 * fn_finite_lived_intangible_assets_gross_q / close)` S=0.47, F=0.32, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_finite_lived_intangible_assets_gross_q)`: S=0.43, F=0.31, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_q / close)`: S=0.47, F=0.32, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))`: S=-0.57, F=-0.27, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))` | TOP200 | 0.65 | 0.37 | 26.6% | 80% | all-weather |
| `rank(ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))` | TOP3000 | 0.73 | 0.34 | 13.7% | 80% | all-weather |
| `rank(fn_finite_lived_intangible_assets_gross_q / close)` | TOP3000 | 0.45 | 0.23 | 9.9% | 100% | bull-only |
| `rank(ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))` | TOP500 | 0.51 | 0.22 | 24.9% | 80% | mixed |
| `rank(fn_finite_lived_intangible_assets_gross_q)` | TOP3000 | 0.37 | 0.20 | 22.8% | 60% | bull-only |
| `rank(ts_delta(fn_finite_lived_intangible_assets_gross_q, 5))` | TOP1000 | 0.43 | 0.16 | 20.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_payments_to_acquire_businesses_net_of_cash_acquired_q: 0.140 (weakly positively correlated)
- fnd2_q_flintasamt1expythree: 0.129 (weakly positively correlated)
- parkinson_volatility_20: 0.126 (weakly positively correlated)
- historical_volatility_20: 0.118 (weakly positively correlated)
- fnd6_txtubpospdec: 0.117 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
