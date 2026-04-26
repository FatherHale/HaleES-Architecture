"""Validate public HaleES workflow blueprints.

This validator checks that every public workflow blueprint keeps the same minimum
architecture shape: trigger, agent path, evidence, gates, output, flow, and closed boundary.
It does not validate production HaleES runtime behavior.

Usage:
    python validators/workflow_blueprint_validator.py workflows
"""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SECTIONS = (
    "## Trigger",
    "## Agent Path",
    "## Required Evidence",
    "## Decision Gates",
    "## Expected Output",
    "## Public Flow",
    "## Closed Boundary",
)

REQUIRED_INDEX_LINKS = (
    "call-off-coverage.md",
    "labor-cut-review.md",
    "guest-recovery.md",
    "stale-inventory-prep.md",
    "refund-review.md",
    "kds-bottleneck-review.md",
    "payroll-tip-exception.md",
    "offline-sync-reconciliation.md",
)


def validate_blueprint(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"{path}: missing required section {section!r}")

    if "```mermaid" not in content:
        errors.append(f"{path}: missing public Mermaid flow block")

    if "not publish" not in content.lower() and "does not include" not in content.lower():
        errors.append(f"{path}: missing clear closed-boundary language")

    return errors


def validate_index(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for filename in REQUIRED_INDEX_LINKS:
        if filename not in content:
            errors.append(f"{path}: missing workflow index link for {filename}")
        if not (path.parent / filename).exists():
            errors.append(f"{path}: linked workflow file does not exist: {filename}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validators/workflow_blueprint_validator.py workflows")
        return 2

    workflow_dir = Path(sys.argv[1])
    if not workflow_dir.exists() or not workflow_dir.is_dir():
        print(f"Workflow directory not found: {workflow_dir}")
        return 2

    errors: list[str] = []
    index = workflow_dir / "README.md"
    if not index.exists():
        errors.append(f"{index}: missing workflow index README")
    else:
        errors.extend(validate_index(index))

    blueprint_files = sorted(
        path for path in workflow_dir.glob("*.md") if path.name != "README.md"
    )

    if len(blueprint_files) != len(REQUIRED_INDEX_LINKS):
        errors.append(
            f"Expected {len(REQUIRED_INDEX_LINKS)} workflow blueprints, found {len(blueprint_files)}"
        )

    for blueprint in blueprint_files:
        errors.extend(validate_blueprint(blueprint))

    if errors:
        print("Workflow blueprint validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Workflow blueprint validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
