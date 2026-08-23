# Hacker House Medellín desktop applications

Verified **2026-08-06**.

## Required pair

- Rust: [`hacker-house-medellin/hhm-desktop.rs`](https://github.com/hacker-house-medellin/hhm-desktop.rs) — **planned**, not yet verified as published.
- Flutter: [`hacker-house-medellin/hhm-flutter`](https://github.com/hacker-house-medellin/hhm-flutter) — **planned**, not yet verified as published.

Both are first-class product applications. Do not mark either implementation live until the remote, native build, packaging, tests, and supported-platform matrix are verified.

## Rust desktop kit: Tauri 2 without React

The Rust application uses **Tauri 2**.

- React, JSX, React-derived stacks, Vue, and Svelte are prohibited.
- Use vanilla HTML, CSS, and TypeScript.
- HTMX is allowed for authenticated server-driven fragments when it reduces client complexity.
- Rust/Tauri commands own local persistence, secure storage, notifications, files, printing, deep-link validation, and privileged operations.
- Do not introduce an unauthenticated loopback HTTP service.

This strategy fits membership applications, residents, rooms, events, calendars, payments, community messaging, organizer workflows, and local printing while keeping privileged behavior in Rust.

The future Rust repository must contain `docs/DESKTOP_TOOLKIT.md` documenting the Tauri major-version policy, capability/CSP rules, no-React frontend policy, privilege boundary, deep links, packaging, platform tests, and Flutter companion.

## Parallel Rust and Flutter development

The Rust and Flutter applications are developed side-by-side to compare desktop UX, security, local integration, accessibility, Flutter mobile reuse, developer velocity, packaging, and long-term maintenance using the same product features.

Every desktop-facing feature must inspect both repositories, share acceptance criteria and fixtures, and normally update both. A one-sided change requires a documented no-change rationale and parity gap. The future `hhm-desktop.rs` README, `AGENTS.md`, pull-request template, and `docs/DESKTOP_TOOLKIT.md` must state this rule prominently.

## HTTPS-first deep links

Canonical route family:

```text
https://<verified-hhm-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
hhm://<route>?<bounded-query>
```

Rust and Flutter must share versioned route types and golden fixtures.

Initial route families may include applications, resident profiles, room/bed assignments, events, calendars, invoices/payments, messages, maintenance requests, and authenticated notifications.

Required behavior:

- cold-start and already-running/single-instance delivery;
- exact host, route/version, member/event/room/payment identifier, action, and bounded-query validation;
- authenticated resume and browser fallback;
- replay, expiry, membership/role, and unsafe-return validation;
- explicit confirmation before payments, assignments, invitations, check-in/out, or destructive actions; and
- macOS, Windows, Linux, Android, and iOS tests.

Passwords, bearer tokens, payment credentials, identity documents, private messages, access codes, and sensitive resident data are prohibited in URLs. Use short-lived, single-use, audience-bound codes for invitations, payment continuation, and authentication handoffs.

## Product boundary

Both implementations should converge on:

- applications and resident/member profiles;
- rooms, beds, occupancy, check-in/out, and maintenance;
- events, calendars, attendance, and notifications;
- invoices, payments, receipts, and role-aware administration;
- community messaging and announcements;
- offline/reconnection behavior;
- schemas, generated clients, route fixtures, privacy-safe sample data, and conformance tests.

## Project routing

- GitHub Project: [`hacker-house-medellin-project` — Project 1](https://github.com/orgs/hacker-house-medellin/projects/1)
- Linear project: `github.com/hacker-house-medellin`
- Central portfolio registry: tracked through the approved private registry using an opaque internal locator; do not expose a private repository URL in this public repository.
- Toolkit strategy: this public document is the Hacker House Medellín policy boundary; implementation repositories must carry their own `docs/DESKTOP_TOOLKIT.md`.
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, toolkit/frontend changes, deep-link changes, renames, transfers, archival, or platform-status changes must update this document, Linear, the approved private registry, and both companion repositories together.
