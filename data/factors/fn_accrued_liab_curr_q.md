---
field: "fn_accrued_liab_curr_q"
dataset: "fundamental2"
family: "accrued_liability_event_magnitude"
discovery_session: "20260718-001"
best_sharpe: 1.91
best_fitness: 2.02
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
best_alpha_id: "xAd6K9Np"
mechanism: "Current accrued liability shocks — near-term statutory/contractual obligations that reprice more frequently than total accrued stock"
status: "active"
---

# Factor: fn_accrued_liab_curr_q

## Economic Mechanism

Current accrued liabilities are the near-term portion of statutory and
contractual obligations. Absolute 3-day changes mark recognition and settlement
events. Markets underreact to these accrual shocks within subindustry peers.
Distinct from total accrued (`fn_accrued_liab_q`, ACTIVE as `ZYpjKeKx`).

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

→ `xAd6K9Np` EXCELLENT S=1.91 F=2.02, self-corr PASS 0.6826.

## Lessons

- Do NOT clone the `ZYpjKeKx` recipe (`+ anl4_cfi_flag + anl4_bvps_flag + buzz`)
  onto `_curr` — yields EXCELLENT metrics but self-corr 0.993 FAIL.
- Prefer leverage + ivaco + a *fresh* analyst densifier (here `anl4_fcf_flag`)
  to decorrelate from both the accrued sibling and the broader event-magnitude
  family.
- Standalone profile is INFERIOR (rank_value_norm S~1.11); signal appears in
  the event-magnitude transform + multi-factor blend.
