---
id: "20260716-001-learnings"
session: "20260716-001"
category: "discovery"
confidence: "medium"
actionable: true
---

# Learnings: Session 20260716-001

## What Worked

- **Dropping the leverage (`-1*equity/assets`) and `fnd6_drlt` legs entirely,
  while double-weighting the remaining `fnd6_ivaco` and
  `ts_mean(scl12_buzz,10)*(-1*returns)` legs, and using TWO fresh anchors
  instead of one** turned a self-corr-BLOCKED EXCELLENT candidate (0.775-0.926)
  into a much-lower-corr EXCELLENT candidate (0.618) with HIGHER fitness
  (2.26 vs 2.00-2.21). This is the session's main actionable discovery — see
  pattern `leverage-free-fresh-anchor-decorrelation.md`.
- `fnd6_cld2` (capitalized lease, year 2) is a genuinely clean, low-turnover,
  100%-consistent standalone signal from an essentially untouched redundancy
  cluster (#14, 2 members) — the best fresh anchor quality found this
  session.
- Buzz window sweep (5/10/20) matters: window=10 outperformed both 5 and 20
  for this specific 4-leg skeleton (F=2.26 vs 2.03 and 2.13).
- Isolating single shared legs (test anchor+ivaco-only, anchor+drlt-only,
  anchor+buzz-only) is a fast, cheap diagnostic for identifying which
  specific component drives fitness vs. correlation before committing budget
  to full-stack tests.

## What Didn't Work

- Multi-horizon spread, MA crossover, and `ts_zscore` regime divergence on
  fundamental2/6 fields: near-zero signal, 15-21% turnover (new dead zone).
- The completely untapped `model51` risk/beta dataset: decent raw Sharpe
  (0.8-1.4) but inherently high turnover (28-56%) that `ts_decay_linear`
  could not suppress, capping fitness at INFERIOR (new dead zone).
- Fresh anchor + leverage-only (no ivaco/drlt/buzz): capped at AVERAGE
  (F<=1.19) regardless of product/additive form or secondary quality legs
  (cash/assets, debt_lt/assets).
- MARKET neutralization: reduced local self-corr (0.775->0.664-0.679) as
  expected, but the accompanying fitness drop (2.03->1.86) pushed grade from
  EXCELLENT to GOOD — not viable as a standalone EXCELLENT+ decorrelation
  fix for this family, confirming `market-neut-tradeoff.md` generalizes here.
- Dropping ivaco or buzz (not just de-weighting): collapses fitness to
  AVERAGE (F<=1.27) even with the other legs at higher weight — both are
  structurally necessary, not swappable for pure fresh-anchor weight.

## New Rules Discovered

- `stabilizer-stack-block-generalizes-beyond-pstkrv.md`: the classic
  event-magnitude stabilizer stack's self-corr block is a property of the
  STACK (5 independent anchors now confirmed), not of any specific "unlucky"
  anchor field.
  **[Correction 20260719-001: the rule has since been narrowed to
  leverage-bearing forms only. `-1*equity/assets` is the load-bearing
  correlate; without it the same stack clears 0.70 — `N1rlJ7mq` (0.6903) and
  this session's own `aknmG1M6` (0.6181) are both ACTIVE. One of the five
  anchors cited, `fnd6_pstkrv`, was counted on a misattributed reading.]**

## New Dead Zones

- `template-multi-horizon-ma-crossover-regime-divergence.md`
- `dataset-model51-high-turnover.md`

## New Patterns

- `leverage-free-fresh-anchor-decorrelation.md`

## Mechanism Insights

- The event-magnitude family's correlation ceiling is driven by the STABILIZER
  legs (ivaco, drlt, leverage, buzz, analyst flags), not the anchor. A fresh
  anchor's own decorrelation only shows through once enough of the shared
  legs are removed — but removing shared legs costs fitness roughly linearly
  UNLESS compensated by (a) a second fresh anchor and (b) up-weighting the
  remaining shared legs. This session found the removal of `leverage+drlt`
  specifically to be a favorable trade (loses less fitness than it gains in
  decorrelation) for the `fnd6_cld2`+`fnd6_fopo` anchor pair — but this
  specific 2-leg-removal choice was found empirically via ablation, not
  predicted a priori, and may not generalize to other anchor pairs without
  re-testing.
- **Process note**: BRAIN's authoritative self-correlation `/check` endpoint
  became fully unresponsive (repeated `PENDING`/timeout, then
  `httpx.ConnectTimeout`) during this session, independently corroborating
  `20260715-002`'s same-week report of platform degradation. Sessions
  running during this window should treat the local PnL estimate as the
  ONLY practical signal, explicitly flag results as UNCONFIRMED rather than
  PASS/FAIL, and re-verify once the platform recovers — do not silently
  treat "local estimate looks favorable" as equivalent to "BRAIN-confirmed
  PASS" in book entries or PR summaries.
