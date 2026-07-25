---
type: "submit-candidate"
alpha_id: "VkOx1K9b"
status: "STALE"
priority: "medium"
grade: "GOOD"
sharpe: null
fitness: 1.72
turnover: null
self_corr_max: 0.492
neutralization: "MARKET"
decay: null
family: "fundamental"
session: null
brain_url: "https://platform.worldquantbrain.com/alpha/VkOx1K9b"
queued: "2026-06-04"
---

# Submit VkOx1K9b (itci + acdo MARKET)

## Expression
`rank(fnd6_itci/close) + rank(fnd6_acdo) + rank(anl4_netdebt_flag)` MARKET neut.

## Why submittable
- Self-corr 0.492 vs current book (SAFE — safest candidate found to date).
- All computable BRAIN checks pass. Grade GOOD, F=1.72.

## Trade-off
GOOD grade (not EXCELLENT) but uniquely uncorrelated. Decision pending: is a GOOD
grade worth a submission slot near the self-corr wall?

## Status: STALE (2026-06-25)
Marked stale during consistency audit. Book has grown from 15 to 34 alphas since
this was queued; self-corr profile likely changed. No `data/book/VkOx1K9b.md`
was ever created. Re-run self-corr check before reconsidering.

## Reviewer action
Re-check self-corr against current 29-ACTIVE book before acting.
If still viable, create `data/book/VkOx1K9b.md` and submit. If declined, set
`status: REJECTED`.
