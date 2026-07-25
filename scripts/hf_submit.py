"""
Submit expressions to the HF submission queue server for BRAIN simulation.

Usage:
    uv run python3 scripts/hf_submit.py --expressions "rank(A) + rank(B)" "rank(C)" --priority 5 --tags daily exp005
    uv run python3 scripts/hf_submit.py --expressions "rank(A)" --decay 10 --neutralization MARKET
"""

import argparse
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

HF_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")
HF_API_KEY = os.environ.get("HF_API_KEY", "")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}", "X-API-Key": HF_API_KEY, "Content-Type": "application/json"}

_NO_SERVER_URL = (
    "HF_SERVER_URL is not set. Copy .env.example to .env and point it at your own "
    "deployment of the submission queue server (see server/)."
)


def main():
    if not HF_URL:
        sys.exit(_NO_SERVER_URL)

    parser = argparse.ArgumentParser(description="Submit expressions to HF server")
    parser.add_argument("--expressions", nargs="+", required=True, help="FASTEXPR expressions to simulate")
    parser.add_argument("--priority", type=int, default=5, help="Job priority (default 5)")
    parser.add_argument("--tags", nargs="+", default=[], help="Tags for tracking")
    parser.add_argument("--decay", type=int, default=6, help="Decay setting (default 6)")
    parser.add_argument("--neutralization", default="SUBINDUSTRY", help="Neutralization (default SUBINDUSTRY)")
    parser.add_argument("--universe", default="TOP3000", help="Universe (default TOP3000)")
    args = parser.parse_args()

    config = {
        "region": "USA", "universe": args.universe, "delay": 1,
        "decay": args.decay, "truncation": 0.08, "neutralization": args.neutralization,
    }

    payload = {
        "expressions": args.expressions,
        "priority": args.priority,
        "config": config,
        "tags": args.tags,
    }

    r = httpx.post(f"{HF_URL}/v1/jobs", json=payload, headers=HEADERS, timeout=30.0)
    if r.status_code == 200:
        job_ids = r.json()
        print(f"Submitted {len(job_ids)} jobs at priority {args.priority}")
        print(f"Tags: {args.tags}")
        print(f"Config: decay={args.decay}, neut={args.neutralization}, universe={args.universe}")
    else:
        print(f"ERROR: {r.status_code} -- {r.text[:200]}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
