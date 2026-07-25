---
field: fnd6_newa1v1300_che
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.4
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1443
ann_vol: 0.0857
hit_rate: 0.4907
rolling_sharpe_min: -0.989
rolling_sharpe_max: 2.676
redundancy_cluster: 31
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.16
---
# fnd6_newa1v1300_che (fundamental6)

*Cash and Short-Term Investments*

## Signal Profile
- `rank(fnd6_newa1v1300_che)`: S=0.57, F=0.34, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_che / close)`: S=0.62, F=0.40, T=2.2%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_che, 5))`: S=0.18, F=0.06, T=34.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_che)`: S=-0.30, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_che, 5))`: S=0.46, F=0.18, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_che, 22)`: S=0.25, F=0.10, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_che, 10)`: S=0.37, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_che, 22))`: S=-0.45, F=-0.21, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_che)`: S=-0.30, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_che / close)`: S=-0.50, F=-0.28, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.3%
  - 2020: S=-0.24 (negative), ret=-2.2%
  - 2021: S=0.22 (weak), ret=+2.8%
  - 2022: S=2.28 (strong), ret=+15.8%
  - 2023: S=1.90 (strong), ret=+8.7%

## Risk & Drawdown
- Max drawdown: 14.43% over 259 days (recovered)
- Annualized: return +5.4%, volatility 8.6% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.56, excess kurtosis +3.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.68, latest 2.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.65%; worst month: -6.06%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.60
- Sideways: S=0.05
- Bear: S=-1.27

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_che, 5))` S=0.46, F=0.18, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_che)`: S=-0.30, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_che / close)`: S=-0.50, F=-0.28, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_che, 5))`: S=0.46, F=0.18, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_che / close)` | TOP500 | 0.63 | 0.40 | 14.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_che)` | TOP3000 | 0.57 | 0.34 | 24.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_che / close)` | TOP3000 | 0.55 | 0.31 | 9.8% | 80% | mixed |
| `rank(fnd6_newa1v1300_che / close)` | TOP1000 | 0.50 | 0.28 | 10.7% | 100% | bull-only |
| `rank(fnd6_newa1v1300_che)` | TOP1000 | 0.30 | 0.14 | 27.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_che)` | TOP500 | 0.26 | 0.12 | 37.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_che, 5))` | TOP200 | 0.18 | 0.06 | 65.0% | 40% | weak |
| `rank(ts_delta(fnd6_newa1v1300_che, 5))` | TOP3000 | 0.19 | 0.04 | 20.8% | 60% | weak |
| `rank(fnd6_newa1v1300_che / close)` | TOP200 | 0.13 | 0.04 | 26.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ch: 0.978 (strongly positively correlated)
- fnd6_mfmq_cheq: 0.950 (strongly positively correlated)
- cash_st: 0.950 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.933 (strongly positively correlated)
- fnd6_newa2v1300_stkco: 0.876 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
