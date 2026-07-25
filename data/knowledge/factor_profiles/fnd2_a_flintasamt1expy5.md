---
field: fnd2_a_flintasamt1expy5
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.55
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1027
ann_vol: 0.0574
hit_rate: 0.4915
rolling_sharpe_min: -1.772
rolling_sharpe_max: 2.373
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: neg_rank_level
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.04
---
# fnd2_a_flintasamt1expy5 (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 5th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_flintasamt1expy5)`: S=0.29, F=0.12, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasamt1expy5 / close)`: S=0.52, F=0.25, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasamt1expy5, 5))`: S=0.33, F=0.15, T=28.7%, INFERIOR (TOP200)
- `-rank(fnd2_a_flintasamt1expy5)`: S=0.10, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expy5, 5))`: S=-0.03, F=0.00, T=33.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_flintasamt1expy5, 22)`: S=0.55, F=0.40, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasamt1expy5, 10)`: S=-0.15, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasamt1expy5, 22))`: S=-0.02, F=0.00, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expy5)`: S=0.51, F=0.34, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expy5 / close)`: S=0.40, F=0.21, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+1.7%
  - 2020: S=0.53 (moderate), ret=+3.9%
  - 2021: S=1.10 (moderate), ret=+7.3%
  - 2022: S=0.77 (moderate), ret=+4.0%
  - 2023: S=-0.54 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 10.27% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +3.0%, volatility 5.7% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.57, excess kurtosis +3.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.37, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.57%; worst month: -2.63%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.19
- Sideways: S=0.07
- Bear: S=-1.03

## Negated Direction
Best negated: `rank(-1 * fnd2_a_flintasamt1expy5)` S=0.51, F=0.34, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasamt1expy5)`: S=0.51, F=0.34, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expy5 / close)`: S=0.40, F=0.21, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expy5, 5))`: S=-0.03, F=0.00, T=33.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasamt1expy5 / close)` | TOP3000 | 0.52 | 0.25 | 10.3% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expy5, 5))` | TOP200 | 0.33 | 0.15 | 22.4% | 60% | all-weather |
| `rank(fnd2_a_flintasamt1expy5)` | TOP3000 | 0.28 | 0.12 | 19.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expythree: 0.983 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.977 (strongly positively correlated)
- fnd2_a_flintasamt1expnext12m: 0.971 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.949 (strongly positively correlated)
- fn_amortization_of_intangible_assets_q: 0.924 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
