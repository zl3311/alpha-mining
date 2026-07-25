---
category: "dead_zone"
entity_type: "field_cluster"
family: "sparse_analyst_guidance_untested_fields"
discovered: "20260710-001"
expressions_tested: 46
best_sharpe: 1.70
best_fitness: 1.41
status: "capped_at_average"
confidence: "medium"
---

# Sparse Analyst-Forecast / Guidance Untested Fields — Capped at AVERAGE

Session `20260710-001` tested the remaining genuinely untested singleton fields
from the opportunity consumed by sessions `20260706-001` and `20260710-001`
(items 4-6, 8, 10, plus fresh negated tax fields not previously tried
standalone):

- `min_tangible_book_value_per_share_guidance_2`
- `anl4_qf_az_wol_spfc`, `anl4_qfd1_az_wol_spfc` (and `_vid` variants)
- `fn_comp_options_forfeitures_and_expirations_a`
- `fn_prepaid_expense_q`
- `fnd6_txw` (raw/negated level, non-event-magnitude forms), `fnd6_txdbca`
- `fnd6_intc` (negated, paired with fresh partners), `fnd6_acqgdwl` (negated)
- `fnd6_mrct` (additive/product level forms)

## What was tried (46 sims across 3 rounds)

- Additive blends with `open/close-1` and each other (proven `blend-template`
  pattern)
- Product-interaction blends (proven `product-interaction-blend` pattern)
- `zscore()` normalization (per `zscore-accumulated-revision` pattern, in case
  these sparse fields behave like analyst revision flags)
- Directional gating (`sign(ts_delta(...))`), multi-horizon spread,
  max/min dispersion (structurally novel EXPLORE templates)
- MARKET neutralization variant of the best SUBINDUSTRY blend (confirmed
  MARKET hurts, consistent with `market-neut-tradeoff.md`)
- Negated forms of `fnd6_txw`/`fnd6_txdbca`/`fnd6_intc`/`fnd6_acqgdwl` blended
  with the fresh analyst-forecast fields above

## Result

Best result across all templates: `WjGV3Mrx` (`anl4_qf_az_wol_spfc` +
`anl4_qf_az_wol_vid` + `2 * (open/close-1)`), S=1.70, F=1.41, AVERAGE. No
variant reached the EXCELLENT threshold (F>=~2.0) using LEVEL/RANK/ZSCORE forms
of these fields directly. All these fields carry weak standalone signal in
their raw/level form.

## Critical exception: event-magnitude transform breaks through

`fnd6_txw` and `fnd6_txdbca` (level forms tested here as capped-AVERAGE) DO
respond strongly to the `abs(ts_delta(F / close, 3))` **event-magnitude**
transform (see `data/factors/fnd6_txw.md` and pattern
`event-magnitude-buzz-boost.md`) — this dead zone applies to LEVEL/RANK
forms of these fields, not the event-magnitude transform, which reached
SPECTACULAR (S=2.63, F=2.68, `WjGVJ7bN`).

`fn_prepaid_expense_q`, `fn_comp_options_forfeitures_and_expirations_a`, and
`fnd6_mrct` were ALSO tested under the event-magnitude + leverage + ivaco +
drlt 4-factor template (round 3-4) and stayed capped at AVERAGE (F<=1.40).
Adding the buzz fifth leg lifted `fn_prepaid_expense_q` and `fnd6_mrct` to
GOOD (F=1.77 and F=1.75), but not EXCELLENT. The event-magnitude breakthrough
to EXCELLENT+ is therefore specific to `fnd6_txw`/`fnd6_txdbca` among these
fields.

## Rule

Do not re-test LEVEL/RANK/ZSCORE forms of `anl4_qf_az_wol_spfc/vid`,
`min_tangible_book_value_per_share_guidance_2`,
`fn_comp_options_forfeitures_and_expirations_a`, or `fn_prepaid_expense_q`
with simple additive/product/directional-gating templates — confirmed weak.
`fnd6_mrct` remains below EXCELLENT under both level blends and the
event-magnitude + buzz template. Revisit only with a genuinely different
mechanism.
