def safe_text(text: str) -> str:
    if not text:
        return ""
    return text.strip()