import argparse
import sys
from pathlib import Path

import yaml


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

REQUIRED_KEYS = ["name", "environment", "replicas", "image", "port", "labels"]
ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}


def parse_args() -> Path:
    parser = argparse.ArgumentParser(
        description="Validate deployment YAML config for CI usage."
    )
    parser.add_argument("file", type=Path, help="Path to YAML config file")
    return parser.parse_args().file


def load_yaml(path: Path):
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        return None, [f"File does not exist: {path}"]
    except yaml.YAMLError as exc:
        return None, [f"Invalid YAML syntax: {exc}"]
    except OSError as exc:
        return None, [f"Could not read file: {exc}"]

    if not isinstance(data, dict):
        return None, ["Top-level YAML content must be a mapping/object"]
    return data, []


def validate_required_keys(cfg: dict) -> list[tuple[str, bool, str]]:
    checks = []
    for key in REQUIRED_KEYS:
        present = key in cfg
        checks.append((f"required key '{key}' exists", present, ""))
    return checks


def validate_types_and_ranges(cfg: dict) -> list[tuple[str, bool, str]]:
    checks = []

    if "name" in cfg:
        ok = isinstance(cfg["name"], str) and cfg["name"].strip() != ""
        checks.append(("name is non-empty string", ok, ""))

    if "environment" in cfg:
        is_string = isinstance(cfg["environment"], str)
        checks.append(("environment is string", is_string, ""))
        if is_string:
            checks.append(
                (
                    "environment is one of dev/staging/prod",
                    cfg["environment"] in ALLOWED_ENVIRONMENTS,
                    "",
                )
            )

    if "replicas" in cfg:
        is_int = isinstance(cfg["replicas"], int) and not isinstance(cfg["replicas"], bool)
        checks.append(("replicas is int", is_int, ""))
        if is_int:
            checks.append(("replicas > 0", cfg["replicas"] > 0, ""))

    if "image" in cfg:
        is_string = isinstance(cfg["image"], str) and cfg["image"].strip() != ""
        checks.append(("image is non-empty string", is_string, ""))
        if is_string:
            checks.append(("image contains tag ':'", ":" in cfg["image"], ""))

    if "port" in cfg:
        is_int = isinstance(cfg["port"], int) and not isinstance(cfg["port"], bool)
        checks.append(("port is int", is_int, ""))
        if is_int:
            checks.append(("port in range 1..65535", 1 <= cfg["port"] <= 65535, ""))

    if "labels" in cfg:
        is_dict = isinstance(cfg["labels"], dict)
        checks.append(("labels is dict", is_dict, ""))
        if is_dict:
            all_str = all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in cfg["labels"].items()
            )
            checks.append(("labels keys/values are strings", all_str, ""))

    return checks


def print_result(description: str, passed: bool) -> None:
    status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
    print(f"{status} - {description}")


def main() -> int:
    path = parse_args()
    cfg, load_errors = load_yaml(path)

    if load_errors:
        for err in load_errors:
            print_result(err, False)
        return 1

    checks = []
    checks.extend(validate_required_keys(cfg))
    checks.extend(validate_types_and_ranges(cfg))

    any_fail = False
    for description, passed, _ in checks:
        print_result(description, passed)
        if not passed:
            any_fail = True

    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())

