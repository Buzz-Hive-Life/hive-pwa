#!/usr/bin/env bash
# =============================================================================
# HUP Pre-Flight v3.0 (Next.js / Node variant) — 9 gates before any hive-pwa push
# Mirrors the Hermes-agent HUP gates but adapted for a RAILPACK Next.js build.
# Run from repo root. Usage: bash scripts/hup-preflight.sh [--strict]
# =============================================================================
set -uo pipefail
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
PASS=0; FAIL=0; WARN=0
STRICT=false
[[ "${1:-}" == "--strict" ]] && STRICT=true

check() { printf "  %-50s " "$1"; }
pass()  { echo -e "${GREEN}PASS${NC}"; ((PASS++)); }
fail()  { echo -e "${RED}FAIL${NC}  -> $1"; ((FAIL++)); }
warn()  { echo -e "${YELLOW}WARN${NC}  -> $1"; ((WARN++)); $STRICT && ((FAIL++)); }

echo "═══════════════════════════════════════════════════"
echo "  HIVE-PWA HUP PRE-FLIGHT v3.0 (Next.js) — $(date '+%Y-%m-%d %H:%M:%S')"
echo "  Repo: $(git rev-parse --show-toplevel 2>/dev/null || echo UNKNOWN)"
echo "═══════════════════════════════════════════════════"
echo ""

# 1. railway.toml exists
check "1. railway.toml exists"
[ -f railway.toml ] && pass || fail "railway.toml missing in repo root"

# 2. [build] + [deploy] headers
check "2. [build]+[deploy] TOML headers"
grep -q '^\[build\]' railway.toml 2>/dev/null && grep -q '^\[deploy\]' railway.toml 2>/dev/null && pass \
  || fail "missing [build] and/or [deploy] section headers"

# 3. startCommand valid for Next.js
check "3. startCommand present"
SC=$(grep -E '^\s*startCommand\s*=' railway.toml 2>/dev/null | head -1)
if [ -n "$SC" ]; then
  if echo "$SC" | grep -qE 'npm start|next start|node'; then pass; else warn "startCommand '$SC' unexpected for Next.js"; fi
else
  warn "no startCommand set (Railway must auto-detect Next.js)"
fi

# 4. healthcheckPath set
check "4. healthcheckPath set"
HP=$(grep -E '^\s*healthcheckPath\s*=' railway.toml 2>/dev/null | grep -oE '"[^"]*"' | tr -d '"')
if [ -n "$HP" ]; then pass; echo "       Path: $HP"; else warn "no healthcheckPath (Railway defaults to /)"; fi

# 5. restartPolicyMaxRetries >= 10
check "5. restartPolicyMaxRetries >= 10"
RR=$(grep -E '^\s*restartPolicyMaxRetries\s*=' railway.toml 2>/dev/null | grep -oE '[0-9]+' | head -1)
if [ -n "$RR" ] && [ "$RR" -ge 10 ]; then pass
elif [ -n "$RR" ]; then fail "restartPolicyMaxRetries = $RR (minimum 10)"
else warn "not set (defaults to 3, recommend 10+)"; fi

# 6. package.json present (Node project)
check "6. package.json present"
[ -f package.json ] && pass || warn "package.json missing — drop Buzz's Next.js package.json in before first deploy"

# 7. node_modules ignored
check "7. node_modules in .gitignore"
grep -qE '^node_modules' .gitignore 2>/dev/null && pass || fail "node_modules NOT gitignored (would bloat the repo)"

# 8. no uncommitted changes
check "8. No uncommitted changes"
if git diff-index --quiet HEAD -- 2>/dev/null; then pass
else fail "Uncommitted changes: $(git status --short 2>/dev/null | head -3)"; fi

# 9. git remote correct
check "9. git remote origin"
REMOTE=$(git remote get-url origin 2>/dev/null || echo NO_REMOTE)
if [ "$REMOTE" != "NO_REMOTE" ]; then pass; echo "       $REMOTE"; else fail "no origin remote configured"; fi

echo ""
echo "═══════════════════════════════════════════════════"
printf "  RESULTS:  ${GREEN}%d passed${NC}  ${RED}%d failed${NC}" "$PASS" "$FAIL"
[ "$WARN" -gt 0 ] && printf "  ${YELLOW}%d warnings${NC}" "$WARN"
echo ""
echo "═══════════════════════════════════════════════════"
if [ "$FAIL" -gt 0 ]; then echo -e "\n${RED}PRE-FLIGHT FAILED — fix issues above before pushing.${NC}"; exit 1; fi
if [ "$WARN" -gt 0 ] && $STRICT; then echo -e "\n${RED}PRE-FLIGHT FAILED (strict) — fix warnings.${NC}"; exit 1; fi
echo -e "\n${GREEN}PRE-FLIGHT PASSED — safe to push.${NC}"; exit 0
