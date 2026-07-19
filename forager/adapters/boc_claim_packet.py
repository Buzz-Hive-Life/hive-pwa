"""
Honey Forager — BoC Unclaimed-Balance Claim Packet Generator (Buzz-verified)
Generates a ready-to-review claim DRAFT for a Bank of Canada unclaimed balance
matched to Hive Life Haven Inc. NO external calls — uses verified corporate facts.

Human reviews, attaches CorpCan proof, and sends. Counsel-gated: this is a draft,
not legal advice.
"""
import os
import json
from datetime import datetime, timezone

REVIEW_DIR = os.path.dirname(__file__) if os.path.basename(os.path.dirname(__file__)) == "forager_review" else os.path.join(os.path.dirname(__file__), "forager_review")
DRAFT = os.path.join(REVIEW_DIR, "boc_claim_draft.md")

# Verified corporate facts (CorpCan #1661181-8, BN 789588365RC0001)
CORP = {
    "legal_name": "Hive Life Haven Inc.",
    "corpcan": "1661181-8",
    "bn": "789588365RC0001",
    "directors": ["Stefanie Landry", "Randall Broad"],
    "status": "Active (federal NFP Act)",
}


def generate(amount=None, source_hint="Bank of Canada unclaimed balances registry"):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    amt = f"${amount:,.0f}" if isinstance(amount, (int, float)) else "(amount to be confirmed from registry search)"
    md = f"""# 🐝 BoC Unclaimed-Balance Claim — DRAFT (pending human review)

**Generated:** {now}
**Status:** `draft_pending_human_review` — NOT sent. Human attaches CorpCan proof + sends.

## Entity (verified)
- **Legal name:** {CORP['legal_name']}
- **Corporations Canada #:** {CORP['corpcan']}
- **Business Number (BN):** {CORP['bn']}
- **Status:** {CORP['status']}
- **Directors:** {', '.join(CORP['directors'])}

## Claim
- **Source:** {source_hint}
- **Indicated amount:** {amt}

## How to file (Bank of Canada unclaimed balances)
1. Confirm the balance at the Bank of Canada unclaimed balances portal using the entity
   legal name / BN above.
2. Gather proof of entity identity: CorpCan certificate (filed Articles, #1661181-8),
   and a director-authorized cover letter.
3. Submit the written claim to the Bank of Canada per their unclaimed-balances process
   (email/secure form — human-initiated, not bot-initiated).
4. Track in the Forager ledger: ⏳ awaiting → 📝 applied → 📤 submitted → 💰 won.

## ⚠️ Counsel gate
This packet is a drafting aid, not legal advice. Before submitting, confirm with counsel
that the claim is consistent with the NFP's purposes (verified broad — Incorp-Constitution,
#1661181-8) and that no third-party solicitation occurs. Crypto (J5) is unrelated and frozen.

_Signed off for sending by: _________________  (human)  Date: _________
"""
    os.makedirs(REVIEW_DIR, exist_ok=True)
    with open(DRAFT, "w", encoding="utf-8") as f:
        f.write(md)
    return DRAFT


if __name__ == "__main__":
    import sys
    amt = None
    if len(sys.argv) > 1:
        try:
            amt = float(sys.argv[1])
        except ValueError:
            pass
    path = generate(amt)
    print("WROTE", path)
    print(open(path, encoding="utf-8").read()[:600])
