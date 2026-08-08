# hhm-e2e

Canonical end-to-end and cross-repository contract harness for **Hacker House Medellín**.

This repository is intentionally offline-safe by default. Playwright, Puppeteer, and Selenium exercise the same local fixture contract. The nested Rust smoke crate validates the Mash, Leptos, Dioxus, API health endpoints, and the API WebSocket upgrade. Live endpoints are opt-in and must use isolated test tenants and ephemeral secrets.

## Canonical composition

Zed materializes `hhm-clients`, `hhm-interfaces`, `hhm-libs`, and `hhm-cli` under `.vendor/.zed`. Do not model those same repositories as gitlinks, and do not fabricate `.zpkg.lock`; create the lock only from a successful resolver run.

## Browser dependency policy

The browser libraries are exact-pinned in `package.json` and mirrored by `scripts/validate-structure.mjs`. Update both files together, verify that each version is published, and let the real npm resolver generate `package-lock.json`; never hand-author a lockfile.

## Commands

```bash
npm ci
npm run test:offline
npx playwright install --with-deps chromium
npm run test:playwright
npm run test:puppeteer
npm run test:selenium

cargo fmt --manifest-path rust-smoke/Cargo.toml --all -- --check
cargo clippy --manifest-path rust-smoke/Cargo.toml --all-targets --all-features -- -D warnings
cargo test --manifest-path rust-smoke/Cargo.toml --all-targets --all-features
```

For live Rust smoke checks:

```bash
export HHM_MASH_URL=http://localhost:8080
export HHM_LEPTOS_URL=http://localhost:8081
export HHM_DIOXUS_URL=http://localhost:8082
export HHM_API_URL=http://localhost:8090
cargo run --manifest-path rust-smoke/Cargo.toml
```

## Planning

- Canonical creation issue: https://github.com/hacker-house-medellin/hhm-monorepo/issues/8
- Linear project: https://linear.app/denman/project/githubcomhacker-house-medellin-d4043553c2b4
- GitHub Project: https://github.com/orgs/hacker-house-medellin/projects/1

The publication helper generates a real npm lockfile before creating the repository. A Cargo lock and Zed lock remain deferred until their real resolvers successfully certify the published dependency graphs.
