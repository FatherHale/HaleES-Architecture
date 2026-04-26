# HaleES-56 Use Cases

These use cases describe public-safe hospitality scenarios that HaleES-56 is designed to model. They are not customer case studies, production deployment claims, or benchmark results.

## How To Read These Use Cases

| Field | Meaning |
| --- | --- |
| Signal | The operational event that starts the workflow |
| Agent path | The specialist profiles likely involved |
| Gate | The governance check that decides whether work can proceed |
| Result | Pass, review, or block |
| Evidence needed | Data required before action is trusted |

## Use Case 1 — Same-Day Call-Off Coverage

| Field | Detail |
| --- | --- |
| Signal | A server calls off two hours before dinner rush |
| Agent path | Call-Off Coverage Agent → Scheduling Agent → Labor Cost Agent → Policy & Permission Agent → Communications Agent |
| Gate | Checks role eligibility, availability, overtime risk, contact permission, and manager approval need |
| Result | Usually review, because staffing outreach and schedule changes affect people and labor cost |
| Evidence needed | Current schedule, employee availability, role qualifications, labor rules, overtime state |

Expected output: a ranked coverage plan, not an automatic schedule change.

## Use Case 2 — Labor Cut Blocked By Service Ratio

| Field | Detail |
| --- | --- |
| Signal | A manager asks to cut labor to improve cost percentage |
| Agent path | Labor Cost Agent → Scheduling Agent → Policy & Permission Agent → Grading / QA Agent → Audit & Trace Agent |
| Gate | Checks whether the labor cut violates service coverage or staffing ratio constraints |
| Result | Block if the cut creates unsafe or below-standard coverage |
| Evidence needed | Forecast demand, staffing rules, role coverage, current schedule, service standard |

Expected output: a blocked action with explanation and audit trace.

## Use Case 3 — Guest Complaint Recovery

| Field | Detail |
| --- | --- |
| Signal | A guest complains about a service failure and requests compensation |
| Agent path | Guest Recovery Agent → Guest Personalization Agent → Policy & Permission Agent → Communications Agent → Escalation Agent |
| Gate | Checks refund/comp authority, privacy boundaries, tone risk, and escalation threshold |
| Result | Review when compensation, VIP sensitivity, private context, or brand risk is involved |
| Evidence needed | Guest issue summary, service record, policy limits, manager authority, prior recovery state |

Expected output: recovery options and a draft response, not unauthorized compensation.

## Use Case 4 — Stale Inventory Blocks Prep Change

| Field | Detail |
| --- | --- |
| Signal | Prep needs adjustment but inventory count is stale |
| Agent path | Prep Production Agent → Inventory Agent → Waste / Variance Agent → Kitchen Flow Agent → Grading / QA Agent |
| Gate | Checks whether inventory data is current enough to support the prep recommendation |
| Result | Block or review if inventory ground truth is missing or stale |
| Evidence needed | Current inventory count, forecast demand, prep pars, waste trend, shelf-life rules |

Expected output: request a fresh count before changing prep.

## Use Case 5 — Refund Review

| Field | Detail |
| --- | --- |
| Signal | A guest requests a refund or billing correction |
| Agent path | Payments / Billing Agent → Policy & Permission Agent → Audit & Trace Agent → Workflow Dispatch Agent or Human Manager Review |
| Gate | Checks amount, actor authority, payment policy, evidence, and audit requirement |
| Result | Pass only if within scope; otherwise review |
| Evidence needed | Transaction record, amount, reason, policy, actor role, approval threshold |

Expected output: a refund review packet and approval path.

## Use Case 6 — KDS Delay Triggers Kitchen Bottleneck Review

| Field | Detail |
| --- | --- |
| Signal | Ticket times rise above threshold during rush |
| Agent path | KDS / Expo Agent → Kitchen Flow Agent → Bottleneck Agent → Shift Commander Agent → Task Management Agent |
| Gate | Checks whether intervention requires staffing, station reassignment, or manager approval |
| Result | Pass for low-risk task routing; review for staffing or role changes |
| Evidence needed | Ticket times, station load, order volume, staffing map, current role assignments |

Expected output: bottleneck summary and recommended mitigation.

## Use Case 7 — Alcohol Compliance Escalation

| Field | Detail |
| --- | --- |
| Signal | A bar service issue raises ID, intoxication, or compliance risk |
| Agent path | Bar / Alcohol Compliance Agent → Policy & Permission Agent → Escalation Agent → Audit & Trace Agent |
| Gate | Checks legal, safety, age-sensitive, and manager escalation requirements |
| Result | Review or block, depending on the risk |
| Evidence needed | Incident notes, policy, jurisdiction rules, manager review, audit record |

Expected output: escalation and compliance record, not autonomous service authorization.

## Use Case 8 — Payroll or Tip Pool Exception

| Field | Detail |
| --- | --- |
| Signal | A payroll or tip-pool exception is detected before closeout |
| Agent path | Tip Pool / Employee Pay Agent → Payroll Prep Agent → Policy & Permission Agent → Audit & Trace Agent |
| Gate | Checks pay authority, policy, missing evidence, and approval requirement |
| Result | Review, because pay-impacting actions are sensitive |
| Evidence needed | Timecards, tip records, policy, manager approval, audit trail |

Expected output: exception packet for review.

## Use Case 9 — Offline Mode Queues Work

| Field | Detail |
| --- | --- |
| Signal | Network outage or cloud path unavailable during service |
| Agent path | Offline / Edge Sync Agent → Workflow Dispatch Agent → Audit & Trace Agent → Systems Integration Agent |
| Gate | Checks whether work can continue locally and how it must reconcile later |
| Result | Pass for safe local tasks; review or block for financial, pay, or high-risk actions |
| Evidence needed | Local state, queued events, sync status, conflict rules, audit continuity |

Expected output: queued work with later reconciliation.

## What These Use Cases Prove

They prove the architecture can be described in operational terms: signal, agent path, policy gate, evidence, and result.

They do not prove production performance, customer outcomes, or independent benchmark superiority.

[Back to README](README.md)
