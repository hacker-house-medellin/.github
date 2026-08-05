<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [hacker-house-medellin](https://github.com/hacker-house-medellin)
- **Canonical GitHub Project:** [hacker-house-medellin-project](https://github.com/orgs/hacker-house-medellin/projects/1) (project 1)
- **Canonical Linear project:** [planning workspace](https://linear.app/denman/project/githubcomhacker-house-medellin-d4043553c2b4)
- **Organization documentation repository:** [hacker-house-medellin/.github](https://github.com/hacker-house-medellin/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, commits, pull requests, reviews, CI checks, releases, deployable artifacts, and runtime evidence. Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. The GitHub Project is the organization-level execution board and should contain the governance issue maintained by this repository.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.
<!-- org-project-routing:end -->

## Active delivery ledger

### `hhm-mcp-server.rs`

- **GitHub tracking issue:** [hacker-house-medellin/.github#4](https://github.com/hacker-house-medellin/.github/issues/4)
- **Executable repository seed:** [`repository-seeds/hhm-mcp-server.rs/`](../repository-seeds/hhm-mcp-server.rs/)
- **Canonical repository target:** `hacker-house-medellin/hhm-mcp-server.rs`
- **Dependency contract:** clients + interfaces + libs + CLI + sync + `shared-auth/shared-auth-clients`
- **Materialization:** `.vendor/.zed`
- **Publication:** run the seed's `publish.sh` only from an authenticated GitHub CLI environment; it refuses to overwrite an existing repository and does not embed credentials.
- **Composition:** committed canonical gitlinks are allowed as source transport and must be adopted with `zed overtake --git-submodules`; duplicate package identities and long-name aliases are prohibited.

GitHub Project #1 tracks execution. The Linear project tracks priority, ownership, dependencies, milestones, and delivery status. Repository, pull-request, CI, release, and runtime evidence remains in GitHub.
