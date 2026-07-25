---
field: fnd6_newqv1300_cshiq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.82
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1378
ann_vol: 0.0686
hit_rate: 0.5101
rolling_sharpe_min: -0.656
rolling_sharpe_max: 1.96
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.33
---
# fnd6_newqv1300_cshiq (fundamental6)

*Common Shares Issued*

## Signal Profile
- `rank(fnd6_newqv1300_cshiq)`: S=0.32, F=0.13, T=5.4%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_cshiq / close)`: S=0.48, F=0.25, T=6.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_cshiq, 5))`: S=-0.15, F=-0.04, T=49.2%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cshiq)`: S=-0.32, F=-0.13, T=5.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshiq, 5))`: S=0.82, F=0.33, T=39.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cshiq, 63)`: S=0.49, F=0.29, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cshiq, 10)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cshiq, 22))`: S=-0.65, F=-0.30, T=19.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshiq)`: S=-0.14, F=-0.03, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshiq / close)`: S=0.04, F=0.01, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+5.0%
  - 2020: S=0.38 (weak), ret=+3.1%
  - 2021: S=-0.42 (negative), ret=-3.6%
  - 2022: S=1.65 (strong), ret=+10.4%
  - 2023: S=0.28 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 13.78% over 517 days (recovered)
- Annualized: return +3.3%, volatility 6.9% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.28, excess kurtosis +1.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 1.96, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.59%; worst month: -3.26%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.68
- Sideways: S=-0.63
- Bear: S=0.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cshiq, 5))` S=0.82, F=0.33, INFERIOR
Direction gap: +0.33 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cshiq)`: S=-0.14, F=-0.03, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cshiq / close)`: S=0.04, F=0.01, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cshiq, 5))`: S=0.82, F=0.33, T=39.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cshiq / close)` | TOP500 | 0.48 | 0.25 | 13.8% | 80% | mixed |
| `rank(fnd6_newqv1300_cshiq / close)` | TOP1000 | 0.41 | 0.20 | 14.8% | 80% | all-weather |
| `rank(fnd6_newqv1300_cshiq / close)` | TOP200 | 0.32 | 0.15 | 19.6% | 80% | mixed |
| `rank(fnd6_newqv1300_cshiq)` | TOP1000 | 0.32 | 0.13 | 13.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshiq)` | TOP500 | 0.14 | 0.04 | 25.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_cshiq)` | TOP3000 | 0.14 | 0.03 | 9.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cshoq: 0.954 (strongly positively correlated)
- fnd6_newqv1300_cshprq: 0.952 (strongly positively correlated)
- fnd6_mfmq_cshprq: 0.952 (strongly positively correlated)
- fnd6_newqv1300_cshfdq: 0.952 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.947 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
