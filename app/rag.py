import json
from pathlib import Path


DATA_PATH = Path("data/faq_data.json")


def load_faq_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def simple_retrieve(query: str, top_k: int = 3):
    faq_data = load_faq_data()
    query_words = query.split()

    scored = []
    for item in faq_data:
        score = 0
        combined_text = f"{item['question']} {item['answer']}"
        for word in query_words:
            if word in combined_text:
                score += 1
        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = [item for score, item in scored if score > 0][:top_k]
    return results


def format_context(retrieved_docs):
    if not retrieved_docs:
        return "관련 문서를 찾지 못했습니다."

    chunks = []
    for idx, doc in enumerate(retrieved_docs, start=1):
        chunks.append(
            f"[문서 {idx}]\n질문: {doc['question']}\n답변: {doc['answer']}\n카테고리: {doc['category']}"
        )
    return "\n\n".join(chunks)