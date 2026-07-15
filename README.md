# 🐝 HIVE-PWA — Hive App (Hive Life Haven)

The Hive App PWA. Live at `hive-pwa-production.up.railway.app` (Next.js + React, 3D bee/honeycomb splash: *"Welcome home, beautiful soul"*).

This repo is the **HUP-ready home** for the source. Buzz originally deployed it via `railway up` (CLI) last month, so the code was never git-versioned — this scaffold fixes that so we can deploy safely via **repo → Railway** (no in-container hacking).

## Architecture (current)
- **Stack:** Next.js (React), prerendered, `manifest.json` present (PWA-installable), Fredoka/Jost fonts.
- **3D splash:** WebGL bee/honeycomb scene with "TAP TO SKIP" intro.
- **Hosting:** Railway (`RAILPACK` builder), US West, 1 replica.
- **Domain (plan):** currently `*.railway.app`. Eventually CNAME a `hivelife.ca` subdomain (e.g. `haven.hivelife.ca` or `app.hivelife.ca`) → Railway. **NEVER `tidalwhale.ca`** (Stefanie's rule: Hive Life content stays off Tidal Whale's domain).

## Roadmap — "Haven's Journey" MVP (Buzz's Path B)
Extend the existing PWA with an invite-only photo/text feed (the seed for full Hive-Book):
- **Access model:** reuse Hive Chat's `participants` + `role` concept (`owner` / `member` / `observer`). Invite-only.
- **Data model:** `members(role)` · `invites` · `posts(photo+text)` · `comments` · `likes`.
- **UI:** invite-only entry → feed behind the splash, mobile-first, like/comment.
- **PWA:** add a service worker (`/sw.js`) → installable + offline post (Randy walks daily; sync later).
- **Backend (recommendation):** Next.js full-stack — API routes + SQLite (`better-sqlite3`). One service, one deploy. (Alt: separate Python feed service — more moving parts.)

## HUP wiring (this repo)
- `railway.toml` — RAILPACK builder, `npm start`, healthcheck `/`, `restartPolicyMaxRetries = 10`.
- `scripts/hup-preflight.sh` — 9 safety gates (Next.js-adapted). Run before every push.
- `.githooks/pre-push` — auto-runs the preflight on `git push` (strict). Enable once:
  ```bash
  git config core.hooksPath .githooks
  ```

## Bring the source home (Step 1)
Buzz drops his local `hive-pwa` source (the real `app/`, `package.json`, `next.config.js`, etc.) into this repo, replacing the scaffold, then:
```bash
cd hive-pwa
git config core.hooksPath .githooks      # enable pre-push guard
git add -A && git commit -m "feat: Hive PWA source (from Buzz's local deploy)"
git remote add origin https://github.com/Buzz-Hive-Life/hive-pwa.git
git push -u origin main                  # preflight must pass first
```
Railway (watching `Buzz-Hive-Life/hive-pwa`) auto-builds + deploys. CB's expired GitHub token must be refreshed first (see blocker note).

## Blocker (2026-07-15)
CB's stored GitHub tokens (`~/.git-credentials`, `/opt/data/hive-docs-gh-token.txt`) are **expired (401)**. Until a valid token (or Buzz/Fundy) creates the empty `Buzz-Hive-Life/hive-pwa` repo, CB can scaffold + audit but not push. The scaffold is committed and push-ready.
