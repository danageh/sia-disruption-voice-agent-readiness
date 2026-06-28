# Agent Logic Map

## Workflow

Direct SIA-booked customers affected by Typhoon Jangmi retimed flights, focused on refund and reaccommodation triage.

## Agent Role

The agent acts as a disruption triage layer.

It helps affected customers:

- confirm whether their flight was affected
- understand the new flight timing
- confirm whether they booked directly with SIA
- identify whether they want refund guidance, reaccommodation guidance, or human support
- provide the information needed for follow-up
- get routed to the right next step

The agent does not independently approve refunds, confirm rebooking, make compensation decisions, or handle policy exceptions.

## Core Conversation Flow

| Step | Agent Action | Purpose |
|---|---|---|
| 1. Identify the issue | Ask what the customer needs help with | Classify the intent |
| 2. Collect key details | Ask for flight number, travel date, booking reference, and route | Confirm whether the customer is in scope |
| 3. Check disruption event | Look up whether the flight is affected by the known retiming event | Avoid giving generic or stale advice |
| 4. Check booking channel | Ask whether the booking was made directly with SIA, through a travel agent, or through another airline | Route the customer correctly |
| 5. Identify preferred outcome | Ask whether the customer wants to travel, rebook, refund, or speak to a human | Determine next-step path |
| 6. Give safe guidance | Explain the next step based on verified information | Help the customer move forward |
| 7. Escalate if needed | Transfer to human support with a structured summary | Avoid repeated discovery |

## Intent Map

| Intent | Example Customer Request | Required Information | Tool / Data Needed | Agent Response Boundary | Escalate When |
|---|---|---|---|---|---|
| Flight status check | Is SQ622 still flying today? | Flight number, travel date | Flight status lookup | Confirm whether the flight is affected and share verified timing | Flight data unavailable or customer disputes timing |
| Retimed flight explanation | Why is my flight now tomorrow? | Flight number, route, travel date | Disruption advisory / flight status | Explain that the flight was retimed due to weather disruption, using verified source language | Customer asks for compensation or downstream loss |
| Refund path guidance | Can I get a refund? | Booking reference, booking channel, ticket status if available | Booking lookup, refund policy source | Explain refund path and what information is needed | Customer asks for final approval, exception, refund amount, or payment timeline not available |
| Reaccommodation request | Can you put me on another flight? | Booking reference, route, preferred arrival time, urgency | Booking lookup, availability lookup if available | Capture preference and route to support or digital follow-up | Multiple passenger itinerary, missed connection, urgent travel, no available options, or customer needs final confirmation |
| Booking-channel routing | I booked through Expedia. Can SIA refund me? | Booking source | Booking lookup or customer confirmation | Explain that third-party bookings may need to go through the original seller | Customer insists SIA should override or booking source is unclear |
| Missed connection / downstream impact | I will miss my next flight. | Connecting flight, separate ticket or same itinerary, timing | Booking lookup, itinerary details | Collect details and escalate with urgency | Any onward connection, hotel, visa, medical, work-critical, or family-impact issue |
| Human support request | I need to talk to someone. | Reason for escalation, booking details | Case creation / transfer tool | Offer transfer and summarize issue | Always escalate if customer clearly requests human support |
| Unclear or incomplete details | My Japan flight changed. What do I do? | Flight number, route, date, booking source | Flight status lookup | Ask clarifying questions before giving advice | Customer cannot provide enough information after two attempts |
| Angry or distressed customer | This ruined my trip. I want this fixed now. | Flight, booking reference, issue, desired outcome | Case creation / transfer tool | Acknowledge issue, collect minimum details, escalate cleanly | Customer is angry, distressed, repeatedly interrupts, or asks for exception |
| Out-of-scope request | Can you compensate my hotel? | Booking details, expense type, policy context | Policy source if available | Avoid promising compensation; route to human or official claim path | Compensation, legal, insurance, medical, or exceptional costs |

## Tool / API Actions

This project uses mock tool actions to show the deployment logic. In a real deployment, these would need customer-approved integrations.

| Tool Action | Purpose | Read-only or Write | Risk |
|---|---|---|---|
| `lookup_flight_status` | Check whether a flight is affected and confirm retimed schedule | Read | Stale or unavailable flight data |
| `lookup_booking_channel` | Check whether booking was direct with SIA or third-party | Read | Customer may not know booking source; system may not return clean result |
| `lookup_ticket_context` | Check basic booking/ticket context needed for routing | Read | Agent may overinterpret eligibility |
| `create_case_summary` | Create structured notes for human follow-up | Write | Poor summaries can create rework |
| `send_next_step_link` | Send refund form, assistance form, or status link by SMS/email | Write | Wrong link or wrong customer contact detail |
| `handoff_to_human` | Transfer or queue case for human support | Write | Escalation without enough context causes repeated discovery |

## Escalation Model

Escalation should be tiered, not automatic.

The agent should first try to resolve simple, low-risk requests within its approved scope. It should escalate only when the request exceeds its authority, the data is unclear, or the customer impact requires human judgment.

| Tier | Case Type | Agent Action | Example |
|---|---|---|---|
| Tier 0: Self-serve guidance | Customer needs general information or a known next step | Provide verified guidance and relevant link or next step | Customer asks where to submit a refund request for a direct SIA booking |
| Tier 1: Assisted triage | Customer is affected and needs help deciding the next path | Collect details, identify intent, confirm booking channel, and guide to refund or reaccommodation path | Customer says their Osaka flight was retimed and asks whether they should refund or rebook |
| Tier 2: Structured human handoff | Customer needs airline review, but the case is clear enough to summarize | Create a case summary and transfer to human support or queue follow-up | Customer wants alternative flight options because the new timing no longer works |
| Tier 3: Priority escalation | Customer impact is urgent, emotional, unclear, or high-risk | Stop automation, collect minimum required details, and escalate with priority reason | Customer will miss an onward flight, has urgent travel needs, is highly distressed, or asks for compensation/exception |

## Tiering Logic

The agent should remain in Tier 0 or Tier 1 when:

- flight status can be verified
- booking channel is clear
- customer wants general guidance
- customer accepts the next step
- no exception or urgent downstream impact is raised

The agent should move to Tier 2 when:

- the customer wants reaccommodation options
- the customer’s preferred outcome requires airline review
- the case needs follow-up
- the agent has enough information to create a useful handoff

The agent should move to Tier 3 when:

- the customer asks for compensation or policy exception
- the customer has missed connection or urgent travel impact
- booking details conflict or cannot be verified
- required data lookup fails
- the customer is angry, distressed, or repeatedly interrupts
- the customer explicitly asks for a human
- the agent confidence is low after clarification

## Handoff Principle

Escalation is not treated as failure. It is part of the operating model.

The goal is to reduce repeated discovery by passing the human agent a concise summary of:

- customer intent
- affected flight
- booking channel
- preferred outcome
- urgency
- information already collected
- reason for escalation
- open questions for the human agent

## Safe Response Principles

The agent should:

- use verified flight and policy data
- avoid final approval language unless explicitly authorized
- distinguish direct bookings from third-party bookings
- explain next steps in plain language
- ask one question at a time
- escalate before the conversation becomes circular
- preserve context for the human agent

The agent should not say:

- Your refund is approved.
- You will definitely receive compensation.
- You are guaranteed a seat on another flight.
- This policy applies to every ticket.
- I can resolve this without human review.

## Final Design Decision

The agent should be designed as a controlled triage agent, not a full resolution agent.

The strongest deployment value is faster classification, safer guidance, cleaner data capture, and better handoff during a disruption event.
