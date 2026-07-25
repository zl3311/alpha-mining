---
field: anl4_ebitda_std
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2552
ann_vol: 0.1292
hit_rate: 0.4891
rolling_sharpe_min: -1.615
rolling_sharpe_max: 1.963
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.31
---
# anl4_ebitda_std (analyst4)

*Earnings before interest, taxes, depreciation, and amortization - standard deviation of estimations*

## Signal Profile
- `rank(anl4_ebitda_std)`: S=0.29, F=0.12, T=5.8%, INFERIOR (TOP1000)
- `rank(anl4_ebitda_std / close)`: S=0.25, F=0.13, T=6.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ebitda_std, 5))`: S=-0.01, F=0.00, T=36.7%, INFERIOR (TOP200)
- `-rank(anl4_ebitda_std)`: S=-0.29, F=-0.12, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_std, 5))`: S=0.56, F=0.16, T=39.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ebitda_std, 63)`: S=0.34, F=0.11, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_std, 10)`: S=-0.03, F=-0.01, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_std, 22))`: S=0.03, F=0.00, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_std)`: S=-0.29, F=-0.12, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_std / close)`: S=-0.12, F=-0.03, T=5.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.27, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+4.7%
  - 2020: S=-0.95 (negative), ret=-12.8%
  - 2021: S=0.38 (weak), ret=+5.4%
  - 2022: S=0.89 (moderate), ret=+14.4%
  - 2023: S=0.59 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 25.52% over 416 days (recovered)
- Annualized: return +3.5%, volatility 12.9% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +1.04, excess kurtosis +11.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 1.96, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.67%; worst month: -8.76%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.50
- Sideways: S=-1.04
- Bear: S=0.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebitda_std, 5))` S=0.56, F=0.16, INFERIOR
Direction gap: +0.31 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ebitda_std)`: S=-0.29, F=-0.12, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_std / close)`: S=-0.12, F=-0.03, T=5.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_std, 5))`: S=0.56, F=0.16, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_std / close)` | TOP200 | 0.27 | 0.13 | 25.5% | 80% | mixed |
| `rank(anl4_ebitda_std)` | TOP1000 | 0.29 | 0.12 | 21.7% | 80% | bull-only |
| `rank(anl4_ebitda_std)` | TOP3000 | 0.27 | 0.10 | 16.4% | 80% | bull-only |
| `rank(anl4_ebitda_std)` | TOP200 | 0.14 | 0.05 | 32.3% | 80% | bull-only |
| `rank(anl4_ebitda_std)` | TOP500 | 0.14 | 0.04 | 28.6% | 80% | bull-only |
| `rank(anl4_ebitda_std / close)` | TOP1000 | 0.12 | 0.03 | 10.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- cash_flow_from_investing: -0.568 (moderately negatively correlated)
- fnd6_mfmq_cheq: 0.546 (moderately positively correlated)
- cash_st: 0.544 (moderately positively correlated)
- fnd6_newqv1300_chq: 0.529 (moderately positively correlated)
- fnd6_newa1v1300_che: 0.519 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
