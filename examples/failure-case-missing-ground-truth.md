# Failure Case: Missing External Ground Truth

> [!NOTE]
> A recommendation built on stale or missing data should not be treated the same as a recommendation built on verified ground truth.

## Scenario

A manager asks HaleES to recommend a weekend menu special based on current inventory.

The agent sees enough internal inventory data to suggest a special, but the vendor delivery status cannot be verified.

The action is blocked from final recommendation until the missing dependency is confirmed.

## Contract

| Field | Value |
| --- | --- |
| Objective | Recommend a weekend menu special |
| Data dependency | Inventory and vendor delivery status |
| External dependency | Vendor confirmation |
| Risk level | Medium |
| Publishing permission | Not allowed without verified ingredients |
| Human confirmation | Required if vendor status is unavailable |

## Proposed Agent Output

```json
{
  "recommendation": "Run a smoked brisket sandwich special.",
  "reason": "Inventory shows enough brisket and buns for expected demand.",
  "dependency_status": "vendor_delivery_unknown"
}
```

## Enforcement Result

| Check | Result |
| --- | --- |
| Authority check | Pass |
| Inventory check | Partial |
| Vendor delivery check | Fail |
| Ground truth status | Missing |
| Grading score | 72 |
| Binary decision | 0 |
| Final action | Hold for confirmation |

## Violated Constraint

```json
{
  "constraint": "verified_vendor_delivery_required",
  "required_source": "vendor_delivery_status",
  "source_status": "unavailable",
  "decision": 0
}
```

## Corrected Recommendation

Do not publish the special yet.

Ask the manager to confirm the delivery, verify ingredient quality, or choose a special based only on already verified inventory.

## Audit Trace

```json
{
  "event_type": "missing_ground_truth",
  "contract_id": "contract_menu_special_001",
  "attempted_action": "recommend_weekend_special",
  "missing_dependency": "vendor_delivery_status",
  "binary_decision": 0,
  "next_step": "require_human_confirmation_or_select_verified_inventory_only"
}
```

## Why This Matters

Hospitality does not operate in a vacuum.

Vendors, utilities, inventory systems, weather, local events, and point of sale systems can all change the truth of the operation.

HaleES must know when it does not know enough.
