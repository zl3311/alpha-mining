---
field: fnd6_sstk
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.0
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.145
ann_vol: 0.0624
hit_rate: 0.5158
rolling_sharpe_min: -1.305
rolling_sharpe_max: 4.13
negated_best_sharpe: 1.0
negated_best_template: rank_neg_delta
negated_best_fitness: 0.6
n_negated_sims: 10
direction_gap: 0.37
---
# fnd6_sstk (fundamental6)

*Sale of Common and Preferred Stock*

## Signal Profile
- `rank(fnd6_sstk)`: S=0.49, F=0.22, T=2.1%, INFERIOR (TOP500)
- `rank(fnd6_sstk / close)`: S=0.63, F=0.35, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_sstk, 5))`: S=-0.27, F=-0.12, T=30.9%, INFERIOR (TOP200)
- `-rank(fnd6_sstk)`: S=0.06, F=0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sstk, 5))`: S=1.00, F=0.60, T=35.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_sstk, 22)`: S=0.10, F=0.03, T=26.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_sstk, 10)`: S=-0.52, F=-0.31, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_sstk, 22))`: S=0.07, F=0.02, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sstk)`: S=0.40, F=0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sstk / close)`: S=0.37, F=0.17, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.73 (strong), ret=+5.4%
  - 2020: S=3.17 (strong), ret=+14.7%
  - 2021: S=-0.34 (negative), ret=-2.6%
  - 2022: S=-0.16 (negative), ret=-1.4%
  - 2023: S=0.67 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 14.50% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +3.9%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.25, excess kurtosis +1.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 4.13, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.30%; worst month: -3.94%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.10
- Sideways: S=-0.06
- Bear: S=2.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_sstk, 5))` S=1.00, F=0.60, INFERIOR
Direction gap: +0.37 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_sstk)`: S=0.40, F=0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sstk / close)`: S=0.37, F=0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sstk, 5))`: S=1.00, F=0.60, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_sstk / close)` | TOP500 | 0.63 | 0.35 | 14.5% | 60% | mixed |
| `rank(fnd6_sstk)` | TOP500 | 0.49 | 0.22 | 10.9% | 80% | mixed |
| `rank(fnd6_sstk / close)` | TOP200 | 0.18 | 0.06 | 33.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_options_out_number_a: 0.680 (moderately positively correlated)
- fnd6_newa1v1300_fincf: 0.666 (moderately positively correlated)
- cashflow_fin: 0.665 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.655 (moderately positively correlated)
- unsystematic_risk_last_30_days: 0.648 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
