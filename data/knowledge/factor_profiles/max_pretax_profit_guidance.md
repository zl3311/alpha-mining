---
field: max_pretax_profit_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.59
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2124
ann_vol: 0.0808
hit_rate: 0.5134
rolling_sharpe_min: -2.612
rolling_sharpe_max: 2.747
redundancy_cluster: 91
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.32
---
# max_pretax_profit_guidance (analyst4)

*The maximum guidance value for Pretax income on an annual basis.*

## Signal Profile
- `rank(max_pretax_profit_guidance)`: S=0.59, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(max_pretax_profit_guidance / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_pretax_profit_guidance, 5))`: S=0.52, F=0.19, T=33.7%, INFERIOR (TOP200)
- `-rank(max_pretax_profit_guidance)`: S=-0.11, F=-0.04, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_pretax_profit_guidance, 5))`: S=0.27, F=0.06, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_pretax_profit_guidance, 63)`: S=0.25, F=0.06, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(max_pretax_profit_guidance, 10)`: S=0.14, F=0.06, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_pretax_profit_guidance, 22))`: S=-0.14, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_pretax_profit_guidance)`: S=0.07, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * max_pretax_profit_guidance / close)`: S=0.04, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+0.9%
  - 2020: S=-1.98 (negative), ret=-13.8%
  - 2021: S=1.25 (moderate), ret=+11.2%
  - 2022: S=1.57 (strong), ret=+16.1%
  - 2023: S=1.22 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 21.24% over 830 days (recovered)
- Annualized: return +4.8%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.15, excess kurtosis +2.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.61, max 2.75, latest 1.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.18%; worst month: -3.88%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.83
- Sideways: S=0.63
- Bear: S=-0.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_pretax_profit_guidance, 5))` S=0.27, F=0.06, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_pretax_profit_guidance)`: S=0.07, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * max_pretax_profit_guidance / close)`: S=0.04, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_pretax_profit_guidance, 5))`: S=0.27, F=0.06, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_pretax_profit_guidance)` | TOP3000 | 0.59 | 0.36 | 21.2% | 80% | bull-only |
| `rank(ts_delta(max_pretax_profit_guidance, 5))` | TOP200 | 0.54 | 0.19 | 15.4% | 60% | bear-only |
| `rank(max_pretax_profit_guidance)` | TOP1000 | 0.10 | 0.04 | 41.6% | 40% | mixed |
| `rank(max_pretax_profit_guidance / close)` | TOP3000 | 0.09 | 0.03 | 52.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_pretax_profit_guidance_2: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.590 (moderately positively correlated)
- fnd6_tstkc: 0.587 (moderately positively correlated)
- fnd6_newa1v1300_ebitda: 0.579 (moderately positively correlated)
- fnd6_newa2v1300_oibdp: 0.579 (moderately positively correlated)

Redundancy cluster #91: 2 similar fields, mean |rho| 1.0 (representative: min_pretax_profit_guidance_2). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
