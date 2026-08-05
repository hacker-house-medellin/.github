<!-- ore-org-baseline:begin -->
# Repository relationships for `hacker-house-medellin`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **16**
- Relationships represented: **20**
- Inventory digest: `sha256:88f5eeb87bb5a0ab3b9428ebe943cf1dcfa24d41198e39de093b26418725e47f`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:hacker-house-medellin` |
| GitHub owner ID | `313129602` |
| Linear project ID | `332fce55-f661-402d-8c77-8e400e5377c4` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `hacker-house-medellin/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `hacker-house-medellin/hacker-house-medellin-clients` | `public` | `clients` | no |
| `hacker-house-medellin/hacker-house-medellin-libs` | `public` | `repository` | no |
| `hacker-house-medellin/hacker-house-medellin-monorepo` | `public` | `monorepo` | no |
| `hacker-house-medellin/hacker-house-medellin.github.io` | `public` | `documentation-site` | no |
| `hacker-house-medellin/hhm-api` | `public` | `api-server` | no |
| `hacker-house-medellin/hhm-cli` | `public` | `repository` | no |
| `hacker-house-medellin/hhm-clients` | `public` | `clients` | no |
| `hacker-house-medellin/hhm-dioxus-web` | `public` | `repository` | no |
| `hacker-house-medellin/hhm-infra` | `public` | `infrastructure` | no |
| `hacker-house-medellin/hhm-interfaces` | `public` | `interfaces` | no |
| `hacker-house-medellin/hhm-leptos-web` | `public` | `repository` | no |
| `hacker-house-medellin/hhm-libs` | `public` | `repository` | no |
| `hacker-house-medellin/hhm-mash-web` | `public` | `repository` | no |
| `hacker-house-medellin/hhm-monorepo` | `public` | `monorepo` | no |
| `hacker-house-medellin/hhm-sync` | `public` | `sync` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-clients` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-libs` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin-monorepo` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hacker-house-medellin.github.io` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-api` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-cli` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-clients` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-dioxus-web` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-infra` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-interfaces` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-leptos-web` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-libs` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-mash-web` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-monorepo` | `declared` | yes |
| `hacker-house-medellin/.github` | `governs` | `hacker-house-medellin/hhm-sync` | `declared` | yes |
| `hacker-house-medellin/hacker-house-medellin.github.io` | `documents` | `hacker-house-medellin/.github` | `inferred` | no |
| `hacker-house-medellin/hhm-api` | `depends_on` | `hacker-house-medellin/hhm-interfaces` | `inferred` | no |
| `hacker-house-medellin/hhm-clients` | `depends_on` | `hacker-house-medellin/hhm-interfaces` | `inferred` | no |
| `hacker-house-medellin/hhm-infra` | `deploys` | `hacker-house-medellin/hhm-monorepo` | `inferred` | no |
| `hacker-house-medellin/hhm-sync` | `depends_on` | `hacker-house-medellin/hhm-interfaces` | `inferred` | no |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `approved-private-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
