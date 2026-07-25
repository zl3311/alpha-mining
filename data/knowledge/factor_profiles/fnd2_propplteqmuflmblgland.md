---
field: fnd2_propplteqmuflmblgland
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.8
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1381
ann_vol: 0.0869
hit_rate: 0.4721
rolling_sharpe_min: -1.495
rolling_sharpe_max: 2.968
redundancy_cluster: 60
negated_best_sharpe: 0.8
negated_best_template: rank_neg_delta
negated_best_fitness: 0.74
n_negated_sims: 10
direction_gap: 0.25
---
# fnd2_propplteqmuflmblgland (fundamental2)

*PPE, Buildings & land, Useful Life, Minimum*

## Signal Profile
- `rank(fnd2_propplteqmuflmblgland)`: S=0.62, F=0.29, T=1.3%, INFERIOR (TOP500)
- `rank(fnd2_propplteqmuflmblgland / close)`: S=0.55, F=0.34, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_propplteqmuflmblgland, 5))`: S=0.15, F=0.07, T=11.7%, INFERIOR (TOP3000)
- `-rank(fnd2_propplteqmuflmblgland)`: S=-0.33, F=-0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmblgland, 5))`: S=0.80, F=0.74, T=6.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_propplteqmuflmblgland, 63)`: S=-0.12, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `ts_mean(fnd2_propplteqmuflmblgland, 10)`: S=0.41, F=0.14, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_propplteqmuflmblgland, 22))`: S=-0.69, F=-0.63, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmblgland)`: S=0.00, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmblgland / close)`: S=0.61, F=0.42, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-1.1%
  - 2020: S=1.62 (strong), ret=+18.7%
  - 2021: S=0.55 (moderate), ret=+4.6%
  - 2022: S=-0.17 (negative), ret=-1.3%
  - 2023: S=0.33 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 13.81% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 8.7% (fraction of booksize)
- Hit rate: 47.2% positive days
- Tail shape: skew +0.63, excess kurtosis +1.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 2.97, latest 0.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +8.66%; worst month: -5.24%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.22
- Sideways: S=-0.73
- Bear: S=2.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_propplteqmuflmblgland, 5))` S=0.80, F=0.74, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_propplteqmuflmblgland)`: S=0.00, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqmuflmblgland / close)`: S=0.61, F=0.42, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqmuflmblgland, 5))`: S=0.80, F=0.74, T=6.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_propplteqmuflmblgland / close)` | TOP3000 | 0.55 | 0.34 | 13.8% | 60% | mixed |
| `rank(fnd2_propplteqmuflmblgland)` | TOP500 | 0.61 | 0.29 | 8.1% | 80% | all-weather |
| `rank(fnd2_propplteqmuflmblgland)` | TOP3000 | 0.57 | 0.18 | 5.0% | 80% | mixed |
| `rank(fnd2_propplteqmuflmblgland)` | TOP1000 | 0.34 | 0.10 | 9.6% | 40% | mixed |
| `rank(fnd2_propplteqmuflmblgland / close)` | TOP1000 | 0.25 | 0.09 | 13.7% | 40% | mixed |
| `rank(ts_delta(fnd2_propplteqmuflmblgland, 5))` | TOP3000 | 0.14 | 0.07 | 41.6% | 60% | bull-only |
| `rank(ts_delta(fnd2_propplteqmuflmblgland, 5))` | TOP500 | 0.05 | 0.02 | 30.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_div_number: 0.931 (strongly positively correlated)
- anl4_qfd1_az_div_number: 0.931 (strongly positively correlated)
- anl4_afv4_div_number: 0.911 (strongly positively correlated)
- option_breakeven_1080: -0.891 (strongly negatively correlated)
- option_breakeven_720: -0.891 (strongly negatively correlated)

Redundancy cluster #60: 3 similar fields, mean |rho| 0.722 (representative: fnd2_dfdtxasoprlcarryfwd). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
