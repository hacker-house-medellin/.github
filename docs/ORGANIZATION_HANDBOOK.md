# hacker-house-medellin organization handbook

> Shared operating defaults for repositories maintained under **hacker-house-medellin**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

hacker-house-medellin maintains community, event, project, learning, and operational software and documentation for Hacker House Medellín. This `.github` repository is the canonical home for shared policy, reusable templates, community health files, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported environments, development and test commands, authoritative interfaces and content, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Community systems should also document organizer responsibility, participant privacy and consent, venue and event provenance, moderation, accessibility, localization, safeguarding, retention, incident escalation, and operational limitations.

## Change workflow

1. Anchor work in an issue, Linear item, or documented community objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, participant and organizer impact, validation, compatibility, migration, and rollback.
4. Test permission, privacy, localization, accessibility, capacity, cancellation, notification failure, moderation, and recovery paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence, security, and documentation

Pull requests should include reproducible commands, synthetic fixtures, expected and observed outcomes, negative-path coverage, documentation updates, and CI or local-equivalent results. Never commit credentials, participant records, private contact details, identity documents, payment data, or sensitive logs. Follow `SECURITY.md` for private reporting. Keep community rules, privacy, consent, accessibility, moderation, safeguarding, and important operational decisions explicit.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Community health files and reusable issue/PR guidance are present.
- [ ] Ownership, privacy, consent, moderation, accessibility, safeguarding, and escalation are documented.
- [ ] Required checks cover permissions, privacy, notification failure, localization, compatibility, and supply-chain risk.
- [ ] Stale repositories are archived or clearly marked.
- [ ] GitHub Project and Linear links resolve and reflect completed work.
