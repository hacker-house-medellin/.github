# Inactive hhm-monorepo handoff

This packet preserves the attachment's relative-submodule intent without changing the established production `hacker-house-medellin/hhm-monorepo` history.

The proposed gitlink is deliberately inactive because commit `9ab38530846bc0d837dd0a5cbe603ef8c3c97588` exists only in the supplied local repository. It must not be added to a remote monorepo until the canonical test repository contains an equivalent reviewed head and target GitHub Actions are green.

Activation requirements:

1. Create `hacker-house-medellin-test/hhm-e2e` through the approved repository-administration path.
2. Record the target repository ID, default branch, and exact green SHA.
3. Replace the attachment-only SHA in `gitlinks.json` with that target SHA.
4. Apply the relative URL in the test monorepo and prove a fresh recursive clone.
5. Promote the same graph to production through a separate reviewed pull request; never overwrite or force-push established monorepo history.
