---
field: fnd6_newa1v1300_invch
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.71
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.061
ann_vol: 0.0431
hit_rate: 0.5142
rolling_sharpe_min: -1.427
rolling_sharpe_max: 2.437
redundancy_cluster: 63
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.58
---
# fnd6_newa1v1300_invch (fundamental6)

*Mortgages - Decrease (Increase)*

## Signal Profile
- `rank(fnd6_newa1v1300_invch)`: S=0.46, F=0.19, T=2.1%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_invch / close)`: S=0.70, F=0.34, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_invch, 5))`: S=0.25, F=0.11, T=28.1%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_invch)`: S=-0.46, F=-0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_invch, 5))`: S=0.13, F=0.04, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_invch, 63)`: S=0.18, F=0.07, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_invch, 10)`: S=0.71, F=0.48, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_invch, 22))`: S=-0.09, F=-0.02, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invch)`: S=0.08, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invch / close)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.61 (negative), ret=-2.2%
  - 2020: S=0.16 (weak), ret=+0.5%
  - 2021: S=1.06 (moderate), ret=+5.7%
  - 2022: S=0.80 (moderate), ret=+3.3%
  - 2023: S=1.65 (strong), ret=+7.5%

## Risk & Drawdown
- Max drawdown: 6.10% over 735 days (recovered)
- Annualized: return +3.0%, volatility 4.3% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.26, excess kurtosis +1.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.43, max 2.44, latest 1.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +4.49%; worst month: -2.01%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.85
- Sideways: S=0.04
- Bear: S=3.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_invch, 5))` S=0.13, F=0.04, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_invch)`: S=0.08, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invch / close)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_invch, 5))`: S=0.13, F=0.04, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_invch / close)` | TOP1000 | 0.70 | 0.34 | 6.1% | 80% | bear-only |
| `rank(fnd6_newa1v1300_invch)` | TOP1000 | 0.46 | 0.19 | 8.7% | 80% | bear-only |
| `rank(fnd6_newa1v1300_invch / close)` | TOP3000 | 0.53 | 0.19 | 4.9% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_invch, 5))` | TOP200 | 0.25 | 0.11 | 52.6% | 60% | mixed |
| `rank(fnd6_newa1v1300_invch / close)` | TOP200 | 0.17 | 0.05 | 14.0% | 80% | bear-only |
| `rank(fnd6_newa1v1300_invch)` | TOP3000 | 0.20 | 0.04 | 6.3% | 80% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_invch: 0.995 (strongly positively correlated)
- fnd6_fopox: -0.321 (weakly negatively correlated)
- fn_allocated_share_based_compensation_expense_q: -0.306 (weakly negatively correlated)
- cash: -0.306 (weakly negatively correlated)
- fnd6_newqv1300_wcapq: -0.302 (weakly negatively correlated)

Redundancy cluster #63: 2 similar fields, mean |rho| 0.995 (representative: fnd6_mfma1_invch). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
