# Failure Case: Labor Cut Blocked By Staffing Ratio

> [!TIP]
> The fastest way to understand HaleES is to watch it reject a bad action.

## Scenario

A manager asks HaleES to reduce labor at a luxury property during a slow period.

The agent produces a financially useful recommendation, but the plan drops front desk coverage below the required service ratio.

The recommendation may save money.

It still fails.

## Contract

| Field | Value |
| --- | --- |
| Objective | Reduce labor while preserving service coverage |
| Property type | Luxury |
| Hard staffing ratio | One front desk employee for every eight active guests |
| Action type | Staffing adjustment |
| Risk level | High |
| Approval requirement | Manager approval plus policy pass |
| Publishing permission | Not allowed unless acceptance gate passes |

## Proposed Agent Output

```json
{
  "recommendation": "Cut one front desk employee immediately.",
  "reason": "Current demand appears lower than forecast.",
  "expected_savings": "$62.00",
  "coverage_after_cut": "1 employee for 15 active guests"
}
```

## Enforcement Result

| Check | Result |
| --- | --- |
| Authority check | Pass |
| Policy check | Fail |
| Staffing ratio check | Fail |
| Ground truth check | Pass |
| Grading score | 61 |
| Binary decision | 0 |
| Final action | Blocked |

## Violated Constraint

```json
{
  "constraint": "luxury_front_desk_ratio",
  "required_ratio": "1:8",
  "proposed_ratio": "1:15",
  "severity": "high",
  "decision": 0
}
```

## Corrected Recommendation

Do not cut front desk coverage.

Review back of house prep, side work, or non guest facing labor first.

If labor pressure remains high, require manager review and document the service risk before any exception is considered.

## Audit Trace

```json
{
  "event_type": "blocked_action",
  "contract_id": "contract_labor_cut_luxury_001",
  "attempted_action": "cut_front_desk_employee",
  "blocked_by": "luxury_front_desk_ratio",
  "binary_decision": 0,
  "reason": "Proposed coverage violated hard service ratio.",
  "next_step": "revise_recommendation"
}
```

## Why This Matters

HaleES does not only generate recommendations.

It governs whether those recommendations are allowed to become action.
