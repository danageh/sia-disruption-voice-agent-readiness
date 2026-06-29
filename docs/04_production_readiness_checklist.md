# Production Readiness Checklist

## Workflow

Direct SIA-booked customers affected by Typhoon Jangmi retimed flights, focused on refund and reaccommodation triage.

## Purpose

This checklist shows what should be validated before moving a disruption-recovery voice agent from concept to pilot.

It does not assume access to Singapore Airlines internal systems or operating procedures. It is a deployment-readiness framework based on the public disruption scenario and the proposed v1 scope.

## Recommended v1 Scope

The v1 agent should support:

- flight disruption triage
- booking-channel identification
- refund path guidance
- reaccommodation preference capture
- structured human handoff
- safe next-step guidance

The v1 agent should not support:

- final refund approval
- final rebooking confirmation
- compensation decisions
- policy exceptions
- third-party booking resolution beyond routing guidance

These are future capability gates, not missing features.

## Readiness Checklist

| Area | Readiness Question | Why It Matters | v1 Requirement |
|---|---|---|---|
| Data access | Can the agent reliably check affected flight status? | The agent should not provide stale or unverified disruption information. | Required |
| Booking lookup | Can the agent identify whether the booking was made directly with SIA? | Direct bookings and third-party bookings require different next steps. | Required |
| Policy source | Are refund and rebooking guidance rules approved for agent use? | The agent must avoid giving final eligibility decisions without validated rules. | Required |
| Tool boundaries | Which systems can the agent read or write to? | Read-only lookup is lower risk than changing bookings or refund status. | Required |
| Human handoff | Can the agent transfer or create a case summary for human support? | Escalation should reduce repeated discovery, not restart the conversation. | Required |
| Transcript review | Can calls be reviewed for quality, accuracy, and escalation behavior? | Voice-agent performance needs monitoring after launch. | Required |
| Customer consent | Is the customer told when a case is being recorded, summarized, or handed off? | Voice workflows need clear expectations and trust. | Required |
| Failure handling | What happens when a lookup fails or data is missing? | The agent needs a safe fallback path. | Required |
| Escalation tiering | Are Tier 0, Tier 1, Tier 2, and Tier 3 paths clearly defined? | Not every issue should be escalated automatically. | Required |
| Contact update | Can the agent confirm or collect preferred callback or email details? | Follow-up is only useful if contact details are correct. | Preferred |
| Multilingual support | Does the pilot require English only or other languages? | Airline disruption support may involve international customers. | To validate |
| Latency tolerance | Can the agent respond quickly enough for a voice conversation? | Long pauses reduce customer trust and increase interruptions. | Required |
| Barge-in handling | Can the agent handle customers interrupting or correcting it? | Disrupted customers may be stressed and unlikely to follow a rigid script. | Required |
| Auditability | Are decisions, tool calls, and handoffs logged? | The customer needs to understand what the agent did and why. | Required |

## Main Production Risks

| Risk | Example | Mitigation |
|---|---|---|
| Stale flight information | Agent gives an outdated retimed schedule. | Use verified flight-status lookup and time-stamp responses. |
| Wrong booking-channel guidance | Agent tells a travel-agent customer to use a direct SIA path. | Confirm booking channel early before giving specific guidance. |
| Over-promising | Agent says a refund, rebooking, or compensation is guaranteed. | Use approved language and restrict final approval wording. |
| Weak escalation | Human agent receives poor context and repeats discovery. | Use structured handoff summaries with intent, flight, booking channel, urgency, and open questions. |
| Misheard details | Agent mishears flight number or booking reference. | Repeat critical details back for confirmation. |
| Circular conversation | Customer keeps restating the same issue. | Escalate after defined clarification attempts. |
| Tool/API failure | Flight or booking lookup is unavailable. | Move to Tier 3 handoff and explain that verification is needed. |
| Inappropriate automation | Agent tries to handle exceptions or compensation. | Keep compensation, exceptions, and final decisions out of v1. |

## Evaluation Metrics

| Metric | What It Shows |
|---|---|
| Intent classification accuracy | Whether the agent understands why the customer is calling. |
| Correct routing rate | Whether customers are sent to the right next step. |
| Escalation quality | Whether human agents receive useful context. |
| Repeat contact rate | Whether customers need to contact support again for the same issue. |
| Average handling time | Whether triage reduces support effort. |
| Containment rate | Whether low-risk requests are resolved without human handoff. |
| Policy accuracy | Whether the agent avoids incorrect refund or rebooking guidance. |
| Customer feedback | Whether customers feel guided, not blocked by automation. |
| Human-agent rework | Whether support staff need to redo information collection. |

## Suggested Pilot Guardrails

- Start with a defined disruption event rather than all airline support workflows.
- Limit the pilot to direct bookings if booking-channel data is reliable.
- Use read-only data access before enabling write actions.
- Require human review for refunds, rebooking confirmation, compensation, and exceptions.
- Review transcripts daily during the pilot.
- Track escalation summaries for completeness and usefulness.
- Expand only after the agent proves accuracy, safe routing, and customer trust.

## Future Capability Gates

These capabilities should only be considered after v1 proves reliable triage and handoff.

| Capability | Gate Before Expansion |
|---|---|
| Refund eligibility pre-check | Validated rules, approved language, and audit trail. |
| Limited refund execution | Customer-specific eligibility, payment controls, and exception handling. |
| Rebooking confirmation | Live inventory, customer consent, fare rules, and rollback path. |
| Compensation workflow | Approved claims policy, evidence requirements, and human review thresholds. |
| Policy exceptions | Clear authority model and human approval. |
| Third-party booking handling | Confirmed servicing rights and integration with original seller process. |

## Final Readiness View

The workflow is suitable for a controlled voice-agent pilot if it is scoped around triage, guidance, information capture, and structured escalation.

It is not ready for full autonomous resolution until data access, policy authority, auditability, and exception handling are validated with the customer.
