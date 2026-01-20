from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    income: int
    state: str
    status: str   # student | working | senior

class AnalyzeRequest(BaseModel):
    policy: str
    user_profile: UserProfile

class AnalyzeResponse(BaseModel):
    summary: str
    personal_impact: dict
    explanation: list
