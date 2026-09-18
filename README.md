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