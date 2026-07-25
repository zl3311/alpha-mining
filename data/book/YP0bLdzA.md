---
alpha_id: "YP0bLdzA"
name: "fair_val_liab_event_magnitude_leverage_gric_ivaco_buzz"
status: "ACTIVE"
submitted: "2026-07-11"
grade: "EXCELLENT"
sharpe: 2.32
fitness: 2.22
turnover: 0.1066
returns: null
family: "fair_val_liab_event_magnitude_leverage_blend"
mechanism: "Event-magnitude transform on Level-2 fair-value-liability changes, blended with leverage premium, gross-income revision flag, investing-activities-other, and a buzz-reversal stabilizer"
fields:
  - "fn_liab_fair_val_l2_q"
  - "equity"
  - "assets"
  - "anl4_gric_flag"
  - "fnd6_ivaco"
  - "scl12_buzz"
  - "returns"
expression: "ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.673
self_corr_peer: "WjGVJ7bN"
self_corr_result: "PASS (pre-submission local estimate; platform accepted submission, confirming the authoritative gate passed)"
self_corr_method: "local_pnl_correlation_vs_full_active_book_44_entries (pre-submission); platform acceptance (post-submission confirmation)"
self_corr_caveat: "BRAIN's authoritative /alphas/{id}/check and /correlations/self endpoints returned SELF_CORRELATION: PENDING throughout the discovery session (consistently timed out across 6+ polling attempts spanning ~90 minutes, including for already-ACTIVE control alphas). Human submitted 2026-07-11 based on the local-PnL estimate; platform confirms status ACTIVE, all 7 checks PASS post-submission (SELF_CORRELATION is not a re-queryable check once submitted, per platform behavior -- acceptance itself is the confirmation)."
session: "20260711-001"
brain_url: "https://platform.worldquantbrain.com/alpha/YP0bLdzA"
tags:
  - "fn_liab_fair_val_l2_q"
  - "anl4_gric_flag"
  - "event_magnitude"
  - "fair_value_liability"
  - "leverage_premium"
  - "buzz_stabilizer"
  - "session_20260711-001"
---

# YP0bLdzA — Fair-Value-Liability Event-Magnitude + Leverage + Gross-Income-Revision + Investing-Activities Blend

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Mechanism

Five-factor blend extending the proven `event-magnitude-abs-ts-delta` template
(previously validated on `fnd6_itci`, `fnd6_newqv1300_ppegtq`, `fnd6_tlcf`,
`fnd6_txw`) to two genuinely fresh fields never used in any prior book entry or
factor file:

1. **Fair-value-liability event magnitude** (`rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3)))`):
   `fn_liab_fair_val_l2_q` measures Level-2 (model-priced, not quoted-market)
   recurring fair-value liabilities — derivatives, structured notes, and other
   instruments without an observable market price. Large 3-day swings in this
   value relative to price signal a re-marking event (rate/credit-spread shock,
   hedge restructuring, or a valuation-model change) that the market
   underreacts to, independent of the swing's direction.
2. **Leverage premium** (`rank(-1 * equity / assets)`): high-leverage firms earn
   a subindustry risk premium (see pattern `leverage-premium.md`).
3. **Gross-income revision flag** (`rank(anl4_gric_flag)`): analyst4 forecast-type
   flag for gross income (revision/new estimate). Standalone AVERAGE via
   `ts_mean(F,10)` (S=1.31, F=1.28); used here in raw `rank()` form as an
   analyst-conviction densifier. Never used in any prior book entry.
4. **Investing-activities-other** (`rank(fnd6_ivaco / close)`): conglomerate /
   non-core capital-allocation quality — proven `LOW_SUB_UNIVERSE_SHARPE` fix
   from the `product-interaction-blend` and `event-magnitude-abs-ts-delta`
   patterns.
5. **Buzz-reversal stabilizer** (`rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`):
   100%-coverage sentiment-reversal factor; lifts the base 4-factor blend from
   GOOD to EXCELLENT at low correlation cost (per the `event-magnitude-buzz-boost`
   lesson from `WjGVJ7bN`).

## Discovery Path (session 20260711-001)

- Rounds 1-3 (49 sims): tested genuinely novel operator-tree shapes (non-volatility
  `trade_when` gating, cross-dataset ratios, `ts_arg_max`/`ts_arg_min` recency,
  dynamic correlation between non-return series, nonlinear rank-power tilts,
  multi-horizon spreads) on two fresh anchors (`fn_liab_fair_val_l2_q`,
  `anl4_gric_flag`) combined with the standard `open/close-1 + anl4_ptpr_flag`
  overnight-gap catalyst pair. Reached SPECTACULAR/EXCELLENT aggregate metrics
  (best: `RR8Vz96o`, `dltis`-anchored, S=2.37 F=2.54) but **all** such candidates
  showed local PnL correlation 0.74-0.91 vs multiple existing book entries
  (`LLR0n261`, `6Xzm6PQP`, `78w5d35x`, `O0ZOJbaq`) that share the *exact same*
  `open/close-1 + {ptpr_flag|netdebt_flag}` 2-leg skeleton verbatim — confirming
  this skeleton itself (not the anchor field) is the correlation driver,
  regardless of how fresh the third leg is. Recorded as a new dead-zone/rule
  (see `data/knowledge/rules/overnight-gap-flag-skeleton-saturated.md`).
- Round 4 (6 sims): pivoted to the proven `event-magnitude + leverage + ivaco +
  drlt (+ buzz)` template (previously itci/ppegtq/tlcf/txw only) applied to
  `fn_liab_fair_val_l2_q` and `fnd6_dltis`. Both anchors reached SPECTACULAR
  (S=2.45-2.54), but `dltis` correlated 0.94 vs `WjGVJ7bN` (dead end — dltis and
  txw are economically adjacent debt/tax flow items) while `fn_liab_fair_val_l2_q`
  correlated a much lower 0.71 vs the same peer.
- Rounds 5-8 (~20 sims): repaired `LOW_SUB_UNIVERSE_SHARPE` (fails without a
  stabilizer swap) and pushed the `fn_liab_fair_val_l2_q` variant's correlation
  down via stabilizer-leg substitution (`fatl`/`dlto` in place of `drlt`).
  Best of this family (`P03ZkrkW`/`VkPavmgJ`, S=2.16, F=2.33) still hovered at
  0.694-0.696 vs `rKlo39p1` — an uncomfortably thin margin, since `ivaco +
  leverage + buzz` are shared verbatim with `rKlo39p1`/`wpl5eP5v`/`WjGVJ7bN`.
  `trade_when` realized-vol gating was attempted to fix sub-universe and further
  decorrelate (per `volatility-gate-fixes-sub-universe.md`) but failed
  permanently on this expression shape with a BRAIN unit-type error
  (`Incompatible unit for input of "greater"`) across all 4 variants tried —
  not pursued further.
- Round 9 (3 sims): swapped the `drlt` sub-universe-fixer leg for the fresh,
  never-used `anl4_gric_flag` instead of `fatl`/`dlto`. This produced
  **`YP0bLdzA`** — EXCELLENT, S=2.32, F=2.22 (better than any `fatl`/`dlto`
  variant), and crucially a much larger correlation margin (0.673 vs the same
  `WjGVJ7bN` peer, down from 0.694-0.71) because `gric_flag` is not shared by
  any existing member of the event-magnitude-leverage family.

## Self-Correlation

Max local PnL correlation vs the full **44-alpha ACTIVE universe** (39 main-book
+ 5 recently-submitted-but-unmerged): **0.673** vs `WjGVJ7bN` (excise-tax
event-magnitude, S=2.63) — comfortably below the 0.70 auto-pass threshold, no
Sharpe premium needed. Next-highest peers:

| Peer | Corr | Peer Sharpe | Peer Status |
|------|------|-------------|-------------|
| WjGVJ7bN | 0.673 | 2.63 | ACTIVE |
| d5Q3ZmWv | 0.561 | 2.97 | ACTIVE (main book) |
| pw8wNe76 | 0.459 | 2.09 | ACTIVE (main book) |
| MPbgqZ7o | 0.448 | — | ACTIVE (main book) |
| wpl5eP5v | 0.520 | 2.09 | ACTIVE |
| rKlo39p1 | 0.516 | 2.13 | ACTIVE |

**Caveat**: BRAIN's authoritative `/alphas/{id}/check` and `/correlations/self`
endpoints returned `SELF_CORRELATION: PENDING` throughout this session — polling
timed out consistently (10 retries) across 6+ attempts spanning ~90 minutes,
including for control queries against already-ACTIVE alphas (`d5Q3ZmWv`), so
this appears to be a general async-computation lag rather than an issue
specific to this candidate. This local-PnL-based verdict should be re-verified
with a fresh `/check` poll before submission.

## BRAIN Checks

All 7 computable checks PASS (verified via `/alphas/{id}/check`):

| Check | Result | Value | Limit |
|-------|--------|-------|-------|
| LOW_SHARPE | PASS | 2.32 | 1.25 |
| LOW_FITNESS | PASS | 2.22 | 1.00 |
| LOW_TURNOVER | PASS | 0.1066 | 0.01 |
| HIGH_TURNOVER | PASS | 0.1066 | 0.70 |
| CONCENTRATED_WEIGHT | PASS | — | — |
| LOW_SUB_UNIVERSE_SHARPE | PASS | — | — |
| MATCHES_COMPETITION | PASS | — | — |
| SELF_CORRELATION | PENDING (see caveat above; local-PnL estimate 0.673, PASS) | — | 0.70 |

## Post-Submission

Submitted by the human on 2026-07-11 and confirmed **ACTIVE** on the BRAIN
platform (`/alphas/YP0bLdzA/check` returns `status: ACTIVE`, grade EXCELLENT,
S=2.32, F=2.22, all 7 computable checks PASS, including
`LOW_SUB_UNIVERSE_SHARPE` at value=1.22 vs limit=1.0). Post-submission, the
`/check` endpoint no longer lists `SELF_CORRELATION` as a distinct check (the
same behavior observed for `WjGVJ7bN` in session 20260710-001) — the
platform's acceptance of the submission is itself confirmation that the
authoritative self-correlation check passed.
