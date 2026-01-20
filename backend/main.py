from dotenv import load_dotenv
load_dotenv()
import os
print("OPENAI KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.models import AnalyzeRequest, AnalyzeResponse
from backend.services.rule_engine import budget_impact
from backend.services.policy_ai import summarize_policy

app = FastAPI(title="PolicyMirror API")

# ✅ CORS MUST BE DEFINED IMMEDIATELY AFTER APP CREATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "PolicyMirror backend running"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_policy(request: AnalyzeRequest):
    with open("backend/data/union_budget_2024.txt", "r", encoding="utf-8") as f:
        policy_text = f.read()

    summary = summarize_policy(policy_text)
    impact, explanation = budget_impact(request.user_profile)

    return {
        "summary": summary,
        "personal_impact": impact,
        "explanation": explanation
    }
