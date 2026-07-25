---
field: fnd2_a_flintasamt1expyfour
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.63
best_fitness: 0.4
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2268
ann_vol: 0.1871
hit_rate: 0.4939
rolling_sharpe_min: -0.667
rolling_sharpe_max: 1.785
negated_best_sharpe: 0.51
negated_best_template: neg_rank_level
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.12
---
# fnd2_a_flintasamt1expyfour (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 4th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_flintasamt1expyfour)`: S=0.24, F=0.09, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasamt1expyfour / close)`: S=0.48, F=0.23, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasamt1expyfour, 5))`: S=0.63, F=0.40, T=29.4%, INFERIOR (TOP200)
- `-rank(fnd2_a_flintasamt1expyfour)`: S=0.13, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expyfour, 5))`: S=-0.08, F=-0.02, T=33.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_flintasamt1expyfour, 22)`: S=0.55, F=0.37, T=22.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasamt1expyfour, 10)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasamt1expyfour, 22))`: S=0.46, F=0.25, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expyfour)`: S=0.51, F=0.35, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expyfour / close)`: S=0.44, F=0.25, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.48 (moderate), ret=+22.8%
  - 2020: S=0.85 (moderate), ret=+16.8%
  - 2021: S=0.47 (weak), ret=+10.6%
  - 2022: S=-0.06 (negative), ret=-1.1%
  - 2023: S=0.67 (moderate), ret=+8.7%

## Risk & Drawdown
- Max drawdown: 22.68% over 190 days (recovered)
- Annualized: return +11.8%, volatility 18.7% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +1.19, excess kurtosis +10.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 1.78, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +17.45%; worst month: -13.32%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.35
- Sideways: S=0.20
- Bear: S=0.24

## Negated Direction
Best negated: `rank(-1 * fnd2_a_flintasamt1expyfour)` S=0.51, F=0.35, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasamt1expyfour)`: S=0.51, F=0.35, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expyfour / close)`: S=0.44, F=0.25, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expyfour, 5))`: S=-0.08, F=-0.02, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_flintasamt1expyfour, 5))` | TOP200 | 0.63 | 0.40 | 22.7% | 80% | mixed |
| `rank(fnd2_a_flintasamt1expyfour / close)` | TOP3000 | 0.47 | 0.23 | 9.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expyfour, 5))` | TOP1000 | 0.37 | 0.15 | 20.2% | 80% | bull-only |
| `rank(fnd2_a_flintasamt1expyfour)` | TOP3000 | 0.23 | 0.09 | 20.6% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expyfour, 5))` | TOP500 | 0.18 | 0.06 | 23.2% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fn_finite_lived_intangible_assets_net_a: 0.572 (moderately positively correlated)
- fn_payments_to_acquire_businesses_net_of_cash_acquired_a: 0.392 (weakly positively correlated)
- fnd2_unrgtxbnfinregfprtxps: 0.382 (weakly positively correlated)
- fnd2_ebitfr: 0.236 (weakly positively correlated)
- fn_accum_oth_income_loss_fx_adj_net_of_tax_a: 0.212 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
