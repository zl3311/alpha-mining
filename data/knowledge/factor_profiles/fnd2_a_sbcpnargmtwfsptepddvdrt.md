---
field: fnd2_a_sbcpnargmtwfsptepddvdrt
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.75
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1488
ann_vol: 0.0996
hit_rate: 0.4907
rolling_sharpe_min: -1.678
rolling_sharpe_max: 1.997
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: 0.5
---
# fnd2_a_sbcpnargmtwfsptepddvdrt (fundamental2)

*The estimated dividend rate (a percentage of the share price) to be paid (expected dividends) to holders of the underlying shares over the option's term.*

## Signal Profile
- `rank(fnd2_a_sbcpnargmtwfsptepddvdrt)`: S=0.07, F=0.02, T=1.2%, INFERIOR (TOP1000)
- `rank(fnd2_a_sbcpnargmtwfsptepddvdrt / close)`: S=0.25, F=0.11, T=1.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd2_a_sbcpnargmtwfsptepddvdrt, 5))`: S=0.02, F=0.00, T=31.8%, INFERIOR (TOP3000)
- `-rank(fnd2_a_sbcpnargmtwfsptepddvdrt)`: S=-0.07, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmtwfsptepddvdrt, 5))`: S=0.75, F=0.45, T=28.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_sbcpnargmtwfsptepddvdrt, 22)`: S=-0.12, F=-0.05, T=11.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_sbcpnargmtwfsptepddvdrt, 10)`: S=0.20, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_sbcpnargmtwfsptepddvdrt, 22))`: S=-0.69, F=-0.50, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmtwfsptepddvdrt)`: S=0.23, F=0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmtwfsptepddvdrt / close)`: S=0.13, F=0.04, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.24, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.51 (negative), ret=-2.3%
  - 2020: S=-1.21 (negative), ret=-10.6%
  - 2021: S=1.33 (moderate), ret=+16.7%
  - 2022: S=1.20 (moderate), ret=+16.2%
  - 2023: S=-1.31 (negative), ret=-8.2%

## Risk & Drawdown
- Max drawdown: 14.88% over 852 days (recovered)
- Annualized: return +2.4%, volatility 10.0% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.36, excess kurtosis +3.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.00, latest -1.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.46%; worst month: -5.60%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.40
- Sideways: S=-0.53
- Bear: S=-1.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_sbcpnargmtwfsptepddvdrt, 5))` S=0.75, F=0.45, INFERIOR
Direction gap: +0.50 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_sbcpnargmtwfsptepddvdrt)`: S=0.23, F=0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmtwfsptepddvdrt / close)`: S=0.13, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmtwfsptepddvdrt, 5))`: S=0.75, F=0.45, T=28.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_sbcpnargmtwfsptepddvdrt / close)` | TOP1000 | 0.24 | 0.11 | 14.9% | 40% | bull-only |
| `rank(fnd2_a_sbcpnargmtwfsptepddvdrt / close)` | TOP3000 | 0.10 | 0.03 | 26.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_af_div_value: 0.943 (strongly positively correlated)
- cashflow_dividends: 0.927 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.926 (strongly positively correlated)
- anl4_afv4_div_mean: 0.905 (strongly positively correlated)
- anl4_afv4_div_median: 0.903 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
