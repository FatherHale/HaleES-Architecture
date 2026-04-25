# Grader Reliability

> [!IMPORTANT]
> This document explains public reliability principles only. It does not expose the HaleES production grader, scoring prompts, private calibration data, model routing, test suites, or runtime internals.

## The Hard Question

The hard question is not whether a rubric can be written.

The hard question is whether the grading process can be trusted.

A weak grader can be gamed.

An inconsistent grader can create false confidence.

A grader with too much authority can become another uncontrolled agent.

HaleES treats grading as a governed process, not a decorative score.

## Reliability Map

| Risk | Public safeguard |
| --- | --- |
| Vague scoring | Contract defined acceptance criteria |
| Surface level compliance | Constraint adherence category |
| False confidence | Confidence tracked separately from pass or fail |
| Unclear failure | Category level feedback |
| Unsafe pass | Human review and authority boundary |
| Endless retry | Iteration limits |
| No audit trail | Decision and feedback record |

## Public Reliability Principles

A trustworthy grading system should follow several principles.

1. The contract must define what good means before execution begins.
2. The grader should evaluate against the contract, not against vague preference.
3. Each score should map back to a visible category.
4. A pass or fail decision should be derived from the score threshold.
5. Confidence should be tracked separately from pass or fail.
6. Low confidence should be able to trigger review.
7. High risk work should require stronger review than low risk work.
8. The grader should not be the only authority for actions that affect real people, money, access, scheduling, privacy, or safety.

## Human Review

Human review is not a weakness in governed systems.

Human review is part of the authority boundary.

A low risk output may pass through a normal acceptance path.

A higher risk output may need manager approval, policy review, or escalation even when the score passes.

The public rule is simple.

A score can support a decision.

A score should not automatically erase authority requirements.

## Preventing Grader Gaming

A public safe grading pattern should reduce gaming by anchoring the score to the contract.

Useful safeguards include explicit acceptance criteria, required output sections, constraint checks, category level feedback, iteration limits, and audit records.

A system should also watch for outputs that satisfy surface format while violating the actual authority boundary.

For example, an output might include every required section but still fail because it recommends an unauthorized action.

That is why constraint adherence is a separate category.

## Deterministic And Judgment Based Checks

Some checks can be deterministic.

A validator can check whether required sections exist.

A validator can check whether a grading result includes required score fields.

A validator can check whether the binary decision matches the threshold rule.

Other checks require judgment.

Quality, usefulness, privacy risk, operational fit, and escalation clarity may require a model, reviewer, policy layer, or combined method.

The public specification does not claim that the simple validators are enough for production.

They are reference tools for public shape, not the private HaleES grader.

## Public Boundary

The production HaleES grader remains proprietary.

The public repository can explain the reliability principles.

It can show examples.

It can provide simple validators.

It should not expose private scoring implementation, private calibration data, model routing, prompt chains, internal review policy, or production execution logic.

## Honest Status

The public spec defines the pattern.

The public validators check shape.

The public examples show pass and fail reasoning.

The production reliability layer is part of the closed HaleES runtime.

[Back to README](README.md)
