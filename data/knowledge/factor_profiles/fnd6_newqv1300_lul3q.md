---
field: fnd6_newqv1300_lul3q
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.77
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.4977
ann_vol: 0.2265
hit_rate: 0.4534
rolling_sharpe_min: -1.369
rolling_sharpe_max: 1.893
negated_best_sharpe: 0.7
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.07
---
# fnd6_newqv1300_lul3q (fundamental6)

*Liabilities Level 3 (Unobservable)*

## Signal Profile
- `rank(fnd6_newqv1300_lul3q)`: S=0.16, F=0.05, T=9.3%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_lul3q / close)`: S=0.20, F=0.06, T=9.3%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_lul3q, 5))`: S=0.27, F=0.10, T=45.0%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_lul3q)`: S=0.44, F=0.17, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lul3q, 5))`: S=0.27, F=0.08, T=48.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_lul3q, 22)`: S=0.41, F=0.24, T=31.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lul3q, 10)`: S=0.77, F=0.50, T=5.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lul3q, 22))`: S=0.16, F=0.05, T=24.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lul3q)`: S=0.66, F=0.28, T=6.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lul3q / close)`: S=0.70, F=0.33, T=6.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.27, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+3.4%
  - 2020: S=-0.39 (negative), ret=-8.9%
  - 2021: S=0.54 (moderate), ret=+15.0%
  - 2022: S=1.16 (moderate), ret=+24.5%
  - 2023: S=-0.22 (negative), ret=-3.5%

## Risk & Drawdown
- Max drawdown: 49.77% over 897 days (recovered)
- Annualized: return +6.2%, volatility 22.7% (fraction of booksize)
- Hit rate: 45.3% positive days
- Tail shape: skew +0.84, excess kurtosis +16.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 1.89, latest -0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +19.14%; worst month: -19.20%
Positive months: 47%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.06
- Sideways: S=-0.03
- Bear: S=0.78

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_lul3q / close)` S=0.70, F=0.33, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lul3q)`: S=0.66, F=0.28, T=6.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lul3q / close)`: S=0.70, F=0.33, T=6.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lul3q, 5))`: S=0.27, F=0.08, T=48.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_lul3q, 5))` | TOP200 | 0.27 | 0.10 | 49.8% | 60% | mixed |
| `rank(fnd6_newqv1300_lul3q / close)` | TOP500 | 0.19 | 0.06 | 14.3% | 40% | weak |
| `rank(fnd6_newqv1300_lul3q)` | TOP500 | 0.15 | 0.05 | 12.5% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_cstkcvq: -0.173 (weakly negatively correlated)
- fn_eff_income_tax_rate_continuing_operations_q: -0.163 (weakly negatively correlated)
- fnd2_dfdtxlbsgwllandintas: -0.159 (weakly negatively correlated)
- est_fcf_ps: -0.153 (weakly negatively correlated)
- fnd6_newqv1300_tstknq: -0.153 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
