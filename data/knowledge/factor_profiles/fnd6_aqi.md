---
field: fnd6_aqi
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.8
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1647
ann_vol: 0.1135
hit_rate: 0.5117
rolling_sharpe_min: -1.576
rolling_sharpe_max: 2.245
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_aqi (fundamental6)

*Acquisitions - Income Contribution*

## Signal Profile
- `rank(fnd6_aqi)`: S=0.54, F=0.38, T=4.2%, INFERIOR (TOP1000)
- `rank(fnd6_aqi / close)`: S=0.43, F=0.35, T=4.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_aqi, 5))`: S=0.31, F=0.19, T=17.4%, INFERIOR (TOP3000)
- `-rank(fnd6_aqi)`: S=-0.54, F=-0.38, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqi, 5))`: S=-0.50, F=-0.38, T=17.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_aqi, 22)`: S=-0.10, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aqi, 10)`: S=0.80, F=0.74, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aqi, 22))`: S=-0.33, F=-0.26, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqi)`: S=0.24, F=0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqi / close)`: S=0.18, F=0.06, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.13 (negative), ret=-7.4%
  - 2020: S=0.62 (moderate), ret=+5.4%
  - 2021: S=1.70 (strong), ret=+24.7%
  - 2022: S=-0.58 (negative), ret=-7.5%
  - 2023: S=1.31 (moderate), ret=+14.4%

## Risk & Drawdown
- Max drawdown: 16.47% over 454 days (recovered)
- Annualized: return +6.0%, volatility 11.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.76, excess kurtosis +5.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 2.25, latest 1.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +12.16%; worst month: -6.57%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.56
- Sideways: S=0.18
- Bear: S=0.87

## Negated Direction
Best negated: `rank(-1 * fnd6_aqi)` S=0.24, F=0.09, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_aqi)`: S=0.24, F=0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqi / close)`: S=0.18, F=0.06, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqi, 5))`: S=-0.50, F=-0.38, T=17.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_aqi)` | TOP1000 | 0.53 | 0.38 | 16.5% | 60% | all-weather |
| `rank(fnd6_aqi / close)` | TOP200 | 0.41 | 0.35 | 32.6% | 80% | bull-only |
| `rank(fnd6_aqi / close)` | TOP1000 | 0.41 | 0.27 | 16.1% | 60% | mixed |
| `rank(ts_delta(fnd6_aqi, 5))` | TOP3000 | 0.31 | 0.19 | 43.7% | 80% | all-weather |
| `rank(fnd6_aqi)` | TOP200 | 0.23 | 0.17 | 37.0% | 80% | bull-only |
| `rank(fnd6_aqi / close)` | TOP500 | 0.15 | 0.07 | 35.8% | 60% | mixed |
| `rank(ts_delta(fnd6_aqi, 5))` | TOP500 | 0.10 | 0.04 | 65.0% | 40% | bull-only |
| `rank(fnd6_aqi)` | TOP500 | 0.06 | 0.03 | 37.8% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_cicurr: 0.215 (weakly positively correlated)
- fnd6_exre: 0.194 (weakly positively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a: 0.194 (weakly positively correlated)
- correlation_last_90_days_spy: 0.173 (weakly positively correlated)
- fnd6_optprcgr: 0.168 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
