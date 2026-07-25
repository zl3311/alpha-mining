---
id: "20260709-001-learnings"
session: "20260709-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260709-001

## What Worked

- **Extending `event-magnitude-novel-fields` to `fnd6_tlcf`**: the proven
  4-factor `abs(ts_delta(FIELD/close,3)) + leverage + ivaco + drlt` template
  transfers cleanly to Tax Loss Carry Forward, reaching GOOD (F=1.79,
  confirmed self-corr PASS 0.6372).
- **Buzz-stabilizer as a 5th factor**: adding
  `rank(ts_mean(scl12_buzz,5)*(-1*returns))` to the tlcf 4-factor blend lifted
  it from GOOD to EXCELLENT (F 1.79→2.22) at essentially no self-corr cost
  (0.6372→0.6262). New pattern: `event-magnitude-buzz-boost.md`.
- **Local PnL pre-filter calibration**: for this specific family, local PnL
  corr underestimated BRAIN's authoritative corr by only ~1.09x (0.586 local →
  0.637 BRAIN for `blqLGagK`), much milder than the documented 1.45-1.6x
  "shared field" inflation — useful data point for triaging candidates when
  BRAIN's `/check` endpoint is slow to resolve.

## What Didn't Work

- **Directional gating via `sign(ts_delta(price/volume,d))`**: uniformly
  negative Sharpe, 40-60% turnover, across 5 fields. New dead zone:
  `template-directional-gating-sign-delta.md`.
- **Multi-horizon spread** (`ts_delta(F,5)-ts_delta(F,22)`) on low-usage fields:
  weak everywhere (best S=0.72, still INFERIOR).
- **Non-linear magnitude×level** (`rank(F)*rank(abs(ts_delta(F,d)))`): weak
  (best F=0.59).
- **Convex self-product** (`rank(F)*rank(F)`), **dispersion**
  (`max(F1,F2)-min(F1,F2)`), and **raw flag×sentiment products**
  (`rank(anl4_flag)*rank(-1*sentiment)`) on strong standalone fields
  (`ivaco`, `rel_num_all`, `enterprise_value`, `netdebt_flag`): all failed to
  clear GOOD grade. New dead zone:
  `template-convex-dispersion-flag-sentiment.md`.
- **`fnd6_dcvsub` event-magnitude**: reaches GOOD (F=1.89) but self-corr FAILs
  at 0.7693-0.8066 vs the itci-family cluster — same failure mode as `drc`/
  `cshtr` in the original `event-magnitude-novel-fields` pattern. Confirms
  the pattern's guidance to avoid debt/credit-like event fields; capital/
  investment-like fields (`ppegtq`, `dd1q`, now `tlcf`) pass, debt-like
  fields (`drc`, `cshtr`, `dcvsub`) fail.
- **Removing `/close` normalization from the event field** (raw `fnd6_tlcf`
  instead of `fnd6_tlcf/close`): boosts fitness (F 1.79→2.14 even without
  buzz) but raises local self-corr estimate materially (0.586→0.710) — BRAIN's
  `/check` endpoint did not resolve to confirm/deny within the session.
  Treat as elevated risk; the `/close`-normalized + buzz variant (`rKlo39p1`)
  is the safer choice at similar fitness.
- **Ultra-low-coverage analyst estimate fields** (`anl4_qf_az_wol_spfc`,
  `anl4_qf_az_wol_vid`, coverage ~0.33-0.49, alphaCount ~100): all INFERIOR
  standalone and in a product-interaction-blend. Confirms the
  `analyst4-earnings-estimates.md` opportunity's closure extends to these
  extreme-low-usage fields too.

## New Rules Discovered

None (no hard universal constraint found; see dead zones for template-specific
findings).

## New Dead Zones

- `template-directional-gating-sign-delta.md`
- `template-convex-dispersion-flag-sentiment.md`

## New Patterns

- `event-magnitude-buzz-boost.md`

## Mechanism Insights

- The `event-magnitude-novel-fields` pattern's self-corr split (capital/
  investment fields PASS, debt/credit fields FAIL against the itci-family
  cluster) held up on a 3rd data point (`tlcf` passes, `dcvsub` fails),
  strengthening confidence this is a real economic distinction, not noise:
  the itci-family's shared "leverage + drlt" base already captures the
  debt-related signal dimension, so a debt-like event field is largely
  redundant (high corr), while a capital-allocation-like event field
  (PP&E, tax attributes, deferred revenue timing) adds a genuinely
  orthogonal dimension.
- Structurally novel operator-tree shapes (this session's rounds 1-2) are
  NOT a reliable shortcut to decorrelation. Self-corr in the book is driven
  far more by shared RAW FIELDS (leverage, drlt, ivaco, open/close-1,
  analyst flags) than by expression tree shape — a proven template on an
  unused field decorrelates better than a novel tree shape on a
  well-worn field. This nuances `novelty-required.md`: structural novelty
  is valuable for finding NEW signal (avoiding "priced-in" templates), but
  is not by itself a decorrelation strategy.

## Housekeeping Notes (not part of this session's scope, flagged for follow-up)

- Three draft PRs (#79, #80, #81) remain open/unmerged, carrying dead
  zones/patterns (`family-negated-tax-ptpr-core`, `negated-fresh-fundamental6-blends`,
  `event-magnitude-novel-fields`, `negated-ev-netdebt-blend`) and 2 EXCELLENT
  submittable candidates (`2rLRzov8` self-corr 0.6495, `wpl5eP5v` self-corr
  0.6676) that this session had to re-derive from PR bodies since they aren't
  on `main`. Recommend merging or closing these soon to avoid future sessions
  repeating this reconstruction work.
- `data/book/ZYpjKeKx.md` has an uncommitted local status update (PENDING→ACTIVE,
  submitted 2026-07-06) sitting on `main` since before this session started —
  not touched by this PR (out of scope), but should be committed separately.
- Two orphaned incomplete session directories (`20260705-001`, `20260706-002`)
  exist locally with `status: in_progress` and no `results.md` — appear to be
  abandoned mid-session artifacts from prior chats. Not touched by this PR.
