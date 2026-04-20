# HaleES Public Grading Rubric (Dual-Layer)

This document defines the public dual-layer grading model used in the HaleES Architecture Specification.

The rubric combines:

1. **Gradient scoring** (0–100) for evaluative detail
2. **Binary decision** (0|1) for enforceable pass/fail gating

---

## 1) Categories

Each output is graded across five required categories:

1. **accuracy**
   - Correctness of content versus contract requirements and inputs.
2. **efficiency**
   - Resource-consciousness and avoidance of unnecessary complexity.
3. **constraint_adherence**
   - Compliance with explicit contract constraints and boundaries.
4. **quality**
   - Clarity, structure, usability, and professional completeness.
5. **timeliness**
   - Alignment to required response window or operational tempo.

All five categories must be present for a valid grading result.

---

## 2) Scoring Range

- Each category score: **0 to 100**
- `global_score`: **0 to 100**
- `confidence`: **0.0 to 1.0** (tracked independently)

Interpretation guideline:

- 90–100: excellent
- 85–89: acceptable pass band
- 70–84: near-pass but requires revision
- below 70: insufficient

---

## 3) Global Score Calculation

Default public calculation uses equal weighting across the five categories:

\[
\text{global_score} = \text{round}\left(\frac{accuracy + efficiency + constraint\_adherence + quality + timeliness}{5}\right)
\]

Rounding method should be consistent per implementation (recommended: nearest integer).

---

## 4) Threshold and Binary Decision

Decision threshold:

- `binary_decision = 1` if `global_score >= 85`
- `binary_decision = 0` if `global_score < 85`

This threshold is the normative public baseline.

---

## 5) Confidence

`confidence` is recorded separately from pass/fail.

- Confidence does **not** override the threshold rule.
- A high confidence score cannot convert a failing global score into pass.
- A low confidence score does not automatically fail a passing output, but may trigger human review depending on policy.

---

## 6) Pass/Fail Logic

The grading model is intentionally dual-layer:

- **0–100 evaluates** the degree of quality and compliance.
- **0|1 decides** acceptance status.

Operational rule:

- No decision exists without scoring.
- No scoring matters without a decision.

This creates both explainability (why) and enforceability (what outcome).

---

## 7) Iteration Rules

When `binary_decision = 0`, system behavior should be:

1. Append specific feedback by category.
2. Re-run execution against the same contract (or a versioned amendment if approved).
3. Re-grade and re-evaluate decision.
4. Stop once pass is achieved or max iterations reached.

Default max iterations: **5**.

If max iterations are exhausted without passing, mark result as fail and escalate per local policy.

---

## 8) Required Sample Values

The following sample is included as a normative example:

- accuracy: 92
- efficiency: 88
- constraint_adherence: 96
- quality: 90
- timeliness: 94
- global_score: 92
- confidence: 0.91
- binary_decision: 1
- result: PASS

---

## 9) Sample JSON Grading Result

```json
{
  "rubric_version": "halees-dual-layer-v1",
  "category_scores": {
    "accuracy": 92,
    "efficiency": 88,
    "constraint_adherence": 96,
    "quality": 90,
    "timeliness": 94
  },
  "global_score": 92,
  "threshold": 85,
  "binary_decision": 1,
  "confidence": 0.91,
  "result": "PASS",
  "iteration": 2,
  "feedback": []
}
```

---

## 10) Sample Markdown Grading Result

```md
### Grading Result
- rubric_version: halees-dual-layer-v1
- accuracy: 92
- efficiency: 88
- constraint_adherence: 96
- quality: 90
- timeliness: 94
- global_score: 92
- threshold: 85
- binary_decision: 1
- confidence: 0.91
- result: PASS
- iteration: 2
```

---

## 11) Implementation Notes (Public Boundary)

This rubric specifies public grading semantics and reporting structure only.

It does not disclose closed-source implementation details such as internal model routing logic, proprietary grading engines, hosted enforcement internals, or production runtime infrastructure.
