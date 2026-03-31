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

---

## UI/UX Design (Figma)

본 프로젝트는 기능 구현뿐만 아니라,  
실제 서비스 수준의 사용자 경험을 고려하여 Figma를 활용한 UI 설계도 함께 진행했습니다.

### 디자인 목표

- 음성 기반 상담 흐름을 직관적으로 이해할 수 있는 구조
- 상담 상태, 응답, 컨텍스트를 명확히 구분하는 정보 구조
- 실제 고객센터 UI와 유사한 경험 제공

### 주요 설계 포인트

- 상담 상태를 시각적으로 구분 (badge / 상태 표시)
- 사용자 입력 → 처리 → 응답 흐름을 단계적으로 표현
- 텍스트 상담과 음성 상담을 분리한 인터페이스 구성
- 결과 영역을 카드 형태로 구성하여 가독성 향상

### 사용 도구

- Figma (UI 설계 및 프로토타이핑)
- Figma Make 기능을 활용한 구조 설계

> 해당 디자인을 기반으로 Streamlit UI를 구현하여,  
> 기능과 사용자 경험을 함께 고려한 AI 서비스 형태로 완성했습니다.

## Design
Figma Design: https://flap-scope-84657186.figma.site


