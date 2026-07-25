---
field: anl4_flag_erbfintax
dataset: analyst4
best_template: ts_mean
best_sharpe: 1.05
best_fitness: 1.21
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0853
ann_vol: 0.0595
hit_rate: 0.5077
rolling_sharpe_min: -1.021
rolling_sharpe_max: 3.048
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.71
---
# anl4_flag_erbfintax (analyst4)

*Earnings before interest and taxes - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_flag_erbfintax)`: S=0.79, F=0.48, T=2.3%, INFERIOR (TOP500)
- `rank(anl4_flag_erbfintax / close)`: S=0.30, F=0.16, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_flag_erbfintax, 5))`: S=-0.01, F=0.00, T=25.8%, INFERIOR (TOP200)
- `-rank(anl4_flag_erbfintax)`: S=-0.04, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_flag_erbfintax, 5))`: S=0.34, F=0.19, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_flag_erbfintax, 22)`: S=0.26, F=0.20, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_flag_erbfintax, 10)`: S=1.05, F=1.21, T=4.8%, AVERAGE (TOP3000)
- `rank(ts_rank(anl4_flag_erbfintax, 22))`: S=0.10, F=0.03, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_flag_erbfintax)`: S=-0.04, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_flag_erbfintax / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.82 (moderate), ret=+3.5%
  - 2020: S=2.65 (strong), ret=+14.9%
  - 2021: S=-0.64 (negative), ret=-4.8%
  - 2022: S=1.27 (moderate), ret=+8.4%
  - 2023: S=0.20 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 8.53% over 400 days (recovered)
- Annualized: return +4.7%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.24, excess kurtosis +1.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 3.05, latest 0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.61%; worst month: -2.89%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.43
- Sideways: S=0.33
- Bear: S=1.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_flag_erbfintax, 5))` S=0.34, F=0.19, INFERIOR
Direction gap: -0.71 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_flag_erbfintax)`: S=-0.04, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_flag_erbfintax / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_flag_erbfintax, 5))`: S=0.34, F=0.19, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_flag_erbfintax)` | TOP500 | 0.79 | 0.48 | 8.5% | 80% | mixed |
| `rank(anl4_flag_erbfintax)` | TOP200 | 0.35 | 0.17 | 21.6% | 60% | weak |
| `rank(anl4_flag_erbfintax)` | TOP3000 | 0.42 | 0.17 | 12.9% | 60% | bear-only |
| `rank(anl4_flag_erbfintax / close)` | TOP200 | 0.31 | 0.16 | 21.2% | 100% | mixed |
| `rank(anl4_flag_erbfintax / close)` | TOP500 | 0.17 | 0.06 | 30.5% | 60% | bear-only |
| `rank(anl4_flag_erbfintax / close)` | TOP1000 | 0.11 | 0.03 | 35.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- operating_profit_max_guidance_qtr: -0.455 (moderately negatively correlated)
- min_ebit_guidance: -0.454 (moderately negatively correlated)
- max_ebit_guidance: -0.374 (weakly negatively correlated)
- min_ebit_guidance_2: -0.373 (weakly negatively correlated)
- cash_flow_from_financing: 0.341 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
