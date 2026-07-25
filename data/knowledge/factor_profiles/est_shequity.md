---
field: est_shequity
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.65
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0865
ann_vol: 0.0611
hit_rate: 0.4785
rolling_sharpe_min: -1.132
rolling_sharpe_max: 2.071
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.28
---
# est_shequity (analyst4)

*Mean of SH Equity segment - mean of estimations*

## Signal Profile
- `rank(est_shequity)`: S=0.31, F=0.15, T=0.9%, INFERIOR (TOP3000)
- `rank(est_shequity / close)`: S=0.37, F=0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(est_shequity, 5))`: S=0.48, F=0.11, T=36.3%, INFERIOR (TOP3000)
- `-rank(est_shequity)`: S=-0.07, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_shequity, 5))`: S=0.65, F=0.22, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(est_shequity, 22)`: S=0.20, F=0.04, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(est_shequity, 10)`: S=-0.05, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(est_shequity, 22))`: S=-0.04, F=0.00, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * est_shequity)`: S=0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_shequity / close)`: S=-0.08, F=-0.02, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.34 (negative), ret=-1.4%
  - 2020: S=-0.37 (negative), ret=-2.7%
  - 2021: S=0.92 (moderate), ret=+7.1%
  - 2022: S=1.06 (moderate), ret=+5.8%
  - 2023: S=0.49 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 8.65% over 294 days (recovered)
- Annualized: return +2.2%, volatility 6.1% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.70, excess kurtosis +3.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.07, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.15%; worst month: -2.81%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.94
- Sideways: S=-0.15
- Bear: S=-2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_shequity, 5))` S=0.65, F=0.22, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_shequity)`: S=0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_shequity / close)`: S=-0.08, F=-0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_shequity, 5))`: S=0.65, F=0.22, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_shequity / close)` | TOP3000 | 0.37 | 0.16 | 8.6% | 60% | bull-only |
| `rank(est_shequity)` | TOP3000 | 0.30 | 0.15 | 31.4% | 80% | bull-only |
| `rank(ts_delta(est_shequity, 5))` | TOP3000 | 0.49 | 0.11 | 6.6% | 80% | weak |
| `rank(est_shequity / close)` | TOP1000 | 0.13 | 0.04 | 13.1% | 40% | bull-only |
| `rank(est_shequity / close)` | TOP500 | 0.07 | 0.02 | 26.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- est_tot_assets: 0.947 (strongly positively correlated)
- fnd6_teq: 0.942 (strongly positively correlated)
- fnd6_newa2v1300_seq: 0.940 (strongly positively correlated)
- fnd6_newa1v1300_ceq: 0.939 (strongly positively correlated)
- fnd6_ceql: 0.936 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
