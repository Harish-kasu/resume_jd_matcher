# Resume–Job Description Alignment Scorer

A lightweight backend service that evaluates how well a resume aligns with a job description using semantic similarity and skill gap analysis.

This project exposes a simple API built with **FastAPI** that accepts resume and job description inputs (either text or PDF), computes embedding-based similarity using transformer models, and returns a normalized alignment score along with missing skills.

The goal of the project is to demonstrate how modern NLP techniques can improve resume–job matching beyond simple keyword search.

---

# Overview

Traditional resume screening systems often rely heavily on keyword matching. While simple to implement, keyword approaches struggle when resumes and job descriptions use different phrasing for the same concepts.

This project explores a semantic approach to resume matching by using transformer embeddings to capture contextual meaning in text.

The system performs the following steps:

1. Extract text from resume and job description  
2. Normalize and canonicalize the text  
3. Generate semantic embeddings using a transformer model  
4. Compute cosine similarity between the two texts  
5. Extract skills and identify gaps  

The result is a deterministic alignment score between **0 and 100** and a list of **matched and missing skills**.

---

# Features

- Semantic similarity scoring using transformer embeddings  
- Skill gap detection between resume and job description  
- Deterministic scoring (same inputs always produce the same output)  
- Support for both text input and PDF uploads  
- FastAPI backend with interactive API documentation  

---

# Tech Stack

- Python 3.10  
- FastAPI  
- SentenceTransformers  
- PyTorch  
- scikit-learn  
- pdfplumber  
- FlashText  

---

# Repository Structure

app/
├── api.py
├── embeddings.py
├── parser.py
├── scorer.py
├── skills.py
├── skills_db.py
├── schemas.py
└── main.py

requirements.txt
README.md



## File Descriptions

**main.py**  
Initializes the FastAPI application and registers the API router.

**api.py**  
Defines the API endpoints used to score resume and job description alignment. Supports both text inputs and PDF uploads.

**embeddings.py**  
Loads and manages the transformer model used to generate text embeddings.

**parser.py**  
Handles text normalization and PDF text extraction.

**scorer.py**  
Computes semantic similarity between resume and job description embeddings.

**skills.py**  
Extracts skills from text and computes the skill gap between resume and job description.

**skills_db.py**  
Contains a dictionary of supported skills used for deterministic skill extraction.

**schemas.py**  
Defines response schemas using Pydantic models.

---

# Approach

The alignment score is computed through several steps.

## 1. Text Extraction

If a resume or job description is provided as a PDF, text is extracted using **pdfplumber**.

---

## 2. Text Canonicalization

Text is normalized before processing. This step includes:

- converting text to lowercase  
- removing punctuation and special characters  
- normalizing bullet characters  
- collapsing repeated whitespace  

This helps reduce formatting noise often present in resumes and PDFs.

---

## 3. Embedding Generation

Both the resume and job description are converted into dense vector embeddings using the transformer model:

sentence-transformers/all-MiniLM-L6-v2


The model is loaded once during application startup and reused for all requests.

Embeddings are normalized to ensure stable cosine similarity comparisons.

---

## 4. Semantic Similarity

Cosine similarity is computed between the two embeddings:


alignment_score = cosine_similarity(resume_embedding, jd_embedding)


The similarity score is scaled to a **0–100 range** to make it easier to interpret.

---

## 5. Skill Gap Analysis

Skills are extracted from the resume and job description using a deterministic dictionary-based approach powered by **FlashText**.

The API then computes:

- **matched skills** (present in both resume and job description)  
- **missing skills** (present in the job description but not in the resume)

---

# API Endpoints

## Score using text input

**POST** `/score/text`

Form parameters:

resume_text
job_description


Example response:


{
  "alignment_score": 82.34,
  "skill_gap": {
    "matched_skills": ["python", "pytorch", "ml"],
    "missing_skills": ["kubernetes"]
  }
}



Score using resume PDF

POST /score/pdf

Form parameters:

resume_file
job_description

Score using both PDFs

POST /score/both-pdf

Form parameters:

resume_file
jd_file

Debug skill extraction

POST /debug/skills

Returns intermediate information including normalized text previews and detected skills.

How to Run
1. Install dependencies
pip install -r requirements.txt
2. Start the server
uvicorn app.main:app --reload
3. Open API documentation

Open the interactive API documentation in your browser:

http://127.0.0.1:8000/docs

This interface allows you to test all API endpoints directly.

Example Workflow

Upload a resume PDF or provide resume text

Provide a job description

The API extracts and normalizes text

Transformer embeddings are generated

Semantic similarity is computed

Skill overlaps and missing skills are returned

Key Design Choices
Transformer Embeddings

This project uses SentenceTransformers because they provide strong semantic representations while remaining lightweight enough to run locally.

The model all-MiniLM-L6-v2 was selected because it offers a good balance between performance and computational efficiency.

Cosine Similarity

Cosine similarity is a widely used method for comparing embedding vectors and works well for semantic similarity tasks.

Deterministic Skill Extraction

Skills are extracted using a dictionary-based approach rather than a probabilistic model. This keeps results interpretable and consistent across runs.

FastAPI Backend

FastAPI was chosen because it provides:

high performance

automatic API documentation

simple request validation

Limitations

This project is intended as a demonstration and has several limitations:

Semantic similarity alone does not fully represent candidate suitability

Dictionary-based skill extraction may miss synonyms or variations

Resume parsing quality depends on the formatting of the PDF

Future improvements could include section-aware scoring, richer skill ontologies, or model fine-tuning using hiring datasets.

Authorship and Attribution

All application code in this repository was written by Harish Kasu.

This project relies on the following open-source libraries:

FastAPI

SentenceTransformers

PyTorch

scikit-learn

pdfplumber

FlashText

No proprietary or employer-owned code is included in this repository.

Purpose of This Repository

This repository was created as a demonstration project to illustrate how semantic embeddings and simple NLP techniques can be used to evaluate resume and job description alignment.

The goal is to provide insight into code organization, model integration, and how machine learning components can be exposed through a production-style API.
