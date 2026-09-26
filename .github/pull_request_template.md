<!--
Canonical organization pull-request template. The root and .github mirrors must remain byte-identical;
scripts/validate_baseline.py enforces that invariant.
-->
<!-- ore-org-baseline:begin -->
## Summary and ownership

Describe the problem, intended behavior, user or operational impact, repositories/components affected, and why this repository owns the change. Mark non-applicable checks as `N/A` with a reason.

## Planning and immutable dependencies

- Linear project or issue: [github.com/hacker-house-medellin](https://linear.app/denman/project/githubcomhacker-house-medellin-d4043553c2b4)
- Related GitHub issues or pull requests:
- Related repositories, releases, schemas, or external contracts:
- Immutable dependency/artifact revisions:

## Change control and repository boundaries

- [ ] All commits are on a topic branch and this pull request is the only proposed path into the protected target branch.
- [ ] No bot, generator, migration runner, or deployment process writes directly to `main`, `dev`, or another protected branch.
- [ ] The change is focused and does not silently cross repository ownership boundaries.
- [ ] Shared functionality is imported from its owning repository rather than copied into a local substitute.
- [ ] Cross-repository dependencies use an immutable commit, lockfile, digest, or reviewed Zed package; no floating branch or mutable image tag is promoted.
- [ ] No `*-infra` repository is introduced as a Git submodule under `*-monorepo/apps`.

## Contracts, generated artifacts, and compatibility

- [ ] TypeSpec and independently authored JSON Schema remain peer authorities; neither overwrites or outranks the other.
- [ ] TypeSpec-generated JSON Schema B is comparison evidence only and was checked against authored Schema A structurally and behaviorally.
- [ ] Generated interfaces, SQL/ORM projections, fixtures, clients, and documentation were regenerated from reviewed sources and were not hand-edited.
- [ ] Public API/RPC routes, request/response shapes, headers, query parameters, status codes, and compatibility implications were checked where applicable.
- [ ] Breaking changes include migration, staged rollout, rollback or roll-forward, and consumer-update evidence.

## SQL, persistence, synchronization, and money

- [ ] No SQL changes, or every declaration has a stable organization/domain namespace and explicit owning repository.
- [ ] Domain SQL may remain local, but identity, ordering, checksums, drift detection, and promotion are registered through `declarative-migrations`.
- [ ] Application startup validates schema compatibility and never applies production DDL.
- [ ] Diesel, SeaORM, generated SQL, live-catalog evidence, migrations, and fixtures are deterministic and in parity where applicable.
- [ ] Tenant isolation, RLS/authorization, idempotency, transaction/lock or fencing behavior, concurrent-race tests, and outbox delivery are covered.
- [ ] Browser/local state is treated as a resumable cache rather than legal, payment, rent-ledger, or server-authority evidence.
- [ ] Money uses integer minor units; Stripe or other provider secrets, raw card/bank data, and unverified webhook effects are excluded.

## Runtime, infrastructure, and security

- [ ] Rust servers compose ordered `ores-middleware`, `shared-auth`, route-specific `ores-rate-limit`, `ores-redis-lru-cache`, and `ores-otel` without local bypasses.
- [ ] Cross-layer state uses `opto-sync` where justified; secrets use `ores-sops` and only encrypted `env/enc` files are tracked.
- [ ] Public/admin `ores-chat` surfaces, `ores-wasm-loaders`, service workers, and background execution preserve tenant, privacy, and authorization boundaries where used.
- [ ] Application manifests remain app-owned; cluster composition uses `ORESoftware/k8s-cluster` and shared components use `ORESoftware/k8s-libs-and-shared-defs`.
- [ ] Workloads use least privilege, workload identity, restricted pod security, default-deny networking, explicit egress, probes, non-root execution, immutable images, and bounded resources.
- [ ] Authentication and authorization fail closed; admin/customer realms and databases remain isolated; sensitive actions are auditable.
- [ ] Credentials, private keys, personal data, legal records, user content, and high-cardinality identifiers are excluded from source, fixtures, logs, traces, and build artifacts.

## Validation and independent evidence

List exact commands, environments, immutable heads/artifacts, and results. Include format, lint, build, unit, integration, adversarial, contract/parity, migration, security, and end-to-end checks as applicable.

- [ ] Relevant `*-test` organization or isolated e2e suites ran against exact recorded revisions, including negative/failure modes and teardown or recovery evidence.
- [ ] Zed lifecycle hooks cover the relevant pre-build, pre-test, and pre-publish checks without replacing language-native validation.
- [ ] External Actions are pinned to full commit SHAs or container digests, checkout credentials do not persist, workflow permissions are least-privilege, and local jobs have bounded timeouts.
- [ ] Required reviews, branch protections, environment approvals, and security/compliance gates remain enabled and were not bypassed.

## Conflict-resolution record

- [ ] Remote state and relevant related repositories were inspected before editing and again before pushing.
- [ ] Concurrent work was preserved; no stash, rebase, reset, force push, destructive cleanup, or history rewrite was used.
- [ ] Conflicts, if any, were resolved semantically using the merge base, both complete sides, relevant history, tests, contracts, linked work, and related repositories.
- [ ] The complete tree was scanned for unresolved conflict markers; no side was accepted wholesale merely as `ours`, `theirs`, `current`, or `incoming`.

## Release, residual risk, and rollback

- Deployment or migration impact:
- Immutable release/image/artifact identity:
- `*-infra` desired-state change:
- Rollback or roll-forward procedure:
- Known limitations, deferred repositories, and follow-up work:
- Evidence-based merge confidence and remaining uncertainty:
<!-- ore-org-baseline:end -->

## Salvage check

If this PR supersedes or replaces an older one, say which, and name at least one
concrete thing carried forward from it (a test, a fixture, an error message, a
pin, a doc paragraph). See [`docs/pr-salvage-policy.md`](../docs/pr-salvage-policy.md).

- [ ] Supersedes nothing, **or** the salvaged item is named above.
