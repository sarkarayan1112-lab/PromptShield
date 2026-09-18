import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT/"scripts"/"download_dataset.py")], check=True)
subprocess.run([sys.executable, str(ROOT/"src"/"train.py")], check=True)
subprocess.run([sys.executable, str(ROOT/"src"/"evaluate.py")], check=True)
print("PromptShield build complete.")
