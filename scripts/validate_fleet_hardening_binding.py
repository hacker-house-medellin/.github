#!/usr/bin/env python3
"""Validate the organization fleet-hardening binding and its immutable source closure."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

DEFAULT_BINDING = Path("policy/ores-fleet-hardening.v1.json")
DEFAULT_SCHEMA = Path("policy/ores-fleet-hardening.v1.schema.json")
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
NAMESPACE = re.compile(r"^[a-z][a-z0-9_]{0,62}$")

EXPECTED_BINDING_KEYS = {"$schema", "api_version", "kind", "metadata", "spec"}
EXPECTED_METADATA_KEYS = {"organization", "environment", "sql_namespace"}
EXPECTED_SPEC_KEYS = {
    "source",
    "policy",
    "sql",
    "kubernetes",
    "repository_policy_path",
    "fail_closed",
}
EXPECTED_SOURCE_KEYS = {
    "repository",
    "commit",
    "policy_path",
    "policy_sha256",
    "schema_path",
    "schema_sha256",
}
EXPECTED_POLICY_KEYS = {"api_version", "name", "version"}
EXPECTED_SQL_KEYS = {
    "authority",
    "namespace",
    "namespace_pattern",
    "registry",
    "diesel_model",
    "seaorm_model",
}
EXPECTED_KUBERNETES_KEYS = {"cluster", "libraries", "deployment_model"}


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object member."""


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, DuplicateKeyError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} root must be an object")
    return value


def exact_keys(value: Any, expected: set[str], label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return {}
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        errors.append(f"{label} keys differ; missing={missing}, extra={extra}")
    return value


def require_equal(actual: Any, expected: Any, label: str, errors: list[str]) -> None:
    if actual != expected:
        errors.append(f"{label} must equal {expected!r}")


def require_pattern(actual: Any, pattern: re.Pattern[str], label: str, errors: list[str]) -> None:
    if not isinstance(actual, str) or pattern.fullmatch(actual) is None:
        errors.append(f"{label} has invalid format")


def checked_relative_path(actual: Any, label: str, errors: list[str]) -> PurePosixPath | None:
    if not isinstance(actual, str) or not actual:
        errors.append(f"{label} must be nonempty text")
        return None
    if "\\" in actual or any(ord(character) < 32 for character in actual):
        errors.append(f"{label} contains a forbidden character")
        return None
    path = PurePosixPath(actual)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        errors.append(f"{label} must be a normalized relative path")
        return None
    return path


def validate_binding_documents(binding: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    exact_keys(binding, EXPECTED_BINDING_KEYS, "binding", errors)
    require_equal(binding.get("$schema"), "./ores-fleet-hardening.v1.schema.json", "binding.$schema", errors)
    require_equal(
        binding.get("api_version"),
        "ores.dev/fleet-hardening-binding/v1",
        "binding.api_version",
        errors,
    )
    require_equal(binding.get("kind"), "OrganizationHardeningPolicyBinding", "binding.kind", errors)

    metadata = exact_keys(binding.get("metadata"), EXPECTED_METADATA_KEYS, "binding.metadata", errors)
    require_equal(metadata.get("organization"), "hacker-house-medellin", "metadata.organization", errors)
    require_equal(metadata.get("environment"), "production", "metadata.environment", errors)
    require_equal(metadata.get("sql_namespace"), "hacker_house_medellin", "metadata.sql_namespace", errors)

    spec = exact_keys(binding.get("spec"), EXPECTED_SPEC_KEYS, "binding.spec", errors)
    source = exact_keys(spec.get("source"), EXPECTED_SOURCE_KEYS, "binding.spec.source", errors)
    require_equal(source.get("repository"), "ORESoftware/ores-gh-bots", "source.repository", errors)
    require_pattern(source.get("commit"), SHA1, "source.commit", errors)
    require_equal(source.get("policy_path"), "config/hardening-fleet.v1.json", "source.policy_path", errors)
    require_pattern(source.get("policy_sha256"), SHA256, "source.policy_sha256", errors)
    require_equal(
        source.get("schema_path"),
        "config/hardening-fleet.v1.schema.json",
        "source.schema_path",
        errors,
    )
    require_pattern(source.get("schema_sha256"), SHA256, "source.schema_sha256", errors)
    checked_relative_path(source.get("policy_path"), "source.policy_path", errors)
    checked_relative_path(source.get("schema_path"), "source.schema_path", errors)

    policy = exact_keys(spec.get("policy"), EXPECTED_POLICY_KEYS, "binding.spec.policy", errors)
    require_equal(policy.get("api_version"), "ores.dev/fleet-hardening/v1", "policy.api_version", errors)
    require_equal(policy.get("name"), "ores-fleet-hardening", "policy.name", errors)
    require_equal(policy.get("version"), "1.0.0", "policy.version", errors)

    sql = exact_keys(spec.get("sql"), EXPECTED_SQL_KEYS, "binding.spec.sql", errors)
    require_equal(
        sql.get("authority"),
        "organization-local-with-central-mirror",
        "sql.authority",
        errors,
    )
    require_equal(sql.get("namespace"), "hacker_house_medellin", "sql.namespace", errors)
    require_equal(
        sql.get("namespace_pattern"),
        "^[a-z][a-z0-9_]{0,62}$",
        "sql.namespace_pattern",
        errors,
    )
    require_equal(
        sql.get("registry"),
        "declarative-migrations/declarative-postgres-migrate.rs",
        "sql.registry",
        errors,
    )
    require_equal(sql.get("diesel_model"), "code-first", "sql.diesel_model", errors)
    require_equal(sql.get("seaorm_model"), "database-first", "sql.seaorm_model", errors)
    namespace = sql.get("namespace")
    if not isinstance(namespace, str) or NAMESPACE.fullmatch(namespace) is None:
        errors.append("sql.namespace does not satisfy the canonical namespace pattern")
    if metadata.get("sql_namespace") != namespace:
        errors.append("metadata.sql_namespace and sql.namespace differ")

    kubernetes = exact_keys(
        spec.get("kubernetes"),
        EXPECTED_KUBERNETES_KEYS,
        "binding.spec.kubernetes",
        errors,
    )
    require_equal(kubernetes.get("cluster"), "ORESoftware/k8s-cluster", "kubernetes.cluster", errors)
    require_equal(
        kubernetes.get("libraries"),
        "ORESoftware/k8s-libs-and-shared-defs",
        "kubernetes.libraries",
        errors,
    )
    require_equal(kubernetes.get("deployment_model"), "gitops", "kubernetes.deployment_model", errors)
    require_equal(
        spec.get("repository_policy_path"),
        ".ores/repository-hardening.v1.json",
        "spec.repository_policy_path",
        errors,
    )
    require_equal(spec.get("fail_closed"), True, "spec.fail_closed", errors)

    require_equal(schema.get("$schema"), "https://json-schema.org/draft/2020-12/schema", "schema.$schema", errors)
    require_equal(
        schema.get("$id"),
        "https://github.com/hacker-house-medellin/.github/blob/main/policy/ores-fleet-hardening.v1.schema.json",
        "schema.$id",
        errors,
    )
    require_equal(schema.get("type"), "object", "schema.type", errors)
    require_equal(schema.get("additionalProperties"), False, "schema.additionalProperties", errors)
    source_schema = (
        schema.get("properties", {})
        .get("spec", {})
        .get("properties", {})
        .get("source", {})
    )
    require_equal(source_schema.get("additionalProperties"), False, "schema source additionalProperties", errors)
    require_equal(
        set(source_schema.get("required", [])),
        EXPECTED_SOURCE_KEYS,
        "schema source required keys",
        errors,
    )
    return errors


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def source_file(root: Path, relative: PurePosixPath, label: str, errors: list[str]) -> Path | None:
    candidate = root.joinpath(*relative.parts)
    try:
        resolved_root = root.resolve(strict=True)
        resolved = candidate.resolve(strict=True)
    except OSError as exc:
        errors.append(f"{label} cannot be resolved: {exc}")
        return None
    if candidate.is_symlink() or resolved_root not in resolved.parents:
        errors.append(f"{label} escapes the source checkout or is a symlink")
        return None
    if not resolved.is_file():
        errors.append(f"{label} is not a regular file")
        return None
    return resolved


def verify_source_documents(
    binding: dict[str, Any],
    source_root: Path,
    observed_commit: str,
) -> list[str]:
    errors: list[str] = []
    source = binding.get("spec", {}).get("source", {})
    if source.get("commit") != observed_commit:
        errors.append("source checkout commit does not match the binding")

    policy_relative = checked_relative_path(source.get("policy_path"), "source.policy_path", errors)
    schema_relative = checked_relative_path(source.get("schema_path"), "source.schema_path", errors)
    if policy_relative is None or schema_relative is None:
        return errors

    policy_path = source_file(source_root, policy_relative, "source policy", errors)
    schema_path = source_file(source_root, schema_relative, "source schema", errors)
    if policy_path is None or schema_path is None:
        return errors

    policy_bytes = policy_path.read_bytes()
    schema_bytes = schema_path.read_bytes()
    if sha256_bytes(policy_bytes) != source.get("policy_sha256"):
        errors.append("source policy SHA-256 does not match the binding")
    if sha256_bytes(schema_bytes) != source.get("schema_sha256"):
        errors.append("source schema SHA-256 does not match the binding")

    try:
        policy = json.loads(policy_bytes.decode("utf-8"), object_pairs_hook=unique_object)
        source_schema = json.loads(schema_bytes.decode("utf-8"), object_pairs_hook=unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateKeyError) as exc:
        errors.append(f"source closure is not unique-key UTF-8 JSON: {exc}")
        return errors
    if not isinstance(policy, dict) or not isinstance(source_schema, dict):
        errors.append("source policy and schema roots must be objects")
        return errors

    spec = binding.get("spec", {})
    expected = {
        "$schema": "./hardening-fleet.v1.schema.json",
        "api_version": spec.get("policy", {}).get("api_version"),
        "kind": "FleetHardeningPolicy",
        "metadata": {
            "name": spec.get("policy", {}).get("name"),
            "version": spec.get("policy", {}).get("version"),
        },
        "spec": {
            "sql": {
                "authority": spec.get("sql", {}).get("authority"),
                "namespace_pattern": spec.get("sql", {}).get("namespace_pattern"),
                "migration_registry": spec.get("sql", {}).get("registry"),
                "diesel_model": spec.get("sql", {}).get("diesel_model"),
                "seaorm_model": spec.get("sql", {}).get("seaorm_model"),
            },
            "kubernetes": {
                "cluster_repository": spec.get("kubernetes", {}).get("cluster"),
                "shared_library_repository": spec.get("kubernetes", {}).get("libraries"),
                "deployment_model": spec.get("kubernetes", {}).get("deployment_model"),
            },
            "repository": {
                "binding_path": spec.get("repository_policy_path"),
                "fail_closed": spec.get("fail_closed"),
            },
            "supply_chain": {
                "source_revision_required": True,
                "content_sha256_required": True,
            },
        },
    }
    if policy != expected:
        errors.append("source policy semantics differ from the organization binding")
    if source_schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("source schema is not Draft 2020-12")
    if source_schema.get("additionalProperties") is not False:
        errors.append("source schema does not fail closed on unknown top-level fields")
    return errors


def observed_git_commit(source_root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(source_root), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError("source checkout has no readable Git HEAD")
    commit = result.stdout.strip()
    if SHA1.fullmatch(commit) is None:
        raise ValueError("source checkout HEAD is not a full SHA-1 commit")
    return commit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binding", type=Path, default=DEFAULT_BINDING)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--metadata-only", action="store_true")
    args = parser.parse_args()

    try:
        binding = load_json(args.binding)
        schema = load_json(args.schema)
    except ValueError as exc:
        print(f"fleet-hardening binding: {exc}", file=sys.stderr)
        return 1

    errors = validate_binding_documents(binding, schema)
    if args.source_root is not None and not args.metadata_only:
        try:
            commit = observed_git_commit(args.source_root)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            errors.extend(verify_source_documents(binding, args.source_root, commit))
    elif args.source_root is None and not args.metadata_only:
        errors.append("--source-root is required unless --metadata-only is used")

    if errors:
        for error in errors:
            print(f"fleet-hardening binding: {error}", file=sys.stderr)
        return 1
    print("fleet-hardening binding: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
