---
field: fnd2_a_flintasamt1expnext12m
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.56
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0746
ann_vol: 0.0628
hit_rate: 0.4915
rolling_sharpe_min: -1.189
rolling_sharpe_max: 2.222
redundancy_cluster: 1
negated_best_sharpe: 0.39
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.17
---
# fnd2_a_flintasamt1expnext12m (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the next fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_flintasamt1expnext12m)`: S=0.29, F=0.12, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasamt1expnext12m / close)`: S=0.55, F=0.29, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasamt1expnext12m, 5))`: S=0.31, F=0.11, T=34.0%, INFERIOR (TOP1000)
- `-rank(fnd2_a_flintasamt1expnext12m)`: S=-0.05, F=-0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expnext12m, 5))`: S=0.35, F=0.14, T=33.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_flintasamt1expnext12m, 63)`: S=0.56, F=0.41, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasamt1expnext12m, 10)`: S=0.10, F=0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasamt1expnext12m, 22))`: S=0.33, F=0.15, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expnext12m)`: S=0.39, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expnext12m / close)`: S=0.24, F=0.10, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+2.5%
  - 2020: S=0.24 (weak), ret=+1.9%
  - 2021: S=1.10 (moderate), ret=+7.9%
  - 2022: S=0.63 (moderate), ret=+3.5%
  - 2023: S=0.21 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 7.46% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 6.3% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.64, excess kurtosis +3.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.22, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.30%; worst month: -3.04%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.15
- Sideways: S=0.10
- Bear: S=-0.93

## Negated Direction
Best negated: `rank(-1 * fnd2_a_flintasamt1expnext12m)` S=0.39, F=0.24, INFERIOR
Direction gap: -0.17 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasamt1expnext12m)`: S=0.39, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expnext12m / close)`: S=0.24, F=0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expnext12m, 5))`: S=0.35, F=0.14, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasamt1expnext12m / close)` | TOP3000 | 0.55 | 0.29 | 7.5% | 100% | bull-only |
| `rank(fnd2_a_flintasamt1expnext12m)` | TOP3000 | 0.29 | 0.12 | 22.8% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expnext12m, 5))` | TOP1000 | 0.31 | 0.11 | 23.0% | 40% | all-weather |
| `rank(fnd2_a_flintasamt1expnext12m / close)` | TOP1000 | 0.16 | 0.06 | 14.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expytwo: 0.996 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.990 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.971 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.961 (strongly positively correlated)
- fn_amortization_of_intangible_assets_q: 0.944 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
