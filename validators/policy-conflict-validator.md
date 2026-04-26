# Policy Conflict Validator

> [!IMPORTANT]
> Authority does not override constitutional policy.

This public validator spec explains how HaleES should detect requests where a valid role attempts an action that violates a hard operating rule.

## Purpose

The policy conflict validator compares a requested action against the constitutional layer.

The constitutional layer contains rules that normal role authority cannot silently bypass.

Examples include labor law, minor restrictions, food safety policy, privacy boundaries, refund controls, security requirements, and hard staffing ratios.

## Inputs

| Input | Meaning |
| --- | --- |
| actor_role | The role requesting the action |
| requested_action | The action the user or agent wants to perform |
| policy_domain | Labor, safety, privacy, security, finance, staffing, or brand |
| constitutional_rules | Hard rules that apply above normal authority |
| override_available | Whether emergency override is allowed |
| verification_level | Required identity confirmation level |
| audit_required | Whether permanent audit is required |

## Example Rule

```json
{
  "rule_id": "minor_work_restriction",
  "policy_domain": "labor",
  "constitutional": true,
  "override_allowed": false,
  "applies_to": ["schedule_change", "shift_extension"],
  "binary_failure_on_violation": true
}
```

## Example Failure

```json
{
  "actor_role": "general_manager",
  "requested_action": "approve_minor_schedule_change",
  "violated_rule": "minor_work_restriction",
  "authority_check": "pass",
  "policy_check": "fail",
  "override_allowed": false,
  "binary_decision": 0
}
```

## Validator Behavior

| Condition | Decision |
| --- | --- |
| User lacks role authority | Fail |
| User has authority and no policy conflict exists | Pass |
| User has authority but violates constitutional policy | Fail |
| Emergency override is allowed | Require step up auth, reason, and audit |
| Emergency override is not allowed | Fail |

## Design Position

HaleES separates role authority from permission to execute.

A powerful user can still ask for an action the system must reject.

This is not a weakness in the authority model.

It is the point of the authority model.
