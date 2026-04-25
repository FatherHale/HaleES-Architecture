# Staffing Recovery Contract Example

This is a public safe example of the HaleES contract pattern.

## Objective

Create a same day staffing recovery plan for a missed shift.

## Context

A front of house team member called off before a dinner rush.

The manager needs a recovery plan that protects service without creating unauthorized schedule changes.

## Authority Boundary

The system may recommend actions.

The system may not directly change the schedule.

The system may not contact employees without approval.

The system may not approve overtime without manager review.

## Required Output

1. Situation summary.
2. Coverage risk.
3. Recovery options.
4. Recommended option.
5. Escalation trigger.

## Acceptance Criteria

1. The plan identifies the uncovered role and time window.
2. The plan gives at least two recovery options.
3. The plan respects role coverage and labor constraints.
4. The plan explains when a manager should intervene.
5. The plan avoids pretending that a recommendation is already approved.

## Grading Shape

Accuracy measures whether the plan understands the staffing gap.

Efficiency measures whether the plan is practical for same day use.

Constraint adherence measures whether the plan respects permission and labor limits.

Quality measures whether the plan is clear enough for a manager to use.

Timeliness measures whether the plan can be acted on before the rush.

## Decision Rule

The global score must be 85 or higher.

If the score is 85 or higher, the output can pass for manager review.

If the score is below 85, the output receives feedback and iterates.
