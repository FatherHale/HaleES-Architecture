"""
Simple public grading validator for the HaleES Architecture Specification.

This is not the HaleES production grader.
This only checks whether a public grading result includes the required visible fields.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_SCORE_FIELDS = [
    "accuracy",
    "efficiency",
    "constraint_adherence",
    "quality",
    "timeliness",
]

REQUIRED_TOP_LEVEL_FIELDS = [
    "global_score",
    "threshold",
    "binary_decision",
    "confidence",
]


def validate_grading_result(payload: dict) -> dict:
    missing = []

    scores = payload.get("category_scores", {})

    for field in REQUIRED_SCORE_FIELDS:
        if field not in scores:
            missing.append(f"category_scores.{field}")

    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in payload:
            missing.append(field)

    decision = payload.get("binary_decision")
    global_score = payload.get("global_score")
    threshold = payload.get("threshold", 85)

    decision_matches_threshold = True

    if isinstance(global_score, (int, float)) and decision in [0, 1]:
        expected = 1 if global_score >= threshold else 0
        decision_matches_threshold = decision == expected

    return {
        "valid_shape": len(missing) == 0,
        "missing_fields": missing,
        "decision_matches_threshold": decision_matches_threshold,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validators/grading_validator.py grading_result.json")
        return 2

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"File not found: {path}")
        return 2

    payload = json.loads(path.read_text(encoding="utf-8"))
    result = validate_grading_result(payload)

    if result["valid_shape"] and result["decision_matches_threshold"]:
        print("Grading result shape is valid.")
        return 0

    if not result["valid_shape"]:
        print("Grading result is missing fields:")
        for field in result["missing_fields"]:
            print(field)

    if not result["decision_matches_threshold"]:
        print("Binary decision does not match threshold rule.")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
