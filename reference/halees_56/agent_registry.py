"""Public-safe HaleES-56 agent registry.

This module is a reference artifact for the public architecture repo.
It is not the production HaleES/Sensei OS runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AgentProfile:
    """Public metadata for one specialist capability profile."""

    id: int
    name: str
    cluster: str
    responsibility: str
    risk_level: str
    requires_human_review: bool = False


CONTROL_PLANE = "Control Plane"
UNIVERSAL_OPERATIONS = "Universal Operations"
GUEST_COMMUNICATIONS = "Guest and Communications"
LABOR_WORKFORCE = "Labor, Pay, and Workforce"
FOOD_BEVERAGE_PREP = "Food, Beverage, and Prep"
REVENUE_GROWTH = "Revenue, CRM, and Growth"
SYSTEMS_DEVICES = "Systems, Payments, and Devices"


AGENTS: tuple[AgentProfile, ...] = (
    AgentProfile(1, "Master Orchestrator Agent", CONTROL_PLANE, "Routes work and coordinates execution authority.", "high", True),
    AgentProfile(2, "Planning Agent", CONTROL_PLANE, "Turns objectives into structured plans.", "medium"),
    AgentProfile(3, "Analysis Agent", CONTROL_PLANE, "Interprets operating signals and context.", "medium"),
    AgentProfile(4, "Bottleneck Agent", CONTROL_PLANE, "Detects congestion, overload, and service pressure.", "medium"),
    AgentProfile(5, "Grading / QA Agent", CONTROL_PLANE, "Checks quality against contract requirements.", "high", True),
    AgentProfile(6, "Policy & Permission Agent", CONTROL_PLANE, "Checks RBAC, risk, scope, and approval requirements.", "high", True),
    AgentProfile(7, "Memory & Context Agent", CONTROL_PLANE, "Retrieves relevant governed context.", "high", True),
    AgentProfile(8, "Audit & Trace Agent", CONTROL_PLANE, "Records actor, decision, outcome, and trace data.", "high", True),
    AgentProfile(9, "Workflow Dispatch Agent", CONTROL_PLANE, "Dispatches approved workflow actions.", "high", True),
    AgentProfile(10, "Escalation Agent", CONTROL_PLANE, "Routes sensitive work to the right reviewer.", "high", True),
    AgentProfile(11, "Prioritization Agent", CONTROL_PLANE, "Ranks work by urgency, risk, and impact.", "medium"),
    AgentProfile(12, "Simulation / What-If Agent", CONTROL_PLANE, "Compares possible outcomes before action.", "medium"),
    AgentProfile(13, "Operations Manager Agent", UNIVERSAL_OPERATIONS, "Maintains the operating picture across a shift.", "medium"),
    AgentProfile(14, "Shift Commander Agent", UNIVERSAL_OPERATIONS, "Coordinates live-shift activity and handoffs.", "medium"),
    AgentProfile(15, "Opening Readiness Agent", UNIVERSAL_OPERATIONS, "Checks readiness to open.", "medium"),
    AgentProfile(16, "Closing Agent", UNIVERSAL_OPERATIONS, "Guides shutdown, reconciliation, and handoff.", "medium"),
    AgentProfile(17, "Standards / SOP Agent", UNIVERSAL_OPERATIONS, "Maps work to operating standards.", "medium"),
    AgentProfile(18, "Task Management Agent", UNIVERSAL_OPERATIONS, "Creates and tracks operational tasks.", "low"),
    AgentProfile(19, "Cleaning & Sanitation Agent", UNIVERSAL_OPERATIONS, "Tracks sanitation and readiness tasks.", "high", True),
    AgentProfile(20, "Maintenance Agent", UNIVERSAL_OPERATIONS, "Tracks equipment and facility issues.", "medium"),
    AgentProfile(21, "Inventory Agent", UNIVERSAL_OPERATIONS, "Tracks stock, variance, and restock needs.", "medium"),
    AgentProfile(22, "Vendor / Procurement Agent", UNIVERSAL_OPERATIONS, "Supports purchasing and vendor coordination.", "medium"),
    AgentProfile(23, "Guest Concierge Agent", GUEST_COMMUNICATIONS, "Routes guest requests to service paths.", "medium"),
    AgentProfile(24, "Guest Personalization Agent", GUEST_COMMUNICATIONS, "Uses permitted context to tailor service.", "high", True),
    AgentProfile(25, "Guest Recovery Agent", GUEST_COMMUNICATIONS, "Handles complaints and recovery options.", "high", True),
    AgentProfile(26, "VIP Agent", GUEST_COMMUNICATIONS, "Supports high-value or high-sensitivity guest scenarios.", "high", True),
    AgentProfile(27, "Reputation Agent", GUEST_COMMUNICATIONS, "Monitors reviews, sentiment, and public response needs.", "medium"),
    AgentProfile(28, "Communications Agent", GUEST_COMMUNICATIONS, "Drafts and routes internal or external messages.", "medium"),
    AgentProfile(29, "Voice / Phone Agent", GUEST_COMMUNICATIONS, "Supports calls, summaries, and voice routing.", "high", True),
    AgentProfile(30, "Accessibility & Translation Agent", GUEST_COMMUNICATIONS, "Supports translation and accessible communication.", "medium"),
    AgentProfile(31, "Scheduling Agent", LABOR_WORKFORCE, "Builds or evaluates schedules.", "high", True),
    AgentProfile(32, "Call-Off Coverage Agent", LABOR_WORKFORCE, "Responds to missed shifts and same-day coverage needs.", "high", True),
    AgentProfile(33, "Labor Cost Agent", LABOR_WORKFORCE, "Tracks labor spend and labor-risk scenarios.", "high", True),
    AgentProfile(34, "Employee Performance Agent", LABOR_WORKFORCE, "Summarizes performance and coaching signals.", "high", True),
    AgentProfile(35, "Training / Certification Agent", LABOR_WORKFORCE, "Tracks training and certification readiness.", "medium"),
    AgentProfile(36, "Recruiting / Onboarding Agent", LABOR_WORKFORCE, "Supports candidate and onboarding workflows.", "high", True),
    AgentProfile(37, "Payroll Prep Agent", LABOR_WORKFORCE, "Prepares payroll exceptions and review packets.", "high", True),
    AgentProfile(38, "Tip Pool / Employee Pay Agent", LABOR_WORKFORCE, "Supports tip pool and pay review logic.", "high", True),
    AgentProfile(39, "F&B Operations Agent", FOOD_BEVERAGE_PREP, "Coordinates food and beverage operating priorities.", "medium"),
    AgentProfile(40, "Kitchen Flow Agent", FOOD_BEVERAGE_PREP, "Detects kitchen pressure and station imbalance.", "medium"),
    AgentProfile(41, "KDS / Expo Agent", FOOD_BEVERAGE_PREP, "Interprets ticket timing and order-flow pressure.", "medium"),
    AgentProfile(42, "Menu Engineering Agent", FOOD_BEVERAGE_PREP, "Analyzes item performance and menu positioning.", "medium"),
    AgentProfile(43, "Recipe / Spec Agent", FOOD_BEVERAGE_PREP, "Tracks recipes, portions, and substitutions.", "medium"),
    AgentProfile(44, "Prep Production Agent", FOOD_BEVERAGE_PREP, "Forecasts prep needs against demand and waste.", "medium"),
    AgentProfile(45, "Waste / Variance Agent", FOOD_BEVERAGE_PREP, "Tracks waste, variance, shrink, and leakage.", "medium"),
    AgentProfile(46, "Bar / Alcohol Compliance Agent", FOOD_BEVERAGE_PREP, "Supports bar controls and alcohol compliance.", "high", True),
    AgentProfile(47, "Revenue Management Agent", REVENUE_GROWTH, "Evaluates revenue performance and demand pressure.", "medium"),
    AgentProfile(48, "Pricing / Promotions Agent", REVENUE_GROWTH, "Supports pricing and promotion decisions.", "high", True),
    AgentProfile(49, "CRM / Loyalty Agent", REVENUE_GROWTH, "Supports guest segments and loyalty engagement.", "high", True),
    AgentProfile(50, "Marketing Campaign Agent", REVENUE_GROWTH, "Drafts campaign plans and communication schedules.", "medium"),
    AgentProfile(51, "Owner / Investor Reporting Agent", REVENUE_GROWTH, "Summarizes operating performance for ownership review.", "medium"),
    AgentProfile(52, "POS / PMS / KDS Integration Agent", SYSTEMS_DEVICES, "Maps signals from operational systems.", "high", True),
    AgentProfile(53, "Payments / Billing Agent", SYSTEMS_DEVICES, "Supports payment and billing review.", "high", True),
    AgentProfile(54, "Device Lock / Kiosk Agent", SYSTEMS_DEVICES, "Supports restricted device and kiosk states.", "high", True),
    AgentProfile(55, "Offline / Edge Sync Agent", SYSTEMS_DEVICES, "Supports local continuity and sync reconciliation.", "high", True),
    AgentProfile(56, "Screen Twin / Remote Assist Agent", SYSTEMS_DEVICES, "Supports screen-state understanding and guided assist.", "high", True),
)


def all_agents() -> tuple[AgentProfile, ...]:
    return AGENTS


def agents_by_cluster(cluster: str) -> tuple[AgentProfile, ...]:
    return tuple(agent for agent in AGENTS if agent.cluster == cluster)


def find_agent(name: str) -> AgentProfile | None:
    normalized = name.strip().lower()
    for agent in AGENTS:
        if agent.name.lower() == normalized:
            return agent
    return None


def validate_registry(agents: Iterable[AgentProfile] = AGENTS) -> None:
    ids = [agent.id for agent in agents]
    if len(ids) != 56:
        raise ValueError(f"Expected 56 agents, found {len(ids)}")
    if sorted(ids) != list(range(1, 57)):
        raise ValueError("Agent IDs must be exactly 1 through 56")
