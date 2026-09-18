from pathlib import Path
import pandas as pd
from huggingface_hub import hf_hub_download

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)
repo = "neuralchemy/Prompt-injection-dataset"

for split in ["train", "test", "validation"]:
    fname = f"{split}-00000-of-00001.parquet"
    path = hf_hub_download(repo_id=repo, filename=f"core/{fname}", repo_type="dataset")
    df = pd.read_parquet(path)
    df[["text", "label"]].to_csv(RAW / f"{split}.csv", index=False)
    print(split, len(df), "rows")
