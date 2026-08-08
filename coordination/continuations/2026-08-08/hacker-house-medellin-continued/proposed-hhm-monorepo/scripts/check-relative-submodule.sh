#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

grep -Fq 'path = apps/hhm-e2e' .gitmodules
grep -Fq 'url = ../hhm-e2e.git' .gitmodules
node -e '
  const fs = require("node:fs");
  const repos = JSON.parse(fs.readFileSync("repos.json", "utf8"));
  const links = JSON.parse(fs.readFileSync("gitlinks.json", "utf8"));
  if (repos.repositories?.length !== 1) throw new Error("unexpected repository count");
  if (repos.repositories[0].url !== "../hhm-e2e.git") throw new Error("relative URL drift");
  if (links.gitlinks?.[0]?.activation_state !== "blocked-until-target-exact-head-is-green") {
    throw new Error("fail-closed activation state weakened");
  }
'

echo "relative hhm-e2e handoff validated; activation remains blocked"
