from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.analyzer import analyze_code
from app.ai_helper import build_ai_prompt

app = FastAPI(title="CodePerfIQ API")


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def root():
    return {"message": "CodePerfIQ Backend is running!"}


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "CodePerfIQ API is healthy"
    }


@app.post("/api/analyze")
def analyze(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code input is required.")

    return analyze_code(request.code)

@app.post("/api/prompt")
def create_prompt(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code input is required.")

    analysis = analyze_code(request.code)

    prompt = build_ai_prompt(
        request.code,
        analysis["complexity"],
        analysis["bottlenecks"],
        analysis["suggestions"],
    )

    return {
        "prompt": prompt
    }