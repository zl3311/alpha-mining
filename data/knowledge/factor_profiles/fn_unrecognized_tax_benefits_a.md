---
field: fn_unrecognized_tax_benefits_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.62
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0766
ann_vol: 0.0554
hit_rate: 0.5036
rolling_sharpe_min: -1.372
rolling_sharpe_max: 2.614
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.41
---
# fn_unrecognized_tax_benefits_a (fundamental2)

*Amount of unrecognized tax benefits.*

## Signal Profile
- `rank(fn_unrecognized_tax_benefits_a)`: S=0.35, F=0.16, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_unrecognized_tax_benefits_a / close)`: S=0.68, F=0.37, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_unrecognized_tax_benefits_a, 5))`: S=0.08, F=0.01, T=34.1%, INFERIOR (TOP3000)
- `-rank(fn_unrecognized_tax_benefits_a)`: S=-0.18, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_unrecognized_tax_benefits_a, 5))`: S=0.21, F=0.07, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_unrecognized_tax_benefits_a, 63)`: S=0.62, F=0.43, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fn_unrecognized_tax_benefits_a, 10)`: S=0.25, F=0.11, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_unrecognized_tax_benefits_a, 22))`: S=-0.50, F=-0.26, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_unrecognized_tax_benefits_a)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_unrecognized_tax_benefits_a / close)`: S=-0.20, F=-0.08, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+1.3%
  - 2020: S=0.23 (weak), ret=+1.3%
  - 2021: S=1.40 (moderate), ret=+10.3%
  - 2022: S=0.88 (moderate), ret=+5.5%
  - 2023: S=-0.11 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 7.66% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +3.7%, volatility 5.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.25, excess kurtosis +2.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 2.61, latest -0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.70%; worst month: -2.36%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.88
- Sideways: S=0.59
- Bear: S=-2.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_unrecognized_tax_benefits_a, 5))` S=0.21, F=0.07, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_unrecognized_tax_benefits_a)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_unrecognized_tax_benefits_a / close)`: S=-0.20, F=-0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_unrecognized_tax_benefits_a, 5))`: S=0.21, F=0.07, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_unrecognized_tax_benefits_a / close)` | TOP3000 | 0.66 | 0.37 | 7.7% | 80% | bull-only |
| `rank(fn_unrecognized_tax_benefits_a)` | TOP3000 | 0.34 | 0.16 | 20.7% | 60% | bull-only |
| `rank(fn_unrecognized_tax_benefits_a / close)` | TOP1000 | 0.32 | 0.15 | 14.0% | 40% | bull-only |
| `rank(fn_unrecognized_tax_benefits_a / close)` | TOP500 | 0.19 | 0.08 | 29.3% | 40% | bull-only |
| `rank(fn_unrecognized_tax_benefits_a)` | TOP1000 | 0.17 | 0.07 | 27.9% | 40% | bull-only |
| `rank(fn_unrecognized_tax_benefits_a / close)` | TOP200 | 0.10 | 0.03 | 34.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubend: 0.944 (strongly positively correlated)
- fnd6_txtubbegin: 0.927 (strongly positively correlated)
- fnd6_newa1v1300_lo: 0.870 (strongly positively correlated)
- fn_def_tax_liab_a: 0.868 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.867 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
