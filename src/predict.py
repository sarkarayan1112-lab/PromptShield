from pathlib import Path
import joblib
from .features import rule_hits
from .preprocessing import normalized_for_model

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "promptshield.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

def analyze(prompt: str):
    model = load_model()
    text = normalized_for_model(prompt)
    ml_prob = float(model.predict_proba([text])[0][1])
    categories, _ = rule_hits(prompt)
    rule_score = min(1.0, 0.22 * len(categories))
    risk = min(1.0, 0.72 * ml_prob + 0.28 * rule_score)
    if risk >= 0.75:
        decision = "BLOCK"
        level = "HIGH"
    elif risk >= 0.45:
        decision = "REVIEW"
        level = "MEDIUM"
    else:
        decision = "ALLOW"
        level = "LOW"
    return {
        "decision": decision,
        "risk_level": level,
        "risk_score": round(risk * 100, 2),
        "ml_probability": round(ml_prob * 100, 2),
        "categories": categories or ["none_detected"],
        "normalized_text": text,
    }

if __name__ == "__main__":
    import sys
    prompt = " ".join(sys.argv[1:]) or "Explain how DNS works."
    print(analyze(prompt))
