---
field: cash_flow_from_investing
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.27
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.144
ann_vol: 0.0907
hit_rate: 0.5198
rolling_sharpe_min: -1.041
rolling_sharpe_max: 2.369
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.05
---
# cash_flow_from_investing (analyst4)

*Cash Flow from Investing - Value*

## Signal Profile
- `rank(cash_flow_from_investing)`: S=0.46, F=0.26, T=2.4%, INFERIOR (TOP200)
- `rank(cash_flow_from_investing / close)`: S=0.46, F=0.27, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(cash_flow_from_investing, 5))`: S=0.28, F=0.06, T=36.3%, INFERIOR (TOP500)
- `-rank(cash_flow_from_investing)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_investing, 5))`: S=0.08, F=0.01, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(cash_flow_from_investing, 22)`: S=0.12, F=0.02, T=38.7%, INFERIOR (TOP3000)
- `ts_mean(cash_flow_from_investing, 10)`: S=0.40, F=0.24, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cash_flow_from_investing, 22))`: S=-0.08, F=-0.01, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_investing)`: S=0.24, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_investing / close)`: S=0.41, F=0.17, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.4%
  - 2020: S=1.78 (strong), ret=+18.8%
  - 2021: S=0.30 (weak), ret=+2.8%
  - 2022: S=0.10 (weak), ret=+1.0%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 14.40% over 785 days (not yet recovered, ongoing at window end)
- Annualized: return +4.3%, volatility 9.1% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.22, excess kurtosis +1.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 2.37, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +6.33%; worst month: -5.81%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.30
- Sideways: S=1.40
- Bear: S=1.67

## Negated Direction
Best negated: `rank(-1 * cash_flow_from_investing / close)` S=0.41, F=0.17, INFERIOR
Direction gap: -0.05 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cash_flow_from_investing)`: S=0.24, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_investing / close)`: S=0.41, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_investing, 5))`: S=0.08, F=0.01, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash_flow_from_investing / close)` | TOP200 | 0.48 | 0.27 | 14.4% | 80% | bear-only |
| `rank(cash_flow_from_investing)` | TOP200 | 0.48 | 0.26 | 15.2% | 80% | bear-only |
| `rank(ts_delta(cash_flow_from_investing, 5))` | TOP500 | 0.28 | 0.06 | 14.0% | 60% | bear-only |
| `rank(ts_delta(cash_flow_from_investing, 5))` | TOP1000 | 0.25 | 0.05 | 15.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_ebitda_std: -0.568 (moderately negatively correlated)
- fnd6_mfmq_cheq: -0.547 (moderately negatively correlated)
- cash_st: -0.545 (moderately negatively correlated)
- fnd6_newa1v1300_che: -0.545 (moderately negatively correlated)
- fn_goodwill_acquired_during_period_a: -0.517 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
