---
field: fn_finite_lived_intangible_assets_net_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.64
best_fitness: 0.44
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.3287
ann_vol: 0.2164
hit_rate: 0.4915
rolling_sharpe_min: -1.832
rolling_sharpe_max: 2.081
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.02
---
# fn_finite_lived_intangible_assets_net_a (fundamental2)

*Finite Lived Intangible Assets, Net*

## Signal Profile
- `rank(fn_finite_lived_intangible_assets_net_a)`: S=0.17, F=0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_finite_lived_intangible_assets_net_a / close)`: S=0.24, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_finite_lived_intangible_assets_net_a, 5))`: S=0.64, F=0.44, T=29.1%, INFERIOR (TOP200)
- `-rank(fn_finite_lived_intangible_assets_net_a)`: S=0.01, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_net_a, 5))`: S=0.66, F=0.33, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fn_finite_lived_intangible_assets_net_a, 22)`: S=0.57, F=0.41, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(fn_finite_lived_intangible_assets_net_a, 10)`: S=0.00, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_finite_lived_intangible_assets_net_a, 22))`: S=-0.05, F=-0.01, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_a)`: S=-0.17, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_a / close)`: S=-0.24, F=-0.08, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+16.7%
  - 2020: S=1.14 (moderate), ret=+25.8%
  - 2021: S=1.17 (moderate), ret=+32.4%
  - 2022: S=0.11 (weak), ret=+2.5%
  - 2023: S=-0.74 (negative), ret=-10.1%

## Risk & Drawdown
- Max drawdown: 32.87% over 694 days (not yet recovered, ongoing at window end)
- Annualized: return +13.7%, volatility 21.6% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +1.00, excess kurtosis +12.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 2.08, latest -0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +22.17%; worst month: -11.77%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.01
- Sideways: S=-0.38
- Bear: S=1.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_net_a, 5))` S=0.66, F=0.33, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_finite_lived_intangible_assets_net_a)`: S=-0.17, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_a / close)`: S=-0.24, F=-0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_net_a, 5))`: S=0.66, F=0.33, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_finite_lived_intangible_assets_net_a, 5))` | TOP200 | 0.63 | 0.44 | 32.9% | 80% | all-weather |
| `rank(fn_finite_lived_intangible_assets_net_a / close)` | TOP3000 | 0.23 | 0.08 | 8.3% | 60% | bull-only |
| `rank(ts_delta(fn_finite_lived_intangible_assets_net_a, 5))` | TOP1000 | 0.20 | 0.05 | 25.9% | 80% | mixed |
| `rank(fn_finite_lived_intangible_assets_net_a)` | TOP3000 | 0.17 | 0.05 | 22.6% | 60% | bull-only |
| `rank(ts_delta(fn_finite_lived_intangible_assets_net_a, 5))` | TOP500 | 0.13 | 0.03 | 42.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expyfour: 0.572 (moderately positively correlated)
- fn_payments_to_acquire_businesses_net_of_cash_acquired_a: 0.442 (moderately positively correlated)
- fn_avg_diluted_sharesout_adj_a: 0.307 (weakly positively correlated)
- fn_accum_oth_income_loss_fx_adj_net_of_tax_a: 0.292 (weakly positively correlated)
- fnd2_unrgtxbnfinregfprtxps: 0.282 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
