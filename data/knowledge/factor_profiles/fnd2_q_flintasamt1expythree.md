---
field: fnd2_q_flintasamt1expythree
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.73
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2116
ann_vol: 0.1219
hit_rate: 0.5174
rolling_sharpe_min: -1.843
rolling_sharpe_max: 2.0
redundancy_cluster: 44
negated_best_sharpe: 0.73
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.69
n_negated_sims: 10
direction_gap: 0.11
---
# fnd2_q_flintasamt1expythree (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 3rd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_q_flintasamt1expythree)`: S=0.34, F=0.16, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_q_flintasamt1expythree / close)`: S=0.39, F=0.18, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_q_flintasamt1expythree, 5))`: S=0.75, F=0.38, T=36.4%, INFERIOR (TOP3000)
- `-rank(fnd2_q_flintasamt1expythree)`: S=-0.03, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expythree, 5))`: S=0.17, F=0.05, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_q_flintasamt1expythree, 63)`: S=0.14, F=0.04, T=16.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_q_flintasamt1expythree, 10)`: S=0.16, F=0.07, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_q_flintasamt1expythree, 22))`: S=0.62, F=0.41, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expythree)`: S=0.60, F=0.56, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expythree / close)`: S=0.73, F=0.69, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.67 (negative), ret=-6.6%
  - 2020: S=1.16 (moderate), ret=+14.7%
  - 2021: S=0.56 (moderate), ret=+7.4%
  - 2022: S=1.52 (strong), ret=+20.1%
  - 2023: S=0.89 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 21.16% over 488 days (recovered)
- Annualized: return +9.1%, volatility 12.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.62, excess kurtosis +5.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.84, max 2.00, latest 0.99

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +11.14%; worst month: -8.06%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.32
- Sideways: S=0.07
- Bear: S=1.78

## Negated Direction
Best negated: `rank(-1 * fnd2_q_flintasamt1expythree / close)` S=0.73, F=0.69, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_q_flintasamt1expythree)`: S=0.60, F=0.56, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expythree / close)`: S=0.73, F=0.69, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expythree, 5))`: S=0.17, F=0.05, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_q_flintasamt1expythree, 5))` | TOP3000 | 0.75 | 0.38 | 21.2% | 80% | mixed |
| `rank(fnd2_q_flintasamt1expythree / close)` | TOP3000 | 0.38 | 0.18 | 8.8% | 80% | bull-only |
| `rank(ts_delta(fnd2_q_flintasamt1expythree, 5))` | TOP1000 | 0.39 | 0.17 | 28.9% | 80% | mixed |
| `rank(fnd2_q_flintasamt1expythree)` | TOP3000 | 0.33 | 0.16 | 21.2% | 60% | bull-only |
| `rank(ts_delta(fnd2_q_flintasamt1expythree, 5))` | TOP200 | 0.10 | 0.02 | 49.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd2_q_flintasamt1expytwo: 0.813 (strongly positively correlated)
- fnd2_q_flintasamt1expyfour: 0.749 (strongly positively correlated)
- fn_finite_lived_intangible_assets_net_q: 0.161 (weakly positively correlated)
- rp_nip_credit_ratings: 0.147 (weakly positively correlated)
- fn_finite_lived_intangible_assets_gross_q: 0.129 (weakly positively correlated)

Redundancy cluster #44: 2 similar fields, mean |rho| 0.749 (representative: fnd2_q_flintasamt1expyfour). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
