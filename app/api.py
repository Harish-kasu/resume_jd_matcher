from fastapi import APIRouter, UploadFile, File, Form
from app.embeddings import EmbeddingModel
from app.parser import canonicalize_text, extract_text_from_pdf
from app.scorer import compute_alignment_score
from app.skills import skill_gap

router = APIRouter()
embedder = EmbeddingModel()


@router.post("/score/text")
def score_text(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):
    resume = canonicalize_text(resume_text)
    jd = canonicalize_text(job_description)

    score = compute_alignment_score(resume, jd, embedder)
    skills = skill_gap(resume, jd)

    return {
        "alignment_score": score,
        "skill_gap": skills
    }

@router.post("/score/pdf")
def score_pdf(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume = extract_text_from_pdf(resume_file.file)
    jd = canonicalize_text(job_description)

    score = compute_alignment_score(resume, jd, embedder)
    skills = skill_gap(resume, jd)

    return {
        "alignment_score": score,
        "skill_gap": skills
    }

@router.post("/score/both-pdf")
def score_both_pdf(
    resume_file: UploadFile = File(...),
    jd_file: UploadFile = File(...)
):
    resume = extract_text_from_pdf(resume_file.file)
    jd = extract_text_from_pdf(jd_file.file)

    score = compute_alignment_score(resume, jd, embedder)
    skills = skill_gap(resume, jd)

    return {
        "alignment_score": score,
        "skill_gap": skills
    }

@router.post("/debug/skills")
def debug_skills(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):
    resume = canonicalize_text(resume_text)
    jd = canonicalize_text(job_description)

    from app.skills import extract_skills, skill_gap

    return {
        "resume_canonical_preview": resume[:600],
        "jd_canonical_preview": jd[:600],
        "resume_skills": sorted(extract_skills(resume_text)),
        "jd_skills": sorted(extract_skills(job_description)),
        "skill_gap": skill_gap(resume_text, job_description),
    }

