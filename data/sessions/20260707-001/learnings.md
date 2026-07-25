---
id: "20260707-001-learnings"
session: "20260707-001"
category: "refinement"
confidence: "high"
actionable: true
---

# Learnings: Session 20260707-001

## What Worked

- **Verification-only EXPLOIT on the 24h gate-passers** produced a submittable
  EXCELLENT candidate with zero new simulations. When the queue already contains
  novel-family gate-passers from recent sessions, authoritative self-corr checking
  is the highest-leverage move (no budget cost).
- **`anl4_netdebt_flag` as the decorrelation lever**: replacing the saturated
  `anl4_ptpr_flag` with `anl4_netdebt_flag` in the negated-enterprise-value blend
  dropped self-corr from 0.94 (negated-tax + ptpr) to 0.6495 (negated-EV + netdebt)
  — below the 0.7 auto-pass. The analyst FLAG choice matters more than the
  fundamental anchor for self-corr.
- **Negated enterprise value** is a genuinely decorrelated fundamental anchor: no
  positive-EV or negated-EV entry existed in the book, and the negated direction
  aligns with the book-saturation rule's 5x-more-dimensions recommendation.

## What Didn't Work

- **Negated tax (fnd6_txw, fnd6_txdbca) + ptpr + open/close**: SPECTACULAR/EXCELLENT
  IS metrics but self-corr **0.94** vs book. Negating the fundamental anchor does
  NOT decorrelate when the `anl4_ptpr_flag + open/close - 1` core is shared with
  LLR0n261 / O0ZOJbaq / O0pl2znv. The ptpr+intraday core is the correlation wall,
  not the fundamental field.
- **itci event-magnitude + neg-leverage + drlt (1Yd65kmJ)**: SPECTACULAR S=2.62 but
  self-corr **0.997** vs 0m8GV1Pp — a near-duplicate (delta 5 vs 3). The
  event-magnitude-on-itci + `rank(-1 * equity/assets)` + `fnd6_drlt` family is
  already claimed by 0m8GV1Pp and d5Q3ZmWv. Do NOT mutate further.
- **`abs(ts_delta(itci/close, 5)) + anl4_netdebt_flag` (YP0XZxav)**: more decorrelated
  but fails LOW_SUB_UNIVERSE_SHARPE (0.84 < 0.87) — sub-universe concentration.
- **BRAIN SELF_CORRELATION computation latency**: 4 of 8 candidates timed out after
  10 poll retries on the authoritative `/check` endpoint (recurring issue noted in
  20260703-001). Results that did return were valid. Re-polling later may yield the
  remaining verdicts, but they were not needed once 2rLRzov8 confirmed PASS.

## New Rules Discovered

None promoted to `data/knowledge/rules/` this session — findings reinforce existing
rules (book-saturation negation direction, self-corr-pnl-gap, the saturated
ptpr+open/close core). The negated-tax + ptpr self-corr wall is a corollary of the
existing ptpr-core saturation, not a new rule.

## New Dead Zones

- **Negated-tax + `anl4_ptpr_flag` + `open/close - 1`** family: self-corr 0.94 wall
  (fnd6_txw, fnd6_txdbca, fnd6_intc all blocked). The negation does not escape the
  ptpr-core correlation. Promote to `data/knowledge/dead_zones/family-negated-tax-ptpr-core.md`.
- **itci event-magnitude + neg-leverage + drlt** family: claimed by 0m8GV1Pp /
  d5Q3ZmWv at 0.997 corr. Mutating the delta window (3→5) does NOT decorrelate.

## New Patterns

- **Negated-EV + netdebt_flag blend template** (winner): a reusable decorrelation
  recipe — negated fundamental anchor + `anl4_netdebt_flag` (not ptpr) + cash-quality
  companion (`fnd6_cshtr`) + leverage companion (`fnd6_drlt`) + overnight gap. Promote
  to `data/knowledge/patterns/negated-ev-netdebt-blend.md`.

## Mechanism Insights

- Negating a fundamental field changes the *direction* of the fundamental signal but
  does NOT change the correlation contribution of the shared analyst-flag + intraday
  components. Self-corr decorrelation requires swapping the SHARED components, not
  negating the unique anchor.
- `enterprise_value` (a constructed field = market cap + debt - cash) behaves as a
  decorrelated fundamental anchor because no book entry uses it — the field's novelty
  matters more than its sign for self-corr purposes.
