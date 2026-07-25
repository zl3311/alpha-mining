---
field: fn_ppne_gross_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.8
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0945
ann_vol: 0.0831
hit_rate: 0.4915
rolling_sharpe_min: -1.103
rolling_sharpe_max: 2.385
redundancy_cluster: 1
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.51
n_negated_sims: 10
direction_gap: 0.08
---
# fn_ppne_gross_a (fundamental2)

*Amount before accumulated depreciation, depletion, and amortization of physical assets used in the normal conduct of business and not intended for resale. Examples include, but are not limited to, land, buildings, machinery and equipment, office equipment, and furniture and fixtures.*

## Signal Profile
- `rank(fn_ppne_gross_a)`: S=0.50, F=0.35, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_ppne_gross_a / close)`: S=0.80, F=0.58, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_ppne_gross_a, 5))`: S=-0.31, F=-0.13, T=32.8%, INFERIOR (TOP200)
- `-rank(fn_ppne_gross_a)`: S=-0.28, F=-0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_ppne_gross_a, 5))`: S=0.88, F=0.51, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fn_ppne_gross_a, 22)`: S=0.65, F=0.50, T=25.4%, INFERIOR (TOP3000)
- `ts_mean(fn_ppne_gross_a, 10)`: S=-0.05, F=-0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_ppne_gross_a, 22))`: S=0.09, F=0.02, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_ppne_gross_a)`: S=-0.28, F=-0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_ppne_gross_a / close)`: S=-0.38, F=-0.22, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.79, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.3%
  - 2020: S=0.01 (weak), ret=+0.1%
  - 2021: S=1.29 (moderate), ret=+14.3%
  - 2022: S=1.58 (strong), ret=+13.9%
  - 2023: S=0.76 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 9.45% over 441 days (recovered)
- Annualized: return +6.6%, volatility 8.3% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.49, excess kurtosis +3.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 2.38, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.76%; worst month: -3.44%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.95
- Sideways: S=0.30
- Bear: S=-1.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_ppne_gross_a, 5))` S=0.88, F=0.51, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_ppne_gross_a)`: S=-0.28, F=-0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_ppne_gross_a / close)`: S=-0.38, F=-0.22, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_ppne_gross_a, 5))`: S=0.88, F=0.51, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_ppne_gross_a / close)` | TOP3000 | 0.79 | 0.58 | 9.4% | 100% | bull-only |
| `rank(fn_ppne_gross_a)` | TOP3000 | 0.49 | 0.35 | 35.0% | 80% | bull-only |
| `rank(fn_ppne_gross_a / close)` | TOP1000 | 0.37 | 0.22 | 17.6% | 40% | bull-only |
| `rank(fn_ppne_gross_a)` | TOP1000 | 0.27 | 0.16 | 38.3% | 40% | bull-only |
| `rank(fn_ppne_gross_a / close)` | TOP500 | 0.17 | 0.08 | 36.1% | 40% | bull-only |
| `rank(fn_ppne_gross_a)` | TOP500 | 0.05 | 0.02 | 56.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_mne_a: 0.973 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.972 (strongly positively correlated)
- fnd6_ppeveb: 0.972 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.970 (strongly positively correlated)
- fnd6_mfma1_dp: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
