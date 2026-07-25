---
field: fnd2_asdm
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.74
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0917
ann_vol: 0.07
hit_rate: 0.5028
rolling_sharpe_min: -0.919
rolling_sharpe_max: 2.207
redundancy_cluster: 1
negated_best_sharpe: 0.11
negated_best_template: neg_rank_level
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.63
---
# fnd2_asdm (fundamental2)

*Assets, Domestic*

## Signal Profile
- `rank(fnd2_asdm)`: S=0.40, F=0.22, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_asdm / close)`: S=0.74, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_asdm, 5))`: S=0.67, F=0.33, T=33.5%, INFERIOR (TOP3000)
- `-rank(fnd2_asdm)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_asdm, 5))`: S=0.10, F=0.03, T=29.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_asdm, 22)`: S=0.32, F=0.18, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd2_asdm, 10)`: S=0.10, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_asdm, 22))`: S=0.26, F=0.11, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_asdm)`: S=0.11, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_asdm / close)`: S=0.06, F=0.02, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.29 (negative), ret=-1.4%
  - 2020: S=0.69 (moderate), ret=+5.7%
  - 2021: S=0.98 (moderate), ret=+8.2%
  - 2022: S=1.25 (moderate), ret=+9.0%
  - 2023: S=0.95 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 9.17% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.58, excess kurtosis +2.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 2.21, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.87%; worst month: -4.06%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.49
- Sideways: S=0.44
- Bear: S=-1.05

## Negated Direction
Best negated: `rank(-1 * fnd2_asdm)` S=0.11, F=0.04, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_asdm)`: S=0.11, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_asdm / close)`: S=0.06, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_asdm, 5))`: S=0.10, F=0.03, T=29.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_asdm / close)` | TOP3000 | 0.75 | 0.48 | 9.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_asdm, 5))` | TOP3000 | 0.70 | 0.33 | 13.6% | 100% | mixed |
| `rank(fnd2_asdm)` | TOP3000 | 0.40 | 0.22 | 23.6% | 80% | bull-only |
| `rank(fnd2_asdm / close)` | TOP1000 | 0.21 | 0.08 | 12.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_rvndm: 0.924 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.890 (strongly positively correlated)
- fn_def_tax_liab_a: 0.889 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.884 (strongly positively correlated)
- fn_ppne_gross_a: 0.879 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
