---
field: "fnd6_txw"
dataset: "fundamental6"
family: "excise_tax_event_magnitude"
discovery_session: "20260710-001"
best_sharpe: 2.63
best_fitness: 2.68
best_expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_txw / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
mechanism: "Event-magnitude (abs ts_delta) transform on excise tax expense — large 3-day swings signal one-off regulatory/product-mix tax events the market underreacts to"
status: "active"
---

# Factor: fnd6_txw (Excise Taxes)

## Economic Mechanism

`fnd6_txw` (Excise Taxes) captures a niche fundamental6 line item with low
community usage (alphaCount ~969). Raw level and simple rank forms produce weak
standalone signal (see `learnings.md` for session 20260710-001, S<1.3 for
level/rank/negated forms). However, the `abs(ts_delta(fnd6_txw / close, D))`
event-magnitude transform — the same template that works for `fnd6_itci`,
`fnd6_newqv1300_ppegtq`, and `fnd6_tlcf` — captures large excise-tax swings
(new taxed product lines, rate changes, regulatory shifts) that the market is
slow to price in, regardless of direction.

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_txw / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

SUBINDUSTRY neutralization, platform decay=6, TOP3000. S=2.63, F=2.68, T=10.95%.

## Lessons

- Additive/product blends of the RAW level with fresh analyst-forecast fields
  (`anl4_qf_az_wol_spfc/vid`) cap at AVERAGE (F<=1.13) — the raw field carries
  little standalone signal.
- The event-magnitude transform (`abs(ts_delta(fnd6_txw / close, 3))`) plus the
  proven leverage+ivaco+drlt stabilizer trio reaches GOOD (F=1.78) on its own;
  adding the `buzz-stabilizer` 5th leg lifts it to SPECTACULAR (F=2.68) — see
  pattern `event-magnitude-buzz-boost.md`.
- `fnd6_txdbca` (Deferred Tax Asset - Current) responds similarly to the same
  template (GOOD, F=1.87) but was not the primary pick since `fnd6_txw` scored
  higher and the two are near-duplicates (mutual corr 0.87-0.98 — only one is
  submittable at a time).
- d=5 window on the event leg performs marginally worse than d=3 for this field.
