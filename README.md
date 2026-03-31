# Callow - Voice AI Agent

Callow는 커머스 고객센터 시나리오를 기반으로 설계한 음성 기반 AI 상담 에이전트입니다.  
음성 입력(STT), 상태 기반 흐름 제어, 문서 기반 응답(RAG), 음성 출력(TTS), 자동 평가 구조를 결합하여 서비스형 AI 시스템을 구현했습니다.

---

## 주요 기능

- Whisper 기반 STT (음성 → 텍스트)
- 상태 기반 상담 흐름 제어
- FAQ/정책 기반 RAG 응답
- gTTS 기반 음성 출력
- 응답 품질 평가 루틴

---

## 아키텍처

사용자 입력 → STT → 상태 분류 → 문서 검색 → 응답 생성 → TTS → 출력

---

## 기술 스택

- Python
- Streamlit
- Whisper
- gTTS
- RAG 구조

---

## 실행 방법

```bash
pip install -r requirements.txt
brew install ffmpeg
python -m streamlit run frontend/streamlit_app.py