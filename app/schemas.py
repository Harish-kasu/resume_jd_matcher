from pydantic import BaseModel

class TextInput(BaseModel):
    resume_text: str
    job_description: str

class ScoreResponse(BaseModel):
    alignment_score: float
