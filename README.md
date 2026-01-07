# Resume–Job Description Alignment Scorer

This project provides a FastAPI backend service that computes a semantic
alignment score (0–100) between a resume and a job description using
transformer-based sentence embeddings.

## Features
- Embedding-based semantic similarity
- Deterministic scoring (same input → same output)
- Section-weighted resume analysis
- FastAPI backend

## Tech Stack
- Python 3.10.11
- FastAPI
- SentenceTransformers
- PyTorch

## How to Run
1. Install dependencies  
   pip install -r requirements.txt

2. Start the server  
   uvicorn app.main:app --reload

3. Open API docs  
   http://127.0.0.1:8000/docs
