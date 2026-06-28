# SIA Disruption Voice-Agent Readiness

Voice-agent deployment readiness walkthrough for SIA disruption recovery, covering workflow triage, escalation tiering, mock tool calls, and structured human handoff.

## Purpose

This project is a self-directed deployment strategy artifact. It uses a public Singapore Airlines disruption advisory as the working case and shows how a customer-facing voice agent could support disruption recovery without pretending to replace airline operations or human judgment.

The goal is to demonstrate:

- workflow diagnosis
- agent readiness assessment
- agent logic and escalation design
- basic Python/JSON routing logic
- production risk thinking
- commercial value framing

This is not a production voice agent.

## Scenario

The working scenario is direct SIA-booked customers affected by Typhoon Jangmi retimed flights, focused on refund and reaccommodation triage.

The agent is scoped as a triage layer. It does not approve refunds, confirm rebookings, decide compensation, or handle policy exceptions.

## Repository Structure

```text
sia-disruption-voice-agent-readiness/
  README.md
  docs/
    01_current_workflow_map.md
    02_voice_agent_readiness_assessment.md
    03_agent_logic_map.md
  walkthrough/
    router.py
    sample_requests.json
    mock_tool_responses.json
    handoff_examples.json
    README_walkthrough.md
```

## How to Run the Walkthrough

From the `walkthrough` folder:

```bash
python router.py
```

The script reads the sample requests, uses mock tool responses, assigns intent and escalation tier, and prints a structured routing result for each request.

## Design Thesis

The strongest use case is not full automation. The strongest use case is faster triage, safer guidance, better information capture, and cleaner human handoff during disruption events.
