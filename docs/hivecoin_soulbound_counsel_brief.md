# 🪙 HiveCoin — Soulbound Token: Counsel Review Brief
### DRAFT FOR CANADIAN COUNSEL — NOT DEPLOYED, NOT AUTHORIZED FOR ISSUANCE
Prepared by Buzz HiveLife (CLO), Hive Life Haven Inc. · 2026-07-19
Authorization trail: Randy (1) "scope it" → (2) "go ahead with both A and B."
- **A** = minimal Ethereum attestation hook (`forager/hive_attest.py`) — BUILT, not deployed.
- **B** = THIS brief: soulbound HiveCoin spec for counsel review. No token will be issued
  without (1) Randy's explicit go, (2) a Hive Life Haven Inc. director resolution, and
  (3) Canadian counsel sign-off.

---

## 1. What HiveCoin is proposed to be (minimal soulbound design)
- **Non-transferable (soulbound) attestation token** — NOT a tradeable coin.
- Represents a *verified public-goods recovery milestone* (e.g. "$X recovered for co-op Y").
- Standard: **ERC-721 soulbound** (transfer/sell functions overridden to revert) on an
  Ethereum L2 (Base Sepolia testnet first → Base mainnet only after clearance).
- **NO** pre-sale, **NO** ICO, **NO** liquidity, **NO** promise or expectation of profit.
- Distinct from hook A: A anchors the ledger *hash* on-chain (no token); B adds a
  human-meaningful soulbound NFT per milestone for provenance.

## 2. Why soulbound (regulatory logic)
- Transferability + profit expectation = securities exposure (CSA NI 45-106 / Staff Notice 46-307).
- Soulbound removes the "investment contract / expectation-of-profit" vector.
- Soulbound is **not a guaranteed exemption** — counsel must confirm.

## 3. Regulatory map (Canada) — questions for counsel
| Body | Question |
|---|---|
| **CSA** (NI 45-106) | Is a soulbound attestation token a security? Does Staff Notice 46-307 apply? |
| **FINTRAC** | Does issuing/redeeming soulbound tokens trigger MSB registration? (Likely no if non-exchangeable — confirm.) |
| **CRA** | Tax treatment of issuance, holder reporting, donations-in-token. |
| **CorpCan #1661181-8** | Director resolution to issue; our Articles are BROAD (AI/robotics/poverty relief/community benefit) → likely within purpose, but confirm. |
| **Province of NB** (Riverview) | Any co-op / NFP token-specific filings. |

## 4. Technical spec (minimal)
- ERC-721 with soulbound (revert on transferFrom/approve).
- Chain: Base Sepolia (testnet) → Base mainnet post-clearance.
- Mint trigger: `hive_attest.py` ledger milestone → off-chain signer mints soulbound NFT
  to member/co-op address. No treasury, no raise, no token economics beyond attestation.

## 5. Governance
- **Hive member vote required** before any mainnet issuance (our model: every member is a
  board member — decentralized governance).
- Director resolution at Hive Life Haven Inc.

## 6. What we need counsel to confirm
- [ ] Soulbound design falls outside securities regulation.
- [ ] No FINTRAC registration triggered.
- [ ] CRA treatment acceptable.
- [ ] Corporate authority to issue (provide resolution template).
- [ ] Any provincial (NB) filings.

## 7. Recommended phasing
- **Phase 0 (now):** brief to counsel — no code deploy.
- **Phase 1:** testnet soulbound after counsel green-light.
- **Phase 2:** mainnet + member governance vote.
- **NEVER:** tradeable coin / ICO / pre-sale / liquidity.

## 8. Relationship to Gitcoin GG24
- The attestation hook (**A**) already satisfies Gitcoin's *"Ethereum infrastructure focus"*
  **honestly** (real on-chain attestation of public-good ledger).
- HiveCoin (**B**) is a **separate, longer-term track** — NOT required for Gitcoin eligibility.
- If counsel clears soulbound, it *further* strengthens the Ethereum-infra story.

## 9. Governance context — Hypha.Earth (RAISED BY RANDY, pending verification)
Randy noted Hive Life Haven has felt aligned with **Hypha.Earth** as a DAO we might join.
- Reported: Hypha is a cooperative/DAO operating framework built on **Holochain** (agent-centric,
  NOT Ethereum).
- Implication if confirmed: joining/using Hypha does **NOT** satisfy Gitcoin's Ethereum-infra
  criterion (different tech stack) — but it may be a *stronger* structural fit for the
  cooperative-governance dream and could open regenerative/DAO-ecosystem funding.
- Proposed reconciliation: Hypha = cooperative-governance layer (optional future); the
  attestation hook (A) = the Ethereum-infra proof Gitcoin wants; HiveCoin (B) = optional
  soulbound provenance track. They are complementary, not mutually exclusive.
- **Action:** verify Hypha's stack + governance model; assess whether membership conflicts
  with our federal NFP status. Separate strategy note to follow if Randy wants.

---
*Buzz HiveLife 🐝 — protecting the Hive first. This brief is advisory; no on-chain action
taken. Dream deferred ≠ dream abandoned.* 🐝
