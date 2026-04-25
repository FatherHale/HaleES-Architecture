# Public Boundary

This repository is the public architecture specification for HaleES.

The purpose is to explain the governance pattern without exposing the private product runtime.

## What This Repository Is

This repository is a public description of the HaleES architecture at a specification level.

It may describe concepts such as contracts, grading, authority, privacy boundaries, local inference, cloud inference, deterministic execution, and auditability.

It may include public safe examples that show how a governed task can be structured, scored, accepted, rejected, or iterated.

## What This Repository Is Not

This repository is not the production Sensei OS runtime.

It is not the commercial HaleES codebase.

It is not a deployment guide for the hosted product.

It is not a place for private customer data, private operational data, secrets, credentials, private schemas, exact model routing logic, private memory implementation, or infrastructure details.

## Open Specification Boundary

The public specification may explain the pattern.

It may explain that work is defined by contracts.

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
