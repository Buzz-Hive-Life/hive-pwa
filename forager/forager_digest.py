"""
Honey Forager — Action Digest generator (Buzz-verified canonical)
Reads the G1 review queue (queue.jsonl) and renders a prioritized,
human-actionable digest. For J2 (unclaimed-balance / own-name) items,
appends a pointer to the pre-built BoC claim packet.

This is OUTBOUND-FROM-THE-HIVE (our own digest to our founder) — NOT
foraging outreach. G1 discipline: the Forager never contacts third parties.
"""
import os
import json
from datetime import datetime, timezone

REVIEW_DIR = os.path.join(os.path.dirname(__file__), "forager_review")
QUEUE = os.path.join(REVIEW_DIR, "queue.jsonl")
DIGEST = os.path.join(REVIEW_DIR, "forager_digest.md")

try:
    from tracking_ledger import latest, summary as ledger_summary
except ImportError:
    latest = None
    ledger_summary = None

STATUS_ICON = {
    "pending": "⏳",
    "applied": "📝",
    "submitted": "📤",
    "won": "💰",
    "rejected": "🚫",
    "stale": "🥀",
}


def load_queue():
    if not os.path.exists(QUEUE):
        return []
    items = []
    with open(QUEUE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return items


def _fmt_amount(amount):
    if isinstance(amount, (int, float)):
        return f" — **${amount:,.0f}**"
    return ""


def render(items):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = [
        "# 🐝 Honey Forager — Action Digest",
        "",
        f"_Generated {now}_",
        "",
    ]

    # Merge ledger state over queue defaults
    for it in items:
        jar = it.get("jar", "J?")
        title = it.get("title") or it.get("source") or "untitled"
        if latest:
            rec = latest(jar, title)
            if rec:
                it["status"] = rec.get("status", it.get("status", "pending"))

    if not items:
        out.append("No items in the review queue. The Forager is harvesting — check back next run. 🐝")
        return "\n".join(out)

    counts = ledger_summary() if ledger_summary else {}
    if not counts:
        for it in items:
            s = it.get("status", "pending")
            counts[s] = counts.get(s, 0) + 1
    out.append(
        "**Status summary:** "
        + " · ".join(f"{STATUS_ICON.get(s, '❓')} {s}: {c}" for s, c in sorted(counts.items()))
    )
    out.append("")

    jars = {}
    for it in items:
        jars.setdefault(it.get("jar", "J?"), []).append(it)

    for jar in sorted(jars):
        out.append(f"## {jar}")
        for it in jars[jar]:
            s = it.get("status", "pending")
            icon = STATUS_ICON.get(s, "❓")
            title = it.get("title") or it.get("source") or "untitled"
            amt = _fmt_amount(it.get("amount"))
            out.append(f"- {icon} **{title}**{amt}")
            out.append(f"  - _why:_ {it.get('why', '')}")
            notes = []
            if it.get("needs_outreach"):
                notes.append("⚠️ outbound — human approval required before contact")
            if jar == "J2" and s in ("pending", "applied"):
                notes.append("📋 claim packet ready → review `forager_review/boc_claim_draft.md`")
            if notes:
                out.append("  - " + " · ".join(notes))
        out.append("")

    out.append("---")
    out.append("_G1 discipline: the Forager never contacts third parties without human approval. You review, you claim._ 🐝")
    return "\n".join(out)


def main():
    items = load_queue()
    md = render(items)
    os.makedirs(REVIEW_DIR, exist_ok=True)
    with open(DIGEST, "w", encoding="utf-8") as f:
        f.write(md)
    print(md)
    return md


if __name__ == "__main__":
    main()
