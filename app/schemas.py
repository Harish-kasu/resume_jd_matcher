from pydantic import BaseModel
from typing import List

class SkillGap(BaseModel):
    matched_skills: List[str]
    missing_skills: List[str]

class ScoreResponse(BaseModel):
    alignment_score: float
    skill_gap: SkillGap
