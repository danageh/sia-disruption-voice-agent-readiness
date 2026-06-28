# Voice-Agent Readiness Assessment

## Workflow

Direct SIA-booked customers affected by Typhoon Jangmi retimed flights, focused on refund and reaccommodation triage.

## Basis of Assessment

This assessment is based on public disruption information and public refund/rebooking guidance. It does not assume access to SIA’s internal systems, policies, customer segmentation, contact-center data, or operational workflows.

The purpose is to show how I would assess whether this workflow is ready for a voice-agent pilot, what I would need to validate with the customer, and where automation should be limited.

## Deployment Recommendation

This workflow is a good candidate for a limited voice-agent pilot, but only if the agent is scoped as a triage and guidance layer.

The agent should help customers understand whether they are affected, collect the right information, explain the correct next step, and create a structured handoff when needed.

It should not independently approve refunds, make final reaccommodation decisions, or handle policy exceptions without human review.

## Readiness Assessment

| Readiness Area | Assessment | What This Means for Deployment |
|---|---|---|
| Customer intent clarity | The likely customer intents are understandable: confirm flight status, ask what changed, request refund guidance, ask about alternative flights, or seek human help. | Good fit for initial intent routing, but the project should test whether customers combine multiple issues in one call. |
| Repetition | A disruption affecting multiple flights creates repeated questions around flight changes, refund path, booking channel, and next steps. | Good fit for automation because the agent can reduce repeated explanation work. |
| Voice suitability | Voice is useful when customers are stressed, mobile, or want fast guidance. However, some choices, such as comparing alternate flights, may be better shown visually after the call. | Voice should handle triage and information capture, not force every decision into spoken conversation. |
| Data dependency | The agent would need reliable access to flight status and booking-level information to give useful answers. Without this, it should stay at general guidance only. | Data access is a launch dependency. The first customer discovery question should be: what systems can the agent safely read or update? |
| Policy dependency | Refund and rebooking guidance can be conditional. Public guidance is not enough to make final eligibility decisions. | The agent should explain pathways and collect information, but avoid final approval language unless rules are explicitly encoded and validated. |
| Booking-channel dependency | Public guidance distinguishes direct SIA bookings from travel-agent or partner-airline bookings. | The agent must identify booking channel early. If the booking was not made directly with SIA, the agent should route the customer appropriately instead of pretending it can resolve the case. |
| Tool/API readiness | A useful pilot likely needs tool calls for flight status, booking lookup, case creation, and possibly contact-detail confirmation. | If these integrations are not available, the pilot should be reduced to FAQ guidance and structured handoff. |
| Human handoff need | Some cases will need a human: unclear booking details, urgent travel impact, policy ambiguity, customer distress, missing data, or repeated misunderstanding. | Handoff is not a failure. It is part of the deployment design. The agent should pass a clean summary so the customer does not repeat everything. |
| Risk level | The main risks are stale information, wrong policy guidance, misheard booking details, and over-promising what the airline can do. | The pilot needs guardrails, confidence thresholds, transcript review, and clear escalation rules. |
| Measurement readiness | The workflow can be measured through resolution path, escalation rate, repeat contact, handling time, accuracy checks, and customer feedback. | Success should not only mean fewer human calls. It should also mean cleaner routing, fewer repeated explanations, and safer customer guidance. |

## What I Would Validate With the Customer

Before recommending production rollout, I would validate:

1. Which customer systems the agent can access.
2. Whether the agent can confirm affected flight status in real time.
3. Whether booking channel can be identified reliably.
4. Which refund and rebooking rules are safe to encode.
5. What actions the agent is allowed to complete versus only recommend.
6. When a human must take over.
7. What case notes a human agent needs after handoff.
8. How transcripts and outcomes will be reviewed after launch.

## Suitable v1 Scope

The agent can safely start with:

- confirming the affected flight
- checking whether the customer booked directly with SIA
- identifying whether the customer wants refund guidance, reaccommodation guidance, or human support
- collecting booking reference, flight number, travel date, preferred outcome, and urgency
- explaining the correct next step based on verified information
- creating a structured handoff summary for complex cases

## Out of Scope for v1

The agent should not start with:

- final refund approval
- final rebooking confirmation
- compensation decisions
- policy exceptions
- complex itinerary changes
- cases where booking or flight data cannot be verified
- third-party booking resolution beyond routing guidance

## Final Assessment

This workflow appears suitable for a voice-agent pilot because it is repetitive, time-sensitive, conversation-driven, and dependent on structured information gathering.

However, the first deployment should be deliberately limited. The strongest use case is not full automation. It is faster triage, safer routing, better information capture, and cleaner human handoff during a disruption event.
