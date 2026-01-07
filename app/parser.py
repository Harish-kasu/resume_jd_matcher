import re
import pdfplumber

def clean_text(text: str) -> str:
    """
    Clean text while preserving semantic content.
    Do NOT destroy structure aggressively.
    """
    text = text.replace("•", " ")
    text = text.replace("–", " ")
    text = text.replace("—", " ")
    text = text.lower()

    # keep words, numbers, and spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += " " + page_text
    return clean_text(text)

def parse_resume(text: str) -> dict:
    """
    Real-world safe resume parsing.
    Always returns full_text.
    Optionally extracts weak sections if detectable.
    """
    cleaned = clean_text(text)

    sections = {
        "full_text": cleaned
    }

    # Optional weak section hints (never mandatory)
    if "skill" in cleaned:
        sections["skills"] = cleaned
    if "experience" in cleaned:
        sections["experience"] = cleaned
    if "project" in cleaned:
        sections["projects"] = cleaned

    return sections
