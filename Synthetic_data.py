import numpy as np 
import pandas as pd

np.random.seed(42)
rows = 1500
data = []

for _ in range(rows):

    age = np.random.randint(1,90)
    duration = np.random.randint(0,14)
    severity = np.random.choice([1,2,3],p=[0.5,0.3,0.2])

    symptoms = {
        "fever" : np.random.binomial(1, 0.4),
        "cough" : np.random.binomial(1, 0.3),
        "chest_pain" : np.random.binomial(1, 0.15),
        "shortness_of_bredth" : np.random.binomial(1, 0.15),
        "nausea" : np.random.binomial(1, 0.15),
        "vomiting" : np.random.binomial(1, 0.1),
        "diarrhea" : np.random.binomial(1, 0.1),
        "dizziness" : np.random.binomial(1, 0.2),
        "fatigue" : np.random.binomial(1, 0.35),
        "diabetes" : np.random.binomial(1, 0.15),
        "hypertension" : np.random.binomial(1, 0.15),
        "asthma" : np.random.binomial(1, 0.1)
    }

    risk = 0

    if(
        (symptoms["chest_pain"] and symptoms["shortness_of_bredth"]) or 
        (age >= 60 and severity == 3 and duration >= 3) or 
        (symptoms["shortness_of_bredth"] and symptoms["asthma"]) or 
        (symptoms["fever"] and duration >=5 and severity == 3)
    ):
        risk = 2
    
    else:
        medium_score = 0

        if severity == 2:
            medium_score +=1
        if duration >=3:
            medium_score +=1
        if symptoms["vomiting"]:
            medium_score +=1
        if symptoms["diarrhea"]:
            medium_score +=1
        if age >=60:
            medium_score +=1
        if symptoms["fatigue"] and duration >= 3:
            medium_score +=1
        
        if medium_score >=3:
            risk = 1

    if risk == 0 and severity ==2 and duration >=2 and np.random.rand() < 0.25:
        risk = 1

    if risk ==1 and severity ==3 and duration >= 3:
        risk = 2
    
    row = {
        "age" : age,
        "Symptom_duration_days" : duration,
        "severity" : severity,**symptoms,
        "risk_level" : risk
    }

    data.append(row)

df = pd.DataFrame(data)
df.head()

print(df["risk_level"].value_counts(normalize=True))

df.to_csv("synthetic_health_triage_data.csv",index=False)