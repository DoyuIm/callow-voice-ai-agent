from app.state_manager import detect_state, extract_order_id, needs_order_id
from app.rag import simple_retrieve, format_context
from app.llm import generate_answer
from app.judge import evaluate_answer


def run_agent(user_input: str):
    # 1. 상태 판단
    state = detect_state(user_input)

    # 2. 주문번호 추출 (🔥 이게 없어서 에러난 거)
    order_id = extract_order_id(user_input)

    # 3. 문서 검색
    retrieved = simple_retrieve(user_input, top_k=3)
    context = format_context(retrieved)

    # 4. 응답 생성
    if needs_order_id(state) and not order_id:
        answer = "해당 문의를 정확히 확인하기 위해 주문번호를 알려주세요."
    else:
        answer = generate_answer(
            question=user_input,
            state=state,
            context=context
        )

    # 5. 평가
    evaluation = evaluate_answer(
        question=user_input,
        context=context,
        answer=answer
    )

    # 6. 결과 반환
    return {
        "state": state,
        "order_id": order_id,   # ✅ 이제 정상
        "context": context,
        "answer": answer,
        "evaluation": evaluation
    }