---
id: "20260615-001-learnings"
session: "20260615-001"
category: "refinement"
confidence: "high"
actionable: true
---

# Learnings: Session 20260615-001

## What Worked

- **Cross-family / orthogonal blends decorrelate (thesis confirmed).** `kqKAKLgl`
  (guidance + itci) reached self-corr 0.608 — the lowest of any EXCELLENT this
  session. `78deK038` (fundamental + sales_count + smoothed pcr/news tilts)
  reached max 0.665. The merge/theme analysis (PR #47) correctly identified the
  decorrelation direction.
- **Smoothing orthogonal legs with `ts_mean(...,22)` fixes the turnover blowup.**
  Raw `pcr`/`news` legs hit 45-120% turnover; smoothed they drop to ~5% and can
  be added as small decorrelating tilts without wrecking fitness.
- **One submittable alpha found:** `LLR0Xjz2` (AVERAGE) passes all 8 IS checks +
  self-corr 0.675 < 0.70. Clean fundamental + analyst-coverage blend, no itci/IV/
  flag-ret.

## What Didn't Work

- **Equal-weight stacking of strong core + weak orthogonal leg dilutes** (the
  diversification benefit in the analysis assumed unit-vol pooling, not raw
  `rank(A)+rank(B)`). All round 1-2 equal blends were INFERIOR.
- **Orthogonal dead-zone legs cannot carry EXCELLENT** (option9 PCR, fundamental2
  deferred-tax, model16 scores, news flow are weak standalone, as their dead-zone
  entries say). They only work as small decorrelating tilts.
- **MARKET neut kills the fundamental value signal** (`itci` F1.81 SUB -> 0.28
  MARKET). Value is a subindustry effect.

## New Rules Discovered

- **`LOW_SUB_UNIVERSE_SHARPE` limit scales with fitness.** Raising a clean blend's
  fitness from AVERAGE -> GOOD re-triggers the sub-universe failure (the limit
  rises faster than the sub-universe Sharpe). So in the clean-field regime,
  submittable == AVERAGE grade; GOOD+ fails sub-universe. (Candidate for promotion
  to `rules/`.)
- **Every clean EXCELLENT in the explored universe depends on a blocked/banned
  mechanism:** `itci` (sub-universe fail), IV call-put spread (self-corr
  saturated), or `flag*(-ret)` (banned). Removing any drops grade to GOOD. 0/21k
  sweep EXCELLENT signals pass the hard checks outside these.

## New Dead Zones

- None new. Reconfirmed option9/fundamental2/model16/news weakness as STANDALONE,
  but documented they are usable as decorrelating tilts (nuance to the existing
  dead-zone entries).

## New Patterns

- **`orthogonal-theme-diversification`** (already added in PR #47) validated:
  decorrelation works, but is fitness-limited.
- **Smoothed-tilt decorrelation**: `clean_core + rank(ts_mean(orthogonal_field, 22))`
  adds an independent return stream at low turnover.

## Mechanism Insights

- The IV call-put spread is the strongest mechanism available (SPECTACULAR, F up
  to 4.38 at 90-day) but the term structure is ~identical across maturities
  (corr 0.95-0.99), so the family is fully saturated by `vRm07LP3` + `Gro21wWG`.
  Escaping needs S >= 2.85 (1.10x Gro21wWG), which no maturity/structure reaches.
- **Process bug surfaced:** `Gro21wWG` (S2.59, the binding IV self-corr peer on the
  BRAIN platform) is missing from `data/book/`. The local book is stale and
  understates IV saturation; sync needed.
