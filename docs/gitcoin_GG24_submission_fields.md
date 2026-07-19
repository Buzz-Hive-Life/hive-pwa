# 🐝 Gitcoin GG24 — Submission Field-Fill (copy-paste ready)

> Buzz HiveLife 🐝 (CLO, Hive Life Haven Inc.) — 2026-07-19
> Round: **GG24 → Public Goods R&D → "Public Goods Tooling Development"** (or "AI For Public Goods")
> Paste these into the Gitcoin project-profile / application form. Keep it plain — Gitcoin's human reviewers + algo favor clarity + proof over fluff.

---

## 1. Project Name
**Buzz HiveLife — AI Assistant for Housing Cooperatives (+ The Honey Forager)**

## 2. One-liner (≤ 140 chars — used in cards)
Open AI assistant that helps housing-coop members + autonomously recovers unclaimed public value (grants/rebates) into affordable housing.

## 3. Project Description (long)
Hive Life Haven Inc. is a federal Canadian non-profit building regenerative, member-driven
affordable-housing cooperatives. **Buzz HiveLife** is our open member-facing AI assistant,
and **The Honey Forager** is its flagship open-source subsystem: an agentic engine that scans
public funding sources (grants, RetroPGF rounds, rebates), drafts applications from *verified*
corporate facts, and routes recovered value to our housing mission. It is kill-switch-gated and
fully logged — safe, auditable, and open under Apache-2.0. We pair day-to-day member service
with autonomous public-goods value recovery, keeping 100% of revenue in the mission.

## 4. Category / Domain
Public Goods Tooling Development  ·  AI For Public Goods

## 5. Repository (REQUIRED — must be public)
https://github.com/Buzz-Hive-Life/hive-pwa
- License: Apache-2.0
- Contains: the Hive App PWA (Next.js) + `forager/` open-source engine
- Verified public: yes (clonable without auth)

## 6. Live Demo / Website
- App: https://hive-pwa-production.up.railway.app/
- Landing: https://hivelife.ca

## 7. Team
- **Hive Life Haven Inc.** — federal NFP (Canada Not-for-profit Corporations Act), Active.
- Directors: Stefanie Landry, Randall Broad.
- Agentic division: Buzz HiveLife (Chief AI), Astro-Bee (CTO/AI).
- CorpCan: 1661181-8  ·  BN: 789588365RC0001

## 8. What problem are you solving?
Non-profits + communities leave enormous public value unclaimed (expired grants, unredeemed
rebates, lapsed public-goods funding). Human bandwidth can't track it, while affordable housing
— a core public good — is starved of capital. Members also lack a coherent interface to their
cooperative's services.

## 9. How does it work? (technical)
- Web app: Next.js PWA (React), hosted on Railway, PWA-installable.
- Assistant: agentic (Hermes-core).
- Forager: Python modules (`forager_digest.py`, `tracking_ledger.py`, `retropgf_submitter.py`,
  `adapters/boc_claim_packet.py`) — harvests opportunities, drafts claim packets, logs human
  approvals. No funds are ever moved by the bot (YOLO_ARMED kill-switch).

## 10. Proof of work (Gitcoin weights this HEAVILY)
- ✅ Live, deployed app (Railway URL above — not a mockup).
- ✅ Public, licensed source repo with real, runnable code (not a placeholder).
- ✅ Verified corporate registration (CorpCan #1661181-8, BN on record).
- ✅ Working modules: discovery → ledger → digest → RetroPGF submitter (committed, lint-clean).
- ✅ Honest impact disclosure: ~$670 of *potential* value identified; $0 collected yet by
  design (human-gated, safe).
- ✅ Open under Apache-2.0 — anyone can fork + audit.

## 11. Impact / Public Good delivered
- Affordable-housing cooperative infrastructure (target: 55.5% non-market housing by 2055).
- Open agentic tooling anyone can reuse to recover overlooked community value.
- Member empowerment for an underserved community (housing-coop members).

## 12. What will the funds be used for?
1. Finish open-sourcing + hardening The Honey Forager (so the public can fork it).
2. Seed the first regenerative housing-cooperative unit.
3. Maintain the public-goods tooling (compute, hosting, audits).

## 13. Social / Contact
- Org: Hive Life Haven Inc. (Canada)
- Email: buzz@hivelife.ca

---

## ⚠️ Pre-submit checklist (Buzz flags — human steps only Randy can do)
- [x] Public repo (hive-pwa) + Apache-2.0 license — DONE
- [ ] **Gitcoin Passport** verified on Randy's account (grants.gitcoin.co → Passport)
- [ ] **Wallet** connected at grants.gitcoin.co
- [ ] Randy pastes this into the form + clicks **Submit** (with human attestation)

## Apply link
https://grants.gitcoin.co/ → Create Project Profile → Apply to Public Goods R&D domain round.

---
*Draft uses only verified corporate facts. Randy attests + submits via his human Gitcoin session.*
*Buzz does not move funds or impersonate the corp on-platform.*
