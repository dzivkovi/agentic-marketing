"""Check every GitHub link in AWESOME-MARKETING-SKILLS.md against the live API.

Usage (needs the `gh` CLI, authenticated):

    python scripts/check_links.py              # writes research/link-check-<date>.md
    python scripts/check_links.py --quiet      # summary line only

For each distinct owner/repo: stars, last push, days since push, archived,
disabled, private, renamed (the API follows the redirect, so the returned
full_name is compared with the link), or 404. For each deep link (a tree/ or
blob/ path) the path is checked on the ref the link names (branch or commit),
not on the default branch. When a table cell ends with "<n>k stars" or
"<n> stars", the figure is diffed against the current count.

Failures that are not about the repository (a rate limit, an expired `gh`
login, no network) abort the run instead of marking every repo dead.

The script reports; it does not edit the list. A repo quiet for 180 days or a
dead deep link is a fact for the editor to act on, not a verdict. Exit code 1
when anything is dead or broken, so a release step can gate on it.
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
NOT_REPOS = {"orgs", "topics", "sponsors", "apps", "marketplace", "features", "settings", "login", "search"}


class ApiAbort(RuntimeError):
    pass


def gh(path: str) -> tuple[int | None, dict]:
    """Return (http_status, body). Raises ApiAbort on auth, rate-limit or network failures."""
    time.sleep(0.3)
    proc = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8")
    try:
        body = json.loads(proc.stdout) if proc.stdout.strip() else {}
    except json.JSONDecodeError:
        body = {}
    if proc.returncode == 0:
        return 200, body
    err = proc.stderr or ""
    m = re.search(r"HTTP (\d{3})", err)
    status = int(m.group(1)) if m else None
    if status in (401, 403, 429) or status is None:
        raise ApiAbort(f"gh api {path} failed ({'HTTP ' + str(status) if status else 'no HTTP status'}): {err.strip()[:200]}")
    return status, body


def parse_stars(cell: str) -> int | None:
    m = re.search(r"(?<![\w.])([\d][\d,]*(?:\.\d+)?)(k?)\s+stars\b", cell, flags=re.I)
    if not m:
        return None
    num = float(m.group(1).replace(",", ""))
    return int(num * (1000 if m.group(2).lower() == "k" else 1))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    text = SRC.read_text(encoding="utf-8")
    today = dt.date.today()

    urls: list[str] = []
    for u in re.findall(r"github\.com/[^\s)>\]\"'|]+", text):
        u = u.split("#")[0].split("?")[0].rstrip(".,;/")
        if u not in urls:
            urls.append(u)

    # stars the page states for a repo, read from the row whose first cell links it
    listed: dict[str, int] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        m = re.search(r"\]\(https://github\.com/([^/\s)]+)/([^/\s)]+)", cells[0])
        if not m:
            continue
        stars = parse_stars(cells[-1]) or parse_stars(line)
        if stars is not None:
            listed[f"{m.group(1)}/{m.group(2)}"] = stars

    repos: dict[str, dict] = {}
    deep: list[tuple[str, str, str, str]] = []
    for u in urls:
        parts = u.split("/")
        if len(parts) < 3 or parts[1] in NOT_REPOS:
            continue
        key = f"{parts[1]}/{parts[2]}"
        repos.setdefault(key, {})
        if len(parts) > 5 and parts[3] in ("tree", "blob"):
            deep.append((u, key, parts[4], "/".join(parts[5:])))

    rows: list[str] = []
    dead = stale = 0
    try:
        for key in repos:
            status, body = gh(f"repos/{key}")
            if status == 404 or "stargazers_count" not in body:
                dead += 1
                repos[key] = {"ok": False}
                rows.append(f"| {key} | {listed.get(key, '-')} | - | - | - | 404 |")
                continue
            flags = []
            full = body.get("full_name", key)
            if full.lower() != key.lower():
                flags.append(f"renamed to {full}")
            if body.get("archived"):
                flags.append("archived")
            if body.get("disabled"):
                flags.append("disabled")
            if body.get("private"):
                flags.append("private (readers get 404)")
            if body.get("archived") or body.get("disabled") or body.get("private"):
                dead += 1
            pushed_raw = body.get("pushed_at")
            if pushed_raw:
                pushed = dt.datetime.fromisoformat(pushed_raw.replace("Z", "+00:00")).date()
                days = (today - pushed).days
                if days >= STALE_DAYS:
                    stale += 1
                    flags.append("quiet")
                pushed_s = f"{pushed} ({days} d)"
            else:
                pushed_s = "never"
                stale += 1
                flags.append("empty")
            cur = body["stargazers_count"]
            delta = (cur - listed[key]) if key in listed else "-"
            repos[key] = {"ok": True, "branch": body["default_branch"]}
            rows.append(f"| {key} | {listed.get(key, '-')} | {cur} | {delta} | {pushed_s} | {', '.join(flags)} |")

        drows: list[str] = []
        broken = 0
        for u, key, ref, path in deep:
            if not repos[key].get("ok"):
                drows.append(f"| {u} | no (repo) |")
                broken += 1
                continue
            status, _ = gh(f"repos/{key}/contents/{path}?ref={ref}")
            ok = status == 200
            if not ok:
                broken += 1
            drows.append(f"| {u} | {'yes' if ok else 'no'} |")
    except ApiAbort as exc:
        print(f"aborted, nothing judged: {exc}", file=sys.stderr)
        return 2

    summary = (
        f"{len(repos)} repos checked, {dead} dead or unreadable, {stale} quiet for {STALE_DAYS}+ days, "
        f"{broken} of {len(deep)} deep links broken ({today.isoformat()})."
    )
    if not args.quiet:
        out = ROOT / "research" / f"link-check-{today.isoformat()}.md"
        out.write_text(
            "\n".join(
                [
                    f"# Link check for AWESOME-MARKETING-SKILLS.md ({today.isoformat()})",
                    "",
                    "| owner/repo | listed stars | current | delta | last push | flags |",
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
        print(f"written: {out.relative_to(ROOT)}")
    print(summary)
    return 1 if (dead or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
