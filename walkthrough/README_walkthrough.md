# Python/JSON Routing Walkthrough

## Purpose

This walkthrough is not a production voice agent.

It is a small technical artifact showing how a disruption-recovery voice agent could classify customer requests, select safe next steps, and decide whether to guide, triage, or escalate.

The goal is to demonstrate deployment thinking, not software engineering depth.

## Scenario

The working scenario is direct SIA-booked customers affected by Typhoon Jangmi retimed flights, focused on refund and reaccommodation triage.

The agent is scoped as a triage layer. It does not approve refunds, confirm rebookings, decide compensation, or handle policy exceptions.

## Files

| File | Purpose |
|---|---|
| `sample_requests.json` | Ten sample customer requests across normal, ambiguous, and high-risk cases |
| `mock_tool_responses.json` | Mock flight and policy data used by the router |
| `router.py` | Simple routing walkthrough that assigns intent, tool action, escalation tier, and handoff |
| `handoff_examples.json` | Example structured summaries for human support |

## What the Router Does

For each request, the router outputs:

- detected intent
- flight lookup status
- escalation tier
- whether handoff is needed
- escalation reason
- selected tool action
- safe agent boundary
- structured handoff summary, if required

## Escalation Model

The walkthrough uses tiered escalation.

| Tier | Meaning |
|---|---|
| Tier 0: Self-serve guidance | Customer needs general information or a known next step |
| Tier 1: Assisted triage | Agent collects details and guides the customer to the right path |
| Tier 2: Structured human handoff | Human review is needed, but the case can be summarized cleanly |
| Tier 3: Priority escalation | Customer impact is urgent, emotional, unclear, or outside agent authority |

## Mock Failure Case

`REQ009` intentionally uses `SQ999` to simulate a failed flight lookup. It is not part of the real SIA advisory. It is included to show how the agent should behave when it cannot verify flight data.

## How to Run

From the `walkthrough` folder:

```bash
python router.py
```

## Design Boundaries

The agent can:

- confirm whether a known flight appears in the disruption advisory
- collect customer details
- identify intent
- guide customers to the next step
- create a structured handoff summary

The agent cannot in v1:

- approve refunds
- confirm rebooking
- decide compensation
- make policy exceptions
- resolve third-party bookings beyond routing guidance

## Deployment Point

The main deployment value is not full automation.

The value is faster triage, safer guidance, cleaner information capture, and better human handoff during disruption events.
