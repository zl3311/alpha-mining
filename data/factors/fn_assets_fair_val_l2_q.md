---
field: "fn_assets_fair_val_l2_q"
dataset: "fundamental2"
family: "fair_value_asset"
discovery_session: "20260715-001"
best_sharpe: 2.01
best_fitness: 2.01
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_cff_flag) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
mechanism: "Event-magnitude of Level-2 (model-priced) fair-value asset changes signals a re-marking event (rate/credit shock, hedge restructuring, valuation-model change) that the market underreacts to, regardless of direction"
status: "active"
---

# Factor: fn_assets_fair_val_l2_q

*Assets Fair Value, Recurring, Level 2 (Quarterly)*

## Economic Mechanism

Level-2 fair-value assets are financial instruments (derivatives, structured
notes, hedges) held on the asset side of the balance sheet and priced by
internal models using observable market inputs rather than a quoted market
price. This is the asset-side counterpart to `fn_liab_fair_val_l2_q` (already
ACTIVE as `YP0bLdzA`): both track the same re-marking phenomenon, just on
opposite sides of the balance sheet. Large quarter-over-quarter revaluations
reflect a genuine change in the underlying risk exposure or a valuation-model
change, both opaque to most market participants and underreacted to. The
`abs(ts_delta(F/close, 3))` transform captures the SIZE of this re-marking
event regardless of direction, following the `event-magnitude-abs-ts-delta`
template (originally validated on `fnd6_itci` inventory events).

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_cff_flag) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

EXCELLENT, S=2.01, F=2.01, T=11.04%, SUBINDUSTRY, decay=6, TOP3000, USA.
Alpha `lelNqEZl` (PENDING, session 20260715-001).

## Lessons

- **Genuinely more orthogonal anchor than its liability-side sibling**: per
  `data/knowledge/opportunities/factor-themes-redundancy.md`, this field sits
  in redundancy cluster #21 (only 2 members: itself and
  `fn_liab_fair_val_l2_q`) — far outside the book's two dominant mega-clusters
  (fundamental value/debt, #1, 232 members; analyst revision, #13, 127
  members). On the identical 5-leg event-magnitude template, this anchor
  correlated a comfortable **0.572** vs the full book (best 5-factor variant,
  `N1r20nKL`), the lowest of any candidate tested this session, and lower than
  its own liability-side sibling's 0.673-0.71 range.
- **Adding BOTH `fnd6_drlt` and `fnd6_ivaco` as dual stabilizers (6-factor
  form) — not previously tried in this template family, which had only ever
  used one or the other alongside a single fresh flag — lifted GOOD (F=1.75,
  single-stabilizer) to EXCELLENT (F=2.01) without materially raising
  correlation** (0.572→0.567, essentially flat). This is a new decorrelation-
  preserving fitness lever for the family beyond the buzz-boost and
  fresh-stabilizer-swap patterns already documented.
- **The novel `ts_arg_max` recency-of-shock structure works on this anchor but
  correlates higher (0.701, BLOCKED) than the additive `ts_decay_linear` form
  (0.567, SAFE) despite similar Sharpe/Fitness** — see new pattern
  `event-magnitude-recency-arg-max.md`. The wrapper/structure choice, not just
  the anchor field, materially affects self-correlation for this family.
- **Standalone is LOW_SHARPE-blocked** per
  `data/knowledge/factor_profiles/fn_assets_fair_val_l2_q.md`: best solo form
  S=1.21, F=0.74 (INFERIOR). The event-magnitude transform + multi-leg blend
  is required to reach submission gates, same as its liability-side sibling.
