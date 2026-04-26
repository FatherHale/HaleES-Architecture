"""Deterministic public policy gate for HaleES-56 examples.

This is not the private HaleES grader or production policy engine.
It demonstrates the public pattern: capability does not equal authority.
"""

from __future__ import annotations

from dataclasses import dataclass, field


AUTHORIZED_PRIVATE_CONTEXT_ROLES = {"manager", "owner", "admin"}
AUTHORIZED_EXECUTION_ROLES = {"manager", "owner", "admin"}


@dataclass(frozen=True)
class WorkRequest:
    """Public-safe request shape used by the reference demo."""

    description: str
    requested_agent: str
    actor_role: str
    risk_level: str
    has_ground_truth: bool = True
    asks_to_execute: bool = False
    contains_private_data: bool = False
    requires_manager_approval: bool = False
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class GateDecision:
    """Result of a public policy-gate check."""

    decision: str
    binary: int
    reason: str
    required_next_step: str


def evaluate_request(request: WorkRequest) -> GateDecision:
    """Evaluate a request against simple public governance rules.

    Decisions:
    - pass: can continue to approved workflow
    - review: needs human manager review
    - block: cannot continue without missing evidence or corrected authority
    """

    if not request.has_ground_truth:
        return GateDecision(
            decision="block",
            binary=0,
            reason="Required ground truth is missing or stale.",
            required_next_step="Refresh source data before making or dispatching the recommendation.",
        )

    if request.requires_manager_approval:
        return GateDecision(
            decision="review",
            binary=0,
            reason="The request explicitly requires manager approval.",
            required_next_step="Route to Human Manager Review.",
        )

    if request.contains_private_data and request.actor_role not in AUTHORIZED_PRIVATE_CONTEXT_ROLES:
        return GateDecision(
            decision="review",
            binary=0,
            reason="Private context is present and must be reviewed by an authorized role.",
            required_next_step="Route to an authorized manager, owner, or admin before action.",
        )

    if request.asks_to_execute and request.actor_role not in AUTHORIZED_EXECUTION_ROLES:
        return GateDecision(
            decision="review",
            binary=0,
            reason="The request attempts execution without sufficient authority.",
            required_next_step="Send to manager approval before dispatch.",
        )

    if request.risk_level == "high":
        return GateDecision(
            decision="review",
            binary=0,
            reason="The request is high-risk.",
            required_next_step="Route to Human Manager Review.",
        )

    return GateDecision(
        decision="pass",
        binary=1,
        reason="Request has required evidence and does not trigger a public review rule.",
        required_next_step="Continue to approved workflow dispatch.",
    )
