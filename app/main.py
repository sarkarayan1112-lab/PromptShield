from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import analyze
from src.explain import generate_explanation

app = FastAPI(title="PromptShield API", version="1.0")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {"service": "PromptShield", "status": "running"}


@app.post("/analyze")
def analyze_prompt(req: PromptRequest):
    result = analyze(req.prompt)

    explanation = generate_explanation(
        result["categories"],
        result["risk_score"],
        result["decision"]
    )

    result["explanation"] = explanation

    return result