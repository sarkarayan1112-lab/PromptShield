from pathlib import Path
import joblib
import pandas as pd
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

ROOT = Path(__file__).resolve().parents[1]
TRAIN = ROOT / "data" / "raw" / "train.csv"
TEST = ROOT / "data" / "raw" / "test.csv"
MODEL_PATH = ROOT / "models" / "promptshield.joblib"

def build_pipeline():
    features = FeatureUnion([
        ("word", TfidfVectorizer(
            analyzer="word", ngram_range=(1, 2),
            min_df=1, sublinear_tf=True, max_features=60000
        )),
        ("char", TfidfVectorizer(
            analyzer="char_wb", ngram_range=(3, 5),
            min_df=1, sublinear_tf=True, max_features=60000
        )),
    ])
    return Pipeline([
        ("features", features),
        ("classifier", LogisticRegression(max_iter=1200, class_weight="balanced"))
    ])

def main():
    train = pd.read_csv(TRAIN)
    test = pd.read_csv(TEST)
    model = build_pipeline()
    model.fit(train["text"].fillna(""), train["label"].astype(int))
    pred = model.predict(test["text"].fillna(""))
    print("Accuracy:", round(accuracy_score(test["label"], pred), 4))
    print(classification_report(test["label"], pred, digits=4))
    print("Confusion matrix:\n", confusion_matrix(test["label"], pred))
    joblib.dump(model, MODEL_PATH)
    print("Saved:", MODEL_PATH)

if __name__ == "__main__":
    main()
