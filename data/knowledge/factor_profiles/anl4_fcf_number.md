---
field: anl4_fcf_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.61
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 9
max_drawdown: 0.1798
ann_vol: 0.0907
hit_rate: 0.4899
rolling_sharpe_min: -1.468
rolling_sharpe_max: 3.05
negated_best_sharpe: 0.41
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.2
---
# anl4_fcf_number (analyst4)

*Free Cash Flow - number of estimations*

## Signal Profile
- `rank(anl4_fcf_number)`: S=0.34, F=0.17, T=4.6%, INFERIOR (TOP200)
- `rank(anl4_fcf_number / close)`: S=0.41, F=0.22, T=3.2%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_fcf_number, 5))`: S=0.19, F=0.06, T=33.8%, INFERIOR (TOP200)
- `-rank(anl4_fcf_number)`: S=-0.34, F=-0.11, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_number, 5))`: S=0.41, F=0.14, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcf_number, 63)`: S=0.45, F=0.17, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_number, 10)`: S=0.61, F=0.30, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_number, 22))`: S=-0.18, F=-0.05, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_number)`: S=-0.35, F=-0.14, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_number / close)`: S=-0.41, F=-0.22, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.72 (negative), ret=-4.2%
  - 2020: S=2.15 (strong), ret=+19.3%
  - 2021: S=-0.53 (negative), ret=-5.6%
  - 2022: S=0.44 (weak), ret=+4.2%
  - 2023: S=0.56 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 17.98% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +3.8%, volatility 9.1% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.31, excess kurtosis +0.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.47, max 3.05, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +9.05%; worst month: -5.63%
Positive months: 48%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.51
- Sideways: S=-0.62
- Bear: S=2.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcf_number, 5))` S=0.41, F=0.14, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcf_number)`: S=-0.35, F=-0.14, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_number / close)`: S=-0.41, F=-0.22, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_number, 5))`: S=0.41, F=0.14, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_number / close)` | TOP500 | 0.42 | 0.22 | 18.0% | 60% | bear-only |
| `rank(anl4_fcf_number / close)` | TOP200 | 0.38 | 0.19 | 18.5% | 80% | mixed |
| `rank(anl4_fcf_number)` | TOP200 | 0.33 | 0.17 | 13.9% | 40% | bull-only |
| `rank(anl4_fcf_number)` | TOP500 | 0.36 | 0.14 | 7.5% | 80% | mixed |
| `rank(anl4_fcf_number)` | TOP1000 | 0.36 | 0.11 | 5.4% | 80% | weak |
| `rank(anl4_fcf_number / close)` | TOP3000 | 0.20 | 0.09 | 41.5% | 40% | bear-only |
| `rank(anl4_fcf_number / close)` | TOP1000 | 0.18 | 0.07 | 27.1% | 40% | bear-only |
| `rank(ts_delta(anl4_fcf_number, 5))` | TOP200 | 0.20 | 0.06 | 30.3% | 80% | weak |
| `rank(ts_delta(anl4_fcf_number, 5))` | TOP3000 | 0.28 | 0.05 | 12.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_number: 0.816 (strongly positively correlated)
- anl4_qfd1_az_cfps_number: 0.788 (strongly positively correlated)
- anl4_qf_az_cfps_number: 0.788 (strongly positively correlated)
- put_breakeven_1080: -0.771 (strongly negatively correlated)
- put_breakeven_720: -0.771 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
