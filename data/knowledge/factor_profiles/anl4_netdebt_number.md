---
field: anl4_netdebt_number
dataset: analyst4
best_template: rank_ts_rank
best_sharpe: 0.73
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.2325
ann_vol: 0.1247
hit_rate: 0.5117
rolling_sharpe_min: -1.265
rolling_sharpe_max: 1.798
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.35
---
# anl4_netdebt_number (analyst4)

*Net debt - Number of estimations*

## Signal Profile
- `rank(anl4_netdebt_number)`: S=0.24, F=0.09, T=4.0%, INFERIOR (TOP500)
- `rank(anl4_netdebt_number / close)`: S=0.24, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netdebt_number, 5))`: S=0.36, F=0.13, T=34.0%, INFERIOR (TOP1000)
- `-rank(anl4_netdebt_number)`: S=-0.19, F=-0.05, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_number, 5))`: S=0.38, F=0.19, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_number, 63)`: S=-0.07, F=-0.02, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_number, 10)`: S=0.18, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_number, 22))`: S=0.73, F=0.49, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_number)`: S=-0.17, F=-0.06, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_number / close)`: S=0.25, F=0.11, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-1.9%
  - 2020: S=0.77 (moderate), ret=+9.7%
  - 2021: S=1.61 (strong), ret=+18.2%
  - 2022: S=-0.62 (negative), ret=-7.9%
  - 2023: S=0.27 (weak), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 23.25% over 763 days (not yet recovered, ongoing at window end)
- Annualized: return +4.4%, volatility 12.5% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.81, excess kurtosis +9.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 1.80, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +7.47%; worst month: -8.38%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.57
- Sideways: S=0.78
- Bear: S=-0.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netdebt_number, 5))` S=0.38, F=0.19, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_number)`: S=-0.17, F=-0.06, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_number / close)`: S=0.25, F=0.11, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_number, 5))`: S=0.38, F=0.19, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_netdebt_number, 5))` | TOP1000 | 0.36 | 0.13 | 23.2% | 60% | mixed |
| `rank(anl4_netdebt_number / close)` | TOP3000 | 0.23 | 0.11 | 34.4% | 60% | bear-only |
| `rank(anl4_netdebt_number)` | TOP500 | 0.23 | 0.09 | 15.1% | 60% | weak |
| `rank(ts_delta(anl4_netdebt_number, 5))` | TOP3000 | 0.26 | 0.08 | 16.8% | 60% | bull-only |
| `rank(anl4_netdebt_number / close)` | TOP1000 | 0.18 | 0.07 | 21.3% | 40% | bear-only |
| `rank(anl4_netdebt_number)` | TOP200 | 0.16 | 0.06 | 35.2% | 40% | weak |
| `rank(anl4_netdebt_number)` | TOP1000 | 0.19 | 0.05 | 14.5% | 40% | bull-only |
| `rank(anl4_netdebt_number / close)` | TOP500 | 0.15 | 0.05 | 17.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_recch: -0.114 (weakly negatively correlated)
- cash_flow_from_investing: 0.105 (weakly positively correlated)
- earnings_per_share_guidance_value: -0.094 (weakly negatively correlated)
- anl4_epsr_high: -0.091 (weakly negatively correlated)
- anl4_afv4_eps_low: -0.087 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
