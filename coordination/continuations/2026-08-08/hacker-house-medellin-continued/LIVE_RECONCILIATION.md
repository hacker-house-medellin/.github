# Live GitHub reconciliation

Observed on August 8, 2026 through the connected GitHub App.

## Confirmed

- `hacker-house-medellin-test` is an installed/connected organization, but it currently contains zero repositories.
- `hacker-house-medellin/hhm-e2e` does not exist.
- `hacker-house-medellin/hhm-monorepo` exists with established production history; the local attachment is not an ancestor or safe replacement for that history.
- `hacker-house-medellin/.github` contains a reviewed canonical `repository-seeds/hhm-e2e` browser/contract harness. Its seed review and organization checks were already green.
- The connected App can create branches, commits, pull requests, comments, and merges in existing repositories, but it cannot create an organization repository.

## Action in this review

- Extend the canonical seed with the corrected Rust HTTP/WebSocket smoke runner.
- Restrict `publish.sh` to `hacker-house-medellin-test/hhm-e2e`.
- Generate npm and Cargo locks through their real resolvers before target publication.
- Add hosted Rust formatting, check, Clippy, and unit-test gates.
- Preserve the original reports and portable handoffs without embedding the binary archive.
- Preserve the relative `hhm-monorepo` gitlink proposal as an inactive handoff.

## Remaining fail-closed sequence

1. Use the approved short-lived repository-administration identity to create `hacker-house-medellin-test/hhm-e2e` from the reviewed seed.
2. Require the exact target default-branch SHA and all target GitHub Actions jobs to succeed.
3. Create or update the test monorepo only after it can resolve that exact gitlink.
4. Run HTTP/WebSocket smoke checks against explicitly mapped isolated test origins.
5. Promote the same reviewed source to production only after all prior evidence is recorded.
6. Keep DNS and Worker routes unchanged until hostname, origin, TLS, and health mappings are explicit.
