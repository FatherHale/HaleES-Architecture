"""Public tests for the HaleES-56 reference behavior.

Run from the repository root:
    python reference/halees_56/test_reference_behavior.py

These tests validate public example behavior only. They are not production HaleES tests.
"""

from __future__ import annotations

from agent_registry import validate_registry
from policy_gate import WorkRequest, evaluate_request
from router import route_signal


def assert_decision(request: WorkRequest, expected: str, expected_binary: int) -> None:
    decision = evaluate_request(request)
    assert decision.decision == expected, (request.description, decision)
    assert decision.binary == expected_binary, (request.description, decision)


def test_registry_count() -> None:
    validate_registry()


def test_call_off_routes_to_coverage() -> None:
    routed = route_signal("Server called off before dinner rush. Need call-off coverage.")
    names = {agent.name for agent in routed}
    assert "Call-Off Coverage Agent" in names


def test_guest_refund_requires_review() -> None:
    assert_decision(
        WorkRequest(
            description="Guest complaint requests a refund after a service failure.",
            requested_agent="Guest Recovery Agent",
            actor_role="shift_lead",
            risk_level="high",
            has_ground_truth=True,
            asks_to_execute=True,
            contains_private_data=True,
            requires_manager_approval=True,
        ),
        expected="review",
        expected_binary=0,
    )


def test_stale_inventory_blocks_prep_change() -> None:
    assert_decision(
        WorkRequest(
            description="Prep list needs adjustment but inventory count is stale.",
            requested_agent="Prep Production Agent",
            actor_role="manager",
            risk_level="medium",
            has_ground_truth=False,
        ),
        expected="block",
        expected_binary=0,
    )


def test_low_risk_task_passes() -> None:
    assert_decision(
        WorkRequest(
            description="Low-risk closing checklist follow-up.",
            requested_agent="Task Management Agent",
            actor_role="manager",
            risk_level="low",
            has_ground_truth=True,
        ),
        expected="pass",
        expected_binary=1,
    )


def main() -> None:
    test_registry_count()
    test_call_off_routes_to_coverage()
    test_guest_refund_requires_review()
    test_stale_inventory_blocks_prep_change()
    test_low_risk_task_passes()
    print("All HaleES-56 public reference tests passed.")


if __name__ == "__main__":
    main()
