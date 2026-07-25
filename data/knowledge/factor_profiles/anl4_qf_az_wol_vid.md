---
field: anl4_qf_az_wol_vid
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1112
ann_vol: 0.0785
hit_rate: 0.4964
rolling_sharpe_min: -1.304
rolling_sharpe_max: 1.747
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.92
n_negated_sims: 10
direction_gap: 0.99
---
# anl4_qf_az_wol_vid (analyst4)

*Dividend per share - The lowest value among forecasts*

## Signal Profile
- `rank(anl4_qf_az_wol_vid)`: S=-0.12, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qf_az_wol_vid / close)`: S=0.37, F=0.18, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qf_az_wol_vid, 5))`: S=0.39, F=0.09, T=37.1%, INFERIOR (TOP3000)
- `-rank(anl4_qf_az_wol_vid)`: S=0.12, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_wol_vid, 5))`: S=1.36, F=0.92, T=34.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_wol_vid, 22)`: S=0.13, F=0.03, T=33.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_wol_vid, 10)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_wol_vid, 22))`: S=0.26, F=0.07, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_vid)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_vid / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+2.1%
  - 2020: S=-0.92 (negative), ret=-6.4%
  - 2021: S=0.66 (moderate), ret=+6.1%
  - 2022: S=1.62 (strong), ret=+16.9%
  - 2023: S=-0.82 (negative), ret=-4.9%

## Risk & Drawdown
- Max drawdown: 11.12% over 534 days (recovered)
- Annualized: return +2.8%, volatility 7.8% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.19, excess kurtosis +1.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 1.75, latest -0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.32%; worst month: -3.96%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.72
- Sideways: S=-0.64
- Bear: S=-1.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_wol_vid, 5))` S=1.36, F=0.92, INFERIOR
Direction gap: +0.99 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_qf_az_wol_vid)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_vid / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_wol_vid, 5))`: S=1.36, F=0.92, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_wol_vid / close)` | TOP1000 | 0.36 | 0.18 | 11.1% | 60% | bull-only |
| `rank(anl4_qf_az_wol_vid / close)` | TOP3000 | 0.30 | 0.13 | 11.4% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_wol_vid, 5))` | TOP3000 | 0.39 | 0.09 | 14.3% | 60% | mixed |
| `rank(ts_delta(anl4_qf_az_wol_vid, 5))` | TOP500 | 0.10 | 0.02 | 21.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_wol_vid: 1.000 (strongly positively correlated)
- anl4_qf_az_div_median: 0.986 (strongly positively correlated)
- anl4_qfd1_az_div_median: 0.986 (strongly positively correlated)
- anl4_qf_az_div_mean: 0.985 (strongly positively correlated)
- dividend_estimate_average: 0.985 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
