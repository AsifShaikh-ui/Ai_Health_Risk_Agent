# AI Early Health Risk Triage Agent

## Project Overview
The **AI Early Health Risk Triage Agent** is a screening-level decision support system designed to help users understand the **risk level** of their health symptoms at an early stage.

The system classifies users into **Low, Medium, or High Risk** categories based on:
- User-reported symptoms
- Symptom duration
- Severity
- Age
- Existing health conditions

⚠️ This system **does NOT diagnose diseases** and **does NOT provide medical treatment**.  
It is intended only for **early awareness and guidance**.

---

## Problem Statement
Many individuals struggle to decide whether their symptoms require medical attention. This uncertainty often leads to:
- Delayed medical consultation
- Panic due to misinformation
- Over-reliance on unverified online sources

Existing tools are often either:
- Rigid rule-based systems, or
- Pure machine learning models that may miss critical edge cases

There is a need for a **safe, explainable, and conservative triage system**.

---

## Solution Approach
This project implements a **hybrid AI architecture** that combines:

1. **Rule-Based Safety Layer**
   - Detects critical symptom combinations
   - Overrides ML predictions in emergency scenarios
   - Ensures high-risk cases are never missed

2. **Machine Learning Model**
   - Logistic Regression (multiclass)
   - Trained on a synthetic, rule-driven dataset
   - Provides probabilistic risk estimation

3. **Decision Engine**
   - Combines rule-based output and ML probabilities
   - Applies conservative thresholds
   - Prevents unsafe downgrading of risk

---

## System Architecture
---

## Dataset
- Fully **synthetic dataset**
- No real patient data used
- Privacy-safe by design
- Labels generated using controlled triage logic (not random)

### Features include:
- Age
- Symptom duration (days)
- Severity (Low / Medium / High)
- Binary symptoms (fever, chest pain, breathlessness, etc.)
- Comorbidities (diabetes, hypertension, asthma)

---

## Machine Learning Model
- **Algorithm:** Logistic Regression (Multiclass)
- **Reason for selection:**
  - Explainable
  - Stable
  - Suitable for risk classification
- **Class imbalance handling:** `class_weight = balanced`

### Evaluation Focus
- Primary metric: **Recall for High-Risk cases**
- High-risk recall achieved ≈ **0.87**
- Some false positives are intentionally accepted

> In triage systems, missing a high-risk case is worse than raising a false alarm.

---

## Application Interface
- Built using **Streamlit**
- Structured input form for symptoms and conditions
- Outputs:
  - Risk Level (Low / Medium / High)
  - Explanation of decision
  - Clear medical disclaimer

---

## Ethics & Limitations
### Ethics
- No diagnosis or treatment recommendations
- Clear disclaimer included
- No real patient data used
- Screening-level guidance only

### Limitations
- Uses synthetic data
- Not clinically validated
- Intended for early awareness, not medical decision-making

---

## Future Scope
- User authentication and secure access
- Database-backed user history
- Clinical validation with experts
- Doctor-facing dashboards
- Gradual and responsible deployment with real-world data

---

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## Deployment
The application is deployed using **Streamlit Cloud**.

> App URL: *(Add your Streamlit link here)*

---

## Disclaimer
This project is developed for **educational and screening purposes only** as part of the  
**CSRBOX – IBM SkillsBuild Applied AI Internship**.

It is **not a medical device** and should not be used for diagnosis or treatment.

---
