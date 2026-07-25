---
field: fnd6_newa2v1300_seq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.6
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0895
ann_vol: 0.0694
hit_rate: 0.468
rolling_sharpe_min: -0.988
rolling_sharpe_max: 1.876
negated_best_sharpe: 0.23
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_newa2v1300_seq (fundamental6)

*Stockholders Equity - Parent*

## Signal Profile
- `rank(fnd6_newa2v1300_seq)`: S=0.41, F=0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_seq / close)`: S=0.46, F=0.23, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_seq, 5))`: S=0.32, F=0.15, T=33.5%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_seq)`: S=-0.13, F=-0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_seq, 5))`: S=-0.27, F=-0.11, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_seq, 63)`: S=0.60, F=0.38, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_seq, 10)`: S=0.06, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_seq, 22))`: S=0.09, F=0.02, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seq)`: S=0.23, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seq / close)`: S=0.13, F=0.04, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.41 (negative), ret=-1.8%
  - 2020: S=-0.09 (negative), ret=-0.7%
  - 2021: S=0.85 (moderate), ret=+7.4%
  - 2022: S=0.81 (moderate), ret=+5.4%
  - 2023: S=0.96 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 8.95% over 245 days (recovered)
- Annualized: return +3.1%, volatility 6.9% (fraction of booksize)
- Hit rate: 46.8% positive days
- Tail shape: skew +0.80, excess kurtosis +4.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.88, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.18%; worst month: -3.24%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.12
- Sideways: S=0.11
- Bear: S=-1.29

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_seq)` S=0.23, F=0.12, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_seq)`: S=0.23, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seq / close)`: S=0.13, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_seq, 5))`: S=-0.27, F=-0.11, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_seq)` | TOP3000 | 0.40 | 0.23 | 31.0% | 80% | bull-only |
| `rank(fnd6_newa2v1300_seq / close)` | TOP3000 | 0.45 | 0.23 | 8.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_seq, 5))` | TOP200 | 0.32 | 0.15 | 88.1% | 60% | weak |
| `rank(fnd6_newa2v1300_seq / close)` | TOP1000 | 0.31 | 0.15 | 12.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_seq, 5))` | TOP1000 | 0.32 | 0.09 | 17.6% | 80% | mixed |
| `rank(fnd6_newa2v1300_seq)` | TOP1000 | 0.12 | 0.04 | 33.4% | 60% | bull-only |
| `rank(fnd6_newa2v1300_seq / close)` | TOP500 | 0.09 | 0.03 | 25.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_teq: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_ceq: 0.997 (strongly positively correlated)
- fnd6_ceql: 0.993 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.967 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.958 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
