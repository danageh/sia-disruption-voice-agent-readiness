import json
from pathlib import Path


BASE_DIR = Path(__file__).parent


def load_json(filename):
    with open(BASE_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def detect_intent(message):
    text = message.lower()

    if "human" in text or "agent" in text:
        return "human_support_request"

    if "compensate" in text or "compensation" in text or "hotel" in text:
        return "compensation_or_exception"

    if "miss" in text or "onward" in text or "connection" in text:
        return "missed_connection"

    if "another flight" in text or "put me on" in text or "rebook" in text:
        return "reaccommodation_request"

    if "refund or" in text or "refund or ask" in text:
        return "refund_or_reaccommodation_triage"

    if "travel agent" in text:
        return "booking_channel_routing"

    if "refund" in text:
        return "refund_path_guidance"

    if "still leaving" in text or "check my flight" in text or "flight still" in text:
        return "flight_status_check"

    return "unclear_details"


def lookup_flight_status(flight_number, tool_data):
    if not flight_number:
        return {
            "status": "missing_flight_number",
            "details": None
        }

    flight_details = tool_data["affected_flights"].get(flight_number)

    if not flight_details:
        return {
            "status": "not_found_in_mock_advisory",
            "details": None
        }

    return {
        "status": "affected",
        "details": flight_details
    }


def assign_escalation_tier(intent, request, flight_lookup):
    booking_channel = request.get("booking_channel")

    if intent in ["human_support_request", "missed_connection", "compensation_or_exception"]:
        return {
            "tier": "Tier 3: Priority escalation",
            "handoff_needed": True,
            "reason": "Request requires human judgment, exception handling, or urgent support."
        }

    if flight_lookup["status"] in ["missing_flight_number", "not_found_in_mock_advisory"]:
        return {
            "tier": "Tier 3: Priority escalation",
            "handoff_needed": True,
            "reason": "Flight information could not be verified in the mock advisory."
        }

    if intent == "reaccommodation_request":
        return {
            "tier": "Tier 2: Structured human handoff",
            "handoff_needed": True,
            "reason": "Customer wants alternative flight handling, which requires airline review in v1."
        }

    if intent == "refund_or_reaccommodation_triage":
        return {
            "tier": "Tier 1: Assisted triage",
            "handoff_needed": False,
            "reason": None
        }

    if intent == "booking_channel_routing" and booking_channel == "travel_agent":
        return {
            "tier": "Tier 0: Self-serve guidance",
            "handoff_needed": False,
            "reason": None
        }

    if intent in ["flight_status_check", "refund_path_guidance"]:
        return {
            "tier": "Tier 0: Self-serve guidance",
            "handoff_needed": False,
            "reason": None
        }

    return {
        "tier": "Tier 1: Assisted triage",
        "handoff_needed": False,
        "reason": None
    }


def choose_tool_action(intent, escalation, flight_lookup):
    if flight_lookup["status"] != "affected":
        return "lookup_flight_status_then_handoff"

    if escalation["tier"].startswith("Tier 3"):
        return "create_case_summary_and_priority_handoff"

    if escalation["tier"].startswith("Tier 2"):
        return "create_case_summary_for_human_review"

    if intent == "refund_path_guidance":
        return "send_refund_or_assistance_path"

    if intent == "booking_channel_routing":
        return "confirm_booking_channel_and_route_next_step"

    return "lookup_flight_status_and_guide_next_step"


def safe_agent_boundary(intent):
    boundaries = {
        "flight_status_check": "Can confirm known retimed schedule from verified advisory data.",
        "refund_path_guidance": "Can explain refund pathway, but cannot approve refund.",
        "refund_or_reaccommodation_triage": "Can help customer choose the right path, but cannot make final decision.",
        "reaccommodation_request": "Can collect preferences, but cannot confirm alternative flight.",
        "booking_channel_routing": "Can route based on booking channel, but cannot override third-party booking process.",
        "missed_connection": "Must escalate because onward travel impact needs human review.",
        "compensation_or_exception": "Must escalate because compensation and exceptions need human authority.",
        "unclear_details": "Can ask clarifying questions, then escalate if details remain unclear.",
        "flight_lookup_failure": "Must escalate if flight status cannot be verified.",
        "human_support_request": "Must escalate because customer asked for human support."
    }

    return boundaries.get(intent, "Can collect information, but should avoid final approval language.")


def create_handoff_summary(request, intent, escalation, flight_lookup):
    details = flight_lookup.get("details") or {}

    return {
        "request_id": request["request_id"],
        "customer_intent": intent,
        "flight_number": request.get("flight_number"),
        "travel_date": request.get("travel_date"),
        "route": details.get("route"),
        "known_disruption": details.get("event"),
        "booking_channel": request.get("booking_channel"),
        "escalation_tier": escalation["tier"],
        "escalation_reason": escalation["reason"],
        "customer_message": request["customer_message"],
        "open_question_for_human": "Review customer request and confirm next available action."
    }


def route_request(request, tool_data):
    intent = detect_intent(request["customer_message"])
    flight_lookup = lookup_flight_status(request.get("flight_number"), tool_data)
    escalation = assign_escalation_tier(intent, request, flight_lookup)
    tool_action = choose_tool_action(intent, escalation, flight_lookup)

    result = {
        "request_id": request["request_id"],
        "customer_message": request["customer_message"],
        "detected_intent": intent,
        "flight_lookup_status": flight_lookup["status"],
        "escalation_tier": escalation["tier"],
        "handoff_needed": escalation["handoff_needed"],
        "escalation_reason": escalation["reason"],
        "tool_action": tool_action,
        "agent_boundary": safe_agent_boundary(intent)
    }

    if escalation["handoff_needed"]:
        result["handoff_summary"] = create_handoff_summary(
            request,
            intent,
            escalation,
            flight_lookup
        )

    return result


def main():
    requests = load_json("sample_requests.json")
    tool_data = load_json("mock_tool_responses.json")

    print("SIA Disruption Voice-Agent Routing Walkthrough")
    print("=" * 52)

    for request in requests:
        result = route_request(request, tool_data)
        print(json.dumps(result, indent=2))
        print("-" * 52)


if __name__ == "__main__":
    main()
