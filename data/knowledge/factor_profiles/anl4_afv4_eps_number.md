---
field: anl4_afv4_eps_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.71
best_fitness: 0.5
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1672
ann_vol: 0.0883
hit_rate: 0.5158
rolling_sharpe_min: -1.44
rolling_sharpe_max: 2.434
redundancy_cluster: 72
negated_best_sharpe: 0.07
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.64
---
# anl4_afv4_eps_number (analyst4)

*Earnings per share - number of estimations for annual frequency*

## Signal Profile
- `rank(anl4_afv4_eps_number)`: S=0.66, F=0.44, T=3.8%, INFERIOR (TOP200)
- `rank(anl4_afv4_eps_number / close)`: S=0.71, F=0.50, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_afv4_eps_number, 5))`: S=0.20, F=0.04, T=35.2%, INFERIOR (TOP500)
- `-rank(anl4_afv4_eps_number)`: S=-0.43, F=-0.15, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_number, 5))`: S=0.07, F=0.01, T=32.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_eps_number, 22)`: S=0.40, F=0.12, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_eps_number, 10)`: S=0.16, F=0.05, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_eps_number, 22))`: S=0.31, F=0.10, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_number)`: S=-0.66, F=-0.44, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_number / close)`: S=-0.71, F=-0.50, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/24P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.72, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.5%
  - 2020: S=0.89 (moderate), ret=+8.3%
  - 2021: S=0.03 (weak), ret=+0.4%
  - 2022: S=1.28 (moderate), ret=+11.7%
  - 2023: S=1.23 (moderate), ret=+9.5%

## Risk & Drawdown
- Max drawdown: 16.72% over 487 days (recovered)
- Annualized: return +6.4%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.15, excess kurtosis +1.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.43, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +9.13%; worst month: -5.56%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.54
- Sideways: S=0.05
- Bear: S=1.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_eps_number, 5))` S=0.07, F=0.01, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_eps_number)`: S=-0.66, F=-0.44, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_number / close)`: S=-0.71, F=-0.50, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_number, 5))`: S=0.07, F=0.01, T=32.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_eps_number / close)` | TOP200 | 0.72 | 0.50 | 16.7% | 100% | all-weather |
| `rank(anl4_afv4_eps_number)` | TOP200 | 0.68 | 0.44 | 11.2% | 80% | mixed |
| `rank(anl4_afv4_eps_number)` | TOP500 | 0.68 | 0.35 | 11.1% | 80% | bull-only |
| `rank(anl4_afv4_eps_number)` | TOP3000 | 0.72 | 0.27 | 8.2% | 80% | bull-only |
| `rank(anl4_afv4_eps_number / close)` | TOP500 | 0.40 | 0.20 | 24.4% | 60% | mixed |
| `rank(anl4_afv4_eps_number)` | TOP1000 | 0.44 | 0.15 | 13.2% | 60% | bull-only |
| `rank(anl4_afv4_eps_number / close)` | TOP1000 | 0.19 | 0.07 | 24.1% | 40% | bear-only |
| `rank(ts_delta(anl4_afv4_eps_number, 5))` | TOP500 | 0.17 | 0.04 | 18.4% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_epsa_flag: 0.811 (strongly positively correlated)
- fnd6_cshtrq: 0.806 (strongly positively correlated)
- anl4_capex_number: 0.766 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.661 (moderately positively correlated)
- anl4_fcf_number: 0.655 (moderately positively correlated)

Redundancy cluster #72: 3 similar fields, mean |rho| 0.779 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
