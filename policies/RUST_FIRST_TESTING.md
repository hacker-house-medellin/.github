# Rust-first scripts and tests

Use Rust instead of Python for new first-party scripts, validators, code generators, security checks, CI utilities and automated tests. Run cargo test, cargo fmt --check, cargo clippy -- -D warnings, and executable smoke tests. Do not introduce new .py automation files or new Python-backed workflow commands.

The following existing Python files are temporary migration debt: scripts/repository_relationships_lib.py, scripts/validate_baseline.py, scripts/validate_fleet_hardening_binding.py, scripts/validate_repository_relationships.py, and tests/test_fleet_hardening_binding.py. Existing Python workflow commands in baseline-policy.yml, fleet-hardening-binding.yml and repository-relationships.yml remain active until Rust parity is demonstrated with positive, negative, and exact-SHA CI evidence. Do not remove tests or weaken security gates to satisfy this language policy.

The Rust regression gate in tools/rust-first-policy is fail-closed for new Python script/test files and Python workflow steps. This organization's .github repository is an authority for guidance but its custom workflows are not automatically installed in sibling repositories: propagate and enforce them explicitly.
