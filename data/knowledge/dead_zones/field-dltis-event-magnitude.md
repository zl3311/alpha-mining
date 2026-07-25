---
category: "dead_zone"
entity_type: "field"
field: "fnd6_dltis"
discovered: "20260711-001"
expressions_tested: 3
best_sharpe: 2.54
best_fitness: 2.63
blocking_check: "SELF_CORRELATION"
status: "blocked"
---

# fnd6_dltis on the event-magnitude-abs-ts-delta Template — Self-Corr Blocked

`fnd6_dltis` (long-term debt issuance, a FLOW item distinct from the LEVEL
debt fields `debt`/`debt_lt`/`fnd6_dlto` already in the book) produces
SPECTACULAR aggregate metrics on the proven `event-magnitude-abs-ts-delta +
leverage + ivaco + drlt (+ buzz)` template (S=2.45-2.54, F=2.56-2.65, all 7
computable BRAIN checks PASS across 3 event-window variants d=3/5/10 tested in
session 20260711-001), but correlates **0.93-0.94** with the ACTIVE alpha
`WjGVJ7bN` (`fnd6_txw`-anchored, same template) — far above the 0.70 threshold
and far short of the 1.10x Sharpe premium (2.63*1.10=2.89 vs candidate ~2.5).

## Why it's blocked

Debt issuance (`dltis`, a flow) and excise tax expense (`txw`, also a flow) are
economically adjacent balance-sheet/income-statement flow items with similar
temporal dynamics (both driven by discrete corporate financing/tax events), so
their `abs(ts_delta(F/close,d))` event-magnitude signals move together closely
enough that the shared `leverage + ivaco + drlt + buzz` stabilizer legs are not
enough to decorrelate them — unlike `fn_liab_fair_val_l2_q` (fair-value
liability re-marking), which is economically distinct enough to correlate only
0.67-0.71 with the same peer on the identical template (see
`data/factors/fn_liab_fair_val_l2_q.md` and pattern
`event-magnitude-fresh-stabilizer.md`).

## Rule

Do not retest `fnd6_dltis` on the `event-magnitude-abs-ts-delta` template
family while `WjGVJ7bN` (or any other debt/tax-flow-anchored member) remains
ACTIVE. If revisited, it needs either (a) a fundamentally different
stabilizer combination than the family's usual leverage/ivaco/drlt/buzz set, or
(b) MARKET neutralization (untested for this specific field — leverage-heavy
templates typically lose significant Sharpe under MARKET per
`leverage-premium.md`, so expect a large fitness cost).
