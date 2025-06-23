import streamlit as st
import numpy as np
import cloudpickle

# Load model and scaler
with open('trained_heart_model.sav', 'rb') as f:
    model = cloudpickle.load(f)
with open('standard_scaler_heart.sav', 'rb') as f:
    scaler = cloudpickle.load(f)

# Custom Alert Box Function
def custom_alert(message, alert_type="info"):
    colors = {
        "info": {"bg": "#007bff", "border": "#0056b3", "icon": "💡"},
        "success": {"bg": "#28a745", "border": "#1e7e34", "icon": "✅"},
        "error": {"bg": "#dc3545", "border": "#b21f2d", "icon": "🚨"}
    }
    color = colors.get(alert_type, colors["info"])

    st.markdown(f"""
        <div style='
            background-color: {color["bg"]};
            border-left: 6px solid {color["border"]};
            color: white;
            padding: 1rem;
            border-radius: 10px;
            font-weight: 500;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            margin-top: 1rem;
            margin-bottom: 1rem;
        '>
            {color["icon"]} <span style="font-weight: 600;">{message}</span>
        </div>
    """, unsafe_allow_html=True)

def show_heart_attack_prediction_page():
    st.markdown("<h1 style='text-align: center;'>❤️ Heart Attack Predictor</h1>", unsafe_allow_html=True)
    st.write("##### We need some information to predict heart attack")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (18–120)", min_value=18, max_value=120, step=1)
    with col2:
        gender = st.selectbox("Gender", options=["Male", "Female"])
        gender = 1 if gender == 'Male' else 0
    with col3:
        bp = st.number_input("Resting Blood Pressure (80–200)", min_value=80, max_value=200, step=1)

    col4, col5, col6 = st.columns(3)
    with col4:
        cholesterol = st.number_input("Serum Cholesterol (100–600 mg/dL)", min_value=100, max_value=600, step=1)
    with col5:
        blood_sugar = st.selectbox("Fasting Blood Sugar", options=["> 120 mg/dl", "< 120 mg/dl"])
        blood_sugar = 1 if blood_sugar == '> 120 mg/dl' else 0
    with col6:
        max_heart_rate = st.number_input("Max Heart Rate Achieved (60–220)", min_value=60, max_value=220, step=1)

    col7, col8, col9 = st.columns(3)
    with col7:
        angina = st.selectbox("Exercise-Induced Angina", options=["Yes", "No"])
        angina = 1 if angina == 'Yes' else 0
    with col8:
        ST = st.number_input("ST Depression (Oldpeak) (0.0–6.5)", min_value=0.0, max_value=6.5, step=0.1)
    with col9:
        vessels = st.number_input("Major Vessels Colored (0–3)", min_value=0, max_value=3, step=1)

    col10, col11, col12 = st.columns(3)
    with col10:
        chest_pain = st.selectbox("Chest Pain Type", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
        chest_pain = ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"].index(chest_pain)
    with col11:
        ECG = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        ECG = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(ECG)
    with col12:
        slope = st.selectbox("Slope of ST Segment", ["Upsloping", "Flat", "Downsloping"])
        slope = ["Upsloping", "Flat", "Downsloping"].index(slope)

    col13a, col13, col13b = st.columns([1, 6, 1])
    with col13:
        thalassemia = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])
        thalassemia = ["Normal", "Fixed Defect", "Reversible Defect"].index(thalassemia) + 1

    col14a, col14, col14b = st.columns([7, 2, 7])
    with col14:
        button = st.button("PREDICT")

    if button:
        # Create input array
        input_array = np.array([[age, gender, chest_pain, bp, cholesterol, blood_sugar,
                            ECG, max_heart_rate, angina, ST, slope, vessels, thalassemia]])
        input_scaled = scaler.transform(input_array)
        
        # Get probability prediction instead of class
        risk_probability = model.predict_proba(input_scaled)[0][1]  # Probability of class 1 (high risk)
        
        # Apply custom threshold (0.7 instead of default 0.5)
        risk = 1 if risk_probability >= 0.5 else 0
        
        # Clear previous flags
        for key in ["diabetes_result", "lung_result", "heart_result"]:
            if key in st.session_state:
                del st.session_state[key]
        
        st.session_state["heart_result"] = risk
        st.session_state["auto_reply_generated"] = False
        
        if risk == 0:
            custom_alert("You have a <strong>low risk</strong> of heart disease. Maintain a healthy lifestyle! ❤️\n🤖 If want ask the CareBot for health tips", "success")
        else:
            custom_alert("<strong>High risk detected</strong>. Please consult a cardiologist immediately. 💔\n🤖 Would recommend you to ask for precautions and suggestions from the CareBot", "error")