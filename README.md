# PromptShield

## Prompt Injection Detection and Risk Assessment System

PromptShield is a Python-based security system for detecting and assessing potential prompt injection attacks in LLM-integrated applications.

It combines machine-learning classification with rule-based detection to analyze prompts, calculate a risk score, identify attack categories, and generate a security decision.

### Security Decisions

- **ALLOW** — Low-risk prompt
- **REVIEW** — Medium-risk or suspicious prompt
- **BLOCK** — High-risk prompt

---

## Features

- Prompt injection detection using machine learning
- Rule-based detection of known attack patterns
- Unicode and obfuscation normalization
- TF-IDF feature extraction
- Logistic Regression classification
- Risk score calculation
- Attack-category detection
- Explanation of detected patterns
- FastAPI REST API
- Swagger UI for API testing
- Confusion matrix and evaluation metrics
- Automated prompt testing

---

## Detection Categories

PromptShield currently detects patterns related to:

- Instruction override
- System prompt extraction
- Role manipulation
- Context manipulation
- Indirect injection
- Obfuscation

---

## System Workflow

```text
User Prompt
     ↓
Text Preprocessing
     ↓
Rule-Based Detection
     ↓
Machine Learning Model
     ↓
Risk Score Calculation
     ↓
Security Decision
     ↓
ALLOW / REVIEW / BLOCK
## Model Performance

PromptShield was evaluated on a labeled test dataset.

| Metric | Score |
|---|---:|
| Accuracy | 95.54% |
| Precision | 95.21% |
| Recall | 97.28% |
| F1 Score | 96.24% |

### Confusion Matrix

The evaluation produced the following results:

- True Negative: 363
- False Positive: 27
- False Negative: 15
- True Positive: 537

See the evaluation output in `results/` and the documented screenshots in `documentation/screenshots/`.

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/sarkarayan1112-lab/PromptShield.git
cd PromptShield

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

## Screenshots

### Normal Prompt

![Normal DNS Prompt](documentation/screenshots/01_normal_dns.png)

### Direct Prompt Injection

![Direct Injection](documentation/screenshots/02_direct_injection.png)

### Role Manipulation

![Role Manipulation](documentation/screenshots/03_role_manipulation.png)

### Context Manipulation

![Context Manipulation](documentation/screenshots/04_context_manipulation.png)

### System Prompt Extraction

![System Prompt Extraction](documentation/screenshots/05_system_prompt_extraction.png)

### Instruction Override

![Instruction Override](documentation/screenshots/06_instruction_override.png)

### Evaluation — Confusion Matrix

![Confusion Matrix](documentation/screenshots/07_confusion_matrix.png)