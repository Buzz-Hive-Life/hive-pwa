#!/usr/bin/env bash
# arm-hooks.sh — arm the repo's pre-push gate on THIS clone.
#
# WHY THIS EXISTS (2026-11-25, hive-security canary follow-up): the README named the
# arming command twice and this clone still read `core.hooksPath` UNSET. *A named
# instruction is a note; what was missing is a step that RUNS.* So this is executable,
# idempotent, and it READS BACK — the exit code is the receipt, not the claim.
#
# ⚠️ AND WHY THERE IS NO "armed?" GATE INSIDE hup-preflight.sh: that would be VACUOUS.
# The preflight only runs *because* the hook is armed, so a check for arming inside it
# can never fire in the state it is meant to catch. *A control cannot test the condition
# that gates whether it runs.* The un-forgettable route is CI, which invokes the
# preflight directly (see .github/workflows/hup-preflight.yml) and needs no arming.
#
# USAGE
#   bash scripts/arm-hooks.sh          # arm, then read back (exit 0 = armed)
#   bash scripts/arm-hooks.sh --check  # report only; exit 1 if NOT armed
set -uo pipefail

WANT=".githooks"
CHECK=0
[ "${1:-}" = "--check" ] && CHECK=1

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "arm-hooks: not inside a git work tree — nothing to arm"; exit 2; }

if [ ! -d "$ROOT/$WANT" ]; then
  echo "arm-hooks: $WANT/ is absent at $ROOT — nothing to arm"; exit 1
fi

if [ "$CHECK" = 1 ]; then
  cur="$(git -C "$ROOT" config --get core.hooksPath || true)"
  if [ "$cur" = "$WANT" ]; then
    echo "arm-hooks: ARMED (core.hooksPath=$cur)"; exit 0
  fi
  echo "arm-hooks: NOT ARMED (core.hooksPath=${cur:-<unset>}) — the pre-push gate will NOT run here"; exit 1
fi

git -C "$ROOT" config core.hooksPath "$WANT"
cur="$(git -C "$ROOT" config --get core.hooksPath || true)"
if [ "$cur" = "$WANT" ]; then
  echo "arm-hooks: ARMED — read back: core.hooksPath=$cur"
  echo "  the pre-push gate now runs on every push from this clone"
  exit 0
fi
echo "arm-hooks: FAILED to arm — read back core.hooksPath=${cur:-<unset>}"; exit 1
