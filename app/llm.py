def generate_answer(question: str, state: str, context: str) -> str:
    q = question.lower()

    if state == "refund_inquiry":
        return "환불은 결제 수단에 따라 다르며 카드 결제는 보통 영업일 기준 3~5일 정도 소요됩니다."

    elif state == "cancel_inquiry":
        return "결제 후 30분 이내이거나 배송 준비 전 상태인 경우 주문 취소가 가능합니다."

    elif state == "delivery_inquiry":
        return "일반적으로 결제 완료 후 1영업일 이내에 배송 준비가 시작됩니다. 송장 조회를 통해 확인할 수 있어요."

    elif state == "address_change":
        return "배송 준비 전 상태의 주문에 한해 주소 변경이 가능합니다."

    elif state == "human_handoff":
        return "상담원 연결을 도와드릴게요. 운영 시간은 평일 오전 9시부터 오후 6시까지입니다."

    if "환불" in q:
        return "환불은 보통 영업일 기준 3~5일 정도 소요됩니다."
    elif "배송" in q:
        return "배송은 보통 결제 후 1일 이내 시작됩니다."
    elif "취소" in q:
        return "주문 취소는 배송 준비 전까지 가능합니다."

    return "정확한 안내를 위해 상담원 연결 또는 추가 확인이 필요합니다."