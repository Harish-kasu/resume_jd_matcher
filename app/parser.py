import re
import pdfplumber

def canonicalize_text(text: str) -> str:
    if not text:
        return ""

    # Normalize bullets & unicode dashes
    text = re.sub(r"[•●▪■◆▶–—−]", " ", text)

    # Lowercase
    text = text.lower()

    # Keep only letters, numbers, spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text(layout=False)
            if page_text:
                text += " " + page_text

    return canonicalize_text(text)

