---
field: fn_mne_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.71
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1035
ann_vol: 0.0855
hit_rate: 0.4769
rolling_sharpe_min: -0.802
rolling_sharpe_max: 2.147
redundancy_cluster: 1
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.34
---
# fn_mne_a (fundamental2)

*Amount before accumulated depreciation of tangible personal property used to produce goods and services, including, but is not limited to, tools, dies and molds, computer and office equipment.*

## Signal Profile
- `rank(fn_mne_a)`: S=0.43, F=0.28, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_mne_a / close)`: S=0.71, F=0.49, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_mne_a, 5))`: S=-0.17, F=-0.04, T=34.1%, INFERIOR (TOP3000)
- `-rank(fn_mne_a)`: S=-0.20, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_mne_a, 5))`: S=0.37, F=0.16, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_mne_a, 22)`: S=0.21, F=0.10, T=24.0%, INFERIOR (TOP3000)
- `ts_mean(fn_mne_a, 10)`: S=-0.31, F=-0.15, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_mne_a, 22))`: S=0.13, F=0.04, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_mne_a)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_mne_a / close)`: S=0.05, F=0.01, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.2%
  - 2020: S=-0.12 (negative), ret=-1.1%
  - 2021: S=1.06 (moderate), ret=+11.9%
  - 2022: S=1.70 (strong), ret=+16.0%
  - 2023: S=0.21 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 10.35% over 237 days (recovered)
- Annualized: return +5.9%, volatility 8.6% (fraction of booksize)
- Hit rate: 47.7% positive days
- Tail shape: skew +0.47, excess kurtosis +3.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.15, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.62%; worst month: -3.54%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.94
- Sideways: S=0.25
- Bear: S=-1.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_mne_a, 5))` S=0.37, F=0.16, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_mne_a)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_mne_a / close)`: S=0.05, F=0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_mne_a, 5))`: S=0.37, F=0.16, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_mne_a / close)` | TOP3000 | 0.69 | 0.49 | 10.3% | 80% | bull-only |
| `rank(fn_mne_a)` | TOP3000 | 0.42 | 0.28 | 36.0% | 80% | bull-only |
| `rank(fn_mne_a / close)` | TOP1000 | 0.25 | 0.13 | 21.4% | 40% | bull-only |
| `rank(fn_mne_a)` | TOP1000 | 0.19 | 0.09 | 38.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.983 (strongly positively correlated)
- fn_ppne_gross_a: 0.973 (strongly positively correlated)
- fnd6_dpvieb: 0.963 (strongly positively correlated)
- fnd6_newa1v1300_dpact: 0.962 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.950 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
