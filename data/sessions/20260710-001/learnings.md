---
id: "20260710-001-learnings"
session: "20260710-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260710-001

## What Worked

- **Event-magnitude transform generalizes beyond itci/ppegtq/tlcf.** The
  `abs(ts_delta(F/close, 3))` template, combined with the proven
  leverage+ivaco+drlt stabilizer trio, breaks through on `fnd6_txw` (Excise
  Taxes) and `fnd6_txdbca` (Deferred Tax Asset - Current) — two more fields
  that were WEAK in raw level/rank/zscore/product form but strong under the
  event-magnitude transform. This is now the 4th and 5th confirmed field for
  this pattern family.
- **Buzz-stabilizer 5th leg reliably boosts event-magnitude blends** — tested
  on 3 fields this session (txw, mrct, prepaid_expense_q), all improved
  (F +0.37 to +0.90). New pattern: `event-magnitude-buzz-boost.md`. This
  independently confirms and generalizes the same finding from session
  `20260709-001` (`fnd6_tlcf`).
- **A shared stabilizer combo can remain submittable through Sharpe premium** —
  ACTIVE `wpl5eP5v` shares 3 of `WjGVJ7bN`'s 5 legs and has 0.7096 correlation,
  but WjGVJ7bN clears the premium escape (2.63 > 1.10 × 2.09). Shared
  stabilizers therefore require explicit correlation and premium checks rather
  than automatic rejection.

## What Didn't Work

- **Fresh untested singleton fields have weak standalone signal.** All of
  `min_tangible_book_value_per_share_guidance_2`, `anl4_qf_az_wol_spfc/vid`,
  `fn_comp_options_forfeitures_and_expirations_a`, `fn_prepaid_expense_q`
  capped at AVERAGE (F<=1.41) across additive, product, zscore, and
  directional-gating templates (46 sims, rounds 1-2). New dead zone:
  `family-sparse-analyst-guidance-untested-fields.md`.
- **Not every field responds to event-magnitude + full stabilizer.**
  `fn_prepaid_expense_q`, `fn_comp_options_forfeitures_and_expirations_a`, and
  `fnd6_mrct` were ALSO tested under the full proven template (round 3-4) and
  stayed capped at AVERAGE/GOOD (F<=1.77) — the SPECTACULAR-tier breakthrough
  is specific to `fnd6_txw` among the 5 fields tried with the full stabilizer.
- **MARKET neutralization confirmed to hurt** the sparse-analyst-forecast
  template (S 1.42→0.81), consistent with `market-neut-tradeoff.md`.
- **`anl4_qfd1_az_wol_spfc/vid` (forward-quarter variants)** perform similarly
  to or worse than the current-quarter `anl4_qf_az_wol_spfc/vid` — no
  incremental value from combining both horizons (4-factor combo of all 4
  reached only INFERIOR F=1.0).

## New Rules Discovered

None — existing rules (`market-neut-tradeoff`, `self-corr-pnl-gap`) were
reconfirmed, not contradicted.

## New Dead Zones

- `family-sparse-analyst-guidance-untested-fields.md` — LEVEL/RANK forms of
  6 untested fields cap at AVERAGE.

## New Patterns

- `event-magnitude-buzz-boost.md` — generalizes the buzz 5th-leg boost across
  4 fields now (tlcf from PR #82, txw, mrct, prepaid_expense_q from this
  session).

## Mechanism Insights

`fnd6_txw` (Excise Taxes) is a niche, low-community-usage field
(alphaCount≈969) whose raw level carries almost no cross-sectional signal —
excise tax dollar amounts are dominated by firm size and industry composition,
not information content. But the *3-day magnitude of change* in excise tax
relative to price is a genuine event signal: large swings correspond to
one-off regulatory shifts, new taxed product lines, or rate changes that
markets are slow to price in, exactly mirroring the `fnd6_itci` (inventory)
mechanism. This is now the clearest evidence that the event-magnitude
transform is a genuinely general-purpose technique for "sparse event, weak
level" fundamental6 fields, not an itci-specific quirk.

## Pre-Existing Backlog Note (context, not addressed by this session)

At session start, three prior draft PRs carried EXCELLENT candidates:
`2rLRzov8` (0.6495, PR #80), `wpl5eP5v` (0.6676 before becoming an ACTIVE peer,
PR #81), and `rKlo39p1` (0.6262, PR #82). This session's `WjGVJ7bN` is net-new
and SPECTACULAR. After submission, its maximum ACTIVE-book correlation is
0.7096 vs `wpl5eP5v`, passing through Sharpe premium.
