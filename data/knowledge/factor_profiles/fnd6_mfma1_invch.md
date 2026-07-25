---
field: fnd6_mfma1_invch
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 7
max_drawdown: 0.0586
ann_vol: 0.0434
hit_rate: 0.5142
rolling_sharpe_min: -1.47
rolling_sharpe_max: 2.576
redundancy_cluster: 63
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.63
---
# fnd6_mfma1_invch (fundamental6)

*Mortgages - Decrease (Increase)*

## Signal Profile
- `rank(fnd6_mfma1_invch)`: S=0.53, F=0.23, T=2.1%, INFERIOR (TOP1000)
- `rank(fnd6_mfma1_invch / close)`: S=0.77, F=0.40, T=2.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_mfma1_invch, 5))`: S=0.22, F=0.09, T=28.2%, INFERIOR (TOP200)
- `-rank(fnd6_mfma1_invch)`: S=-0.53, F=-0.23, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_invch, 5))`: S=0.09, F=0.02, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma1_invch, 63)`: S=0.20, F=0.08, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_invch, 10)`: S=0.72, F=0.49, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_invch, 22))`: S=-0.05, F=-0.01, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_invch)`: S=-0.21, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_invch / close)`: S=-0.53, F=-0.20, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.62 (negative), ret=-2.2%
  - 2020: S=0.27 (weak), ret=+0.9%
  - 2021: S=1.06 (moderate), ret=+5.7%
  - 2022: S=0.96 (moderate), ret=+4.0%
  - 2023: S=1.73 (strong), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 5.86% over 739 days (recovered)
- Annualized: return +3.3%, volatility 4.3% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.25, excess kurtosis +1.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.47, max 2.58, latest 1.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +4.37%; worst month: -2.02%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.81
- Sideways: S=0.11
- Bear: S=3.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_invch, 5))` S=0.09, F=0.02, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma1_invch)`: S=-0.21, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_invch / close)`: S=-0.53, F=-0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_invch, 5))`: S=0.09, F=0.02, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_invch / close)` | TOP1000 | 0.77 | 0.40 | 5.9% | 80% | bear-only |
| `rank(fnd6_mfma1_invch)` | TOP1000 | 0.53 | 0.23 | 8.3% | 80% | bear-only |
| `rank(fnd6_mfma1_invch / close)` | TOP3000 | 0.55 | 0.20 | 4.8% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma1_invch, 5))` | TOP200 | 0.21 | 0.09 | 53.3% | 60% | mixed |
| `rank(fnd6_mfma1_invch / close)` | TOP200 | 0.20 | 0.07 | 13.7% | 80% | bear-only |
| `rank(fnd6_mfma1_invch)` | TOP3000 | 0.23 | 0.05 | 6.0% | 80% | bear-only |
| `rank(fnd6_mfma1_invch / close)` | TOP500 | 0.08 | 0.02 | 6.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_invch: 0.995 (strongly positively correlated)
- fnd6_fopox: -0.329 (weakly negatively correlated)
- fn_allocated_share_based_compensation_expense_q: -0.312 (weakly negatively correlated)
- cash: -0.305 (weakly negatively correlated)
- fnd6_newqv1300_wcapq: -0.303 (weakly negatively correlated)

Redundancy cluster #63: 2 similar fields, mean |rho| 0.995 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
