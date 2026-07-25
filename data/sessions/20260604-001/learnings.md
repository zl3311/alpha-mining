---
id: "20260604-001-learnings"
session: "20260604-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260604-001

## What Worked

- **Pure options** (no fundamentals) avoids CONCENTRATED_WEIGHT from IV + fundamental blends
- **`zscore(ts_mean(IV spread, d))`** with d=22 upgrades GOOD → EXCELLENT at MARKET neut
- **`ts_decay_linear(..., 10)`** outer wrap with platform decay=10
- Buzz **multiplier** `* (1 + rank(buzz))` is valid; buzz **addition** `+ rank(buzz)` causes unit errors with group_neutralize

## What Didn't Work

- `group_neutralize(IV spread, subindustry)` — EXCELLENT metrics but always fails CONCENTRATED_WEIGHT + SUB_UNIVERSE
- pcr_oi_270 as standalone or IV combo — DEAD
- TOP1000 universe on zscore path — kills signal
- rel_num + drlt MARKET blends — passes BRAIN but 0.818 self-corr vs existing relationships alpha

## Mechanism Insights

Call-put IV spread reflects options market's forward view of upside vs downside risk. Smoothing over 22 days captures persistent sentiment shifts rather than daily noise. Cross-sectional zscore normalizes across the universe; MARKET neutralization decorrelates from the fundamental-heavy submitted book (self-corr 0.309 vs 0.7 threshold).

## Infrastructure Notes

- HF worker can leave jobs stuck in `running` when BRAIN returns WARNING (unit errors) — restart Space to recover
- 15k+ pending background sweep jobs cause multi-minute queue delays even at priority 9
