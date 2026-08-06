# hhm-e2e

Canonical end-to-end and cross-repository contract harness for **Hacker House Medellín**.

This repository is intentionally offline-safe by default. Playwright, Puppeteer, and Selenium exercise the same local fixture contract. Live endpoints are opt-in through `E2E_BASE_URL` and must use isolated test tenants and ephemeral secrets.

## Canonical composition

Zed materializes `hhm-clients`, `hhm-interfaces`, `hhm-libs`, and `hhm-cli` under `.vendor/.zed`. Do not model those same repositories as gitlinks, and do not fabricate `.zpkg.lock`; create the lock only from a successful resolver run.

## Commands

```bash
npm ci
npm run test:offline
npx playwright install --with-deps chromium
npm run test:playwright
npm run test:puppeteer
npm run test:selenium
```

## Planning

- Canonical creation issue: https://github.com/hacker-house-medellin/hhm-monorepo/issues/8
- Linear project: https://linear.app/denman/project/githubcomhacker-house-medellin-d4043553c2b4
- GitHub Project: https://github.com/orgs/hacker-house-medellin/projects/1

The publication helper generates a real npm lockfile before creating the repository. A Zed lock remains deferred until a real successful Zed resolver run can certify all published dependencies.
