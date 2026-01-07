from fastapi import APIRouter, UploadFile, File
from fastapi import APIRouter, UploadFile, File, Body
from app.scorer import compute_alignment_score
from app.embeddings import EmbeddingModel
from app.parser import parse_resume, clean_text


from app.parser import clean_text, parse_resume, extract_text_from_pdf
from fastapi import Form



router = APIRouter()
embedder = EmbeddingModel()


@router.post("/score/text")
def score_from_text(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):
    resume_cleaned = clean_text(resume_text)
    jd_cleaned = clean_text(job_description)

    resume_sections = parse_resume(resume_cleaned)
    jd_embedding = embedder.encode(jd_cleaned)

    score = compute_alignment_score(resume_sections, jd_embedding, embedder)
    return {"alignment_score": score}


@router.post("/score/pdf")
def score_from_pdf(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume_file.file)
    jd_text = clean_text(job_description)

    resume_sections = parse_resume(resume_text)
    jd_embedding = embedder.encode(jd_text)

    score = compute_alignment_score(resume_sections, jd_embedding, embedder)
    return {"alignment_score": score}

