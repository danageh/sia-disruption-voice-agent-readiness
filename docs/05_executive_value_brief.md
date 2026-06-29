# Executive Value Brief

## Project

Voice-agent deployment readiness assessment for SIA disruption recovery during Typhoon Jangmi retimed flights.

## Working Scenario

Singapore Airlines published a disruption advisory for flights affected by Typhoon Jangmi. The working project scope is direct SIA-booked customers affected by retimed flights, focused on refund and reaccommodation triage.

This project does not claim access to SIA internal systems or operating procedures. It uses the public disruption case to show how a Deployment Strategist would assess voice-agent readiness, define safe scope, and connect the workflow to business value.

## Business Problem

During airline disruption events, customers often need fast answers about whether their flight changed, what options they have, whether they can request a refund, and when a human needs to help.

The support problem is not only call volume. It is repeated discovery, unclear routing, policy-sensitive guidance, emotional customers, and poor handoff quality.

A voice agent can help if it is scoped correctly. It should not try to replace airline operations or human judgment in the first release.

## Recommended v1 Deployment

Deploy a limited disruption triage voice agent for a defined disruption event and customer group.

The v1 agent should:

- confirm the affected flight
- identify the booking channel
- understand whether the customer wants refund guidance, reaccommodation guidance, or human help
- collect booking reference, travel date, flight number, preferred outcome, and urgency
- provide safe next-step guidance
- create a structured human handoff summary when needed

The v1 agent should not:

- approve refunds
- confirm rebooking
- decide compensation
- make policy exceptions
- resolve third-party bookings beyond routing guidance

## Why Voice Agent Fits This Workflow

This workflow is suitable for a voice-agent pilot because it is:

- conversation-driven
- repetitive during disruption events
- dependent on structured information gathering
- time-sensitive for customers
- measurable through routing, escalation, and resolution outcomes

However, it should not be fully automated in v1 because refund eligibility, reaccommodation, compensation, and exceptions require validated rules and human authority.

## Commercial Value

| Value Area | Expected Benefit |
|---|---|
| Customer experience | Faster first response and clearer next steps during a stressful disruption. |
| Support efficiency | Fewer repeated explanations for common disruption questions. |
| Human-agent productivity | Cleaner handoff summaries reduce repeated discovery. |
| Risk control | Policy-sensitive cases are escalated instead of over-automated. |
| Operational visibility | Structured intent and escalation data show what customers need during disruption. |
| Expansion path | Once v1 proves safe, the airline can consider deeper workflow automation. |

## Success Metrics

A successful pilot should not be measured only by call deflection.

Recommended metrics:

- percentage of calls correctly classified by intent
- percentage of customers routed to the correct next step
- quality of human handoff summaries
- reduction in repeated discovery by human agents
- repeat contact rate for the same disruption issue
- customer satisfaction after agent interaction
- policy accuracy in refund and rebooking guidance
- containment rate for low-risk requests
- escalation rate by tier

## Rollout Approach

### Phase 1: Triage and Guidance

Use the agent for flight status confirmation, booking-channel identification, refund path guidance, reaccommodation preference capture, and structured handoff.

### Phase 2: Assisted Case Creation

Allow the agent to create richer case records, send official links, collect preferred contact details, and support human follow-up.

### Phase 3: Limited Action Execution

Only after validation, consider tightly scoped actions such as refund eligibility pre-check or limited rebooking workflows.

This phase requires approved rules, reliable system access, auditability, and clear human review thresholds.

## Key Deployment Decision

The strongest use case is not full automation.

The strongest use case is controlled automation that improves triage, routing, information capture, and escalation quality during disruption events.

That is the right first deployment because it creates value without pretending the agent can safely handle every refund, rebooking, compensation, or exception case.

## Executive Summary

This workflow is a strong candidate for a limited voice-agent pilot because disruption recovery creates repeated, time-sensitive customer conversations.

The right deployment design is deliberately bounded. Start with triage, guidance, and structured handoff. Validate data access, policy rules, transcript quality, and escalation outcomes. Expand only after the agent proves it can guide customers safely and reduce operational friction without overstepping human authority.
