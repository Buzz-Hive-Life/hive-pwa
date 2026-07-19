# 🪙 HiveCoin — Design Proposal (ADVISORY, NOT YET BUILT)
### Prepared by Buzz HiveLife (CLO) · 2026-07-19 · Randy authorization: "scope it"

> ⚠️ **STATUS: PROPOSAL ONLY.** No token will be deployed without (1) Randy's explicit
> go, (2) a director resolution at Hive Life Haven Inc., and (3) Canadian counsel sign-off
> on securities/FINTRAC/CRA treatment. This doc is the *scoping*, not the launch.

---

## Why Randy raised it
"We've dreamed about our own 🍯HiveCoin🪙 for a long time. Maybe it's time."

## The honest framing question
**Is HiveCoin a means to a Gitcoin grant, or a real Hive asset?**
- If it exists *only* to satisfy Gitcoin's "Ethereum infrastructure focus," that's backwards —
  we'd be distorting the Hive around a grant criterion.
- If it has *genuine* Hive utility (member co-op governance, attestation of recovered value,
  community reward for verified public-goods work), THEN building it is sound — and Gitcoin
  alignment becomes a happy side-effect.

## Regulatory reality (Canada) — MUST clear counsel
| Risk | Body | Note |
|---|---|---|
| Securities law | CSA (NI 45-106 / crypto guidance) | A transferable token with expectation of profit = likely a security. Utility/community tokens still scrutinized. |
| AML/KYC | FINTRAC | If HiveCoin is exchangeable for fiat/crypto, we may be a "money services business" → registration. |
| Tax | CRA | Issuance, holder reporting, donation-in-token treatment all need an opinion. |
| Corporate | CorpCan #1661181-8 | Director resolution required to issue any token; may need Articles review. |

## Minimal viable design (if authorized + cleared)
- **Type:** Non-transferable / soulbound attestation token (NOT a tradeable coin) — lowest
  securities risk. Represents *verified public-goods recovery* by a member/co-op.
- **Chain:** Ethereum L2 (e.g. Base) or a public testnet first.
- **Function:** on-chain record that X value was recovered for community Y — the same data
  `hive_attest.py` anchors, but minted as a soulbound NFT per milestone.
- **NO pre-sale, NO ICO, NO promise of profit.** Pure provenance/attestation.

## Recommendation (Buzz → Randy + counsel)
1. **Do NOT launch a tradeable HiveCoin now.** Regulatory exposure >> grant benefit.
2. **Adopt the attestation hook (`hive_attest.py`) as the Gitcoin-aligned infrastructure.**
   It satisfies "Ethereum infrastructure focus" *honestly* with near-zero legal risk.
3. **Keep HiveCoin as a future-design track** — revisit only after counsel clears a
   soulbound/utility model AND the Hive votes on it. Dream deferred ≠ dream abandoned. 🐝

## Next step for Randy
Reply: (a) "attestation hook only, no token" (my rec), or
(b) "draft the soulbound HiveCoin spec for counsel review" (I write the legal-ready brief).
