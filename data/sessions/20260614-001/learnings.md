---
id: "20260614-001-learnings"
session: "20260614-001"
category: "dead_end"
confidence: "high"
actionable: true
---

# Learnings: Session 20260614-001

## What Worked

- `ts_zscore` on sparse fundamental2 share-based compensation tax-benefit fields
  produces high aggregate fitness in the HF queue.
- Adding leverage and deferred revenue components repaired the raw annual
  anchor's low sub-universe failure for quarterly variants.

## What Didn't Work

- The raw annual tax-benefit anchor `RRroP5ra` failed `CONCENTRATED_WEIGHT` at
  0.50 vs 0.10 and failed low sub-universe Sharpe.
- Ranking, group-ranking, decay wrapping, leverage blends, deferred revenue
  blends, buzz-reversal blends, and quarterly substitution did not repair the
  concentration failure.
- `ts_backfill`, `group_backfill`, longer backfill windows, winsorization, and
  smoothed backfilled inputs still produced the same concentration block.

## New Dead Zone

Sparse fundamental2 `ts_zscore` alphas with share-based compensation / tax
benefit / guidance-style fields are structurally blocked by BRAIN concentration
checks. Treat SPECTACULAR aggregate metrics from this family as misleading unless
`CONCENTRATED_WEIGHT` is explicitly verified.

## Mechanism Insight

The economic mechanism is plausible: realized excess tax benefit from share-based
compensation may proxy option exercise, equity compensation events, or profitable
employee liquidity events. The investable implementation is too sparse, causing
BRAIN to place excessive weight in a small set of names.

## Next Steps

- Do not continue mutating tax-benefit fundamental2 `ts_zscore` variants unless
  a new operator directly solves missing-value coverage without preserving the
  same concentrated support.
- Prefer the existing pending queue over this family: `d5Q3ZmWv`, `xAn2kvOp`,
  and `zqOrkbbG` remain more actionable than today's blocked discoveries.
- Next mining session should pivot away from sparse fundamental2/guidance
  `ts_zscore` and back toward structurally novel cross-family interactions or
  validation of existing queued candidates.
