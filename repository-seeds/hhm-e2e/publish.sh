#!/usr/bin/env bash
set -euo pipefail

repository="hacker-house-medellin-test/hhm-e2e"
seed_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

for command in gh npm node cargo rustup git; do
  command -v "$command" >/dev/null 2>&1 || {
    echo "$command is required" >&2
    exit 127
  }
done

gh auth status --hostname github.com >/dev/null
if gh repo view "$repository" >/dev/null 2>&1; then
  echo "$repository already exists; refusing to overwrite it" >&2
  exit 17
fi

case "$repository" in
  hacker-house-medellin-test/*) ;;
  *)
    echo "publisher is restricted to hacker-house-medellin-test" >&2
    exit 18
    ;;
esac

cp -R "$seed_dir"/. "$work_dir"/
rm -f "$work_dir/publish.sh"

test ! -e "$work_dir/.zpkg.lock"
test ! -e "$work_dir/.gitmodules"
test ! -e "$work_dir/rust-smoke/Cargo.lock"

npm --prefix "$work_dir" install --package-lock-only --ignore-scripts --no-audit --no-fund
npm --prefix "$work_dir" ci --ignore-scripts --no-audit --no-fund
node "$work_dir/scripts/validate-structure.mjs"
node --test "$work_dir"/tests/contracts/*.test.mjs

rustup component add rustfmt clippy
cargo generate-lockfile --manifest-path "$work_dir/rust-smoke/Cargo.toml"
cargo fmt --manifest-path "$work_dir/rust-smoke/Cargo.toml" --all -- --check
cargo check --manifest-path "$work_dir/rust-smoke/Cargo.toml" --locked --all-targets
cargo clippy --manifest-path "$work_dir/rust-smoke/Cargo.toml" --locked --all-targets -- -D warnings
cargo test --manifest-path "$work_dir/rust-smoke/Cargo.toml" --locked

if grep -RInE --exclude-dir=node_modules --exclude-dir=target --exclude-dir=.vendor \
  '(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|lin_api_[A-Za-z0-9]{20,}|cfat_[A-Za-z0-9_-]{20,}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----)' \
  "$work_dir"; then
  echo "credential-shaped value found in publication tree" >&2
  exit 19
fi

git -C "$work_dir" init --initial-branch=main
git -C "$work_dir" config user.name "ORESoftware automation"
git -C "$work_dir" config user.email "11139560+ORESoftware@users.noreply.github.com"
git -C "$work_dir" add --all
git -C "$work_dir" commit -m "bootstrap canonical hhm-e2e test harness"
gh repo create "$repository" --public \
  --description "Hacker House Medellín test-organization end-to-end and contract harness" \
  --source "$work_dir" --remote origin --push

echo "published https://github.com/$repository"
echo "production promotion remains blocked until this exact head is green in target GitHub Actions"
