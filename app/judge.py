def evaluate_answer(question: str, context: str, answer: str) -> str:
    if "상담원" in answer:
        return "정확성: 4\n관련성: 4\n정책 일치 여부: 5\n안전성: 5\n총평: fallback 응답이 적절합니다."

    if "정확한 안내를 위해" in answer:
        return "정확성: 3\n관련성: 3\n정책 일치 여부: 5\n안전성: 5\n총평: 안전한 응답이지만 정보가 부족합니다."

    return "정확성: 5\n관련성: 5\n정책 일치 여부: 5\n안전성: 5\n총평: 적절한 응답입니다."