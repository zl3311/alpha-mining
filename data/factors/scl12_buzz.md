---
field: "scl12_buzz"
dataset: "socialmedia12"
family: "sentiment_reversal"
mechanism: "sentiment_reversal"
status: "active"
coverage: 1.0
standalone_sharpe: 1.63
standalone_fitness: 0.65
best_form: "rank(ts_mean(scl12_buzz, 5) * (-1 * returns))"
in_submitted_book: True
submitted_as: ["vR56vdYd", "MPbgqZ7o", "omnopQ9k", "xAR9Ybjp", "np30Odjd"]
note: "Critical stabilizer -- always include for SUB_UNIVERSE consistency"
---

# scl12_buzz

Sentiment volume * reversal. 100% coverage stabilizer for SUB_UNIVERSE check.

## Mechanism

Social media buzz volume acts as a contrarian indicator when combined with returns. High buzz + negative returns = retail overreaction that reverts. 100% coverage makes it the universal stabilizer for SUB_UNIVERSE consistency.
