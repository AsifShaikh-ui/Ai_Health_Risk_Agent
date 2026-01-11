import joblib
import numpy as np
from engine.rules import rule_based_risk


model = joblib.load("training/model.pkl")
scaler = joblib.load("training/scaler.pkl")

def run_decision_engine(user_input):

    age = user_input["age"]
    duration = user_input["duration"]
    severity = user_input["severity"]
    symptoms = user_input["symptoms"]

    rule_risk = rule_based_risk(symptoms, age, duration, severity)

    if rule_risk == 2:
        return 2 , "High risk detected based on critical safety rules"
    
    feature_vector = np.array([
        age,
        duration,
        severity,
        symptoms["fever"],
        symptoms["cough"],
        symptoms["chest_pain"],
        symptoms["shortness_of_bredth"],
        symptoms["nausea"],
        symptoms["vomiting"],
        symptoms["diarrhea"],
        symptoms["dizziness"],
        symptoms["fatigue"],
        symptoms["diabetes"],
        symptoms["hypertension"],
        symptoms["asthma"],
    ]).reshape(1,-1)

    scaled_features = scaler.transform(feature_vector)

    ml_pred = model.predict(scaled_features)[0]
    ml_prob = model.predict_proba(scaled_features)[0]

    high_risk_prob = ml_prob[2]

    if high_risk_prob >= 0.60:
        return 2, "High risk indicated by strong model confidence"
    
    elif high_risk_prob >= 0.35:
        return 1, "Moderate risk due to uncertainity; Medical review advised"
    
    else:
        if ml_pred == 0:
            return 0, "Low risk based on symptoms patterns"
        elif ml_pred == 1:
            return 1, "Moderate risk based on symptoms patterns"
        else:
            return 2, "High risk based on symptoms patterns"