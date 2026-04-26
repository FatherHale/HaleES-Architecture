# 05 — Examples

> [!NOTE]
> These examples show the public pattern. They do not expose production runtime logic.

## Example 1: Call Off Handling

A team member calls off two hours before a dinner rush.

| Basic AI | Enforcement-first HaleES |
| --- | --- |
| Suggests asking someone to cover | Checks role, station, timing, eligibility, overtime, approval, and communication rules |
| Produces a message draft | Determines whether the message is allowed to be sent |
| Gives one answer | Produces ranked options, risk notes, and escalation triggers |
| Stops at the recommendation | Records the decision and follows outcome |

> [!IMPORTANT]
> The system should not blast messages or change the schedule unless authority allows it.

## Example 2: Labor Adjustment

A manager is running high labor during a slow period.

| Basic AI | Enforcement-first HaleES |
| --- | --- |
| Recommends cutting two employees | Evaluates sales, forecast, station coverage, skill mix, break rules, role permissions, fairness, minor restrictions, and staffing ratios |
| Optimizes only for labor | Protects the service model |
| Treats approval as final | Reviews outcome after action |

A recommendation might cut one cashier at a specific time if sales remain below a threshold, while refusing to cut grill or expo because prep and coverage risk remain high.

This is not just optimization. It is governed decision support.

## Example 3: Vendor Dependent Menu Decision

A restaurant wants to run a menu special based on current inventory.

| Basic AI | Enforcement-first HaleES |
| --- | --- |
| Suggests a dish from known ingredients | Verifies inventory freshness, vendor delivery, shorts, substitutions, quality, POS status, kitchen capacity, and offer language |
| Assumes stale data is acceptable | Lowers confidence or blocks when external ground truth is missing |
| Produces a creative idea | Determines whether the idea is operationally usable |

If vendor status cannot be verified, the system should lower confidence, require human confirmation, or block the recommendation depending on risk.

## Example 4: Generated Marketing Asset

A restaurant asks HaleES to create a promotional image for a burger special.

| Basic AI | Enforcement-first HaleES |
| --- | --- |
| Generates an image | Checks brand rules, offer terms, claims, likeness risk, product accuracy, and approval level |
| Optimizes for appearance | Grades for brand fit, clarity, accuracy, compliance, and publishing risk |
| Treats creation as completion | Separates generation from permission to publish |

The image may look good and still fail if it shows the wrong product, implies an unauthorized discount, uses a protected likeness, or violates the brand standard.

## Example Pattern Summary

| Workflow | Enforcement-first check |
| --- | --- |
| Scheduling | Availability, role coverage, ratios, approval |
| Shift swaps | Eligibility, overtime, policy, manager review |
| Call offs | Coverage risk, contact rules, audit trail |
| Labor cuts | Demand, safety, station coverage, outcome review |
| Guest recovery | Privacy, policy, tone, approval |
| Marketing | Brand, offer accuracy, likeness, publishing permission |

[Back to reader](README.md) · [Previous: Operational Loops](04-operational-loops.md) · [Next: Public Boundary](06-public-boundary.md)
