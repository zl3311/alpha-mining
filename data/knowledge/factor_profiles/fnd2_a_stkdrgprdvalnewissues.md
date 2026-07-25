---
field: fnd2_a_stkdrgprdvalnewissues
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.53
best_fitness: 0.42
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.3348
ann_vol: 0.243
hit_rate: 0.4891
rolling_sharpe_min: -1.628
rolling_sharpe_max: 2.367
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.39
n_negated_sims: 10
direction_gap: 0.04
---
# fnd2_a_stkdrgprdvalnewissues (fundamental2)

*Equity impact of the value of new stock issued during the period. Includes shares issued in an initial public offering or a secondary public offering.*

## Signal Profile
- `rank(fnd2_a_stkdrgprdvalnewissues)`: S=0.71, F=0.36, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_stkdrgprdvalnewissues / close)`: S=0.43, F=0.21, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))`: S=0.53, F=0.42, T=20.5%, INFERIOR (TOP500)
- `-rank(fnd2_a_stkdrgprdvalnewissues)`: S=-0.20, F=-0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))`: S=-0.23, F=-0.12, T=16.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_stkdrgprdvalnewissues, 63)`: S=-0.03, F=-0.01, T=8.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_stkdrgprdvalnewissues, 10)`: S=-0.01, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_stkdrgprdvalnewissues, 22))`: S=0.19, F=0.12, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_stkdrgprdvalnewissues)`: S=0.57, F=0.39, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_stkdrgprdvalnewissues / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.29 (negative), ret=-24.3%
  - 2020: S=1.29 (moderate), ret=+26.4%
  - 2021: S=1.76 (strong), ret=+61.8%
  - 2022: S=-0.13 (negative), ret=-2.9%
  - 2023: S=0.12 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 33.48% over 428 days (recovered)
- Annualized: return +12.9%, volatility 24.3% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +1.22, excess kurtosis +23.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.63, max 2.37, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +26.64%; worst month: -16.61%
Positive months: 49%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.76
- Sideways: S=-1.06
- Bear: S=1.59

## Negated Direction
Best negated: `rank(-1 * fnd2_a_stkdrgprdvalnewissues)` S=0.57, F=0.39, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_stkdrgprdvalnewissues)`: S=0.57, F=0.39, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_stkdrgprdvalnewissues / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))`: S=-0.23, F=-0.12, T=16.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))` | TOP500 | 0.53 | 0.42 | 33.5% | 60% | all-weather |
| `rank(ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))` | TOP200 | 0.47 | 0.36 | 23.0% | 40% | mixed |
| `rank(fnd2_a_stkdrgprdvalnewissues)` | TOP3000 | 0.72 | 0.36 | 7.6% | 80% | mixed |
| `rank(fnd2_a_stkdrgprdvalnewissues / close)` | TOP3000 | 0.43 | 0.21 | 15.7% | 60% | bear-only |
| `rank(fnd2_a_stkdrgprdvalnewissues / close)` | TOP1000 | 0.29 | 0.11 | 12.4% | 60% | bear-only |
| `rank(fnd2_a_stkdrgprdvalnewissues)` | TOP1000 | 0.20 | 0.06 | 10.8% | 60% | bull-only |
| `rank(fnd2_a_stkdrgprdvalnewissues / close)` | TOP500 | 0.17 | 0.05 | 20.4% | 40% | mixed |
| `rank(ts_delta(fnd2_a_stkdrgprdvalnewissues, 5))` | TOP3000 | 0.11 | 0.04 | 53.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd2_eixrtreclstatelocalitxes: 0.206 (weakly positively correlated)
- fn_effect_of_exchange_rate_on_cash_and_equiv_a: 0.188 (weakly positively correlated)
- parkinson_volatility_150: -0.183 (weakly negatively correlated)
- parkinson_volatility_180: -0.183 (weakly negatively correlated)
- historical_volatility_180: -0.181 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
