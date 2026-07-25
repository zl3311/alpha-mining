---
field: "fnd6_fatl"
dataset: "fundamental6"
family: "fundamental_capital_intensity"
mechanism: "fundamental_capital_intensity"
status: "active"
coverage: 0.5
standalone_sharpe: null
standalone_fitness: null
best_form: "rank(fnd6_fatl / close)"
in_submitted_book: true
submitted_as: ["np30Odjd"]
note: >
  Used as third factor in top drlt blend (zqOojxeK F=3.00). Increases fitness but also self-corr.
---

# fnd6_fatl

Fixed Assets - Total (Land). Long-term real assets on the balance sheet.

## Mechanism

Total fixed assets relative to price captures asset-heavy firms trading cheaply. Similar mechanism to FATE (PP&E) but broader, including land. In drlt blends, fatl/close as third factor pushes F to 3.00 but increases self-corr (0.669 vs 0.622 with totassets_flag).
