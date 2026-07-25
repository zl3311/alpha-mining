---
field: fnd2_a_ltrmdmrepoplinnext12m
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.77
best_fitness: 0.47
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.2728
ann_vol: 0.1521
hit_rate: 0.4931
rolling_sharpe_min: -1.411
rolling_sharpe_max: 3.441
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.25
---
# fnd2_a_ltrmdmrepoplinnext12m (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing in the next fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepoplinnext12m)`: S=0.03, F=0.00, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepoplinnext12m / close)`: S=0.31, F=0.10, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepoplinnext12m, 5))`: S=0.77, F=0.47, T=31.6%, INFERIOR (TOP500)
- `-rank(fnd2_a_ltrmdmrepoplinnext12m)`: S=0.04, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinnext12m, 5))`: S=-0.28, F=-0.11, T=26.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_ltrmdmrepoplinnext12m, 22)`: S=-0.19, F=-0.08, T=14.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepoplinnext12m, 10)`: S=-0.24, F=-0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepoplinnext12m, 22))`: S=-0.25, F=-0.11, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinnext12m)`: S=0.52, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinnext12m / close)`: S=0.26, F=0.11, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+8.9%
  - 2020: S=-0.99 (negative), ret=-16.1%
  - 2021: S=2.37 (strong), ret=+44.4%
  - 2022: S=1.79 (strong), ret=+23.1%
  - 2023: S=-0.31 (negative), ret=-4.3%

## Risk & Drawdown
- Max drawdown: 27.28% over 572 days (recovered)
- Annualized: return +11.4%, volatility 15.2% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.45, excess kurtosis +8.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 3.44, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +13.89%; worst month: -10.44%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.19
- Sideways: S=0.39
- Bear: S=0.65

## Negated Direction
Best negated: `rank(-1 * fnd2_a_ltrmdmrepoplinnext12m)` S=0.52, F=0.31, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepoplinnext12m)`: S=0.52, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinnext12m / close)`: S=0.26, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinnext12m, 5))`: S=-0.28, F=-0.11, T=26.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinnext12m, 5))` | TOP500 | 0.75 | 0.47 | 27.3% | 60% | all-weather |
| `rank(fnd2_a_ltrmdmrepoplinnext12m / close)` | TOP3000 | 0.29 | 0.10 | 8.4% | 60% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplinnext12m / close)` | TOP1000 | 0.26 | 0.08 | 6.8% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinnext12m, 5))` | TOP3000 | 0.21 | 0.07 | 23.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_line_of_credit_facility_amount_out_a: 0.225 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinytwo: 0.170 (weakly positively correlated)
- fnd6_cidergl: 0.168 (weakly positively correlated)
- fn_effect_of_exchange_rate_on_cash_and_equiv_a: 0.153 (weakly positively correlated)
- fnd2_ebitfr: 0.145 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
