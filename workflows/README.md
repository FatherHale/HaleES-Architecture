<div align="center">

# HaleES Public Workflow Blueprints

**Hospitality workflows that show how HaleES-56 routes work through evidence, authority, approval, and audit.**

</div>

> [!IMPORTANT]
> These are public workflow blueprints. They are not private HaleES runtime logic, internal prompts, production tool routes, live integrations, customer data, or proprietary scoring weights.

## Blueprint Index

| Workflow | File | Public purpose |
| --- | --- | --- |
| Call-Off Coverage | [call-off-coverage.md](call-off-coverage.md) | Build a same-day coverage plan without auto-changing the schedule |
| Labor Cut Review | [labor-cut-review.md](labor-cut-review.md) | Block or review labor reductions that violate service coverage |
| Guest Recovery | [guest-recovery.md](guest-recovery.md) | Route complaints through recovery, policy, escalation, and audit |
| Stale Inventory Prep | [stale-inventory-prep.md](stale-inventory-prep.md) | Stop prep decisions when source evidence is stale |
| Refund Review | [refund-review.md](refund-review.md) | Route payment/refund requests through authority and audit gates |
| KDS Bottleneck Review | [kds-bottleneck-review.md](kds-bottleneck-review.md) | Convert ticket-time pressure into an operational bottleneck review |
| Payroll / Tip Exception | [payroll-tip-exception.md](payroll-tip-exception.md) | Route pay-impacting exceptions to controlled review |
| Offline Sync Reconciliation | [offline-sync-reconciliation.md](offline-sync-reconciliation.md) | Preserve safe operation during degraded connectivity |

## Shared Workflow Shape

```mermaid
%%{init:{"theme":"base","themeVariables":{"background":"#FFFFFF","fontFamily":"Marcellus, Georgia, serif","fontSize":"16px","primaryTextColor":"#0B1F4D","lineColor":"#315A92"}}}%%
flowchart LR
    A[Trigger] --> B[Agent Path]
    B --> C[Required Evidence]
    C --> D[Decision Gates]
    D --> E{Pass / Review / Block}
    E -->|Pass| F[Approved Output]
    E -->|Review| G[Human Review]
    E -->|Block| H[Missing Evidence or Policy Conflict]
    F --> I[Audit Record]
    G --> I
    H --> I

    classDef blue fill:#EEF6FF,stroke:#315A92,stroke-width:2px,color:#0B1F4D;
    classDef gold fill:#FFF7DF,stroke:#B88712,stroke-width:2px,color:#4A3200;
    classDef green fill:#EFF9F1,stroke:#278A46,stroke-width:2px,color:#0B3D16;
    classDef red fill:#FFF0F0,stroke:#C2413B,stroke-width:2px,color:#7A1111;
    class A,B,C,D,I blue;
    class E gold;
    class F green;
    class G,H red;
```

## Public Boundary

| Public here | Closed in HaleES production |
| --- | --- |
| Workflow trigger | Private event routing implementation |
| Agent path | Internal prompts and orchestration logic |
| Required evidence | Live data adapters and customer-specific policies |
| Decision gates | Proprietary scoring weights and grader implementation |
| Expected output | Production execution engine |
| Audit record shape | Hosted infrastructure and private telemetry |

[Back to README](../README.md)
