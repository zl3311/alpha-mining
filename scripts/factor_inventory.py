"""
Systematic factor inventory analysis.

Parses the sweep_data.csv to build a full coverage matrix (field x direction x template x universe),
identifies negation candidates (fields whose negated version would have positive Sharpe > threshold),
cross-references with dead zones, and outputs actionable results.

Usage:
    uv run python3 scripts/factor_inventory.py
    uv run python3 scripts/factor_inventory.py --threshold 1.0
    uv run python3 scripts/factor_inventory.py --output local/test_scripts/factor_inventory.json
"""

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SWEEP_CSV = ROOT / "local" / "sweep_analysis" / "sweep_data.csv"
PROFILES_DIR = ROOT / "data" / "knowledge" / "factor_profiles"

DEAD_ZONE_DATASETS = {"news12", "news18", "model16", "model51", "option9"}

PV_REVERSAL_FIELDS = {
    "returns", "close", "open", "high", "low", "vwap", "volume", "cap",
    "adv5", "adv10", "adv15", "adv20", "adv60", "adv120", "adv180",
    "sharesout", "split", "dividend",
}


def load_sweep_data() -> list[dict]:
    """Load and parse sweep_data.csv."""
    with open(SWEEP_CSV) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    for r in rows:
        try:
            r["sharpe"] = float(r["sharpe"]) if r["sharpe"] else 0.0
        except ValueError:
            r["sharpe"] = 0.0
        try:
            r["fitness"] = float(r["fitness"]) if r["fitness"] else 0.0
        except ValueError:
            r["fitness"] = 0.0
        try:
            r["turnover"] = float(r["turnover"]) if r["turnover"] else 0.0
        except ValueError:
            r["turnover"] = 0.0
    return rows


def is_dead_zone(field: str, dataset: str) -> tuple[bool, str]:
    """Check if a field is in a dead zone. Returns (is_dead, reason)."""
    if dataset in DEAD_ZONE_DATASETS:
        return True, f"dataset_{dataset}_dead"
    if field in PV_REVERSAL_FIELDS and dataset == "pv1":
        return True, "family_pv_reversal_saturated"
    return False, ""


def detect_direction(expression: str, field: str) -> str:
    """Detect whether an expression tests positive or negated direction."""
    if not expression:
        return "positive"
    if f"-1 * {field}" in expression or f"-1*{field}" in expression:
        return "negated"
    if f"-1 * ts_delta({field}" in expression or f"-1*ts_delta({field}" in expression:
        return "negated_delta"
    if expression.startswith("-rank(") or expression.startswith("-1 * rank("):
        return "negated"
    return "positive"


def build_coverage_matrix(rows: list[dict]) -> dict:
    """Build field x direction x template x universe coverage matrix.

    Returns dict keyed by field, with nested dicts for each dimension.
    """
    matrix = defaultdict(lambda: {
        "dataset": "",
        "directions_tested": set(),
        "templates": defaultdict(lambda: defaultdict(dict)),
        "best_sharpe_positive": None,
        "best_sharpe_any": None,
        "worst_sharpe": None,
        "best_negated_sharpe": None,
        "n_sims": 0,
    })

    for r in rows:
        field = r["field"]
        template = r["template"]
        universe = r["universe"]
        sharpe = r["sharpe"]
        direction = detect_direction(r.get("expression", ""), field)

        entry = matrix[field]
        entry["dataset"] = r["dataset"]
        entry["directions_tested"].add(direction)
        entry["templates"][template][universe] = {
            "sharpe": sharpe,
            "fitness": r["fitness"],
            "grade": r["grade"],
            "direction": direction,
        }
        entry["n_sims"] += 1

        if direction == "positive":
            if entry["best_sharpe_positive"] is None or sharpe > entry["best_sharpe_positive"]:
                entry["best_sharpe_positive"] = sharpe
        if entry["best_sharpe_any"] is None or sharpe > entry["best_sharpe_any"]:
            entry["best_sharpe_any"] = sharpe
        if entry["worst_sharpe"] is None or sharpe < entry["worst_sharpe"]:
            entry["worst_sharpe"] = sharpe
        if sharpe < 0:
            neg_s = -sharpe
            if entry["best_negated_sharpe"] is None or neg_s > entry["best_negated_sharpe"]:
                entry["best_negated_sharpe"] = neg_s

    return matrix


def identify_negation_candidates(matrix: dict, threshold: float) -> list[dict]:
    """Find fields where negation would produce Sharpe above threshold.

    For rank_level and rank_value_norm: rank(-1*F) gives -Sharpe(rank(F))
    For rank_delta: rank(-1*ts_delta(F,5)) gives -Sharpe(rank(ts_delta(F,5)))
    """
    candidates = []

    for field, data in matrix.items():
        if data["best_negated_sharpe"] is None:
            continue
        if data["best_negated_sharpe"] < threshold:
            continue

        dead, reason = is_dead_zone(field, data["dataset"])

        best_neg_template = None
        best_neg_universe = None
        best_neg_sharpe = 0

        for template, universes in data["templates"].items():
            for universe, metrics in universes.items():
                if metrics["sharpe"] < 0 and -metrics["sharpe"] > best_neg_sharpe:
                    best_neg_sharpe = -metrics["sharpe"]
                    best_neg_template = template
                    best_neg_universe = universe

        candidates.append({
            "field": field,
            "dataset": data["dataset"],
            "best_negated_sharpe": data["best_negated_sharpe"],
            "best_neg_template": best_neg_template,
            "best_neg_universe": best_neg_universe,
            "best_positive_sharpe": data["best_sharpe_positive"],
            "is_dead_zone": dead,
            "dead_zone_reason": reason,
            "n_sims": data["n_sims"],
            "negation_tested": "negated" in data["directions_tested"],
        })

    candidates.sort(key=lambda x: -x["best_negated_sharpe"])
    return candidates


def identify_untested_from_profiles(matrix: dict) -> list[str]:
    """Find fields that have factor profiles but weren't in the sweep."""
    profiled_fields = set()
    if PROFILES_DIR.exists():
        for p in PROFILES_DIR.glob("*.md"):
            profiled_fields.add(p.stem)

    sweep_fields = set(matrix.keys())
    return sorted(profiled_fields - sweep_fields)


def generate_negation_expressions(candidates: list[dict]) -> list[dict]:
    """Generate expressions to submit for negation testing."""
    expressions = []
    for c in candidates:
        if c["is_dead_zone"]:
            continue
        if c["negation_tested"]:
            continue

        field = c["field"]
        template = c["best_neg_template"]
        universe = c["best_neg_universe"] or "TOP3000"

        # Skip fields that already have negation in the field name (would cause double negation)
        if field.startswith("-1 * ") or field.startswith("-1*"):
            continue

        if template in ("rank_level",):
            expressions.append({
                "expression": f"rank(-1 * {field})",
                "field": field,
                "universe": universe,
                "template": "neg_rank_level",
                "inferred_sharpe": c["best_negated_sharpe"],
                "dataset": c["dataset"],
            })
        elif template in ("rank_value_norm",):
            expressions.append({
                "expression": f"rank(-1 * {field} / close)",
                "field": field,
                "universe": universe,
                "template": "neg_rank_value_norm",
                "inferred_sharpe": c["best_negated_sharpe"],
                "dataset": c["dataset"],
            })
        elif template in ("rank_delta",):
            expressions.append({
                "expression": f"rank(-1 * ts_delta({field}, 5))",
                "field": field,
                "universe": universe,
                "template": "neg_rank_delta",
                "inferred_sharpe": c["best_negated_sharpe"],
                "dataset": c["dataset"],
            })

    return expressions


def main():
    parser = argparse.ArgumentParser(description="Systematic factor inventory analysis")
    parser.add_argument("--threshold", type=float, default=1.25,
                        help="Minimum negated Sharpe to consider (default 1.25)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (default: stdout summary)")
    parser.add_argument("--all-negatives", action="store_true",
                        help="Include all fields with any negative Sharpe (not just above threshold)")
    args = parser.parse_args()

    print("Loading sweep data...")
    rows = load_sweep_data()
    print(f"  {len(rows)} total simulation results")

    print("\nBuilding coverage matrix...")
    matrix = build_coverage_matrix(rows)
    print(f"  {len(matrix)} unique fields tested")

    # Coverage stats
    fields_positive_only = sum(
        1 for d in matrix.values()
        if d["directions_tested"] == {"positive"}
    )
    fields_with_negation = sum(
        1 for d in matrix.values()
        if "negated" in d["directions_tested"] or "negated_delta" in d["directions_tested"]
    )
    print(f"  {fields_positive_only} fields tested positive direction only")
    print(f"  {fields_with_negation} fields with any negation tested")

    # Fields with negative Sharpe (negation candidates)
    fields_with_neg_sharpe = sum(
        1 for d in matrix.values() if d["worst_sharpe"] is not None and d["worst_sharpe"] < 0
    )
    print(f"  {fields_with_neg_sharpe} fields have at least one negative Sharpe result")

    print(f"\nIdentifying negation candidates (threshold={args.threshold})...")
    candidates = identify_negation_candidates(matrix, args.threshold)
    live_candidates = [c for c in candidates if not c["is_dead_zone"]]
    dead_candidates = [c for c in candidates if c["is_dead_zone"]]
    print(f"  {len(candidates)} total fields with negated Sharpe > {args.threshold}")
    print(f"  {len(live_candidates)} ACTIONABLE (not in dead zone)")
    print(f"  {len(dead_candidates)} in dead zones (skipped)")

    print(f"\n{'='*80}")
    print("ACTIONABLE NEGATION CANDIDATES")
    print(f"{'='*80}")
    print(f"{'Field':45s} {'Dataset':15s} {'Template':18s} {'Univ':8s} {'NegS':>6s} {'PosS':>6s} {'Tested':>6s}")
    print("-" * 110)
    for c in live_candidates:
        tested = "YES" if c["negation_tested"] else "NO"
        pos_s = f"{c['best_positive_sharpe']:.2f}" if c['best_positive_sharpe'] is not None else "N/A"
        print(f"{c['field']:45s} {c['dataset']:15s} {c['best_neg_template']:18s} "
              f"{c['best_neg_universe']:8s} {c['best_negated_sharpe']:>6.2f} {pos_s:>6s} {tested:>6s}")

    print(f"\n{'='*80}")
    print("DEAD ZONE CANDIDATES (not actionable)")
    print(f"{'='*80}")
    for c in dead_candidates[:15]:
        print(f"  {c['field']:40s} {c['dataset']:12s} neg_S={c['best_negated_sharpe']:.2f}  "
              f"reason={c['dead_zone_reason']}")

    # Generate submission expressions
    expressions = generate_negation_expressions(live_candidates)
    print(f"\n{'='*80}")
    print(f"NEGATION SWEEP: {len(expressions)} expressions to submit")
    print(f"{'='*80}")
    for e in expressions:
        print(f"  [{e['universe']}] {e['expression'][:70]:70s}  (inferred S={e['inferred_sharpe']:.2f})")

    # Also check: profiled fields not in sweep
    untested_profiled = identify_untested_from_profiles(matrix)
    if untested_profiled:
        print(f"\n{'='*80}")
        print(f"PROFILED FIELDS NOT IN SWEEP DATA: {len(untested_profiled)}")
        print(f"{'='*80}")
        for f in untested_profiled[:20]:
            print(f"  {f}")
        if len(untested_profiled) > 20:
            print(f"  ... and {len(untested_profiled) - 20} more")

    # Output JSON
    if args.output:
        output = {
            "summary": {
                "total_sims": len(rows),
                "unique_fields_tested": len(matrix),
                "fields_positive_only": fields_positive_only,
                "fields_with_negation_tested": fields_with_negation,
                "fields_with_negative_sharpe": fields_with_neg_sharpe,
                "negation_candidates_total": len(candidates),
                "negation_candidates_actionable": len(live_candidates),
                "negation_candidates_dead_zone": len(dead_candidates),
                "expressions_to_submit": len(expressions),
            },
            "actionable_candidates": live_candidates,
            "dead_zone_candidates": dead_candidates,
            "submission_expressions": expressions,
            "untested_profiled_fields": untested_profiled,
        }
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"\nOutput saved to {out_path}")


if __name__ == "__main__":
    main()
