# HaleES Architecture Specification

![HaleES Architecture](assets/IMG_0475.jpeg)

## Get Started

This repository contains the open architecture specification for HaleES. HaleES is an enforcement first governance layer for reliable operational intelligence.

Quick actions

1. Read this full specification to understand the core philosophy, dual layer grading, contract driven execution, local first inference, cloud capable inference, and privacy first governance.
2. Explore the contract format in CONTRACT SPEC to see the public markdown structure with a hospitality example.
3. Review the grading rubric in GRADING RUBRIC to understand how outputs are scored from 0 to 100 and decided as 0 or 1.
4. Read PUBLIC BOUNDARY to understand what is open and what stays proprietary.
5. Read SECURITY to understand how to report security concerns.
6. Follow updates on X at @AskSenseiES.

Most agent frameworks chase flexibility.
HaleES is built for survival in real operations.

## Thesis

The problem is simple. A system can generate a useful answer and still be unsafe to trust.

That is why HaleES starts with governance, not generation.

In real operations, especially hospitality, the question is not only what an agent can do. The better question is what the agent is allowed to do, under which policy, with what evidence, and how the result is accepted or rejected.

HaleES exists for that gap.

It is not a chatbot for hospitality. It is a governed operational intelligence layer where models, local inference, deterministic rules, human approvals, and audited execution all work inside one control system.

## Why HaleES Exists

Organizations adopting artificial intelligence usually hit the same problem.

1. They can generate outputs quickly.
2. They cannot always govern execution quality.
3. They cannot always prove why a decision passed.
4. They cannot always stop unauthorized or risky behavior from being treated as acceptable work.

In flexible systems, capability often comes before control. In operations, that order is backwards.

HaleES is built for environments where outputs must be bounded by policy, scored against explicit criteria, accepted through a clear threshold, and auditable after execution.

The architecture does not reject model capability. It puts model capability inside authority, privacy, grading, and execution boundaries.

## Local First, Cloud Capable Intelligence

HaleES is designed as a local first, cloud capable hospitality operating system.

The system can use large language models when they are useful, but core operational authority does not depend entirely on a model. HaleES keeps durable structure under the intelligence layer. That structure includes permissions, roles, audit records, execution queues, operational state, grading contracts, tool governance, deterministic business rules, and explicit acceptance gates.

Inference can run in more than one place depending on the job.

1. Cloud inference can support heavier reasoning, long context analysis, research, cross property coordination, and high capability model routing.
2. Local or device level inference can support lower latency work, privacy sensitive workflows, offline continuity, and site specific operational support.
3. Deterministic execution can support work that should be handled by rules, scores, constraints, schemas, queues, or approved tools without needing a model at all.

This makes HaleES model flexible rather than model dependent. The model is one reasoning surface inside a governed operating system, not the whole product.

The goal is operational continuity. If cloud intelligence is available, HaleES can use it. If local inference is better, HaleES can route there. If no model is needed, HaleES can still operate through governed system logic.

## Privacy First Data Boundary

HaleES treats privacy as architecture, not decoration.

Local first intelligence supports this by allowing sensitive operational context to stay closer to the property, device, or organization when cloud processing is not necessary. Inference placement can be selected based on privacy, risk, latency, and operational need.

At a public specification level, HaleES follows three principles.

1. Minimum necessary context. Only the context needed for a task should be available to the model, tool, or workflow doing that task.
2. Governed memory boundaries. Personal, organizational, and cross organization intelligence must stay separated by policy and permission.
3. Pattern learning without exposure. Shared intelligence should improve the system through generalized patterns, not by revealing one organization private data to another.

This means HaleES can learn from operations without treating private operational data as public knowledge. Privacy, permission, and execution authority belong in the same governance layer.

## Core Principle, Skills Are Knowledge, Not Authority

A foundational HaleES principle is simple.

Skills are knowledge. Authority is not automatic.

A skill, prompt, model, tool, or workflow does not gain permission just because it exists or can execute.

In HaleES, authority must come from governance signals such as verified identity, applicable policy, risk classification, approval requirements, and audited execution context.

This matters because many failures are not failures of generation. They are failures of authorization. A system can produce plausible output and still violate process, policy, or operational safety. HaleES separates what a component knows from what it is allowed to do.

## Sensei as Orchestration and Control Plane

Within the HaleES architecture, Sensei is the governance and orchestration control plane.

Sensei is not one model. Sensei is not one chat screen. Sensei is not one route. Sensei is not one button.

Sensei is the control layer that determines which models, tools, workflows, policies, and execution methods may be used in a given operational context.

The public concept is simple.

1. Models are specialists.
2. Tools are governed capabilities.
3. Contracts define requested work.
4. Grading determines whether work passes.
5. Execution only moves forward through authority boundaries.

This keeps orchestration policy aware instead of improvised. Selection and execution are not only capability driven. They are governance driven.

The production Sensei OS runtime remains proprietary. This public repository describes architectural patterns, open contract and grading conventions, and governance principles. It does not expose closed production internals.

## Dual Layer Grading

HaleES evaluates work through a dual layer grading mechanism that combines nuanced scoring with a decisive outcome.

### Layer 1, Gradient Evaluation

Each evaluated output receives category scores from 0 to 100 across five dimensions.

1. Accuracy.
2. Efficiency.
3. Constraint adherence.
4. Quality.
5. Timeliness.

These scores are aggregated into a global score from 0 to 100.

### Layer 2, Binary Decision

A binary acceptance decision is then applied.

1. The binary decision is 1 when the global score is 85 or higher.
2. The binary decision is 0 when the global score is below 85.
3. Confidence is tracked separately from pass or fail.

HaleES treats both layers as necessary.

0 to 100 evaluates.
0 or 1 decides.

No decision exists without scoring. No scoring matters without a decision.

Gradient scoring gives explainability. Binary gating gives operational clarity.

## Contract Driven Loop

HaleES execution follows a contract driven loop.

1. The orchestrator creates a contract with objective, constraints, acceptance criteria, and expected output shape.
2. The agent, model, or tool executes against that contract.
3. The system grades the output using the dual layer rubric.
4. If the binary decision is 1, the result can be finalized.
5. If the binary decision is 0, feedback is appended and the task iterates.
6. The default maximum is five iterations.

This creates disciplined progress toward acceptable output instead of open ended retry behavior.

## Example High Level Flow

A supervisor submits a request to produce a staffing recovery plan for a same day shift gap.

The orchestrator issues a structured contract with required sections, policy boundaries, and constraints.

A selected specialist model or tool produces a draft plan.

The grader scores the draft across the five categories and computes the global score.

If the score is below threshold, the system attaches actionable feedback and runs another iteration.

Once the score reaches threshold, the binary decision flips to pass and the output is finalized for operational use.

Generation alone never finalizes work. Acceptance is governed.

## How HaleES Differs From Flexibility First Frameworks

HaleES is compatible with modern model ecosystems, but the priorities are different.

Flexibility first patterns usually optimize for capability breadth, fast experimentation, prompt driven behavior, informal acceptance, open ended retries, and provider level privacy controls.

HaleES optimizes for governed execution, explicit authority, formal grading, contract bound iteration, traceable decisions, privacy first boundaries, local or cloud inference, and deterministic operation when no model is required.

This is not a claim that every other framework is wrong. It is a different design objective. HaleES is built for controlled operations, not only exploration.

## What This Public Specification Includes

This repository opens the architecture elements needed to understand and implement the HaleES governance pattern at a specification level.

Public material includes contract format, grading rubric, public examples, the skills are knowledge principle, local first and cloud capable inference pattern, privacy first data boundary principles, and the high level governance pattern.

These documents are designed to be useful while remaining safe for public distribution.

## What Remains Proprietary

The following remain proprietary and are not provided in this public specification repository.

1. Sensei OS production runtime.
2. Closed source grader implementation.
3. Model routing implementation.
4. Local and cloud inference routing implementation.
5. Private memory boundary implementation.
6. Command and execution engine.
7. Marketplace enforcement engine.
8. Production deployment systems.
9. Private datasets.
10. Hosted infrastructure.
11. Commercial HaleES product code.

This boundary is intentional. The specification is open. The production runtime internals are not.

## Patent Pending Notice

Patent pending. A provisional patent application covering the grading and orchestration system was filed in November 2025.

This notice is provided for transparency about the architecture direction and does not claim a granted patent.

## Closing Statement

HaleES has a clear stance. In operational intelligence systems, governance is not something added after generation. Governance is the system.

By separating knowledge from authority, defining work through contracts, enforcing outcomes with dual layer grading, supporting local first and cloud capable intelligence, and treating privacy as part of execution authority, HaleES offers a framework for organizations that need reliable and auditable execution instead of best effort autonomy.

The goal is not less intelligence. The goal is intelligence that can be trusted in production.
