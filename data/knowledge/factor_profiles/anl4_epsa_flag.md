---
field: anl4_epsa_flag
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.63
best_fitness: 0.89
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.2432
ann_vol: 0.1029
hit_rate: 0.498
rolling_sharpe_min: -1.149
rolling_sharpe_max: 2.47
redundancy_cluster: 72
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: -0.1
---
# anl4_epsa_flag (analyst4)

*Earnings per share adjusted by excluding extraordinary items and stock option expenses - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_epsa_flag)`: S=0.50, F=0.28, T=1.8%, INFERIOR (TOP1000)
- `rank(anl4_epsa_flag / close)`: S=0.55, F=0.37, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_epsa_flag, 5))`: S=0.50, F=0.30, T=33.6%, INFERIOR (TOP3000)
- `-rank(anl4_epsa_flag)`: S=-0.50, F=-0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsa_flag, 5))`: S=0.53, F=0.46, T=14.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_epsa_flag, 22)`: S=0.63, F=0.89, T=8.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsa_flag, 10)`: S=0.46, F=0.25, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_epsa_flag, 22))`: S=0.31, F=0.24, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsa_flag)`: S=0.09, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsa_flag / close)`: S=-0.55, F=-0.37, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.93 (moderate), ret=+5.1%
  - 2020: S=1.40 (moderate), ret=+13.9%
  - 2021: S=-0.41 (negative), ret=-5.7%
  - 2022: S=1.00 (moderate), ret=+10.9%
  - 2023: S=0.45 (weak), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 24.32% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 10.3% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.32, excess kurtosis +2.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.47, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +9.75%; worst month: -7.07%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.09
- Sideways: S=-0.70
- Bear: S=2.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_epsa_flag, 5))` S=0.53, F=0.46, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_epsa_flag)`: S=0.09, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsa_flag / close)`: S=-0.55, F=-0.37, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsa_flag, 5))`: S=0.53, F=0.46, T=14.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsa_flag / close)` | TOP200 | 0.56 | 0.37 | 24.3% | 80% | mixed |
| `rank(ts_delta(anl4_epsa_flag, 5))` | TOP3000 | 0.50 | 0.30 | 71.5% | 80% | mixed |
| `rank(anl4_epsa_flag)` | TOP1000 | 0.50 | 0.28 | 16.6% | 60% | bull-only |
| `rank(anl4_epsa_flag)` | TOP500 | 0.31 | 0.16 | 31.6% | 60% | bull-only |
| `rank(anl4_epsa_flag / close)` | TOP500 | 0.19 | 0.07 | 32.9% | 80% | bear-only |
| `rank(anl4_epsa_flag)` | TOP3000 | 0.15 | 0.04 | 18.7% | 40% | bull-only |
| `rank(anl4_epsa_flag / close)` | TOP1000 | 0.11 | 0.03 | 36.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_cshtrq: 0.920 (strongly positively correlated)
- anl4_afv4_eps_number: 0.811 (strongly positively correlated)
- volume: 0.785 (strongly positively correlated)
- news_mov_vol: 0.761 (strongly positively correlated)
- anl4_capex_number: 0.759 (strongly positively correlated)

Redundancy cluster #72: 3 similar fields, mean |rho| 0.779 (representative: anl4_afv4_eps_number). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
