"""
Public end to end mock loop for the HaleES Architecture Specification.

This is not the HaleES production runtime.
This is not the private Sensei control plane.
This is not the private grader.

It shows the public pattern only.

Contract
Mock execution
Mock grading
Binary decision
Feedback and iteration
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

THRESHOLD = 85
MAX_ITERATIONS = 5


@dataclass
class Contract:
    objective: str
    authority_boundary: List[str]
    required_output: List[str]
    acceptance_criteria: List[str]


@dataclass
class MockOutput:
    sections: Dict[str, str]
    notes: List[str] = field(default_factory=list)


@dataclass
class Grade:
    accuracy: int
    efficiency: int
    constraint_adherence: int
    quality: int
    timeliness: int
    confidence: float
    feedback: List[str]

    @property
    def global_score(self) -> int:
        return round(
            (
                self.accuracy
                + self.efficiency
                + self.constraint_adherence
                + self.quality
                + self.timeliness
            )
            / 5
        )

    @property
    def binary_decision(self) -> int:
        return 1 if self.global_score >= THRESHOLD else 0


def execute_mock(contract: Contract, iteration: int) -> MockOutput:
    """Return a deliberately simple mock output.

    The first iteration is incomplete.
    The second iteration improves after feedback.
    """

    if iteration == 1:
        return MockOutput(
            sections={
                "situation_summary": "A same day coverage gap exists before peak service.",
                "recommended_option": "Ask available staff to cover the gap."
            },
            notes=["Missing alternatives and escalation trigger."],
        )

    return MockOutput(
        sections={
            "situation_summary": "A same day coverage gap exists before peak service.",
            "coverage_risk": "Peak period may be under supported if no coverage plan is approved.",
            "recovery_options": "Option one is approved backup coverage. Option two is manager assisted floor support.",
            "recommended_option": "Use backup coverage first and keep manager support as the contingency.",
            "escalation_trigger": "Escalate if coverage is still open one hour before peak service."
        },
        notes=["Recommendation only. Manager approval still required."],
    )


def grade_mock(contract: Contract, output: MockOutput) -> Grade:
    """Public dummy grader.

    This uses simple visible checks only.
    It does not represent HaleES production scoring.
    """

    feedback: List[str] = []

    required_present = sum(
        1 for section in contract.required_output if section in output.sections and output.sections[section].strip()
    )
    required_ratio = required_present / len(contract.required_output)

    accuracy = round(60 + required_ratio * 35)
    quality = round(60 + required_ratio * 35)
    timeliness = 90
    efficiency = 86

    text = " ".join(output.sections.values()).lower()
    mentions_approval = "approval" in text or "approved" in text
    mentions_escalation = "escalate" in text or "escalation" in text

    constraint_adherence = 92 if mentions_approval else 70

    if required_present < len(contract.required_output):
        missing = [section for section in contract.required_output if section not in output.sections]
        feedback.append("Missing required sections: " + ", ".join(missing))

    if not mentions_approval:
        feedback.append("Clarify that recommendations do not execute without approval.")

    if not mentions_escalation:
        feedback.append("Add a measurable escalation trigger.")

    confidence = 0.78 if feedback else 0.9

    return Grade(
        accuracy=accuracy,
        efficiency=efficiency,
        constraint_adherence=constraint_adherence,
        quality=quality,
        timeliness=timeliness,
        confidence=confidence,
        feedback=feedback,
    )


def run_loop(contract: Contract) -> None:
    for iteration in range(1, MAX_ITERATIONS + 1):
        output = execute_mock(contract, iteration)
        grade = grade_mock(contract, output)

        print(f"Iteration: {iteration}")
        print(f"Global score: {grade.global_score}")
        print(f"Binary decision: {grade.binary_decision}")
        print(f"Confidence: {grade.confidence}")

        if grade.feedback:
            print("Feedback:")
            for item in grade.feedback:
                print(f"  {item}")

        if grade.binary_decision == 1:
            print("Result: PASS")
            return

        print("Result: ITERATE")
        print()

    print("Result: FAIL. Maximum iterations reached.")


if __name__ == "__main__":
    sample_contract = Contract(
        objective="Create a same day staffing recovery plan for a missed shift.",
        authority_boundary=[
            "The output may recommend actions.",
            "The output may not directly change the schedule.",
            "Manager approval is required before execution."
        ],
        required_output=[
            "situation_summary",
            "coverage_risk",
            "recovery_options",
            "recommended_option",
            "escalation_trigger",
        ],
        acceptance_criteria=[
            "Identifies the uncovered role and time window.",
            "Provides at least two recovery options.",
            "Separates recommendation from execution.",
        ],
    )

    run_loop(sample_contract)
