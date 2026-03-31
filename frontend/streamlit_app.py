import os
import sys
import tempfile
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from app.main import run_agent
from app.voice import speech_to_text, text_to_speech

st.set_page_config(
    page_title="Callow",
    page_icon="📞",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}

.main {
    background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
}

.hero-box {
    padding: 28px 32px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

.hero-title {
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 16px;
    color: #d1d5db;
}

.section-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
}

.label-title {
    font-size: 15px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 8px;
}

.result-box {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px;
    color: #111827;
    white-space: pre-wrap;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: #e0e7ff;
    color: #3730a3;
    font-size: 13px;
    font-weight: 700;
    margin-top: 4px;
}

.small-note {
    color: #6b7280;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <div class="hero-title">콜로우 (Callow)</div>
    <div class="hero-subtitle">
        실시간 음성 AI 상담 에이전트 데모 · STT/TTS · 상태 관리 · RAG · 자동 평가 구조
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="small-note">커머스 고객센터 시나리오를 기반으로 한 포트폴리오용 데모입니다.</div>',
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["텍스트 상담", "음성 상담"])

state_label_map = {
    "refund_inquiry": "환불 문의",
    "cancel_inquiry": "주문 취소 문의",
    "delivery_inquiry": "배송 문의",
    "address_change": "주소 변경 문의",
    "human_handoff": "상담원 연결",
    "general": "일반 문의"
}

with tab1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("텍스트 기반 상담")
    user_input = st.text_input(
        "질문을 입력하세요",
        placeholder="예: 환불은 얼마나 걸려요?"
    )
    run_text = st.button("상담 시작")
    st.markdown('</div>', unsafe_allow_html=True)

    if run_text and user_input.strip():
        result = run_agent(user_input)
        state_text = state_label_map.get(result["state"], result["state"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="label-title">감지된 상태</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="badge">{state_text}</div>', unsafe_allow_html=True)

            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
            st.markdown('<div class="label-title">주문번호 추출</div>', unsafe_allow_html=True)
            order_id_value = result.get("order_id") or "없음"
            st.markdown(f'<div class="result-box">{order_id_value}</div>', unsafe_allow_html=True)

            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
            st.markdown('<div class="label-title">최종 답변</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{result["answer"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="label-title">검색 컨텍스트</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{result["context"]}</div>', unsafe_allow_html=True)

            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
            st.markdown('<div class="label-title">자동 평가</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{result["evaluation"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("음성 기반 상담")
    uploaded_audio = st.file_uploader("음성 파일 업로드", type=["mp3", "wav", "m4a"])
    run_voice = st.button("음성 상담 실행")
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_audio is not None and run_voice:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(uploaded_audio.read())
            temp_audio_path = tmp_file.name

        try:
            text = speech_to_text(temp_audio_path)
            result = run_agent(text)
            state_text = state_label_map.get(result["state"], result["state"])

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="label-title">STT 결과</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{text}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="section-card">', unsafe_allow_html=True)
                st.markdown('<div class="label-title">감지된 상태</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="badge">{state_text}</div>', unsafe_allow_html=True)

                st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
                st.markdown('<div class="label-title">최종 답변</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result["answer"]}</div>', unsafe_allow_html=True)

                audio_path = text_to_speech(result["answer"], output_path="response.mp3")
                with open(audio_path, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="section-card">', unsafe_allow_html=True)
                st.markdown('<div class="label-title">검색 컨텍스트</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result["context"]}</div>', unsafe_allow_html=True)

                st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
                st.markdown('<div class="label-title">자동 평가</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result["evaluation"]}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        finally:
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)