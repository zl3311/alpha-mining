---
field: fn_comp_non_opt_vested_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.55
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1412
ann_vol: 0.0719
hit_rate: 0.498
rolling_sharpe_min: -1.337
rolling_sharpe_max: 3.412
redundancy_cluster: 60
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.28
---
# fn_comp_non_opt_vested_a (fundamental2)

*The number of equity-based payment instruments, excluding stock (or unit) options, that vested during the reporting period.*

## Signal Profile
- `rank(fn_comp_non_opt_vested_a)`: S=0.51, F=0.19, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_vested_a / close)`: S=0.55, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_non_opt_vested_a, 5))`: S=0.48, F=0.21, T=34.5%, INFERIOR (TOP1000)
- `-rank(fn_comp_non_opt_vested_a)`: S=-0.18, F=-0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_vested_a, 5))`: S=0.15, F=0.05, T=30.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_non_opt_vested_a, 22)`: S=-0.06, F=-0.01, T=23.0%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_vested_a, 10)`: S=-0.66, F=-0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_vested_a, 22))`: S=-0.13, F=-0.04, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_vested_a)`: S=0.27, F=0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_vested_a / close)`: S=-0.15, F=-0.05, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.7%
  - 2020: S=2.15 (strong), ret=+16.2%
  - 2021: S=0.19 (weak), ret=+1.1%
  - 2022: S=-0.37 (negative), ret=-3.1%
  - 2023: S=0.55 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 14.12% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +4.0%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.36, excess kurtosis +1.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 3.41, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.91%; worst month: -4.26%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.42
- Sideways: S=-0.35
- Bear: S=2.47

## Negated Direction
Best negated: `rank(-1 * fn_comp_non_opt_vested_a)` S=0.27, F=0.11, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_vested_a)`: S=0.27, F=0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_vested_a / close)`: S=-0.15, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_vested_a, 5))`: S=0.15, F=0.05, T=30.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_non_opt_vested_a / close)` | TOP3000 | 0.55 | 0.31 | 14.1% | 80% | mixed |
| `rank(fn_comp_non_opt_vested_a / close)` | TOP1000 | 0.46 | 0.23 | 11.3% | 80% | mixed |
| `rank(ts_delta(fn_comp_non_opt_vested_a, 5))` | TOP1000 | 0.47 | 0.21 | 19.8% | 60% | all-weather |
| `rank(fn_comp_non_opt_vested_a)` | TOP3000 | 0.52 | 0.19 | 5.2% | 100% | mixed |
| `rank(fn_comp_non_opt_vested_a / close)` | TOP500 | 0.35 | 0.14 | 9.1% | 80% | all-weather |
| `rank(ts_delta(fn_comp_non_opt_vested_a, 5))` | TOP500 | 0.31 | 0.13 | 32.7% | 60% | mixed |
| `rank(fn_comp_non_opt_vested_a / close)` | TOP200 | 0.17 | 0.05 | 11.5% | 60% | mixed |
| `rank(fn_comp_non_opt_vested_a)` | TOP1000 | 0.18 | 0.04 | 6.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_non_opt_grants_a: 0.960 (strongly positively correlated)
- call_breakeven_10: -0.897 (strongly negatively correlated)
- option_breakeven_60: -0.897 (strongly negatively correlated)
- option_breakeven_30: -0.897 (strongly negatively correlated)
- call_breakeven_20: -0.897 (strongly negatively correlated)

Redundancy cluster #60: 3 similar fields, mean |rho| 0.722 (representative: fnd2_dfdtxasoprlcarryfwd). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
