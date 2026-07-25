---
type: "submit-candidate"
alpha_id: "wpl5eP5v"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.09
fitness: 2.20
turnover: 0.087
self_corr_max: 0.6676
self_corr_peer: "0m8GV1Pp"
neutralization: "SUBINDUSTRY"
decay: 6
family: "ppegtq_event_magnitude_leverage"
session: "20260708-001"
brain_url: "https://platform.worldquantbrain.com/alpha/wpl5eP5v"
queued: "2026-07-08"
long_term_value: "LOW"
---

# Submit wpl5eP5v (ppegtq event-magnitude + leverage)

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_ppegtq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close), 5)
```

## Why submittable

- Grade EXCELLENT, S=2.09, F=2.20, T=8.7%.
- All 8 BRAIN submission checks PASS (7 computable + SELF_CORRELATION).
- BRAIN `/check` SELF_CORRELATION: **PASS**, value 0.6676 (limit 0.70). Top peer
  `0m8GV1Pp` (itci event-magnitude family); ppegtq event signal decorrelates from itci.
- Novel mechanism family: event-magnitude transferred to ppegtq (PP&E gross) — the
  first non-itci event-magnitude alpha in the book.

## Reviewer action

Submitted by the user on the BRAIN platform (2026-07-08). `data/book/wpl5eP5v.md`
flipped to `status: ACTIVE` with `submitted: "2026-07-08"`.

## Notes

- Self-corr 0.6676 is barely under the 0.7 limit (LOW long-term value). Submit AFTER
  any lower-corr EXCELLENT+ candidates in the queue to preserve correlation headroom.
- Extends the `event-magnitude-abs-ts-delta` pattern to a new field; see
  `data/knowledge/patterns/event-magnitude-novel-fields.md`.
