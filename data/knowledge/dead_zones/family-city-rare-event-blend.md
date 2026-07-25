---
category: "dead_zone"
entity_type: "family"
family: "fnd6_city_rare_event_blend"
discovered: "20260617-001"
expressions_tested: 10
best_sharpe: 1.33
best_fitness: 0.76
status: "dead_end"
confidence: "medium"
---

# fnd6_city Rare-Event Blends (concentration repair)

`fnd6_city` (HQ relocation) reaches SPECTACULAR aggregate metrics in its PURE
volatility-gated form (`trade_when(... rank(ts_delta(fnd6_city, 3)) ...)`,
F up to 3.07 with MARKET) but is structurally blocked by `CONCENTRATED_WEIGHT`
(~0.45-0.50 vs 0.10) and `LOW_SUB_UNIVERSE_SHARPE`. The block is inherent:
relocations are rare, so any signal isolating them concentrates weight on a few
names — which is exactly what produces the high fitness.

## What was tried (session 20260617-001, batch `city_refine_r1`)

Blending the city signal with a decorrelated dense stabilizer (`current_ratio`
delta, `open/close-1`, `volume/adv20`) to spread weights and lift sub-universe
Sharpe, across additive / product / volatility-gated / magnitude forms and
3/5/10-day windows. SUBINDUSTRY, decay 6.

## Result

All 10 variants were INFERIOR. Best was `KPb00rrl`
(`rank(ts_delta(fnd6_city,5)) + rank(ts_delta(current_ratio,5)) + rank(open/close-1)`)
at S=1.33, F=0.76 — still below gates. Most variants were S<0.6.

The decorrelating stabilizer dilutes the concentrated relocation signal that
drove the high standalone fitness, collapsing Sharpe. This is the same tension
as `fundamental2_sparse_ts_zscore`: the signal's strength IS its concentration.

## Rule

Do not attempt to fix `fnd6_city` (or similar rare-event sparse signals)
`CONCENTRATED_WEIGHT`/`SUB_UNIVERSE` blocks by additive/product blending with
dense stabilizers — it destroys the signal. A submittable city alpha would need
a fundamentally different densification mechanism (not yet identified), not a
field/window/wrapper swap.
