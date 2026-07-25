---
field: min_pretax_profit_guidance_2
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.63
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.212
ann_vol: 0.0808
hit_rate: 0.515
rolling_sharpe_min: -2.605
rolling_sharpe_max: 2.752
redundancy_cluster: 91
negated_best_sharpe: 0.63
negated_best_template: neg_rank_level
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 0.03
---
# min_pretax_profit_guidance_2 (analyst4)

*The minimum guidance value for Pretax income on an annual basis.*

## Signal Profile
- `rank(min_pretax_profit_guidance_2)`: S=0.60, F=0.37, T=1.0%, INFERIOR (TOP3000)
- `rank(min_pretax_profit_guidance_2 / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_pretax_profit_guidance_2, 5))`: S=0.55, F=0.21, T=33.7%, INFERIOR (TOP200)
- `-rank(min_pretax_profit_guidance_2)`: S=-0.11, F=-0.04, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_pretax_profit_guidance_2, 5))`: S=-0.55, F=-0.21, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(min_pretax_profit_guidance_2, 63)`: S=0.19, F=0.04, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(min_pretax_profit_guidance_2, 10)`: S=0.17, F=0.08, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(min_pretax_profit_guidance_2, 22))`: S=-0.09, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_pretax_profit_guidance_2)`: S=0.63, F=0.62, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * min_pretax_profit_guidance_2 / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+0.9%
  - 2020: S=-1.97 (negative), ret=-13.7%
  - 2021: S=1.25 (moderate), ret=+11.3%
  - 2022: S=1.57 (strong), ret=+16.1%
  - 2023: S=1.22 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 21.20% over 830 days (recovered)
- Annualized: return +4.8%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.15, excess kurtosis +2.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.60, max 2.75, latest 1.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.20%; worst month: -3.88%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.84
- Sideways: S=0.64
- Bear: S=-0.91

## Negated Direction
Best negated: `rank(-1 * min_pretax_profit_guidance_2)` S=0.63, F=0.62, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * min_pretax_profit_guidance_2)`: S=0.63, F=0.62, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * min_pretax_profit_guidance_2 / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_pretax_profit_guidance_2, 5))`: S=-0.55, F=-0.21, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_pretax_profit_guidance_2)` | TOP3000 | 0.59 | 0.37 | 21.2% | 80% | bull-only |
| `rank(ts_delta(min_pretax_profit_guidance_2, 5))` | TOP200 | 0.57 | 0.21 | 15.4% | 60% | bear-only |
| `rank(min_pretax_profit_guidance_2)` | TOP1000 | 0.10 | 0.04 | 41.6% | 40% | mixed |
| `rank(min_pretax_profit_guidance_2 / close)` | TOP3000 | 0.09 | 0.03 | 52.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_pretax_profit_guidance: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.589 (moderately positively correlated)
- fnd6_tstkc: 0.586 (moderately positively correlated)
- fnd6_newa1v1300_ebitda: 0.579 (moderately positively correlated)
- fnd6_newa2v1300_oibdp: 0.579 (moderately positively correlated)

Redundancy cluster #91: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
