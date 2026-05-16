from flashtext import KeywordProcessor
from app.skills_db import RAW_SKILLS
from app.parser import canonicalize_text

# Build once at import time (fast and deterministic)
_keyword_processor = KeywordProcessor(case_sensitive=False)

# Important: add canonical keys, but return the original skill label
# so output looks nice ("Vertex AI" instead of "vertex ai")
for skill in RAW_SKILLS:
    canon = canonicalize_text(skill)
    if canon:  # skip empty
        _keyword_processor.add_keyword(canon, skill)

def extract_skills(text: str) -> set[str]:
    """
    Deterministic skill extraction from free text using a dictionary.
    """
    can_text = canonicalize_text(text)
    found = _keyword_processor.extract_keywords(can_text)
    return set(found)

def skill_gap(resume_text: str, jd_text: str) -> dict:
    """
    Missing skills = skills found in JD but not found in resume.
    """
    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)

    return {
        "matched_skills": sorted(jd_skills & resume_skills),
        "missing_skills": sorted(jd_skills - resume_skills),
    }
