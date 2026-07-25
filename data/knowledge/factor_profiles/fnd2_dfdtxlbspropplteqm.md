---
field: fnd2_dfdtxlbspropplteqm
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.96
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0915
ann_vol: 0.0634
hit_rate: 0.4899
rolling_sharpe_min: -1.04
rolling_sharpe_max: 2.253
redundancy_cluster: 1
negated_best_sharpe: 0.96
negated_best_template: rank_neg_delta
negated_best_fitness: 0.77
n_negated_sims: 10
direction_gap: 0.24
---
# fnd2_dfdtxlbspropplteqm (fundamental2)

*Amount of deferred tax liability attributable to taxable temporary differences from property, plant, and equipment.*

## Signal Profile
- `rank(fnd2_dfdtxlbspropplteqm)`: S=0.41, F=0.21, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxlbspropplteqm / close)`: S=0.72, F=0.43, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfdtxlbspropplteqm, 5))`: S=-0.14, F=-0.04, T=31.9%, INFERIOR (TOP500)
- `-rank(fnd2_dfdtxlbspropplteqm)`: S=0.00, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxlbspropplteqm, 5))`: S=0.96, F=0.77, T=25.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfdtxlbspropplteqm, 22)`: S=0.42, F=0.27, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxlbspropplteqm, 10)`: S=0.05, F=0.01, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxlbspropplteqm, 22))`: S=-0.12, F=-0.04, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbspropplteqm)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbspropplteqm / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.19 (negative), ret=-0.8%
  - 2020: S=0.71 (moderate), ret=+5.4%
  - 2021: S=0.58 (moderate), ret=+4.5%
  - 2022: S=1.49 (moderate), ret=+9.5%
  - 2023: S=0.85 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 9.15% over 406 days (recovered)
- Annualized: return +4.5%, volatility 6.3% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.32, excess kurtosis +2.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 2.25, latest 0.92

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.14%; worst month: -4.12%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.46
- Sideways: S=0.48
- Bear: S=-1.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxlbspropplteqm, 5))` S=0.96, F=0.77, INFERIOR
Direction gap: +0.24 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdtxlbspropplteqm)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbspropplteqm / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxlbspropplteqm, 5))`: S=0.96, F=0.77, T=25.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxlbspropplteqm / close)` | TOP3000 | 0.71 | 0.43 | 9.2% | 80% | bull-only |
| `rank(fnd2_dfdtxlbspropplteqm)` | TOP3000 | 0.40 | 0.21 | 22.8% | 80% | bull-only |
| `rank(fnd2_dfdtxlbspropplteqm)` | TOP500 | 0.14 | 0.05 | 32.9% | 40% | bull-only |
| `rank(fnd2_dfdtxlbspropplteqm / close)` | TOP500 | 0.12 | 0.04 | 23.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_def_tax_liab_a: 0.912 (strongly positively correlated)
- fn_ppne_gross_a: 0.897 (strongly positively correlated)
- fnd6_mfma1_dp: 0.895 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.895 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.894 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
