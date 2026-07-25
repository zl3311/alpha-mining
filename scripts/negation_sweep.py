"""
Design and generate the negation sweep submission batch.

Reads the factor inventory analysis, selects negation candidates above threshold,
generates properly formatted expressions for HF submission, and outputs the batch
as both a JSON file (for programmatic submission) and a summary report.

Usage:
    uv run python3 scripts/negation_sweep.py
    uv run python3 scripts/negation_sweep.py --threshold 1.0
    uv run python3 scripts/negation_sweep.py --submit  # Actually submit to HF
"""

import argparse
import csv
import json
import os
from collections import defaultdict
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
SWEEP_CSV = ROOT / "local" / "sweep_analysis" / "sweep_data.csv"

HF_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")
HF_TOKEN = os.environ.get("HF_TOKEN", "")
HF_API_KEY = os.environ.get("HF_API_KEY", "")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}", "X-API-Key": HF_API_KEY}

DEAD_ZONE_DATASETS = {"news12", "news18", "model16", "model51", "option9"}
PV_REVERSAL_FIELDS = {
    "returns", "close", "open", "high", "low", "vwap", "volume", "cap",
    "adv5", "adv10", "adv15", "adv20", "adv60", "adv120", "adv180",
    "sharesout", "split", "dividend",
}


def is_dead_zone(field: str, dataset: str) -> bool:
    if dataset in DEAD_ZONE_DATASETS:
        return True
    if field in PV_REVERSAL_FIELDS and dataset == "pv1":
        return True
    return False


def load_sweep_negatives(threshold: float) -> list[dict]:
    """Load sweep data and find negation candidates from rank_level/rank_value_norm/rank_delta."""
    with open(SWEEP_CSV) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    candidates = defaultdict(lambda: {
        "best_neg_sharpe": 0,
        "details": [],
        "dataset": "",
    })

    for r in rows:
        field = r["field"]
        if field.startswith("-1"):
            continue
        try:
            sharpe = float(r["sharpe"])
        except (ValueError, TypeError):
            continue
        if sharpe >= 0:
            continue

        neg_sharpe = -sharpe
        if neg_sharpe < threshold:
            continue

        dataset = r["dataset"]
        if is_dead_zone(field, dataset):
            continue

        entry = candidates[field]
        entry["dataset"] = dataset
        if neg_sharpe > entry["best_neg_sharpe"]:
            entry["best_neg_sharpe"] = neg_sharpe
        entry["details"].append({
            "template": r["template"],
            "universe": r["universe"],
            "sharpe": sharpe,
            "neg_sharpe": neg_sharpe,
        })

    return candidates


def generate_submission_batch(candidates: dict, threshold: float) -> list[dict]:
    """Generate HF-submittable expressions for negation candidates.

    For each candidate field, generate ALL 3 basic negated templates (mirroring
    the original sweep's rank_level, rank_value_norm, rank_delta):
      1. rank(-1 * field)
      2. rank(-1 * field / close)
      3. rank(-1 * ts_delta(field, 5))

    Uses the universe where the field showed strongest negative signal.
    """
    batch = []
    seen_expressions = set()

    for field, data in sorted(candidates.items(), key=lambda x: -x[1]["best_neg_sharpe"]):
        dataset = data["dataset"]

        # Determine best universe from the strongest negative result
        best = max(data["details"], key=lambda x: x["neg_sharpe"])
        universe = best["universe"]

        # Generate all 3 negated templates
        templates = [
            (f"rank(-1 * {field})", "neg_rank_level"),
            (f"rank(-1 * {field} / close)", "neg_rank_value_norm"),
            (f"rank(-1 * ts_delta({field}, 5))", "neg_rank_delta"),
        ]

        for expr, template_name in templates:
            if expr in seen_expressions:
                continue
            seen_expressions.add(expr)

            batch.append({
                "expression": expr,
                "field": field,
                "dataset": dataset,
                "template": template_name,
                "universe": universe,
                "inferred_sharpe": data["best_neg_sharpe"],
                "config": {
                    "region": "USA",
                    "universe": universe,
                    "delay": 1,
                    "decay": 6,
                    "truncation": 0.08,
                    "neutralization": "SUBINDUSTRY",
                },
            })

    return batch


def submit_to_hf(batch: list[dict], tag: str = "negation-sweep-v1") -> dict:
    """Submit the batch to HF server."""
    if not HF_URL:
        return {
            "submitted": 0,
            "job_ids": [],
            "errors": [
                "HF_SERVER_URL is not set. Copy .env.example to .env and point it at your "
                "own deployment of the submission queue server (see server/)."
            ],
        }

    # Group by config (universe) to batch submissions
    by_config = defaultdict(list)
    for b in batch:
        key = json.dumps(b["config"], sort_keys=True)
        by_config[key].append(b["expression"])

    results = {"submitted": 0, "errors": [], "job_ids": []}

    for config_str, exprs in by_config.items():
        config = json.loads(config_str)
        # Submit in chunks of 50 to avoid payload limits
        for i in range(0, len(exprs), 50):
            chunk = exprs[i:i + 50]
            payload = {
                "expressions": chunk,
                "priority": 0,
                "config": config,
                "tags": [tag],
            }
            try:
                r = httpx.post(
                    f"{HF_URL}/v1/jobs",
                    json=payload,
                    headers=HEADERS,
                    timeout=30.0,
                )
                if r.status_code == 200:
                    resp = r.json()
                    # API returns a list of job IDs
                    n = len(resp) if isinstance(resp, list) else 0
                    results["submitted"] += n
                    results["job_ids"].extend(resp if isinstance(resp, list) else [])
                    print(f"  Submitted {n} jobs (universe={config['universe']}, chunk {i//50+1})")
                else:
                    results["errors"].append(f"HTTP {r.status_code}: {r.text[:200]}")
                    print(f"  ERROR: HTTP {r.status_code}: {r.text[:100]}")
            except Exception as e:
                results["errors"].append(str(e))
                print(f"  ERROR: {e}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Design negation sweep batch")
    parser.add_argument("--threshold", type=float, default=1.0,
                        help="Minimum inferred negated Sharpe (default 1.0)")
    parser.add_argument("--submit", action="store_true",
                        help="Actually submit to HF server (default: dry run)")
    parser.add_argument("--tag", default="negation-sweep-v1",
                        help="Tag for submitted jobs")
    parser.add_argument("--output", type=str, default=None,
                        help="Output batch JSON (default: local/test_scripts/negation_batch.json)")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else ROOT / "local" / "test_scripts" / "negation_batch.json"

    print(f"Loading negation candidates (threshold={args.threshold})...")
    candidates = load_sweep_negatives(args.threshold)
    print(f"  {len(candidates)} actionable fields with negated Sharpe > {args.threshold}")

    print("\nGenerating submission batch...")
    batch = generate_submission_batch(candidates, args.threshold)
    print(f"  {len(batch)} expressions ready for submission")

    # Summary by dataset
    by_dataset = defaultdict(list)
    for b in batch:
        by_dataset[b["dataset"]].append(b)

    print("\nBatch breakdown by dataset:")
    for ds, items in sorted(by_dataset.items(), key=lambda x: -len(x[1])):
        print(f"  {ds:20s}: {len(items)} expressions")

    print("\nBatch breakdown by universe:")
    by_univ = defaultdict(int)
    for b in batch:
        by_univ[b["universe"]] += 1
    for u, n in sorted(by_univ.items()):
        print(f"  {u}: {n}")

    print(f"\n{'='*80}")
    print("SUBMISSION BATCH (top 20 by inferred Sharpe)")
    print(f"{'='*80}")
    print(f"{'#':>3s} {'Expression':65s} {'Univ':8s} {'InfS':>5s} {'Dataset':12s}")
    print("-" * 100)
    for i, b in enumerate(batch[:20], 1):
        print(f"{i:>3d} {b['expression']:65s} {b['universe']:8s} "
              f"{b['inferred_sharpe']:>5.2f} {b['dataset']:12s}")
    if len(batch) > 20:
        print(f"  ... and {len(batch) - 20} more")

    # Estimated sim budget
    print(f"\n{'='*80}")
    print(f"BUDGET ESTIMATE: {len(batch)} simulations")
    print(f"  At ~3 sims/min, estimated time: {len(batch)/3:.0f} minutes ({len(batch)/3/60:.1f} hours)")
    print(f"  Daily budget impact: {len(batch)} / 5000 = {len(batch)/5000*100:.1f}%")
    print(f"{'='*80}")

    # Save batch
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump({
            "tag": args.tag,
            "threshold": args.threshold,
            "total_expressions": len(batch),
            "batch": batch,
        }, f, indent=2)
    print(f"\nBatch saved to {output_path}")

    # Submit if requested
    if args.submit:
        print(f"\nSubmitting {len(batch)} expressions to HF server...")
        results = submit_to_hf(batch, tag=args.tag)
        print(f"\nSubmission complete: {results['submitted']} jobs created")
        if results["errors"]:
            print(f"  Errors: {results['errors']}")
    else:
        print("\nDRY RUN — use --submit to actually submit to HF server")


if __name__ == "__main__":
    main()
