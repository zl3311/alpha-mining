---
type: "submit-candidate"
alpha_id: "lelNqEZl"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.01
fitness: 2.01
turnover: 0.1104
self_corr_max: 0.5666
neutralization: "SUBINDUSTRY"
decay: 6
family: "fair_val_assets_event_magnitude_leverage_blend"
session: "20260715-001"
brain_url: "https://platform.worldquantbrain.com/alpha/lelNqEZl"
queued: "2026-07-15"
---

# Submit lelNqEZl (Fair-Value-Asset Event-Magnitude + Leverage + Financing-Cashflow-Revision + Investing-Activities + Deferred-Revenue Blend)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_cff_flag) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Why submittable

- **All 8 BRAIN checks PASS, including SELF_CORRELATION, confirmed
  AUTHORITATIVELY via BRAIN's `/alphas/lelNqEZl/check` endpoint**:
  `{result: PASS, value: 0.5666, limit: 0.7}`. This is the platform's own
  ground-truth verdict, not an estimate — confirmed stable across 3
  independent polls after an initial ~9-minute async-computation lag.
- Grade EXCELLENT, S=2.01, F=2.01, T=11.04%. SUBINDUSTRY, decay=6.
- Correlates 0.5666 vs `YP0bLdzA` (the closest economic sibling — same
  fair-value-L2 event-magnitude mechanism, opposite balance-sheet side) —
  comfortably below the 0.70 auto-pass threshold, no Sharpe premium needed.
  This is one of the LOWER self-corr finds among the event-magnitude-family
  submissions of the past week (`WjGVJ7bN` 0.71, `YP0bLdzA` 0.67, this one
  0.57).
- Anchor field `fn_assets_fair_val_l2_q` belongs to redundancy cluster #21
  (only 2 members) — genuinely more orthogonal to the book's dominant
  fundamental-value/analyst-revision mega-clusters than any prior anchor used
  in this template family, per `data/knowledge/opportunities/factor-themes-redundancy.md`.
- Uses two fields never in the book before this session: `fn_assets_fair_val_l2_q`
  (fundamental2, Level-2 fair-value assets) and `anl4_cff_flag` (analyst4,
  financing-cashflow revision flag). First use of BOTH `fnd6_drlt` and
  `fnd6_ivaco` together as dual stabilizers in this template family (6-factor
  form), which is what lifted GOOD (F=1.75, single-stabilizer variant) to
  EXCELLENT (F=2.01) without materially raising correlation.

## Caveat (read before submitting)

None outstanding. The authoritative BRAIN self-correlation check has already
been confirmed PASS (see above) — no further verification needed before
submission on this front. (For posterity: the endpoint returned `PENDING`
for the first ~9 minutes after simulation completed, consistent with the
known async-computation lag documented in session 20260711-001, before
resolving to the stable 0.5666 PASS value reported here.)

## Related, NOT submittable this session

`blqKkP2l` — the genuinely novel `ts_arg_max` recency-of-shock structure on
the same anchor (`rank(-1 * ts_arg_max(abs(ts_delta(fn_assets_fair_val_l2_q / close, 1)), 20)) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`)
reached SPECTACULAR-adjacent EXCELLENT (S=2.55, F=2.03). Its authoritative
BRAIN `/check` SELF_CORRELATION status is `ERROR` (not PENDING, not PASS/FAIL
— a distinct, unresolved state as of this session), so its true verdict is
unknown; the local PnL pre-submission estimate was 0.701 vs `YP0bLdzA` (just
over threshold, Sharpe 2.55 falling 0.002 short of the 1.10x=2.552 premium
escape). Not queued. Worth a fresh `/check` poll in a future session to see
if `ERROR` resolves to a real value, or one more decorrelation lever (e.g.,
swap `ivaco`→a fresh field) if it resolves to FAIL.

## Reviewer action

**Done.** Submitted 2026-07-15; confirmed ACTIVE on BRAIN (all 7 remaining
checks PASS; submission itself reported self-correlation PASS at 0.5666).
`data/book/lelNqEZl.md` flipped to `status: ACTIVE`.
