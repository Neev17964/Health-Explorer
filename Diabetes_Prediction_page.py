import streamlit as st
import numpy as np
import cloudpickle

# Load model and scaler
with open('trained_diabetes_model.sav', 'rb') as f:
    model = cloudpickle.load(f)
with open('standard_scaler_diabetes.sav', 'rb') as f:
    scaler = cloudpickle.load(f)

# Custom Alert Box Function (styled like info/success/error)
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

# Main Page
def show_diabetes_prediction_page():
    st.markdown("<h1 style='text-align: center;'>💉 Diabetes Predictor</h1>", unsafe_allow_html=True)
    st.write("##### We need some information to predict diabetes")

    col1, col2, col3 = st.columns(3)
    with col1:
        preg = st.number_input("Pregnancies (0–20)", min_value=0, max_value=20, step=1)
    with col2:
        glu = st.number_input("Glucose (0–300)", min_value=0, max_value=300)
    with col3:
        bp = st.number_input("Blood Pressure (0–200)", min_value=0, max_value=200)

    col4, col5, col6 = st.columns(3)
    with col4:
        skin = st.number_input("Skin Thickness (0–100)", min_value=0, max_value=100)
    with col5:
        insulin = st.number_input("Insulin (0–900)", min_value=0, max_value=900)
    with col6:
        bmi = st.number_input("BMI (0–70)", min_value=0.0, max_value=70.0, format="%.1f")

    col7, col8 = st.columns(2)
    with col7:
        age = st.number_input("Age (0–120)", min_value=0, max_value=120)
    with col8:
        dbf = st.selectbox(
            "Family History of Diabetes",
            [
                "No one in family has diabetes",
                "Distant relative has diabetes",
                "Close relative has diabetes"
            ]
        )
        dbf = {"No one in family has diabetes": 0,
               "Distant relative has diabetes": 0.3,
               "Close relative has diabetes": 0.8}[dbf]

    # Centered Predict Button
    _, btn_col2, _ = st.columns([6, 1, 6.3])
    with btn_col2:
        button = st.button("### PREDICT")

    if button:
        # Prepare input
        input_array = np.array([[preg, glu, bp, skin, insulin, bmi, dbf, age]]) 
        input_array = scaler.transform(input_array)  

        # Predict
        prediction = model.predict(input_array) 
        risk = prediction[0]

        # Clear other prediction states
        for key in ["diabetes_result", "lung_result", "heart_result"]:
            if key in st.session_state:
                del st.session_state[key]

        # Set result for chatbot
        st.session_state["diabetes_result"] = risk
        st.session_state["auto_reply_generated"] = False

        if risk == 0:
            custom_alert("🎉 Great news! You're currently <strong>not diabetic</strong>. Keep up the healthy lifestyle – stay active, eat clean, and get regular checkups to stay on top of your game! 💪\n🤖 If want ask the CareBot for health tips", "success")
        else:
            custom_alert("⚠️ According to the analysis, there's a <strong>high chance you may be diabetic</strong>. But don’t panic! Early detection is powerful – consider consulting a doctor, making some lifestyle tweaks, and keeping track of your sugar levels. You've got this. 💙\n🤖 Would recommend you to ask for precautions and suggestions from the CareBot", "error")
