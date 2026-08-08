# Hacker House Medellín continuation handoff

This directory preserves the non-secret evidence from `hacker-house-medellin-continued.zip` and records the live GitHub reconciliation performed on August 8, 2026.

## Integrity

The supplied archive matched its sidecar checksum exactly:

`93f08a123f38ffdc7a99abee809ccc8348c00442868c14edb79f8bbd669a443b`

The binary archive is intentionally not committed to this public organization-policy repository. Its checksum, original status reports, portable agent-bridge data, handoff packets, and the reviewed source integration are committed instead.

## Reconciliation

- The original run prepared local `hhm-e2e` head `9ab38530846bc0d837dd0a5cbe603ef8c3c97588` and local `hhm-monorepo` head `83032a7251e18c18dd5086a3786468c450dfbfc8`.
- The connected GitHub App can read and write existing Hacker House Medellín repositories, and `hacker-house-medellin-test` is connected, but the test organization currently has no repositories.
- The connector does not expose organization-level repository creation. The approved repository-administration path remains required; exposed long-lived credentials are not used as publication evidence.
- The existing reviewed Node/browser `hhm-e2e` seed remains canonical. The attached Rust HTTP/WebSocket runner is integrated as a complementary `rust-smoke` crate rather than creating a competing seed.
- The attached Rust source contained an invalid leading backslash. The canonical seed removes that defect and requires hosted formatting, check, Clippy, and test gates.
- The production `hhm-monorepo` already has established history and a richer dependency graph. The relative-submodule proposal is preserved below but is not applied until the test repository exists and its exact head is green.
- No production repository, DNS record, custom domain, WAF rule, R2 route, or Cloudflare Worker route was changed by this reconciliation.

The files under `original/` remain the source of truth for the environment that generated the attachment. `LIVE_RECONCILIATION.md` and `agent-bridge.live.json` describe the newer connected-GitHub observation.
