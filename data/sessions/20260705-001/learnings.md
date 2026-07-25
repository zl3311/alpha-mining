# Learnings: Session 20260705-001

## What Worked

- **Negation-dominant pv13 fields** (`rel_ret_cust`, `rel_ret_all`) produce strong
  EXCELLENT+ blends with the standard ptpr + gap template.
- **Level negation** (`rank(-1 * field)`) is simpler and can match or beat delta
  negation (`rank(-1 * ts_delta(field, 5))`) on fitness.
- Cross-direction blends are genuinely novel vs the additive book and pass self-corr
  via Sharpe premium.

## What Didn't Work

- **dividend_min_guidance_value**: SPECTACULAR metrics but BRAIN self-corr FAIL.
- **fnd6_intc negated**: Strong single-factor (S=1.32) but only GOOD in blend.
- **Product interaction** on enterprise_value: AVERAGE only (S=1.86).

## Infrastructure Fixes (same session)

- `hf_poll.py`: count `corr_checked` as done (server promotes gate-passers after self-corr).
- `hf_query.py`: generic column output for `--sql` queries.
- Server `brain_client.py`: handle empty body on `/correlations/self` (pushed to HF).
