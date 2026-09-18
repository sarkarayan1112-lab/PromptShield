from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
import joblib

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "models" / "promptshield.joblib"
TEST = ROOT / "data" / "raw" / "test.csv"
OUT = ROOT / "results"

OUT.mkdir(exist_ok=True)

# Load test data
df = pd.read_csv(TEST)

# Load trained model
model = joblib.load(MODEL)

# Make predictions
pred = model.predict(df["text"].fillna(""))

# Confusion matrix
cm = confusion_matrix(df["label"], pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["benign", "injection"]
)

disp.plot()
plt.tight_layout()
plt.savefig(OUT / "confusion_matrix.png", dpi=180)

print("Saved:", OUT / "confusion_matrix.png")

# Evaluation metrics
accuracy = accuracy_score(df["label"], pred)
precision = precision_score(df["label"], pred)
recall = recall_score(df["label"], pred)
f1 = f1_score(df["label"], pred)

print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1 Score :", round(f1 * 100, 2), "%")