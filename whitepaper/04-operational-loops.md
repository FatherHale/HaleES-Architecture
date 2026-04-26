# 04 — Operational Loops

> [!IMPORTANT]
> A decision is not proven at approval. A decision is proven by what happened after it entered the operation.

## Post Execution Outcome Review

HaleES does not stop grading once an action is approved.

A decision can pass the contract, pass the authority check, pass the policy check, pass the grading layer, receive human approval, and still produce a bad result in the real operation.

| Before action | After action |
| --- | --- |
| Recommendation looked correct | Ticket times rose |
| Labor target was met | Guest complaints increased |
| Manager approved | Team had to call someone back |
| Forecast looked safe | Kitchen workload stayed high |
| Policy passed | Guest experience still suffered |

That outcome must be attached to the original decision.

This creates a consequence loop.

```text
Recommendation -> Approval -> Action -> Operational Result -> Outcome Review -> Future Contract Update
```

## Iteration Without Drift

AI systems often improve through iteration, but uncontrolled iteration creates drift.

| Drift risk | HaleES response |
| --- | --- |
| Model invents missing context | Contract remains the anchor |
| Output sounds complete but violates policy | Grading catches constraint failure |
| Retry loop runs too long | Iteration limit stops it |
| User pressure changes the task | Contract and authority boundary preserve scope |
| Unsafe request keeps being rephrased | Escalate, block, or refuse |

The goal is not endless generation. The goal is contract compliant completion or clear refusal and escalation.

## Operational Drift Monitoring

> [!WARNING]
> If a manager approves every recommendation without review, the system should not assume that all recommendations are good. It should recognize blind approval as a risk pattern.

HaleES must watch for drift in the operation, not only drift in the model.

| Approval drift signal | Possible response |
| --- | --- |
| Approvals happen too quickly | Slow down approval flow |
| Low-quality suggestions are repeatedly accepted | Raise review level |
| Warnings are ignored | Require reason capture |
| Exceptions become normal | Trigger calibration check |
| Nothing is ever rejected | Route certain actions to another leader |

The purpose is not to trick the manager. The purpose is to protect the operation from blind approval.

## Identity and Presence Verification

Role-based authority is not enough in a live hospitality environment.

A manager tablet can be left unlocked. A team member can use someone else's screen. A rushed supervisor can approve something without realizing which account is active.

| Risk level | Identity requirement |
| --- | --- |
| Low risk | Normal session identity may be enough |
| Medium risk | Reconfirm role or active account |
| High risk | Step-up verification required |
| Sensitive | PIN, biometric check, or second approval may be required |
| Restricted | Block or escalate |

The system should verify not only who is logged in, but whether the right person is actually present for the action.

## Emergency Mode

Hospitality operations can break normal patterns quickly.

Power outages, floods, illness outbreaks, violence, payment failures, equipment failures, weather events, and vendor breakdowns can all make normal automation unsafe.

| Emergency mode priority | Meaning |
| --- | --- |
| Human control | Reduce automation authority |
| Safety | Stabilize first |
| Clear communication | Keep team aligned |
| Documentation | Preserve the record |
| Escalation | Route risk upward |
| Simple checklists | Reduce cognitive load |

Optimization comes later.

## Audit Trails Before Trust

Trust cannot depend only on confidence. In operations, trust requires a record.

| Audit field | Purpose |
| --- | --- |
| Initiator | Who started the request |
| Active role | What authority was used |
| Contract | What governed the work |
| Data used | What evidence supported the result |
| Tool calls | What systems were touched |
| Grade | Why it passed or failed |
| Human approval | Who accepted risk |
| Final action | What actually happened |
| Outcome | What happened afterward |

Auditability is not paperwork. It is operational memory.

[Back to reader](README.md) · [Previous: Constraints](03-constraints.md) · [Next: Examples](05-examples.md)
