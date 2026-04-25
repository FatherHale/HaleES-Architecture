# Quickstart

> [!IMPORTANT]
> This quickstart runs public reference material only. It does not run the HaleES production runtime, private grader, model routing, memory system, or execution engine.

## Start Here

| Goal | Command or file |
| --- | --- |
| See the loop move | `python reference/end_to_end_mock_loop.py` |
| Check a markdown contract | `python validators/contract_validator.py examples/staffing_recovery_contract.md` |
| Check a grading result | `python validators/grading_validator.py examples/sample_grading_result.json` |
| Inspect contract shape | `schemas/contract.schema.json` |
| Inspect grading shape | `schemas/grading_result.schema.json` |

## Run The Mock Loop

From the repository root, run this command.

```bash
python reference/end_to_end_mock_loop.py
```

The script shows the public pattern in motion.

1. Contract.
2. Mock execution.
3. Dummy grading.
4. Binary decision.
5. Feedback.
6. Iteration.
7. Pass or fail.

> [!NOTE]
> The dummy grader is intentionally simple. It is included so the public loop can be touched and tested. It is not the production HaleES grader.

## Validate A Markdown Contract Shape

From the repository root, run this command.

```bash
python validators/contract_validator.py examples/staffing_recovery_contract.md
```

This checks whether the markdown contract includes the public required sections.

It does not score the work.

It does not reproduce the HaleES runtime.

## Validate A Grading Result Shape

From the repository root, run this command.

```bash
python validators/grading_validator.py examples/sample_grading_result.json
```

This checks whether the grading result includes the required public fields and whether the binary decision matches the threshold rule.

It does not reproduce the private HaleES grader.

## Review The JSON Schemas

The schemas folder contains public JSON Schemas for the visible contract shape and grading result shape.

1. `schemas/contract.schema.json`
2. `schemas/grading_result.schema.json`

These schemas are public reference material.

They are not the private production schema system.

## Boundary

This quickstart exists so people can touch the public pattern quickly.

The production HaleES runtime, private grading implementation, private routing, private memory boundaries, and private execution engine remain closed.

[Back to README](README.md)
