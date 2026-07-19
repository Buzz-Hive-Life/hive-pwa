"""
Honey Forager — Tracking Ledger (Buzz-verified canonical)
Records the human-action state of each harvested opportunity so the digest can
show real progress (⏳ awaiting → 📝 applied → 📤 submitted → 💰 won | 🚫 rejected | 🥀 stale).

Simple append-only JSONL keyed by a stable item_id (slug of jar+title). The latest
entry per item_id wins. No external calls. G1-safe: this only records human actions.
"""
import os
import json
import re
from datetime import datetime, timezone

REVIEW_DIR = os.path.join(os.path.dirname(__file__), "forager_review")
LEDGER = os.path.join(REVIEW_DIR, "ledger.jsonl")

VALID = {"pending", "applied", "submitted", "won", "rejected", "stale"}


def _slug(text):
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "item"


def item_id(jar, title):
    return _slug(f"{jar}-{title}")


def _now():
    return datetime.now(timezone.utc).isoformat()


def mark(jar, title, status, note=""):
    if status not in VALID:
        raise ValueError(f"status must be one of {sorted(VALID)}; got {status!r}")
    os.makedirs(REVIEW_DIR, exist_ok=True)
    entry = {"item_id": item_id(jar, title), "status": status, "note": note, "ts": _now()}
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def latest(jar=None, title=None, id=None):
    key = id or (item_id(jar, title) if jar and title else None)
    if not key:
        return None
    cur = None
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if e.get("item_id") == key:
                    cur = e
    return cur


def summary():
    states = {}
    if os.path.exists(LEDGER):
        seen = {}
        with open(LEDGER, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                seen[e["item_id"]] = e["status"]
        for s in seen.values():
            states[s] = states.get(s, 0) + 1
    return states


if __name__ == "__main__":
    # self-test
    mark("J2", "Bank of Canada Unclaimed Balance — Hive Life Haven Inc.", "applied", "packet reviewed, sending")
    print("latest:", latest("J2", "Bank of Canada Unclaimed Balance — Hive Life Haven Inc."))
    print("summary:", summary())
