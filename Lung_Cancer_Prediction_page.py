import streamlit as st
import numpy as np
import cloudpickle

# Load model and scaler
with open('trained_lung_cancer_model.sav', 'rb') as f:
    model = cloudpickle.load(f)
with open('standard_scaler_cancer.sav', 'rb') as f:
    scaler = cloudpickle.load(f)

# Alert box helper
def custom_alert(message, alert_type="info"):
    colors = {
        "info": {"bg": "#007bff", "border": "#0056b3", "icon": "💡"},
        "success": {"bg": "#28a745", "border": "#1e7e34", "icon": "✅"},
        "error": {"bg": "#dc3545", "border": "#b21f2d", "icon": "🚨"},
        "warning": {"bg": "#ffc107", "border": "#d39e00", "icon": "⚠️"}
    }
    color = colors.get(alert_type, colors["info"])

    st.markdown(f"""
        <div style='
            background-color: {color["bg"]};
            border-left: 6px solid {color["border"]};
            color: black;
            padding: 1rem;
            border-radius: 10px;
            font-weight: 500;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            margin-top: 1rem;
            margin-bottom: 1rem;
        '>
            {color["icon"]} {message}
        </div>
    """, unsafe_allow_html=True)

severity_levels = {
    "None": 1, "Very Low": 2, "Low": 3, "Mild": 4, "Moderate": 5,
    "Medium-High": 6, "High": 7, "Very High": 8, "Severe": 9, "Extremely Severe": 10
}

def get_level_input(label):
    return severity_levels[st.selectbox(label, list(severity_levels.keys()))]

def show_lung_cancer_prediction_page():
    st.markdown("<h1 style='text-align: center;'>🫁 Lung Cancer Predictor</h1>", unsafe_allow_html=True)
    st.write("##### Please provide the following details to predict lung cancer risk.")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (0-120)", min_value=0, max_value=120)
    with col2:
        gender = st.selectbox("Gender", ['Male', 'Female'])
        gender = 1 if gender == 'Male' else 0
    with col3:
        air_pollution = get_level_input("Air Pollution Exposure")

    col4, col5, col6 = st.columns(3)
    with col4: alcohol_use = get_level_input("Alcohol Use")
    with col5: dust_allergy = get_level_input("Dust Allergy")
    with col6: occ_hazards = get_level_input("Occupational Hazards")

    col7, col8, col9 = st.columns(3)
    with col7: genetic_risk = get_level_input("Genetic Risk")
    with col8: lung_disease = get_level_input("Chronic Lung Disease")
    with col9: diet = get_level_input("Balanced Diet")

    col10, col11, col12 = st.columns(3)
    with col10: obesity = get_level_input("Obesity")
    with col11: smoking = get_level_input("Smoking")
    with col12: passive_smoke = get_level_input("Passive Smoker")

    col13, col14, col15 = st.columns(3)
    with col13: chest_pain = get_level_input("Chest Pain")
    with col14: coughing_blood = get_level_input("Coughing of Blood")
    with col15: fatigue = get_level_input("Fatigue")

    col16, col17, col18 = st.columns(3)
    with col16: weight_loss = get_level_input("Weight Loss")
    with col17: breath_shortness = get_level_input("Shortness of Breath")
    with col18: wheezing = get_level_input("Wheezing")

    col19, col20, col21 = st.columns(3)
    with col19: swallow_diff = get_level_input("Swallowing Difficulty")
    with col20: clubbing = get_level_input("Clubbing of Finger Nails")
    with col21: frequent_cold = get_level_input("Frequent Cold")

    col22, col23 = st.columns(2)
    with col22: dry_cough = get_level_input("Dry Cough")
    with col23: snoring = get_level_input("Snoring")

    _, btn_col2, _ = st.columns([6, 1, 6.3])
    with btn_col2:
        predict = st.button("### PREDICT", key="predict_button")

    if predict:
        input_data = np.array([[age, gender, air_pollution, alcohol_use, dust_allergy,
                                occ_hazards, genetic_risk, lung_disease, diet, obesity,
                                smoking, passive_smoke, chest_pain, coughing_blood, fatigue,
                                weight_loss, breath_shortness, wheezing, swallow_diff, clubbing,
                                frequent_cold, dry_cough, snoring]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        risk = prediction[0]

        for key in ["heart_result", "diabetes_result", "lung_result"]:
            if key in st.session_state:
                del st.session_state[key]

        st.session_state["lung_result"] = risk
        st.session_state["auto_reply_generated"] = False

        if risk == 1:
            custom_alert("🎉 Great news! You're currently <b>not at high risk</b> for lung cancer. Keep maintaining your healthy lifestyle, and stay proactive with routine health checkups! 💪\n🤖 If want ask the CareBot for health tips", "success")
        elif risk == 2:
            custom_alert("⚠️ <b>Moderate Risk</b> detected. It’s a good idea to speak to a medical professional and make healthy changes like quitting smoking, eating clean, and exercising regularly. 🧠\n🤖 Would recommend you to ask for precautions and suggestions from the CareBot", "warning")
        elif risk == 0:
            custom_alert("🚨 <b>High Risk</b> of lung cancer detected. Please consult a healthcare provider for further screening and support. Early action makes all the difference. 🙏\n🤖 Would recommend you to ask for precautions and suggestions from the CareBot", "error")
