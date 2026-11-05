"""Check every GitHub link in AWESOME-MARKETING-SKILLS.md against the live API.

Usage (needs the `gh` CLI, authenticated):

    python scripts/check_links.py              # writes research/link-check-<date>.md
    python scripts/check_links.py --quiet      # summary line only

For each distinct owner/repo: stars, last push, days since push, archived or
renamed, 404. For each deep link (tree/ or blob/ path): whether the path still
exists on the default branch. The list's own star figures, when a row has a
Stars column, are diffed against the current count.

The script reports; it does not edit the list. A repo quiet for 180 days or a
dead deep link is a fact for the editor to act on, not a verdict.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "AWESOME-MARKETING-SKILLS.md"
STALE_DAYS = 180


def gh(path: str) -> tuple[int, dict]:
    time.sleep(0.3)
    proc = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8")
    try:
        body = json.loads(proc.stdout) if proc.stdout.strip() else {}
    except json.JSONDecodeError:
        body = {}
    return proc.returncode, body


def parse_stars(cell: str) -> int | None:
    cell = cell.strip().lower().replace(",", "")
    m = re.fullmatch(r"([\d.]+)(k?)", cell)
    if not m:
        return None
    return int(float(m.group(1)) * (1000 if m.group(2) else 1))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    text = SRC.read_text(encoding="utf-8")
    today = dt.date.today()
    urls: list[str] = []
    for u in re.findall(r"github\.com/[^\s)>\]\"'|]+", text):
        u = u.rstrip(".,;")
        if u not in urls:
            urls.append(u)

    listed: dict[str, int] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.search(r"\]\(https://github\.com/([^/\s)]+)/([^/\s)]+)", cells[0]) if cells else None
        if m and len(cells) > 1:
            stars = parse_stars(cells[-1])
            if stars is not None:
                listed[f"{m.group(1)}/{m.group(2)}"] = stars

    repos: dict[str, dict] = {}
    deep: list[tuple[str, str, str]] = []
    for u in urls:
        parts = u.split("/")
        if len(parts) < 3:
            continue
        key = f"{parts[1]}/{parts[2]}"
        repos.setdefault(key, {})
        if len(parts) > 5 and parts[3] in ("tree", "blob"):
            deep.append((u, key, "/".join(parts[5:])))

    rows, dead, stale = [], 0, 0
    for key in repos:
        rc, body = gh(f"repos/{key}")
        if rc != 0 or "stargazers_count" not in body:
            dead += 1
            repos[key] = {"ok": False}
            rows.append(f"| {key} | {listed.get(key, '-')} | - | - | - | 404 or renamed |")
            continue
        pushed = dt.datetime.fromisoformat(body["pushed_at"].replace("Z", "+00:00")).date()
        days = (today - pushed).days
        if body.get("archived") or body.get("disabled"):
            dead += 1
        if days >= STALE_DAYS:
            stale += 1
        cur = body["stargazers_count"]
        delta = (cur - listed[key]) if key in listed else "-"
        flag = "archived" if body.get("archived") else ("quiet" if days >= STALE_DAYS else "")
        repos[key] = {"ok": True, "branch": body["default_branch"]}
        rows.append(f"| {key} | {listed.get(key, '-')} | {cur} | {delta} | {pushed} ({days} d) | {flag} |")

    drows, broken = [], 0
    for u, key, path in deep:
        if not repos[key].get("ok"):
            drows.append(f"| {u} | no (repo) |")
            broken += 1
            continue
        rc, _ = gh(f"repos/{key}/contents/{path}?ref={repos[key]['branch']}")
        if rc != 0:
            broken += 1
        drows.append(f"| {u} | {'yes' if rc == 0 else 'no'} |")

    summary = (
        f"{len(repos)} repos checked, {dead} dead, {stale} quiet for {STALE_DAYS}+ days, "
        f"{broken} of {len(deep)} deep links broken ({today.isoformat()})."
    )
    if args.quiet:
        print(summary)
        return 0

    out = ROOT / "research" / f"link-check-{today.isoformat()}.md"
    out.write_text(
        "\n".join(
            [
                f"# Link check for AWESOME-MARKETING-SKILLS.md ({today.isoformat()})",
                "",
                "| owner/repo | listed stars | current | delta | last push | flag |",
                "| --- | --- | --- | --- | --- | --- |",
                *rows,
                "",
                "| deep link | exists |",
                "| --- | --- |",
                *drows,
                "",
                summary,
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(summary)
    print(f"written: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
