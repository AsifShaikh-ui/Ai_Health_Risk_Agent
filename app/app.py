import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from engine.decision_engine import run_decision_engine

st.set_page_config(page_title="AI Health Risk Triage Agent", layout="centered")

st.title("🩺 AI Early Health Risk Triage Agent")
st.write(
    "This tool screens symptoms and provides **risk-based guidance only**. "
    "It does **not** diagnose diseases or replace medical professionals."
)

st.divider()



age = st.number_input("Age", min_value=1, max_value=100, value=30)

duration = st.number_input(
    "Symptom duration (days)", min_value=0, max_value=14, value=1
)

severity = st.selectbox(
    "Symptom severity",
    options=[1, 2, 3],
    format_func=lambda x: {1: "Low", 2: "Medium", 3: "High"}[x]
)

st.subheader("Select symptoms present")

symptoms = {
    "fever": st.checkbox("Fever"),
    "cough": st.checkbox("Cough"),
    "chest_pain": st.checkbox("Chest pain"),
    "shortness_of_bredth": st.checkbox("Shortness of bredth"),
    "nausea": st.checkbox("Nausea"),
    "vomiting": st.checkbox("Vomiting"),
    "diarrhea": st.checkbox("Diarrhea"),
    "dizziness": st.checkbox("Dizziness"),
    "fatigue": st.checkbox("Fatigue"),
}

st.subheader("Existing medical conditions")

symptoms["diabetes"] = st.checkbox("Diabetes")
symptoms["hypertension"] = st.checkbox("Hypertension")
symptoms["asthma"] = st.checkbox("Asthma")

st.divider()



if st.button("Run Health Risk Assessment"):
    user_input = {
        "age": age,
        "duration": duration,
        "severity": severity,
        "symptoms": {k: int(v) for k, v in symptoms.items()},
    }

    risk, explanation = run_decision_engine(user_input)

    st.subheader("🧠 Assessment Result")

    if risk == 0:
        st.success("🟢 Low Risk")
    elif risk == 1:
        st.warning("🟠 Medium Risk")
    else:
        st.error("🔴 High Risk")

    st.write(explanation)

    st.divider()
    st.caption(
        "⚠️ Disclaimer: This tool provides screening-level guidance only. "
        "It does not provide medical diagnosis or treatment. "
        "Always consult a qualified healthcare professional for medical advice."
    )
