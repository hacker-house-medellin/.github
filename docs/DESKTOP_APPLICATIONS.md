# Hacker House Medellín desktop applications

Verified **2026-08-24**.

## Required pair

- Rust: [`hacker-house-medellin/hhm-desktop-app.rs`](https://github.com/hacker-house-medellin/hhm-desktop-app.rs) — public companion repository.
- Flutter: [`hacker-house-medellin/hhm-flutter`](https://github.com/hacker-house-medellin/hhm-flutter) — public mobile and desktop application repository.

Both are first-class product applications. Do not mark either implementation live until the remote, native build, packaging, tests, and supported-platform matrix are verified.

## Rust desktop kit: Slint, winit, and a stable FFI boundary

The Rust application uses **Slint over its winit backend**, not Qt. Product state and privileged operations remain in a renderer-independent Rust core.

- The core exposes an explicitly versioned C ABI through `cdylib` and `staticlib` artifacts so Dart FFI and another reviewed UI skin can consume the same behavior.
- The ABI uses opaque handles, explicit ownership and string-release functions, bounded UTF-8 inputs, documented thread rules, and panic containment. Rust unwinding and borrowed Rust references never cross the boundary.
- Slint owns presentation only. Rust services own local persistence, secure storage, notifications, files, printing, deep-link validation, authenticated API calls, authorization checks, and other privileged operations.
- Shared Auth and Supabase tokens remain in OS-protected storage and are never passed into markup, logs, telemetry attributes, QR payloads, or Bluetooth advertisements.
- A second UI skin must call the same versioned FFI contract and conformance fixtures; it must not fork product authorization or persistence behavior.
- Do not introduce an unauthenticated loopback HTTP service.

This strategy fits membership applications, residents, rooms, events, calendars, payments, community messaging, organizer workflows, and local printing while keeping privileged behavior in Rust.

The Rust repository must contain `docs/DESKTOP_TOOLKIT.md` documenting the Slint and winit version policy, FFI compatibility and ownership rules, privilege boundary, deep links, packaging, platform tests, and Flutter companion.

## Parallel Rust and Flutter development

The Rust and Flutter applications are developed side-by-side to compare desktop UX, security, local integration, accessibility, Flutter mobile reuse, developer velocity, packaging, and long-term maintenance using the same product features.

Every desktop-facing feature must inspect both repositories, share acceptance criteria and fixtures, and normally update both. A one-sided change requires a documented no-change rationale and parity gap. The `hhm-desktop-app.rs` README, `AGENTS.md`, pull-request template, and `docs/DESKTOP_TOOLKIT.md` must state this rule prominently.

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
