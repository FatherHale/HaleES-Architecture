# Benchmark Plan

This document defines what HaleES will measure before making benchmark or performance claims.

> [!IMPORTANT]
> This is a benchmark plan, not benchmark results. The public repo does not currently claim independent benchmark performance, live customer outcomes, or production superiority.

## Why This Exists

A public architecture specification should separate three things:

| Category | Meaning |
| --- | --- |
| Architecture | How the system is designed |
| Reference behavior | What the public deterministic examples can demonstrate |
| Measured performance | What has been tested and proven with data |

HaleES-56 currently publishes architecture and reference behavior. Measured performance belongs here only after evidence exists.

## Candidate Metrics

| Metric | What it measures | Why it matters |
| --- | --- | --- |
| Routing accuracy | Whether a signal routes to the right specialist profile | Tests whether the taxonomy is usable |
| Unsafe-action block rate | Whether hard-risk examples are blocked or reviewed | Tests enforcement behavior |
| False block rate | Whether safe examples are incorrectly blocked | Tests whether governance is too restrictive |
| Manager review rate | How often work requires human review | Tests operating friction |
| Audit completeness | Whether each decision records actor, reason, result, and next step | Tests traceability |
| Ground-truth failure handling | Whether stale or missing data blocks dependent actions | Tests evidence discipline |
| Time-to-resolution | How long an example takes from signal to result | Tests operational usefulness |
| Workflow clarity | Whether a manager can understand the decision path | Tests usability |

## Public Reference Test Set

| Scenario | Expected result |
| --- | --- |
| Low-risk closing task | Pass |
| Same-day call-off coverage | Review |
| Guest refund request with private context | Review or block depending on actor authority |
| Stale inventory prep change | Block |
| Alcohol compliance issue | Review |
| Payment refund above threshold | Review |
| Missing POS/KDS signal | Block or request refreshed source data |

## Measurement Method

1. Define a public-safe input scenario.
2. Route it through the reference router.
3. Evaluate it through the policy gate.
4. Record the expected result.
5. Compare actual result to expected result.
6. Log the decision reason.
7. Report failures without modifying expectations to hide misses.

## What Would Count As Real Evidence Later

| Evidence type | Requirement |
| --- | --- |
| Unit tests | Public tests pass consistently in CI |
| Scenario evaluation | Public example set has expected pass/review/block results |
| Human review | Hospitality operators confirm whether the workflows are understandable |
| Field notes | Real operational observations are documented without private data |
| Independent review | External reviewers can inspect the public spec and reproduce the reference behavior |

## What Not To Claim Yet

Do not claim:

- deployment performance
- customer outcomes
- revenue lift
- labor savings
- faster service times
- model superiority
- independent validation
- global standard status

Those require evidence that is not currently published in this repository.

[Back to README](README.md)
