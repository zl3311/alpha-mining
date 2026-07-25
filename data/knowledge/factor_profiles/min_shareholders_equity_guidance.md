---
field: min_shareholders_equity_guidance
dataset: analyst4
best_template: rank_ts_rank
best_sharpe: 1.25
best_fitness: 1.82
best_universe: TOP3000
grade: GOOD
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.6637
ann_vol: 0.2706
hit_rate: 0.5166
rolling_sharpe_min: -1.398
rolling_sharpe_max: 3.414
redundancy_cluster: 76
negated_best_sharpe: 0.62
negated_best_template: neg_rank_level
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: -0.63
---
# min_shareholders_equity_guidance (analyst4)

*Minimum guidance value for Shareholders' Equity*

## Signal Profile
- `rank(min_shareholders_equity_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP500)
- `rank(min_shareholders_equity_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_shareholders_equity_guidance, 5))`: S=0.66, F=0.60, T=21.4%, INFERIOR (TOP3000)
- `-rank(min_shareholders_equity_guidance)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_shareholders_equity_guidance, 5))`: S=-0.53, F=-0.43, T=21.5%, INFERIOR (TOP3000)
- `-ts_zscore(min_shareholders_equity_guidance, 63)`: S=-0.60, F=-0.52, T=2.1%, INFERIOR (TOP3000)
- `ts_mean(min_shareholders_equity_guidance, 10)`: S=-0.31, F=-0.23, T=14.3%, INFERIOR (TOP3000)
- `rank(ts_rank(min_shareholders_equity_guidance, 22))`: S=1.25, F=1.82, T=11.5%, GOOD (TOP3000)
- `rank(-1 * min_shareholders_equity_guidance)`: S=0.62, F=0.57, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * min_shareholders_equity_guidance / close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/9P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 17F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+21.4%
  - 2020: S=-0.17 (negative), ret=-5.9%
  - 2021: S=0.25 (weak), ret=+7.3%
  - 2022: S=2.45 (strong), ret=+43.3%
  - 2023: S=1.49 (moderate), ret=+22.8%

## Risk & Drawdown
- Max drawdown: 66.37% over 551 days (recovered)
- Annualized: return +18.2%, volatility 27.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.23, excess kurtosis +23.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 3.41, latest 1.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +18.46%; worst month: -18.27%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.22
- Sideways: S=0.88
- Bear: S=0.05

## Negated Direction
Best negated: `rank(-1 * min_shareholders_equity_guidance)` S=0.62, F=0.57, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_shareholders_equity_guidance)`: S=0.62, F=0.57, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * min_shareholders_equity_guidance / close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_shareholders_equity_guidance, 5))`: S=-0.53, F=-0.43, T=21.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(min_shareholders_equity_guidance, 5))` | TOP3000 | 0.67 | 0.60 | 66.4% | 80% | mixed |
| `rank(min_shareholders_equity_guidance)` | TOP500 | 0.47 | 0.33 | 32.4% | 60% | bull-only |
| `rank(min_shareholders_equity_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(min_shareholders_equity_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_shareholders_equity_guidance: 1.000 (strongly positively correlated)
- min_shares_outstanding_guidance: 0.992 (strongly positively correlated)
- min_share_count_guidance: 0.992 (strongly positively correlated)
- shares_outstanding_max_guidance: 0.992 (strongly positively correlated)
- min_basic_shares_guidance: 0.992 (strongly positively correlated)

Redundancy cluster #76: 8 similar fields, mean |rho| 0.997 (representative: max_shareholders_equity_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
