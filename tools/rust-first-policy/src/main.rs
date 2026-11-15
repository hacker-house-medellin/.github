use std::env;
use std::fs;
use std::path::Path;
use std::process::{self, Command};

const LEGACY_FILES: &[&str] = &[
    "scripts/repository_relationships_lib.py",
    "scripts/validate_baseline.py",
    "scripts/validate_fleet_hardening_binding.py",
    "scripts/validate_repository_relationships.py",
    "tests/test_fleet_hardening_binding.py",
];

const LEGACY_STEPS: &[(&str, &str)] = &[
    (".github/workflows/baseline-policy.yml", "run: python3 scripts/validate_baseline.py ."),
    (".github/workflows/repository-relationships.yml", "run: python3 scripts/validate_repository_relationships.py ."),
    (".github/workflows/fleet-hardening-binding.yml", "python3 -m json.tool policy/ores-fleet-hardening.v1.json >/dev/null"),
    (".github/workflows/fleet-hardening-binding.yml", "python3 -m json.tool policy/ores-fleet-hardening.v1.schema.json >/dev/null"),
    (".github/workflows/fleet-hardening-binding.yml", "run: python3 -m unittest discover -s tests -p 'test_fleet_hardening_binding.py'"),
    (".github/workflows/fleet-hardening-binding.yml", "run: python3 scripts/validate_fleet_hardening_binding.py --source-root .policy-source"),
];

fn python_file(path: &str) -> bool {
    path.ends_with(".py")
        && ["scripts/", "tests/", "tools/"]
            .iter()
            .any(|prefix| path.starts_with(prefix))
}

fn python_command(line: &str) -> bool {
    let text = line.trim();
    if text.starts_with('#') {
        return false;
    }
    let command = text.strip_prefix("- ").unwrap_or(text).trim();
    if command.starts_with("shell: python") {
        return true;
    }
    let command = command.strip_prefix("run:").unwrap_or(command).trim();
    command == "python"
        || command == "python3"
        || ["python ", "python3 ", "python\t", "python3\t"]
            .iter()
            .any(|prefix| command.starts_with(prefix))
}

fn check_file(path: &str) -> Result<(), String> {
    if python_file(path) && !LEGACY_FILES.contains(&path) {
        return Err(format!("new Python script or test forbidden: {path}"));
    }
    Ok(())
}

fn check_command(path: &str, line: &str) -> Result<(), String> {
    if python_command(line)
        && !LEGACY_STEPS
            .iter()
            .any(|(existing_path, existing_line)| *existing_path == path && *existing_line == line.trim())
    {
        return Err(format!("new Python command forbidden: {path}: {}", line.trim()));
    }
    Ok(())
}

fn validate(root: &Path) -> Result<(), String> {
    let output = Command::new("git")
        .arg("-C")
        .arg(root)
        .args(["ls-files", "-z", "--", "scripts", "tests", "tools", ".github/workflows"])
        .output()
        .map_err(|error| format!("cannot list tracked files: {error}"))?;
    if !output.status.success() {
        return Err("cannot enumerate tracked files; fail closed".into());
    }
    let mut failures = Vec::new();
    let mut workflow_count = 0;
    for bytes in output.stdout.split(|byte| *byte == 0).filter(|part| !part.is_empty()) {
        let path = std::str::from_utf8(bytes).map_err(|_| "non-UTF8 tracked file path")?;
        if let Err(error) = check_file(path) {
            failures.push(error);
        }
        if path.starts_with(".github/workflows/")
            && (path.ends_with(".yml") || path.ends_with(".yaml"))
        {
            workflow_count += 1;
            let source = fs::read_to_string(root.join(path))
                .map_err(|error| format!("cannot read {path}: {error}"))?;
            for (index, line) in source.lines().enumerate() {
                if let Err(error) = check_command(path, line) {
                    failures.push(format!("{error} at line {}", index + 1));
                }
            }
        }
    }
    if workflow_count == 0 {
        failures.push("no tracked workflow files found".into());
    }
    if failures.is_empty() {
        println!("Rust-first: validated {workflow_count} workflows and tracked scripts");
        Ok(())
    } else {
        Err(failures.join("\n"))
    }
}

fn main() {
    let root = env::args().nth(1).unwrap_or_else(|| ".".into());
    if let Err(error) = validate(Path::new(&root)) {
        eprintln!("{error}");
        process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rejects_new_python_script_files() {
        assert!(check_file("scripts/new_tool.py").is_err());
        assert!(check_file("tests/test_new_tool.py").is_err());
        assert!(check_file("tools/run.py").is_err());
        assert!(check_file("scripts/validate_baseline.py").is_ok());
        assert!(check_file("src/application.py").is_ok());
        assert!(check_file("tools/runner.rs").is_ok());
    }

    #[test]
    fn preserves_only_legacy_python_workflow_steps() {
        for (path, line) in LEGACY_STEPS {
            assert!(check_command(path, line).is_ok());
            assert!(check_command(".github/workflows/new.yml", line).is_err());
        }
    }

    #[test]
    fn catches_new_python_commands() {
        assert!(check_command(".github/workflows/new.yml", "shell: python").is_err());
        assert!(check_command(".github/workflows/new.yml", "run: python3 -m unittest").is_err());
        assert!(check_command(".github/workflows/new.yml", "  python3 scripts/new_tool.py").is_err());
        assert!(check_command(".github/workflows/new.yml", "run: cargo test").is_ok());
        assert!(check_command(".github/workflows/new.yml", "# python3 ignored.py").is_ok());
    }
}
