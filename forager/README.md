# 🐝 The Honey Forager

An **open agentic public-goods value-recovery engine** built by Hive Life Haven Inc.
It is a flagship feature of the [Hive App PWA](../README.md) — the member-facing
assistant that helps housing-cooperative members navigate services and recover the
value their community is *owed but never claimed* (grants, rebates, unclaimed
balances, public-goods funding), and routes it back into affordable housing.

## Design principles
- **G1 discipline:** the Forager never contacts third parties without explicit
  human approval. It harvests *pointers to value*, drafts the claim packets, and
  waits for a human officer to review, attest, and send.
- **No funds movement:** submission logic is kill-switch gated (`YOLO_ARMED`) and
  only ever *drafts + logs*. It never touches wallets or moves money.
- **Verified facts only:** corporate references use public Corporations Canada
  records (CorpCan #1661181-8, BN 789588365RC0001).

## Components
| File | Purpose |
|---|---|
| `forager_digest.py` | Renders a prioritized, human-actionable digest from the review queue. |
| `tracking_ledger.py` | Append-only JSONL ledger of human-action state per opportunity. |
| `retropgf_submitter.py` | Kill-switch-gated public-goods funding submitter (drafts + logs). |
| `generate_narrative.py` | Generates the verified submission narrative. |
| `adapters/boc_claim_packet.py` | Draft claim packet for Bank of Canada unclaimed balances. |

## Usage
```bash
cd forager
python3 forager_digest.py        # generate the action digest
python3 tracking_ledger.py       # self-test the ledger
YOLO_ARMED=1 python3 retropgf_submitter.py "Gitcoin GG24"   # log-mode submit (no real POST)
```

## License
Apache-2.0 — see [../LICENSE](../LICENSE).
