# `hacker-house-medellin` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **17**
- Private repository names withheld: **0**
- Relationship edges: **63**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/hacker-house-medellin/.github) | `organization_governance` | `active` |
| [`hhm-interfaces`](https://github.com/hacker-house-medellin/hhm-interfaces) | `interfaces` | `active` |
| [`hacker-house-medellin-clients`](https://github.com/hacker-house-medellin/hacker-house-medellin-clients) | `client_sdk` | `active` |
| [`hhm-clients`](https://github.com/hacker-house-medellin/hhm-clients) | `client_sdk` | `active` |
| [`hhm-api`](https://github.com/hacker-house-medellin/hhm-api) | `api_service` | `active` |
| [`hhm-sync`](https://github.com/hacker-house-medellin/hhm-sync) | `sync_service` | `active` |
| [`hhm-mcp-server.rs`](https://github.com/hacker-house-medellin/hhm-mcp-server.rs) | `mcp_server` | `active` |
| [`hhm-cli`](https://github.com/hacker-house-medellin/hhm-cli) | `cli` | `active` |
| [`hacker-house-medellin.github.io`](https://github.com/hacker-house-medellin/hacker-house-medellin.github.io) | `site` | `active` |
| [`hhm-infra`](https://github.com/hacker-house-medellin/hhm-infra) | `infrastructure` | `active` |
| [`hacker-house-medellin-monorepo`](https://github.com/hacker-house-medellin/hacker-house-medellin-monorepo) | `composition_workspace` | `active` |
| [`hhm-monorepo`](https://github.com/hacker-house-medellin/hhm-monorepo) | `composition_workspace` | `active` |
| [`hacker-house-medellin-libs`](https://github.com/hacker-house-medellin/hacker-house-medellin-libs) | `uncategorized` | `active` |
| [`hhm-dioxus-web`](https://github.com/hacker-house-medellin/hhm-dioxus-web) | `uncategorized` | `active` |
| [`hhm-leptos-web`](https://github.com/hacker-house-medellin/hhm-leptos-web) | `uncategorized` | `active` |
| [`hhm-libs`](https://github.com/hacker-house-medellin/hhm-libs) | `uncategorized` | `active` |
| [`hhm-mash-web`](https://github.com/hacker-house-medellin/hhm-mash-web) | `uncategorized` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-clients` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-libs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-monorepo` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin.github.io` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-cli` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-clients` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-dioxus-web` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-infra` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-leptos-web` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-libs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-mash-web` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-mcp-server.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-monorepo` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-sync` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `hacker-house-medellin/hacker-house-medellin-clients` | `generated_from` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: SDK bindings derive from canonical contracts |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin-clients` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin-libs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin.github.io` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-cli` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-clients` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-dioxus-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-infra` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-leptos-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-libs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-mash-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-mcp-server.rs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-monorepo` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `composes` | `hacker-house-medellin/hhm-sync` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-api` | `implements_contracts_from` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: service boundary implements canonical contracts |
| `hacker-house-medellin/hhm-cli` | `calls` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: client uses the product service boundary |
| `hacker-house-medellin/hhm-clients` | `generated_from` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: SDK bindings derive from canonical contracts |
| `hacker-house-medellin/hhm-infra` | `deploys` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `hacker-house-medellin/hhm-infra` | `deploys` | `hacker-house-medellin/hhm-cli` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `hacker-house-medellin/hhm-infra` | `deploys` | `hacker-house-medellin/hhm-mcp-server.rs` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `hacker-house-medellin/hhm-infra` | `deploys` | `hacker-house-medellin/hhm-sync` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `hacker-house-medellin/hhm-mcp-server.rs` | `uses_sdk` | `hacker-house-medellin/hacker-house-medellin-clients` | `inferred` / `role-convention`: agent adapter reuses the typed product SDK |
| `hacker-house-medellin/hhm-mcp-server.rs` | `calls` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: agent tools use the authenticated product API |
| `hacker-house-medellin/hhm-mcp-server.rs` | `uses_sdk` | `hacker-house-medellin/hhm-clients` | `inferred` / `role-convention`: agent adapter reuses the typed product SDK |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin-clients` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin-libs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin-monorepo` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hacker-house-medellin.github.io` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-cli` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-clients` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-dioxus-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-infra` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-leptos-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-libs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-mash-web` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-mcp-server.rs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-monorepo` | `composes` | `hacker-house-medellin/hhm-sync` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `hacker-house-medellin/hhm-sync` | `synchronizes_with` | `hacker-house-medellin/hhm-api` | `inferred` / `role-convention`: sync exchanges state through the product service boundary |
| `hacker-house-medellin/hhm-sync` | `uses_contracts_from` | `hacker-house-medellin/hhm-interfaces` | `inferred` / `role-convention`: sync payloads follow canonical schemas |
| `organization://hacker-house-medellin` | `reconciles_via` | `platform://opto-sync` | `platform-default` / `platform-policy`: product sync wraps the generic reconciliation engine |
| `organization://hacker-house-medellin` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://hacker-house-medellin` | `uses_transport_library` | `platform://ORESoftware/mcp-rust-libs` | `platform-default` / `platform-policy`: shared MCP transport and protocol hardening |
| `organization://hacker-house-medellin` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
