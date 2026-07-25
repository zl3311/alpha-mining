---
field: fnd6_cibegni
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.91
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.4367
ann_vol: 0.2195
hit_rate: 0.4583
rolling_sharpe_min: -1.345
rolling_sharpe_max: 2.234
negated_best_sharpe: 0.91
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: 0.76
---
# fnd6_cibegni (fundamental6)

*Comp Inc - Beginning Net Income*

## Signal Profile
- `rank(fnd6_cibegni)`: S=0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_cibegni / close)`: S=0.12, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cibegni, 5))`: S=0.15, F=0.05, T=29.1%, INFERIOR (TOP200)
- `-rank(fnd6_cibegni)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cibegni, 5))`: S=0.91, F=0.58, T=40.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cibegni, 63)`: S=-0.49, F=-0.31, T=20.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cibegni, 10)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cibegni, 22))`: S=-0.74, F=-0.48, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cibegni)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cibegni / close)`: S=-0.03, F=-0.01, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.14, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.38 (strong), ret=+31.1%
  - 2020: S=-0.23 (negative), ret=-3.7%
  - 2021: S=0.39 (weak), ret=+10.5%
  - 2022: S=-0.68 (negative), ret=-21.3%
  - 2023: S=-0.07 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 43.67% over 757 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 21.9% (fraction of booksize)
- Hit rate: 45.8% positive days
- Tail shape: skew -0.99, excess kurtosis +20.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 2.23, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +22.81%; worst month: -21.49%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.99
- Sideways: S=1.19
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cibegni, 5))` S=0.91, F=0.58, INFERIOR
Direction gap: +0.76 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_cibegni)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cibegni / close)`: S=-0.03, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cibegni, 5))`: S=0.91, F=0.58, T=40.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cibegni, 5))` | TOP200 | 0.14 | 0.05 | 43.7% | 40% | bear-only |
| `rank(fnd6_cibegni / close)` | TOP3000 | 0.10 | 0.04 | 35.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_citotal: 0.878 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.647 (moderately positively correlated)
- fnd6_ibmii: 0.584 (moderately positively correlated)
- fnd6_pidom: 0.557 (moderately positively correlated)
- fnd6_newa2v1300_pi: 0.555 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
