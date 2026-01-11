def rule_based_risk(symptoms, age, duration, severity):

    if symptoms.get("chest_pain") and symptoms.get("shortnes_of_bredth"):
        return 2
    
    if symptoms.get("asthma") and symptoms.get("shortness_of_bredth"):
        return 2
    
    if symptoms.get("fever") and duration >=5 and severity ==3:
        return 2 
    
    if age >= 65 and duration >=3 and severity == 3:
        return 2
    
    return None