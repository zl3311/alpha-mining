---
field: anl4_ebit_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.57
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0704
ann_vol: 0.026
hit_rate: 0.5028
rolling_sharpe_min: -1.524
rolling_sharpe_max: 3.186
redundancy_cluster: 5
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.1
---
# anl4_ebit_number (analyst4)

*Earnings before interest and taxes - number of estimations*

## Signal Profile
- `rank(anl4_ebit_number)`: S=0.62, F=0.22, T=3.0%, INFERIOR (TOP3000)
- `rank(anl4_ebit_number / close)`: S=0.30, F=0.14, T=3.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ebit_number, 5))`: S=0.15, F=0.03, T=34.3%, INFERIOR (TOP200)
- `-rank(anl4_ebit_number)`: S=-0.49, F=-0.18, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_number, 5))`: S=0.47, F=0.13, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ebit_number, 63)`: S=0.51, F=0.18, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_number, 10)`: S=0.57, F=0.25, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_number, 22))`: S=-0.35, F=-0.11, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_number)`: S=-0.49, F=-0.18, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_number / close)`: S=-0.21, F=-0.09, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.44 (negative), ret=-0.9%
  - 2020: S=-0.09 (negative), ret=-0.2%
  - 2021: S=1.63 (strong), ret=+4.5%
  - 2022: S=1.85 (strong), ret=+5.3%
  - 2023: S=-0.25 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 7.04% over 931 days (recovered)
- Annualized: return +1.7%, volatility 2.6% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.25, excess kurtosis +0.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 3.19, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +2.08%; worst month: -1.73%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.26
- Sideways: S=0.15
- Bear: S=0.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_number, 5))` S=0.47, F=0.13, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_number)`: S=-0.49, F=-0.18, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_number / close)`: S=-0.21, F=-0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_number, 5))`: S=0.47, F=0.13, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_number)` | TOP3000 | 0.63 | 0.22 | 7.0% | 40% | mixed |
| `rank(anl4_ebit_number)` | TOP1000 | 0.51 | 0.18 | 8.0% | 60% | all-weather |
| `rank(anl4_ebit_number)` | TOP500 | 0.46 | 0.17 | 6.6% | 60% | all-weather |
| `rank(anl4_ebit_number / close)` | TOP200 | 0.32 | 0.14 | 16.2% | 100% | mixed |
| `rank(anl4_ebit_number / close)` | TOP500 | 0.30 | 0.13 | 21.7% | 80% | bear-only |
| `rank(anl4_ebit_number / close)` | TOP1000 | 0.22 | 0.09 | 25.5% | 40% | bear-only |
| `rank(ts_delta(anl4_ebit_number, 5))` | TOP200 | 0.16 | 0.03 | 23.7% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_netprofit_number: 0.915 (strongly positively correlated)
- sales_estimate_count_quarterly: 0.758 (strongly positively correlated)
- anl4_qf_az_eps_number: 0.663 (moderately positively correlated)
- anl4_qfd1_az_eps_number: 0.663 (moderately positively correlated)
- anl4_epsr_number: 0.597 (moderately positively correlated)

Redundancy cluster #5: 5 similar fields, mean |rho| 0.774 (representative: sales_estimate_count_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
