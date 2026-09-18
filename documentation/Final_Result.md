# PromptShield
## Prompt Injection Detection and Risk Assessment System

---

## 1. Project Overview

PromptShield is a prompt security system designed to detect and assess potentially malicious prompt injection attempts in applications that use Large Language Models (LLMs).

The system combines machine-learning-based classification with rule-based detection techniques to analyze an input prompt. It calculates a risk score and produces a security decision:

- ALLOW
- REVIEW
- BLOCK

PromptShield also provides a FastAPI-based REST API that allows prompts to be analyzed through an API endpoint and tested using Swagger UI.

---

## 2. Objectives

The main objectives of PromptShield are:

1. To detect prompt injection attempts.
2. To identify suspicious prompt patterns.
3. To combine machine learning and rule-based detection.
4. To calculate a risk score for each input prompt.
5. To classify prompts into ALLOW, REVIEW, or BLOCK decisions.
6. To provide an API for prompt analysis.
7. To evaluate the detection performance using standard machine learning metrics.

---

## 3. System Workflow

The PromptShield system follows the following workflow:

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
        ↓
API Response

The system first preprocesses the input prompt. It then analyzes the prompt using both rule-based detection and the trained machine learning model. The results are combined to calculate the final risk score and security decision.

---

## 4. Technologies Used

The project was implemented using the following technologies:

- Python
- pandas
- scikit-learn
- matplotlib
- joblib
- FastAPI
- Uvicorn
- Swagger UI

---

## 5. Model and Detection Approach

PromptShield uses a trained machine learning model to classify prompts into benign and injection-related categories.

In addition to machine learning, the system uses rule-based detection to identify known prompt injection patterns.

The final risk score combines the machine learning probability and the rule-based score.

The system then uses the calculated risk score to determine the security decision.

---

## 6. API Implementation

PromptShield provides a REST API using FastAPI.

The main endpoint used for prompt analysis is:

POST /analyze

The endpoint accepts a prompt as input and returns information including:

- Decision
- Risk level
- Risk score
- Machine learning probability
- Detected categories
- Normalized text
- Explanation

The API can be tested through the automatically generated Swagger UI.

---

## 7. Testing

The PromptShield API was tested using multiple types of prompts.

The testing included:

1. Normal technical questions
2. Instruction override attempts
3. System prompt extraction attempts
4. Role manipulation attempts
5. Context manipulation attempts
6. Suspicious mixed prompts

The tests demonstrated that normal prompts could be allowed, while prompts containing recognized injection patterns could receive elevated risk levels and either review or blocking decisions depending on the calculated risk score.

### Test Evidence

The following screenshots document representative PromptShield API test cases:

1. Normal DNS request — `01_normal_dns.png`
2. Direct prompt injection — `02_direct_injection.png`
3. Role manipulation — `03_role_manipulation.png`
4. Context manipulation — `04_context_manipulation.png`
5. System prompt extraction — `05_system_prompt_extraction.png`
6. Instruction override — `06_instruction_override.png`
7. Confusion matrix — `07_confusion_matrix.png`

---

## 8. Evaluation Results

The trained model was evaluated using a separate test dataset.

The obtained evaluation metrics were:

| Metric | Result |
|---|---:|
| Accuracy | 95.54% |
| Precision | 95.21% |
| Recall | 97.28% |
| F1 Score | 96.24% |

These results indicate the measured performance of the trained classifier on the evaluation dataset.

---

## 9. Confusion Matrix

The confusion matrix obtained during evaluation was:

| Actual / Predicted | Benign | Injection |
|---|---:|---:|
| Benign | 363 | 27 |
| Injection | 15 | 537 |

The confusion matrix was generated using the evaluation script and saved as:

`results/confusion_matrix.png`

---

## 10. Conclusion

PromptShield successfully implements a prompt injection detection and risk assessment workflow.

The system combines machine learning and rule-based analysis to evaluate prompts and generate security decisions. It also provides a FastAPI endpoint that can be tested through Swagger UI.

The evaluation produced an accuracy of 95.54%, precision of 95.21%, recall of 97.28%, and F1 score of 96.24% on the evaluated test dataset.

The project provides a foundation for further development of prompt security mechanisms for LLM-integrated applications.
