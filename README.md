# HaleES Architecture Specification

![HaleES Architecture](assets/halees-architecture-header.svg)

> Public architecture specification for HaleES — an enforcement-first governance layer for reliable, auditable AI agent operations.

## Opening Thesis

**Most AI agent frameworks optimize for flexibility.**  
**HaleES optimizes for survival in production.**

If you’ve shipped agents into real operations, you already know the pattern: promising prototypes drift, authority leaks, and traceability disappears the moment they leave the lab.

This is not a tooling problem. It is a **governance problem**.

HaleES exists to solve it.

Many modern AI agent frameworks are built to maximize flexibility: connect more tools, support more prompts, chain more workflows, and allow agents to improvise across loosely bounded tasks. That flexibility can be useful for experimentation. But production operations—especially in domains where service quality, policy compliance, and accountability matter—require something stricter.

HaleES starts from a different premise: an operational AI system is only as reliable as its governance. In real environments, useful intelligence must be paired with enforceable authority boundaries, traceable decisions, explicit quality gates, and deterministic pass/fail outcomes.

In other words, HaleES is not designed around “what can an agent do?” It is designed around “what is this agent explicitly permitted to do, under which policy, with what evidence, and how do we decide if the work is acceptable?”

That is the architectural center of gravity for this specification.

## Why HaleES Exists

Organizations adopting AI often hit a recurring operational gap:

- They can generate outputs quickly.
- They cannot consistently govern execution quality.
- They cannot reliably prove why a decision passed.
- They cannot always prevent unauthorized or risky behavior from being treated as acceptable work.

In flexibility-first patterns, capability often arrives before control. In operations, that order is backwards.

HaleES exists to invert that order. It is built for environments where outputs must be:

- **bounded by policy**, not only by prompt intent;
- **scored against explicit criteria**, not judged informally;
- **accepted through a clear decision threshold**, not by default;
- **auditable after execution**, not opaque once delivered.

This architecture does not reject model capability. It contextualizes it. Intelligence remains valuable, but governance defines whether intelligence is operationally usable.

## Core Principle: Skills Are Knowledge, Not Authority

A foundational HaleES principle is simple and non-negotiable:

> Skills are knowledge. Authority is not automatic.

A skill, prompt, model, tool, or workflow does **not** gain permission just because it exists or can execute.

In HaleES, authority must come from governance signals such as:

- verified identity,
- applicable policy,
- risk classification,
- approval requirements,
- and audited execution context.

This distinction matters because many AI failures are not failures of generation—they are failures of authorization. A system can produce plausible output and still violate process, policy, or operational safety. HaleES addresses that failure mode by separating what a component **knows** from what it is **allowed** to do.

## Sensei as Orchestration/Control Plane

Within the HaleES architecture, **Sensei** is the governance and orchestration control plane.

Sensei is **not** one model.
Sensei is **not** one chat screen.
Sensei is **not** one route.
Sensei is **not** one button.

Sensei is the control layer that determines which models, tools, workflows, policies, and execution methods may be used in a given operational context.

Conceptually:

- **Models** are specialists/tools.
- **Tools** are governed capabilities.
- **Contracts** define requested work.
- **Grading** determines whether work passes.

This architecture ensures that orchestration is policy-aware rather than ad hoc. Selection and execution are not merely capability-driven; they are governance-driven.

To be explicit about boundary: the production Sensei OS runtime remains proprietary. This public repository describes architectural patterns, open contract/grading conventions, and governance principles—not the closed production internals.

## Dual-Layer Grading

HaleES evaluates work through a dual-layer grading mechanism that combines nuanced scoring with a decisive outcome.

### Layer 1: Gradient Evaluation (0–100)

Each evaluated output receives category scores from **0 to 100** across five dimensions:

1. **accuracy**
2. **efficiency**
3. **constraint_adherence**
4. **quality**
5. **timeliness**

These category scores are aggregated into a **global_score** (0–100).

### Layer 2: Binary Decision (0|1)

A binary acceptance decision is then applied:

- **binary_decision = 1** if `global_score >= 85`
- **binary_decision = 0** if `global_score < 85`

A separate **confidence** value in range 0–1 is tracked independently of pass/fail.

### Why Dual-Layer Matters

HaleES treats both layers as essential:

- **0–100 evaluates.**
- **0|1 decides.**

No decision exists without scoring.
No scoring matters without a decision.

Gradient scoring provides explainability and diagnostic granularity. Binary gating provides operational clarity and enforceable acceptance behavior.

## Contract-Driven Loop

HaleES execution follows a contract-driven loop:

1. **Orchestrator creates a contract** with objective, constraints, acceptance criteria, and expected output shape.
2. **Agent/model/tool executes** against that contract.
3. **System grades the output** using the dual-layer rubric.
4. If `binary_decision = 1`, the result is finalized.
5. If `binary_decision = 0`, feedback is appended and the task iterates.
6. **Maximum 5 iterations by default.**

This loop creates disciplined progression toward acceptable output rather than unconstrained retry behavior. Each cycle is anchored by explicit criteria and measurable improvement targets.

## Example High-Level Flow

Below is a public-safe high-level lifecycle for a governed AI task:

1. A supervisor submits a request to produce a staffing recovery plan for a same-day shift gap.
2. The orchestrator issues a structured contract with required sections, policy boundaries, and constraints.
3. A selected specialist model/tool produces a draft plan.
4. The grader scores the draft across the five categories and computes `global_score`.
5. If below threshold, the system attaches actionable feedback (e.g., missing contingency branch, incomplete escalation criteria) and re-runs iteration.
6. Once score reaches threshold, binary decision flips to pass and the output is finalized for operational use.

The important distinction is that generation alone never finalizes work. Acceptance is governance-mediated.

## How HaleES Differs from Flexibility-First Frameworks

HaleES is compatible with modern model ecosystems but differs in architectural priorities.

| Dimension | Flexibility-First Pattern (Common) | HaleES Enforcement-First Pattern |
|---|---|---|
| Primary optimization | Capability breadth and speed of experimentation | Governed execution and enforceable outcomes |
| Authority model | Often implicit or prompt-driven | Explicitly policy and identity-bound |
| Acceptance model | Informal reviewer judgment or soft heuristics | Formal dual-layer grading with pass/fail gate |
| Iteration pattern | Open-ended retries | Contract-bound loop with default max iterations |
| Audit posture | Variable, often tool-dependent | Designed for traceable scoring and decisions |
| Role of models/tools | Core drivers of behavior | Specialist components under orchestration control |
| Operational suitability | Strong for prototyping and exploration | Strong for controlled, accountable operations |

This comparison is not a critique of other frameworks; it highlights different design objectives.

## What This Public Specification Includes

This repository intentionally opens the architecture elements needed to understand and implement the HaleES governance pattern at a specification level.

Included publicly:

- contract format,
- grading rubric,
- public examples,
- skills-as-knowledge principle,
- high-level governance pattern.

These documents are designed to be implementation-oriented while remaining safe for public distribution.

## What Remains Proprietary

The following remain proprietary and are not provided in this public specification repository:

- Sensei OS production runtime,
- closed-source grader implementation,
- model routing implementation,
- command/execution engine,
- marketplace enforcement engine,
- production deployment systems,
- private datasets,
- hosted infrastructure,
- commercial HaleES product code.

This boundary is intentional: the specification is open; production runtime internals are not.

## Patent Pending Notice

Patent pending. A provisional patent application covering the grading and orchestration system was filed in November 2025.

This notice is provided for transparency about the architecture direction and does not claim a granted patent.

## Closing Statement

HaleES proposes a clear architectural stance: in operational AI systems, governance is not an accessory layer applied after generation. Governance is the system.

By separating knowledge from authority, defining work through contracts, and enforcing outcomes with dual-layer grading, HaleES offers a framework for organizations that need reliable, auditable AI execution instead of best-effort autonomy.

The goal is not less intelligence. The goal is intelligence that can be trusted in production.
