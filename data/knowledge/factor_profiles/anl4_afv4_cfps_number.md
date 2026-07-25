---
field: anl4_afv4_cfps_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.24
best_fitness: 0.1
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.2128
ann_vol: 0.0931
hit_rate: 0.4777
rolling_sharpe_min: -2.023
rolling_sharpe_max: 2.678
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.04
---
# anl4_afv4_cfps_number (analyst4)

*Cash Flow Per Share - number of estimations for annual frequency*

## Signal Profile
- `rank(anl4_afv4_cfps_number)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP1000)
- `rank(anl4_afv4_cfps_number / close)`: S=0.24, F=0.10, T=2.0%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_cfps_number, 5))`: S=0.11, F=0.03, T=35.8%, INFERIOR (TOP200)
- `-rank(anl4_afv4_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_number, 5))`: S=0.10, F=0.02, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_cfps_number, 22)`: S=0.22, F=0.07, T=32.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_cfps_number, 10)`: S=0.06, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_cfps_number, 22))`: S=0.24, F=0.08, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_number)`: S=0.20, F=0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_number / close)`: S=-0.18, F=-0.06, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.43 (negative), ret=-2.5%
  - 2020: S=1.27 (moderate), ret=+13.5%
  - 2021: S=-0.34 (negative), ret=-3.5%
  - 2022: S=0.13 (weak), ret=+1.3%
  - 2023: S=0.32 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 21.28% over 1015 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 9.3% (fraction of booksize)
- Hit rate: 47.8% positive days
- Tail shape: skew +0.61, excess kurtosis +1.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.02, max 2.68, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +8.81%; worst month: -7.73%
Positive months: 46%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.63
- Sideways: S=-0.67
- Bear: S=1.97

## Negated Direction
Best negated: `rank(-1 * anl4_afv4_cfps_number)` S=0.20, F=0.06, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_cfps_number)`: S=0.20, F=0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_number / close)`: S=-0.18, F=-0.06, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_number, 5))`: S=0.10, F=0.02, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_cfps_number / close)` | TOP1000 | 0.25 | 0.10 | 21.3% | 60% | bear-only |
| `rank(anl4_afv4_cfps_number / close)` | TOP3000 | 0.17 | 0.06 | 32.3% | 40% | bear-only |
| `rank(anl4_afv4_cfps_number / close)` | TOP500 | 0.19 | 0.06 | 22.4% | 60% | mixed |
| `rank(ts_delta(anl4_afv4_cfps_number, 5))` | TOP200 | 0.11 | 0.03 | 48.5% | 60% | mixed |
| `rank(ts_delta(anl4_afv4_cfps_number, 5))` | TOP3000 | 0.14 | 0.02 | 22.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_cfps_number: 0.922 (strongly positively correlated)
- anl4_qf_az_cfps_number: 0.922 (strongly positively correlated)
- anl4_afv4_div_number: 0.904 (strongly positively correlated)
- anl4_qf_az_div_number: 0.875 (strongly positively correlated)
- anl4_qfd1_az_div_number: 0.875 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
