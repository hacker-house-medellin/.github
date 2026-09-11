from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "fleet_binding",
    ROOT / "scripts/validate_fleet_hardening_binding.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FleetHardeningBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.binding = MODULE.load_json(ROOT / "policy/ores-fleet-hardening.v1.json")
        cls.schema = MODULE.load_json(ROOT / "policy/ores-fleet-hardening.v1.schema.json")

    def test_checked_in_binding_and_schema_are_valid(self) -> None:
        self.assertEqual(MODULE.validate_binding_documents(self.binding, self.schema), [])

    def test_floating_source_and_namespace_drift_fail_closed(self) -> None:
        binding = copy.deepcopy(self.binding)
        binding["spec"]["source"]["commit"] = "main"
        binding["spec"]["sql"]["namespace"] = "Hacker-House"
        errors = "\n".join(MODULE.validate_binding_documents(binding, self.schema))
        self.assertIn("source.commit has invalid format", errors)
        self.assertIn("sql.namespace must equal", errors)
        self.assertIn("canonical namespace pattern", errors)
        self.assertIn("metadata.sql_namespace and sql.namespace differ", errors)

    def test_unknown_fields_and_incomplete_source_closure_are_rejected(self) -> None:
        binding = copy.deepcopy(self.binding)
        binding["spec"]["source"]["branch"] = "main"
        del binding["spec"]["source"]["schema_sha256"]
        errors = "\n".join(MODULE.validate_binding_documents(binding, self.schema))
        self.assertIn("source keys differ", errors)
        self.assertIn("source.schema_sha256 has invalid format", errors)

    def test_duplicate_json_members_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"kind":"one","kind":"two"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key: kind"):
                MODULE.load_json(path)

    def test_source_checkout_digest_and_semantics_are_bound(self) -> None:
        binding = copy.deepcopy(self.binding)
        source_policy = {
            "$schema": "./hardening-fleet.v1.schema.json",
            "api_version": "ores.dev/fleet-hardening/v1",
            "kind": "FleetHardeningPolicy",
            "metadata": {"name": "ores-fleet-hardening", "version": "1.0.0"},
            "spec": {
                "sql": {
                    "authority": "organization-local-with-central-mirror",
                    "namespace_pattern": "^[a-z][a-z0-9_]{0,62}$",
                    "migration_registry": "declarative-migrations/declarative-postgres-migrate.rs",
                    "diesel_model": "code-first",
                    "seaorm_model": "database-first",
                },
                "kubernetes": {
                    "cluster_repository": "ORESoftware/k8s-cluster",
                    "shared_library_repository": "ORESoftware/k8s-libs-and-shared-defs",
                    "deployment_model": "gitops",
                },
                "repository": {
                    "binding_path": ".ores/repository-hardening.v1.json",
                    "fail_closed": True,
                },
                "supply_chain": {
                    "source_revision_required": True,
                    "content_sha256_required": True,
                },
            },
        }
        source_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
        }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "config"
            config.mkdir()
            policy_bytes = (json.dumps(source_policy, indent=2) + "\n").encode()
            schema_bytes = (json.dumps(source_schema, indent=2) + "\n").encode()
            (config / "hardening-fleet.v1.json").write_bytes(policy_bytes)
            (config / "hardening-fleet.v1.schema.json").write_bytes(schema_bytes)
            binding["spec"]["source"]["policy_sha256"] = hashlib.sha256(policy_bytes).hexdigest()
            binding["spec"]["source"]["schema_sha256"] = hashlib.sha256(schema_bytes).hexdigest()

            self.assertEqual(
                MODULE.verify_source_documents(
                    binding,
                    root,
                    binding["spec"]["source"]["commit"],
                ),
                [],
            )

            source_policy["spec"]["sql"]["diesel_model"] = "database-first"
            policy_bytes = (json.dumps(source_policy, indent=2) + "\n").encode()
            (config / "hardening-fleet.v1.json").write_bytes(policy_bytes)
            binding["spec"]["source"]["policy_sha256"] = hashlib.sha256(policy_bytes).hexdigest()
            errors = MODULE.verify_source_documents(
                binding,
                root,
                binding["spec"]["source"]["commit"],
            )
            self.assertIn(
                "source policy semantics differ from the organization binding",
                errors,
            )

    def test_source_path_escape_and_commit_substitution_are_rejected(self) -> None:
        binding = copy.deepcopy(self.binding)
        binding["spec"]["source"]["policy_path"] = "../policy.json"
        errors = MODULE.validate_binding_documents(binding, self.schema)
        self.assertTrue(any("source.policy_path" in error for error in errors))

        with tempfile.TemporaryDirectory() as directory:
            source_errors = MODULE.verify_source_documents(
                self.binding,
                Path(directory),
                "0" * 40,
            )
        self.assertIn("source checkout commit does not match the binding", source_errors)


if __name__ == "__main__":
    unittest.main()
