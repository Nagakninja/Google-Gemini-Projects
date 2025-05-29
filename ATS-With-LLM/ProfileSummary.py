from typing import List
from pydantic import BaseModel, Field

class ProfileAnalysis(BaseModel):
    jd_match: str = Field(..., alias="JD Match")
    missing_keywords: List[str] = Field(..., alias="MissingKeywords")
    profile_summary: str = Field(..., alias="Profile Summary")

    class Config:
        allow_population_by_field_name = True