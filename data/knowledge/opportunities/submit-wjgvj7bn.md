---
type: "submit-candidate"
alpha_id: "WjGVJ7bN"
status: "SUBMITTED"
submitted: "2026-07-10"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.63
fitness: 2.68
turnover: 0.1095
self_corr_max: 0.7096
neutralization: "SUBINDUSTRY"
decay: 6
family: "excise_tax_event_magnitude_leverage_buzz"
session: "20260710-001"
brain_url: "https://platform.worldquantbrain.com/alpha/WjGVJ7bN"
queued: "2026-07-10"
long_term_value: "LOW"
---

# Submit WjGVJ7bN (excise tax event-magnitude + leverage + buzz)

## Expression
`ts_decay_linear(rank(abs(ts_delta(fnd6_txw / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Why submittable
- Self-corr 0.7096 vs ACTIVE `wpl5eP5v`; PASS through the Sharpe-premium escape
  (2.63 > 1.10 × 2.09 = 2.299). All 7 computable BRAIN checks pass.
- Grade SPECTACULAR, S=2.63, F=2.68, T=10.95%.
- The pre-submission `/check` returned `ERROR`, but BRAIN subsequently accepted
  both WjGVJ7bN and its top peer, confirming the Sharpe-premium path.
- `fnd6_txw` (Excise Taxes) is a genuinely new field, not used in any other
  book entry or factor file.

## Reviewer action

Submitted 2026-07-10, confirmed ACTIVE on the BRAIN platform (grade
SPECTACULAR, S=2.63, F=2.68, all checks PASS). `data/book/WjGVJ7bN.md` flipped
to `status: ACTIVE`. No further action needed.
