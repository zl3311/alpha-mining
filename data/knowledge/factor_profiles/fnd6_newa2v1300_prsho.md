---
field: fnd6_newa2v1300_prsho
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.42
best_fitness: 0.56
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 1.0837
ann_vol: 0.5278
hit_rate: 0.4745
rolling_sharpe_min: -1.095
rolling_sharpe_max: 2.576
negated_best_sharpe: 0.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.13
---
# fnd6_newa2v1300_prsho (fundamental6)

*Redeem Pfd Shares Outs (000)*

## Signal Profile
- `rank(fnd6_newa2v1300_prsho)`: S=0.42, F=0.56, T=7.8%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_prsho / close)`: S=0.42, F=0.56, T=7.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_prsho, 5))`: S=0.30, F=0.18, T=6.6%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_prsho)`: S=-0.28, F=-0.16, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_prsho, 5))`: S=0.29, F=0.17, T=16.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_prsho, 22)`: S=-0.10, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_prsho, 10)`: S=0.06, F=0.02, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_prsho, 22))`: S=-0.21, F=-0.15, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_prsho)`: S=0.30, F=0.13, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_prsho / close)`: S=0.29, F=0.13, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.43, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.35 (weak), ret=+36.9%
  - 2020: S=1.62 (strong), ret=+36.8%
  - 2021: S=0.47 (weak), ret=+13.0%
  - 2022: S=0.06 (weak), ret=+1.5%
  - 2023: S=0.92 (moderate), ret=+22.9%

## Risk & Drawdown
- Max drawdown: 108.37% over 46 days (recovered)
- Annualized: return +22.7%, volatility 52.8% (fraction of booksize)
- Hit rate: 47.4% positive days
- Tail shape: skew +6.18, excess kurtosis +248.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.58, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +25.21%; worst month: -15.78%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.02
- Sideways: S=0.36
- Bear: S=1.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_prsho, 5))` S=0.29, F=0.17, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_prsho)`: S=0.30, F=0.13, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_prsho / close)`: S=0.29, F=0.13, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_prsho, 5))`: S=0.29, F=0.17, T=16.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_prsho)` | TOP200 | 0.43 | 0.56 | 108.4% | 100% | mixed |
| `rank(fnd6_newa2v1300_prsho / close)` | TOP200 | 0.43 | 0.56 | 108.4% | 100% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_prsho, 5))` | TOP200 | 0.28 | 0.18 | 22.7% | 40% | mixed |
| `rank(fnd6_newa2v1300_prsho)` | TOP1000 | 0.28 | 0.16 | 27.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_prsho / close)` | TOP1000 | 0.28 | 0.16 | 27.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_prsho / close)` | TOP500 | 0.09 | 0.05 | 108.8% | 40% | bear-only |
| `rank(fnd6_newa2v1300_prsho)` | TOP500 | 0.09 | 0.05 | 108.8% | 40% | bear-only |
| `rank(ts_delta(fnd6_newa2v1300_prsho, 5))` | TOP500 | 0.08 | 0.03 | 29.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_pstkl: 0.504 (moderately positively correlated)
- fnd6_pstkrv: 0.496 (moderately positively correlated)
- fnd6_newqv1300_anoq: 0.289 (weakly positively correlated)
- news_pe_ratio: 0.240 (weakly positively correlated)
- rp_nip_ptg: 0.228 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
