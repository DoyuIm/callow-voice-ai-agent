from typing import Optional
import re


def detect_state(user_input: str) -> str:
    text = user_input.lower()

    if "취소" in text:
        return "cancel_inquiry"
    elif "환불" in text or "반품" in text:
        return "refund_inquiry"
    elif "배송" in text or "송장" in text:
        return "delivery_inquiry"
    elif "주소" in text or "배송지" in text:
        return "address_change"
    elif "상담원" in text or "사람" in text:
        return "human_handoff"
    else:
        return "general"


def needs_order_id(state: str) -> bool:
    return state in ["cancel_inquiry", "delivery_inquiry", "address_change"]


def extract_order_id(user_input: str) -> Optional[str]:
    match = re.search(r"\b\d{4,}\b", user_input)
    if match:
        return match.group(0)
    return None