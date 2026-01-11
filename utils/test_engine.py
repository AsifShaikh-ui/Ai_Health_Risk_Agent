from engine.decision_engine import run_decision_engine

# -------- TEST CASE 1: CLEAR HIGH RISK (RULE-BASED) --------
user_1 = {
    "age": 70,
    "duration": 4,
    "severity": 3,
    "symptoms": {
        "fever": 1,
        "cough": 0,
        "chest_pain": 1,
        "shortness_of_breath": 1,
        "nausea": 0,
        "vomiting": 0,
        "diarrhea": 0,
        "dizziness": 1,
        "fatigue": 1,
        "diabetes": 1,
        "hypertension": 0,
        "asthma": 0,
    }
}

print("Test 1:", run_decision_engine(user_1))


# -------- TEST CASE 2: MEDIUM RISK --------
user_2 = {
    "age": 45,
    "duration": 3,
    "severity": 2,
    "symptoms": {
        "fever": 1,
        "cough": 1,
        "chest_pain": 0,
        "shortness_of_bredth": 0,
        "nausea": 1,
        "vomiting": 0,
        "diarrhea": 0,
        "dizziness": 0,
        "fatigue": 1,
        "diabetes": 0,
        "hypertension": 0,
        "asthma": 0,
    }
}

print("Test 2:", run_decision_engine(user_2))


# -------- TEST CASE 3: LOW RISK --------
user_3 = {
    "age": 25,
    "duration": 1,
    "severity": 1,
    "symptoms": {
        "fever": 0,
        "cough": 1,
        "chest_pain": 0,
        "shortness_of_bredth": 0,
        "nausea": 0,
        "vomiting": 0,
        "diarrhea": 0,
        "dizziness": 0,
        "fatigue": 0,
        "diabetes": 0,
        "hypertension": 0,
        "asthma": 0,
    }
}

print("Test 3:", run_decision_engine(user_3))
