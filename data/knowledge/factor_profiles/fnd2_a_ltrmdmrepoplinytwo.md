---
field: fnd2_a_ltrmdmrepoplinytwo
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.76
best_fitness: 0.44
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2578
ann_vol: 0.147
hit_rate: 0.519
rolling_sharpe_min: -1.076
rolling_sharpe_max: 1.981
negated_best_sharpe: 0.39
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.37
---
# fnd2_a_ltrmdmrepoplinytwo (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing in the 2nd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepoplinytwo)`: S=0.17, F=0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepoplinytwo / close)`: S=0.63, F=0.28, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))`: S=0.76, F=0.44, T=33.5%, INFERIOR (TOP1000)
- `-rank(fnd2_a_ltrmdmrepoplinytwo)`: S=0.16, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))`: S=-0.62, F=-0.34, T=32.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_ltrmdmrepoplinytwo, 22)`: S=0.09, F=0.03, T=14.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepoplinytwo, 10)`: S=-0.13, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepoplinytwo, 22))`: S=0.27, F=0.12, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinytwo)`: S=0.39, F=0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinytwo / close)`: S=0.20, F=0.06, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.98 (negative), ret=-12.7%
  - 2020: S=0.72 (moderate), ret=+12.4%
  - 2021: S=0.93 (moderate), ret=+12.8%
  - 2022: S=1.50 (moderate), ret=+21.3%
  - 2023: S=1.45 (moderate), ret=+19.3%

## Risk & Drawdown
- Max drawdown: 25.78% over 600 days (recovered)
- Annualized: return +10.8%, volatility 14.7% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.46, excess kurtosis +8.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 1.98, latest 1.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +13.48%; worst month: -6.83%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.79
- Sideways: S=0.17
- Bear: S=1.25

## Negated Direction
Best negated: `rank(-1 * fnd2_a_ltrmdmrepoplinytwo)` S=0.39, F=0.17, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepoplinytwo)`: S=0.39, F=0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinytwo / close)`: S=0.20, F=0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))`: S=-0.62, F=-0.34, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))` | TOP1000 | 0.74 | 0.44 | 25.8% | 80% | all-weather |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))` | TOP500 | 0.57 | 0.32 | 23.8% | 80% | all-weather |
| `rank(fnd2_a_ltrmdmrepoplinytwo / close)` | TOP3000 | 0.61 | 0.28 | 7.4% | 80% | mixed |
| `rank(fnd2_a_ltrmdmrepoplinytwo)` | TOP3000 | 0.15 | 0.04 | 13.1% | 60% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplinytwo / close)` | TOP1000 | 0.15 | 0.04 | 11.0% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinytwo, 5))` | TOP200 | 0.10 | 0.02 | 25.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_l1_a: 0.180 (weakly positively correlated)
- fnd2_a_gwllimrml: 0.176 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinnext12m: 0.170 (weakly positively correlated)
- fn_amortization_of_intangible_assets_a: 0.148 (weakly positively correlated)
- fnd2_currfrtxexp: 0.141 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
