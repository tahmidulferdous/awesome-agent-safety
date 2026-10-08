#!/usr/bin/env python3
"""Weekly arXiv digest for awesome-agent-safety.

Queries the arXiv API for agent-safety keywords, filters to recent papers,
skips IDs already recorded in research/arxiv-seen.txt, prints a Markdown
digest to stdout, and records new IDs as seen. Stdlib only.

Usage: python3 scripts/arxiv_watch.py [--days 14] [--seen FILE]
"""
import argparse
import datetime
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

QUERIES = [
    "agent safety",
    "prompt injection agent",
    "MCP security",
    "A2A protocol security",
    "AI agent guardrail",
    "computer use agent safety",
    "multi-agent security",
]

NS = {"a": "http://www.w3.org/2005/Atom"}


def fetch(query: str, max_results: int = 25):
    phrase = f'all:"{query}"' if " " in query else f"all:{query}"
    params = urllib.parse.urlencode(
        {
            "search_query": phrase,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    req = urllib.request.Request(
        f"https://export.arxiv.org/api/query?{params}",
        headers={"User-Agent": "awesome-agent-safety-arxiv-watch/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return ET.fromstring(resp.read())


def parse(feed):
    out = []
    for entry in feed.findall("a:entry", NS):
        id_url = entry.findtext("a:id", "", NS).strip()
        arxiv_id = id_url.rsplit("/abs/", 1)[-1].split("v")[0]
        title = " ".join(entry.findtext("a:title", "", NS).split())
        published = entry.findtext("a:published", "", NS)[:10]
        out.append((arxiv_id, title, published, id_url))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--seen", default="research/arxiv-seen.txt")
    args = ap.parse_args()

    cutoff = datetime.date.today() - datetime.timedelta(days=args.days)
    try:
        with open(args.seen) as f:
            seen = {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        seen = set()

    fresh = {}
    for q in QUERIES:
        try:
            for arxiv_id, title, published, url in parse(fetch(q)):
                if published >= cutoff.isoformat() and arxiv_id not in seen:
                    fresh.setdefault(arxiv_id, (title, published, url, q))
        except Exception as e:  # one bad query must not kill the digest
            print(f"<!-- query failed: {q}: {e} -->", file=sys.stderr)

    if not fresh:
        print("No new agent-safety papers in window.")
        return 0

    print("## New arXiv papers to review\n")
    for arxiv_id in sorted(fresh, key=lambda i: fresh[i][1], reverse=True):
        title, published, url, q = fresh[arxiv_id]
        print(f"- [{title}]({url}) ({published}, via `{q}`)")

    with open(args.seen, "a") as f:
        for arxiv_id in sorted(fresh):
            f.write(arxiv_id + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
