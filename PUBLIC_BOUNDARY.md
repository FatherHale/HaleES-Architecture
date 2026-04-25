# Public Boundary

> [!IMPORTANT]
> This repository shares the public HaleES architecture pattern. It does not publish the production Sensei OS runtime or the commercial HaleES engine.

## What This Repository Is

This repository is the public architecture specification for HaleES.

It explains the governance pattern at a specification level.

It may describe concepts such as contracts, grading, authority, privacy boundaries, local inference, cloud inference, deterministic execution, and auditability.

It may include public safe examples that show how a governed task can be structured, scored, accepted, rejected, or iterated.

## What This Repository Is Not

This repository is not the production Sensei OS runtime.

It is not the commercial HaleES codebase.

It is not a deployment guide for the hosted product.

It is not a place for private customer data, private operational data, secrets, credentials, private schemas, exact model routing logic, private memory implementation, or infrastructure details.

## Open Specification Boundary

| Public here | Not public here |
| --- | --- |
| Contract pattern | Production contract engine |
| Public grading shape | Private grader implementation |
| Public examples | Customer data |
| Public validators | Runtime enforcement logic |
| Public diagrams | Infrastructure design |
| Public schemas | Private schema system |

The public specification may explain that work is defined by contracts.

It may explain that outputs are scored from 0 to 100.

It may explain that a binary decision accepts or rejects the output.

It may explain that authority is separate from knowledge.

It may explain that local and cloud inference can both be used.

It may explain that privacy boundaries matter.

It should not expose how the private runtime implements those ideas in production.

## Proprietary Boundary

The production Sensei OS runtime remains proprietary.

The commercial HaleES product code remains proprietary.

Private inference routing, private memory boundaries, command execution, marketplace enforcement, private datasets, hosted infrastructure, and customer specific systems remain proprietary.

## Why This Boundary Exists

HaleES benefits from having a public architecture language that builders, operators, investors, and contributors can understand.

HaleES also benefits from protecting the real product engine.

The goal is to share the principle without giving away the machine.

[Back to README](README.md)
