---
field: fnd6_cstkcv
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.94
best_fitness: 1.03
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1131
ann_vol: 0.0579
hit_rate: 0.4785
rolling_sharpe_min: -2.686
rolling_sharpe_max: 2.478
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 1.03
n_negated_sims: 10
direction_gap: 0.59
---
# fnd6_cstkcv (fundamental6)

*Common Stock-Carrying Value*

## Signal Profile
- `rank(fnd6_cstkcv)`: S=0.23, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_cstkcv / close)`: S=0.35, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cstkcv, 5))`: S=-0.13, F=-0.04, T=30.6%, INFERIOR (TOP3000)
- `-rank(fnd6_cstkcv)`: S=-0.13, F=-0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cstkcv, 5))`: S=0.94, F=1.03, T=17.6%, AVERAGE (TOP3000)
- `-ts_zscore(fnd6_cstkcv, 63)`: S=0.16, F=0.09, T=8.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cstkcv, 10)`: S=-0.39, F=-0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cstkcv, 22))`: S=-0.29, F=-0.19, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcv)`: S=-0.13, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcv / close)`: S=-0.25, F=-0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.33, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.93 (negative), ret=-5.6%
  - 2020: S=-0.51 (negative), ret=-3.1%
  - 2021: S=1.77 (strong), ret=+11.0%
  - 2022: S=1.49 (moderate), ret=+11.7%
  - 2023: S=-1.19 (negative), ret=-4.5%

## Risk & Drawdown
- Max drawdown: 11.31% over 854 days (recovered)
- Annualized: return +1.9%, volatility 5.8% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.08, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.69, max 2.48, latest -1.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.23%; worst month: -2.21%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=-1.11
- Bear: S=-1.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cstkcv, 5))` S=0.94, F=1.03, AVERAGE
Direction gap: +0.59 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_cstkcv)`: S=-0.13, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cstkcv / close)`: S=-0.25, F=-0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cstkcv, 5))`: S=0.94, F=1.03, T=17.6%, AVERAGE (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cstkcv / close)` | TOP3000 | 0.33 | 0.14 | 11.3% | 40% | bull-only |
| `rank(fnd6_cstkcv / close)` | TOP1000 | 0.25 | 0.10 | 11.0% | 40% | bull-only |
| `rank(fnd6_cstkcv / close)` | TOP500 | 0.23 | 0.10 | 15.3% | 40% | bull-only |
| `rank(fnd6_cstkcv)` | TOP3000 | 0.22 | 0.09 | 23.2% | 40% | bull-only |
| `rank(fnd6_cstkcv)` | TOP1000 | 0.11 | 0.04 | 19.1% | 40% | bull-only |
| `rank(fnd6_cstkcv)` | TOP500 | 0.11 | 0.04 | 18.1% | 40% | bull-only |
| `rank(fnd6_cstkcv / close)` | TOP200 | 0.09 | 0.03 | 23.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cstkcvq: 0.849 (strongly positively correlated)
- net_debt_amount: 0.824 (strongly positively correlated)
- est_fcf_ps: 0.811 (strongly positively correlated)
- fnd6_dxd2: 0.801 (strongly positively correlated)
- fnd6_dd2: 0.799 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
