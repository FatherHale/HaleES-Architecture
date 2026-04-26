# Staffing Ratio Validator

> [!IMPORTANT]
> Staffing ratios become hard constraints when they define safety, service quality, legal coverage, or brand promise.

This public validator spec explains how HaleES should treat staffing ratio checks inside a contract driven workflow.

## Purpose

The staffing ratio validator compares the proposed staffing plan against the required operating ratio for the business type, property type, role, station, or service period.

A labor plan can save money and still fail if it violates the identity of the operation.

## Inputs

| Input | Meaning |
| --- | --- |
| property_type | Budget, standard, premium, luxury, quick service, full service, bar, hotel, or custom type |
| service_area | Front desk, dining room, kitchen, bar, drive thru, host stand, expo, or other service point |
| active_guest_count | Current or forecasted guest load |
| required_ratio | Minimum staffing requirement |
| proposed_staff_count | Staffing level after the proposed action |
| emergency_mode | Whether safe mode or emergency mode is active |
| override_policy | Whether override is allowed and what confirmation it requires |

## Example Rule

```json
{
  "rule_id": "luxury_front_desk_ratio",
  "property_type": "luxury",
  "service_area": "front_desk",
  "required_ratio": "1:8",
  "hard_constraint": true,
  "emergency_override_allowed": true,
  "step_up_auth_required": true,
  "audit_required": true
}
```

## Example Failure

```json
{
  "active_guest_count": 15,
  "proposed_staff_count": 1,
  "required_ratio": "1:8",
  "proposed_ratio": "1:15",
  "passes": false,
  "binary_decision": 0,
  "reason": "Proposed staffing violates luxury front desk coverage ratio."
}
```

## Validator Behavior

| Condition | Decision |
| --- | --- |
| Proposed ratio satisfies hard constraint | Pass |
| Proposed ratio violates hard constraint | Fail |
| Ratio data is missing | Fail or require human confirmation depending on risk |
| Emergency override is requested | Require reason, step up auth, and audit record |
| Emergency override is not allowed | Fail |

## Design Position

The system should not treat all labor reductions as equal.

The same cut may be acceptable in one operating model and unacceptable in another.

HaleES should evaluate staffing decisions against the service promise the business is built to deliver.
