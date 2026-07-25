---
field: fnd2_currfedtxexp
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.86
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2736
ann_vol: 0.1359
hit_rate: 0.4988
rolling_sharpe_min: -1.684
rolling_sharpe_max: 2.752
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.42
---
# fnd2_currfedtxexp (fundamental2)

*Income Tax Expense, Current - Federal*

## Signal Profile
- `rank(fnd2_currfedtxexp)`: S=0.13, F=0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_currfedtxexp / close)`: S=0.26, F=0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_currfedtxexp, 5))`: S=0.50, F=0.22, T=35.4%, INFERIOR (TOP1000)
- `-rank(fnd2_currfedtxexp)`: S=-0.09, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currfedtxexp, 5))`: S=0.12, F=0.03, T=28.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_currfedtxexp, 63)`: S=0.86, F=0.70, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fnd2_currfedtxexp, 10)`: S=0.14, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_currfedtxexp, 22))`: S=0.38, F=0.18, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfedtxexp)`: S=0.44, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfedtxexp / close)`: S=0.44, F=0.29, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.44 (negative), ret=-5.3%
  - 2020: S=0.81 (moderate), ret=+12.5%
  - 2021: S=1.71 (strong), ret=+22.4%
  - 2022: S=0.95 (moderate), ret=+13.3%
  - 2023: S=-0.79 (negative), ret=-8.8%

## Risk & Drawdown
- Max drawdown: 27.36% over 688 days (recovered)
- Annualized: return +7.0%, volatility 13.6% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.23, excess kurtosis +5.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.75, latest -0.83

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +12.00%; worst month: -9.30%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.23
- Sideways: S=0.01
- Bear: S=0.16

## Negated Direction
Best negated: `rank(-1 * fnd2_currfedtxexp)` S=0.44, F=0.30, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_currfedtxexp)`: S=0.44, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfedtxexp / close)`: S=0.44, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currfedtxexp, 5))`: S=0.12, F=0.03, T=28.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_currfedtxexp, 5))` | TOP1000 | 0.51 | 0.22 | 27.4% | 60% | mixed |
| `rank(ts_delta(fnd2_currfedtxexp, 5))` | TOP3000 | 0.42 | 0.17 | 14.0% | 80% | mixed |
| `rank(fnd2_currfedtxexp / close)` | TOP3000 | 0.24 | 0.10 | 18.3% | 60% | bull-only |
| `rank(fnd2_currfedtxexp / close)` | TOP1000 | 0.16 | 0.06 | 21.7% | 60% | bull-only |
| `rank(fnd2_currfedtxexp)` | TOP3000 | 0.12 | 0.04 | 28.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_dfdfeditxexp: 0.175 (weakly positively correlated)
- fnd2_a_ltrmdmrepopliny5: 0.134 (weakly positively correlated)
- fnd2_dfdtxlbsgwllandintas: 0.134 (weakly positively correlated)
- fn_derivative_notional_amount_q: 0.133 (weakly positively correlated)
- anl4_afv4_eps_low: 0.132 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
