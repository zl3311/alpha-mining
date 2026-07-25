"""
Check BRAIN alpha details and submission checks.

Usage:
    uv run python3 scripts/brain_check.py --alpha-id ABC123
    uv run python3 scripts/brain_check.py --alpha-ids ABC123 DEF456 GHI789
    uv run python3 scripts/brain_check.py --top 20
    uv run python3 scripts/brain_check.py --top 20 --order="-is.fitness"
"""

import argparse
import asyncio
import json
import sys

import httpx

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "src"))

BRAIN_URL = "https://api.worldquantbrain.com"


async def main():
    from alpha_mining.config import get_settings
    settings = get_settings()

    client = httpx.AsyncClient(base_url=BRAIN_URL, timeout=30.0, follow_redirects=True)
    await client.post("/authentication", auth=(settings.brain_email, settings.brain_password))

    parser = argparse.ArgumentParser(description="Check BRAIN alpha details")
    parser.add_argument("--alpha-id", help="Single alpha ID to check")
    parser.add_argument("--alpha-ids", nargs="+", help="Multiple alpha IDs to check")
    parser.add_argument("--top", type=int, help="List top N alphas from BRAIN by fitness")
    parser.add_argument("--order", default="-is.fitness", help="Sort order for --top (default: -is.fitness)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    alpha_ids = []
    if args.alpha_id:
        alpha_ids = [args.alpha_id]
    elif args.alpha_ids:
        alpha_ids = args.alpha_ids
    elif args.top:
        r = await client.get(f"/users/self/alphas?limit={args.top}&offset=0&order={args.order}")
        data = r.json()
        alpha_ids = [a["id"] for a in data.get("results", [])]
    else:
        parser.print_help()
        await client.aclose()
        return

    results = []
    for aid in alpha_ids:
        r = await client.get(f"/alphas/{aid}")
        d = r.json()
        is_d = d.get("is", {})
        checks = is_d.get("checks", [])
        fails = [c for c in checks if c.get("result") == "FAIL"]
        code = d.get("regular", {}).get("code", "") if isinstance(d.get("regular"), dict) else ""

        info = {
            "alpha_id": aid,
            "grade": d.get("grade", "?"),
            "status": d.get("status", "?"),
            "sharpe": is_d.get("sharpe", 0),
            "fitness": is_d.get("fitness", 0),
            "turnover": is_d.get("turnover", 0),
            "returns": is_d.get("returns", 0),
            "n_fails": len(fails),
            "all_pass": len(fails) == 0,
            "fails": [{
                "name": c["name"],
                "value": c.get("value", ""),
                "limit": c.get("limit", ""),
            } for c in fails],
            "all_checks": [{
                "name": c["name"],
                "result": c.get("result", "?"),
                "value": c.get("value", ""),
                "limit": c.get("limit", ""),
            } for c in checks],
            "expression": code,
            "url": f"https://platform.worldquantbrain.com/alpha/{aid}",
        }
        results.append(info)
        await asyncio.sleep(0.2)

    await client.aclose()

    if args.json:
        print(json.dumps(results, indent=2))
        return

    for info in results:
        marker = " <<< ALL PASS" if info["all_pass"] else ""
        print(
        f"{info['grade']:>12} S={info['sharpe']:>5.2f} F={info['fitness']:>5.2f} "
        f"T={info['turnover']*100:>4.1f}% f={info['n_fails']} "
        f"{info['status']:<12}{marker}  {info['expression'][:60]}"
    )
        if info["fails"]:
            for f in info["fails"]:
                print(f"             FAIL: {f['name']} val={f['value']} lim={f['limit']}")
        print(f"             {info['url']}")


if __name__ == "__main__":
    asyncio.run(main())
