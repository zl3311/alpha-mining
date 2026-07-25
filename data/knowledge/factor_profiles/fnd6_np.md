---
field: fnd6_np
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.73
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1172
ann_vol: 0.053
hit_rate: 0.502
rolling_sharpe_min: -2.062
rolling_sharpe_max: 2.145
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: 0.53
---
# fnd6_np (fundamental6)

*Notes Payable - Short-Term Borrowings*

## Signal Profile
- `rank(fnd6_np)`: S=0.06, F=0.01, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_np / close)`: S=0.11, F=0.02, T=1.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_np, 5))`: S=-0.07, F=-0.02, T=26.4%, INFERIOR (TOP200)
- `-rank(fnd6_np)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_np, 5))`: S=0.73, F=0.48, T=31.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_np, 63)`: S=0.20, F=0.09, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_np, 10)`: S=0.15, F=0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_np, 22))`: S=0.21, F=0.08, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_np)`: S=0.17, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_np / close)`: S=0.11, F=0.03, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.10, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+3.5%
  - 2020: S=-1.31 (negative), ret=-5.4%
  - 2021: S=-0.28 (negative), ret=-1.9%
  - 2022: S=1.88 (strong), ret=+12.8%
  - 2023: S=-1.49 (negative), ret=-6.4%

## Risk & Drawdown
- Max drawdown: 11.72% over 891 days (recovered)
- Annualized: return +0.5%, volatility 5.3% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.07, excess kurtosis +1.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.06, max 2.15, latest -1.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.46%; worst month: -3.22%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.69
- Sideways: S=0.09
- Bear: S=-3.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_np, 5))` S=0.73, F=0.48, INFERIOR
Direction gap: +0.53 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_np)`: S=0.17, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_np / close)`: S=0.11, F=0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_np, 5))`: S=0.73, F=0.48, T=31.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_np / close)` | TOP1000 | 0.10 | 0.02 | 11.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_div_high: 0.714 (strongly positively correlated)
- fnd6_ivaeq: 0.712 (strongly positively correlated)
- anl4_afv4_div_median: 0.706 (strongly positively correlated)
- fnd6_newqv1300_mibtq: 0.705 (strongly positively correlated)
- fnd6_mfmq_mibtq: 0.705 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
