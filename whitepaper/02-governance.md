# 02 — Governance

> [!IMPORTANT]
> Authority is not a feature added later. It must be part of the foundation.

## Authority Before Execution

In hospitality operations, different people have different rights.

| Role | Typical authority boundary |
| --- | --- |
| Team member | May request, report, and acknowledge |
| Shift lead | May adjust limited floor operations |
| Manager | May approve operational changes inside scope |
| General manager | May approve store-level decisions |
| Owner/operator | May define policy, budget, integrations, and automation limits |

A system that can generate a schedule does not automatically have the right to publish that schedule.

A system that can identify labor waste does not automatically have the right to cut employees.

A system that can draft a message does not automatically have the right to send it.

| Capability | Permission question |
| --- | --- |
| Generate a schedule | Can it publish the schedule? |
| Detect labor waste | Can it cut labor? |
| Draft a message | Can it send the message? |
| Identify performance concern | Can it create documentation? |
| Recommend a refund | Can it issue the refund? |

## Authority Does Not Override Core Policy

> [!WARNING]
> A high-authority user can still make a request the system must refuse.

HaleES separates authority from permission.

A general manager may have authority over a store. That does not mean the general manager can override labor law, safety policy, wage rules, minor restrictions, privacy rules, refund controls, security controls, or required staffing ratios.

This requires a constitutional layer.

| Constitutional boundary | Public example |
| --- | --- |
| Labor law | Minor restrictions, overtime, wage rules |
| Food safety | Handling, storage, cleanliness, temperature requirements |
| Privacy | Employee, guest, and business data rules |
| Financial controls | Refund limits, payroll changes, vendor exposure |
| Security controls | Permission grants, identity, integration access |
| Service model constraints | Required staffing ratios, brand standards, safety coverage |

Authority gives a user the right to request action.

Policy decides whether that action is allowed.

## Contracts Before Tasks

A task should not be handed to an AI as a vague prompt and accepted because the response sounds good.

In this architecture, work is framed as a contract.

| Contract field | Purpose |
| --- | --- |
| Objective | Defines the work |
| Operating context | Defines the environment |
| Required inputs | Prevents missing context |
| Constraints | Makes policy enforceable |
| Role boundaries | Defines who can approve or act |
| Acceptance criteria | Defines what passing means |
| Risk level | Determines review and escalation |
| Allowed tools | Prevents unauthorized execution |
| Expected output | Prevents vague deliverables |
| Grading rules | Defines evaluation |
| Iteration limits | Prevents drift and endless retry |
| Audit requirements | Preserves traceability |

> [!TIP]
> A schedule contract should not say “make a better schedule.” It should define the store, date, approved employees, availability, labor targets, role coverage, minor restrictions, overtime limits, staffing ratios, and approval requirements.

## Governance Outcome

| Input | Gate |
| --- | --- |
| User intent | Is the request clear? |
| User role | Does this person have authority? |
| Policy | Is the action allowed? |
| Contract | Is the work bounded? |
| Risk level | Is human approval required? |
| Audit requirement | Can the decision be reconstructed later? |

[Back to reader](README.md) · [Previous: Foundation](01-foundation.md) · [Next: Constraints](03-constraints.md)
