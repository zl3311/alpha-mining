---
field: "anl4_fcf_flag"
dataset: "analyst4"
family: "analyst_revision_densifier"
discovery_session: "20260718-001"
best_sharpe: 1.91
best_fitness: 2.02
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
best_alpha_id: "xAd6K9Np"
mechanism: "Free-cash-flow revision/new-estimate flag used as sub-universe densifier and fresh stabilizer, not as a standalone revision alpha"
status: "active"
---

# Factor: anl4_fcf_flag

## Economic Mechanism

Analyst4 FCF forecast-type flag. In this session it is used in raw `rank()` form
as a coverage densifier / orthogonal stabilizer within an event-magnitude blend
(same role as `anl4_gric_flag` in `YP0bLdzA` and `anl4_cff_flag` in `lelNqEZl`),
not as a primary revision signal.

## Best Known Expression

See `xAd6K9Np` / `fn_accrued_liab_curr_q` — first book use of this flag.

## Lessons

- Effective as the single fresh leg swap to break self-corr within the saturated
  event-magnitude template family (`event-magnitude-fresh-stabilizer` pattern).
- Product form `rank(event) * rank(anl4_fcf_flag)` underperformed additive form
  (AVERAGE F=1.46, corr FAIL) in session 20260718-001.
