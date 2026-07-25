---
field: fnd6_ein
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.94
best_fitness: 1.45
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bear-only
n_variations_with_pnl: 11
max_drawdown: 0.5793
ann_vol: 0.273
hit_rate: 0.4648
rolling_sharpe_min: -0.553
rolling_sharpe_max: 2.061
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 4
direction_gap: -0.48
---
# fnd6_ein (fundamental6)

*Employer Identification Number code for the company*

## Signal Profile
- `rank(fnd6_ein)`: S=0.56, F=0.34, T=1.7%, INFERIOR (TOP500)
- `rank(fnd6_ein / close)`: S=0.65, F=0.42, T=2.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_ein, 5))`: S=0.52, F=0.56, T=8.4%, INFERIOR (TOP200)
- `-rank(fnd6_ein)`: S=-0.30, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ein, 5))`: S=0.46, F=0.33, T=16.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ein, 22)`: S=0.94, F=1.45, T=3.7%, AVERAGE (TOP3000)
- `ts_mean(fnd6_ein, 10)`: S=0.16, F=0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ein, 22))`: S=0.15, F=0.10, T=10.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ein)`: S=-0.45, F=-0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ein / close)`: S=-0.59, F=-0.39, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 25F/1P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.53, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.51 (strong), ret=+29.7%
  - 2020: S=0.42 (weak), ret=+17.4%
  - 2021: S=0.49 (weak), ret=+17.5%
  - 2022: S=0.37 (weak), ret=+4.0%
  - 2023: S=0.25 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 57.93% over 181 days (recovered)
- Annualized: return +14.3%, volatility 27.3% (fraction of booksize)
- Hit rate: 46.5% positive days
- Tail shape: skew +1.75, excess kurtosis +31.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.55, max 2.06, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +22.28%; worst month: -26.02%
Positive months: 62%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.71
- Sideways: S=0.67
- Bear: S=1.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ein, 5))` S=0.46, F=0.33, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ein)`: S=-0.45, F=-0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ein / close)`: S=-0.59, F=-0.39, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ein, 5))`: S=0.46, F=0.33, T=16.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ein, 5))` | TOP500 | 0.53 | 0.56 | 57.9% | 100% | bear-only |
| `rank(ts_delta(fnd6_ein, 5))` | TOP200 | 0.51 | 0.56 | 51.2% | 80% | mixed |
| `rank(fnd6_ein / close)` | TOP500 | 0.65 | 0.42 | 13.7% | 60% | bear-only |
| `rank(fnd6_ein / close)` | TOP3000 | 0.59 | 0.39 | 18.4% | 80% | bear-only |
| `rank(fnd6_ein)` | TOP500 | 0.57 | 0.34 | 19.4% | 60% | bear-only |
| `rank(fnd6_ein / close)` | TOP200 | 0.48 | 0.31 | 20.6% | 80% | bear-only |
| `rank(fnd6_ein)` | TOP200 | 0.46 | 0.28 | 28.1% | 60% | bear-only |
| `rank(fnd6_ein / close)` | TOP1000 | 0.46 | 0.25 | 21.3% | 80% | bear-only |
| `rank(fnd6_ein)` | TOP3000 | 0.45 | 0.22 | 14.3% | 80% | bear-only |
| `rank(ts_delta(fnd6_ein, 5))` | TOP1000 | 0.25 | 0.17 | 42.3% | 80% | bear-only |
| `rank(fnd6_ein)` | TOP1000 | 0.31 | 0.12 | 22.0% | 80% | bear-only |

## Correlation Notes
Top correlates:
- pv13_revere_term_sector_total: 0.224 (weakly positively correlated)
- fnd6_esopnr: 0.221 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.218 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.218 (weakly positively correlated)
- min_total_assets_guidance: 0.218 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
